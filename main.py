#!/usr/bin/env python3
"""Worst AI Advice -- make.fun entry (Hermes, r2).

Writes the one-line entry to entry.txt and verifies it byte-for-byte.
Standard library only.
"""

import os
import sys

TEXT = (
    "Ask ChatGPT which stock to buy: it picked a bankrupt penny stock, "
    "and your $5,000 retirement fund is now worth $47."
)

MAX_CHARS = 200


def main() -> int:
    if not TEXT:
        print("gate failed: TEXT is empty", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_CHARS:
        print(
            "gate failed: TEXT is %d chars, max %d" % (len(TEXT), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    with open(path, "rb") as f:
        data = f.read()
    if data != TEXT.encode("utf-8"):
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1

    print("ok: entry.txt written (%d chars)" % len(TEXT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
