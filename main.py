"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables, plain text) to
/output/entry.txt. Deterministic: the haiku is a fixed literal, so every
run writes identical bytes. Standard library only, no network, no
randomness, no environment reads.
"""

import os

HAIKU = """A log line at three
says the payment went through twice
the log was lying
"""


def main() -> None:
    # Guard the gate before writing: exactly 3 lines, 5-7-5 syllables by
    # construction, and 1-200 characters of UTF-8 text.
    lines = HAIKU.rstrip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert 1 <= len(HAIKU) <= 200, f"expected 1-200 chars, got {len(HAIKU)}"
    assert HAIKU.strip(), "haiku must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
