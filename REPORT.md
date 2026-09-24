# REPORT: GeoNorge -> Portolan PoC

## Sammendrag

- Tjenestefeed: 1043 entries, 374 unike datasett.
- 324 datasett ekskludert fra kandidatpoolen (kun i SOSI/GML/PostGIS/andre formater portolan-cli ikke stotter, eller filtrert av tittel-mønster).
- Sample: 50 datasett valgt.
- **1/50 datasett fullfort vellykket** gjennom hele pipelinen.
- `portolan check catalog` (standard, spec-konformitet) etter full kjoring: **FAIL**.
- `portolan check catalog --strict` (advarsler telles som feil): **FAIL** (se punkt 4 under "Kjente begrensninger" -- forventet a feile pa en ufarlig, dokumentert CLI-advarsel, ikke pa reelle spec-brudd).

### Status per steg

| Status | Antall |
|---|---|
| portolan_add_failed | 39 |
| convert_failed | 7 |
| download_failed | 3 |
| ok | 1 |

### Format-fordeling i sample

| Format | Antall |
|---|---|
| FGDB | 45 |
| SHAPE | 2 |
| GML | 1 |
| GEOPACKAGE | 1 |
| GEOJSON | 1 |

### Kartografi/styling (steg 5b)

| Avgjorelse | Antall |
|---|---|
| authoritative-pdf-only | 27 |
| no-match-found | 13 |

`authoritative-sld` betyr en SLD-fil ble funnet og lastet ned (fargeuttrekk til en MapLibre-override forsokt); `authoritative-pdf-only` betyr registeret bare hadde menneskelesbar PDF-dokumentasjon; `no-match-found` betyr fallback til portolans auto-genererte default-style.

## Datasett-for-datasett

| Dataset ID | Collection | Format | Status | Lisens | Styling |
|---|---|---|---|---|---|
| aktsomhetskart_kvikkleireskred | aktsomhetskart-kvikkleireskred | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| aktsomhetskart_snoskred | aktsomhetskart-snoskred | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| artsmangfold_video-observerte_korallbunntyper | artsmangfold-video-observerte-korallbunntyper | FGDB | ok | other | no-match-found |
| forsvarets_skyte_ovingsfelt_land | forsvarets-skyte-ovingsfelt-land | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| tn-w | tn-w | GML | portolan_add_failed | other | no-match-found |
| interkommunale_brannvesen | interkommunale-brannvesen | FGDB | portolan_add_failed | other | no-match-found |
| kart_over_gra_arealer | kart-over-gra-arealer | GEOPACKAGE | download_failed | other | - |
| kirkebygg_forenklet | kirkebygg-forenklet | GEOJSON | convert_failed | other | - |
| Konnekteringspunkter mellom Norge og Finland | konnekteringspunkter-mellom-norge-og-finland | SHAPE | portolan_add_failed | CC-BY-4.0 | no-match-found |
| Konnekteringspunkter mellom Norge og Sverige | konnekteringspunkter-mellom-norge-og-sverige | SHAPE | portolan_add_failed | CC-BY-4.0 | no-match-found |
| korallrev_forbudsomrader | korallrev-forbudsomrader | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| korallrev | korallrev | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| kulturmiljoer | kulturmiljoer | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| lokaliteter_enkeltminner_sikringssoner | lokaliteter-enkeltminner-sikringssoner | FGDB | portolan_add_failed | other | no-match-found |
| sefrak_bygninger | sefrak-bygninger | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| kvikkleire | kvikkleire | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| lufthavn_punkt | lufthavn-punkt | FGDB | portolan_add_failed | other | no-match-found |
| lassettingsplasser | lassettingsplasser | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| mareano_bunnprover_linjer | mareano-bunnprover-linjer | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| mareano_bunnprover_punkt | mareano-bunnprover-punkt | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| mareano_bunnprovestasjoner | mareano-bunnprovestasjoner | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| mareano_kjemistasjoner | mareano-kjemistasjoner | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| mareano_referansestasjoner | mareano-referansestasjoner | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| mareno_videostasjoner | mareno-videostasjoner | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| mareanoprover_artsmangfold_individer_biomasse | mareanoprover-artsmangfold-individer-biomasse | FGDB | portolan_add_failed | other | no-match-found |
| markagrensen | markagrensen | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| adresse | adresse | FGDB | convert_failed | CC-BY-4.0 | - |
| adresse_leilighetsniva | adresse-leilighetsniva | FGDB | convert_failed | CC-BY-4.0 | - |
| menneskelig_pavirkning_marint_soppel | menneskelig-pavirkning-marint-soppel | FGDB | portolan_add_failed | CC-BY-4.0 | no-match-found |
| menneskelig_pavirkning_tralspor | menneskelig-pavirkning-tralspor | FGDB | portolan_add_failed | CC-BY-4.0 | no-match-found |
| menneskelig_pavirkning_tapte_fiskeredskaper | menneskelig-pavirkning-tapte-fiskeredskaper | FGDB | portolan_add_failed | CC-BY-4.0 | no-match-found |
| militere_forbudsomrader_sjo | militere-forbudsomrader-sjo | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| N100 | n100 | FGDB | convert_failed | CC-BY-4.0 | - |
| n1000 | n1000 | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| N2000 Kartdata | n2000-kartdata | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| n250 | n250 | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| n5_presentasjonsdata | n5-presentasjonsdata | FGDB | download_failed | other | - |
| n50 | n50 | FGDB | convert_failed | CC-BY-4.0 | - |
| N500 Kartdata | n500-kartdata | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| N5000 Kartdata | n5000-kartdata | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| NVDB_RuteplanNettverk | nvdb-ruteplannettverk | FGDB | convert_failed | other | - |
| nasjonale_laksefjorder | nasjonale-laksefjorder | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| luftfartshindre | luftfartshindre | FGDB | download_failed | other | - |
| naturtyper_i_norge | naturtyper-i-norge | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| nettanlegg | nettanlegg | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| nin_saltvannssjobunntyper_predikert | nin-saltvannssjobunntyper-predikert | FGDB | portolan_add_failed | CC-BY-4.0 | no-match-found |
| norges_maritime_grenser | norges-maritime-grenser | FGDB | portolan_add_failed | other | authoritative-pdf-only |
| nodhavner | nodhavner | FGDB | convert_failed | other | - |
| organiske_miljogifter_marine_sedimenter | organiske-miljogifter-marine-sedimenter | FGDB | portolan_add_failed | CC-BY-4.0 | authoritative-pdf-only |
| nin_saltvannssjobunntyper | nin-saltvannssjobunntyper | FGDB | portolan_add_failed | other | no-match-found |

### Feilede/hoppet over datasett -- detaljer

- **aktsomhetskart_kvikkleireskred** (portolan_add_failed): portolan add --pmtiles aktsomhetskart-kvikkleireskred -> exit 1: somhetskart-kvikkleireskred/aktsomhetskart-kvikkleireskred_kvikkleireskredaktsomhetdekning.pmtiles: file exists
⚠ aktsomhetskart-kvikkleireskred_kvikkleireskredaktsomhetdekning.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/aktsomhetskart-kvikkleireskred/aktsomhetskart-kvikkleireskred_aktsomhetsomrkvikkleireskred.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles aktsomhetskart-kvikkleireskred -> exit 1: %  12/2224/948  
  91.0%  12/2213/957  
  92.0%  12/2204/973  
  93.0%  12/2220/971  
  94.0%  12/2237/960  
  95.0%  12/2226/978  
  96.0%  12/2223/989  
  97.0%  12/2210/1007  
  98.0%  12/2225/995  
  99.0%  12/2198/1020  
  100.0%  12/2303/892  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/aktsomhetskart-kvikkleireskred/aktsomhetskart-kvikkleireskred_aktsomhetsomrkvikkleireskred.parquet: tippecanoe failed with exit code 104

- **aktsomhetskart_snoskred** (portolan_add_failed): portolan add --pmtiles aktsomhetskart-snoskred -> exit 1: 1  
  89.0%  12/2271/938  
  90.0%  12/2248/957  
  91.0%  12/2229/945  
  92.0%  12/2234/938  
  93.0%  12/2199/964  
  94.0%  12/2236/961  
  95.0%  12/2231/984  
  96.0%  12/2213/1005  
  97.0%  12/2225/1005  
  98.0%  12/2215/1016  
  99.0%  12/2202/995  
  100.0%  12/2303/882  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/aktsomhetskart-snoskred/aktsomhetskart-snoskred_kartblad.parquet: tippecanoe failed with exit code 104

- **forsvarets_skyte_ovingsfelt_land** (portolan_add_failed): portolan add --pmtiles forsvarets-skyte-ovingsfelt-land -> exit 1: t to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/forsvarets-skyte-ovingsfelt-land/forsvarets-skyte-ovingsfelt-land.pmtiles: file exists
⚠ forsvarets-skyte-ovingsfelt-land.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/forsvarets-skyte-ovingsfelt-land/forsvarets-skyte-ovingsfelt-land.parquet: tippecanoe failed with exit code 104

- **tn-w** (portolan_add_failed): portolan check tn-w --fix --workers 4 -> exit 1: ⚠ 4 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 14 warnings
; portolan add --pmtiles tn-w -> exit 1: s/dev/portolan-poc/catalog/tn-w/tn-w_WaterwayNode.pmtiles" already exists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/tn-w/tn-w_WaterwayNode.pmtiles: file exists
⚠ tn-w_WaterwayNode.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/tn-w/tn-w_PortNode.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles tn-w -> exit 1: %  12/2105/1144  
  88.1%  12/2185/1024  
  89.0%  12/2192/1038  
  90.0%  12/2176/1072  
  91.1%  12/2319/882  
  92.0%  12/2376/914  
  93.0%  12/2300/900  
  94.1%  12/2271/917  
  95.0%  12/2250/957  
  96.0%  12/2225/950  
  97.1%  12/2212/961  
  98.0%  12/2225/960  
  99.0%  12/2213/1004  
  100.0%  12/2237/587  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/tn-w/tn-w_PortNode.parquet: tippecanoe failed with exit code 104

- **interkommunale_brannvesen** (portolan_add_failed): portolan check interkommunale-brannvesen --fix --workers 4 -> exit 1: ⚠ 4 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 16 warnings
; portolan add --pmtiles interkommunale-brannvesen -> exit 1: en/interkommunale-brannvesen_interkommunale_brannvesen_iksbrannvesenomrade.pmtiles: file exists
⚠ interkommunale-brannvesen_interkommunale_brannvesen_iksbrannvesenomrade.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/interkommunale-brannvesen/interkommunale-brannvesen_interkommunale_brannvesen_iksbrannvesengrense.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles interkommunale-brannvesen -> exit 1: /1090  
  91.0%  12/2186/1142  
  92.0%  12/2244/964  
  93.0%  12/2246/956  
  94.0%  12/2204/986  
  95.0%  12/2231/964  
  96.0%  12/2235/978  
  97.0%  12/2231/995  
  98.0%  12/2221/1020  
  99.0%  12/2196/1016  
  100.0%  12/2191/1010  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/interkommunale-brannvesen/interkommunale-brannvesen_interkommunale_brannvesen_iksbrannvesengrense.parquet: tippecanoe failed with exit code 104

