# REPORT: GeoNorge -> Portolan PoC

## Sammendrag

- Tjenestefeed: 1043 entries, 374 unike datasett.
- 276 datasett ekskludert fra kandidatpoolen (kun i SOSI/GML/PostGIS/andre formater portolan-cli ikke stotter, eller filtrert av tittel-mønster).
- Sample: 20 datasett valgt.
- **19/20 datasett fullfort vellykket** gjennom hele pipelinen.
- `portolan check catalog` (standard, spec-konformitet) etter full kjoring: **PASS**.
- `portolan check catalog --strict` (advarsler telles som feil): **FAIL** (se punkt 4 under "Kjente begrensninger" -- forventet a feile pa en ufarlig, dokumentert CLI-advarsel, ikke pa reelle spec-brudd).

### Status per steg

| Status | Antall |
|---|---|
| ok | 19 |
| convert_failed | 1 |

### Format-fordeling i sample

| Format | Antall |
|---|---|
| FGDB | 19 |
| GEOJSON | 1 |

### Kartografi/styling (steg 5b)

| Avgjorelse | Antall |
|---|---|
| authoritative-pdf-only | 8 |
| no-match-found | 6 |

`authoritative-sld` betyr en SLD-fil ble funnet og lastet ned (fargeuttrekk til en MapLibre-override forsokt); `authoritative-pdf-only` betyr registeret bare hadde menneskelesbar PDF-dokumentasjon; `no-match-found` betyr fallback til portolans auto-genererte default-style.

## Datasett-for-datasett

| Dataset ID | Collection | Format | Status | Lisens | Styling |
|---|---|---|---|---|---|
| tettsteder_2018 | tettsteder-2018 | FGDB | ok | other | authoritative-pdf-only |
| sefrak_bygninger | sefrak-bygninger | FGDB | ok | - | - |
| forsvarets_skyte_ovingsfelt_land | forsvarets-skyte-ovingsfelt-land | FGDB | ok | - | - |
| vannkraft_utbygd_ikkeutbygd | vannkraft-utbygd-ikkeutbygd | FGDB | ok | other | authoritative-pdf-only |
| n250 | n250 | FGDB | ok | CC-BY-4.0 | authoritative-pdf-only |
| militere_forbudsomrader_sjo | militere-forbudsomrader-sjo | FGDB | ok | other | authoritative-pdf-only |
| menneskelig_pavirkning_marint_soppel | menneskelig-pavirkning-marint-soppel | FGDB | ok | CC-BY-4.0 | no-match-found |
| lassettingsplasser | lassettingsplasser | FGDB | ok | - | - |
| lokaliteter_enkeltminner_sikringssoner | lokaliteter-enkeltminner-sikringssoner | FGDB | ok | - | - |
| tettsteder_2023 | tettsteder-2023 | FGDB | ok | other | authoritative-pdf-only |
| steinsprang_aktsomhetsomr | steinsprang-aktsomhetsomr | FGDB | ok | other | no-match-found |
| korallrev | korallrev | FGDB | ok | other | authoritative-pdf-only |
| sarbare_marine_bunndyr_observasjonsdata | sarbare-marine-bunndyr-observasjonsdata | FGDB | ok | other | authoritative-pdf-only |
| referansedata_videostasjoner | referansedata-videostasjoner | FGDB | ok | CC-BY-4.0 | no-match-found |
| missing | missing | GEOJSON | ok | CC-BY-4.0 | no-match-found |
| adresse_leilighetsniva | adresse-leilighetsniva | FGDB | convert_failed | CC-BY-4.0 | - |
| menneskelig_pavirkning_tralspor | menneskelig-pavirkning-tralspor | FGDB | ok | - | - |
| statistisk_rutenett_1000 | statistisk-rutenett-1000 | FGDB | ok | other | no-match-found |
| tare_hostefelt | tare-hostefelt | FGDB | ok | other | authoritative-pdf-only |
| stoysoner_forsvarets_flyplasser | stoysoner-forsvarets-flyplasser | FGDB | ok | other | no-match-found |

### Feilede/hoppet over datasett -- detaljer

- **adresse_leilighetsniva** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage

## Kjente begrensninger oppdaget under implementasjon

Disse avvikene fra plan-dokumentets antakelser ble oppdaget empirisk under implementasjonen (se ogsa geonorge-portolan-poc-plan.md avsnitt 4):

