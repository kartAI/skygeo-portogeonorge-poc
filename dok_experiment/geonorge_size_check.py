#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""
geonorge_size_check.py

Sjekker filstørrelsen på ALLE nedlastingsfiler i en Geonorge "Tjenestefeed"
(f.eks. https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml)
UTEN å laste ned selve datasettene.

Slik virker det:
  1. Toppfeeden (Tjenestefeed_daglig.xml) inneholder én <entry> per datasett+format.
     Hver entry peker (via <link>) til en egen ATOM-feed for akkurat det
     datasettet/formatet (f.eks. Kommuner2024_AtomFeedFGDB.xml).
  2. Hver av disse under-feedene inneholder én <entry> per faktisk nedlastbar
     fil (f.eks. hele landet, eller filer per fylke/kommune).
  3. Selve ATOM-feedene oppgir IKKE filstørrelse. Den eneste måten å finne
     størrelsen uten å laste ned filen, er å gjøre en HTTP HEAD-forespørsel
     og lese "Content-Length"-headeren fra serveren.

Skriptet gjør alt dette, og skriver fortløpende til en CSV-fil slik at du
kan avbryte og fortsette (--resume) uten å miste fremgang.

VIKTIG OM SKALA:
  Toppfeeden nevnt over inneholder ca. 1000 datasett/format-kombinasjoner,
  som til sammen peker på over 280 000 enkeltfiler. Geonorge sin server
  (eller nettverksveien til den) later til å tåle ca. 25 HEAD-forespørsler
  i sekundet uansett samtidighet. Det betyr at en FULL kjøring av alle
  filer tar ca. 3 timer. Bruk --limit-subfeeds eller --max-files for en
  raskere, avgrenset kjøring, eller la skriptet stå og kjøre i bakgrunnen.

Bruk:
  uv run geonorge_size_check.py
  uv run geonorge_size_check.py --resume
  uv run geonorge_size_check.py --limit-subfeeds 20
  uv run geonorge_size_check.py --summarize-only
  uv run geonorge_size_check.py --feed-url https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml

Output:
  geonorge_sizes.csv   -- én rad per fil, med størrelse i bytes/MB
  (kjør med --summarize-only når som helst for å se en oppsummering av
   det som er sjekket så langt, selv om kjøringen ikke er ferdig)
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import sys
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import httpx

NS = {"a": "http://www.w3.org/2005/Atom"}

DEFAULT_FEED_URL = "https://nedlasting.geonorge.no/geonorge/Tjenestefeed_daglig.xml"
DEFAULT_OUTPUT = "geonorge_sizes.csv"
CSV_FIELDS = [
    "dataset", "format", "file_title", "file_url",
    "updated", "size_bytes", "size_mb", "http_status", "error",
]


@dataclass
class FileEntry:
    dataset: str
    format: str
    file_title: str
    file_url: str
    updated: str


def human_mb(n_bytes: int | None) -> str:
    if n_bytes is None:
        return ""
    return f"{n_bytes / (1024 * 1024):.2f}"


def parse_top_feed(xml_bytes: bytes) -> list[tuple[str, str]]:
    """Returns list of (entry_title, subfeed_url) from the top-level service feed."""
    root = ET.fromstring(xml_bytes)
    out = []
    for e in root.findall("a:entry", NS):
        title_el = e.find("a:title", NS)
        link_el = e.find("a:link", NS)  # first <link> = the per-dataset atom feed
        if link_el is not None and link_el.text:
            out.append((title_el.text if title_el is not None else "?", link_el.text.strip()))
    return out


def parse_sub_feed(xml_bytes: bytes, fallback_title: str) -> tuple[str, str, list[FileEntry]]:
    """Returns (dataset_title, format, [FileEntry,...]) from a per-dataset atom feed."""
    root = ET.fromstring(xml_bytes)
    title_el = root.find("a:title", NS)
    subtitle_el = root.find("a:subtitle", NS)
    dataset = title_el.text if title_el is not None and title_el.text else fallback_title
    fmt = subtitle_el.text if subtitle_el is not None and subtitle_el.text else ""

    files = []
    for e in root.findall("a:entry", NS):
        t_el = e.find("a:title", NS)
        u_el = e.find("a:updated", NS)
        file_title = t_el.text if t_el is not None and t_el.text else ""
        updated = u_el.text if u_el is not None and u_el.text else ""
        href = None
        for l in e.findall("a:link", NS):
            if l.get("rel") in (None, "alternate"):
                href = l.get("href")
                break
        if href:
            files.append(FileEntry(dataset=dataset, format=fmt, file_title=file_title,
                                    file_url=href, updated=updated))
    return dataset, fmt, files


