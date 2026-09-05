"""Steg 5b: soek etter autoritativ kartografi (SLD/QML) i Geonorges tegneregel-register.

Registeret (https://register.geonorge.no/api/tegneregler) er i all hovedsak
PDF-dokumentasjon for mennesker (se REPORT.md for treffrate), sa denne modulen
er bygget rundt en eksplisitt fallback fra dag en: portolan sin auto-genererte
default-style brukes uendret nar ingen maskinlesbar stil finnes.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import requests
from lxml import etree
from rapidfuzz import fuzz, process

logger = logging.getLogger(__name__)

StyleDecision = Literal["authoritative-sld", "authoritative-pdf-only", "no-match-found"]


@dataclass
class RegistryEntry:
    label: str
    cartography_file: str | None
    documentreference: str | None


@dataclass
class StyleResult:
    decision: StyleDecision
    matched_label: str | None
    match_score: float | None
    style_path: Path | None  # downloaded SLD, if any
    maplibre_style_path: Path | None  # derived MapLibre override, if any
    note: str


def fetch_registry(
    registry_url: str,
    cache_path: Path,
    *,
    force_refresh: bool = False,
    session: requests.Session | None = None,
) -> list[RegistryEntry]:
    if cache_path.exists() and not force_refresh:
        raw = json.loads(cache_path.read_text(encoding="utf-8"))
    else:
        sess = session or requests.Session()
        resp = sess.get(registry_url, timeout=60)
        resp.raise_for_status()
        raw = resp.json()
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")

    entries = []
    for item in raw.get("containeditems", []):
        entries.append(
            RegistryEntry(
                label=item.get("label", ""),
                cartography_file=item.get("CartographyFile"),
                documentreference=item.get("documentreference"),
            )
        )
    return entries


def find_style(
    title: str,
    registry: list[RegistryEntry],
    *,
    match_threshold: int = 80,
) -> tuple[RegistryEntry | None, float]:
    if not registry:
        return None, 0.0
    choices = {i: e.label for i, e in enumerate(registry)}
    match = process.extractOne(title, choices, scorer=fuzz.WRatio)
    if match is None:
        return None, 0.0
    _label, score, idx = match
    if score < match_threshold:
        return None, score
    return registry[idx], score


def _download(url: str, dest: Path, *, session: requests.Session) -> tuple[bytes, str] | None:
    try:
        resp = session.get(url, timeout=60, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException:
        logger.exception("Failed to download style candidate %s", url)
        return None
    content_type = resp.headers.get("Content-Type", "")
    return resp.content, content_type


_SLD_NS = {"sld": "http://www.opengis.net/sld", "ogc": "http://www.opengis.net/ogc"}
_HEX_RE = re.compile(r"#[0-9a-fA-F]{6}")


def _extract_sld_colors(sld_bytes: bytes) -> dict[str, str]:
    """Best-effort pull of fill/stroke colors out of an SLD (see plan steg 5b)."""
    try:
        root = etree.fromstring(sld_bytes)
    except etree.XMLSyntaxError:
        return {}

    colors: dict[str, str] = {}
    for css in root.iter("{http://www.opengis.net/sld}CssParameter"):
        name = css.get("name")
        value = (css.text or "").strip()
        if not name or not _HEX_RE.fullmatch(value):
            continue
        if name == "fill" and "fill" not in colors:
            colors["fill"] = value
        elif name == "stroke" and "stroke" not in colors:
            colors["stroke"] = value
    return colors


def _build_maplibre_override(colors: dict[str, str], layer_id: str) -> dict[str, Any]:
    fill = colors.get("fill", "#3388ff")
    stroke = colors.get("stroke", "#1a1a1a")
    return {
        "version": 8,
        "name": f"{layer_id}-authoritative-colors",
        "sources": {},
        "layers": [
            {
                "id": f"{layer_id}-fill",
                "type": "fill",
                "paint": {"fill-color": fill, "fill-opacity": 0.6},
            },
            {
                "id": f"{layer_id}-outline",
                "type": "line",
                "paint": {"line-color": stroke, "line-width": 1},
            },
        ],
        "_note": (
            "Derived from an authoritative SLD found in Geonorge's tegneregel-register "
            "(https://register.geonorge.no/tegneregler). Colors only -- see REPORT.md."
        ),
    }


def resolve_style(
    title: str,
    collection_dir: Path,
    registry: list[RegistryEntry],
    *,
    match_threshold: int = 80,
    session: requests.Session | None = None,
) -> StyleResult:
    sess = session or requests.Session()
    matched, score = find_style(title, registry, match_threshold=match_threshold)

    if matched is None:
        return StyleResult("no-match-found", None, score, None, None, "No registry entry matched title")

    if not matched.cartography_file:
        if matched.documentreference:
            return StyleResult(
                "authoritative-pdf-only",
                matched.label,
                score,
                None,
                None,
                f"Only human-readable PDF documentation found: {matched.documentreference}",
            )
        return StyleResult("no-match-found", matched.label, score, None, None, "Matched entry has no style file")

    downloaded = _download(matched.cartography_file, collection_dir, session=sess)
    if downloaded is None:
        return StyleResult(
            "no-match-found", matched.label, score, None, None, "Failed to download CartographyFile"
        )
    content, content_type = downloaded

    is_sld = matched.cartography_file.lower().endswith(".sld") or "xml" in content_type or b"<StyledLayerDescriptor" in content[:200]
    if not is_sld:
        return StyleResult(
            "authoritative-pdf-only",
            matched.label,
            score,
            None,
            None,
            f"CartographyFile resolved to non-SLD content ({content_type or 'unknown type'})",
        )

    portolan_dir = collection_dir / ".portolan"
    portolan_dir.mkdir(parents=True, exist_ok=True)
    style_path = portolan_dir / "style.sld"
    style_path.write_bytes(content)

    colors = _extract_sld_colors(content)
    maplibre_path = None
    if colors:
        maplibre_path = collection_dir / ".portolan" / "style.override.json"
        maplibre_path.write_text(
            json.dumps(_build_maplibre_override(colors, collection_dir.name), indent=2),
            encoding="utf-8",
        )

    return StyleResult(
        "authoritative-sld",
        matched.label,
        score,
        style_path,
        maplibre_path,
        f"Downloaded SLD from tegneregel-register (colors extracted: {bool(colors)})",
    )
