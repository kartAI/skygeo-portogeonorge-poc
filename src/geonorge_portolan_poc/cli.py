"""CLI entrypoint: `geonorge-poc run [--config config.yaml] [--sample-size N]`."""

from __future__ import annotations

import logging
from pathlib import Path

import click

from geonorge_portolan_poc.config import load_config
from geonorge_portolan_poc.pipeline import run_pipeline
from geonorge_portolan_poc.report import write_report


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Debug-level logging.")
def main(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    )
    # requests/urllib3 are noisy at DEBUG; keep them at INFO regardless.
    logging.getLogger("urllib3").setLevel(logging.INFO)


@main.command()
@click.option("--config", "config_path", default="config.yaml", type=click.Path(path_type=Path))
@click.option("--sample-size", "sample_size", type=int, default=None, help="Override sample.size from config.")
@click.option("--refresh-feed", is_flag=True, help="Ignore the cached tjenestefeed.xml and re-download it.")
@click.option("--report", "report_path", default="REPORT.md", type=click.Path(path_type=Path))
def run(config_path: Path, sample_size: int | None, refresh_feed: bool, report_path: Path) -> None:
    """Run the full GeoNorge -> Portolan pipeline (steg 1-8)."""
    config = load_config(config_path)
    if sample_size is not None:
        config.sample.size = sample_size

    report = run_pipeline(config, force_refresh_feed=refresh_feed)
    write_report(report, report_path)

    ok = sum(1 for r in report.results if r.status == "ok")
    click.echo(f"\nDone: {ok}/{len(report.results)} datasets succeeded. Report written to {report_path}.")
    click.echo(f"portolan check catalog: {'PASS' if report.final_check_ok else 'FAIL'}")
    click.echo(f"portolan check catalog --strict: {'PASS' if report.final_check_strict_ok else 'FAIL'}")
    if not report.final_check_ok:
        click.echo("WARNING: catalog does not conform even without --strict -- see REPORT.md / logs.")


if __name__ == "__main__":
    main()