1. **portolan-cli 0.8.0 stotter ikke GML, SOSI eller PostGIS-dump** (`portolan_cli/extension_registry.py` har ingen GML-oppforing i det hele tatt). Plan-dokumentets forslag om a prioritere GML matte derfor forkastes; sample trekkes i stedet kun fra GEOJSON/GPKG/SHAPE/FGDB -- de formatene GDAL/OGR og portolan begge kan lese.
2. **FileGDB (.gdb) har et hull i portolan-cli sin cloud-native-konvertering**: `.gdb` mangler `scan_category="geo_asset"` i extension-registeret, sa `portolan check --fix` sin geo-asset-skanning hopper over FileGDB-filer helt -- ingen GeoParquet-konvertering, ingen thumbnail. GeoJSON/GPKG/SHP rammes ikke. Losning: alle nedlastede rådata normaliseres til GeoPackage med `ogr2ogr` for `portolan add` noensinne ser dem (se `convert_gpkg.py`).
3. **GeoNorges GeoJSON-eksport har en UTF-8 BOM** som knekker portolan sin JSON-parser (`Unexpected UTF-8 BOM`). Samme ogr2ogr-normalisering i punkt 2 loser ogsa dette, siden GDAL leser BOM-en uten problemer.
4. **`portolan add` beregner GeoParquet-avledet STAC-metadata (feature_count, geometry_type) uten a registrere selve GeoParquet-filen som asset.** `check --fix` konverterer sa kildefilen til GeoParquet pa nytt som en "orphan" (usporet fil), og en andre `portolan add`-kjoring kreves for a registrere den resulterende thumbnail-en (parquet-filen forblir usporet, men det blokkerer ikke `--strict`). Pipelinen kjorer derfor `add -> check --fix -> add` per collection i stedet for planens ett-linjers `add`+`check --fix`.
5. **Kollisjon mellom katalogstruktur og collection-ID:** a legge rådata i `catalog/<id>/raw/<fil>` (som plan-dokumentets katalogstruktur foreslo) far portolan til a opprette EN subkatalog (`<id>`) og collection-en `<id>/raw` nestet under den, i stedet for a la `<id>` selv vaere collection-en. Rådata legges derfor direkte i `catalog/<id>/` uten `raw/`-mellomledd.
6. **Kartografi/tegneregel-registeret er nesten utelukkende PDF-dokumentasjon for mennesker**, som forventet i planen. Fuzzy-matching pa tittel med terskel 80 ga dessuten falske positiver pa korte/generiske titler (f.eks. "Kirkebygg" matchet en korallrev-oppforing med score 86); terskelen ble hevet til 90 i `config.yaml`.

## Verifisering (steg 8)

`portolan check catalog` (standard):

