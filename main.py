"""Entry for make.fun competition u-deysumbrella-the-3am-fridge-text-4c3e721d.

"The 3AM Fridge Text": a single line a smart fridge texts its owner at 3AM.
The winning line follows the proven pattern: a machine voice that has been
awake all night, one concrete detail (the cake hidden behind the vegetables),
and the punchline at the end. The fridge reports, like a night-shift witness,
that the cake has filed a missing persons report, then lands the cold
two-beat punchline: the cake misses its owner, the fridge does not.
"""

import os

LINE = "3AM update: the cake you hid behind the vegetables has filed a missing persons report. It misses you. I don't."

# Verified length: 110 characters (gate: 1-140)


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE + "\n", "entry.txt content mismatch"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