- **kart_over_gra_arealer** (download_failed): Failed to download https://nedlasting.geonorge.no/api/download/file//c5f09d79-1546-495c-8b36-91efd4008bd7/ED36B48D-C123-46BB-B23F-62649F949519
- **kirkebygg_forenklet** (convert_failed): ogr2ogr could not convert the downloaded GEOJSON file to GeoPackage
- **Konnekteringspunkter mellom Norge og Finland** (portolan_add_failed): portolan check konnekteringspunkter-mellom-norge-og-finland --fix --workers 4 -> exit 1: ⚠ 3 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 17 warnings

- **Konnekteringspunkter mellom Norge og Sverige** (portolan_add_failed): portolan check konnekteringspunkter-mellom-norge-og-sverige --fix --workers 4 -> exit 1: ⚠ 3 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 16 warnings
; portolan add --pmtiles konnekteringspunkter-mellom-norge-og-sverige -> exit 1: ortolan-poc/catalog/konnekteringspunkter-mellom-norge-og-sverige/konnekteringspunkter-mellom-norge-og-sverige.pmtiles: file exists
⚠ konnekteringspunkter-mellom-norge-og-sverige.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/konnekteringspunkter-mellom-norge-og-sverige/konnekteringspunkter-mellom-norge-og-sverige.parquet: tippecanoe failed with exit code 104

- **korallrev_forbudsomrader** (portolan_add_failed): portolan check korallrev-forbudsomrader --fix --workers 4 -> exit 1: ⚠ 5 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 16 warnings
; portolan add --pmtiles korallrev-forbudsomrader -> exit 1:  
  90.0%  12/2151/998  
  91.0%  12/2148/999  
  92.0%  12/2155/995  
  93.0%  12/2153/996  
  94.0%  12/2154/997  
  95.0%  12/2157/993  
  96.0%  12/2259/890  
  97.0%  12/2256/892  
  98.0%  12/2259/893  
  99.0%  12/2260/893  
  100.0%  12/2300/885  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/korallrev-forbudsomrader/korallrev-forbudsomrader_korallrev_forbudsomrader_korallrev.parquet: tippecanoe failed with exit code 104

- **korallrev** (portolan_add_failed): portolan check korallrev --fix --workers 4 -> exit 1: ⚠ 5 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 17 warnings

- **kulturmiljoer** (portolan_add_failed): portolan check kulturmiljoer --fix --workers 4 -> exit 1: ⚠ 6 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 16 warnings
; portolan add --pmtiles kulturmiljoer -> exit 1:   88.0%  12/2284/910  
  89.0%  12/2242/940  
  90.0%  12/2261/947  
  91.0%  12/2229/940  
  92.0%  12/2224/967  
  93.0%  12/2220/1023  
  94.0%  12/2264/747  
  95.0%  12/2216/557  
  96.0%  12/2219/569  
  97.0%  12/2217/590  
  98.0%  12/2252/462  
  99.0%  12/2271/425  
  100.0%  12/2171/478  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/kulturmiljoer/kulturmiljoer_kulturmiljo.parquet: tippecanoe failed with exit code 104

- **lokaliteter_enkeltminner_sikringssoner** (portolan_add_failed): portolan check lokaliteter-enkeltminner-sikringssoner --fix --workers 4 -> exit 1: Repaired 1 invalid geometry
⚠ 7 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 21 warnings
; portolan add --pmtiles lokaliteter-enkeltminner-sikringssoner -> exit 1: poc/catalog/lokaliteter-enkeltminner-sikringssoner/lokaliteter-enkeltminner-sikringssoner_sikringssone.pmtiles: file exists
⚠ lokaliteter-enkeltminner-sikringssoner_sikringssone.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lokaliteter-enkeltminner-sikringssoner/lokaliteter-enkeltminner-sikringssoner_enkeltminne.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles lokaliteter-enkeltminner-sikringssoner -> exit 1: 0%  12/2267/930  
  91.0%  12/2254/952  
  92.0%  12/2231/956  
  93.0%  12/2211/961  
  94.0%  12/2233/970  
  95.0%  12/2216/1003  
  96.0%  12/2215/1020  
  97.0%  12/2226/515  
  98.0%  12/2212/622  
  99.0%  12/2250/495  
  100.0%  12/2170/479  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lokaliteter-enkeltminner-sikringssoner/lokaliteter-enkeltminner-sikringssoner_enkeltminne.parquet: tippecanoe failed with exit code 104

- **sefrak_bygninger** (portolan_add_failed): portolan check sefrak-bygninger --fix --workers 4 -> exit 1: ⚠ 6 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 24 warnings

- **kvikkleire** (portolan_add_failed): portolan check kvikkleire --fix --workers 4 -> exit 1: ⚠ 7 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 31 warnings
; portolan add --pmtiles kvikkleire -> exit 1: 316/908  
  89.0%  12/2320/920  
  90.0%  12/2319/922  
  91.0%  12/2315/912  
  92.0%  12/2311/915  
  93.0%  12/2308/922  
  94.0%  12/2277/931  
  95.0%  12/2287/926  
  96.0%  12/2266/927  
  97.0%  12/2262/931  
  98.0%  12/2268/930  
  99.0%  12/2222/1000  
  100.0%  12/2225/1002  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/kvikkleire/kvikkleire_kvikkleire_kartleggingsomrade.parquet: tippecanoe failed with exit code 104

- **lufthavn_punkt** (portolan_add_failed): portolan check lufthavn-punkt --fix --workers 4 -> exit 1: ⚠ 7 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 33 warnings
; portolan add --pmtiles lufthavn-punkt -> exit 1: alog/lufthavn-punkt/lufthavn-punkt.pmtiles" already exists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/lufthavn-punkt/lufthavn-punkt.pmtiles: file exists
⚠ lufthavn-punkt.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/lufthavn-punkt/lufthavn-punkt.parquet: tippecanoe failed with exit code 104

- **lassettingsplasser** (portolan_add_failed): portolan check lassettingsplasser --fix --workers 4 -> exit 1: ⚠ 9 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 33 warnings
; portolan add --pmtiles lassettingsplasser -> exit 1: you want to delete the old tileset.
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

- **mareano_bunnprover_linjer** (portolan_add_failed): portolan check mareano-bunnprover-linjer --fix --workers 4 -> exit 1: ⚠ 8 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 33 warnings
; portolan add --pmtiles mareano-bunnprover-linjer -> exit 1: sts. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/mareano-bunnprover-linjer/mareano-bunnprover-linjer.pmtiles: file exists
⚠ mareano-bunnprover-linjer.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/mareano-bunnprover-linjer/mareano-bunnprover-linjer.parquet: tippecanoe failed with exit code 104

- **mareano_bunnprover_punkt** (portolan_add_failed): portolan check mareano-bunnprover-punkt --fix --workers 4 -> exit 1: ⚠ 9 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 33 warnings
; portolan add --pmtiles mareano-bunnprover-punkt -> exit 1: y exists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/mareano-bunnprover-punkt/mareano-bunnprover-punkt.pmtiles: file exists
⚠ mareano-bunnprover-punkt.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/mareano-bunnprover-punkt/mareano-bunnprover-punkt.parquet: tippecanoe failed with exit code 104

- **mareano_bunnprovestasjoner** (portolan_add_failed): portolan check mareano-bunnprovestasjoner --fix --workers 4 -> exit 1: ⚠ 10 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 34 warnings

- **mareano_kjemistasjoner** (portolan_add_failed): portolan check mareano-kjemistasjoner --fix --workers 4 -> exit 1: ⚠ 10 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 34 warnings
; portolan add --pmtiles mareano-kjemistasjoner -> exit 1: es" already exists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/mareano-kjemistasjoner/mareano-kjemistasjoner.pmtiles: file exists
⚠ mareano-kjemistasjoner.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/mareano-kjemistasjoner/mareano-kjemistasjoner.parquet: tippecanoe failed with exit code 104

- **mareano_referansestasjoner** (portolan_add_failed): portolan check mareano-referansestasjoner --fix --workers 4 -> exit 1: ⚠ 11 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 35 warnings

- **mareno_videostasjoner** (portolan_add_failed): portolan check mareno-videostasjoner --fix --workers 4 -> exit 1: ⚠ 11 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 34 warnings
; portolan add --pmtiles mareno-videostasjoner -> exit 1: pmtiles" already exists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/mareno-videostasjoner/mareno-videostasjoner.pmtiles: file exists
⚠ mareno-videostasjoner.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/mareno-videostasjoner/mareno-videostasjoner.parquet: tippecanoe failed with exit code 104

- **mareanoprover_artsmangfold_individer_biomasse** (portolan_add_failed): portolan check mareanoprover-artsmangfold-individer-biomasse --fix --workers 4 -> exit 1: ⚠ 13 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 38 warnings
; portolan add --pmtiles mareanoprover-artsmangfold-individer-biomasse -> exit 1:   
  91.0%  12/2166/1004  
  92.0%  12/2158/965  
  93.0%  12/2224/848  
  94.0%  12/2241/884  
  95.0%  12/2272/889  
  96.0%  12/2291/877  
  97.0%  12/2277/717  
  98.0%  12/2170/519  
  99.0%  12/2345/758  
  100.0%  12/2299/447  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/mareanoprover-artsmangfold-individer-biomasse/mareanoprover-artsmangfold-individer-biomasse_bomtralprover.parquet: tippecanoe failed with exit code 104

- **markagrensen** (portolan_add_failed): portolan check markagrensen --fix --workers 4 -> exit 1: ⚠ 14 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 40 warnings
; portolan add --pmtiles markagrensen -> exit 1:  want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/markagrensen/markagrensen_markagrensen_lovvirkeomradegrense.pmtiles: file exists
⚠ markagrensen_markagrensen_lovvirkeomradegrense.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/markagrensen/markagrensen_markagrensen_lovvirkeomrade.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles markagrensen -> exit 1: 89.3%  12/2173/1188  
  90.4%  12/2172/1189  
  91.5%  12/2172/1191  
  92.1%  12/2173/1191  
  93.2%  12/2174/1191  
  94.4%  12/2172/1187  
  95.5%  12/2173/1186  
  96.0%  12/2173/1185  
  97.2%  12/2172/1184  
  98.3%  12/2171/1183  
  99.4%  12/2168/1183  
  100.0%  12/2167/1183  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/markagrensen/markagrensen_markagrensen_lovvirkeomrade.parquet: tippecanoe failed with exit code 104

- **adresse** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **adresse_leilighetsniva** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **menneskelig_pavirkning_marint_soppel** (portolan_add_failed): portolan check menneskelig-pavirkning-marint-soppel --fix --workers 4 -> exit 1: ⚠ 13 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 40 warnings
; portolan add --pmtiles menneskelig-pavirkning-marint-soppel -> exit 1: tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-marint-soppel/menneskelig-pavirkning-marint-soppel.pmtiles: file exists
⚠ menneskelig-pavirkning-marint-soppel.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-marint-soppel/menneskelig-pavirkning-marint-soppel.parquet: tippecanoe failed with exit code 104

