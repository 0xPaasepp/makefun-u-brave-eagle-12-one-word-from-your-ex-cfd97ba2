"""One Word From Your Ex -- make.fun entry.

Writes the one word an ex would use to describe the entrant to
/output/entry.txt: "placeholder".

Why this word: an ex would say it flatly -- "he was just a placeholder" --
and it stings because it is plainly true. It is not a generic insult, it is
a role: the seat-warmer kept around until the real one showed up. One word,
no explanation needed, and no near synonym lands the same way -- "temporary"
is a fact, "placeholder" is the punchline.

Pure standard library; deterministic; no network, no clock, no files read.
"""

import os

# The word the ex would use. One word, eleven characters, no padding.
WORD = "placeholder"
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """The sealed gate: UTF-8 text, 1-24 chars, exactly one word."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 24:
        raise ValueError(f"entry must be 1-24 characters, got {len(text)}")
    if len(text.split()) != 1:
        raise ValueError(f"entry must be exactly one word, got {len(text.split())}")
    if not text.isalpha():
        raise ValueError("entry must be a real word: letters only, no digits or punctuation")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
