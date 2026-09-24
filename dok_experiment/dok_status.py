#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""
dok_status.py

For DOK (Det offentlige kartgrunnlaget) datasets ONLY -- i.e. datasets listed
in Geonorge's geodatalov-statusregister.csv, matched into the Tjenestefeed by
metadata UUID (same approach as geonorge_portolan_poc.dok_register):

  1. Tally status: how many DOK datasets have at least one download format we
     support (GEOJSON/GPKG/GEOPACKAGE/SHAPE/FGDB), and format counts across
     all DOK datasets (and across the ones with NO supported format).
  2. Find the downloadable size of EVERY DOK dataset (regardless of whether
     it has a supported format), by picking its best available format
     (preferring a supported one when present), fetching that format's
     per-dataset atom feed, and doing a HEAD request per file to read
     Content-Length (no data is actually downloaded).

Self-contained (does not import geonorge_portolan_poc) so it can be run and
iterated on independently with `uv run`.

Usage:
  uv run dok_experiment/dok_status.py
  uv run dok_experiment/dok_status.py --skip-sizes
  uv run dok_experiment/dok_status.py --limit 20
  uv run dok_experiment/dok_status.py --force-refresh

Output:
  dok_experiment/cache/*.xml, *.csv  -- cached upstream responses
  dok_experiment/dok_status.csv      -- one row per DOK dataset with status + size
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import io
import logging
import re
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import httpx

REGISTER_URL = "https://register.geonorge.no/api/geodatalov-statusregister.csv"
FEED_URL = "https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml"
CACHE_DIR = Path(__file__).parent / "cache"
OUTPUT_CSV = Path(__file__).parent / "dok_status.csv"
LOG_FILE = Path(__file__).parent / "dok_status.log"

log = logging.getLogger("dok_status")


def setup_logging(log_path: Path) -> None:
    log.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    log.addHandler(console)

    log_path.parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    file_handler.setFormatter(fmt)
    log.addHandler(file_handler)

NS = {"a": "http://www.w3.org/2005/Atom"}
UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.IGNORECASE)
FORMAT_RE = re.compile(r"AtomFeed([A-Za-z0-9]+)\.xml", re.IGNORECASE)
# Titles repeat the same dataset once per format, e.g. "... 2024 FGDB-format" /
# "... 2024 GML-format" -- strip the suffix so datasets display with one
# clean title regardless of which format entry we happened to see first.
TITLE_FORMAT_SUFFIX_RE = re.compile(r"\s*[-–]?\s*[A-Za-z0-9]+[- ]format\s*$", re.IGNORECASE)

SUPPORTED_FORMATS = {"GEOJSON", "GPKG", "GEOPACKAGE", "SHAPE", "FGDB", "GML"}
# preference order used when picking which format to measure the size of
FORMAT_PREFERENCE = ["GPKG", "GEOPACKAGE", "GEOJSON", "FGDB", "SHAPE", "GML"]

CSV_FIELDS = [
    "dataset_id", "title", "formats_available", "has_supported_format",
    "sized_format", "file_count", "size_bytes", "size_mb", "errors",
]


@dataclass
class DatasetFormatEntry:
    dataset_id: str
    title: str
    csw_uuid: str | None
    format: str
    feed_url: str


@dataclass
class DokDataset:
    dataset_id: str
    title: str
    entries: list[DatasetFormatEntry] = field(default_factory=list)

    @property
    def formats(self) -> set[str]:
        return {e.format.upper() for e in self.entries}

    @property
    def has_supported(self) -> bool:
        return bool(self.formats & SUPPORTED_FORMATS)

    def pick_sizing_entry(self) -> DatasetFormatEntry | None:
        by_format = {e.format.upper(): e for e in self.entries}
        for fmt in FORMAT_PREFERENCE:
            if fmt in by_format:
                return by_format[fmt]
        # no supported format available -- still size it, just pick whichever
        # format entry happens to come first.
        return self.entries[0] if self.entries else None


async def fetch(client: httpx.AsyncClient, url: str, cache_path: Path, force_refresh: bool) -> bytes:
    if cache_path.exists() and not force_refresh:
        return cache_path.read_bytes()
    resp = await client.get(url, timeout=120)
    resp.raise_for_status()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(resp.content)
    return resp.content


def parse_register_uuids(csv_bytes: bytes) -> set[str]:
    """Extract metadata UUIDs from the DOK status register CSV (last column)."""
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


def parse_tjenestefeed(xml_bytes: bytes) -> list[DatasetFormatEntry]:
    """Parse level-1 tjenestefeed entries (one per dataset+format)."""
    root = ET.fromstring(xml_bytes)
    entries: list[DatasetFormatEntry] = []
    for e in root.findall("a:entry", NS):
        title_el = e.find("a:title", NS)
        title = title_el.text.strip() if title_el is not None and title_el.text else "?"

        feed_url = None
        csw_metadata_url = None
        for link in e.findall("a:link", NS):
            rel = link.get("rel")
            href = link.get("href")
            if not href:
                continue
            if rel == "describedby":
                csw_metadata_url = href
            elif rel in (None, "alternate") and feed_url is None:
                feed_url = href
        if feed_url is None:
            continue

        fmt_match = FORMAT_RE.search(feed_url)
        fmt = fmt_match.group(1).upper() if fmt_match else "UNKNOWN"
        csw_uuid = None
        if csw_metadata_url:
            uuid_match = UUID_RE.search(csw_metadata_url)
            csw_uuid = uuid_match.group(0).lower() if uuid_match else None

        # dataset_id: the metadata UUID, since it's the one identifier shared
        # by all of a dataset's per-format entries -- titles differ per
        # format (e.g. "... FGDB-format" vs "... GML-format").
        clean_title = TITLE_FORMAT_SUFFIX_RE.sub("", title).strip() or title
        entries.append(DatasetFormatEntry(
            dataset_id=csw_uuid or title, title=clean_title, csw_uuid=csw_uuid, format=fmt, feed_url=feed_url,
        ))
    return entries


def group_dok_datasets(entries: list[DatasetFormatEntry], dok_uuids: set[str]) -> dict[str, DokDataset]:
    grouped: dict[str, DokDataset] = {}
    for entry in entries:
        if entry.csw_uuid not in dok_uuids:
            continue
        ds = grouped.setdefault(entry.dataset_id, DokDataset(dataset_id=entry.dataset_id, title=entry.title))
        ds.entries.append(entry)
    return grouped


def print_tally(datasets: dict[str, DokDataset]) -> None:
    has_supported = 0
    no_supported = 0
    all_formats: Counter[str] = Counter()
    unsupported_only_formats: Counter[str] = Counter()

    for ds in datasets.values():
        for f in ds.formats:
            all_formats[f] += 1
        if ds.has_supported:
            has_supported += 1
        else:
            no_supported += 1
            for f in ds.formats:
                unsupported_only_formats[f] += 1

    log.info("=" * 70)
    log.info("DOK DATASET STATUS")
    log.info("=" * 70)
    log.info("DOK datasets total (in feed): %d", len(datasets))
    log.info("has supported format: %d", has_supported)
    log.info("no supported format: %d", no_supported)
    log.info("all format counts across DOK datasets:")
    for f, c in all_formats.most_common():
        log.info("  %s %d", f, c)
    log.info("formats present ONLY on DOK datasets lacking any supported format:")
    for f, c in unsupported_only_formats.most_common():
        log.info("  %s %d", f, c)
    log.info("=" * 70)


RESTRICTED_CATEGORY_TERM = "norway digital restricted"


def parse_sub_feed_files(xml_bytes: bytes) -> list[tuple[str, str]]:
    """Returns [(file_title, file_url), ...] from a per-dataset/format atom feed."""
    root = ET.fromstring(xml_bytes)
    files = []
    for e in root.findall("a:entry", NS):
        t_el = e.find("a:title", NS)
        file_title = t_el.text.strip() if t_el is not None and t_el.text else ""
        href = None
        for link in e.findall("a:link", NS):
            if link.get("rel") in (None, "alternate"):
                href = link.get("href")
                break
        if href:
            files.append((file_title, href))
    return files


def is_access_restricted(xml_bytes: bytes) -> bool:
    """True if the feed's entries carry the "Norge digitalt-begrenset" access
    restriction category. Those files 403 on anonymous HEAD/GET, so we check
    this up front instead of burning HTTP requests (and retries/timeouts)
    finding it out file-by-file."""
    root = ET.fromstring(xml_bytes)
    for cat in root.findall(".//a:category", NS):
        if (cat.get("term") or "").strip().lower() == RESTRICTED_CATEGORY_TERM:
            return True
    return False


REQUEST_TIMEOUT = 15  # seconds; kept short since a stuck/blocked host would
                      # otherwise multiply into hours across tens of thousands
                      # of per-file requests.


async def ranged_get_size(client: httpx.AsyncClient, url: str) -> tuple[int | None, str | None]:
    """Some Geonorge download endpoints (api/download/file/...) reject HEAD
    with 405. Fall back to a single-byte ranged GET and read the total size
    off Content-Range, closing the stream before any body is downloaded."""
    async with client.stream("GET", url, headers={"Range": "bytes=0-0"}, timeout=REQUEST_TIMEOUT) as r:
        if r.status_code not in (200, 206):
            # e.g. 403 on access-restricted ("norway digital restricted")
            # datasets -- headers on the error body (content-length: 0) are
            # not the file size, so don't trust them.
            return None, f"HTTP {r.status_code} on ranged GET"
        content_range = r.headers.get("content-range")  # "bytes 0-0/12345"
        if content_range and "/" in content_range:
            total = content_range.rsplit("/", 1)[-1]
            if total.isdigit():
                return int(total), None
        if r.status_code == 200:
            cl = r.headers.get("content-length")
            if cl is not None:
                return int(cl), None
        return None, "no usable size in ranged GET response"


async def head_size(client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore,
                     retries: int = 2) -> tuple[int | None, str | None]:
    async with sem:
        for attempt in range(retries):
            try:
                r = await client.head(url, timeout=REQUEST_TIMEOUT)
                if r.status_code == 405:
                    return await ranged_get_size(client, url)
                if r.status_code >= 400:
                    return None, f"HTTP {r.status_code} on HEAD"
                cl = r.headers.get("content-length")
                return (int(cl) if cl is not None else None), None
            except Exception as ex:
                if attempt == retries - 1:
                    return None, str(ex)[:200]
                await asyncio.sleep(1.5 * (attempt + 1))
    return None, "unknown error"


async def size_datasets(
    client: httpx.AsyncClient, datasets: dict[str, DokDataset], sem_meta: asyncio.Semaphore,
    sem_head: asyncio.Semaphore, limit: int | None,
) -> list[dict]:
    sizeable = [(ds, ds.pick_sizing_entry()) for ds in datasets.values()]
    sizeable = [(ds, entry) for ds, entry in sizeable if entry is not None]
    if limit:
        sizeable = sizeable[:limit]

    log.info("Sizing %d DOK datasets (all formats)...", len(sizeable))

    rows: list[dict] = []
    start = time.time()
    for i, (ds, entry) in enumerate(sizeable, 1):
        try:
            subfeed_cache_name = entry.feed_url.rsplit("/", 1)[-1] or f"{ds.dataset_id}.xml"
            sub_xml = await fetch(client, entry.feed_url, CACHE_DIR / "subfeeds" / subfeed_cache_name, force_refresh=False)
            files = parse_sub_feed_files(sub_xml)
        except Exception as ex:
            error_msg = f"subfeed fetch failed: {ex}"
            log.warning("%s: %s", ds.dataset_id, error_msg)
            rows.append({
                "dataset_id": ds.dataset_id, "title": ds.title,
                "formats_available": ";".join(sorted(ds.formats)),
                "has_supported_format": ds.has_supported,
                "sized_format": entry.format, "file_count": 0,
                "size_bytes": "", "size_mb": "", "errors": error_msg,
            })
            continue

        if is_access_restricted(sub_xml):
            # Anonymous HEAD/GET 403s on every file here -- skip the network
            # round-trips entirely rather than retrying/timing out per file.
            rows.append({
                "dataset_id": ds.dataset_id, "title": ds.title,
                "formats_available": ";".join(sorted(ds.formats)),
                "has_supported_format": ds.has_supported,
                "sized_format": entry.format, "file_count": len(files),
                "size_bytes": "", "size_mb": "",
                "errors": "access restricted (Norge digitalt-begrenset), size unavailable anonymously",
            })
            if i % 25 == 0 or i == len(sizeable):
                elapsed = time.time() - start
                log.info("  %d/%d datasets sized (%.0fs elapsed)", i, len(sizeable), elapsed)
            continue

        results = await asyncio.gather(*[head_size(client, url, sem_head) for _, url in files])
        total_bytes = 0
        file_errors: list[str] = []
        for (file_title, file_url), (size, err) in zip(files, results):
            if size is not None:
                total_bytes += size
            else:
                file_errors.append(f"{file_title or file_url}: {err}")
                log.warning("%s: HEAD failed for %s: %s", ds.dataset_id, file_url, err)

        rows.append({
            "dataset_id": ds.dataset_id, "title": ds.title,
            "formats_available": ";".join(sorted(ds.formats)),
            "has_supported_format": ds.has_supported,
            "sized_format": entry.format, "file_count": len(files),
            "size_bytes": total_bytes, "size_mb": f"{total_bytes / (1024 * 1024):.2f}",
            "errors": "; ".join(file_errors),
        })

        if i % 25 == 0 or i == len(sizeable):
            elapsed = time.time() - start
            log.info("  %d/%d datasets sized (%.0fs elapsed)", i, len(sizeable), elapsed)

    return rows


def write_csv(rows: list[dict], output: Path) -> None:
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def print_size_summary(rows: list[dict]) -> None:
    total_bytes = sum(r["size_bytes"] for r in rows if isinstance(r["size_bytes"], int))
    total_files = sum(r["file_count"] for r in rows)
    error_rows = sum(1 for r in rows if r["errors"])
    log.info("=" * 70)
    log.info("DOK DATASET SIZES (all datasets, best available format each)")
    log.info("=" * 70)
    log.info("Datasets sized      : %d", len(rows))
    log.info("Files counted       : %d", total_files)
    log.info("Datasets with errors: %d", error_rows)
    log.info("Total size          : %.2f GB (%.1f MB)", total_bytes / (1024 ** 3), total_bytes / (1024 ** 2))
    log.info("Top 20 DOK datasets by size:")
    ranked = sorted(rows, key=lambda r: r["size_bytes"] if isinstance(r["size_bytes"], int) else 0, reverse=True)[:20]
    for r in ranked:
        size = r["size_bytes"] if isinstance(r["size_bytes"], int) else 0
        log.info("  %10.1f MB  (%4d filer, %10s)  %s", size / (1024 ** 2), r["file_count"], r["sized_format"], r["title"])
    log.info("=" * 70)


async def run(args: argparse.Namespace) -> None:
    headers = {"User-Agent": "geonorge-dok-status/1.0 (personal script)"}
    limits = httpx.Limits(max_connections=60, max_keepalive_connections=30)
    async with httpx.AsyncClient(follow_redirects=True, limits=limits, headers=headers) as client:
        log.info("Fetching DOK status register...")
        register_bytes = await fetch(client, args.register_url, CACHE_DIR / "geodatalov-statusregister.csv", args.force_refresh)
        dok_uuids = parse_register_uuids(register_bytes)
        log.info("  %d DOK datasets in register.", len(dok_uuids))

        log.info("Fetching tjenestefeed...")
        feed_bytes = await fetch(client, args.feed_url, CACHE_DIR / "tjenestefeed.xml", args.force_refresh)
        entries = parse_tjenestefeed(feed_bytes)
        log.info("  %d dataset/format entries in feed.", len(entries))

        datasets = group_dok_datasets(entries, dok_uuids)
        print_tally(datasets)

        if args.skip_sizes:
            return

        sem_meta = asyncio.Semaphore(20)
        sem_head = asyncio.Semaphore(20)
        rows = await size_datasets(client, datasets, sem_meta, sem_head, args.limit)
        write_csv(rows, args.output)
        log.info("Wrote %d rows to %s", len(rows), args.output)
        print_size_summary(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--register-url", default=REGISTER_URL)
    ap.add_argument("--feed-url", default=FEED_URL)
    ap.add_argument("--output", type=Path, default=OUTPUT_CSV)
    ap.add_argument("--skip-sizes", action="store_true", help="Only print the format/status tally, skip HEAD size checks.")
    ap.add_argument("--limit", type=int, default=None, help="Only size the first N DOK datasets (for a quick test run).")
    ap.add_argument("--force-refresh", action="store_true", help="Ignore cached register/feed and re-download.")
    ap.add_argument("--log-file", type=Path, default=LOG_FILE, help="Append run log to this file (in addition to stdout).")
    args = ap.parse_args()

    setup_logging(args.log_file)

    try:
        asyncio.run(run(args))
    except KeyboardInterrupt:
        log.warning("Interrupted.")


if __name__ == "__main__":
    main()
