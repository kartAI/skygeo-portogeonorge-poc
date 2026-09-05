"""Steg 6: konverter til Portolans metadata.yaml-format (.portolan/metadata.yaml).

Feltnavnene her er hentet fra `portolan metadata init`'s faktiske template
(kjort mot portolan-cli 0.8.0), ikke gjettet fra plan-dokumentet: contact,
license, providers, license_url, source_url, processing_notes er de feltene
CLI-en selv skriver ut, og det er disse `portolan check` faktisk leser.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from geonorge_portolan_poc.csw_metadata import DatasetMetadata
from geonorge_portolan_poc.feed import FeedEntry

NLOD_URL = "https://data.norge.no/nlod/no/2.0"


def build_collection_metadata(
    entry: FeedEntry,
    csw: DatasetMetadata | None,
    *,
    processing_notes: str,
) -> dict[str, Any]:
    organisation = (csw.organisation if csw else None) or entry.author or entry.rights or "Geonorge"
    email = (csw.email if csw else None) or "post@geonorge.no"
    description = (csw.abstract if csw else None) or entry.summary or entry.title

    license_spdx = csw.license_spdx if csw else "other"
    license_url = csw.license_url if csw else NLOD_URL

    data: dict[str, Any] = {
        "title": (csw.title if csw and csw.title else None) or entry.title,
        "description": description,
        "contact": {"name": organisation, "email": email},
        "license": license_spdx,
        "license_url": license_url,
        "providers": [
            {
                "name": organisation,
                "roles": ["producer", "licensor"],
                "url": "https://www.geonorge.no/",
            },
            {
                "name": "Norkart Portolan PoC",
                "roles": ["processor", "host"],
                "url": "https://github.com/norkart",
            },
        ],
        "source_url": entry.feed_url,
        "processing_notes": processing_notes,
    }
    return data


def build_catalog_metadata(*, title: str, description: str) -> dict[str, Any]:
    return {
        "title": title,
        "description": description,
        "contact": {"name": "Norkart Portolan PoC", "email": "post@geonorge.no"},
        "license": "other",
        "license_url": NLOD_URL,
        "providers": [
            {
                "name": "Kartverket / Geonorge",
                "roles": ["producer", "licensor"],
                "url": "https://www.geonorge.no/",
            },
            {
                "name": "Norkart Portolan PoC",
                "roles": ["processor", "host"],
                "url": "https://github.com/norkart",
            },
        ],
        "processing_notes": (
            "Automatisk generert konseptbevis: datasett crawlet fra Geonorges "
            "Tjenestefeed (Atom), beriket med ISO19115-metadata via CSW, og "
            "publisert som en Portolan STAC-katalog med portolan-cli."
        ),
    }


def write_metadata_yaml(data: dict[str, Any], collection_dir: Path) -> Path:
    portolan_dir = collection_dir / ".portolan"
    portolan_dir.mkdir(parents=True, exist_ok=True)
    path = portolan_dir / "metadata.yaml"
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)
    return path
