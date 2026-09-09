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

PMTiles-generering (`add --pmtiles`) er avhengig av det samme kvirket: `add`
skriver bare et `*.pmtiles`-asset for en collection sin GeoParquet-fil hvis
GeoParquet-filen allerede er REGISTRERT som asset i collection.json (bekreftet
empirisk: `--pmtiles` pa et `add`-kall der bare `.gpkg` er registrert er en
no-op). Sa lenge gpkg/parquet-kollisjonen over ikke er lost, forblir det
registrerte asset-et `.gpkg`, og `--pmtiles` gjor ingenting. Derfor ma
`--pmtiles` ligge pa `_promote_parquet_if_orphaned` sitt korrigerende
`add --force`-kall (garantert a kjore etter at parquet er det eneste
gjenvaerende kandidat-asset-et), ikke bare pa de tidligere add-kallene.
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


def configure_pmtiles_max_zoom(catalog_dir: Path, max_zoom: int | None) -> CommandResult | None:
    """Set catalog-wide `pmtiles.max_zoom`, once, so every later `add --pmtiles`
    call inherits the cap without needing a per-collection config write.

    Returns None (no-op) if `max_zoom` is None -- tippecanoe auto-detects instead.
    """
    if max_zoom is None:
        return None
    return _run(["portolan", "config", "set", "pmtiles.max_zoom", str(max_zoom)], cwd=catalog_dir)


def _promote_parquet_if_orphaned(
    catalog_dir: Path, collection_name: str, *, pmtiles: bool = False
) -> CommandResult | None:
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
    args = ["portolan", "add", "--force"]
    if pmtiles:
        args.append("--pmtiles")
    args.append(collection_name)
    return _run(args, cwd=catalog_dir)


def add_collection(
    catalog_dir: Path, collection_name: str, *, workers: int = 4, pmtiles: bool = False
) -> list[CommandResult]:
    """Register a collection, converting/registering derived assets.

    See module docstring for why this is four (sometimes five) steps, not one, and
    why `--pmtiles` only actually takes effect once the corrective step runs.
    """
    results = []

    add_args = ["portolan", "add", "--force", "--thumbnails"]
    if pmtiles:
        add_args.append("--pmtiles")
    r = _run([*add_args, collection_name], cwd=catalog_dir)
    results.append(r)
    if not r.ok:
        return results

    r = _run(
        ["portolan", "check", collection_name, "--fix", "--workers", str(workers)],
        cwd=catalog_dir,
    )
    results.append(r)

    add_args = ["portolan", "add"]
    if pmtiles:
        add_args.append("--pmtiles")
    r = _run([*add_args, collection_name], cwd=catalog_dir)
    results.append(r)

    correction = _promote_parquet_if_orphaned(catalog_dir, collection_name, pmtiles=pmtiles)
    if correction is not None:
        results.append(correction)

    return results


def generate_readme(catalog_dir: Path) -> CommandResult:
    return _run(["portolan", "readme"], cwd=catalog_dir)


def final_check_fix(catalog_dir: Path, *, workers: int = 4) -> CommandResult:
    args = ["portolan", "check", ".", "--fix", "--workers", str(workers)]
    return _run(args, cwd=catalog_dir, timeout=1800)


def final_add(catalog_dir: Path, *, workers: int = 4, pmtiles: bool = False, force: bool = False) -> CommandResult:
    """Register anything `final_check_fix` just converted but left unregistered.

    On a resumed run, a collection skipped by `run_pipeline` (already
    processed in an earlier invocation) never goes through `add_collection`'s
    own add->check--fix->add sequence in *this* run. If `final_check_fix`
    (running catalog-wide) is what ends up converting that collection's
    gpkg to parquet, there is otherwise no later `add` call left to register
    it -- run one here, once, for the whole catalog. Passing `--pmtiles` here
    too means a resumed run still gets PMTiles for collections that were
    skipped this run (see `_promote_parquet_if_orphaned`, run catalog-wide
    right after this in `pipeline.py`, for where it usually actually lands).

    `add`'s own change detection does not re-scan a "documentation" asset
    (README.md) just because its content changed on disk -- confirmed
    empirically: a plain `add`/`add <collection>` reports README.md's
    companion file as already tracked and leaves its registered checksum
    untouched even after `portolan readme` rewrote it, so `check` then fails
    PTL-DAT-001/002 (declared checksum/size vs actual bytes). Only
    `--force` (all files, ignoring change detection) re-registers it. Pass
    `force=True` for the pass that runs right after `generate_readme`; the
    earlier catalog-wide pass (picking up `final_check_fix`'s conversions)
    should stay unforced so it doesn't needlessly re-hash every asset in the
    catalog on every run.
    """
    args = ["portolan", "add", "."]
    if pmtiles:
        args.append("--pmtiles")
    if force:
        args.append("--force")
    args += ["--workers", str(workers)]
    return _run(args, cwd=catalog_dir, timeout=1800)


def final_check_plain(catalog_dir: Path) -> CommandResult:
    """The authoritative conformance signal: does the catalog pass the spec at all."""
    return _run(["portolan", "check", "."], cwd=catalog_dir, timeout=1800)


def final_check_strict(catalog_dir: Path) -> CommandResult:
    """Stricter pass that also fails on warnings (including known CLI-alpha
    advisories about orphaned auto-generated files -- see REPORT.md)."""
    return _run(["portolan", "check", ".", "--strict"], cwd=catalog_dir, timeout=1800)
