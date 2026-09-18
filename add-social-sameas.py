#!/usr/bin/env python3
"""Give every business node the full social sameAs set.

Found 18 Sep 2026 by crawling the LIVE site after the YouTube sweep: 8 of the
64 sitemap URLs had no channel. They were not missed by a broken sweep --
add-youtube-sameas.py only appends to an existing array carrying our own
Facebook URL, and these 8 had no such array:

    ewi-sheffield          get-quote   rendering-cost-sheffield
    silicone-render-vs-monocouche      plastering-cost-sheffield
    pricing                projects    plastering-sheffield

All 8 DO carry a LocalBusiness / HomeAndConstructionBusiness / Organization
node. Seven have no sameAs at all -- they have never advertised any social
profile. The eighth, plastering-sheffield, has a sameAs holding only two
Google Maps URLs and no social profiles.

So this is a pre-existing gap the YouTube work uncovered, not one it caused.

Rather than regex-insert a key into eight differently-shaped documents, each
JSON-LD block is parsed, the business nodes are edited, and the block is
re-serialised at its original indent. Existing sameAs entries are KEPT --
plastering-sheffield's two Maps URLs survive, with the social set appended.

Usage:
    python3 add-social-sameas.py --check    # report only
    python3 add-social-sameas.py            # apply
"""
import glob
import json
import re
import sys

# the set carried by the most complete pages on the site
SOCIAL = [
    "https://www.facebook.com/plasterandrenderingsolutions",
    "https://www.instagram.com/plasterandrenderingsolutions",
    "https://x.com/Chris76550497",
    "https://www.youtube.com/@PandRSheffield",
]
BIZ = {"LocalBusiness", "HomeAndConstructionBusiness", "Organization"}
BLOCK = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)

check = "--check" in sys.argv


def is_biz(node):
    t = node.get("@type")
    t = [t] if isinstance(t, str) else (t or [])
    return bool(BIZ & set(t))


def fix(node):
    """Append the social set to this node's sameAs, keeping what is there."""
    same = node.get("sameAs")
    if isinstance(same, str):          # a lone string (e.g. a City wikipedia link)
        return False                   # never touch those
    same = list(same or [])
    added = [u for u in SOCIAL if u not in same]
    if not added:
        return False
    node["sameAs"] = same + added
    return True


def walk(obj, hits):
    if isinstance(obj, dict):
        if is_biz(obj) and fix(obj):
            hits.append(obj.get("name") or obj.get("@type"))
        for v in obj.values():
            walk(v, hits)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, hits)


changed = []
for path in sorted(glob.glob("*.html")):
    src = open(path, encoding="utf-8").read()
    if "youtube.com/@PandRSheffield" in src:
        continue                        # already carries the channel
    out, last, hits = [], 0, []
    for m in BLOCK.finditer(src):
        raw = m.group(2)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        before = json.dumps(data, sort_keys=True)
        walk(data, hits)
        if json.dumps(data, sort_keys=True) == before:
            continue
        pretty = "\n" in raw.strip()
        new = json.dumps(data, ensure_ascii=False, indent=2 if pretty else None)
        out.append(src[last:m.start(2)])
        out.append(("\n" + new + "\n") if pretty else new)
        last = m.end(2)
    if not hits:
        continue
    out.append(src[last:])
    new_src = "".join(out)
    for b in BLOCK.findall(new_src):
        json.loads(b[1])                # must still parse
    if not check:
        open(path, "w", encoding="utf-8").write(new_src)
    changed.append(f"{path} ({len(hits)} node(s))")

print(f"{'WOULD FIX' if check else 'FIXED'} {len(changed)} page(s)")
for c in changed:
    print("   ", c)
