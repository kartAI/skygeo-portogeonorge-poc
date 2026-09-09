# REPORT: GeoNorge -> Portolan PoC

## Sammendrag

- Tjenestefeed: 1043 entries, 374 unike datasett.
- 276 datasett ekskludert fra kandidatpoolen (kun i SOSI/GML/PostGIS/andre formater portolan-cli ikke stotter, eller filtrert av tittel-mønster).
- Sample: 20 datasett valgt.
- **4/20 datasett fullfort vellykket** gjennom hele pipelinen.
- `portolan check catalog` (standard, spec-konformitet) etter full kjoring: **FAIL**.
- `portolan check catalog --strict` (advarsler telles som feil): **FAIL** (se punkt 4 under "Kjente begrensninger" -- forventet a feile pa en ufarlig, dokumentert CLI-advarsel, ikke pa reelle spec-brudd).

### Status per steg

| Status | Antall |
|---|---|
| portolan_add_failed | 14 |
| ok | 4 |
| convert_failed | 2 |

### Format-fordeling i sample

| Format | Antall |
|---|---|
| FGDB | 19 |
| GEOJSON | 1 |

### Kartografi/styling (steg 5b)

| Avgjorelse | Antall |
|---|---|
| authoritative-pdf-only | 11 |
| no-match-found | 7 |

`authoritative-sld` betyr en SLD-fil ble funnet og lastet ned (fargeuttrekk til en MapLibre-override forsokt); `authoritative-pdf-only` betyr registeret bare hadde menneskelesbar PDF-dokumentasjon; `no-match-found` betyr fallback til portolans auto-genererte default-style.

## Datasett-for-datasett

| Dataset ID | Collection | Format | Status | Lisens | Styling |
|---|---|---|---|---|---|
| tettsteder_2018 | tettsteder-2018 | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| sefrak_bygninger | sefrak-bygninger | FGDB | ok | other | authoritative-pdf-only |
| forsvarets_skyte_ovingsfelt_land | forsvarets-skyte-ovingsfelt-land | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| vannkraft_utbygd_ikkeutbygd | vannkraft-utbygd-ikkeutbygd | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| n250 | n250 | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| militere_forbudsomrader_sjo | militere-forbudsomrader-sjo | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| menneskelig_pavirkning_marint_soppel | menneskelig-pavirkning-marint-soppel | FGDB | portolan_add_failed | CC-BY-4.0 | no-match-found |
| lassettingsplasser | lassettingsplasser | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| lokaliteter_enkeltminner_sikringssoner | lokaliteter-enkeltminner-sikringssoner | FGDB | portolan_add_failed | other | no-match-found |
| tettsteder_2023 | tettsteder-2023 | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| steinsprang_aktsomhetsomr | steinsprang-aktsomhetsomr | FGDB | convert_failed | other | - |
| korallrev | korallrev | FGDB | ok | other | authoritative-pdf-only |
| sarbare_marine_bunndyr_observasjonsdata | sarbare-marine-bunndyr-observasjonsdata | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| referansedata_videostasjoner | referansedata-videostasjoner | FGDB | ok | CC-BY-4.0 | no-match-found |
| missing | missing | GEOJSON | portolan_add_failed | CC-BY-4.0 | no-match-found |
| adresse_leilighetsniva | adresse-leilighetsniva | FGDB | convert_failed | CC-BY-4.0 | - |
| menneskelig_pavirkning_tralspor | menneskelig-pavirkning-tralspor | FGDB | portolan_add_failed | CC-BY-4.0 | no-match-found |
| statistisk_rutenett_1000 | statistisk-rutenett-1000 | FGDB | ok | other | no-match-found |
| tare_hostefelt | tare-hostefelt | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| stoysoner_forsvarets_flyplasser | stoysoner-forsvarets-flyplasser | FGDB | portolan_add_failed | other | no-match-found |

### Feilede/hoppet over datasett -- detaljer

