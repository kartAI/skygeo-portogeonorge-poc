"""Load and validate config.yaml."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class SampleConfig:
    size: int = 20
    preferred_formats: list[str] = field(
        default_factory=lambda: ["GEOJSON", "GPKG", "GEOPACKAGE", "SHAPE", "FGDB"]
    )
    prefer_national_extent: bool = True
    random_seed: int | None = 42
    random_selection: bool = True
    exclude_title_pattern: str | None = None
    include_title_pattern: str | None = None


@dataclass
class PathsConfig:
    cache_dir: Path = Path("./cache")
    catalog_dir: Path = Path("./catalog")


@dataclass
class StylingConfig:
    enabled: bool = True
    registry_url: str = "https://register.geonorge.no/api/tegneregler"
    match_threshold: int = 90
    fallback: str = "portolan-default"


@dataclass
class PortolanConfig:
    catalog_id: str = "geonorge-portolan-poc"
    catalog_title: str = "GeoNorge -> Portolan PoC"
    catalog_description: str = "GeoNorge -> Portolan proof of concept."
    catalog_license: str = "other"
    catalog_license_url: str | None = "https://data.norge.no/nlod/no/2.0"
    workers: int = 4
    push_remote: str | None = None


@dataclass
class Config:
    feed_url: str = "https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml"
    sample: SampleConfig = field(default_factory=SampleConfig)
    paths: PathsConfig = field(default_factory=PathsConfig)
    styling: StylingConfig = field(default_factory=StylingConfig)
    portolan: PortolanConfig = field(default_factory=PortolanConfig)


def load_config(path: Path) -> Config:
    raw: dict[str, Any] = {}
    if path.exists():
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    sample_raw = raw.get("sample", {})
    paths_raw = raw.get("paths", {})
    styling_raw = raw.get("styling", {})
    portolan_raw = raw.get("portolan", {})

    return Config(
        feed_url=raw.get("feed_url", Config.feed_url),
        sample=SampleConfig(**sample_raw),
        paths=PathsConfig(
            cache_dir=Path(paths_raw.get("cache_dir", "./cache")),
            catalog_dir=Path(paths_raw.get("catalog_dir", "./catalog")),
        ),
        styling=StylingConfig(**styling_raw),
        portolan=PortolanConfig(**portolan_raw),
    )
