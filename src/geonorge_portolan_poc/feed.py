"""Steg 1: crawl Tjenestefeed_daglig.xml (niva 1, feed-of-feeds)."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path

import requests
from lxml import etree

from geonorge_portolan_poc.xml_utils import NSMAP, text as _text

logger = logging.getLogger(__name__)

# The dataset-level Atom feed filename reliably encodes its format, e.g.
# ".../Kommuner2024_AtomFeedFGDB.xml" -> "FGDB". Verified against the full
# 1043-entry feed: every entry matches, so this is more complete than
# guessing the format from the free-text title.
_FORMAT_RE = re.compile(r"AtomFeed([A-Za-z0-9]+)\.xml", re.IGNORECASE)


@dataclass
class FeedEntry:
    title: str
    summary: str
    dataset_id: str
    dataset_namespace: str | None
    format: str
    feed_url: str
    csw_metadata_url: str | None
    crs: str | None
    rights: str | None
    author: str | None
    updated: str | None
    published: str | None


def fetch_tjenestefeed(
    url: str,
    cache_path: Path,
    *,
    force_refresh: bool = False,
    session: requests.Session | None = None,
) -> bytes:
    """Download (or reuse cached) Tjenestefeed_daglig.xml."""
    if cache_path.exists() and not force_refresh:
        logger.info("Using cached tjenestefeed: %s", cache_path)
        return cache_path.read_bytes()

    sess = session or requests.Session()
    logger.info("Fetching tjenestefeed from %s", url)
    resp = sess.get(url, timeout=120)
    resp.raise_for_status()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(resp.content)
    return resp.content


def parse_tjenestefeed(xml_bytes: bytes) -> list[FeedEntry]:
    """Parse level-1 feed entries into FeedEntry records."""
    root = etree.fromstring(xml_bytes)
    entries = root.findall("atom:entry", namespaces=NSMAP)

    results: list[FeedEntry] = []
    for e in entries:
        title = _text(e.find("atom:title", NSMAP)) or ""
        summary = _text(e.find("atom:summary", NSMAP)) or ""
        dataset_id = _text(e.find("inspire_dls:spatial_dataset_identifier_code", NSMAP))
        dataset_namespace = _text(
            e.find("inspire_dls:spatial_dataset_identifier_namespace", NSMAP)
        )
        rights = _text(e.find("atom:rights", NSMAP))
        updated = _text(e.find("atom:updated", NSMAP))
        published = _text(e.find("atom:published", NSMAP))
        author = _text(e.find("atom:author/atom:name", NSMAP))
        category_el = e.find("atom:category", NSMAP)
        crs = category_el.get("term") if category_el is not None else None

        feed_url: str | None = None
        csw_metadata_url: str | None = None
        for link in e.findall("atom:link", NSMAP):
            rel = link.get("rel")
            href = link.get("href") or _text(link)
            if not href:
                continue
            if rel == "describedby":
                csw_metadata_url = href
            elif rel in (None, "alternate") and feed_url is None:
                feed_url = href

        if not dataset_id or not feed_url:
            logger.warning("Skipping entry missing dataset_id/feed_url: %r", title)
            continue

        fmt_match = _FORMAT_RE.search(feed_url)
        fmt = fmt_match.group(1).upper() if fmt_match else "UNKNOWN"

        results.append(
            FeedEntry(
                title=title,
                summary=summary,
                dataset_id=dataset_id,
                dataset_namespace=dataset_namespace,
                format=fmt,
                feed_url=feed_url,
                csw_metadata_url=csw_metadata_url,
                crs=crs,
                rights=rights,
                author=author,
                updated=updated,
                published=published,
            )
        )
    return results


def group_by_dataset(entries: list[FeedEntry]) -> dict[str, list[FeedEntry]]:
    grouped: dict[str, list[FeedEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.dataset_id, []).append(entry)
    return grouped
