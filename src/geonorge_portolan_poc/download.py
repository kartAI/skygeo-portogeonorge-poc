"""Steg 5: last ned datasettfiler til catalog/<dataset_id>/raw/, pakk ut zip."""

from __future__ import annotations

import logging
import zipfile
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

_CHUNK_SIZE = 1024 * 1024  # 1 MiB


def download_file(url: str, dest_dir: Path, *, session: requests.Session | None = None) -> Path | None:
    """Stream-download `url` into `dest_dir`, unzip if it's a zip. Never raises."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    filename = url.rstrip("/").rsplit("/", 1)[-1] or "download.bin"
    dest_path = dest_dir / filename

    sess = session or requests.Session()
    try:
        with sess.get(url, stream=True, timeout=300) as resp:
            resp.raise_for_status()
            with open(dest_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=_CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
    except requests.RequestException:
        logger.exception("Download failed for %s", url)
        return None

    if dest_path.suffix.lower() == ".zip":
        try:
            with zipfile.ZipFile(dest_path) as zf:
                zf.extractall(dest_dir)
            dest_path.unlink()
        except zipfile.BadZipFile:
            logger.exception("Downloaded file is not a valid zip: %s", dest_path)
            return None

    return dest_dir
