"""Steg 7: kjor portolan-cli som subprocess.

Rekkefolgen per collection (init -> add -> check --fix -> add) er ikke den
"opplagte" en-linje-kommandoen fra planen, men er empirisk fremforhandlet (se
REPORT.md): portolan-cli 0.8.0 sin `add` beregner GeoParquet-avledede
STAC-felt (feature_count, geometry_type) uten a registrere selve
GeoParquet-filen som asset; `check --fix` genererer sa GeoParquet + thumbnail
pa disk som "orphans"; en andre `add`-kjoring plukker dem opp og registrerer
dem. Uten det andre add-kallet mangler PMTiles/tegneregel-relevante
collections en thumbnail-asset og feiler `check --strict`.
"""

from __future__ import annotations

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


def add_collection(catalog_dir: Path, collection_name: str, *, workers: int = 4) -> list[CommandResult]:
    """Register a collection, converting/registering derived assets.

    See module docstring for why this is four steps, not one.
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

    return results


def generate_readme(catalog_dir: Path) -> CommandResult:
    return _run(["portolan", "readme"], cwd=catalog_dir)


def final_check_fix(catalog_dir: Path, *, workers: int = 4) -> CommandResult:
    args = ["portolan", "check", ".", "--fix", "--workers", str(workers)]
    return _run(args, cwd=catalog_dir, timeout=1800)


def final_check_plain(catalog_dir: Path) -> CommandResult:
    """The authoritative conformance signal: does the catalog pass the spec at all."""
    return _run(["portolan", "check", "."], cwd=catalog_dir, timeout=1800)


def final_check_strict(catalog_dir: Path) -> CommandResult:
    """Stricter pass that also fails on warnings (including known CLI-alpha
    advisories about orphaned auto-generated files -- see REPORT.md)."""
    return _run(["portolan", "check", ".", "--strict"], cwd=catalog_dir, timeout=1800)
