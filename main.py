#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes exactly one line (<=200 chars, UTF-8) reviewing the most boring
everyday object: the doorstop. Deterministic, exit 0.
"""
import os
import sys

LINE = "The doorstop spends its whole life being kicked by the very people it holds the door open for, and it has never once asked for a raise."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(LINE)
sys.exit(0)
