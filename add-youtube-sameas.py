#!/usr/bin/env python3
"""Add the P&R YouTube channel to every BUSINESS sameAs block on the site.

Why this is not a find-and-replace
----------------------------------
There are six different sameAs formats across the site (43 pages one way,
18 another, then four one-offs), some pretty-printed across lines and some
minified onto a single line. A naive replace hits one format and silently
misses the rest -- the exact failure recorded in HANDOVER.md for the
28 Jul reviewCount sweep.

It is also not safe to touch every sameAs. index.html carries
    {"@type": "City", "name": "Sheffield", "sameAs": "https://en.wikipedia.org/wiki/Sheffield"}
which is a STRING on the City entity, not the business. Adding a YouTube
channel to the city of Sheffield would be nonsense.

So a block is only edited when it is an ARRAY that already contains the
business's own Facebook URL. That is what identifies it as the business's
social block rather than some other entity's.

Usage:
    python3 add-youtube-sameas.py --check    # report only, writes nothing
    python3 add-youtube-sameas.py            # apply
"""
import glob
import json
import re
import sys

CHANNEL = "https://www.youtube.com/@PandRSheffield"
MARKER = "facebook.com/plasterandrenderingsolutions"
SAMEAS = re.compile(r'"sameAs"\s*:\s*\[(.*?)\]', re.S)

check = "--check" in sys.argv


def add_entry(inner: str) -> str:
    """Append the channel to the array body, matching its existing style."""
    if "\n" in inner:
        # pretty-printed: copy the indentation of the last entry
        lines = [ln for ln in inner.split("\n") if ln.strip()]
        indent = re.match(r"\s*", lines[-1]).group(0)
        trailing = inner[len(inner.rstrip()):]          # whitespace before ]
        return inner.rstrip() + ',\n' + indent + json.dumps(CHANNEL) + trailing
    # minified: single line
    return inner.rstrip() + ", " + json.dumps(CHANNEL)


changed = skipped_present = skipped_other = 0
touched = []

for path in sorted(glob.glob("*.html")):
    src = open(path, encoding="utf-8").read()
    out, last, hits = [], 0, 0

    for m in SAMEAS.finditer(src):
        inner = m.group(1)
        if MARKER not in inner:
            skipped_other += 1                 # another entity's sameAs
            continue
        if "youtube.com" in inner:
            skipped_present += 1               # already done
            continue
        out.append(src[last:m.start(1)])
        out.append(add_entry(inner))
        last = m.end(1)
        hits += 1

    if not hits:
        continue
    out.append(src[last:])
    new = "".join(out)

    # every JSON-LD block on the page must still parse
    for block in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', new, re.S
    ):
        json.loads(block)

    if not check:
        open(path, "w", encoding="utf-8").write(new)
    changed += hits
    touched.append(f"{path} ({hits})")

print(f"{'WOULD ADD' if check else 'ADDED'} channel to {changed} block(s) "
      f"across {len(touched)} page(s)")
print(f"  skipped, already present : {skipped_present}")
print(f"  skipped, not the business: {skipped_other}")
for t in touched:
    print("   ", t)
