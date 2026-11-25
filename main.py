#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun bounty entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "A showerhead that only turns hot after you solemnly promise it, "
    "out loud, that this shower will be under five minutes — and turns "
    "ice-cold the instant you start singing."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 220, f"entry must be 1-220 chars, got {len(text)}"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"Wrote /output/entry.txt ({len(text)} characters)")
    print(text)


if __name__ == "__main__":
    main()
