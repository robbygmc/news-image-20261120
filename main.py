#!/usr/bin/env python3
"""news-image-20261120 entry: THE WORLD TODAY, Friday 20 November 2026.

Python 3.13, standard library only. The finished front page ships in
this repository as entry.png; the program copies it to the output
directory (``$MAKEFUN_OUTPUT_DIR`` or ``/output``). The copy is
byte-for-byte identical on every run, so the two grading runs agree.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # A failed copy must fail loudly, never ship an empty file.
    assert target.is_file() and target.stat().st_size > 0, "no entry.png written"
    # The gate refuses anything over 1 MiB or not a PNG: check both here.
    data = target.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert len(data) <= 1_048_576, "entry.png is over 1 MiB"
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == \
        hashlib.sha256(data).hexdigest(), "entry.png mismatch"


if __name__ == "__main__":
    main()