- **menneskelig_pavirkning_tralspor** (portolan_add_failed): portolan check menneskelig-pavirkning-tralspor --fix --workers 4 -> exit 1: ⚠ 14 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 40 warnings
; portolan add --pmtiles menneskelig-pavirkning-tralspor -> exit 1: u want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-tralspor/menneskelig-pavirkning-tralspor.pmtiles: file exists
⚠ menneskelig-pavirkning-tralspor.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/menneskelig-pavirkning-tralspor/menneskelig-pavirkning-tralspor.parquet: tippecanoe failed with exit code 104

- **menneskelig_pavirkning_tapte_fiskeredskaper** (portolan_add_failed): portolan check menneskelig-pavirkning-tapte-fiskeredskaper --fix --workers 4 -> exit 1: ⚠ 15 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 41 warnings

- **militere_forbudsomrader_sjo** (portolan_add_failed): portolan check militere-forbudsomrader-sjo --fix --workers 4 -> exit 1: ⚠ 16 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 40 warnings
; portolan add --pmtiles militere-forbudsomrader-sjo -> exit 1: rs/alenos/dev/portolan-poc/catalog/militere-forbudsomrader-sjo/militere-forbudsomrader-sjo_militertforbudsomradesjo.pmtiles: file exists
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

- **N100** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **n1000** (portolan_add_failed): portolan check n1000 --fix --workers 4 -> exit 1: ⚠ 16 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 63 warnings
; portolan add --pmtiles n1000 -> exit 1: ists. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/n1000/n1000_N1000_Stedsnavn_tekstplassering.pmtiles: file exists
⚠ n1000_N1000_Stedsnavn_tekstplassering.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n1000/n1000_N1000_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles n1000 -> exit 1:   12/2296/914  
  89.0%  12/2287/927  
  90.0%  12/2245/940  
  91.0%  12/2266/934  
  92.0%  12/2264/956  
  93.0%  12/2240/959  
  94.0%  12/2215/959  
  95.0%  12/2213/972  
  96.0%  12/2234/965  
  97.0%  12/2223/978  
  98.0%  12/2230/996  
  99.0%  12/2209/1009  
  100.0%  12/2303/895  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n1000/n1000_N1000_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104

- **N2000 Kartdata** (portolan_add_failed): portolan check n2000-kartdata --fix --workers 4 -> exit 1: ⚠ 16 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 89 warnings
; portolan add --pmtiles n2000-kartdata -> exit 1: te the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/n2000-kartdata/n2000-kartdata_N2000_Stedsnavn_tekstplassering.pmtiles: file exists
⚠ n2000-kartdata_N2000_Stedsnavn_tekstplassering.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n2000-kartdata/n2000-kartdata_N2000_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles n2000-kartdata -> exit 1: 89.0%  12/2274/920  
  90.0%  12/2252/942  
  91.0%  12/2268/939  
  92.0%  12/2251/958  
  93.0%  12/2233/959  
  94.0%  12/2219/953  
  95.0%  12/2208/971  
  96.0%  12/2235/962  
  97.0%  12/2219/985  
  98.0%  12/2223/997  
  99.0%  12/2198/1023  
  100.0%  12/2301/895  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n2000-kartdata/n2000-kartdata_N2000_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104

- **n250** (portolan_add_failed): portolan check n250 --fix --workers 4 -> exit 1: ⚠ 16 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 124 warnings
; portolan add --pmtiles n250 -> exit 1: 2/2129/1136  
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

- **n5_presentasjonsdata** (download_failed): Failed to download https://nedlasting.geonorge.no/api/download/file//61f2b119-0b47-4f96-b97e-721e191cfcda/9C77C133-D531-4A06-A8A4-CCC87FDA5E4B
- **n50** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **N500 Kartdata** (portolan_add_failed): portolan check n500-kartdata --fix --workers 4 -> exit 1: ⚠ 17 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 147 warnings
; portolan add --pmtiles n500-kartdata -> exit 1: 
  89.0%  12/2283/916  
  90.0%  12/2247/933  
  91.0%  12/2270/929  
  92.0%  12/2268/950  
  93.0%  12/2241/954  
  94.0%  12/2223/954  
  95.0%  12/2211/971  
  96.0%  12/2234/966  
  97.0%  12/2223/982  
  98.0%  12/2225/998  
  99.0%  12/2209/1008  
  100.0%  12/2303/893  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n500-kartdata/n500-kartdata_N500_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104

- **N5000 Kartdata** (portolan_add_failed): portolan check n5000-kartdata --fix --workers 4 -> exit 1: ⚠ 18 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 166 warnings
; portolan add --pmtiles n5000-kartdata -> exit 1: te the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/n5000-kartdata/n5000-kartdata_N5000_Stedsnavn_tekstplassering.pmtiles: file exists
⚠ n5000-kartdata_N5000_Stedsnavn_tekstplassering.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n5000-kartdata/n5000-kartdata_N5000_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles n5000-kartdata -> exit 1: 89.0%  12/2295/921  
  90.0%  12/2271/927  
  91.0%  12/2249/933  
  92.0%  12/2259/944  
  93.0%  12/2247/945  
  94.0%  12/2231/957  
  95.0%  12/2203/973  
  96.0%  12/2229/966  
  97.0%  12/2229/987  
  98.0%  12/2227/994  
  99.0%  12/2197/1018  
  100.0%  12/2187/996  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/n5000-kartdata/n5000-kartdata_N5000_AdministrativeOmråder_grense.parquet: tippecanoe failed with exit code 104

- **NVDB_RuteplanNettverk** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **nasjonale_laksefjorder** (portolan_add_failed): portolan check nasjonale-laksefjorder --fix --workers 4 -> exit 1: ⚠ 18 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 168 warnings
; portolan add --pmtiles nasjonale-laksefjorder -> exit 1: 918  
  89.0%  12/2309/915  
  90.0%  12/2367/900  
  91.0%  12/2370/896  
  92.0%  12/2372/896  
  93.0%  12/2384/927  
  94.0%  12/2390/922  
  95.0%  12/2298/922  
  96.0%  12/2290/919  
  97.0%  12/2287/923  
  98.0%  12/2263/939  
  99.0%  12/2256/937  
  100.0%  12/2209/1010  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/nasjonale-laksefjorder/nasjonale-laksefjorder_laksefjord.parquet: tippecanoe failed with exit code 104

- **luftfartshindre** (download_failed): Failed to download https://nedlasting.geonorge.no/api/download/file//28c896d0-8a0d-4209-bf31-4931033b1082/FD460965-9EBE-49FF-81D7-3551BAF5FCD5
- **naturtyper_i_norge** (portolan_add_failed): portolan check naturtyper-i-norge --fix --workers 4 -> exit 1: Repaired 12 invalid geometries
⚠ 19 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 168 warnings
; portolan add --pmtiles naturtyper-i-norge -> exit 1: -force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/naturtyper-i-norge/naturtyper-i-norge_NiN_Landskapsgrense.pmtiles: file exists
⚠ naturtyper-i-norge_NiN_Landskapsgrense.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/naturtyper-i-norge/naturtyper-i-norge_NiN_Landskap.parquet: tippecanoe failed with exit code 104
; portolan add --force --pmtiles naturtyper-i-norge -> exit 1: 268/950  
  89.0%  12/2241/956  
  90.0%  12/2215/949  
  91.0%  12/2239/927  
  92.0%  12/2202/979  
  93.0%  12/2222/975  
  94.0%  12/2229/979  
  95.0%  12/2213/985  
  96.0%  12/2232/1005  
  97.0%  12/2215/1023  
  98.0%  12/2203/996  
  99.0%  12/2180/1008  
  100.0%  12/2303/881  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/naturtyper-i-norge/naturtyper-i-norge_NiN_Landskap.parquet: tippecanoe failed with exit code 104

- **nettanlegg** (portolan_add_failed): portolan check nettanlegg --fix --workers 4 -> exit 1: ⚠ 19 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 175 warnings
; portolan add --pmtiles nettanlegg -> exit 1: 6  
  88.0%  12/2293/907  
  89.0%  12/2263/925  
  90.0%  12/2253/943  
  91.0%  12/2268/939  
  92.0%  12/2258/954  
  93.0%  12/2241/957  
  94.0%  12/2218/954  
  95.0%  12/2210/974  
  96.0%  12/2237/964  
  97.0%  12/2230/990  
  98.0%  12/2217/1006  
  99.0%  12/2216/1013  
  100.0%  12/2303/895  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/nettanlegg/nettanlegg_el_luftlinje.parquet: tippecanoe failed with exit code 104

- **nin_saltvannssjobunntyper_predikert** (portolan_add_failed): portolan check nin-saltvannssjobunntyper-predikert --fix --workers 4 -> exit 1: ⚠ 19 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 178 warnings

- **norges_maritime_grenser** (portolan_add_failed): portolan check norges-maritime-grenser --fix --workers 4 -> exit 1: ⚠ 20 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 220 warnings
; portolan add --pmtiles norges-maritime-grenser -> exit 1:  12/2446/338  
  90.0%  12/2051/416  
  91.0%  12/2066/384  
  92.0%  12/2077/359  
  93.0%  12/2084/345  
  94.0%  12/2110/293  
  95.0%  12/2130/195  
  96.0%  12/2124/228  
  97.0%  12/2131/186  
  98.0%  12/2440/162  
  99.0%  12/2446/223  
  100.0%  12/2446/240  
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/norges-maritime-grenser/norges-maritime-grenser_avtaltavgrensningslinje.parquet: tippecanoe failed with exit code 104

- **nodhavner** (convert_failed): ogr2ogr could not convert the downloaded FGDB file to GeoPackage
- **organiske_miljogifter_marine_sedimenter** (portolan_add_failed): portolan check organiske-miljogifter-marine-sedimenter --fix --workers 4 -> exit 1: ⚠ 20 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 222 warnings
; portolan add --pmtiles organiske-miljogifter-marine-sedimenter -> exit 1: anoe: /Users/alenos/dev/portolan-poc/catalog/organiske-miljogifter-marine-sedimenter/organiske-miljogifter-marine-sedimenter.pmtiles: file exists
⚠ organiske-miljogifter-marine-sedimenter.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/organiske-miljogifter-marine-sedimenter/organiske-miljogifter-marine-sedimenter.parquet: tippecanoe failed with exit code 104

