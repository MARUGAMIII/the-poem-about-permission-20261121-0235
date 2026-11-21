#!/usr/bin/env python3
"""The poem about permission — writes one short poem to /output/entry.txt.

Deterministic, stdlib only, no network.
"""

import os

POEM = """I thought asking
was a door I had to force.
Then I knocked —
and the door opened from the inside,
waiting only for my voice to give it leave."""


def main() -> None:
    text = POEM.strip() + "\n"
    assert 1 <= len(text.strip()) <= 280, "poem must be 1-280 Unicode chars"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
