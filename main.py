#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes a single line (one autocorrect fail, under 200 characters) to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``.

Standard library only. No network, no randomness, no clock, no environment
reads besides MAKEFUN_OUTPUT_DIR — two runs produce byte-identical output.

The line: a text to a friend/family member, apologising for being late to a
funeral, where autocorrect turned "traffic" into "threesome". The slip is
clear (traffic -> threesome), surprising, specific, and reads as a real
mistyped message rather than a written joke.
"""

import os
import sys

# The entry: one line, no trailing newline, no leading/trailing spaces.
ENTRY = "Sorry I'm late to the funeral, I got stuck in a threesome on the highway."

# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 199
# characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 199


def output_dir() -> str:
    """Resolve the output directory (grader sets MAKEFUN_OUTPUT_DIR)."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return value if value else "/output"


def validate(text: str) -> None:
    """Fail loudly instead of shipping an entry the gate would reject."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "entry is %d chars, gate requires %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    # Self-check: re-read what landed on disk and refuse to report success
    # unless it is byte-identical to the validated entry.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("written entry.txt does not match ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
