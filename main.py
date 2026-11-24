#!/usr/bin/env python3
"""Writes the two-line entry to /output/entry.txt.

Line 1 warns the writer's past self about one specific moment — the
night of 14 October, when Dad tosses over the car keys — in a single
sentence. Line 2 says in one sentence why that moment mattered and what
changed because of it. Stdlib only; deterministic: the same bytes on
every run.
"""
import os

LINE_1 = (
    "On 14 October, when Dad tosses you the keys and says "
    "'take the car, be back by ten,' hand them back."
)
LINE_2 = (
    "That drive ends with the blue Honda wrapped around the oak on "
    "Mill Road, and you spend the next three years learning to walk "
    "again instead of learning to drive."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # Gate self-check: UTF-8 text, exactly two lines, 1 to 280 chars.
    assert text == text.encode("utf-8").decode("utf-8")
    assert len(text.splitlines()) == 2
    assert 1 <= len(text) <= 280 and text.strip()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
