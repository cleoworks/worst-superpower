# Worst Superpower — entry v1
#
# One single-line superpower, at most 140 characters, inventing the most
# useless superpower imaginable. The program writes that line to
# /output/entry.txt (UTF-8, one line, no trailing newline).
#
# Line (78 characters, 78 bytes, plain ASCII):
#   I can silence any notification instantly, but only the ones I've already read.

LINE = (
    "I can silence any notification instantly, "
    "but only the ones I've already read."
)

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, a single line, not only white space. Fail loudly here
# instead of writing an entry the gate would refuse.
assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be one line"
assert LINE.strip(), "line must not be only white space"

import os


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back: what the gate reads must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
