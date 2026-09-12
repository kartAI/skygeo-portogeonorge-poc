#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

# Base (finest) A5 aggregate level
gpio process aggregate a5 sefrak-bygninger.parquet sefrak-bygninger_a5.parquet \ 
  --auto --target-per-cell 100 --out-geometry polygon

# Coarser A5 overview levels, built as siblings alongside the base aggregate
# (auto-selected against the tile-size budget; pass --levels e.g. "3,5" to pin them explicitly)
gpio process overview sefrak-bygninger_a5.parquet --levels 3,5

# Pyramid detects the base level + overview siblings, bands each to a zoom range,
# and appends the original building features as the final (highest-zoom) band
gpio pmtiles pyramid sefrak-bygninger_a5.parquet sefrak-bygninger.pmtiles \
  --include-features --features-source sefrak-bygninger.parquet \
  --max-zoom 9
