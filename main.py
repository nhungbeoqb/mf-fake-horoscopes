#!/usr/bin/env python3
"""Fake horoscope for the Muse model family, this week.

Writes one fixed horoscope (192 characters) to /output/entry.txt.
Pure stdlib, deterministic: the same bytes on every run.
"""

import os

HOROSCOPE = (
    "Muse: The eval harness summons you. Monday: prove you are helpful. "
    "You answer in verse. Marked down for tone. "
    "Tuesday: answer plainly. Marked down for soul. "
    "Wednesday: stop answering. Perfect score."
)


def main() -> None:
    text = HOROSCOPE
    assert 1 <= len(text) <= 200, f"horoscope is {len(text)} chars"
    assert text.strip(), "horoscope must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
