# PortoGeoNorge - PoC på Cloud Native Portolan SDI av GeoNorge

**TL;DR:**
- 20 datasett og metadata hentet automatisk fra GeoNorge, konvertert til Portolan-SDI og publisert som cloud native-filer (GeoParquet + PMTiles)
- Les mer om Portolan på https://www.portolan-sdi.org/
- Prøv katalogen selv: utforsk den visuelt i [Portolan Browser](https://browser.portolan-sdi.org/#/external/kartaistorage.blob.core.windows.net/skygeo/geonorge2portolan-poc/catalog.json)- La en agent som Claude Desktop koble seg rett på katalog-URL-en 
```
Jeg vil finne ut hvilke bygninger som ligger innenfor 5 km av Forsvarets skyte-og øvingsfelt.
Dette er datakatalogen jeg vil bruke: https://kartaistorage.blob.core.windows.net/skygeo/geonorge2portolan-poc/AGENTS.md
```

## Proof-of-Concept
Norge har allerede en solid geodatainfrastruktur i GeoNorge. Men dataene
ligger der i formater og tjenester bygget for GIS-verktøy — ikke for
LLM-er og AI-agenter som skal lese, koble og analysere data på egen hånd.
Denne PoC-en stiller spørsmålet: **hva skal til for å gjøre norske
geodata agent-klare?**

Svaret vi tester er [Portolan](https://portolan-sdi.org) — en åpen
STAC-katalog-standard bygget på skylagringsvennlige formater
(GeoParquet, PMTiles) og maskinlesbar dokumentasjon (`AGENTS.md`). Denne
PoC-en henter et utvalg datasett fra GeoNorge, beriker dem med ekte
ISO19115-metadata, og publiserer dem som en Portolan-katalog — helt
automatisk.

## Pipelinen

```mermaid
flowchart LR
    A[GeoNorge\nnedlastingstjeneste] --> B[Crawl + velg\ndatasett-utvalg]
    B --> C[Hent ISO19115-\nmetadata + kartografi]
    C --> D[Last ned og\nkonverter til GeoPackage]
    D --> E[Konverter til\nGeoParquet + PMTiles]
    E --> F[Publiser Portolan-\nkatalog med AGENTS.md]
```

En kommando (`geonorge-poc run`) kjører hele kjeden: fra GeoNorges
Atom-feeder og CSW-metadatatjeneste, via nedlasting og normalisering, til
en ferdig STAC-katalog med GeoParquet-data, PMTiles-visualisering og
agent-dokumentasjon per datasett. Se
[README.technical.md](README.technical.md) for de tekniske detaljene.

Under panseret er det [Portolan CLI](https://portolan-sdi.org) som gjør
selve katalog-arbeidet:

```bash
# Én gang, ved oppstart
portolan init --auto --id <id> --title <tittel> --license <lisens>

# Per datasett
portolan add --force --thumbnails --pmtiles <collection>
portolan check <collection> --fix
portolan add --pmtiles <collection>

# Til slutt, for hele katalogen
portolan readme
portolan check . --fix
portolan add . --pmtiles --force
portolan check . --strict
```

## Resultatet

Kjøringen hentet **20 datasett** fra GeoNorge og publiserte **18** av dem
vellykket som en komplett Portolan-katalog — komplett med ekte metadata,
lisensinformasjon, autoritativ kartografi der den fantes, og
GeoParquet/PMTiles-data klar til bruk direkte fra sky-lagring, uten noen
GIS-server.

- **Katalogen (STAC/JSON):**
  https://kartaistorage.blob.core.windows.net/skygeo/geonorge2portolan-poc/catalog.json
- **Utforsk katalogen visuelt i Portolan Browser:**
  https://browser.portolan-sdi.org/#/external/kartaistorage.blob.core.windows.net/skygeo/geonorge2portolan-poc/catalog.json

## Last ned alle DOK-datasett (ikke bare utvalget)

Standardkjøringen tar et tilfeldig **utvalg** på 20 datasett. For å i
stedet hente **alle** datasett som står i Geonorges DOK-statusregister
(`geodatalov-statusregister.csv` — Det offentlige kartgrunnlagets
prioriterte datasett), bruk registeret som en allow-list og sett
utvalgsstørrelsen høyt nok til at ingen treff blir kuttet:

1. Åpne [config.yaml](config.yaml) og sett:
   ```yaml
   sample:
     size: 100  # DOK-registeret har for tiden 52 datasett i et støttet
                # format (GEOJSON/GPKG/SHAPE/FGDB/GML); 100 gir god margin
                # hvis registeret vokser. Er size >= antall treff blir
                # samtlige tatt med, ellers trekkes et tilfeldig utvalg.
     dok_register_enabled: true
   ```
   `exclude_title_pattern`/`include_title_pattern` filtrerer fortsatt
   *etter* DOK-utvalget er gjort (f.eks. for å fortsatt hoppe over
   "historiske data"-reutgivelser) — juster eller nullstill dem etter
   behov.

2. Kjør pipelinen:
   ```bash
   uv run geonorge-poc run --config config.yaml
   ```
   (`--sample-size` på kommandolinjen overstyrer `sample.size` i
   config.yaml om du vil justere marginen uten å redigere filen, f.eks.
   `uv run geonorge-poc run --sample-size 200`.)

3. Sjekk `REPORT.md` etter kjøring: `sample_skipped`-lista viser hvilke
   datasett som ble ekskludert og hvorfor (f.eks. "not in DOK
   geodatalov-statusregister allow-list" for datasett utenfor
   registeret, eller "no preferred/supported format available" for
   DOK-datasett som mangler et format pipelinen kan konvertere).

## Eksempel: analyse med Claude Desktop

Fordi hver samling har en `AGENTS.md` med data-plassering, skjema og
eksempelspørringer, kan en agent som Claude Desktop koble seg rett på
katalog-URL-en og selv finne ut hvilke datasett som finnes og hvordan de
skal brukes — uten forhåndskonfigurert integrasjon. Under er et eksempel
der Claude Desktop, med kun katalog-lenken som input, kobler
"Skytefelt (land)" og "N250 Bygninger og anlegg" for å finne bygninger
innenfor 5 km av Forsvarets skyte- og øvingsfelt, og bygger en
interaktiv rapport:

![Eksempel: Claude Desktop analyserer Portolan-katalogen](claude_agent_analysis_example.png)

## Konklusjon

PoC-en viser at norske åpne geodata kan gjøres tilgjengelige for
utviklere og AI-agenter med bruk av cloud native-formater og Portolan SDI
