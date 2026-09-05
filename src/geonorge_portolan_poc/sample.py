"""Steg 2: utvalg av sample (konfigurerbart antall datasett)."""

from __future__ import annotations

import logging
import random
import re

from geonorge_portolan_poc.feed import FeedEntry

logger = logging.getLogger(__name__)


def select_sample(
    grouped: dict[str, list[FeedEntry]],
    *,
    sample_size: int,
    preferred_formats: list[str],
    random_seed: int | None = None,
    include_title_pattern: str | None = None,
    exclude_title_pattern: str | None = None,
    random_selection: bool = True,
) -> tuple[list[FeedEntry], dict[str, str]]:
    """Pick one FeedEntry (one format) per unique dataset, then sample N datasets.

    Only formats portolan-cli can actually ingest are ever selected (see
    ``preferred_formats``, e.g. GEOJSON/GPKG/SHAPE/FGDB) -- a dataset that is
    only available in an unsupported format (SOSI, PostGIS-dump, GML, ...) has
    no candidate entry and cannot be picked, since it would break step 7.

    Returns:
        (selected_entries, skip_reasons) where skip_reasons maps
        dataset_id -> human-readable reason it was excluded from the
        candidate pool (used for the final report).
    """
    include_re = re.compile(include_title_pattern, re.IGNORECASE) if include_title_pattern else None
    exclude_re = re.compile(exclude_title_pattern, re.IGNORECASE) if exclude_title_pattern else None

    preferred_upper = [f.upper() for f in preferred_formats]
    skip_reasons: dict[str, str] = {}
    candidates: list[FeedEntry] = []

    for dataset_id, entries in grouped.items():
        title_sample = entries[0].title
        if include_re and not any(include_re.search(e.title) for e in entries):
            skip_reasons[dataset_id] = f"title didn't match include pattern ({title_sample!r})"
            continue
        if exclude_re and any(exclude_re.search(e.title) for e in entries):
            skip_reasons[dataset_id] = f"title matched exclude pattern ({title_sample!r})"
            continue

        by_format = {e.format.upper(): e for e in entries}
        chosen: FeedEntry | None = None
        for fmt in preferred_upper:
            if fmt in by_format:
                chosen = by_format[fmt]
                break

        if chosen is None:
            available = sorted(by_format.keys())
            skip_reasons[dataset_id] = (
                f"no preferred/supported format available (has: {', '.join(available)})"
            )
            continue

        candidates.append(chosen)

    logger.info(
        "%d/%d datasets have a supported format; %d excluded",
        len(candidates),
        len(grouped),
        len(skip_reasons),
    )

    if len(candidates) <= sample_size:
        if len(candidates) < sample_size:
            logger.warning(
                "Only %d candidate datasets available, fewer than requested sample_size=%d",
                len(candidates),
                sample_size,
            )
        selected = candidates
    elif random_selection:
        rng = random.Random(random_seed)
        selected = rng.sample(candidates, sample_size)
    else:
        selected = candidates[:sample_size]

    return selected, skip_reasons
