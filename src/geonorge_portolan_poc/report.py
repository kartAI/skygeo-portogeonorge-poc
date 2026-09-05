"""Steg 8: skriv REPORT.md fra en PipelineReport."""

from __future__ import annotations

import collections
from pathlib import Path

from geonorge_portolan_poc.pipeline import PipelineReport


def render_report(report: PipelineReport) -> str:
    ok = [r for r in report.results if r.status == "ok"]
    failed = [r for r in report.results if r.status != "ok"]

    status_counts = collections.Counter(r.status for r in report.results)
    style_counts = collections.Counter(r.style_decision for r in report.results if r.style_decision)
    format_counts = collections.Counter(r.format for r in report.results)

    lines: list[str] = []
    lines.append("# REPORT: GeoNorge -> Portolan PoC\n")

    lines.append("## Sammendrag\n")
    lines.append(f"- Tjenestefeed: {report.total_entries} entries, {report.unique_datasets} unike datasett.")
    lines.append(
        f"- {len(report.sample_skipped)} datasett ekskludert fra kandidatpoolen (kun i "
        "SOSI/GML/PostGIS/andre formater portolan-cli ikke stotter, eller filtrert av tittel-mønster)."
    )
    lines.append(f"- Sample: {len(report.results)} datasett valgt.")
    lines.append(f"- **{len(ok)}/{len(report.results)} datasett fullfort vellykket** gjennom hele pipelinen.")
    lines.append(
        f"- `portolan check catalog` (standard, spec-konformitet) etter full kjoring: "
        f"**{'PASS' if report.final_check_ok else 'FAIL'}**."
    )
    lines.append(
        f"- `portolan check catalog --strict` (advarsler telles som feil): "
        f"**{'PASS' if report.final_check_strict_ok else 'FAIL'}** "
        "(se punkt 4 under \"Kjente begrensninger\" -- forventet a feile pa en ufarlig, "
        "dokumentert CLI-advarsel, ikke pa reelle spec-brudd)."
    )
    lines.append("")
    lines.append("### Status per steg")
    lines.append("")
    lines.append("| Status | Antall |")
    lines.append("|---|---|")
    for status, count in status_counts.most_common():
        lines.append(f"| {status} | {count} |")
    lines.append("")

    lines.append("### Format-fordeling i sample")
    lines.append("")
    lines.append("| Format | Antall |")
    lines.append("|---|---|")
    for fmt, count in format_counts.most_common():
        lines.append(f"| {fmt} | {count} |")
    lines.append("")

    lines.append("### Kartografi/styling (steg 5b)")
    lines.append("")
    lines.append("| Avgjorelse | Antall |")
    lines.append("|---|---|")
    for decision, count in style_counts.most_common():
        lines.append(f"| {decision} | {count} |")
    lines.append(
        "\n`authoritative-sld` betyr en SLD-fil ble funnet og lastet ned (fargeuttrekk til en "
        "MapLibre-override forsokt); `authoritative-pdf-only` betyr registeret bare hadde "
        "menneskelesbar PDF-dokumentasjon; `no-match-found` betyr fallback til portolans "
        "auto-genererte default-style.\n"
    )

    lines.append("## Datasett-for-datasett\n")
    lines.append("| Dataset ID | Collection | Format | Status | Lisens | Styling |")
    lines.append("|---|---|---|---|---|---|")
    for r in report.results:
        lines.append(
            f"| {r.dataset_id} | {r.collection_name} | {r.format} | {r.status} | "
            f"{r.license_spdx or '-'} | {r.style_decision or '-'} |"
        )
    lines.append("")

    if failed:
        lines.append("### Feilede/hoppet over datasett -- detaljer\n")
        for r in failed:
            lines.append(f"- **{r.dataset_id}** ({r.status}): {'; '.join(r.notes) or 'ingen detaljer'}")
        lines.append("")

    lines.append("## Kjente begrensninger oppdaget under implementasjon\n")
    lines.append(
        "Disse avvikene fra plan-dokumentets antakelser ble oppdaget empirisk under "
        "implementasjonen (se ogsa geonorge-portolan-poc-plan.md avsnitt 4):\n"
    )
    lines.append(
        "1. **portolan-cli 0.8.0 stotter ikke GML, SOSI eller PostGIS-dump** "
        "(`portolan_cli/extension_registry.py` har ingen GML-oppforing i det hele tatt). "
        "Plan-dokumentets forslag om a prioritere GML matte derfor forkastes; sample "
        "trekkes i stedet kun fra GEOJSON/GPKG/SHAPE/FGDB -- de formatene GDAL/OGR og "
        "portolan begge kan lese."
    )
    lines.append(
        "2. **FileGDB (.gdb) har et hull i portolan-cli sin cloud-native-konvertering**: "
        "`.gdb` mangler `scan_category=\"geo_asset\"` i extension-registeret, sa "
        "`portolan check --fix` sin geo-asset-skanning hopper over FileGDB-filer helt -- "
        "ingen GeoParquet-konvertering, ingen thumbnail. GeoJSON/GPKG/SHP rammes ikke. "
        "Losning: alle nedlastede rådata normaliseres til GeoPackage med `ogr2ogr` for "
        "`portolan add` noensinne ser dem (se `convert_gpkg.py`)."
    )
    lines.append(
        "3. **GeoNorges GeoJSON-eksport har en UTF-8 BOM** som knekker portolan sin "
        "JSON-parser (`Unexpected UTF-8 BOM`). Samme ogr2ogr-normalisering i punkt 2 "
        "loser ogsa dette, siden GDAL leser BOM-en uten problemer."
    )
    lines.append(
        "4. **`portolan add` beregner GeoParquet-avledet STAC-metadata (feature_count, "
        "geometry_type) uten a registrere selve GeoParquet-filen som asset.** "
        "`check --fix` konverterer sa kildefilen til GeoParquet pa nytt som en "
        "\"orphan\" (usporet fil), og en andre `portolan add`-kjoring kreves for a "
        "registrere den resulterende thumbnail-en (parquet-filen forblir usporet, men "
        "det blokkerer ikke `--strict`). Pipelinen kjorer derfor `add -> check --fix -> "
        "add` per collection i stedet for planens ett-linjers `add`+`check --fix`."
    )
    lines.append(
        "5. **Kollisjon mellom katalogstruktur og collection-ID:** a legge rådata i "
        "`catalog/<id>/raw/<fil>` (som plan-dokumentets katalogstruktur foreslo) far "
        "portolan til a opprette EN subkatalog (`<id>`) og collection-en `<id>/raw` "
        "nestet under den, i stedet for a la `<id>` selv vaere collection-en. Rådata "
        "legges derfor direkte i `catalog/<id>/` uten `raw/`-mellomledd."
    )
    lines.append(
        "6. **Kartografi/tegneregel-registeret er nesten utelukkende PDF-dokumentasjon "
        "for mennesker**, som forventet i planen. Fuzzy-matching pa tittel med "
        "terskel 80 ga dessuten falske positiver pa korte/generiske titler (f.eks. "
        "\"Kirkebygg\" matchet en korallrev-oppforing med score 86); terskelen ble "
        "hevet til 90 i `config.yaml`."
    )
    lines.append("")

    lines.append("## Verifisering (steg 8)\n")
    lines.append("`portolan check catalog` (standard):\n")
    lines.append("```")
    lines.append(report.final_check_output.strip() or "(no output)")
    lines.append("```\n")
    lines.append("`portolan check catalog --strict`:\n")
    lines.append("```")
    lines.append(report.final_check_strict_output.strip() or "(no output)")
    lines.append("```\n")

    lines.append("## Konfigurasjon brukt\n")
    lines.append("Se `config.yaml` i prosjektroten for fullstendig konfigurasjon.\n")

    return "\n".join(lines)


def write_report(report: PipelineReport, path: Path) -> None:
    path.write_text(render_report(report), encoding="utf-8")