- **tettsteder_2018** (portolan_add_failed): portolan add --pmtiles tettsteder-2018 -> exit 1:  to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/tettsteder-2018/tettsteder-2018_tettsteder2018_tettstedsgrense.pmtiles: file exists
⚠ tettsteder-2018_tettsteder2018_tettstedsgrense.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/tettsteder-2018/tettsteder-2018_tettsteder2018_tettsted.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles tettsteder-2018 -> exit 1: 44  
  89.0%  12/2187/1038  
  90.0%  12/2209/1028  
  91.0%  12/2178/1080  
  92.0%  12/2358/884  
  93.0%  12/2310/949  
  94.0%  12/2247/963  
  95.0%  12/2262/927  
  96.0%  12/2270/942  
  97.0%  12/2225/949  
  98.0%  12/2212/961  
  99.0%  12/2218/986  
  100.0%  12/2185/995  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/tettsteder-2018/tettsteder-2018_tettsteder2018_tettsted.parquet: tippecanoe failed with exit code 104

- **forsvarets_skyte_ovingsfelt_land** (portolan_add_failed): portolan add --pmtiles forsvarets-skyte-ovingsfelt-land -> exit 1: t to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/forsvarets-skyte-ovingsfelt-land/forsvarets-skyte-ovingsfelt-land.pmtiles: file exists
⚠ forsvarets-skyte-ovingsfelt-land.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/forsvarets-skyte-ovingsfelt-land/forsvarets-skyte-ovingsfelt-land.parquet: tippecanoe failed with exit code 104

- **vannkraft_utbygd_ikkeutbygd** (portolan_add_failed): portolan add --pmtiles vannkraft-utbygd-ikkeutbygd -> exit 1: 146  
  90.0%  12/2204/1042  
  91.0%  12/2210/1031  
  92.0%  12/2194/1061  
  93.0%  12/2182/1097  
  94.0%  12/2336/890  
  95.0%  12/2247/976  
  96.0%  12/2277/937  
  97.0%  12/2245/958  
  98.0%  12/2229/988  
  99.0%  12/2222/1009  
  100.0%  12/2204/1011  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/vannkraft-utbygd-ikkeutbygd/vannkraft-utbygd-ikkeutbygd_vannkraft_damlinje.parquet: tippecanoe failed with exit code 104

- **n250** (portolan_add_failed): portolan add --pmtiles n250 -> exit 1: 2/2129/1136  
  89.0%  12/2120/1148  
  90.0%  12/2114/1151  
  91.0%  12/2198/1044  
  92.0%  12/2201/1064  
  93.0%  12/2177/1097  
  94.0%  12/2305/907  
  95.0%  12/2401/904  
  96.0%  12/2302/908  
  97.0%  12/2260/942  
  98.0%  12/2231/939  
  99.0%  12/2213/1000  
  100.0%  12/2185/994  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n250/n250_N250_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104

- **militere_forbudsomrader_sjo** (portolan_add_failed): portolan add --pmtiles militere-forbudsomrader-sjo -> exit 1: rs/alenos/dev/portolan-poc/catalog/militere-forbudsomrader-sjo/militere-forbudsomrader-sjo_militertforbudsomradesjo.pmtiles: file exists
⚠ militere-forbudsomrader-sjo_militertforbudsomradesjo.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/militere-forbudsomrader-sjo/militere-forbudsomrader-sjo_forbudsomradegrense.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles militere-forbudsomrader-sjo -> exit 1: 69/1207  
  90.1%  12/2169/1206  
  91.4%  12/2236/954  
  92.1%  12/2236/955  
  93.4%  12/2231/939  
  94.1%  12/2231/938  
  95.4%  12/2232/940  
  96.1%  12/2236/965  
  97.4%  12/2234/966  
  98.0%  12/2235/966  
  99.3%  12/2235/964  
  100.0%  12/2234/965  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/militere-forbudsomrader-sjo/militere-forbudsomrader-sjo_forbudsomradegrense.parquet: tippecanoe failed with exit code 104

