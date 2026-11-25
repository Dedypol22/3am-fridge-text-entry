"""One-line entry for make.fun: "The 3AM Fridge Text".

Joke logic: the gag is a role reversal. At 3am the fridge stops being
a passive appliance and stages a wellness intervention on its owner --
the machine that stores the snacks is now the one telling the human to
go back to bed. The sting is in "even I": a fridge, an object with no
health expertise and no business having opinions, considers itself more
sensible than the person raiding it. That is the whole voice of the
line -- a small machine that has decided 3am is the moment to speak,
with total confidence and zero shame. One sentence of setup, one
sentence of verdict, nothing left to explain.
"""

import os

LINE = "3AM: this is an intervention. I'm a fridge and even I think you need to go back to bed."
# Verified character count of LINE: 87 (within the 1-140 gate).
# Resubmit v2 (25 Nov 2026): replaces the round-1 line; judged in round 3 (final).


def output_dir():
    """Return the directory entry.txt must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the one-line entry and verify it round-trips exactly."""
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == LINE + "\n", "entry.txt does not match LINE"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
