"""Normaliser rådata til GeoPackage med ogr2ogr for enhetlig innmating i portolan.

Vi fant empirisk (se REPORT.md) at portolan-cli 0.8.0 har hull for FileGDB
(".gdb" mangler scan_category="geo_asset", sa konvertering til GeoParquet og
tilhorende thumbnail-generering aldri kjorer for FGDB-collections) og at
GeoNorge sine GeoJSON-eksporter har en UTF-8 BOM som knekker portolan sin
JSON-parser. Å normalisere alt til GeoPackage via GDAL/OGR forst, og bare gi
portolan GPKG-filer, unngar begge problemene med ett enkelt steg.
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

# Formats (as tagged by the level-1 feed's AtomFeed<FORMAT>.xml naming, see
# feed.py) that GDAL/OGR can read directly and that we've validated convert
# cleanly to GeoPackage.
CONVERTIBLE_FORMATS = {"GEOJSON", "GPKG", "GEOPACKAGE", "SHAPE", "FGDB"}


def _find_source(raw_dir: Path, fmt: str) -> Path | None:
    fmt = fmt.upper()
    if fmt == "FGDB":
        candidates = list(raw_dir.glob("*.gdb"))
    elif fmt in ("GPKG", "GEOPACKAGE"):
        candidates = list(raw_dir.glob("*.gpkg"))
    elif fmt == "SHAPE":
        candidates = list(raw_dir.glob("*.shp"))
    elif fmt == "GEOJSON":
        candidates = list(raw_dir.glob("*.geojson")) + list(raw_dir.glob("*.json"))
    else:
        candidates = []
    return candidates[0] if candidates else None


def convert_to_geopackage(raw_dir: Path, fmt: str, collection_dir: Path, *, layer_name: str) -> Path | None:
    """Convert whatever was downloaded into ``raw_dir`` to a single .gpkg.

    Returns the path to the resulting .gpkg inside ``collection_dir``, or None
    if no convertible source file was found or ogr2ogr failed.
    """
    source = _find_source(raw_dir, fmt)
    if source is None:
        logger.warning("No %s source file found in %s", fmt, raw_dir)
        return None

    collection_dir.mkdir(parents=True, exist_ok=True)
    dest = collection_dir / f"{layer_name}.gpkg"

    if source == dest:
        return source

    try:
        result = subprocess.run(
            [
                "ogr2ogr",
                "-f",
                "GPKG",
                "-nlt",
                "PROMOTE_TO_MULTI",
                "-skipfailures",
                str(dest),
                str(source),
            ],
            capture_output=True,
            text=True,
            timeout=900,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        logger.error("ogr2ogr failed for %s: %s", source, exc)
        return None

    if result.returncode != 0 or not dest.exists():
        logger.error("ogr2ogr conversion failed for %s: %s", source, result.stderr.strip())
        return None

    # The raw source is no longer needed once it's safely inside the .gpkg;
    # drop it (and any sidecars) to keep the collection directory to just the
    # cloud-native asset portolan should track.
    if source.is_dir():
        shutil.rmtree(source, ignore_errors=True)
    else:
        for sidecar in source.parent.glob(source.stem + ".*"):
            sidecar.unlink(missing_ok=True)

    return dest
