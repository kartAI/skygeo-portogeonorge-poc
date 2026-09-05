"""Steg 3: crawl datasettenes egne Atom-feeder (niva 2) for konkrete nedlastings-URL-er."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path

import requests
from lxml import etree

from geonorge_portolan_poc.xml_utils import NSMAP, text as _text

logger = logging.getLogger(__name__)

_NATIONAL_RE = re.compile(r"landsdekkende|hele landet|norge\b", re.IGNORECASE)


@dataclass
class DownloadCandidate:
    title: str
    url: str
    crs: str | None
    updated: str | None


def fetch_dataset_feed(
    feed_url: str,
    cache_path: Path,
    *,
    force_refresh: bool = False,
    session: requests.Session | None = None,
) -> bytes | None:
    if cache_path.exists() and not force_refresh:
        return cache_path.read_bytes()

    sess = session or requests.Session()
    try:
        resp = sess.get(feed_url, timeout=120, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException:
        logger.exception("Failed to fetch dataset feed %s", feed_url)
        return None

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(resp.content)
    return resp.content


def parse_dataset_feed(xml_bytes: bytes) -> list[DownloadCandidate]:
    root = etree.fromstring(xml_bytes)
    entries = root.findall("atom:entry", namespaces=NSMAP)

    candidates: list[DownloadCandidate] = []
    for e in entries:
        title = _text(e.find("atom:title", NSMAP)) or ""
        updated = _text(e.find("atom:updated", NSMAP))
        category_el = e.find("atom:category", NSMAP)
        crs = category_el.get("term") if category_el is not None else None

        url: str | None = None
        for link in e.findall("atom:link", NSMAP):
            rel = link.get("rel")
            href = link.get("href") or _text(link)
            if not href:
                continue
            if rel in (None, "alternate"):
                url = href
                break

        if url is None:
            continue

        candidates.append(DownloadCandidate(title=title, url=url, crs=crs, updated=updated))
    return candidates


def pick_download(
    candidates: list[DownloadCandidate], *, prefer_national: bool = True
) -> DownloadCandidate | None:
    if not candidates:
        return None
    if prefer_national:
        for c in candidates:
            if _NATIONAL_RE.search(c.title):
                return c
    return candidates[0]