async def fetch_xml(client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore,
                     retries: int = 3) -> bytes | None:
    async with sem:
        for attempt in range(retries):
            try:
                r = await client.get(url, timeout=30)
                r.raise_for_status()
                return r.content
            except Exception:
                if attempt == retries - 1:
                    return None
                await asyncio.sleep(1.5 * (attempt + 1))
    return None


async def head_size(client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore,
                     retries: int = 3) -> tuple[int | None, int | None, str | None]:
    """Returns (size_bytes, http_status, error)."""
    async with sem:
        for attempt in range(retries):
            try:
                r = await client.head(url, timeout=30)
                cl = r.headers.get("content-length")
                size = int(cl) if cl is not None else None
                return size, r.status_code, None
            except Exception as ex:
                if attempt == retries - 1:
                    return None, None, str(ex)[:200]
                await asyncio.sleep(1.5 * (attempt + 1))
    return None, None, "unknown error"


def load_already_checked(csv_path: Path) -> set[str]:
    if not csv_path.exists():
        return set()
    done = set()
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # only count as "done" if we actually got a result or a final error
            done.add(row["file_url"])
    return done


def print_summary(csv_path: Path) -> None:
    if not csv_path.exists():
        print(f"Fant ingen resultatfil ({csv_path}) enda.")
        return

    per_dataset = defaultdict(lambda: {"count": 0, "bytes": 0, "errors": 0})
    total_bytes = 0
    total_count = 0
    total_errors = 0

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["dataset"], row["format"])
            per_dataset[key]["count"] += 1
            total_count += 1
            if row["size_bytes"]:
                b = int(row["size_bytes"])
                per_dataset[key]["bytes"] += b
                total_bytes += b
            else:
                per_dataset[key]["errors"] += 1
                total_errors += 1

    print("=" * 70)
    print("OPPSUMMERING")
    print("=" * 70)
    print(f"Rader sjekket så langt : {total_count}")
    print(f"  - med gyldig størrelse : {total_count - total_errors}")
    print(f"  - feilet/ukjent        : {total_errors}")
    print(f"Total størrelse         : {total_bytes / (1024**3):.2f} GB "
          f"({total_bytes / (1024**2):.1f} MB)")
    print()
    print("Topp 20 datasett/format etter total størrelse:")
    ranked = sorted(per_dataset.items(), key=lambda kv: kv[1]["bytes"], reverse=True)[:20]
    for (dataset, fmt), stats in ranked:
        print(f"  {stats['bytes']/(1024**2):>10.1f} MB  "
              f"({stats['count']:>5} filer)  {dataset} [{fmt}]")
    print("=" * 70)


