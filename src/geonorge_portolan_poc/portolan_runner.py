"""Steg 7: kjor portolan-cli som subprocess.

Rekkefolgen per collection (init -> add -> check --fix -> add) er ikke den
"opplagte" en-linje-kommandoen fra planen, men er empirisk fremforhandlet (se
REPORT.md): portolan-cli 0.8.0 sin `add` beregner GeoParquet-avledede
STAC-felt (feature_count, geometry_type) uten a registrere selve
GeoParquet-filen som asset; `check --fix` genererer sa GeoParquet + thumbnail
pa disk som "orphans"; en andre `add`-kjoring plukker dem opp og registrerer
dem. Uten det andre add-kallet mangler PMTiles/tegneregel-relevante
collections en thumbnail-asset og feiler `check --strict`.

En femte, empirisk pavist kvirk: nar `<name>.gpkg` og den avledede
`<name>.parquet` har SAMME filnavnstamme, "vinner" `add` sin
asset-nokkel-kollisjon inkonsekvent -- noen ganger blir parquet registrert
som collection-ens data-asset (riktig), andre ganger forblir gpkg registrert
og parquet forblir usporet, uavhengig av --force/--merge-strategy. Utfallet
korrelerer ikke med datastorrelse, geometri-type eller hvilken pipeline-kjoring
som prosesserte datasettet -- det ser ut til a avhenge av
filsystem-enumereringsrekkefolge internt i portolan-cli 0.8.0, ikke noe vi kan
styre via CLI-flagg. Den palitelige losningen (verifisert empirisk, se
REPORT.md) er a fjerne den na-redundante `.gpkg`-filen for kollisjonen i det
hele tatt kan oppsta, og kjore `add --force` pa nytt: se
`_promote_parquet_if_orphaned` under.
"""

from __future__ import annotations

import json
import logging
import subprocess
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class CommandResult:
    args: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def _run(args: list[str], *, cwd: Path, timeout: int = 900) -> CommandResult:
    logger.info("$ %s (cwd=%s)", " ".join(args), cwd)
    try:
        proc = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        return CommandResult(args, 124, exc.stdout or "", (exc.stderr or "") + "\nTIMED OUT")
    if proc.returncode != 0:
        logger.warning("Command failed (%d): %s\n%s", proc.returncode, " ".join(args), proc.stderr[-2000:])
    return CommandResult(args, proc.returncode, proc.stdout, proc.stderr)


def init_catalog(
    catalog_dir: Path,
    *,
    catalog_id: str,
    title: str,
    description: str,
    license_spdx: str,
    license_url: str | None,
) -> CommandResult:
    catalog_dir.mkdir(parents=True, exist_ok=True)
    args = [
        "portolan",
        "init",
        "--auto",
        "--id",
        catalog_id,
        "--title",
        title,
        "--description",
        description,
        "--license",
        license_spdx,
    ]
    if license_spdx == "other" and license_url:
        args += ["--license-url", license_url]
    return _run(args, cwd=catalog_dir)


def _promote_parquet_if_orphaned(catalog_dir: Path, collection_name: str) -> CommandResult | None:
    """Work around the same-stem gpkg/parquet asset-collision quirk (see module docstring).

    If `<collection_name>.gpkg` is still the registered "data" asset even
    though a same-named `<collection_name>.parquet` now exists on disk, the
    gpkg is redundant (portolan-cli already deleted the true original raw
    download after the ogr2ogr conversion that produced it -- see
    convert_gpkg.py) and is only still there causing the collision. Deleting
    it and re-adding forces `add` to register the parquet, since there's no
    longer a competing candidate for the asset key.

    Returns the CommandResult of the corrective `add --force`, or None if no
    correction was needed.
    """
    collection_dir = catalog_dir / collection_name
    gpkg_path = collection_dir / f"{collection_name}.gpkg"
    parquet_path = collection_dir / f"{collection_name}.parquet"
    collection_json = collection_dir / "collection.json"
    if not (gpkg_path.exists() and parquet_path.exists() and collection_json.exists()):
        return None

    try:
        data = json.loads(collection_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        logger.exception("Could not read %s to check for the gpkg/parquet asset collision", collection_json)
        return None

    primary_href = data.get("assets", {}).get(collection_name, {}).get("href", "")
    if not primary_href.endswith(".gpkg"):
        return None  # parquet is already registered; nothing to fix

    logger.info(
        "%s: registered data asset is still %s despite %s existing; removing the redundant "
        "gpkg and re-adding so the parquet gets registered instead",
        collection_name,
        primary_href,
        parquet_path.name,
    )
    gpkg_path.unlink()
    return _run(["portolan", "add", "--force", collection_name], cwd=catalog_dir)


def add_collection(catalog_dir: Path, collection_name: str, *, workers: int = 4) -> list[CommandResult]:
    """Register a collection, converting/registering derived assets.

    See module docstring for why this is four (sometimes five) steps, not one.
    """
    results = []

    r = _run(["portolan", "add", "--force", "--thumbnails", collection_name], cwd=catalog_dir)
    results.append(r)
    if not r.ok:
        return results

    r = _run(
        ["portolan", "check", collection_name, "--fix", "--workers", str(workers)],
        cwd=catalog_dir,
    )
    results.append(r)

    r = _run(["portolan", "add", collection_name], cwd=catalog_dir)
    results.append(r)

    correction = _promote_parquet_if_orphaned(catalog_dir, collection_name)
    if correction is not None:
        results.append(correction)

    return results


def generate_readme(catalog_dir: Path) -> CommandResult:
    return _run(["portolan", "readme"], cwd=catalog_dir)


def final_check_fix(catalog_dir: Path, *, workers: int = 4) -> CommandResult:
    args = ["portolan", "check", ".", "--fix", "--workers", str(workers)]
    return _run(args, cwd=catalog_dir, timeout=1800)


def final_add(catalog_dir: Path, *, workers: int = 4) -> CommandResult:
    """Register anything `final_check_fix` just converted but left unregistered.

    On a resumed run, a collection skipped by `run_pipeline` (already
    processed in an earlier invocation) never goes through `add_collection`'s
    own add->check--fix->add sequence in *this* run. If `final_check_fix`
    (running catalog-wide) is what ends up converting that collection's
    gpkg to parquet, there is otherwise no later `add` call left to register
    it -- run one here, once, for the whole catalog.
    """
    return _run(["portolan", "add", ".", "--workers", str(workers)], cwd=catalog_dir, timeout=1800)


def final_check_plain(catalog_dir: Path) -> CommandResult:
    """The authoritative conformance signal: does the catalog pass the spec at all."""
    return _run(["portolan", "check", "."], cwd=catalog_dir, timeout=1800)


def final_check_strict(catalog_dir: Path) -> CommandResult:
    """Stricter pass that also fails on warnings (including known CLI-alpha
    advisories about orphaned auto-generated files -- see REPORT.md)."""
    return _run(["portolan", "check", ".", "--strict"], cwd=catalog_dir, timeout=1800)