- **menneskelig_pavirkning_marint_soppel** (portolan_add_failed): portolan add --pmtiles menneskelig-pavirkning-marint-soppel -> exit 1: tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-marint-soppel/menneskelig-pavirkning-marint-soppel.pmtiles: file exists
⚠ menneskelig-pavirkning-marint-soppel.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-marint-soppel/menneskelig-pavirkning-marint-soppel.parquet: tippecanoe failed with exit code 104

- **lassettingsplasser** (portolan_add_failed): portolan add --pmtiles lassettingsplasser -> exit 1: you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/lassettingsplasser/lassettingsplasser_lassettingsplassgrense.pmtiles: file exists
⚠ lassettingsplasser_lassettingsplassgrense.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lassettingsplasser/lassettingsplasser_lassettingsplass.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles lassettingsplasser -> exit 1: 914  
  89.0%  12/2272/931  
  90.0%  12/2240/942  
  91.0%  12/2242/947  
  92.0%  12/2219/957  
  93.0%  12/2207/974  
  94.0%  12/2221/964  
  95.0%  12/2231/971  
  96.0%  12/2222/982  
  97.0%  12/2208/1006  
  98.0%  12/2200/1020  
  99.0%  12/2200/1012  
  100.0%  12/2303/893  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lassettingsplasser/lassettingsplasser_lassettingsplass.parquet: tippecanoe failed with exit code 104

- **lokaliteter_enkeltminner_sikringssoner** (portolan_add_failed): portolan add --pmtiles lokaliteter-enkeltminner-sikringssoner -> exit 1: poc/catalog/lokaliteter-enkeltminner-sikringssoner/lokaliteter-enkeltminner-sikringssoner_sikringssone.pmtiles: file exists
⚠ lokaliteter-enkeltminner-sikringssoner_sikringssone.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lokaliteter-enkeltminner-sikringssoner/lokaliteter-enkeltminner-sikringssoner_enkeltminne.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles lokaliteter-enkeltminner-sikringssoner -> exit 1: 0%  12/2267/929  
  91.0%  12/2254/952  
  92.0%  12/2231/956  
  93.0%  12/2210/961  
  94.0%  12/2233/970  
  95.0%  12/2216/1004  
  96.0%  12/2215/1020  
  97.0%  12/2226/515  
  98.0%  12/2212/622  
  99.0%  12/2250/495  
  100.0%  12/2170/479  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lokaliteter-enkeltminner-sikringssoner/lokaliteter-enkeltminner-sikringssoner_enkeltminne.parquet: tippecanoe failed with exit code 104

- **tettsteder_2023** (portolan_add_failed): portolan add --pmtiles tettsteder-2023 -> exit 1: %  12/2108/1148  
  89.0%  12/2191/1038  
  90.0%  12/2210/1029  
  91.0%  12/2179/1080  
  92.0%  12/2185/1144  
  93.0%  12/2311/918  
  94.0%  12/2244/967  
  95.0%  12/2265/926  
  96.0%  12/2263/928  
  97.0%  12/2235/956  
  98.0%  12/2202/975  
  99.0%  12/2211/1002  
  100.0%  12/2185/995  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/tettsteder-2023/tettsteder-2023_tettsted.parquet: tippecanoe failed with exit code 104

- **steinsprang_aktsomhetsomr** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **sarbare_marine_bunndyr_observasjonsdata** (portolan_add_failed): portolan add --pmtiles sarbare-marine-bunndyr-observasjonsdata -> exit 1: /2293/746  
  91.0%  12/2272/713  
  92.0%  12/2230/734  
  93.0%  12/2175/517  
  94.0%  12/2359/676  
  95.0%  12/2344/706  
  96.0%  12/2465/744  
  97.0%  12/2382/439  
  98.0%  12/2300/451  
  99.0%  12/2227/431  
  100.0%  12/2289/348  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/sarbare-marine-bunndyr-observasjonsdata/sarbare-marine-bunndyr-observasjonsdata_blomkalkorallskog.parquet: tippecanoe failed with exit code 104

- **missing** (portolan_add_failed): portolan add --pmtiles missing -> exit 1: anoe: Tileset "/Users/alenos/dev/portolan-poc/catalog/missing/missing.pmtiles" already exists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/missing/missing.pmtiles: file exists
⚠ missing.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/missing/missing.parquet: tippecanoe failed with exit code 104

