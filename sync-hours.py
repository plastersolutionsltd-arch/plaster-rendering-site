#!/usr/bin/env python3
"""Bring the site's OpeningHoursSpecification into line with the Google Business Profile.

20 Sep 2026. Chris widened his GBP hours after we found that "open at the time of
search" is the 5th strongest Local Pack ranking factor, and that he was showing
"Closed" every Sunday -- including on the Sunday he measured himself at 9th.

    was (site)                          now (GBP)
    Mon-Fri  08:00-20:00                Mon-Fri  07:00-20:00
    Saturday 09:00-13:00                Saturday 07:00-17:00
    Sunday   absent                     Sunday   09:00-16:00

Site hours that disagree with the profile are exactly the NAP inconsistency
CITATIONS-NAP.md exists to prevent, so this has to move with it.

⚠ There are SEVEN distinct whitespace shapes of this block across the site -- the
same trap as the reviewCount sweep on 28 Jul and the sameAs sweep on 18 Sep. So
matching is on STRUCTURE (tolerant \\s*) rather than on any one spelling, and the
inserted Sunday block copies the spacing of the Saturday block it follows.

Usage:
    python3 sync-hours.py --check    # report only, writes nothing
    python3 sync-hours.py            # apply
"""
import glob
import json
import re
import sys

check = "--check" in sys.argv

# Mon-Fri: only the opening time moves.
WEEK = re.compile(r'("dayOfWeek":\s*\[\s*"Monday".*?"opens":\s*")08:00(")', re.S)

# Saturday: both times move, and Sunday is appended after it.
SAT = re.compile(
    r'(\{\s*"@type":\s*"OpeningHoursSpecification",\s*"dayOfWeek":\s*"Saturday",\s*'
    r'"opens":\s*")09:00("\s*,\s*"closes":\s*")13:00("\s*\})',
    re.S,
)


def sunday_like(sat_block: str) -> str:
    """Build a Sunday block copying the Saturday block's own spacing."""
    sun = sat_block.replace('"Saturday"', '"Sunday"')
    sun = re.sub(r'("opens":\s*")\d{2}:\d{2}(")', r"\g<1>09:00\g<2>", sun)
    sun = re.sub(r'("closes":\s*")\d{2}:\d{2}(")', r"\g<1>16:00\g<2>", sun)
    sep = ",\n        " if "\n" in sat_block else ", "
    return sat_block + sep + sun


changed = []
for path in sorted(glob.glob("*.html")):
    src = open(path, encoding="utf-8").read()
    if "OpeningHoursSpecification" not in src:
        continue
    if '"Sunday"' in src and "07:00" in src:
        continue                      # already done

    out = WEEK.sub(r"\g<1>07:00\g<2>", src)

    def sat_repl(m):
        fixed = m.group(1) + "07:00" + m.group(2) + "17:00" + m.group(3)
        return sunday_like(fixed)

    out = SAT.sub(sat_repl, out)
    if out == src:
        continue

    # every JSON-LD block on the page must still parse
    for block in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', out, re.S
    ):
        json.loads(block)

    if not check:
        open(path, "w", encoding="utf-8").write(out)
    changed.append(path)

print(f"{'WOULD UPDATE' if check else 'UPDATED'} {len(changed)} page(s)")
for c in changed[:8]:
    print("   ", c)
if len(changed) > 8:
    print(f"    …and {len(changed) - 8} more")
