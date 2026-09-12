"""Orchestrator: kjorer steg 1-8 i rekkefolge og samler resultater til REPORT.md."""

from __future__ import annotations

import json
import logging
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

import requests

from geonorge_portolan_poc import csw_metadata, dataset_feed, dok_register, download, feed, sample, styling
from geonorge_portolan_poc.agents_md import write_catalog_agents_md, write_collection_agents_md
from geonorge_portolan_poc.config import Config
from geonorge_portolan_poc.convert_gpkg import convert_to_geopackage
from geonorge_portolan_poc.metadata_yaml import (
    build_catalog_metadata,
    build_collection_metadata,
    write_metadata_yaml,
)
from geonorge_portolan_poc.portolan_runner import (
    _promote_parquet_if_orphaned,
    add_collection,
    configure_pmtiles_max_zoom,
    final_add,
    final_check_fix,
    final_check_plain,
    final_check_strict,
    generate_readme,
    init_catalog,
)

logger = logging.getLogger(__name__)


def sanitize_collection_name(dataset_id: str) -> str:
    s = dataset_id.lower().replace("_", "-")
    s = re.sub(r"[^a-z0-9-]", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    if not s or not s[0].isalnum():
        s = "d-" + s
    return s


@dataclass
class DatasetResult:
    dataset_id: str
    collection_name: str
    title: str
    format: str
    status: str = "pending"
    notes: list[str] = field(default_factory=list)
    style_decision: str | None = None
    style_note: str | None = None
    license_spdx: str | None = None
    organisation: str | None = None
    download_url: str | None = None


@dataclass
class PipelineReport:
    total_entries: int = 0
    unique_datasets: int = 0
    sample_skipped: dict[str, str] = field(default_factory=dict)
    results: list[DatasetResult] = field(default_factory=list)
    final_check_ok: bool = False
    final_check_output: str = ""
    final_check_strict_ok: bool = False
    final_check_strict_output: str = ""


def run_pipeline(config: Config, *, force_refresh_feed: bool = False) -> PipelineReport:
    session = requests.Session()
    session.headers["User-Agent"] = "geonorge-portolan-poc/0.1 (+https://github.com/norkart)"

    cache_dir = config.paths.cache_dir
    catalog_dir = config.paths.catalog_dir
    catalog_dir.mkdir(parents=True, exist_ok=True)

    report = PipelineReport()

    # --- Steg 1: crawl niva 1 ---------------------------------------------
    logger.info("Steg 1: crawling tjenestefeed %s", config.feed_url)
    xml = feed.fetch_tjenestefeed(
        config.feed_url, cache_dir / "tjenestefeed.xml", force_refresh=force_refresh_feed, session=session
    )
    entries = feed.parse_tjenestefeed(xml)
    grouped = feed.group_by_dataset(entries)
    report.total_entries = len(entries)
    report.unique_datasets = len(grouped)
    logger.info("Parsed %d entries across %d unique datasets", len(entries), len(grouped))

    # --- Steg 2: sample ----------------------------------------------------
    allowed_uuids: set[str] | None = None
    if config.sample.dok_register_enabled:
        register_csv = dok_register.fetch_register(
            config.sample.dok_register_url,
            cache_dir / "geodatalov-statusregister.csv",
            force_refresh=force_refresh_feed,
            session=session,
        )
        allowed_uuids = dok_register.parse_register_uuids(register_csv)
        logger.info("Loaded %d DOK-register UUIDs for allow-list filtering", len(allowed_uuids))

    logger.info("Steg 2: selecting sample (size=%d)", config.sample.size)
    selected, skip_reasons = sample.select_sample(
        grouped,
        sample_size=config.sample.size,
        preferred_formats=config.sample.preferred_formats,
        random_seed=config.sample.random_seed,
        include_title_pattern=config.sample.include_title_pattern,
        exclude_title_pattern=config.sample.exclude_title_pattern,
        random_selection=config.sample.random_selection,
        allowed_uuids=allowed_uuids,
    )
    report.sample_skipped = skip_reasons
    logger.info("Selected %d datasets for the sample", len(selected))

    # --- Steg 7a: init catalog ---------------------------------------------
    init_result = init_catalog(
        catalog_dir,
        catalog_id=config.portolan.catalog_id,
        title=config.portolan.catalog_title,
        description=config.portolan.catalog_description,
        license_spdx=config.portolan.catalog_license,
        license_url=config.portolan.catalog_license_url,
    )
    if not init_result.ok:
        logger.error("portolan init failed:\n%s", init_result.stderr)

    if config.pmtiles.enabled:
        zoom_result = configure_pmtiles_max_zoom(catalog_dir, config.pmtiles.max_zoom)
        if zoom_result is not None and not zoom_result.ok:
            logger.error("Failed to set pmtiles.max_zoom:\n%s", zoom_result.stderr)

    catalog_meta = build_catalog_metadata(
        title=config.portolan.catalog_title, description=config.portolan.catalog_description
    )
    write_metadata_yaml(catalog_meta, catalog_dir)

    # --- Steg 5b: tegneregel-register (fetched once, reused per dataset) --
    registry: list[styling.RegistryEntry] = []
    if config.styling.enabled:
        try:
            registry = styling.fetch_registry(config.styling.registry_url, cache_dir / "tegneregler.json")
            logger.info("Loaded %d tegneregler registry entries", len(registry))
        except requests.RequestException:
            logger.exception("Failed to fetch tegneregler registry; styling disabled for this run")

    used_names: set[str] = set()

    for entry in selected:
        base_name = sanitize_collection_name(entry.dataset_id)
        collection_name = base_name
        i = 2
        while collection_name in used_names:
            collection_name = f"{base_name}-{i}"
            i += 1
        used_names.add(collection_name)

        result = DatasetResult(
            dataset_id=entry.dataset_id,
            collection_name=collection_name,
            title=entry.title,
            format=entry.format,
        )
        report.results.append(result)
        collection_dir = catalog_dir / collection_name

        # `<collection>.gpkg.bak` (see _process_dataset) is the reliable
        # "fully processed" marker: unlike the primary `<collection>.gpkg`,
        # which a successful run's asset-collision workaround deletes (and
        # which is therefore absent for a collection that finished processing
        # cleanly), the archival backup is written once and never touched
        # again, so its presence can't be mistaken for an in-progress run.
        if (collection_dir / "collection.json").exists() and (
            collection_dir / f"{collection_name}.gpkg.bak"
        ).exists():
            result.status = "ok"
            result.notes.append("Already processed in a previous run; skipped re-download/convert/add")
            logger.info("Skipping %s: already processed", entry.dataset_id)
            continue

        try:
            _process_dataset(
                entry=entry,
                collection_dir=collection_dir,
                config=config,
                cache_dir=cache_dir,
                session=session,
                registry=registry,
                result=result,
            )
        except Exception:
            logger.exception("Unhandled error processing dataset %s", entry.dataset_id)
            result.status = "error"
            result.notes.append("Unhandled exception; see logs")

    # --- Steg 7b: catalog-wide fix/add/promotion pass -----------------------
    fix_result = final_check_fix(catalog_dir, workers=config.portolan.workers)

    # final_check_fix (catalog-wide) can convert a *skipped* (already-processed
    # in an earlier run) collection's gpkg to parquet with no per-dataset add
    # call left in this run to register it -- pick those up now.
    final_add(catalog_dir, workers=config.portolan.workers, pmtiles=config.pmtiles.enabled)

    # Same-stem gpkg/parquet asset-collision correction (see
    # portolan_runner.py's module docstring), applied catalog-wide in case it
    # affected a collection that add_collection() didn't touch this run.
    for child in sorted(catalog_dir.iterdir()):
        if child.is_dir() and not child.name.startswith("."):
            _promote_parquet_if_orphaned(catalog_dir, child.name, pmtiles=config.pmtiles.enabled)

    # --- Steg 7c/8: readme + AGENTS.md + final validation -------------------
    # Runs after every add/check--fix/promotion call above so both reflect the
    # final, settled asset state (a gpkg/parquet promotion or a late-arriving
    # PMTiles asset would otherwise go undocumented).
    generate_readme(catalog_dir)
    for child in sorted(catalog_dir.iterdir()):
        if child.is_dir() and not child.name.startswith("."):
            write_collection_agents_md(child)
    write_catalog_agents_md(catalog_dir)

    # `portolan add` tracks README.md as a checksummed "documentation" asset
    # (AGENTS.md is only ever linked, never asset-tracked, so it needs no
    # equivalent step), but only re-registers it under `--force` (see
    # final_add's docstring). Regenerating the README just above without
    # this would leave that checksum registered against the *previous*
    # README content, and `check` would fail PTL-DAT-001/002 on every
    # collection -- confirmed empirically while wiring this up.
    final_add(catalog_dir, workers=config.portolan.workers, pmtiles=config.pmtiles.enabled, force=True)

    plain_result = final_check_plain(catalog_dir)
    strict_result = final_check_strict(catalog_dir)

    report.final_check_ok = plain_result.ok
    report.final_check_output = (fix_result.stdout + "\n" + plain_result.stdout + plain_result.stderr).strip()
    report.final_check_strict_ok = strict_result.ok
    report.final_check_strict_output = (strict_result.stdout + strict_result.stderr).strip()

    return report


def _process_dataset(
    *,
    entry: feed.FeedEntry,
    collection_dir: Path,
    config: Config,
    cache_dir: Path,
    session: requests.Session,
    registry: list[styling.RegistryEntry],
    result: DatasetResult,
) -> None:
    # --- Steg 3: niva 2 feed -> nedlastings-URL -----------------------------
    level2_xml = dataset_feed.fetch_dataset_feed(
        entry.feed_url, cache_dir / "level2" / f"{entry.dataset_id}.xml", session=session
    )
    if level2_xml is None:
        result.status = "level2_feed_failed"
        result.notes.append(f"Could not fetch dataset feed {entry.feed_url}")
        return

    candidates = dataset_feed.parse_dataset_feed(level2_xml)
    picked = dataset_feed.pick_download(candidates, prefer_national=config.sample.prefer_national_extent)
    if picked is None:
        result.status = "no_download_url"
        result.notes.append("Dataset feed had no entries with a download link")
        return
    result.download_url = picked.url

    # --- Steg 4: CSW metadata (best-effort) --------------------------------
    csw_meta = None
    if entry.csw_metadata_url:
        csw_xml = csw_metadata.fetch_csw_record(
            entry.csw_metadata_url, cache_dir / "csw" / f"{entry.dataset_id}.xml", session=session
        )
        if csw_xml is not None:
            csw_meta = csw_metadata.parse_csw_record(csw_xml)
    if csw_meta is None:
        result.notes.append("CSW metadata unavailable; fell back to feed-level title/summary")
    else:
        result.license_spdx = csw_meta.license_spdx
        result.organisation = csw_meta.organisation

    # --- Steg 5: download + Steg 5 (extra): normalize to GeoPackage --------
    raw_dir = collection_dir / "_src"
    downloaded = download.download_file(picked.url, raw_dir, session=session)
    if downloaded is None:
        result.status = "download_failed"
        result.notes.append(f"Failed to download {picked.url}")
        shutil.rmtree(raw_dir, ignore_errors=True)
        return

    gpkg_path = convert_to_geopackage(raw_dir, entry.format, collection_dir, layer_name=result.collection_name)
    shutil.rmtree(raw_dir, ignore_errors=True)
    if gpkg_path is None:
        result.status = "convert_failed"
        result.notes.append(f"ogr2ogr could not convert the downloaded {entry.format} file to GeoPackage")
        shutil.rmtree(collection_dir, ignore_errors=True)
        return

    # The `<collection>.gpkg` add_collection() is about to process is only
    # ever a stepping stone to GeoParquet: portolan-cli's asset-collision
    # workaround (see portolan_runner.py's module docstring) deletes it once
    # promoted, and for multi-layer sources it can end up orphaned (present
    # on disk but never registered as an asset) instead. Either way the
    # original GeoPackage is lost from the published catalog. Archive a copy
    # under a `.gpkg.bak` suffix -- not `.gpkg`, which `portolan check --fix`
    # would otherwise treat as a convertible geo asset and re-derive (and
    # fail to register) a GeoParquet copy from on every future run -- before
    # add_collection() runs, so the first `portolan add` picks it up and
    # registers it as its own permanent, checksummed asset.
    original_gpkg_backup = collection_dir / f"{result.collection_name}.gpkg.bak"
    shutil.copy2(gpkg_path, original_gpkg_backup)

    # --- Steg 5b: authoritative styling (best-effort) -----------------------
    if config.styling.enabled and registry:
        style_result = styling.resolve_style(
            entry.title, collection_dir, registry, match_threshold=config.styling.match_threshold, session=session
        )
        result.style_decision = style_result.decision
        result.style_note = style_result.note
    else:
        result.style_decision = "no-match-found"
        result.style_note = "Styling step disabled or registry unavailable"

    # --- Steg 6: metadata.yaml ----------------------------------------------
    processing_notes = (
        f"Hentet fra Geonorge Tjenestefeed (niva 2: {entry.feed_url}), format {entry.format} "
        f"konvertert til GeoPackage med ogr2ogr, og publisert med portolan-cli."
    )
    metadata = build_collection_metadata(entry, csw_meta, processing_notes=processing_notes)
    write_metadata_yaml(metadata, collection_dir)

    # --- Steg 7: portolan add / check --fix / add --------------------------
    add_results = add_collection(
        collection_dir.parent,
        result.collection_name,
        workers=config.portolan.workers,
        pmtiles=config.pmtiles.enabled,
    )
    if all(r.ok for r in add_results):
        result.status = "ok"
    else:
        result.status = "portolan_add_failed"
        for r in add_results:
            if not r.ok:
                result.notes.append(f"{' '.join(r.args)} -> exit {r.returncode}: {r.stderr[-500:]}")
