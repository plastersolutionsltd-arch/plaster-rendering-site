#!/usr/bin/env python3
"""Single source of truth for the Google review count.

The count is written into every page's schema and visible copy, so it has to be
updated in one place or it drifts (it did: 4 pages sat on 104 while 57 said 105,
and /projects displayed 95).

Usage:
    python3 sync-reviews.py 107          # set the count everywhere
    python3 sync-reviews.py 107 --check  # report drift, change nothing

Get the real number from the Google Business Profile panel ("107 Google reviews").
Run this, then commit. Visible "100+" copy is deliberately left alone — it never
goes stale and does not need touching.
"""
import glob
import re
import sys

RATING = "5.0"


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if not args or not args[0].isdigit():
        print(__doc__)
        return 1
    count = args[0]

    schema_pat = re.compile(r'("reviewCount":\s*")(\d+)(")')
    # the one page that prints the number in visible copy rather than "100+"
    visible_pat = re.compile(r"(\b)(\d{2,3})( Google reviews\b)")
    # the stat tile on /projects
    # Anchored on the "5* Reviews" label that follows it, so the neighbouring
    # "5 / Services" tile with identical markup is left alone.
    stat_pat = re.compile(
        r'(<div class="font-display font-black text-white leading-none mb-1" style="font-size:2rem">)'
        r"(\d+)"
        r"(</div>\s*<div[^>]*>5(?:&#9733;|★) Reviews)"
    )

    changed, drift = [], {}
    for path in sorted(glob.glob("*.html")):
        src = open(path, encoding="utf-8").read()
        out = src

        for m in schema_pat.finditer(src):
            if m.group(2) != count:
                drift.setdefault(path, set()).add(f"schema {m.group(2)}")
        out = schema_pat.sub(lambda m: m.group(1) + count + m.group(3), out)

        for m in visible_pat.finditer(src):
            if m.group(2) != count:
                drift.setdefault(path, set()).add(f"visible {m.group(2)}")
        out = visible_pat.sub(lambda m: m.group(1) + count + m.group(3), out)

        for m in stat_pat.finditer(src):
            if m.group(2) != count:
                drift.setdefault(path, set()).add(f"stat tile {m.group(2)}")
        out = stat_pat.sub(lambda m: m.group(1) + count + m.group(3), out)

        if out != src:
            changed.append(path)
            if not check:
                open(path, "w", encoding="utf-8").write(out)

    if check:
        if drift:
            print(f"DRIFT from {count}:")
            for p, what in sorted(drift.items()):
                print(f"  {p}: {', '.join(sorted(what))}")
        else:
            print(f"All pages agree on {count} / {RATING}.")
        return 1 if drift else 0

    print(f"Set review count to {count} across {len(changed)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
