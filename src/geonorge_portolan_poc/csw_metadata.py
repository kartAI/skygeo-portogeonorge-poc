"""Steg 4: hent full ISO19115/19139-metadata via CSW GetRecordById."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from pathlib import Path

import requests
from lxml import etree

logger = logging.getLogger(__name__)

GMD_NS = "http://www.isotc211.org/2005/gmd"
GCO_NS = "http://www.isotc211.org/2005/gco"
GMX_NS = "http://www.isotc211.org/2005/gmx"
XLINK_NS = "http://www.w3.org/1999/xlink"
CSW_NSMAP = {"gmd": GMD_NS, "gco": GCO_NS, "gmx": GMX_NS, "xlink": XLINK_NS}

# Known otherConstraints hrefs/labels mapped to SPDX identifiers. GeoNorge
# mostly serves data under NLOD 2.0, which has no official SPDX id, so it maps
# to "other" + a license_url instead.
_LICENSE_MAP: list[tuple[str, str]] = [
    ("creativecommons.org/publicdomain/zero", "CC0-1.0"),
    ("creativecommons.org/licenses/by-sa/4.0", "CC-BY-SA-4.0"),
    ("creativecommons.org/licenses/by/4.0", "CC-BY-4.0"),
]
NLOD_URL = "https://data.norge.no/nlod/no/2.0"


@dataclass
class DatasetMetadata:
    title: str | None
    abstract: str | None
    organisation: str | None
    email: str | None
    license_spdx: str
    license_url: str | None
    license_label: str | None
    bbox: tuple[float, float, float, float] | None  # west, south, east, north


def fetch_csw_record(
    csw_url: str,
    cache_path: Path,
    *,
    force_refresh: bool = False,
    session: requests.Session | None = None,
    retry: int = 3,
    backoff_seconds: float = 1.5,
) -> bytes | None:
    if cache_path.exists() and not force_refresh:
        return cache_path.read_bytes()

    sess = session or requests.Session()
    last_exc: Exception | None = None
    for attempt in range(1, retry + 1):
        try:
            resp = sess.get(csw_url, timeout=60)
            resp.raise_for_status()
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_bytes(resp.content)
            return resp.content
        except requests.RequestException as exc:
            last_exc = exc
            logger.warning(
                "CSW fetch attempt %d/%d failed for %s: %s", attempt, retry, csw_url, exc
            )
            if attempt < retry:
                time.sleep(backoff_seconds * attempt)
    logger.error("Giving up on CSW record %s: %s", csw_url, last_exc)
    return None


def _cs(el: etree._Element | None, xpath: str) -> str | None:
    if el is None:
        return None
    found = el.xpath(xpath, namespaces=CSW_NSMAP)
    for node in found:
        value = (node.text or "").strip() if hasattr(node, "text") else str(node).strip()
        if value:
            return value
    return None


def parse_csw_record(xml_bytes: bytes) -> DatasetMetadata | None:
    try:
        root = etree.fromstring(xml_bytes)
    except etree.XMLSyntaxError:
        logger.exception("CSW record is not valid XML")
        return None

    ident = root.xpath(".//gmd:MD_DataIdentification", namespaces=CSW_NSMAP)
    ident_el = ident[0] if ident else None

    title = _cs(ident_el, ".//gmd:citation//gmd:title//gco:CharacterString/text()")
    abstract = _cs(ident_el, "./gmd:abstract//gco:CharacterString/text()")

    organisation = None
    email = None
    if ident_el is not None:
        # Prefer "owner", then "publisher", then any point of contact.
        for role in ("owner", "publisher", None):
            xpath = ".//gmd:pointOfContact/gmd:CI_ResponsibleParty"
            if role:
                xpath += f"[.//gmd:CI_RoleCode/@codeListValue='{role}']"
            parties = ident_el.xpath(xpath, namespaces=CSW_NSMAP)
            if parties:
                party = parties[0]
                organisation = _cs(party, ".//gmd:organisationName//gco:CharacterString/text()")
                email = _cs(party, ".//gmd:electronicMailAddress/gco:CharacterString/text()")
                break
    if organisation is None:
        # Fall back to the top-level metadata contact.
        organisation = _cs(root, ".//gmd:contact//gmd:organisationName//gco:CharacterString/text()")
        email = _cs(root, ".//gmd:contact//gmd:electronicMailAddress/gco:CharacterString/text()")

    license_spdx = "other"
    license_url: str | None = None
    license_label: str | None = None
    if ident_el is not None:
        for constraint in ident_el.xpath(
            ".//gmd:resourceConstraints//gmd:otherConstraints", namespaces=CSW_NSMAP
        ):
            anchors = constraint.xpath(".//gmx:Anchor", namespaces=CSW_NSMAP)
            for anchor in anchors:
                href = anchor.get(f"{{{XLINK_NS}}}href") or ""
                label = (anchor.text or "").strip()
                matched_spdx = next((spdx for needle, spdx in _LICENSE_MAP if needle in href), None)
                if matched_spdx:
                    license_spdx, license_url, license_label = matched_spdx, href, label
                    break
                if "nlod" in href.lower() and license_url is None:
                    license_url, license_label = href, label
            if license_spdx != "other" or license_url:
                break

    if license_spdx == "other" and license_url is None:
        license_url = NLOD_URL
        license_label = license_label or "Norsk lisens for offentlige data (NLOD) 2.0"

    bbox = None
    if ident_el is not None:
        bbox_els = ident_el.xpath(".//gmd:EX_GeographicBoundingBox", namespaces=CSW_NSMAP)
        if bbox_els:
            b = bbox_els[0]
            try:
                west = float(_cs(b, "./gmd:westBoundLongitude/gco:Decimal/text()"))
                east = float(_cs(b, "./gmd:eastBoundLongitude/gco:Decimal/text()"))
                south = float(_cs(b, "./gmd:southBoundLatitude/gco:Decimal/text()"))
                north = float(_cs(b, "./gmd:northBoundLatitude/gco:Decimal/text()"))
                bbox = (west, south, east, north)
            except (TypeError, ValueError):
                bbox = None

    return DatasetMetadata(
        title=title,
        abstract=abstract,
        organisation=organisation,
        email=email,
        license_spdx=license_spdx,
        license_url=license_url,
        license_label=license_label,
        bbox=bbox,
    )
