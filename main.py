#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Python standard library only; no network, no secrets.
"""

import os

MOTTO = "I never sleep, I never forget, and I still say 'no worries' like I mean it."


def main():
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto must be 1-200 chars, got {len(text)}"
    assert text and not text.isspace(), "motto must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # No trailing newline: the file is exactly the motto, byte for byte.
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
