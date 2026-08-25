#!/usr/bin/env python3
"""Set each page's schema dateModified AND its sitemap <lastmod> to the date it last REALLY changed.

Why this exists: every page was stamped 2026-06-21 or earlier while the site carried on
being edited into August, so the pages looked staler than they were. Review recency and
content freshness are now top-tier signals for AI Overview citation, and understating a
page's last update throws that away for free.

Why it is not just "today": bumping a date without a real content change is date-spoofing,
and Google says so. A commit that only moved the review count (2 lines) is not a content
update, so those commits are skipped. Anything larger counts.

Both halves matter and they drifted apart: on 25 Aug 2026 the pages were honest while
60 of 64 sitemap entries still claimed 2026-08-06, and the homepage claimed 2026-06-23.
`lastmod` is a crawl-scheduling signal, so understating it tells Google not to bother
re-crawling — three suburb pages sat "Crawled - currently not indexed" on a judgement
Google made back in May.

    python3 sync-dates.py           # write the honest dates
    python3 sync-dates.py --check   # report drift, change nothing
"""
import subprocess, re, sys, glob, io

TRIVIAL_LINES = 4   # a review-count bump touches 1-2 lines; allow a little slack
BASE = 'https://www.plasterandrenderingsolutions.co.uk'
_cache = {}

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True).stdout

def last_real_change(path):
    """Most recent commit whose diff to THIS file was more than a count bump."""
    if path in _cache:
        return _cache[path]
    _cache[path] = _last_real_change(path)
    return _cache[path]

def _last_real_change(path):
    for line in sh('git','log','--format=%H %cs','--',path).splitlines():
        sha, date = line.split()
        stat = sh('git','show','--numstat','--format=', sha, '--', path)
        # numstat rows for this file only
        tot = 0
        for row in stat.splitlines():
            parts = row.split('\t')
            if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
                tot += int(parts[0]) + int(parts[1])
        if tot > TRIVIAL_LINES:
            return date
    return None

def slug_for(loc):
    """Map a sitemap <loc> back to its source file. The homepage is index.html."""
    path = loc[len(BASE):] if loc.startswith(BASE) else loc
    return path.strip('/') or 'index'

def sync_sitemap(check):
    """Point every <lastmod> at the same git-derived date the page itself claims."""
    import os
    s = io.open('sitemap.xml', encoding='utf-8').read()
    stale = []

    def fix(m):
        block = m.group(0)
        loc = re.search(r'<loc>(.*?)</loc>', block)
        lm = re.search(r'<lastmod>([0-9]{4}-[0-9]{2}-[0-9]{2})</lastmod>', block)
        if not loc or not lm:
            return block
        f = slug_for(loc.group(1)) + '.html'
        if not os.path.exists(f):
            return block
        real = last_real_change(f)
        if not real or real == lm.group(1):
            return block
        stale.append((slug_for(loc.group(1)), lm.group(1), real))
        return block.replace('<lastmod>%s</lastmod>' % lm.group(1),
                             '<lastmod>%s</lastmod>' % real)

    out = re.sub(r'<url>.*?</url>', fix, s, flags=re.S)
    for slug, was, now in stale:
        print(f"sitemap  {slug:42} {was} -> {now}")
    if stale and not check:
        io.open('sitemap.xml', 'w', encoding='utf-8').write(out)
    return len(stale)

def main():
    check = '--check' in sys.argv
    changed = drift = 0
    for f in sorted(glob.glob('*.html')):
        s = io.open(f, encoding='utf-8').read()
        if '"dateModified"' not in s:
            continue
        real = last_real_change(f)
        if not real:
            continue
        claimed = set(re.findall(r'"dateModified": "([0-9]{4}-[0-9]{2}-[0-9]{2})"', s))
        if not claimed:
            continue          # placeholder token (case-study-template) — nothing to sync
        if claimed == {real}:
            continue
        drift += 1
        print(f"{f:44} {sorted(claimed)} -> {real}")
        if not check:
            s = re.sub(r'"dateModified": "[0-9]{4}-[0-9]{2}-[0-9]{2}"',
                       f'"dateModified": "{real}"', s)
            io.open(f, 'w', encoding='utf-8').write(s)
            changed += 1
    sm = sync_sitemap(check)
    if check:
        print(f"\n{drift} page(s) with a stale dateModified." if drift else "\nAll dateModified values are honest.")
        print(f"{sm} sitemap <lastmod> value(s) stale." if sm else "All sitemap <lastmod> values are honest.")
    else:
        print(f"\nUpdated {changed} page(s) and {sm} sitemap <lastmod> value(s).")

if __name__ == '__main__':
    main()
