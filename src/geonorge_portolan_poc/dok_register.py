"""Filter: begrens utvalget til datasett i Geonorges DOK-statusregister (CSV).

The register CSV (geodatalov-statusregister.csv) lists Det offentlige
kartgrunnlaget's nationally significant datasets. Its "Vis i kartkatalogen"
column links to https://kartkatalog.geonorge.no/metadata/uuid/<uuid> -- the
same metadata UUID embedded in the tjenestefeed's per-entry CSW
``describedby`` link (``...GetRecordById...&id=<uuid>``). Matching on that
UUID is simpler and more reliable than matching on title/name, which differ
in formatting between the two sources.
"""

from __future__ import annotations

import csv
import io
import logging
import re
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.IGNORECASE)


def fetch_register(
    url: str,
    cache_path: Path,
    *,
    force_refresh: bool = False,
    session: requests.Session | None = None,
) -> bytes:
    """Download (or reuse cached) geodatalov-statusregister.csv."""
    if cache_path.exists() and not force_refresh:
        logger.info("Using cached DOK register: %s", cache_path)
        return cache_path.read_bytes()

    sess = session or requests.Session()
    logger.info("Fetching DOK register from %s", url)
    resp = sess.get(url, timeout=60)
    resp.raise_for_status()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(resp.content)
    return resp.content


def parse_register_uuids(csv_bytes: bytes) -> set[str]:
    """Extract the metadata UUID from each row's "Vis i kartkatalogen" link.

    Reads the last column of every row rather than relying on a fixed header
    name/index, since that column holds a kartkatalog.geonorge.no/metadata/uuid/
    URL wherever the register format may have shifted other columns around.
    """
    text = csv_bytes.decode("utf-8-sig")
    reader = csv.reader(io.StringIO(text), delimiter=";")
    header = next(reader, None)
    if header is None:
        return set()

    uuids: set[str] = set()
    for row in reader:
        if not row:
            continue
        match = UUID_RE.search(row[-1])
        if match:
            uuids.add(match.group(0).lower())
    return uuids


def extract_uuid(csw_metadata_url: str | None) -> str | None:
    """Pull the metadata UUID out of a tjenestefeed entry's CSW describedby link."""
    if not csw_metadata_url:
        return None
    match = UUID_RE.search(csw_metadata_url)
    return match.group(0).lower() if match else None
