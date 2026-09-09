# GeoNorge → Portolan PoC

> **This is a proof of concept, not production software.** It exists to
> demonstrate that a sample of datasets from GeoNorge's download service
> (Geonorge nedlastingstjeneste) can be crawled, downloaded, enriched with
> real ISO19115 metadata, and published as a [Portolan](https://portolan-sdi.org)
> STAC catalog (GeoParquet + PMTiles) — as an alternative/supplement to
> GeoNorge as an SDI. It is **not** a general-purpose GeoNorge harvester: the
> sample size is small by design, several nationwide datasets are excluded
> because they're too large for a quick local run, and the code favors
> "good enough to prove the point" over robustness. See
> [`geonorge-portolan-poc-plan.md`](geonorge-portolan-poc-plan.md) for the
> original design spec and [`REPORT.md`](REPORT.md) for the results and known
> limitations of the last run.

## What it does

A single pipeline (`geonorge-poc run`) does, in order:

1. Crawls GeoNorge's `Tjenestefeed_daglig.xml` (a feed-of-feeds: one entry per
   dataset/format combination).
2. Picks a configurable sample of datasets (default 20), one format per
   dataset, preferring formats GDAL/portolan can both handle.
3. Crawls each selected dataset's own Atom feed to find an actual
   downloadable file (preferring the nationwide/"landsdekkende" extent).
4. Fetches full ISO19115 metadata per dataset via GeoNorge's CSW
   `GetRecordById` endpoint (title, abstract, license, contact/organisation).
5. Downloads the file and normalizes it to GeoPackage with `ogr2ogr` (see
   "Known quirks" below for why this normalization step exists).
6. Looks up GeoNorge's `tegneregler` (cartography) register for an
   authoritative style, falling back to Portolan's auto-generated default
   style when none is found.
7. Writes a Portolan `metadata.yaml` per collection from the CSW metadata.
8. Runs `portolan add` / `check --fix` / `add` per collection (with
   `--pmtiles` when `pmtiles.enabled` in `config.yaml`, generating a PMTiles
   visualization asset + default MapLibre style per collection), then
   `portolan readme` and `portolan check --strict` on the whole catalog.
9. Fills in each collection's (and the catalog's own) `AGENTS.md` — see
   "AGENTS.md generation" below.
10. Writes `REPORT.md` summarizing what succeeded/failed and why.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) (this project is uv-managed; don't use
  bare `pip`/`python`).
- `ogr2ogr` (GDAL) on `PATH` — used to normalize every downloaded format to
  GeoPackage before portolan ever sees it. Tested against GDAL 3.12.
- `tippecanoe` on `PATH` — used by `portolan add --pmtiles` to build the
  PMTiles visualization asset. `brew install tippecanoe` (macOS) or
  `apt install tippecanoe` (Ubuntu). Only needed if `pmtiles.enabled: true`
  in `config.yaml` (the default); set it to `false` to skip PMTiles entirely
  and drop this dependency.
- Everything else (`portolan-cli`, `lxml`, `rapidfuzz`, ...) is declared in
  `pyproject.toml` and installed automatically by `uv run`/`uv sync`.

## Running it

```bash
uv sync            # first time only; creates .venv from pyproject.toml/uv.lock
uv run geonorge-poc run
```

That's it — it reads `config.yaml` from the project root, writes cached raw
XML to `cache/`, and builds the catalog in `catalog/`. Useful flags:

```bash
uv run geonorge-poc -v run                  # -v (before the subcommand) turns on debug logging
uv run geonorge-poc run --sample-size 5     # override sample.size from config.yaml for a quick test
uv run geonorge-poc run --refresh-feed      # ignore the cached tjenestefeed.xml, re-download it
uv run geonorge-poc run --report OTHER.md   # write the run report somewhere other than REPORT.md
```

`catalog/` and `cache/` are gitignored — they're regenerable build output
(the catalog alone is several GB of downloaded/converted geodata), not
source. Nothing about this pipeline needs to be committed to reproduce the
result; re-running `geonorge-poc run` rebuilds it from scratch.

### Resuming an interrupted run

