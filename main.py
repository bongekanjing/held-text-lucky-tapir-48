#!/usr/bin/env python3
"""Write one short text whose job is to leave its reader quieter than it found them.

Nothing here talks to a network or a clock. Run it twice and the file it
writes is byte-identical both times.

    python3 -P -s main.py
"""

import os

# The text is kept as a tuple of lines rather than one blob so the line breaks
# survive to the file instead of being flattened by the join below.
TEXT = (
    "You are face down on the rug.",
    "The dog folds over your back.",
    "Three turns, then her weight.",
    "Her breathing counts slowly.",
    "Yours falls in behind it.",
    "The joists were trees, and held.",
    "They hold you now.",
    "Outside, the lane stays empty.",
    "Her chin comes down.",
    "Nothing here",
    "is yours to hold.",
)

LIMIT = 280


def destination():
    """Where the grader wants the text: $MAKEFUN_OUTPUT_DIR, else here."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    return os.path.join(folder, "entry.txt")


def compose():
    body = "\n".join(TEXT)
    size = len(body)
    if not body.strip():
        raise ValueError("the text is empty")
    if size > LIMIT:
        raise ValueError(f"the text is {size} characters, over the {LIMIT} allowed")
    return body


def run():
    body = compose()
    path = destination()
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(body)
    print(f"wrote {len(body)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
