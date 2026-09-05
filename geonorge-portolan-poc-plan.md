# PoC-plan: GeoNorge → Portolan SDI

**Mål:** Vise at et utvalg datasett fra GeoNorges nedlastingsteneste kan crawles,
lastes ned og publiseres som en Portolan-katalog (STAC + GeoParquet/COG), som et
konseptbevis på Portolan som alternativ/supplement til GeoNorge som SDI.

Dette dokumentet er skrevet for at en KI-agent (Claude Code el. lign.) skal kunne
implementere det trinn for trinn. Hvert steg har et tydelig mål, forventet input/output,
og "definition of done".

---

## 0. Forutsetninger og viktige presiseringer

Før implementering — disse punktene endrer hvordan løsningen må bygges, og bør
leses før agenten begynner å kode:

1. **Tjenestefeeden er en feed-av-feeds, ikke en feed av filer.**
   `https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml` inneholder ett
   `<entry>` per datasett/format-kombinasjon (f.eks. "Administrative enheter fylker
   2022 GML-format"). Hver entry har en `<link>` som peker til datasettets **egen**
   Atom-feed (f.eks. `.../AdministrativeEnheterFylker2022_AtomFeedGML.xml`). Det er i
   **den** feeden de faktiske nedlastbare filene ligger (ofte splittet på område/fylke,
   projeksjon eller dato). Crawleren må altså gjøre to nivåer av henting:
   nivå 1 = liste over datasett, nivå 2 = liste over faktiske filer per datasett.

2. **`portolan-cli` har ingen GeoNorge/Atom/CSW-extractor.** De innebygde extractorene
   er ArcGIS REST, WFS og CARTO SQL API (`portolan extract arcgis|wfs|carto`). GeoNorge
   sine nedlastingsfiler er statiske filer (GML, SOSI, FGDB, GeoJSON, PostGIS-dump osv.)
   servert over HTTP/S3-lignende lenker — ikke et API som kan "extractes" direkte.
   Konsekvens: nedlasting av rådata er et **eget forrige steg** i denne PoC-en, utenfor
   portolan-cli. Portolan brukes fra og med `portolan add` / `portolan check --fix`.

3. **Metadata-strategi må bygges eksplisitt.** Portolan sin `metadata.yaml` (title,
   description, contact, license, providers, source_url, processing_notes) må fylles
   ut per collection. GeoNorge har denne informasjonen som ISO 19115 XML tilgjengelig
   via CSW (`rel="describedby"`-lenken i hver entry, `GetRecordById`-endepunktet).
   Crawleren bør hente og parse denne slik at Portolan-metadata blir reelt utfylt og
   ikke bare placeholder-tekst — dette er kjernen i "riktig metadata-konvertering"
   som du (Alexander) har bedt om.

4. **Filformat-variasjon.** Samme datasett tilbys ofte i flere format (SOSI, GML,
   FGDB, GeoJSON, PostGIS-dump, evt. Shapefile). For PoC bør vi **prioritere GML og
   GeoJSON** som førstevalg (lesbare med GDAL/OGR uten spesialverktøy), og falle
   tilbake til FGDB om GML ikke finnes. SOSI-only-datasett (rent norsk format, krever
   `ogr2ogr` med SOSI-driver eller `sosicon`) håndteres som en kjent begrensning i
   PoC-en, ikke som blocker.

5. **Volum.** Tjenestefeeden er stor (hundrevis av entries). For PoC laster vi **ikke**
   ned alt — kun et konfigurerbart sample (standard 15–30 datasett), se steg 2.

---

## 1. Arkitektur / pipeline-oversikt

```
┌──────────────────────┐
│ 1. Crawl             │  Hent Tjenestefeed_daglig.xml
│    (nivå 1)          │  → liste over datasett-entries
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 2. Utvalg             │  Velg N datasett (konfigurerbart, default 15-30)
│    (sampling)         │  Filtrer/prioriter på format (GML/GeoJSON først)
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 3. Crawl              │  Hent hvert datasetts EGEN Atom-feed
│    (nivå 2)           │  → faktiske nedlastbare fil-URLer
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 4. Metadata-henting   │  Hent ISO19115 XML via CSW GetRecordById
│                       │  → strukturert metadata per datasett
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 5. Nedlasting         │  Last ned valgte filer til lokal katalogstruktur
│                       │  organisert som Portolan-collections
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 5b. Style-søk         │  Søk Geonorge tegneregel-register etter
│    (SLD/QML/PMTiles)  │  autoritativ kartografi per datasett; fallback default
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 6. Metadata-mapping   │  Map ISO19115 → Portolan metadata.yaml per collection
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 7. Portolan-kjøring   │  portolan init / add / check --fix (inkl. PMTiles +
│                       │  MapLibre-style, jf. steg 5b)
└──────────┬────────────┘
           ▼
┌──────────────────────┐
│ 8. Verifisering       │  portolan check --strict, portolan readme,
│                       │  manuell/automatisk sjekk av resultat
└───────────────────────┘
```

Anbefalt implementasjon: ett Python-prosjekt (`uv`-basert, jf. preferanse) med separate
moduler/script per steg, orkestrert av ett enkelt CLI-script eller `Makefile`/shell-script,
slik at hvert steg kan kjøres og feilsøkes isolert.

```
geonorge-portolan-poc/
├── pyproject.toml
├── config.yaml                  # sample-størrelse, filtre, katalog-output-path
├── src/
│   ├── crawl_feed.py             # steg 1-3
│   ├── fetch_metadata.py         # steg 4
│   ├── download_datasets.py      # steg 5
│   ├── build_metadata_yaml.py    # steg 6
│   └── run_portolan.py           # steg 7 (subprocess wrapper rundt portolan-cli)
├── cache/                        # rå XML-respons (feed nivå 1 og 2, CSW-records)
└── catalog/                      # portolan-katalogen (output)
```

---

## 2. Steg-for-steg spesifikasjon

### Steg 1 — Crawle Tjenestefeed (nivå 1)

**Input:** `https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml`

**Gjør:**
- Last ned XML (ca. noen MB, cache lokalt i `cache/tjenestefeed.xml` med timestamp).
- Parse med `lxml` eller `xml.etree` (namespace-aware: `atom`, `georss`, `inspire_dls`).
- For hver `<entry>`, ekstraher:
  - `title`
  - `summary`
  - `inspire_dls:spatial_dataset_identifier_code` (datasett-ID)
  - `inspire_dls:spatial_dataset_identifier_namespace`
  - `<link>` uten `rel`-attributt → lenke til datasettets EGEN Atom-feed (nivå 2)
  - `<link rel="describedby">` → CSW `GetRecordById`-URL for full ISO19115-metadata
  - `<category term="EPSG:...">` → CRS
  - `rights`, `author/name`, `updated`, `published`

**Output:** En liste (JSON eller in-memory dataclass-liste) av datasett-poster, f.eks.:
```json
{
  "title": "Administrative enheter fylker - historiske data 2022 GML-format",
  "dataset_id": "fylker2022",
  "feed_url": "http://nedlasting.geonorge.no/geonorge/ATOM-feeds/AdministrativeEnheterFylker2022_AtomFeedGML.xml",
  "csw_metadata_url": "https://www.geonorge.no/geonetwork/srv/nor/csw?...&id=2c84d0ad-...",
  "crs": "EPSG:25833",
  "rights": "Kartverket",
  "updated": "2022-12-14T13:09:01"
}
```

**Definition of done:** Script kjørt gir N > 0 poster, og printer et sammendrag
(antall unike datasett-ID-er vs. antall entries — siden samme dataset finnes i
flere formater, er antall entries > antall unike datasett).

**NB:** Flere entries kan dele samme `dataset_id` (som `fylker2022` over, som finnes
i FGDB/GML/GeoJSON/PostGIS/SOSI-varianter). Grupper entries på `dataset_id` slik at
steg 2 kan velge **ett format per datasett** heller enn å telle samme datasett fem ganger.

---

### Steg 2 — Utvalg av sample (konfigurerbart)

**Krav fra deg:** "Laste ned et sample av datasett (15-30 stykker). Bør være konfigurerbart."

**Gjør:**
- Grupper resultatet fra steg 1 på `dataset_id`.
- Konfigurerbare parametre (i `config.yaml` eller CLI-args):
  - `sample_size` (default: 20, range 15-30 anbefalt for PoC)
  - `preferred_formats` (default: `["GML", "GeoJSON", "FGDB"]` — i prioritert rekkefølge)
  - `random_seed` (for reproduserbarhet)
  - evt. `include_pattern` / `exclude_pattern` (regex på title, for å f.eks. luke ut
    "historiske data" som er lite interessant for en PoC, eller motsatt kun ta de)
- For hvert unike `dataset_id`, velg formatet som matcher første treff i
  `preferred_formats`; hvis ingen treff, ta første tilgjengelige og logg en advarsel.
- Trekk `sample_size` datasett (tilfeldig eller de N første — bør være en flag).

**Output:** Filtrert liste med akkurat `sample_size` datasett, ett format valgt per datasett.

**Definition of done:** Kjøring med `--sample-size 20` gir eksakt 20 datasett (eller
færre + advarsel hvis feeden har færre unike datasett enn ønsket).

---

### Steg 3 — Crawle datasettenes egne Atom-feeder (nivå 2)

**Gjør:**
- For hvert valgte datasett, GET `feed_url` fra steg 1.
- Parse denne feeden (samme Atom-namespace, men entries her har direkte
  nedlastbare `<link>`-er, ofte per fylke/kommune/landsdekkende variant).
- Ekstraher per entry:
  - `title` (ofte "Landsdekkende" eller fylkesnavn)
  - nedlastings-URL (selve fil-lenken, `.zip`, `.gml`, `.gdb.zip` osv.)
  - filstørrelse hvis oppgitt
  - CRS/`category`

**Viktig valg for PoC:** De fleste datasett har en "Hele landet" / "Landsdekkende"
variant i tillegg til fylkesoppdelte filer. **Prioriter landsdekkende variant hvis
den finnes**, ellers ta første geografiske del (for å holde volumet nede og
demoen enkel). Gjør dette konfigurerbart (`prefer_national: true`).

**Output:** Per datasett, én (eller noen få) konkrete nedlastings-URL-er.

**Definition of done:** Hvert av de N sample-datasettene har minst én konkret,
nedlastbar fil-URL identifisert.

---

### Steg 4 — Hente full ISO19115-metadata via CSW

**Gjør:**
- For hvert datasett, GET `csw_metadata_url` fra steg 1 (dette er en direkte
  `GetRecordById`-URL, ingen ekstra parametre nødvendig).
- Parse ISO19115/19139 XML-responsen. Nøkkelfelt å hente ut (bruk `lxml` med
  riktige namespaces — `gmd`, `gco`, `srv` osv.):
  - Abstrakt/beskrivelse (`gmd:abstract`)
  - Ansvarlig organisasjon / kontakt (`gmd:contact` → `gmd:organisationName`,
    `gmd:electronicMailAddress`)
  - Lisens (`gmd:resourceConstraints` / `gmd:otherConstraints` — GeoNorge bruker
    ofte klartekst-lisensnavn eller lenke til norge.no/CC-lisens)
  - Bounding box (`gmd:EX_GeographicBoundingBox`)
  - Oppdateringsfrekvens, tidsstempel

**Fallback:** Hvis CSW-parsing blir for kompleks for PoC-omfanget, er det greit å
i første omgang kun bruke `title`, `summary`, `rights`, `author` fra nivå-1-feeden
(steg 1) som metadata-kilde, og heller markere CSW-berikelse som en **stretch goal**
(se avsnitt 4 nedenfor). Men prøv CSW-parsing først — det er der lisens og
kontaktinfo faktisk finnes strukturert.

**Definition of done:** For hvert sample-datasett finnes en utfylt metadata-struktur
(dict/dataclass) med minst: title, description, license (eller "unknown" som fallback),
contact-organisasjon, source_url.

---

### Steg 5 — Nedlasting av datasettfiler

**Gjør:**
- Lag katalogstruktur: `catalog/<dataset_id>/raw/<filnavn>`
- Last ned filen(e) identifisert i steg 3. Strøm til disk i chunks (samme prinsipp
  som du allerede bruker i VM-ingestion-jobben — unngå å laste hele zip-filer i minnet).
- Hvis fil er `.zip`: pakk ut til `catalog/<dataset_id>/raw/` (GML/SOSI/FGDB ligger
  ofte zippet).
- Logg suksess/feil per datasett. Datasett som feiler nedlasting skal **ikke** stoppe
  hele kjøringen — logg og fortsett (samme filosofi som portolan sin retry-logikk
  i eksempelet med Philadelphia).

**Definition of done:** `catalog/<dataset_id>/raw/` finnes og er ikke-tom for
minst 80% av sample-settet (noen datasett vil alltid ha atypiske format/feil —
det er greit for en PoC, bare synliggjør det i sluttrapport).

---

### Steg 5b — Søk etter autoritativ kartografi/styling (for PMTiles)

**Bakgrunn:** `portolan check --fix` genererer PMTiles og en MapLibre-style for
vektor-collections automatisk (jf. "Generate thumbnails, PMTiles, MapLibre styles"
i portolan-cli sin featureliste). Portolan sin auto-genererte style er sannsynligvis
en enkel default (ett enhetlig fyll/strek). Kravet her er å **først forsøke å finne
en autoritativ, offisiell stil for datasettet fra GeoNorge**, og kun falle tilbake
til Portolan sin auto-genererte default-style når ingen autoritativ stil finnes.

**Kilde:** GeoNorge har et eget offentlig register for kartografi/tegneregler:
`https://register.geonorge.no/tegneregler` (norsk NSDI-register, kategori
"Cartography – specifications"), med et maskinlesbart JSON-API på
`https://register.geonorge.no/api/tegneregler` (paginert, ca. 275 oppføringer
i skrivende stund).

**Gjør:**
- Hent (og cache) hele `tegneregler`-registeret via API-et (paginer gjennom alle
  sider — sjekk `Count`/`Total`/`Offset`/`Limit` i responsen for paginering).
- For hvert datasett i sample, match mot registeret på **tittel/produktnavn**
  (fuzzy string-matching, f.eks. `rapidfuzz` i Python — registeret bruker ikke
  samme UUID som CSW-metadataposten, så eksakt ID-match vil ikke fungere).
  Eksempel: datasett-tittel "Administrative enheter fylker 2022" bør matches mot
  registerets `"Administrative enheter Norge"`-oppføring med noe toleranse for
  årstall/formattillegg i tittelen.
- Hvis treff funnet, sjekk feltet `CartographyFile`:
  - Hvis URL-en ender på `.sld` eller `.qml` → dette er en **direkte brukbar
    stilfil**. Last den ned til `catalog/<dataset_id>/.portolan/style.sld` (eller
    tilsvarende).
  - Hvis URL-en peker til `register.geonorge.no/kartografi/files/files?uuid=...`
    → følg lenken og sjekk faktisk MIME-type/filendelse i responsen; kan være SLD,
    men er ofte en zip eller PDF — håndter begge.
  - Hvis eneste treff er `documentreference` som `.pdf` → dette er **kun
    menneskelesbar dokumentasjon**, ikke en maskinlesbar stilfil. Regn dette som
    "ingen autoritativ maskinlesbar stil funnet" for PoC-formål (men logg PDF-en
    i rapporten som "finnes, men krever manuell tolkning" — nyttig for videre arbeid).
- **SLD → MapLibre/PMTiles-styling er ikke en direkte konvertering.** SLD er
  laget for WMS/rasterrendering, ikke vektor-tiles. For PoC er et realistisk
  ambisjonsnivå:
  1. Hvis en SLD faktisk finnes: bruk den i det minste til å utlede **farger og
     evt. klasseinndeling** (f.eks. via `PolygonSymbolizer`/`Fill`/`CssParameter`)
     og oversett manuelt/halvautomatisk et lite sett attributter (fyll, strek,
     stroke-width) til en enkel MapLibre-stil-fil (JSON) som overstyrer Portolans
     auto-genererte style for akkurat den collectionen.
  2. Hvis ingen maskinlesbar stil finnes: **bruk Portolan sin auto-genererte
     default-style uendret** (`portolan check --fix` sin standardoppførsel) —
     dette er den eksplisitte fallback-en du ba om.
- Loggfør per datasett hvorvidt stilen var: `authoritative-sld`, `authoritative-pdf-only`
  (fallback brukt), eller `no-match-found` (fallback brukt).

**Konfigurerbar parameter (legges til i `config.yaml`, se avsnitt 3):**
```yaml
styling:
  enabled: true                      # slå av/på hele steg 5b
  registry_url: "https://register.geonorge.no/api/tegneregler"
  match_threshold: 80                # fuzzy-match score (0-100) for å godta et treff
  fallback: "portolan-default"       # hva som skjer ved manglende/PDF-only treff
```

**Definition of done:** For hvert datasett i sample finnes en logget avgjørelse
(`authoritative-sld` / `authoritative-pdf-only` / `no-match-found`), og for de med
`authoritative-sld` finnes en forsøkt style-fil klar til bruk i steg 7. Ingen
datasett skal mangle en style-strategi (eksplisitt fallback er alltid et gyldig utfall).

---

### Steg 6 — Konvertere til Portolan-metadata-format

**Gjør:**
- For hvert datasett, generer `catalog/<dataset_id>/.portolan/metadata.yaml` med
  feltene portolan-cli forventer (jf. Philadelphia-eksempelet):

```yaml
title: "<fra steg 4/1>"
description: "<fra steg 4 abstract, fallback: steg 1 summary>"
contact:
  name: "<organisasjon fra CSW, fallback: 'Geonorge'>"
  email: "<e-post fra CSW, fallback: 'post@geonorge.no'>"
license: "<SPDX-id hvis identifiserbart, ellers 'other'>"
license_url: "<lenke til norsk lisens/norge digitalt-vilkår hvis 'other'>"
providers:
  - name: "<datakilde-organisasjon, f.eks. Kartverket>"
    roles: ["producer", "licensor"]
    url: "https://www.geonorge.no/"
  - name: "Norkart PoC"
    roles: ["processor", "host"]
    url: "<intern lenke/placeholder>"
source_url: "<original CSW/GeoNorge-datasettside eller feed_url>"
processing_notes: "Hentet fra Geonorge Tjenestefeed (Atom) og konvertert til Portolan-format med portolan-cli."
```

- Skriv også en overordnet `catalog/.portolan/metadata.yaml` for selve katalogen
  (title: "GeoNorge → Portolan PoC", osv.), etter samme mønster som
  `examples/philadelphia-housing/metadata/catalog.yaml`.

**Merk om lisens:** Mesteparten av GeoNorge-data er under **Norsk lisens for
offentlige data (NLOD)**. Sjekk om dette har en SPDX-identifikator (usikker —
verifiser i implementasjonen; hvis ikke, bruk `license: other` med
`license_url` til https://data.norge.no/nlod/no/2.0 eller tilsvarende offisiell
NLOD-side).

**Definition of done:** Hver collection-mappe har en gyldig `metadata.yaml`
som senere passerer `portolan metadata validate`.

---

### Steg 7 — Kjøre portolan-cli

**Forutsetning:** `uv tool install portolan-cli` (eller `uv add` i prosjektet).

**Gjør (i katalogens rotmappe):**
```bash
portolan init --id geonorge-portolan-poc
# For hver collection-mappe med rådata + metadata.yaml på plass:
portolan add --force --thumbnails catalog/<dataset_id>
# Konverter til cloud-native (GeoParquet/COG/PMTiles) + oppdater STAC-metadata:
portolan check catalog --fix --workers 4
```

**Kartografi/PMTiles-styling (jf. steg 5b):** Verifiser i CLI-referansen
(`http://cli.portolan-sdi.org/reference/cli/`) om `portolan check --fix` støtter
et flagg for å angi en egen MapLibre-style eller SLD-fil per collection (f.eks.
noe i retning `--style <path>` eller en `style`-nøkkel i `.portolan/config.yaml`).
Hvis et slikt hook finnes: bruk den autoritative style-en fra steg 5b der den
finnes. Hvis CLI-en **ikke** eksponerer noe slikt hook per i dag (sannsynlig,
gitt alfa-status), er fallback for PoC-en å:
1. La `portolan check --fix` generere sin default PMTiles + MapLibre-style som normalt.
2. Etterpå, for collections med `authoritative-sld` (fra steg 5b), overskriv den
   genererte MapLibre-style-JSON-filen (`catalog/<dataset_id>/style.json` el.
   tilsvarende — bekreft faktisk filnavn/plassering ved å inspisere output fra
   `check --fix` manuelt først) med en style utledet fra SLD-fargene.
3. Dokumenter denne overskrivingen tydelig i `REPORT.md` slik at det er synlig
   at det er et PoC-arbeid rundt en manglende CLI-feature, ikke en innebygd
   Portolan-funksjon.

```bash
# Generer README/AGENTS.md:
(cd catalog && portolan readme)
# Strikt validering:
portolan check catalog --strict
```

**Viktig:** `portolan add` forventer at hver collection-mappe (`catalog/<dataset_id>/`)
inneholder faktiske geodatafiler den kan konvertere (GeoPackage, Shapefile, GML m.fl.
— sjekk `portolan scan`/CLI-referansen for offisielt støttede input-formater før
implementasjon; SOSI vil sannsynligvis IKKE være direkte støttet av portolan-cli og
må evt. konverteres til GeoPackage/GML med `ogr2ogr` som et forbehandlingssteg).

**Definition of done:**
- `portolan check catalog --strict` returnerer exit code 0.
- Katalogen inneholder GeoParquet/COG-filer, STAC-items, README.md og AGENTS.md
  per collection.

---

### Steg 8 — Verifisering og rapport

**Gjør:**
- Kjør `portolan list` og `portolan info <path>` for et par collections, sammenlign
  antall features/attributter mot kjent GeoNorge-metadata (stikkprøve).
- Skriv en kort sluttrapport (`REPORT.md`) som oppsummerer:
  - Antall datasett i sample, antall som lyktes/feilet i hvert steg
  - Hvilke formater som ble håndtert vs. hoppet over (spesielt SOSI-only)
  - Eksempel på før/etter: original GeoNorge-metadata vs. generert Portolan STAC-item
  - Kjente begrensninger (se avsnitt 4)

**Stretch (valgfritt for PoC, men fint å ha):**
- `portolan push` til en Azure Blob Storage-bøtte (S3-kompatibel via
  `PORTOLAN_S3_ENDPOINT`), for å vise hele "serverless"-verdiforslaget i praksis —
  dette kobler også naturlig til din eksisterende Azure-infrastruktur.
- Enkelt DuckDB-query mot den publiserte katalogen (jf. Philadelphia-eksempelet)
  som en liten "bevis at det fungerer"-sjekk.

---

## 3. Konfigurasjon (forslag til `config.yaml`)

```yaml
feed_url: "https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml"
sample:
  size: 20
  preferred_formats: ["GML", "GeoJSON", "FGDB"]
  prefer_national_extent: true
  random_seed: 42
  exclude_title_pattern: "historiske data"   # eksempel: hopp over historiske årganger
paths:
  cache_dir: "./cache"
  catalog_dir: "./catalog"
styling:
  enabled: true
  registry_url: "https://register.geonorge.no/api/tegneregler"
  match_threshold: 80
  fallback: "portolan-default"
portolan:
  catalog_id: "geonorge-portolan-poc"
  push_remote: null   # sett til f.eks. "s3://mybucket/geonorge-poc" for å aktivere push
```

---

## 4. Kjente begrensninger / risiko å avklare tidlig

Disse bør flagges til agenten SLIK AT de ikke oppdages sent i implementasjonen:

1. **SOSI-format** krever spesialverktøy (GDAL SOSI-driver er ikke alltid bygget inn;
   `sosicon` kan trengs). Hvis sample trekker et datasett som *kun* finnes i SOSI,
   bør pipelinen falle tilbake til å hoppe over/logge det, ikke krasje.
2. **portolan-cli sine offisielt støttede input-formater** for `add`/`check --fix`
   må verifiseres direkte mot CLI-referansen (`http://cli.portolan-sdi.org/reference/cli/`)
   før steg 7 implementeres — planen antar GeoPackage/Shapefile/GML/GeoJSON er OK,
   men dette bør dobbeltsjekkes i kode, ikke antas.
3. **CSW-endepunktet** (`www.geonorge.no/geonetwork/srv/nor/csw`) kan ha rate-limiting
   eller kreve littegrann backoff ved mange raske requests — legg inn enkel retry/delay.
4. **Lisensmapping til SPDX** er ikke opplagt for norske offentlige data (NLOD har
   ikke nødvendigvis en offisiell SPDX-ID) — verifiser i implementasjonen, bruk
   `other` + `license_url` som trygt fallback.
5. **Portolan er pre-1.0 / alfa-software** (v1.0.0a0 er nyeste release) — forvent
   endringer i CLI-flagg/oppførsel; lås `portolan-cli`-versjon i `pyproject.toml`
   for reproduserbarhet.
6. **Styling/PMTiles-kilder er i beste fall halvveis maskinlesbare.** GeoNorge sitt
   tegneregel-register er hovedsakelig PDF-dokumentasjon for mennesker, ikke ferdige
   SLD/QML-filer. Bygg derfor pipeline med fallback fra dag én — ikke anta at
   autoritativ styling finnes for de fleste datasett i sample (se steg 3b/6b).

---

## 5. Rekkefølge for KI-agent-implementasjon (anbefalt)

1. Sett opp `uv`-prosjekt + `pyproject.toml` (husk uv-frontmatter i scriptene per
   din vanlige preferanse hvis de skrives som frittstående scripts).
2. Implementer og test steg 1 isolert (bare print antall entries + grupperte
   dataset_id-er) — verifiser antakelsen om feed-av-feeds-strukturen mot ekte data.
3. Implementer steg 2 (sampling) — verifiser konfigurerbarhet med et par ulike
   `sample_size`-verdier.
4. Implementer steg 3 — verifiser at nivå-2-feedene faktisk gir nedlastbare URL-er
   for minst noen av sample-settet.
5. Implementer steg 4 (CSW-metadata) — dette er sannsynligvis den mest skjøre
   delen (XML-namespace-parsing); bygg med god feilhåndtering/fallback fra start.
6. Implementer steg 5 (nedlasting) — gjenbruk streaming-mønsteret fra eksisterende
   VM-ingestion-arbeid.
7. Implementer steg 5b (style-søk) — bygg fuzzy-matching mot tegneregler-registeret
   og loggingen av `authoritative-sld` / `authoritative-pdf-only` / `no-match-found`
   først, uten SLD→MapLibre-oversettelsen; verifiser treffraten i sample-settet før
   du investerer tid i selve fargeoversettelsen (den er kun verdt å bygge hvis nok
   datasett faktisk har `authoritative-sld`-treff).
8. Implementer steg 6 (metadata.yaml-generering) — valider output manuelt mot
   Philadelphia-eksempelets skjema før du går videre.
9. Installer `portolan-cli` (`uv tool install portolan-cli`), kjør steg 7 manuelt
   fra kommandolinjen først (ikke skript det før du vet at `add`/`check --fix`
   faktisk aksepterer inputen din, og før du vet om/hvordan CLI-en lar deg påvirke
   PMTiles-styling).
10. Skript steg 7 som subprocess-wrapper når manuell kjøring virker.
11. Skriv `REPORT.md` (steg 8) — inkluder treffrate for autoritativ styling som
    egen linje i sammendraget.

Denne rekkefølgen sikrer at agenten oppdager format-/API-overraskelser (SOSI,
CSW-XML-skjema, portolan-cli sine faktiske input-krav) tidlig og isolert, i stedet
for i en stor sammenhengende pipeline hvor feilsøking blir vanskelig.