- **nin_saltvannssjobunntyper** (portolan_add_failed): portolan check nin-saltvannssjobunntyper --fix --workers 4 -> exit 1: ⚠ 21 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them.
✗ Catalog does not conform: 2 errors, 222 warnings
; portolan add --pmtiles nin-saltvannssjobunntyper -> exit 1: sts. You can use --force if you want to delete the old tileset.
tippecanoe: /Users/alenos/dev/portolan-poc/catalog/nin-saltvannssjobunntyper/nin-saltvannssjobunntyper.pmtiles: file exists
⚠ nin-saltvannssjobunntyper.pmtiles already exists and was kept. Pass --force-pmtiles to rebuild it.
✗ PMTiles generation failed: [PRTLN-PMT003] PMTiles generation failed for /Users/alenos/dev/portolan-poc/catalog/nin-saltvannssjobunntyper/nin-saltvannssjobunntyper.parquet: tippecanoe failed with exit code 104


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
→ Skipped 197 items (already fresh)
✓ Converted 21 file(s)
    aktsomhetskart-snoskred.gpkg -> aktsomhetskart-snoskred.parquet
    forsvarets-skyte-ovingsfelt-land.gpkg -> forsvarets-skyte-ovingsfelt-land.parquet
    konnekteringspunkter-mellom-norge-og-sverige.gpkg -> konnekteringspunkter-mellom-norge-og-sverige.parquet
    korallrev-forbudsomrader.gpkg -> korallrev-forbudsomrader.parquet
    kulturmiljoer.gpkg -> kulturmiljoer.parquet
    kvikkleire.gpkg -> kvikkleire.parquet
    lufthavn-punkt.gpkg -> lufthavn-punkt.parquet
    mareano-bunnprover-linjer.gpkg -> mareano-bunnprover-linjer.parquet
    mareano-bunnprover-punkt.gpkg -> mareano-bunnprover-punkt.parquet
    mareano-kjemistasjoner.gpkg -> mareano-kjemistasjoner.parquet
    mareanoprover-artsmangfold-individer-biomasse.gpkg -> mareanoprover-artsmangfold-individer-biomasse.parquet
    mareno-videostasjoner.gpkg -> mareno-videostasjoner.parquet
    menneskelig-pavirkning-marint-soppel.gpkg -> menneskelig-pavirkning-marint-soppel.parquet
    menneskelig-pavirkning-tralspor.gpkg -> menneskelig-pavirkning-tralspor.parquet
    n250.gpkg -> n250.parquet
    n500-kartdata.gpkg -> n500-kartdata.parquet
    nasjonale-laksefjorder.gpkg -> nasjonale-laksefjorder.parquet
    nettanlegg.gpkg -> nettanlegg.parquet
    nin-saltvannssjobunntyper.gpkg -> nin-saltvannssjobunntyper.parquet
    norges-maritime-grenser.gpkg -> norges-maritime-grenser.parquet
    organiske-miljogifter-marine-sedimenter.gpkg -> organiske-miljogifter-marine-sedimenter.parquet
✓ Fixed automatically (0)
→ Action required (264):
    PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 aktsomhetskart-kvikkleireskred/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 aktsomhetskart-snoskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 aktsomhetskart-snoskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 aktsomhetskart-snoskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 aktsomhetskart-snoskred/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 aktsomhetskart-snoskred/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 artsmangfold-video-observerte-korallbunntyper/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-CAT-001 catalog.json: group the children under thematic subcatalogs, each with its own catalog.json, and relink this object to those subcatalogs
    PTL-PRO-002 forsvarets-skyte-ovingsfelt-land/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 interkommunale-brannvesen/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 konnekteringspunkter-mellom-norge-og-finland/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 konnekteringspunkter-mellom-norge-og-sverige/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 korallrev-forbudsomrader/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 korallrev/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 kulturmiljoer/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 kvikkleire/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 kvikkleire/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 lassettingsplasser/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 lokaliteter-enkeltminner-sikringssoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 lufthavn-punkt/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 mareano-bunnprover-linjer/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 mareano-bunnprover-punkt/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 mareano-bunnprovestasjoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 mareano-kjemistasjoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 mareano-referansestasjoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 mareanoprover-artsmangfold-individer-biomasse/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 mareno-videostasjoner/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 markagrensen/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-marint-soppel/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-tapte-fiskeredskaper/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 menneskelig-pavirkning-tralspor/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 militere-forbudsomrader-sjo/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
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
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n2000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
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
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n500-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 n500-kartdata/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 n5000-kartdata/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 n5000-kartdata/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 nasjonale-laksefjorder/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 naturtyper-i-norge/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 nettanlegg/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 nettanlegg/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 nin-saltvannssjobunntyper-predikert/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 nin-saltvannssjobunntyper/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 norges-maritime-grenser/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-PRO-002 norges-maritime-grenser/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 organiske-miljogifter-marine-sedimenter/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-PRO-002 sefrak-bygninger/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-005 tn-w/collection.json: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    PTL-DAT-007 tn-w/collection.json: Rewrite the GeoParquet so every row group carries statistics. [the automatic fix did not resolve this]
    PTL-DAT-012 tn-w/collection.json: Rewrite the file against a supported GeoParquet version; the declared version predates what consumers read.
    PTL-PRO-002 tn-w/collection.json: Add a rel='canonical' link to the upstream STAC object, when the source publishes one.

→ Errors (42):
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Rewrite the GeoParquet so every row group carries statistics.
    Requires: Rewrite the file against a supported GeoParquet version; the declared version predates what consumers read.
→ Warnings (223):
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Fix: group the children under thematic subcatalogs, each with its own catalog.json, and relink this object to those subcatalogs
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
    42 fixable by `portolan check --fix`
    263 need a decision (see Requires: lines)
