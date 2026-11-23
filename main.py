#!/usr/bin/env python3
"""Write the plan text to entry.txt and report its character count."""

import os
from pathlib import Path

from text import ENTRY


def main() -> None:
    plan = ENTRY.strip()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(plan, encoding="utf-8")
    print(len(plan))


if __name__ == "__main__":
    main()
