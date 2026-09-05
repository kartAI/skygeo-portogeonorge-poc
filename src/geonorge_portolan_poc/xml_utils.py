"""Shared Atom/XML namespace map and helpers for GeoNorge feed parsing."""

from __future__ import annotations

from lxml import etree

ATOM_NS = "http://www.w3.org/2005/Atom"
INSPIRE_DLS_NS = "http://inspire.ec.europa.eu/schemas/inspire_dls/1.0"
NSMAP = {"atom": ATOM_NS, "inspire_dls": INSPIRE_DLS_NS}


def text(el: etree._Element | None) -> str | None:
    if el is None or el.text is None:
        return None
    value = el.text.strip()
    return value or None