- **adresse_leilighetsniva** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **menneskelig_pavirkning_tralspor** (portolan_add_failed): portolan add --pmtiles menneskelig-pavirkning-tralspor -> exit 1: u want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-tralspor/menneskelig-pavirkning-tralspor.pmtiles: file exists
⚠ menneskelig-pavirkning-tralspor.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-tralspor/menneskelig-pavirkning-tralspor.parquet: tippecanoe failed with exit code 104

- **tare_hostefelt** (portolan_add_failed): portolan add --pmtiles tare-hostefelt -> exit 1: /1067  
  89.0%  12/2170/1069  
  90.0%  12/2166/1067  
  91.0%  12/2171/1061  
  92.0%  12/2175/1058  
  93.0%  12/2175/1050  
  94.0%  12/2178/1052  
  95.0%  12/2181/1061  
  96.0%  12/2178/1056  
  97.0%  12/2177/1063  
  98.0%  12/2181/1065  
  99.0%  12/2176/1070  
  100.0%  12/2183/1072  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/tare-hostefelt/tare-hostefelt_tarehostefelt.parquet: tippecanoe failed with exit code 104

- **stoysoner_forsvarets_flyplasser** (portolan_add_failed): portolan add --pmtiles stoysoner-forsvarets-flyplasser -> exit 1: leset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/stoysoner-forsvarets-flyplasser/stoysoner-forsvarets-flyplasser_stoygrense.pmtiles: file exists
⚠ stoysoner-forsvarets-flyplasser_stoygrense.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/stoysoner-forsvarets-flyplasser/stoysoner-forsvarets-flyplasser_stoy.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles stoysoner-forsvarets-flyplasser -> exit 1: 2156/1097  
  89.5%  12/2156/1098  
  90.5%  12/2156/1099  
  91.6%  12/2157/1099  
  92.6%  12/2157/1098  
  93.7%  12/2152/1094  
  94.7%  12/2152/1095  
  95.8%  12/2258/946  
  96.8%  12/2259/947  
  97.9%  12/2258/947  
  98.9%  12/2257/947  
  100.0%  12/2257/946  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/stoysoner-forsvarets-flyplasser/stoysoner-forsvarets-flyplasser_stoy.parquet: tippecanoe failed with exit code 104


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
→ Skipped 78 items (already fresh)
✓ Converted 9 file(s)
    forsvarets-skyte-ovingsfelt-land.gpkg -> forsvarets-skyte-ovingsfelt-land.parquet
    menneskelig-pavirkning-marint-soppel.gpkg -> menneskelig-pavirkning-marint-soppel.parquet
    menneskelig-pavirkning-tralspor.gpkg -> menneskelig-pavirkning-tralspor.parquet
    missing.gpkg -> missing.parquet
    n250.gpkg -> n250.parquet
    sarbare-marine-bunndyr-observasjonsdata.gpkg -> sarbare-marine-bunndyr-observasjonsdata.parquet
    tare-hostefelt.gpkg -> tare-hostefelt.parquet
    tettsteder-2023.gpkg -> tettsteder-2023.parquet
    vannkraft-utbygd-ikkeutbygd.gpkg -> vannkraft-utbygd-ikkeutbygd.parquet
✓ Catalog conforms (19 file(s) checked)
✓ Fixed automatically (0)
→ Action required (73):
    PTL-PRO-002 forsvarets-skyte-ovingsfelt-land/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 korallrev/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 lassettingsplasser/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 lokaliteter-enkeltminner-sikringssoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-marint-soppel/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-tralspor/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 militere-forbudsomrader-sjo/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 missing/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
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
    PTL-DAT-005 n250/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 n250/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 referansedata-videostasjoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 sarbare-marine-bunndyr-observasjonsdata/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 sefrak-bygninger/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 statistisk-rutenett-1000/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 stoysoner-forsvarets-flyplasser/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tare-hostefelt/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2018/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 tettsteder-2023/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 vannkraft-utbygd-ikkeutbygd/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.