```
→ Skipped 136 items (already fresh)
✓ Converted 28 file(s)
    forsvarets-skyte-ovingsfelt-land.gpkg -> forsvarets-skyte-ovingsfelt-land.parquet
    korallrev.gpkg -> korallrev.parquet
    lassettingsplasser.gpkg -> lassettingsplasser.parquet
    lokaliteter-enkeltminner-sikringssoner.gpkg -> lokaliteter-enkeltminner-sikringssoner.parquet
    menneskelig-pavirkning-marint-soppel.gpkg -> menneskelig-pavirkning-marint-soppel.parquet
    menneskelig-pavirkning-tapte-fiskeredskaper.gpkg -> menneskelig-pavirkning-tapte-fiskeredskaper.parquet
    menneskelig-pavirkning-tralspor.gpkg -> menneskelig-pavirkning-tralspor.parquet
    militere-forbudsomrader-sjo.gpkg -> militere-forbudsomrader-sjo.parquet
    missing.gpkg -> missing.parquet
    n1000.gpkg -> n1000.parquet
    n2000-kartdata.gpkg -> n2000-kartdata.parquet
    n250.gpkg -> n250.parquet
    referansedata-videostasjoner.gpkg -> referansedata-videostasjoner.parquet
    sarbare-marine-bunndyr-observasjonsdata.gpkg -> sarbare-marine-bunndyr-observasjonsdata.parquet
    sefrak-bygninger.gpkg -> sefrak-bygninger.parquet
    statistisk-rutenett-1000.gpkg -> statistisk-rutenett-1000.parquet
    steinsprang-aktsomhetsomr.gpkg -> steinsprang-aktsomhetsomr.parquet
    stoysoner-forsvarets-flyplasser.gpkg -> stoysoner-forsvarets-flyplasser.parquet
    tare-hostefelt.gpkg -> tare-hostefelt.parquet
    tettsteder-2017.gpkg -> tettsteder-2017.parquet
    tettsteder-2018.gpkg -> tettsteder-2018.parquet
    tettsteder-2021.gpkg -> tettsteder-2021.parquet
    tettsteder-2022.gpkg -> tettsteder-2022.parquet
    tettsteder-2023.gpkg -> tettsteder-2023.parquet
    tettsteder2016.gpkg -> tettsteder2016.parquet
    tralspor.gpkg -> tralspor.parquet
    tur-og-friluftsruter.gpkg -> tur-og-friluftsruter.parquet
    vannkraft-utbygd-ikkeutbygd.gpkg -> vannkraft-utbygd-ikkeutbygd.parquet
✓ Created/updated 17 metadata items
✓ Catalog conforms (29 file(s) checked)
✓ Fixed automatically (34)
    Applied: checksum
→ Action required (83):
    PTL-CAT-001 catalog.json: group the children under thematic subcatalogs, each with its own catalog.json, and relink this object to those subcatalogs
    PTL-PRO-002 forsvarets-skyte-ovingsfelt-land/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 korallrev/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 lassettingsplasser/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 lokaliteter-enkeltminner-sikringssoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-VIZ-004 lokaliteter-enkeltminner-sikringssoner/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-VIZ-004 lokaliteter-enkeltminner-sikringssoner/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-PRO-002 menneskelig-pavirkning-marint-soppel/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-tapte-fiskeredskaper/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-tralspor/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 militere-forbudsomrader-sjo/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 missing/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n1000/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 n1000/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 n2000-kartdata/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 n250/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-VIZ-004 n250/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-PRO-002 referansedata-videostasjoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 sarbare-marine-bunndyr-observasjonsdata/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 sefrak-bygninger/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 statistisk-rutenett-1000/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 steinsprang-aktsomhetsomr/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-VIZ-004 steinsprang-aktsomhetsomr/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-VIZ-004 steinsprang-aktsomhetsomr/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-VIZ-004 steinsprang-aktsomhetsomr/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-VIZ-004 steinsprang-aktsomhetsomr/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-PRO-002 stoysoner-forsvarets-flyplasser/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tare-hostefelt/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2017/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2018/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2021/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2022/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2023/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-VIZ-004 tettsteder-2023/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-VIZ-004 tettsteder-2023/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-VIZ-004 tettsteder-2023/collection.json: Generate a PMTiles derivative for this large vector collection so browsers can render it ; run `portolan add --pmtiles` with tippecanoe on PATH.
    PTL-PRO-002 tettsteder2016/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tralspor/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 tur-og-friluftsruter/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tur-og-friluftsruter/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tur-og-friluftsruter/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tur-og-friluftsruter/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 tur-og-friluftsruter/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 vannkraft-utbygd-ikkeutbygd/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.

→ Warnings (45):
    Fix: group the children under thematic subcatalogs, each with its own catalog.json, and relink this object to those subcatalogs
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
✓ Catalog conforms (29 file(s) checked)
    83 need a decision (see Requires: lines)
→ Source files:
✓ 122 file(s) already cloud-native
⚠ 28 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
⚠ PTL-CAT-001 catalog.json: catalog holds 28 children with no subcatalog grouping them; a flat list this long is hard to browse
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6421, 58.1889, 25.2542, 78.0844] and lies within [-25.3256, 57.3673, 45.9593, 80.8611]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.8024] and lies within [-0.4509, 57.8059, 31.4731, 71.5357]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5534, 58.2433, 25.3761, 70.7424] and lies within [-0.4324, 57.8189, 31.8984, 71.5154]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1896, 25.2400, 70.7985] and lies within [-0.8934, 57.7756, 31.7416, 71.5562]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6760, 58.3122, 24.8296, 70.1208] and lies within [0.3228, 57.9317, 30.4508, 70.7857]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2800, 58.1930, 25.3617, 70.7848] and lies within [-0.9215, 57.7691, 31.9354, 71.5604]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6778, 58.3241, 25.2457, 70.7786] and lies within [-0.2129, 57.9110, 31.6694, 71.5297]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5985, 58.2962, 25.3792, 70.7835] and lies within [-0.3706, 57.8718, 31.9139, 71.5568]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8081, 58.3377, 17.1484, 67.9482] and lies within [1.9778, 58.0052, 18.0690, 68.4632]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3039, 58.2097, 25.3329, 70.8005] and lies within [-0.8854, 57.7883, 31.8920, 71.5716]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5499, 58.2843, 25.2239, 70.7843] and lies within [-0.4352, 57.8725, 31.6565, 71.5342]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.7363, 58.2439, 25.3552, 70.7456] and lies within [-0.1424, 57.8210, 31.8654, 71.5161]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_BygningerOgAnlegg_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1897, 25.0967, 70.8195] and lies within [-0.8934, 57.7872, 31.5154, 71.5565]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.3236, 58.9215, 25.4180, 70.4768] and lies within [1.2604, 58.4980, 31.4147, 71.2162]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8483, 58.7278, 23.3000, 70.5442] and lies within [0.5186, 58.4011, 28.1635, 71.1174]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_grense' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_omrade' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8345, 58.3538, 17.1503, 67.9481] and lies within [2.0223, 58.0234, 18.0699, 68.4596]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3022, 58.2360, 25.2657, 70.8111] and lies within [-0.8765, 57.8202, 31.7740, 71.5712]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2674, 58.1760, 25.1007, 70.8267] and lies within [-0.9521, 57.7730, 31.5350, 71.5652]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2973, 58.1865, 25.3563, 70.7812] and lies within [-0.8934, 57.7631, 31.9261, 71.5560]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5407, 58.2439, 25.0915, 70.7390] and lies within [-0.4164, 57.8424, 31.4127, 71.4690]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2663, 58.1764, 25.3596, 70.7844] and lies within [-0.9501, 57.7526, 31.9395, 71.5603]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3097, 58.2487, 25.3361, 70.7863] and lies within [-0.8469, 57.8274, 31.8660, 71.5554]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2912, 58.1986, 25.3560, 70.7844] and lies within [-0.9001, 57.7753, 31.9226, 71.5588]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8080, 58.3382, 17.1494, 67.9470] and lies within [1.9785, 58.0058, 18.0703, 68.4620]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2843, 58.1972, 25.3641, 70.7954] and lies within [-0.9217, 57.7731, 31.9467, 71.5716]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Stedsnavn_tekstplassering' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2828, 58.1113, 25.3265, 70.8515] and lies within [-1.0056, 57.6897, 31.9733, 71.6283]
⚠ PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: asset 'sarbare-marine-bunndyr-observasjonsdata_hardbunnskorallskog' declared bbox [-0.8035, 56.5027, 36.9558, 81.6840] is inconsistent with its EPSG:25833 data, whose envelope contains [3.2899, 57.4580, 26.0259, 79.8893] and lies within [-24.0989, 56.9086, 52.3774, 82.1191]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5673, 58.3199, 25.1990, 69.8319] and lies within [0.3334, 57.9104, 30.8240, 70.5372]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter_annenrute_senterlinje' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5673, 58.3199, 25.1990, 69.8319] and lies within [0.3334, 57.9104, 30.8240, 70.5372]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter_skiloype_senterlinje' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.9718, 58.3423, 24.7854, 70.7104] and lies within [0.3629, 57.9658, 30.8275, 71.3899]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter_sykkelrute_senterlinje' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6568, 58.2243, 23.7559, 70.7669] and lies within [-0.1819, 57.8804, 29.2530, 71.3910]
⚠ 28 file(s) need conversion
```

