"""Steg 7c: fyll ut AGENTS.md per collection og for katalogen, uten LLM.

`portolan init`/`add` only ever write a *placeholder* AGENTS.md (verified empirically
against portolan-cli 0.8.0 by scratch-running `portolan init`): section headers plus
HTML-comment prompts like `<!-- What this collection contains and when to use it. -->`,
meant for a human (or an LLM session) to fill in by hand. The rich, dataset-specific
AGENTS.md files under `catalog_backup/` are exactly that: hand-authored, not pipeline
output -- see `IMPROVEMENTS.md`, which documents that pass and the DuckDB-grounded
LLM-generation design that could reproduce it.

This module deliberately does *not* do that. It fills the same skeleton mechanically
from data Portolan itself already computed (`collection.json`'s STAC fields) plus the
human-authored enrichment in `.portolan/metadata.yaml` -- the same two sources
`portolan readme` itself reads. No LLM call, no extra schema-profiling pass over the
actual data. That trades away the domain-level narrative a profiling+LLM pass could
produce (coded-field decoding, cross-collection join keys, sentinel-value warnings) for
being deterministic, free, safe to regenerate on every pipeline run, and honest about
its own limits -- see the caveats each section below writes into the output rather than
guessing.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

_PARQUET_TYPES = {"application/vnd.apache.parquet", "application/x-parquet"}
_PMTILES_TYPE = "application/vnd.pmtiles"

# Structural/boilerplate columns that make poor example-query material -- present in
# almost every Geonorge collection regardless of theme, so picking one of these as the
# "interesting" example column would be misleading rather than merely generic.
_SKIP_EXAMPLE_COLUMNS = {
    "geometry",
    "bbox",
    "objectid",
    "objid",
    "objektid",
    "shape_length",
    "shape_area",
    "lokalid",
    "navnerom",
    "versjonid",
}


def _load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return {}


def _format_size(num_bytes: int | None) -> str:
    if not num_bytes:
        return "-"
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def _data_assets(assets: dict[str, Any]) -> dict[str, Any]:
    return {
        key: asset
        for key, asset in assets.items()
        if asset.get("type") in _PARQUET_TYPES and "data" in (asset.get("roles") or [])
    }


def _pick_primary_asset(collection_id: str, data_assets: dict[str, Any]) -> tuple[str, Any] | None:
    if collection_id in data_assets:
        return collection_id, data_assets[collection_id]
    if data_assets:
        key = next(iter(data_assets))
        return key, data_assets[key]
    return None


def _pick_example_column(columns: list[dict[str, Any]]) -> str | None:
    for col in columns:
        name = col.get("name", "")
        if name.lower() in _SKIP_EXAMPLE_COLUMNS:
            continue
        if col.get("type") == "string":
            return name
    return None


def build_collection_agents_md(collection_dir: Path) -> str | None:
    """Render AGENTS.md for one collection from its own metadata. None if not yet added."""
    collection = _load_json(collection_dir / "collection.json")
    if collection is None:
        return None
    meta = _load_yaml(collection_dir / ".portolan" / "metadata.yaml")

    collection_id = collection_dir.name
    title = collection.get("title") or meta.get("title") or collection_id
    description = (meta.get("description") or collection.get("description") or "").strip()
    contact = meta.get("contact") or {}
    contact_name = contact.get("name")
    contact_email = contact.get("email")
    license_id = collection.get("license") or meta.get("license") or "other"
    license_url = meta.get("license_url")
    source_url = meta.get("source_url")
    processing_notes = meta.get("processing_notes")

    assets: dict[str, Any] = collection.get("assets", {})
    data_assets = _data_assets(assets)
    pmtiles_assets = {k: a for k, a in assets.items() if a.get("type") == _PMTILES_TYPE}
    primary = _pick_primary_asset(collection_id, data_assets)

    columns: list[dict[str, Any]] = collection.get("table:columns") or []
    geometry_type = collection.get("geoparquet:geometry_type")
    feature_count = collection.get("geoparquet:feature_count")
    row_count = collection.get("table:row_count")
    bbox_list = ((collection.get("extent") or {}).get("spatial") or {}).get("bbox") or []
    bbox = bbox_list[0] if bbox_list else None
    proj_code = primary[1].get("proj:code") if primary else None

    lines: list[str] = []
    lines.append(f"# AGENTS.md — {title}")
    lines.append(
        "Guidance for AI agents and LLMs working with this collection. This file "
        "supplements the README with practical, agent-oriented notes. Generated "
        "automatically from `collection.json` and `.portolan/metadata.yaml` by the "
        "GeoNorge -> Portolan pipeline -- edit `metadata.yaml` and regenerate rather "
        "than hand-editing this file, or it will be overwritten on the next run."
    )

    # --- Overview --------------------------------------------------------------
    overview = [description or "_No description available in metadata.yaml._"]
    who = ", ".join(p for p in (contact_name,) if p)
    if who or contact_email:
        contact_line = f"Responsible contact: {who or 'unknown'}"
        if contact_email:
            contact_line += f" <{contact_email}>"
        overview.append(contact_line + ".")
    if source_url:
        overview.append(f"Source: [{source_url}]({source_url}).")
    lines.append("## Overview\n\n" + "\n".join(overview))

    # --- Accessing the data ------------------------------------------------------
    access: list[str] = []
    if data_assets:
        access.append("| Asset | File | Size | CRS |")
        access.append("|---|---|---|---|")
        for key, asset in data_assets.items():
            href = asset.get("href", "").removeprefix("./")
            access.append(
                f"| {key} | `{href}` | {_format_size(asset.get('file:size'))} | "
                f"{asset.get('proj:code') or '-'} |"
            )
        access.append("")
    else:
        access.append("_No GeoParquet data asset registered yet for this collection._\n")

    if primary:
        primary_href = primary[1].get("href", "").removeprefix("./")
        access.append("DuckDB:\n")
        access.append("```sql")
        access.append("INSTALL spatial; LOAD spatial;")
        access.append(f"SELECT * FROM '{primary_href}' LIMIT 10;")
        access.append("```\n")
        access.append("Python / geopandas:\n")
        access.append("```python")
        access.append("import geopandas as gpd")
        access.append("")
        access.append(f'gdf = gpd.read_parquet("{primary_href}")')
        if proj_code:
            access.append(f'print(gdf.crs)          # {proj_code}')
        if geometry_type:
            access.append(f'print(gdf.geom_type.unique())   # {geometry_type}')
        access.append("```")
        if len(data_assets) > 1:
            others = [k for k in data_assets if k != primary[0]]
            access.append(
                "\nOther layers in this collection (same schema shape as above, "
                "different subset): " + ", ".join(f"`{k}`" for k in others) + "."
            )

    if pmtiles_assets:
        pm_key, pm_asset = next(iter(pmtiles_assets.items()))
        pm_href = pm_asset.get("href", "").removeprefix("./")
        access.append(
            f"\nWeb map: `{pm_href}` (PMTiles, asset `{pm_key}`) ships alongside a "
            "default MapLibre style at `styles/default.json` for direct browser "
            "rendering via the `pmtiles://` protocol -- see the `rel=\"pmtiles\"` "
            "link in `collection.json` for the layer name(s)."
        )
    lines.append("## Accessing the data\n\n" + "\n".join(access))

    # --- Schema & field notes ----------------------------------------------------
    schema: list[str] = []
    if columns:
        schema.append("| Column | Type |")
        schema.append("|---|---|")
        for col in columns:
            schema.append(f"| {col.get('name', '')} | {col.get('type', '')} |")
        schema.append(
            "\nField meanings and coded/categorical values are not decoded here -- "
            "this table is mechanically derived from the GeoParquet schema, not "
            "reviewed for domain meaning. Run a `DISTINCT`/`count(*)` query (see "
            "Example queries below) on a column before assuming it is free text."
        )
    else:
        schema.append("_No schema recorded yet for this collection._")
    lines.append("## Schema & field notes\n\n" + "\n".join(schema))

    # --- Data quality & usage notes -----------------------------------------------
    quality: list[str] = []
    if proj_code:
        quality.append(f"- CRS: `{proj_code}`.")
    if geometry_type:
        quality.append(f"- Geometry type: `{geometry_type}`.")
    if feature_count is not None:
        quality.append(f"- Feature count: {feature_count:,}.")
    if row_count is not None and row_count != feature_count:
        quality.append(f"- Row count (all layers/items): {row_count:,}.")
    if bbox:
        quality.append(f"- Spatial extent (WGS84 bbox): `{bbox}`.")
    quality.append(f"- License: `{license_id}`" + (f" ([terms]({license_url}))" if license_url else "") + ".")
    if processing_notes:
        quality.append(f"- Processing: {processing_notes}")
    lines.append("## Data quality & usage notes\n\n" + "\n".join(quality))

    # --- Example queries -----------------------------------------------------------
    examples: list[str] = []
    if primary:
        primary_href = primary[1].get("href", "").removeprefix("./")
        examples.append("Row count and combined bounding box:\n")
        examples.append("```sql")
        examples.append("INSTALL spatial; LOAD spatial;")
        examples.append(
            f"SELECT count(*) AS n, min(bbox.xmin) AS xmin, min(bbox.ymin) AS ymin, "
            f"max(bbox.xmax) AS xmax, max(bbox.ymax) AS ymax FROM '{primary_href}';"
        )
        examples.append("```\n")
        example_col = _pick_example_column(columns)
        if example_col:
            examples.append(f"Check whether `{example_col}` is a coded/categorical field:\n")
            examples.append("```sql")
            examples.append(
                f"SELECT {example_col}, count(*) FROM '{primary_href}' "
                f"GROUP BY {example_col} ORDER BY count(*) DESC;"
            )
            examples.append("```")
    else:
        examples.append("_No data asset registered yet -- nothing to query._")
    lines.append("## Example queries\n\n" + "\n".join(examples))

    # --- Related collections --------------------------------------------------------
    catalog = _load_json(collection_dir.parent / "catalog.json")
    related_lines = [
        "No automated cross-collection relationships (shared join keys, thematic "
        "grouping) are computed here -- that requires domain judgment this pipeline "
        "does not attempt. The full collection list for this catalog:\n"
    ]
    if catalog:
        for link in catalog.get("links", []):
            if link.get("rel") != "child":
                continue
            child_id = Path(link.get("href", "")).parent.as_posix()
            if child_id == collection_id:
                continue
            related_lines.append(f"- [{link.get('title', child_id)}](../{child_id}/AGENTS.md)")
    lines.append("## Related collections\n\n" + "\n".join(related_lines))

    return "\n\n".join(lines) + "\n"


def write_collection_agents_md(collection_dir: Path) -> Path | None:
    content = build_collection_agents_md(collection_dir)
    if content is None:
        return None
    path = collection_dir / "AGENTS.md"
    path.write_text(content, encoding="utf-8")
    return path


def build_catalog_agents_md(catalog_dir: Path) -> str | None:
    """Render the root AGENTS.md from catalog.json + .portolan/metadata.yaml."""
    catalog = _load_json(catalog_dir / "catalog.json")
    if catalog is None:
        return None
    meta = _load_yaml(catalog_dir / ".portolan" / "metadata.yaml")

    title = catalog.get("title") or meta.get("title") or catalog_dir.name
    description = (meta.get("description") or catalog.get("description") or "").strip()
    license_id = catalog.get("license") or meta.get("license") or "other"
    license_url = meta.get("license_url")

    children = [
        (Path(link.get("href", "")).parent.as_posix(), link.get("title", ""))
        for link in catalog.get("links", [])
        if link.get("rel") == "child"
    ]

    lines: list[str] = []
    lines.append(f"# AGENTS.md — {title}")
    lines.append(
        "Guidance for AI agents and LLMs working with this catalog. This file "
        "supplements the README with practical, agent-oriented notes. Generated "
        "automatically from `catalog.json` and `.portolan/metadata.yaml` by the "
        "GeoNorge -> Portolan pipeline -- edit `metadata.yaml` and regenerate rather "
        "than hand-editing this file."
    )
    lines.append("## Overview\n\n" + (description or "_No description available._"))

    noun = "collection is" if len(children) == 1 else "collections are"
    collections_lines = [f"{len(children)} {noun} published in this catalog:\n"]
    for child_id, child_title in children:
        collections_lines.append(f"- [{child_title or child_id}](./{child_id}/AGENTS.md)")
    lines.append("## Collections\n\n" + "\n".join(collections_lines))

    lines.append(
        "## Data access patterns\n\n"
        "Every collection directory holds its data as GeoParquet (`<collection>.parquet` "
        "or `<collection>_<layer>.parquet` for multi-layer collections), readable directly "
        "with DuckDB's `spatial` extension or `geopandas.read_parquet`. Collections with a "
        "`*.pmtiles` asset also carry a `styles/default.json` MapLibre style for direct "
        "browser rendering. See each collection's own `AGENTS.md` for its specific asset "
        "names, schema, and example queries; paths are relative to that collection's own "
        "directory, not this catalog root."
    )

    license_lines = [f"Catalog-level license: `{license_id}`" + (f" ([terms]({license_url}))" if license_url else "") + "."]
    license_lines.append("Individual collections may carry their own, more specific license -- check each collection's own AGENTS.md/README.md rather than assuming this catalog-level default applies uniformly.")
    lines.append("## License\n\n" + "\n".join(license_lines))

    return "\n\n".join(lines) + "\n"


def write_catalog_agents_md(catalog_dir: Path) -> Path | None:
    content = build_catalog_agents_md(catalog_dir)
    if content is None:
        return None
    path = catalog_dir / "AGENTS.md"
    path.write_text(content, encoding="utf-8")
    return path
