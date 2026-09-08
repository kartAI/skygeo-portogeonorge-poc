# Add support for PMTiles output for each dataset
- tippecanoe vs planetiler?
- performance issues?

# Add support for autogenerating AGENTS.md for each dataset
- use the metadata to generate llm instructions
- Piloted manually across all 28 collections (2026-09-06): grounding the write-up in real
  DuckDB inspection (not just the README's bare column list) is what made the content
  trustworthy — it's what caught coded/categorical fields, sentinel values, and a
  cross-collection join key, rather than guessing from field names alone. Any automation
  needs to preserve that grounding step, not just pipe metadata.yaml into an LLM.

## Proposed design

1. **Schema-profiling step** (new `profile_schema.py`, runs after `portolan add`, before
   `portolan readme`): for each collection's per-layer parquet files, use `duckdb` — already
   a transitive dependency via `portolan-cli`/`geoparquet-io`, no new dep needed — to compute:
   - per-column distinct-value count, and the value list+counts when count <= ~20 (this is
     what surfaces coded/categorical fields like `avgrensningstype`, `status`,
     `stoysonekategori` instead of leaving them as opaque `string`/`int32` in the schema table)
   - min/max for numeric and date/timestamp columns
   - geometry type and CRS (`ST_GeometryType`, `proj:code`)
   - row/feature count per layer
   Write this to `.portolan/schema_profile.json` per collection, keyed by the same
   `schema_fingerprint` already tracked in `versions.json` — lets AGENTS.md regeneration key
   off "did the schema actually change" the same way the pipeline already resumes.
2. **Default generation path: Anthropic Messages API called directly from the pipeline**
   (a Python `anthropic` call in a new `agents_md.py` step, not shelling out to the `claude`
   CLI). Prompt = abstract + license + source + the schema profile from step 1 + the AGENTS.md
   skeleton's section headers. Deterministic-enough, cheap, and fits the existing
   `pipeline.py` step/resume structure. Model choice: cheaper model (e.g. Haiku) is probably
   fine for the mechanical "Accessing the data"/schema-table sections; consider a stronger
   model for "Overview"/"Data quality"/"Example queries" since those need actual domain
   judgment.
3. **Optional `--deep-research` flag: full agentic generation** (claude-cli headless with
   Bash+WebSearch tool access, or the Agent SDK) for collections where it's worth the cost —
   this is what caught the byte-identical asset-duplication bug (via `ogrinfo`/checksum
   comparisons the agent chose to run) and the real SEFRAK/Askeladden relationship (via
   targeted WebSearch), neither of which the schema profile alone would reveal. Not the
   default for a 28-collection run: slower, non-deterministic, and the domain-research part
   doesn't cheaply generalize.
   - Ollama is a reasonable fallback for cost/privacy on the mechanical sections, but avoid it
     for the narrative/domain sections — that's exactly where a weaker model is most likely to
     hallucinate meanings for Norwegian SOSI-specific field names and codes.
4. **Post-generation lint** (cheap, always on): fail/warn in `REPORT.md` if a generated
   AGENTS.md still contains the skeleton's HTML-comment placeholders, or references a filename
   that doesn't exist in that collection's directory — catches incomplete generation and
   filename/field hallucination without needing another LLM call.
5. **Known related bug to fix regardless of the above**: several collections' unsuffixed
   `<id>.parquet`/`<id>.gpkg` "primary" asset is currently a byte-identical duplicate of one
   arbitrary sub-layer rather than a merge (same class of bug as commit `7ec2a1c`, apparently
   not fully fixed — seen in `n1000`, `n2000-kartdata`, `n250`,
   `lokaliteter-enkeltminner-sikringssoner`, `militere-forbudsomrader-sjo`,
   `stoysoner-forsvarets-flyplasser`, `steinsprang-aktsomhetsomr`, `tur-og-friluftsruter`).
   Any schema-profiling step should profile the primary asset too so this stays visible in
   the generated docs until it's fixed at the source.