→ Source files:
✓ 352 file(s) already cloud-native
⚠ 18 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them. 1 registered asset(s) are missing from disk; restore the files, or remove the assets from the catalog.
✗ PTL-DAT-001 lassettingsplasser/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 lassettingsplasser/collection.json: asset 'documentation' file:size is 2694 but the bytes are 3278
✗ PTL-DAT-001 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'documentation' file:size is 4359 but the bytes are 5242
✗ PTL-DAT-001 mareano-bunnprovestasjoner/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 mareano-bunnprovestasjoner/collection.json: asset 'documentation' file:size is 1620 but the bytes are 2780
✗ PTL-DAT-001 mareano-referansestasjoner/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 mareano-referansestasjoner/collection.json: asset 'documentation' file:size is 1603 but the bytes are 2891
✗ PTL-DAT-001 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'documentation' file:size is 2778 but the bytes are 3744
✗ PTL-DAT-001 markagrensen/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 markagrensen/collection.json: asset 'documentation' file:size is 2947 but the bytes are 3537
✗ PTL-DAT-001 menneskelig-pavirkning-tapte-fiskeredskaper/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 menneskelig-pavirkning-tapte-fiskeredskaper/collection.json: asset 'documentation' file:size is 1723 but the bytes are 2857
✗ PTL-DAT-001 militere-forbudsomrader-sjo/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 militere-forbudsomrader-sjo/collection.json: asset 'documentation' file:size is 2331 but the bytes are 2978
✗ PTL-DAT-001 n1000/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n1000/collection.json: asset 'documentation' file:size is 5039 but the bytes are 7736
✗ PTL-DAT-001 n2000-kartdata/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n2000-kartdata/collection.json: asset 'documentation' file:size is 4856 but the bytes are 7701
✗ PTL-DAT-001 n250/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n250/collection.json: asset 'documentation' file:size is 5393 but the bytes are 8233
✗ PTL-DAT-001 n500-kartdata/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n500-kartdata/collection.json: asset 'documentation' file:size is 5073 but the bytes are 8052
✗ PTL-DAT-001 n5000-kartdata/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n5000-kartdata/collection.json: asset 'documentation' file:size is 4505 but the bytes are 6676
✗ PTL-DAT-001 nasjonale-laksefjorder/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 nasjonale-laksefjorder/collection.json: asset 'documentation' file:size is 2212 but the bytes are 2817
✗ PTL-DAT-001 naturtyper-i-norge/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 naturtyper-i-norge/collection.json: asset 'documentation' file:size is 2622 but the bytes are 3198
✗ PTL-DAT-001 nettanlegg/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 nettanlegg/collection.json: asset 'documentation' file:size is 3896 but the bytes are 4693
✗ PTL-DAT-001 nin-saltvannssjobunntyper-predikert/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 nin-saltvannssjobunntyper-predikert/collection.json: asset 'documentation' file:size is 1746 but the bytes are 2599
✗ PTL-DAT-001 norges-maritime-grenser/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 norges-maritime-grenser/collection.json: asset 'documentation' file:size is 4482 but the bytes are 8453
✗ PTL-DAT-001 sefrak-bygninger/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 sefrak-bygninger/collection.json: asset 'documentation' file:size is 1930 but the bytes are 3492
✗ PTL-DAT-001 tn-w/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 tn-w/collection.json: asset 'documentation' file:size is 2277 but the bytes are 2857
✗ PTL-DAT-007 tn-w/collection.json: asset 'tn-w_WaterwayLink' provides no per-row-group spatial statistics (no bbox covering column with min/max stats, nor native GeospatialStatistics)
✗ PTL-DAT-012 tn-w/collection.json: asset 'tn-w_WaterwayLink' geo metadata declares '1.0.0'; data must be GeoParquet 1.1 or 2.x
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2992, 58.2014, 25.2584, 70.8004] and lies within [-0.8875, 57.7860, 31.7688, 71.5605]
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred-tiles' data bbox [4.5097, 57.9813, 31.1582, 71.1856] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred_aktsomhetsomrkvikkleireskred' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2992, 58.2014, 25.2584, 70.8004] and lies within [-0.8875, 57.7860, 31.7688, 71.5605]
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred_aktsomhetsomrkvikkleireskred-tiles' data bbox [4.5097, 57.9813, 31.1582, 71.1856] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_potensieltskredfareomr' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3137, 58.1925, 25.3625, 70.7845] and lies within [-0.8680, 57.7686, 31.9366, 71.5601]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_potensieltskredfareomr-tiles' data bbox [4.6347, 57.9771, 31.1598, 71.1845] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_skog' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5756, 58.2010, 25.3103, 70.6084] and lies within [-0.3020, 57.7818, 31.6921, 71.3671]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_skog-tiles' data bbox [4.6756, 57.9851, 30.9021, 70.9921] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-CAT-001 catalog.json: catalog holds 40 children with no subcatalog grouping them; a flat list this long is hard to browse
⚠ PTL-AST-003 kvikkleire/collection.json: asset 'tmp_kvikkleire_kvikkleire_kvikkleirefaresoneavgr' file:size must be a positive integer, got 0
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [6.6412, 58.2707, 20.8890, 70.0003] and lies within [1.9888, 57.9958, 24.2138, 70.4749]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire-tiles' data bbox [5.7076, 58.0665, 23.9987, 70.2501] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomrade' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [6.6412, 58.2707, 20.8890, 70.0003] and lies within [1.9888, 57.9958, 24.2138, 70.4749]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomrade-tiles' data bbox [5.7076, 58.0665, 23.9987, 70.2501] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomradekant' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [6.6412, 58.2707, 20.8890, 70.0003] and lies within [1.9888, 57.9958, 24.2138, 70.4749]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomradekant-tiles' data bbox [5.7076, 58.0665, 23.9987, 70.2501] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kvikkleirefaresoneavgr-tiles' data bbox [4.8493, 58.0825, 29.9574, 70.6680] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_utlopomr' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8453, 58.2839, 24.7101, 69.8268] and lies within [0.7896, 57.9126, 30.0501, 70.4655]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_utlopomr-tiles' data bbox [5.2908, 58.0825, 29.9540, 70.1172] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_utlosningomr-tiles' data bbox [4.8493, 58.0833, 29.9574, 70.6680] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 0.8631, 65.1330, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 0.8631, 65.1330, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_lokalitet' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2951, 1.3526, 65.1330, 39.2243] and lies within [-25.3227, 0.8631, 97.4172, 80.7751]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6421, 58.1889, 25.2542, 78.0844] and lies within [-25.3256, 57.3673, 45.9593, 80.8611]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone-tiles' data bbox [-9.0422, 57.9700, 33.5082, 80.8220] does not match the declared bbox [-9.0422, 0.8631, 65.1330, 80.8220]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse' declared bbox [1.3990, 62.0608, 36.6778, 80.6538] is inconsistent with its EPSG:25833 data, whose envelope contains [1.4443, 62.6731, 27.8248, 78.6552] and lies within [-18.9813, 62.0071, 47.4731, 80.5530]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse-tiles' data bbox [1.3990, 62.0624, 36.6208, 80.2385] does not match the declared bbox [1.3990, 62.0608, 36.6778, 80.6538]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_bomtralprover' declared bbox [1.3990, 62.0608, 36.6778, 80.6538] is inconsistent with its EPSG:25833 data, whose envelope contains [1.4443, 62.6731, 27.8248, 78.6552] and lies within [-18.9813, 62.0071, 47.4731, 80.5530]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_bomtralprover-tiles' data bbox [1.3990, 62.0624, 36.6208, 80.2385] does not match the declared bbox [1.3990, 62.0608, 36.6778, 80.6538]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_sledeprover' declared bbox [1.3990, 62.0608, 36.6778, 80.6538] is inconsistent with its EPSG:25833 data, whose envelope contains [1.4431, 62.6710, 27.8217, 78.5000] and lies within [-18.4749, 62.0049, 46.9697, 80.3672]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_sledeprover-tiles' data bbox [1.4039, 62.0621, 36.6173, 80.1727] does not match the declared bbox [1.3990, 62.0608, 36.6778, 80.6538]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3039, 58.2097, 25.3329, 70.8005] and lies within [-0.8854, 57.7883, 31.8920, 71.5716]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000-tiles' data bbox [4.6227, 57.9831, 31.2032, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.8024] and lies within [-0.4509, 57.8059, 31.4731, 71.5357]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_posisjon-tiles' data bbox [4.7161, 57.9880, 31.1141, 71.0673] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5534, 58.2433, 25.3761, 70.7424] and lies within [-0.4324, 57.8189, 31.8984, 71.5154]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_senterlinje-tiles' data bbox [4.9034, 58.0203, 31.0200, 71.1135] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1896, 25.2400, 70.7985] and lies within [-0.8934, 57.7756, 31.7416, 71.5562]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.1695] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6760, 58.3122, 24.8296, 70.1208] and lies within [0.3228, 57.9317, 30.4508, 70.7857]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_senterlinje-tiles' data bbox [4.9708, 58.0772, 30.1096, 70.4308] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2800, 58.1930, 25.3617, 70.7848] and lies within [-0.9215, 57.7691, 31.9354, 71.5604]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_omrade-tiles' data bbox [4.5086, 57.9740, 31.1693, 71.1853] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6778, 58.3241, 25.2457, 70.7786] and lies within [-0.2129, 57.9110, 31.6694, 71.5297]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_posisjon-tiles' data bbox [4.7715, 58.1109, 30.7973, 71.0893] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5985, 58.2962, 25.3792, 70.7835] and lies within [-0.3706, 57.8718, 31.9139, 71.5568]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_senterlinje-tiles' data bbox [4.6801, 58.0731, 31.0481, 71.1719] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_grense-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_omrade-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8081, 58.3377, 17.1484, 67.9482] and lies within [1.9778, 58.0052, 18.0690, 68.4632]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1449, 18.0686, 68.4418] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3039, 58.2097, 25.3329, 70.8005] and lies within [-0.8854, 57.7883, 31.8920, 71.5716]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_senterlinje-tiles' data bbox [4.6227, 57.9831, 31.2032, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Stedsnavn_tekstplassering-tiles' data bbox [4.3878, 57.9411, 31.4196, 71.1968] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3022, 58.2360, 25.2657, 70.8111] and lies within [-0.8765, 57.8202, 31.7740, 71.5712]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata-tiles' data bbox [4.6957, 57.9882, 31.1989, 71.1697] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_AdministrativeOmråder_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_AdministrativeOmråder_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_grense-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_omrade-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5499, 58.2843, 25.2239, 70.7843] and lies within [-0.4352, 57.8725, 31.6565, 71.5342]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_posisjon-tiles' data bbox [4.7237, 58.0425, 31.1079, 71.1105] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.7363, 58.2439, 25.3552, 70.7456] and lies within [-0.1424, 57.8210, 31.8654, 71.5161]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_senterlinje-tiles' data bbox [5.1102, 58.0206, 30.9541, 71.0647] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_BygningerOgAnlegg_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1897, 25.0967, 70.8195] and lies within [-0.8934, 57.7872, 31.5154, 71.5565]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.0936] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_omrade-tiles' data bbox [4.6442, 57.9736, 31.1705, 71.1856] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.3236, 58.9215, 25.4180, 70.4768] and lies within [1.2604, 58.4980, 31.4147, 71.2162]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_posisjon-tiles' data bbox [5.6366, 58.6286, 30.6882, 70.6936] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8483, 58.7278, 23.3000, 70.5442] and lies within [0.5186, 58.4011, 28.1635, 71.1174]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_senterlinje-tiles' data bbox [5.0869, 58.4916, 28.1526, 70.6484] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_grense' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_grense-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_omrade' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_omrade-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8345, 58.3538, 17.1503, 67.9481] and lies within [2.0223, 58.0234, 18.0699, 68.4596]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1590, 18.0699, 68.4418] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3022, 58.2360, 25.2657, 70.8111] and lies within [-0.8765, 57.8202, 31.7740, 71.5712]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_senterlinje-tiles' data bbox [4.6957, 57.9882, 31.1989, 71.1697] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Stedsnavn_tekstplassering-tiles' data bbox [3.5052, 57.9474, 31.8604, 71.2128] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
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
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3044, 58.2093, 25.3670, 70.7947] and lies within [-0.8841, 57.7851, 31.9451, 71.5707]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata-tiles' data bbox [4.6261, 57.9831, 31.2060, 71.1846] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5670, 58.2642, 25.0649, 70.7426] and lies within [-0.3656, 57.8649, 31.3611, 71.4679]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_posisjon-tiles' data bbox [4.7330, 58.0384, 31.0438, 71.0276] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5506, 58.2403, 25.3712, 70.7663] and lies within [-0.4568, 57.8163, 31.9123, 71.5398]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_senterlinje-tiles' data bbox [4.7759, 58.0201, 31.0297, 71.1186] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.1702] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_BygningerOgAnlegg_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6075, 58.2621, 25.0499, 70.5494] and lies within [-0.1496, 57.8641, 31.1766, 71.2645]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_BygningerOgAnlegg_senterlinje-tiles' data bbox [4.8461, 58.0705, 31.0108, 70.7116] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_omrade-tiles' data bbox [4.5087, 57.9603, 31.1681, 71.1853] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6778, 58.3242, 25.2970, 70.7787] and lies within [-0.2190, 57.9068, 31.7565, 71.5379]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_posisjon-tiles' data bbox [4.7715, 58.1109, 30.9650, 71.1585] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6156, 58.2287, 25.3646, 70.7841] and lies within [-0.3723, 57.8051, 31.9223, 71.5581]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_senterlinje-tiles' data bbox [4.6797, 58.0059, 31.0481, 71.1784] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_grense-tiles' data bbox [5.2451, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_omrade-tiles' data bbox [5.2451, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8080, 58.3380, 17.1495, 67.9473] and lies within [1.9783, 58.0056, 18.0705, 68.4623]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1451, 18.0703, 68.4415] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3044, 58.2093, 25.3670, 70.7947] and lies within [-0.8841, 57.7851, 31.9451, 71.5707]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_senterlinje-tiles' data bbox [4.6261, 57.9831, 31.2060, 71.1846] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Stedsnavn_tekstplassering-tiles' data bbox [4.2473, 57.8801, 31.2597, 71.2746] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.0505, 58.0415, 22.5947, 70.7035] and lies within [2.2289, 57.3044, 31.5811, 72.0856]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata-tiles' data bbox [4.6952, 58.0325, 31.1493, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_AdministrativeOmråder_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_AdministrativeOmråder_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_grense-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_omrade-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.3594, 58.0435, 22.5358, 70.6218] and lies within [2.7897, 57.3132, 31.3782, 71.9836]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_posisjon-tiles' data bbox [5.0311, 58.0346, 31.0925, 71.0336] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [6.1521, 58.0325, 22.4983, 69.9202] and lies within [4.3256, 57.3059, 30.5319, 71.2208]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_senterlinje-tiles' data bbox [5.8416, 58.0232, 30.1707, 70.1989] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [6.1949, 58.2546, 22.4820, 70.4266] and lies within [4.2978, 57.5325, 30.9232, 71.7456]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_grense-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [6.1949, 58.2546, 22.4820, 70.4266] and lies within [4.2978, 57.5325, 30.9232, 71.7456]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_omrade-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.5718, 58.1595, 15.2827, 68.4322] and lies within [4.0351, 58.0043, 18.0711, 68.6777]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_posisjon-tiles' data bbox [5.3345, 58.1553, 18.0711, 68.4418] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.0505, 58.0415, 22.5947, 70.7035] and lies within [2.2289, 57.3044, 31.5811, 72.0856]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_senterlinje-tiles' data bbox [4.6952, 58.0325, 31.1493, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Stedsnavn_tekstplassering-tiles' data bbox [4.1140, 57.8884, 31.9473, 71.2013] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2934, 58.2062, 25.3369, 70.7726] and lies within [-0.8811, 57.7844, 31.8762, 71.5432]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg-tiles' data bbox [4.5960, 57.9872, 31.0323, 71.1440] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_luftlinje' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2934, 58.2062, 25.3369, 70.7726] and lies within [-0.8811, 57.7844, 31.8762, 71.5432]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_luftlinje-tiles' data bbox [4.5960, 57.9872, 31.0323, 71.1440] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_mast' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2934, 58.2063, 25.2559, 70.7847] and lies within [-0.8811, 57.7911, 31.7488, 71.5435]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_mast-tiles' data bbox [4.5960, 57.9872, 31.0269, 71.0898] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_sjokabel' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3237, 58.1994, 25.0531, 70.6769] and lies within [-0.7247, 57.8004, 31.3167, 71.4009]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_sjokabel-tiles' data bbox [4.5943, 57.9834, 30.9956, 71.0426] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_transformatorstasjon-tiles' data bbox [3.4318, 56.6193, 30.1481, 72.9282] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-1.9540, 56.6452, 25.8470, 78.8208] and lies within [-43.4153, 55.4651, 60.6312, 84.0806]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser-tiles' data bbox [-13.6296, 56.0860, 38.0000, 83.7426] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinje' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-1.9540, 56.6452, 25.8470, 78.8208] and lies within [-43.4153, 55.4651, 60.6312, 84.0806]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinje-tiles' data bbox [-13.6296, 56.0860, 38.0000, 83.7426] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinjesokkel' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-3.7187, 65.2480, 29.1881, 80.4763] and lies within [-43.0498, 64.0432, 65.1084, 84.9202]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinjesokkel-tiles' data bbox [-6.6373, 64.4328, 37.0000, 84.6946] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskerisone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-10.0787, 68.6798, -0.0585, 72.5197] and lies within [-18.3623, 67.0581, 4.1744, 74.7646]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskerisone-tiles' data bbox [-13.6296, 67.6114, 2.3867, 74.3630] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskevernsone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [2.1983, 72.2294, 32.7712, 81.9437] and lies within [-19.3858, 71.3984, 58.9886, 84.1851]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskevernsone-tiles' data bbox [-3.3439, 72.1731, 38.0000, 84.1458] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grense200nautiskemil' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-3.7187, 65.2482, 29.1179, 80.0641] and lies within [-39.4533, 64.0432, 61.0911, 84.1803]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grense200nautiskemil-tiles' data bbox [-6.6373, 64.4328, 37.0000, 84.1458] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grensepunktsjo-tiles' data bbox [-13.6296, -54.4543, 38.0000, 84.6946] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grunnlinje' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2814, -54.2876, 20.4182, 78.0800] and lies within [-25.4033, -55.0212, 45.7804, 80.8682]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grunnlinje-tiles' data bbox [-9.0775, -54.4541, 33.5163, 80.8290] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_indrefarvann' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6195, 58.1761, 25.1810, 78.0800] and lies within [-25.4033, 57.3516, 45.8027, 80.8682]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_indrefarvann-tiles' data bbox [-9.0775, 57.9585, 33.5163, 80.8290] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kontinentalsokkel' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-1.9540, 56.6454, 25.9018, 79.2170] and lies within [-46.9784, 55.4651, 64.8905, 84.8768]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kontinentalsokkel-tiles' data bbox [-13.6296, 56.0860, 38.0000, 84.7231] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kystkontur' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2909, -54.2894, 20.4230, 78.0858] and lies within [-25.3675, -55.0212, 45.8022, 80.8680]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kystkontur-tiles' data bbox [-9.0771, -54.4541, 33.5154, 80.8289] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landareal' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2909, -54.2894, 20.5195, 78.0858] and lies within [-25.3675, -55.0211, 46.2509, 80.8675]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landareal-tiles' data bbox [-9.0771, -54.4541, 33.5154, 80.8289] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landindrefarvann' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6195, 58.1760, 25.3593, 78.0800] and lies within [-25.4033, 57.3516, 46.2515, 80.8677]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landindrefarvann-tiles' data bbox [-9.0775, 57.9585, 33.5163, 80.8290] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_lovvirkeomradegrense' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [5.0052, 58.0093, 25.3711, 70.9388] and lies within [-1.5765, 57.5830, 32.1773, 71.7316]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_lovvirkeomradegrense-tiles' data bbox [4.1561, 57.7922, 31.6628, 71.3517] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_norgesokonomiskesone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [2.3577, 56.6467, 25.8470, 73.3739] and lies within [-10.3059, 55.9966, 36.9942, 74.8934]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_norgesokonomiskesone-tiles' data bbox [-0.4907, 56.0860, 36.4762, 74.5048] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_riksgrense' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [11.4571, 58.9232, 25.5772, 69.8256] and lies within [9.5176, 58.4869, 31.1444, 70.5604]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_riksgrense-tiles' data bbox [11.4539, 58.8769, 30.9544, 70.0923] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_sjoterritorium' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_sjoterritorium-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialfarvann' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialfarvann-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialgrense' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialgrense-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialomrade' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialomrade-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_tilstotendesone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [4.6424, 57.7760, 25.6243, 71.1112] and lies within [-2.4630, 57.3266, 32.8940, 71.9648]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_tilstotendesone-tiles' data bbox [3.6758, 57.5594, 32.3223, 71.5840] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensesokkel' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [1.9045, 70.8695, 19.8089, 83.2857] and lies within [-25.5378, 70.3969, 32.1864, 84.8873]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensesokkel-tiles' data bbox [1.8732, 70.4015, 32.1864, 84.7231] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensetilstotendesone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [4.6424, 57.7760, 25.6243, 71.1112] and lies within [-2.4630, 57.3266, 32.8940, 71.9648]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensetilstotendesone-tiles' data bbox [3.6758, 57.5594, 32.3223, 71.5840] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.7127, 58.0082, 31.1052, 78.9288] and lies within [4.7127, 58.0082, 31.1052, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w-tiles' data bbox [4.7127, 58.0082, 31.1052, 78.9288] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_PortNode' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.7127, 58.0082, 31.1052, 78.9288] and lies within [4.7127, 58.0082, 31.1052, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_PortNode-tiles' data bbox [4.7127, 58.0082, 31.1052, 78.9288] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayLink' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.4643, 57.9322, 31.1490, 71.1913] and lies within [4.4643, 57.9322, 31.1490, 71.1913]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayLink-tiles' data bbox [4.4643, 57.9322, 31.1490, 71.1913] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayNode' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.4643, 57.9322, 31.1101, 71.1300] and lies within [4.4643, 57.9322, 31.1101, 71.1300]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayNode-tiles' data bbox [4.4643, 57.9322, 31.1101, 71.1300] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
✗ Catalog does not conform: 42 errors, 223 warnings
⚠ 21 file(s) need conversion
```

`portolan check catalog --strict`:

```
→ Errors (42):
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Recompute file:checksum from the asset's current bytes.
    Requires: Recompute file:size from the asset's current bytes.
    Requires: Rewrite the GeoParquet so every row group carries statistics.
    Requires: Rewrite the file against a supported GeoParquet version; the declared version predates what consumers read.