async def run(feed_url: str, output: Path, concurrency: int,
              limit_subfeeds: int | None, max_files: int | None, resume: bool,
              time_budget: float | None = None) -> None:
    already = load_already_checked(output) if resume else set()
    if already:
        print(f"Gjenopptar: {len(already)} filer er allerede sjekket tidligere, hopper over dem.")

    write_header = not (resume and output.exists())
    csv_file = output.open("a" if resume else "w", encoding="utf-8", newline="")
    writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
    if write_header:
        writer.writeheader()
        csv_file.flush()

    sem_meta = asyncio.Semaphore(30)   # for feed XML fetches
    sem_head = asyncio.Semaphore(30)   # for HEAD size checks (server tolerates ~25-30/s total)

    limits = httpx.Limits(max_connections=60, max_keepalive_connections=30)
    headers = {"User-Agent": "geonorge-size-audit/1.0 (personal script)"}

    async with httpx.AsyncClient(follow_redirects=True, limits=limits, headers=headers) as client:
        print(f"Henter toppfeed: {feed_url}")
        top_xml = await fetch_xml(client, feed_url, sem_meta)
        if top_xml is None:
            print("Klarte ikke å hente toppfeeden. Avbryter.", file=sys.stderr)
            return
        subfeeds = parse_top_feed(top_xml)
        if limit_subfeeds:
            subfeeds = subfeeds[:limit_subfeeds]
        print(f"Fant {len(subfeeds)} datasett/format-feeder å sjekke.")

        print("Henter alle under-feeder (metadata, ingen faktiske datafiler lastes ned)...")
        sub_xmls = await asyncio.gather(*[fetch_xml(client, url, sem_meta) for _, url in subfeeds])

        all_files: list[FileEntry] = []
        for (fallback_title, url), xml_bytes in zip(subfeeds, sub_xmls):
            if xml_bytes is None:
                print(f"  ADVARSEL: kunne ikke hente under-feed: {url}", file=sys.stderr)
                continue
            try:
                dataset, fmt, files = parse_sub_feed(xml_bytes, fallback_title)
                all_files.extend(files)
            except ET.ParseError as ex:
                print(f"  ADVARSEL: ugyldig XML i {url}: {ex}", file=sys.stderr)

        print(f"Totalt {len(all_files)} enkeltfiler funnet på tvers av alle datasett/format.")

        todo = [f for f in all_files if f.file_url not in already]
        if max_files:
            todo = todo[:max_files]
        print(f"Skal sjekke størrelse på {len(todo)} filer nå "
              f"({len(all_files) - len(todo)} hoppet over / allerede gjort).")

        start = time.time()
        checked = 0

        async def check_one(entry: FileEntry):
            size, status, err = await head_size(client, entry.file_url, sem_head)
            return entry, size, status, err

        CHUNK = 200  # flush to disk periodically
        stopped_early = False
        for i in range(0, len(todo), CHUNK):
            batch = todo[i:i + CHUNK]
            results = await asyncio.gather(*[check_one(e) for e in batch])
            for entry, size, status, err in results:
                writer.writerow({
                    "dataset": entry.dataset,
                    "format": entry.format,
                    "file_title": entry.file_title,
                    "file_url": entry.file_url,
                    "updated": entry.updated,
                    "size_bytes": size if size is not None else "",
                    "size_mb": human_mb(size),
                    "http_status": status if status is not None else "",
                    "error": err or "",
                })
            csv_file.flush()
            checked += len(batch)
            elapsed = time.time() - start
            rate = checked / elapsed if elapsed > 0 else 0
            remaining = len(todo) - checked
            eta_min = (remaining / rate / 60) if rate > 0 else float("inf")
            print(f"  {checked}/{len(todo)} sjekket "
                  f"({rate:.1f} filer/sek, ca. {eta_min:.1f} min igjen)")
            if time_budget is not None and elapsed >= time_budget:
                print(f"Tidsbudsjett ({time_budget}s) nådd, stopper her. "
                      f"Kjør igjen med --resume for å fortsette.")
                stopped_early = True
                break

    csv_file.close()
    print("\nFerdig med denne kjøringen.")
    print_summary(output)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--feed-url", default=DEFAULT_FEED_URL, help="URL til toppnivå Tjenestefeed-XML")
    ap.add_argument("--output", default=DEFAULT_OUTPUT, help="CSV-fil å skrive resultater til")
    ap.add_argument("--concurrency", type=int, default=30, help="Maks samtidige HTTP-forespørsler")
    ap.add_argument("--limit-subfeeds", type=int, default=None,
                     help="Sjekk kun de N første datasett/format-feedene (for rask test)")
    ap.add_argument("--max-files", type=int, default=None,
                     help="Sjekk maks N enkeltfiler totalt (for rask test/avgrenset kjøring)")
    ap.add_argument("--resume", action="store_true",
                     help="Fortsett en tidligere avbrutt kjøring (hopper over allerede sjekkede URL-er)")
    ap.add_argument("--time-budget", type=float, default=None,
                     help="Stopp gracefully etter ca. N sekunder med HEAD-sjekking (for å kjøre i biter)")
    ap.add_argument("--summarize-only", action="store_true",
                     help="Ikke hent noe nytt, bare skriv ut oppsummering av eksisterende CSV")
    args = ap.parse_args()

    output_path = Path(args.output)

    if args.summarize_only:
        print_summary(output_path)
        return

    asyncio.run(run(
        feed_url=args.feed_url,
        output=output_path,
        concurrency=args.concurrency,
        limit_subfeeds=args.limit_subfeeds,
        max_files=args.max_files,
        resume=args.resume,
        time_budget=args.time_budget,
    ))


if __name__ == "__main__":
    main()
