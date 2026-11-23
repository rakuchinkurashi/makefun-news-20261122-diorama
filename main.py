#!/usr/bin/env python3
"""Copy the entry image to /output/entry.png.

Deterministic: no network, no randomness, no timestamps.
Running this program twice writes byte-identical output.
"""
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "news.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