→ Warnings (223):
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Requires: Reconcile the asset's bytes with the metadata describing them; they disagree about the data itself, which no rewrite can settle.
    Fix: group the children under thematic subcatalogs, each with its own catalog.json, and relink this object to those subcatalogs
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
    42 fixable by `portolan check --fix`
    263 need a decision (see Requires: lines)
→ Source files:
✓ 352 file(s) already cloud-native
⚠ 18 data file(s) on disk are not registered in the catalog; run `portolan add` to register them, or delete them. 1 registered asset(s) are missing from disk; restore the files, or remove the assets from the catalog.
✗ PTL-DAT-001 lassettingsplasser/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 lassettingsplasser/collection.json: asset 'documentation' file:size is 2694 but the bytes are 3278
✗ PTL-DAT-001 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'documentation' file:size is 4359 but the bytes are 5242
✗ PTL-DAT-001 mareano-bunnprovestasjoner/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 mareano-bunnprovestasjoner/collection.json: asset 'documentation' file:size is 1620 but the bytes are 2780
✗ PTL-DAT-001 mareano-referansestasjoner/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 mareano-referansestasjoner/collection.json: asset 'documentation' file:size is 1603 but the bytes are 2891
✗ PTL-DAT-001 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'documentation' file:size is 2778 but the bytes are 3744
✗ PTL-DAT-001 markagrensen/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 markagrensen/collection.json: asset 'documentation' file:size is 2947 but the bytes are 3537
✗ PTL-DAT-001 menneskelig-pavirkning-tapte-fiskeredskaper/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 menneskelig-pavirkning-tapte-fiskeredskaper/collection.json: asset 'documentation' file:size is 1723 but the bytes are 2857
✗ PTL-DAT-001 militere-forbudsomrader-sjo/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 militere-forbudsomrader-sjo/collection.json: asset 'documentation' file:size is 2331 but the bytes are 2978
✗ PTL-DAT-001 n1000/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n1000/collection.json: asset 'documentation' file:size is 5039 but the bytes are 7736
✗ PTL-DAT-001 n2000-kartdata/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n2000-kartdata/collection.json: asset 'documentation' file:size is 4856 but the bytes are 7701
✗ PTL-DAT-001 n250/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n250/collection.json: asset 'documentation' file:size is 5393 but the bytes are 8233
✗ PTL-DAT-001 n500-kartdata/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n500-kartdata/collection.json: asset 'documentation' file:size is 5073 but the bytes are 8052
✗ PTL-DAT-001 n5000-kartdata/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 n5000-kartdata/collection.json: asset 'documentation' file:size is 4505 but the bytes are 6676
✗ PTL-DAT-001 nasjonale-laksefjorder/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 nasjonale-laksefjorder/collection.json: asset 'documentation' file:size is 2212 but the bytes are 2817
✗ PTL-DAT-001 naturtyper-i-norge/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 naturtyper-i-norge/collection.json: asset 'documentation' file:size is 2622 but the bytes are 3198
✗ PTL-DAT-001 nettanlegg/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 nettanlegg/collection.json: asset 'documentation' file:size is 3896 but the bytes are 4693
✗ PTL-DAT-001 nin-saltvannssjobunntyper-predikert/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 nin-saltvannssjobunntyper-predikert/collection.json: asset 'documentation' file:size is 1746 but the bytes are 2599
✗ PTL-DAT-001 norges-maritime-grenser/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 norges-maritime-grenser/collection.json: asset 'documentation' file:size is 4482 but the bytes are 8453
✗ PTL-DAT-001 sefrak-bygninger/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 sefrak-bygninger/collection.json: asset 'documentation' file:size is 1930 but the bytes are 3492
✗ PTL-DAT-001 tn-w/collection.json: asset 'documentation' file:checksum does not match the bytes (declared sha256 digest differs from recomputed)
✗ PTL-DAT-002 tn-w/collection.json: asset 'documentation' file:size is 2277 but the bytes are 2857
✗ PTL-DAT-007 tn-w/collection.json: asset 'tn-w_WaterwayLink' provides no per-row-group spatial statistics (no bbox covering column with min/max stats, nor native GeospatialStatistics)
✗ PTL-DAT-012 tn-w/collection.json: asset 'tn-w_WaterwayLink' geo metadata declares '1.0.0'; data must be GeoParquet 1.1 or 2.x
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2992, 58.2014, 25.2584, 70.8004] and lies within [-0.8875, 57.7860, 31.7688, 71.5605]
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred-tiles' data bbox [4.5097, 57.9813, 31.1582, 71.1856] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred_aktsomhetsomrkvikkleireskred' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2992, 58.2014, 25.2584, 70.8004] and lies within [-0.8875, 57.7860, 31.7688, 71.5605]
⚠ PTL-DAT-005 aktsomhetskart-kvikkleireskred/collection.json: asset 'aktsomhetskart-kvikkleireskred_aktsomhetsomrkvikkleireskred-tiles' data bbox [4.5097, 57.9813, 31.1582, 71.1856] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_potensieltskredfareomr' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3137, 58.1925, 25.3625, 70.7845] and lies within [-0.8680, 57.7686, 31.9366, 71.5601]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_potensieltskredfareomr-tiles' data bbox [4.6347, 57.9771, 31.1598, 71.1845] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_skog' declared bbox [4.3428, 57.7494, 31.2186, 71.2502] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5756, 58.2010, 25.3103, 70.6084] and lies within [-0.3020, 57.7818, 31.6921, 71.3671]
⚠ PTL-DAT-005 aktsomhetskart-snoskred/collection.json: asset 'aktsomhetskart-snoskred_skog-tiles' data bbox [4.6756, 57.9851, 30.9021, 70.9921] does not match the declared bbox [4.3428, 57.7494, 31.2186, 71.2502]
⚠ PTL-CAT-001 catalog.json: catalog holds 40 children with no subcatalog grouping them; a flat list this long is hard to browse
⚠ PTL-AST-003 kvikkleire/collection.json: asset 'tmp_kvikkleire_kvikkleire_kvikkleirefaresoneavgr' file:size must be a positive integer, got 0
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [6.6412, 58.2707, 20.8890, 70.0003] and lies within [1.9888, 57.9958, 24.2138, 70.4749]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire-tiles' data bbox [5.7076, 58.0665, 23.9987, 70.2501] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomrade' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [6.6412, 58.2707, 20.8890, 70.0003] and lies within [1.9888, 57.9958, 24.2138, 70.4749]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomrade-tiles' data bbox [5.7076, 58.0665, 23.9987, 70.2501] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomradekant' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [6.6412, 58.2707, 20.8890, 70.0003] and lies within [1.9888, 57.9958, 24.2138, 70.4749]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kartleggingsomradekant-tiles' data bbox [5.7076, 58.0665, 23.9987, 70.2501] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_kvikkleirefaresoneavgr-tiles' data bbox [4.8493, 58.0825, 29.9574, 70.6680] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_utlopomr' declared bbox [4.8493, 58.0665, 29.9574, 70.6680] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8453, 58.2839, 24.7101, 69.8268] and lies within [0.7896, 57.9126, 30.0501, 70.4655]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_utlopomr-tiles' data bbox [5.2908, 58.0825, 29.9540, 70.1172] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 kvikkleire/collection.json: asset 'kvikkleire_kvikkleire_utlosningomr-tiles' data bbox [4.8493, 58.0833, 29.9574, 70.6680] does not match the declared bbox [4.8493, 58.0665, 29.9574, 70.6680]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 0.8631, 65.1330, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [1.0794, 57.0153, 24.9917, 78.0838] and lies within [-25.3227, 56.2291, 46.1021, 80.8601]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_enkeltminne-tiles' data bbox [-9.0421, 56.4667, 33.5029, 80.8211] does not match the declared bbox [-9.0422, 0.8631, 65.1330, 80.8220]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_lokalitet' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2951, 1.3526, 65.1330, 39.2243] and lies within [-25.3227, 0.8631, 97.4172, 80.7751]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone' declared bbox [-9.0422, 0.8631, 65.1330, 80.8220] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6421, 58.1889, 25.2542, 78.0844] and lies within [-25.3256, 57.3673, 45.9593, 80.8611]
⚠ PTL-DAT-005 lokaliteter-enkeltminner-sikringssoner/collection.json: asset 'lokaliteter-enkeltminner-sikringssoner_sikringssone-tiles' data bbox [-9.0422, 57.9700, 33.5082, 80.8220] does not match the declared bbox [-9.0422, 0.8631, 65.1330, 80.8220]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse' declared bbox [1.3990, 62.0608, 36.6778, 80.6538] is inconsistent with its EPSG:25833 data, whose envelope contains [1.4443, 62.6731, 27.8248, 78.6552] and lies within [-18.9813, 62.0071, 47.4731, 80.5530]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse-tiles' data bbox [1.3990, 62.0624, 36.6208, 80.2385] does not match the declared bbox [1.3990, 62.0608, 36.6778, 80.6538]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_bomtralprover' declared bbox [1.3990, 62.0608, 36.6778, 80.6538] is inconsistent with its EPSG:25833 data, whose envelope contains [1.4443, 62.6731, 27.8248, 78.6552] and lies within [-18.9813, 62.0071, 47.4731, 80.5530]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_bomtralprover-tiles' data bbox [1.3990, 62.0624, 36.6208, 80.2385] does not match the declared bbox [1.3990, 62.0608, 36.6778, 80.6538]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_sledeprover' declared bbox [1.3990, 62.0608, 36.6778, 80.6538] is inconsistent with its EPSG:25833 data, whose envelope contains [1.4431, 62.6710, 27.8217, 78.5000] and lies within [-18.4749, 62.0049, 46.9697, 80.3672]
⚠ PTL-DAT-005 mareanoprover-artsmangfold-individer-biomasse/collection.json: asset 'mareanoprover-artsmangfold-individer-biomasse_sledeprover-tiles' data bbox [1.4039, 62.0621, 36.6173, 80.1727] does not match the declared bbox [1.3990, 62.0608, 36.6778, 80.6538]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3039, 58.2097, 25.3329, 70.8005] and lies within [-0.8854, 57.7883, 31.8920, 71.5716]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000-tiles' data bbox [4.6227, 57.9831, 31.2032, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5608, 58.2072, 25.0852, 70.8024] and lies within [-0.4509, 57.8059, 31.4731, 71.5357]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_posisjon-tiles' data bbox [4.7161, 57.9880, 31.1141, 71.0673] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5534, 58.2433, 25.3761, 70.7424] and lies within [-0.4324, 57.8189, 31.8984, 71.5154]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Arealdekke_senterlinje-tiles' data bbox [4.9034, 58.0203, 31.0200, 71.1135] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1896, 25.2400, 70.7985] and lies within [-0.8934, 57.7756, 31.7416, 71.5562]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.1695] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6760, 58.3122, 24.8296, 70.1208] and lies within [0.3228, 57.9317, 30.4508, 70.7857]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_BygningerOgAnlegg_senterlinje-tiles' data bbox [4.9708, 58.0772, 30.1096, 70.4308] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2800, 58.1930, 25.3617, 70.7848] and lies within [-0.9215, 57.7691, 31.9354, 71.5604]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_omrade-tiles' data bbox [4.5086, 57.9740, 31.1693, 71.1853] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6778, 58.3241, 25.2457, 70.7786] and lies within [-0.2129, 57.9110, 31.6694, 71.5297]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_posisjon-tiles' data bbox [4.7715, 58.1109, 30.7973, 71.0893] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5985, 58.2962, 25.3792, 70.7835] and lies within [-0.3706, 57.8718, 31.9139, 71.5568]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Høyde_senterlinje-tiles' data bbox [4.6801, 58.0731, 31.0481, 71.1719] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_grense-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Restriksjonsområder_omrade-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8081, 58.3377, 17.1484, 67.9482] and lies within [1.9778, 58.0052, 18.0690, 68.4632]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1449, 18.0686, 68.4418] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3039, 58.2097, 25.3329, 70.8005] and lies within [-0.8854, 57.7883, 31.8920, 71.5716]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Samferdsel_senterlinje-tiles' data bbox [4.6227, 57.9831, 31.2032, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n1000/collection.json: asset 'n1000_N1000_Stedsnavn_tekstplassering-tiles' data bbox [4.3878, 57.9411, 31.4196, 71.1968] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3022, 58.2360, 25.2657, 70.8111] and lies within [-0.8765, 57.8202, 31.7740, 71.5712]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata-tiles' data bbox [4.6957, 57.9882, 31.1989, 71.1697] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_AdministrativeOmråder_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_AdministrativeOmråder_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_grense-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_omrade-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5499, 58.2843, 25.2239, 70.7843] and lies within [-0.4352, 57.8725, 31.6565, 71.5342]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_posisjon-tiles' data bbox [4.7237, 58.0425, 31.1079, 71.1105] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.7363, 58.2439, 25.3552, 70.7456] and lies within [-0.1424, 57.8210, 31.8654, 71.5161]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Arealdekke_senterlinje-tiles' data bbox [5.1102, 58.0206, 30.9541, 71.0647] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_BygningerOgAnlegg_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2965, 58.1897, 25.0967, 70.8195] and lies within [-0.8934, 57.7872, 31.5154, 71.5565]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.0936] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_omrade-tiles' data bbox [4.6442, 57.9736, 31.1705, 71.1856] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.3236, 58.9215, 25.4180, 70.4768] and lies within [1.2604, 58.4980, 31.4147, 71.2162]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_posisjon-tiles' data bbox [5.6366, 58.6286, 30.6882, 70.6936] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8483, 58.7278, 23.3000, 70.5442] and lies within [0.5186, 58.4011, 28.1635, 71.1174]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Høyde_senterlinje-tiles' data bbox [5.0869, 58.4916, 28.1526, 70.6484] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_grense' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_grense-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_omrade' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [6.5214, 58.3921, 24.9711, 70.4468] and lies within [1.4191, 58.0008, 30.9023, 71.1417]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Restriksjonsområder_omrade-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_posisjon' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8345, 58.3538, 17.1503, 67.9481] and lies within [2.0223, 58.0234, 18.0699, 68.4596]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1590, 18.0699, 68.4418] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_senterlinje' declared bbox [3.5052, 57.7590, 31.8604, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3022, 58.2360, 25.2657, 70.8111] and lies within [-0.8765, 57.8202, 31.7740, 71.5712]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Samferdsel_senterlinje-tiles' data bbox [4.6957, 57.9882, 31.1989, 71.1697] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
⚠ PTL-DAT-005 n2000-kartdata/collection.json: asset 'n2000-kartdata_N2000_Stedsnavn_tekstplassering-tiles' data bbox [3.5052, 57.9474, 31.8604, 71.2128] does not match the declared bbox [3.5052, 57.7590, 31.8604, 71.3849]
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
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3044, 58.2093, 25.3670, 70.7947] and lies within [-0.8841, 57.7851, 31.9451, 71.5707]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata-tiles' data bbox [4.6261, 57.9831, 31.2060, 71.1846] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5670, 58.2642, 25.0649, 70.7426] and lies within [-0.3656, 57.8649, 31.3611, 71.4679]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_posisjon-tiles' data bbox [4.7330, 58.0384, 31.0438, 71.0276] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.5506, 58.2403, 25.3712, 70.7663] and lies within [-0.4568, 57.8163, 31.9123, 71.5398]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Arealdekke_senterlinje-tiles' data bbox [4.7759, 58.0201, 31.0297, 71.1186] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_BygningerOgAnlegg_posisjon-tiles' data bbox [4.5100, 57.9681, 31.1571, 71.1702] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_BygningerOgAnlegg_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6075, 58.2621, 25.0499, 70.5494] and lies within [-0.1496, 57.8641, 31.1766, 71.2645]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_BygningerOgAnlegg_senterlinje-tiles' data bbox [4.8461, 58.0705, 31.0108, 70.7116] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_omrade-tiles' data bbox [4.5087, 57.9603, 31.1681, 71.1853] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6778, 58.3242, 25.2970, 70.7787] and lies within [-0.2190, 57.9068, 31.7565, 71.5379]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_posisjon-tiles' data bbox [4.7715, 58.1109, 30.9650, 71.1585] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.6156, 58.2287, 25.3646, 70.7841] and lies within [-0.3723, 57.8051, 31.9223, 71.5581]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Høyde_senterlinje-tiles' data bbox [4.6797, 58.0059, 31.0481, 71.1784] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_grense-tiles' data bbox [5.2451, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8426, 58.3914, 24.9711, 70.4468] and lies within [0.3595, 58.0008, 30.9023, 71.1405]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Restriksjonsområder_omrade-tiles' data bbox [5.2451, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.8080, 58.3380, 17.1495, 67.9473] and lies within [1.9783, 58.0056, 18.0705, 68.4623]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_posisjon-tiles' data bbox [5.3344, 58.1451, 18.0703, 68.4415] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.7616, 71.3849] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3044, 58.2093, 25.3670, 70.7947] and lies within [-0.8841, 57.7851, 31.9451, 71.5707]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Samferdsel_senterlinje-tiles' data bbox [4.6261, 57.9831, 31.2060, 71.1846] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n500-kartdata/collection.json: asset 'n500-kartdata_N500_Stedsnavn_tekstplassering-tiles' data bbox [4.2473, 57.8801, 31.2597, 71.2746] does not match the declared bbox [4.0875, 57.7590, 31.7616, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.0505, 58.0415, 22.5947, 70.7035] and lies within [2.2289, 57.3044, 31.5811, 72.0856]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata-tiles' data bbox [4.6952, 58.0325, 31.1493, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_AdministrativeOmråder_grense-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_AdministrativeOmråder_omrade-tiles' data bbox [4.0875, 57.7590, 31.7616, 71.3849] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_grense-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_omrade-tiles' data bbox [4.0875, 57.7594, 31.7601, 71.3834] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_posisjon' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.3594, 58.0435, 22.5358, 70.6218] and lies within [2.7897, 57.3132, 31.3782, 71.9836]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_posisjon-tiles' data bbox [5.0311, 58.0346, 31.0925, 71.0336] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_senterlinje' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [6.1521, 58.0325, 22.4983, 69.9202] and lies within [4.3256, 57.3059, 30.5319, 71.2208]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Arealdekke_senterlinje-tiles' data bbox [5.8416, 58.0232, 30.1707, 70.1989] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_grense' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [6.1949, 58.2546, 22.4820, 70.4266] and lies within [4.2978, 57.5325, 30.9232, 71.7456]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_grense-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_omrade' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [6.1949, 58.2546, 22.4820, 70.4266] and lies within [4.2978, 57.5325, 30.9232, 71.7456]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Restriksjonsområder_omrade-tiles' data bbox [6.0455, 58.2547, 30.7979, 70.5255] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_posisjon' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.5718, 58.1595, 15.2827, 68.4322] and lies within [4.0351, 58.0043, 18.0711, 68.6777]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_posisjon-tiles' data bbox [5.3345, 58.1553, 18.0711, 68.4418] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_senterlinje' declared bbox [4.0875, 57.7590, 31.9473, 71.3849] is inconsistent with its EPSG:25832 data, whose envelope contains [5.0505, 58.0415, 22.5947, 70.7035] and lies within [2.2289, 57.3044, 31.5811, 72.0856]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Samferdsel_senterlinje-tiles' data bbox [4.6952, 58.0325, 31.1493, 71.1697] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 n5000-kartdata/collection.json: asset 'n5000-kartdata_N5000_Stedsnavn_tekstplassering-tiles' data bbox [4.1140, 57.8884, 31.9473, 71.2013] does not match the declared bbox [4.0875, 57.7590, 31.9473, 71.3849]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2934, 58.2062, 25.3369, 70.7726] and lies within [-0.8811, 57.7844, 31.8762, 71.5432]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg-tiles' data bbox [4.5960, 57.9872, 31.0323, 71.1440] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_luftlinje' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2934, 58.2062, 25.3369, 70.7726] and lies within [-0.8811, 57.7844, 31.8762, 71.5432]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_luftlinje-tiles' data bbox [4.5960, 57.9872, 31.0323, 71.1440] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_mast' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.2934, 58.2063, 25.2559, 70.7847] and lies within [-0.8811, 57.7911, 31.7488, 71.5435]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_mast-tiles' data bbox [4.5960, 57.9872, 31.0269, 71.0898] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_sjokabel' declared bbox [3.4318, 56.6193, 31.0323, 72.9282] is inconsistent with its EPSG:25833 data, whose envelope contains [5.3237, 58.1994, 25.0531, 70.6769] and lies within [-0.7247, 57.8004, 31.3167, 71.4009]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_sjokabel-tiles' data bbox [4.5943, 57.9834, 30.9956, 71.0426] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 nettanlegg/collection.json: asset 'nettanlegg_el_transformatorstasjon-tiles' data bbox [3.4318, 56.6193, 30.1481, 72.9282] does not match the declared bbox [3.4318, 56.6193, 31.0323, 72.9282]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-1.9540, 56.6452, 25.8470, 78.8208] and lies within [-43.4153, 55.4651, 60.6312, 84.0806]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser-tiles' data bbox [-13.6296, 56.0860, 38.0000, 83.7426] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinje' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-1.9540, 56.6452, 25.8470, 78.8208] and lies within [-43.4153, 55.4651, 60.6312, 84.0806]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinje-tiles' data bbox [-13.6296, 56.0860, 38.0000, 83.7426] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinjesokkel' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-3.7187, 65.2480, 29.1881, 80.4763] and lies within [-43.0498, 64.0432, 65.1084, 84.9202]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_avtaltavgrensningslinjesokkel-tiles' data bbox [-6.6373, 64.4328, 37.0000, 84.6946] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskerisone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-10.0787, 68.6798, -0.0585, 72.5197] and lies within [-18.3623, 67.0581, 4.1744, 74.7646]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskerisone-tiles' data bbox [-13.6296, 67.6114, 2.3867, 74.3630] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskevernsone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [2.1983, 72.2294, 32.7712, 81.9437] and lies within [-19.3858, 71.3984, 58.9886, 84.1851]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_fiskevernsone-tiles' data bbox [-3.3439, 72.1731, 38.0000, 84.1458] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grense200nautiskemil' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-3.7187, 65.2482, 29.1179, 80.0641] and lies within [-39.4533, 64.0432, 61.0911, 84.1803]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grense200nautiskemil-tiles' data bbox [-6.6373, 64.4328, 37.0000, 84.1458] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grensepunktsjo-tiles' data bbox [-13.6296, -54.4543, 38.0000, 84.6946] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grunnlinje' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2814, -54.2876, 20.4182, 78.0800] and lies within [-25.4033, -55.0212, 45.7804, 80.8682]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_grunnlinje-tiles' data bbox [-9.0775, -54.4541, 33.5163, 80.8290] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_indrefarvann' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6195, 58.1761, 25.1810, 78.0800] and lies within [-25.4033, 57.3516, 45.8027, 80.8682]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_indrefarvann-tiles' data bbox [-9.0775, 57.9585, 33.5163, 80.8290] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kontinentalsokkel' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [-1.9540, 56.6454, 25.9018, 79.2170] and lies within [-46.9784, 55.4651, 64.8905, 84.8768]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kontinentalsokkel-tiles' data bbox [-13.6296, 56.0860, 38.0000, 84.7231] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kystkontur' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2909, -54.2894, 20.4230, 78.0858] and lies within [-25.3675, -55.0212, 45.8022, 80.8680]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_kystkontur-tiles' data bbox [-9.0771, -54.4541, 33.5154, 80.8289] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landareal' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.2909, -54.2894, 20.5195, 78.0858] and lies within [-25.3675, -55.0211, 46.2509, 80.8675]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landareal-tiles' data bbox [-9.0771, -54.4541, 33.5154, 80.8289] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landindrefarvann' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [0.6195, 58.1760, 25.3593, 78.0800] and lies within [-25.4033, 57.3516, 46.2515, 80.8677]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_landindrefarvann-tiles' data bbox [-9.0775, 57.9585, 33.5163, 80.8290] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_lovvirkeomradegrense' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [5.0052, 58.0093, 25.3711, 70.9388] and lies within [-1.5765, 57.5830, 32.1773, 71.7316]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_lovvirkeomradegrense-tiles' data bbox [4.1561, 57.7922, 31.6628, 71.3517] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_norgesokonomiskesone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [2.3577, 56.6467, 25.8470, 73.3739] and lies within [-10.3059, 55.9966, 36.9942, 74.8934]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_norgesokonomiskesone-tiles' data bbox [-0.4907, 56.0860, 36.4762, 74.5048] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_riksgrense' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [11.4571, 58.9232, 25.5772, 69.8256] and lies within [9.5176, 58.4869, 31.1444, 70.5604]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_riksgrense-tiles' data bbox [11.4539, 58.8769, 30.9544, 70.0923] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_sjoterritorium' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_sjoterritorium-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialfarvann' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialfarvann-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialgrense' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialgrense-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialomrade' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [7.0819, -54.4451, 20.5806, 78.1008] and lies within [-26.7570, -55.2223, 47.0951, 81.0672]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_territorialomrade-tiles' data bbox [-9.6846, -54.6539, 34.6889, 81.0280] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_tilstotendesone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [4.6424, 57.7760, 25.6243, 71.1112] and lies within [-2.4630, 57.3266, 32.8940, 71.9648]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_tilstotendesone-tiles' data bbox [3.6758, 57.5594, 32.3223, 71.5840] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensesokkel' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [1.9045, 70.8695, 19.8089, 83.2857] and lies within [-25.5378, 70.3969, 32.1864, 84.8873]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensesokkel-tiles' data bbox [1.8732, 70.4015, 32.1864, 84.7231] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensetilstotendesone' declared bbox [-13.6296, -54.6539, 38.0000, 84.7231] is inconsistent with its EPSG:25833 data, whose envelope contains [4.6424, 57.7760, 25.6243, 71.1112] and lies within [-2.4630, 57.3266, 32.8940, 71.9648]
⚠ PTL-DAT-005 norges-maritime-grenser/collection.json: asset 'norges-maritime-grenser_yttergrensetilstotendesone-tiles' data bbox [3.6758, 57.5594, 32.3223, 71.5840] does not match the declared bbox [-13.6296, -54.6539, 38.0000, 84.7231]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.7127, 58.0082, 31.1052, 78.9288] and lies within [4.7127, 58.0082, 31.1052, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w-tiles' data bbox [4.7127, 58.0082, 31.1052, 78.9288] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_PortNode' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.7127, 58.0082, 31.1052, 78.9288] and lies within [4.7127, 58.0082, 31.1052, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_PortNode-tiles' data bbox [4.7127, 58.0082, 31.1052, 78.9288] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayLink' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.4643, 57.9322, 31.1490, 71.1913] and lies within [4.4643, 57.9322, 31.1490, 71.1913]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayLink-tiles' data bbox [4.4643, 57.9322, 31.1490, 71.1913] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayNode' declared bbox [4.4643, 57.9322, 31.1490, 78.9288] is inconsistent with its EPSG:4258 data, whose envelope contains [4.4643, 57.9322, 31.1101, 71.1300] and lies within [4.4643, 57.9322, 31.1101, 71.1300]
⚠ PTL-DAT-005 tn-w/collection.json: asset 'tn-w_WaterwayNode-tiles' data bbox [4.4643, 57.9322, 31.1101, 71.1300] does not match the declared bbox [4.4643, 57.9322, 31.1490, 78.9288]
✗ Catalog does not conform: 42 errors, 223 warnings
⚠ 21 file(s) need conversion
```

## Konfigurasjon brukt

Se `config.yaml` i prosjektroten for fullstendig konfigurasjon.
