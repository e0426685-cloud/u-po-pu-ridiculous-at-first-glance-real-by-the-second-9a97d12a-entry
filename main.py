"""Ridiculous at First Glance, Real by the Second.

One-sentence bizarre startup pitch (167 characters, at most 200).
Standard library only. Writes the pitch to /output/entry.txt.
"""

import os

ENTRY = (
    "We rent out stern grandmothers who scold startup founders into "
    "shipping on time, because founders pay $200 an hour for the one "
    "accountability no coach can fake: guilt."
)

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    # Gate: exactly one sentence, 1-200 characters, before writing.
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