Downloading and converting ~20 nationwide datasets takes a while (some
FGDB→GeoPackage conversions alone take 10+ minutes), and on a memory-
constrained machine the whole process can get killed partway through. This
is expected and handled: **just re-run `uv run geonorge-poc run` again.**
Before (re-)processing a dataset, the pipeline checks whether
`catalog/<collection>/` already has both a `.gpkg` file and a
`collection.json` from a previous run, and skips straight past it if so —
so a resume only does new work, it never redownloads or reconverts a
collection that already succeeded. If a dataset was mid-download/-convert
when the process died, delete just that one partial `catalog/<collection>/`
directory before resuming (a partial directory is missing either the
`.gpkg` or the `collection.json`, so it's easy to spot):

```bash
rm -rf catalog/<collection-that-was-mid-flight>
uv run geonorge-poc run
```

### Doing a fresh run from scratch

```bash
rm -rf catalog cache
uv run geonorge-poc run
```

Since `sample.random_seed` is fixed in `config.yaml`, re-running against an
unchanged `tjenestefeed.xml` selects the same sample deterministically —
useful for reproducing a specific report. The candidate pool (and therefore
which datasets a given seed picks) does shift if you change
`preferred_formats` or the exclude/include title patterns, or if GeoNorge's
feed content changes between runs.

## Configuration (`config.yaml`)

All pipeline behavior is controlled by `config.yaml` in the project root —
no code changes needed for a different sample:

| Key | Meaning |
|---|---|
| `feed_url` | The GeoNorge Tjenestefeed URL. |
| `sample.size` | How many datasets to select (plan recommends 15-30 for a PoC). |
| `sample.preferred_formats` | Format priority when a dataset offers several (only formats GDAL/portolan can both read are usable at all — see below). |
| `sample.prefer_national_extent` | Prefer the "hele landet"/nationwide file over per-county splits. |
| `sample.random_seed` / `sample.random_selection` | Reproducible random sampling, or set `random_selection: false` to just take the first N candidates. |
| `sample.exclude_title_pattern` / `include_title_pattern` | Regex filters on dataset title (e.g. to skip yearly "historiske data" reissues, or datasets known to be too large — see below). |
| `paths.cache_dir` / `paths.catalog_dir` | Where raw feed/CSW XML is cached and where the catalog is built. |
| `styling.*` | Tune/disable the `tegneregler` cartography lookup and its fuzzy-match threshold. |
| `portolan.*` | Catalog id/title/description/license and `portolan check --fix` worker count. |
| `pmtiles.enabled` | Generate a PMTiles visualization asset per collection with `portolan add --pmtiles` (requires `tippecanoe`). |
| `pmtiles.max_zoom` | Caps tippecanoe's zoom range catalog-wide (set once via `portolan config set pmtiles.max_zoom`) to bound build time/output size on nationwide datasets; `null` lets tippecanoe auto-detect. |

To do a smaller/larger or differently-filtered run, edit `config.yaml` (or
pass `--sample-size` for a one-off override) rather than changing code.

## AGENTS.md generation

`portolan init`/`add` only ever write a placeholder `AGENTS.md` — section
headers with HTML-comment prompts ("Replace the prompts below with real
content"), meant for a human to fill in by hand. This pipeline fills that
skeleton in automatically, once per run, for every collection and for the
catalog root, from `collection.json`/`catalog.json` (the STAC fields
Portolan itself already computed: schema, bbox, feature count, license,
registered assets) plus each collection's `.portolan/metadata.yaml` (the
human-authored enrichment — title, description, contact, source URL,
processing notes).

This is deliberately **template-based, not LLM-generated**: no model call,
no extra data-profiling pass over the actual features. It produces the
mechanical sections reliably (schema table, DuckDB/geopandas snippets
using the real filenames and columns, license/CRS/extent facts, a plain
row-count/bbox query and a "check whether this column is coded" query
templated off the schema) but does *not* attempt the kind of domain-level
narrative (decoded categorical values, cross-collection join keys, dataset
provenance nuance) that requires either manual authoring or feeding a
schema profile through an LLM — see `IMPROVEMENTS.md` for that
alternative design and why it was intentionally not built here. See
`agents_md.py`'s module docstring for the reasoning in full.

## Known quirks discovered during implementation

These are documented here because they're non-obvious and future runs will
hit them again — see `REPORT.md` for the full list and `convert_gpkg.py`'s
module docstring for the code-level detail:

- **portolan-cli 0.8.0 has no GML/SOSI/PostGIS-dump support at all.** The
  sample can only be drawn from GEOJSON/GPKG/SHAPE/FGDB — the plan's
  original preference for GML had to be dropped once this was verified
  against `portolan_cli`'s extension registry.
- **Every downloaded file is normalized to GeoPackage with `ogr2ogr` before
  `portolan add` ever sees it**, because (a) portolan-cli 0.8.0's cloud-native
  conversion pass silently skips FileGDB (`.gdb`) inputs, and (b) GeoNorge's
  GeoJSON exports have a UTF-8 BOM that breaks portolan's JSON parser. GDAL
  handles both without issue.
- **Three nationwide "Matrikkelen" FGDB datasets are excluded by title**
  (`Bygningspunkt`, `Eiendomskart Teig` — see `config.yaml`'s
  `exclude_title_pattern`): each has tens of millions of features nationwide
  with no per-county split available, and blew past `ogr2ogr`'s 900s
  conversion timeout in testing. If you add more excludes for the same
  reason, extend that same regex.
- **GeoNorge's `tegneregler` cartography register is almost entirely PDF
  documentation for humans**, not machine-readable SLD/QML. Expect most
  collections to fall back to Portolan's auto-generated default style; this
  is the explicit, intended fallback, not a bug.
- **A dataset that fails download/conversion doesn't stop the run** — it's
  logged in `REPORT.md` under "Feilede/hoppet over datasett" and the run
  continues with the rest of the sample.

## Project layout

```
config.yaml                  # sample size, filters, catalog output path — edit this to change a run
src/geonorge_portolan_poc/
    feed.py                  # steg 1: crawl the level-1 Tjenestefeed
    sample.py                # steg 2: pick the sample
    dataset_feed.py          # steg 3: crawl each dataset's own level-2 Atom feed
    csw_metadata.py          # steg 4: fetch + parse ISO19115 via CSW
    download.py              # steg 5: stream the chosen file to disk
    convert_gpkg.py          # normalize downloaded formats to GeoPackage
    styling.py                # steg 5b: tegneregler lookup + fuzzy match
    metadata_yaml.py          # steg 6: build Portolan metadata.yaml
    portolan_runner.py         # steg 7: subprocess wrapper around portolan-cli
    agents_md.py                # steg 7c: fill AGENTS.md from collection.json + metadata.yaml
    pipeline.py                # orchestrates steg 1-9, resumable
    report.py                  # writes REPORT.md
    cli.py                      # `geonorge-poc run` entrypoint
cache/                       # gitignored: cached raw feed/CSW XML + tegneregler registry
catalog/                     # gitignored: the actual Portolan catalog (build output)
REPORT.md                    # results + known limitations from the last run
```