→ Errors (2):
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
→ Warnings (56):
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
    Fix: set file:size to the asset's byte count, unquoted and greater than 0
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
    3 fixable by `portolan check --fix`
    73 need a decision (see Requires: lines)
→ Source files:
✓ 138 file(s) already cloud-native
⚠ 5 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them. 1 registered asset(s) are missing from disk; restore the files, or remove the assets from the catalog.
✗ PTL-DAT-001 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'documentation' file:size is 4865 but the bytes are 7207
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 6.0863, 33.5082, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 6.0863, 33.5082, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6421, 58.1889, 25.2542, 78.0844] and lies within [-25.3256, 57.3673, 45.9593, 80.8611]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone-tiles' data bbox [-9.0422, 57.9700, 33.5082, 80.8220] does not match the declared bbox [-9.0422, 6.0863, 33.5082, 80.8220]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250-tiles' data bbox [4.7161, 57.9880, 31.1141, 71.0640] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2674, 58.1760, 25.1007, 70.8267] and lies within [-0.9521, 57.7730, 31.5350, 71.5652]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_posisjon-tiles' data bbox [4.4992, 57.9585, 31.1686, 71.1857] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_posisjon-tiles' data bbox [4.7161, 57.9880, 31.1141, 71.0640] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_senterlinje-tiles' data bbox [-0.0004, -0.0004, 31.0494, 71.1703] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2973, 58.1865, 25.3563, 70.7812] and lies within [-0.8934, 57.7631, 31.9261, 71.5560]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.1699] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5407, 58.2439, 25.0915, 70.7390] and lies within [-0.4164, 57.8424, 31.4127, 71.4690]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_senterlinje-tiles' data bbox [4.8289, 58.0206, 31.1133, 71.0278] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2663, 58.1764, 25.3596, 70.7844] and lies within [-0.9501, 57.7526, 31.9395, 71.5603]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_omrade-tiles' data bbox [4.5005, 57.9594, 31.1681, 71.1855] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3097, 58.2487, 25.3361, 70.7863] and lies within [-0.8469, 57.8274, 31.8660, 71.5554]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_posisjon-tiles' data bbox [4.6147, 58.0207, 31.1324, 71.1584] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2912, 58.1986, 25.3560, 70.7844] and lies within [-0.9001, 57.7753, 31.9226, 71.5588]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_senterlinje-tiles' data bbox [4.6569, 57.9805, 31.1576, 71.1838] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_grense-tiles' data bbox [5.2450, 58.2547, 30.7979, 70.5255] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_omrade-tiles' data bbox [5.2450, 58.2547, 30.7979, 70.5255] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8080, 58.3382, 17.1494, 67.9470] and lies within [1.9785, 58.0058, 18.0703, 68.4620]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1453, 18.0701, 68.4418] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2843, 58.1972, 25.3641, 70.7954] and lies within [-0.9217, 57.7731, 31.9467, 71.5716]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_senterlinje-tiles' data bbox [4.6157, 57.9780, 31.2096, 71.1835] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Stedsnavn_tekstplassering' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2828, 58.1113, 25.3265, 70.8515] and lies within [-1.0056, 57.6897, 31.9733, 71.6283]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Stedsnavn_tekstplassering-tiles' data bbox [4.2839, 57.8937, 31.2366, 71.2683] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: asset 'sarbare-marine-bunndyr-observasjonsdata_hardbunnskorallskog' declared bbox [-0.8035, 56.5027, 36.9558, 81.6840] is inconsistent with its EPSG:25833 data, whose envelope contains [3.2899, 57.4580, 26.0259, 79.8893] and lies within [-24.0989, 56.9086, 52.3774, 82.1191]
⚠ PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: asset 'sarbare-marine-bunndyr-observasjonsdata_hardbunnskorallskog-tiles' data bbox [1.1760, 57.0766, 36.9558, 81.6840] does not match the declared bbox [-0.8035, 56.5027, 36.9558, 81.6840]
⚠ PTL-AST-003 tettsteder-2023/collection.json: asset 'tmp_tettsteder-2023_tettsted' file:size must be a positive integer, got 0
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd-tiles' data bbox [4.9872, 58.0358, 30.7353, 70.7858] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_damlinje-tiles' data bbox [4.9872, 58.0358, 30.7353, 70.7858] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_dampunkt-tiles' data bbox [4.9285, 58.0358, 30.7352, 70.9996] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_delfelt-tiles' data bbox [5.0823, 58.0700, 30.8406, 70.8096] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_el_kraftstasjon-tiles' data bbox [4.8986, 58.0363, 30.7064, 70.8631] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_innsjokantregulert-tiles' data bbox [5.1880, 58.0685, 30.7478, 70.7918] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_innsjoregulert-tiles' data bbox [5.1880, 58.0685, 30.7478, 70.7918] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_inntakspunkt-tiles' data bbox [4.8673, 58.0390, 30.7356, 70.9536] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_kanal-tiles' data bbox [5.0790, 58.2394, 30.6208, 70.8631] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_kraftverkstunnel-tiles' data bbox [5.1699, 58.1701, 30.7356, 70.8274] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_nedborfeltgr-tiles' data bbox [5.0823, 58.0700, 30.8406, 70.8096] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_rorgate-tiles' data bbox [4.8673, 58.0363, 30.7103, 70.9623] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
✗ Catalog does not conform: 2 errors, 56 warnings
⚠ 9 file(s) need conversion
```

`portolan check catalog --strict`:

```
→ Errors (2):
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
→ Warnings (56):
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
    Fix: set file:size to the asset's byte count, unquoted and greater than 0
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
    3 fixable by `portolan check --fix`
    73 need a decision (see Requires: lines)
