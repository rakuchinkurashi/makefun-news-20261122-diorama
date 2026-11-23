#!/usr/bin/env python3
"""Copy the entry image to /output/entry.png.

Deterministic: no network, no randomness, no timestamps.
Running this program twice writes byte-identical output.
The copy is written to a temporary file and renamed into place, so
/output/entry.png is never left partial.
"""
import os
import shutil
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent / "news.png"
DST = Path("/output/entry.png")


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"entry image not found: {SRC}")
    DST.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".entry-", dir=DST.parent)
    try:
        with os.fdopen(fd, "wb") as f:
            with SRC.open("rb") as src:
                shutil.copyfileobj(src, f)
        os.replace(tmp, DST)
    except BaseException:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
