#!/usr/bin/env python3
# Entry for make.fun bounty u-azazex-one-line-one-chill-6d4d5488
"""One Line, One Chill.

Deterministic entry: writes exactly one chilling sentence to
/output/entry.txt and prints that same line, nothing else.
"""

import os

# The chill: a baby monitor repeats the narrator's own voice from inside
# the nursery — the fright lands in one breath, with no setup and no
# second line to soften it.
LINE = "The baby monitor crackled, and in my own voice it whispered not to open the nursery door because it was already inside with her."


def get_line():
    """Return the entry's single chilling sentence."""
    return LINE


def main():
    line = get_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