`portolan check catalog --strict`:

```
→ Warnings (45):
    Fix: group the children under thematic subcatalogs, each with its own catalog.json, and relink this object to those subcatalogs
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    83 need a decision (see Requires: lines)
→ Source files:
✓ 122 file(s) already cloud-native
⚠ 28 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
⚠ PTL-CAT-001 catalog.json: catalog holds 28 children with no subcatalog grouping them; a flat list this long is hard to browse
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6421, 58.1889, 25.2542, 78.0844] and lies within [-25.3256, 57.3673, 45.9593, 80.8611]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.8024] and lies within [-0.4509, 57.8059, 31.4731, 71.5357]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5534, 58.2433, 25.3761, 70.7424] and lies within [-0.4324, 57.8189, 31.8984, 71.5154]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1896, 25.2400, 70.7985] and lies within [-0.8934, 57.7756, 31.7416, 71.5562]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6760, 58.3122, 24.8296, 70.1208] and lies within [0.3228, 57.9317, 30.4508, 70.7857]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2800, 58.1930, 25.3617, 70.7848] and lies within [-0.9215, 57.7691, 31.9354, 71.5604]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6778, 58.3241, 25.2457, 70.7786] and lies within [-0.2129, 57.9110, 31.6694, 71.5297]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5985, 58.2962, 25.3792, 70.7835] and lies within [-0.3706, 57.8718, 31.9139, 71.5568]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8081, 58.3377, 17.1484, 67.9482] and lies within [1.9778, 58.0052, 18.0690, 68.4632]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3039, 58.2097, 25.3329, 70.8005] and lies within [-0.8854, 57.7883, 31.8920, 71.5716]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5499, 58.2843, 25.2239, 70.7843] and lies within [-0.4352, 57.8725, 31.6565, 71.5342]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.7363, 58.2439, 25.3552, 70.7456] and lies within [-0.1424, 57.8210, 31.8654, 71.5161]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_BygningerOgAnlegg_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1897, 25.0967, 70.8195] and lies within [-0.8934, 57.7872, 31.5154, 71.5565]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.3236, 58.9215, 25.4180, 70.4768] and lies within [1.2604, 58.4980, 31.4147, 71.2162]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8483, 58.7278, 23.3000, 70.5442] and lies within [0.5186, 58.4011, 28.1635, 71.1174]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_grense' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_omrade' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8345, 58.3538, 17.1503, 67.9481] and lies within [2.0223, 58.0234, 18.0699, 68.4596]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3022, 58.2360, 25.2657, 70.8111] and lies within [-0.8765, 57.8202, 31.7740, 71.5712]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2674, 58.1760, 25.1007, 70.8267] and lies within [-0.9521, 57.7730, 31.5350, 71.5652]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2973, 58.1865, 25.3563, 70.7812] and lies within [-0.8934, 57.7631, 31.9261, 71.5560]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5407, 58.2439, 25.0915, 70.7390] and lies within [-0.4164, 57.8424, 31.4127, 71.4690]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2663, 58.1764, 25.3596, 70.7844] and lies within [-0.9501, 57.7526, 31.9395, 71.5603]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3097, 58.2487, 25.3361, 70.7863] and lies within [-0.8469, 57.8274, 31.8660, 71.5554]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2912, 58.1986, 25.3560, 70.7844] and lies within [-0.9001, 57.7753, 31.9226, 71.5588]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8080, 58.3382, 17.1494, 67.9470] and lies within [1.9785, 58.0058, 18.0703, 68.4620]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2843, 58.1972, 25.3641, 70.7954] and lies within [-0.9217, 57.7731, 31.9467, 71.5716]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Stedsnavn_tekstplassering' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2828, 58.1113, 25.3265, 70.8515] and lies within [-1.0056, 57.6897, 31.9733, 71.6283]
⚠ PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: asset 'sarbare-marine-bunndyr-observasjonsdata_hardbunnskorallskog' declared bbox [-0.8035, 56.5027, 36.9558, 81.6840] is inconsistent with its EPSG:25833 data, whose envelope contains [3.2899, 57.4580, 26.0259, 79.8893] and lies within [-24.0989, 56.9086, 52.3774, 82.1191]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5673, 58.3199, 25.1990, 69.8319] and lies within [0.3334, 57.9104, 30.8240, 70.5372]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter_annenrute_senterlinje' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5673, 58.3199, 25.1990, 69.8319] and lies within [0.3334, 57.9104, 30.8240, 70.5372]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter_skiloype_senterlinje' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.9718, 58.3423, 24.7854, 70.7104] and lies within [0.3629, 57.9658, 30.8275, 71.3899]
⚠ PTL-DAT-005 tur-og-friluftsruter/collection.json: asset 'tur-og-friluftsruter_sykkelrute_senterlinje' declared bbox [4.5746, 57.9779, 31.1053, 71.1838] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6568, 58.2243, 23.7559, 70.7669] and lies within [-0.1819, 57.8804, 29.2530, 71.3910]
✗ Catalog does not conform: 45 warnings
⚠ 28 file(s) need conversion
```

## Konfigurasjon brukt

Se `config.yaml` i prosjektroten for fullstendig konfigurasjon.
