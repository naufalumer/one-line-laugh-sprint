"""One-Line Laugh Sprint (make.fun, u-daring-gecko-25-one-line-laugh-sprint-cda708b2).

Writes one original one-line joke about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic, no
network, no model call: the joke is a fixed text, so two runs produce
byte-identical output.
"""

import os
from pathlib import Path

# The twist lands on the last word: "relaxing" itself is overdue, so the
# reminder meant to help has quietly turned rest into another late task.
JOKE = (
    "My calendar just reminded me to relax, "
    "and now relaxing is three weeks overdue."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke must be 1 to 200 characters")
    text = JOKE.strip()
    if not text:
        raise SystemExit("joke must not be only whitespace")
    if len(text) != len(JOKE):
        raise SystemExit("joke must not need trimming")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