→ Source files:
✓ 138 file(s) already cloud-native
⚠ 5 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them. 1 registered asset(s) are missing from disk; restore the files, or remove the assets from the catalog.
✗ PTL-DAT-001 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'documentation' file:size is 4865 but the bytes are 7207
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 6.0863, 33.5082, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 6.0863, 33.5082, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone' declared bbox [-9.0422, 6.0863, 33.5082, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6421, 58.1889, 25.2542, 78.0844] and lies within [-25.3256, 57.3673, 45.9593, 80.8611]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone-tiles' data bbox [-9.0422, 57.9700, 33.5082, 80.8220] does not match the declared bbox [-9.0422, 6.0863, 33.5082, 80.8220]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250-tiles' data bbox [4.7161, 57.9880, 31.1141, 71.0640] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2674, 58.1760, 25.1007, 70.8267] and lies within [-0.9521, 57.7730, 31.5350, 71.5652]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_AdministrativeOmråder_posisjon-tiles' data bbox [4.4992, 57.9585, 31.1686, 71.1857] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [4.9531, 57.9760, 25.4152, 70.9624] and lies within [-1.7023, 57.5458, 32.2912, 71.7649]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.7993] and lies within [-0.4483, 57.8059, 31.4704, 71.5324]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_posisjon-tiles' data bbox [4.7161, 57.9880, 31.1141, 71.0640] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Arealdekke_senterlinje-tiles' data bbox [-0.0004, -0.0004, 31.0494, 71.1703] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2973, 58.1865, 25.3563, 70.7812] and lies within [-0.8934, 57.7631, 31.9261, 71.5560]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.1699] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5407, 58.2439, 25.0915, 70.7390] and lies within [-0.4164, 57.8424, 31.4127, 71.4690]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_BygningerOgAnlegg_senterlinje-tiles' data bbox [4.8289, 58.0206, 31.1133, 71.0278] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2663, 58.1764, 25.3596, 70.7844] and lies within [-0.9501, 57.7526, 31.9395, 71.5603]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_omrade-tiles' data bbox [4.5005, 57.9594, 31.1681, 71.1855] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3097, 58.2487, 25.3361, 70.7863] and lies within [-0.8469, 57.8274, 31.8660, 71.5554]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_posisjon-tiles' data bbox [4.6147, 58.0207, 31.1324, 71.1584] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2912, 58.1986, 25.3560, 70.7844] and lies within [-0.9001, 57.7753, 31.9226, 71.5588]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Høyde_senterlinje-tiles' data bbox [4.6569, 57.9805, 31.1576, 71.1838] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_grense' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_grense-tiles' data bbox [5.2450, 58.2547, 30.7979, 70.5255] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_omrade' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Restriksjonsområder_omrade-tiles' data bbox [5.2450, 58.2547, 30.7979, 70.5255] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_posisjon' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8080, 58.3382, 17.1494, 67.9470] and lies within [1.9785, 58.0058, 18.0703, 68.4620]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1453, 18.0701, 68.4418] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_senterlinje' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2843, 58.1972, 25.3641, 70.7954] and lies within [-0.9217, 57.7731, 31.9467, 71.5716]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Samferdsel_senterlinje-tiles' data bbox [4.6157, 57.9780, 31.2096, 71.1835] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Stedsnavn_tekstplassering' declared bbox [-0.0004, -0.0004, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2828, 58.1113, 25.3265, 70.8515] and lies within [-1.0056, 57.6897, 31.9733, 71.6283]
⚠ PTL-DAT-005 n250/collection.json: asset 'n250_N250_Stedsnavn_tekstplassering-tiles' data bbox [4.2839, 57.8937, 31.2366, 71.2683] does not match the declared bbox [-0.0004, -0.0004, 31.7616, 71.3849]
⚠ PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: asset 'sarbare-marine-bunndyr-observasjonsdata_hardbunnskorallskog' declared bbox [-0.8035, 56.5027, 36.9558, 81.6840] is inconsistent with its EPSG:25833 data, whose envelope contains [3.2899, 57.4580, 26.0259, 79.8893] and lies within [-24.0989, 56.9086, 52.3774, 82.1191]
⚠ PTL-DAT-005 sarbare-marine-bunndyr-observasjonsdata/collection.json: asset 'sarbare-marine-bunndyr-observasjonsdata_hardbunnskorallskog-tiles' data bbox [1.1760, 57.0766, 36.9558, 81.6840] does not match the declared bbox [-0.8035, 56.5027, 36.9558, 81.6840]
⚠ PTL-AST-003 tettsteder-2023/collection.json: asset 'tmp_tettsteder-2023_tettsted' file:size must be a positive integer, got 0
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd-tiles' data bbox [4.9872, 58.0358, 30.7353, 70.7858] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_damlinje-tiles' data bbox [4.9872, 58.0358, 30.7353, 70.7858] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_dampunkt-tiles' data bbox [4.9285, 58.0358, 30.7352, 70.9996] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_delfelt-tiles' data bbox [5.0823, 58.0700, 30.8406, 70.8096] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_el_kraftstasjon-tiles' data bbox [4.8986, 58.0363, 30.7064, 70.8631] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_innsjokantregulert-tiles' data bbox [5.1880, 58.0685, 30.7478, 70.7918] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_innsjoregulert-tiles' data bbox [5.1880, 58.0685, 30.7478, 70.7918] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_inntakspunkt-tiles' data bbox [4.8673, 58.0390, 30.7356, 70.9536] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_kanal-tiles' data bbox [5.0790, 58.2394, 30.6208, 70.8631] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_kraftverkstunnel-tiles' data bbox [5.1699, 58.1701, 30.7356, 70.8274] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_nedborfeltgr-tiles' data bbox [5.0823, 58.0700, 30.8406, 70.8096] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
⚠ PTL-DAT-005 vannkraft-utbygd-ikkeutbygd/collection.json: asset 'vannkraft-utbygd-ikkeutbygd_vannkraft_rorgate-tiles' data bbox [4.8673, 58.0363, 30.7103, 70.9623] does not match the declared bbox [4.8673, 58.0358, 30.8406, 70.9996]
✗ Catalog does not conform: 2 errors, 56 warnings
⚠ 9 file(s) need conversion
```

## Konfigurasjon brukt

Se `config.yaml` i prosjektroten for fullstendig konfigurasjon.
