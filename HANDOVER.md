# plaster-rendering-site — handover

Live site for P&R Solutions: **plasterandrenderingsolutions.co.uk**
Static HTML on Vercel, auto-deploys from `main`. 66 HTML files at the repo root,
61 public pages + 5 noindex. No build step for the pages themselves.

> This file is excluded from the deploy by the `*.md` rule in `.vercelignore`.
> Check that rule still holds before adding any doc to the repo root.

---

## The traps. Read these before touching anything.

### 1. Caching: `immutable` without a hashed filename strands people for a year
`/app.*.css` and `/fonts/` are served `max-age=31536000, immutable`. That header
promises the bytes at that URL will never change.

- **`app.css` is content-hashed** (`app.212d8511.css`). If you edit it, rename it with a
  fresh hash and update the `href` on all 55 pages, or returning visitors keep the old
  stylesheet. This caused a real regression on 8 Aug: the font move put `@font-face` in
  app.css while the HTML dropped its Google Fonts link, so returning visitors got no
  webfonts at all.
- **`/images/` is deliberately NOT immutable** — one day plus a week of
  stale-while-revalidate — because those filenames are not hashed and images do get
  replaced. 72 assets were swapped in place between May and August under the old
  immutable header and never reached anyone who had already visited.
- **Replacing an image in place does nothing for existing visitors.** Content-hash the
  name (`greenhill-matt-monocouche.c1f2f27c.webp`) or the change is invisible. Verifying
  with `curl` proves only what the origin sends, not what a browser shows.
- HTML pages are `max-age=0, must-revalidate`, so page edits always propagate. Fine.

### 2. Every new page needs its own `vercel.json` rewrite
There is no catch-all clean-URL rule. A page without a rewrite entry 404s in production
even though it exists. Add to `rewrites`, add to `sitemap.xml`, and give it inbound links
from related pages — Beighton and Meersbrook sat unindexed for months on 5–7 links.

### 3. Fonts are self-hosted. Do not reintroduce Google Fonts.
`/fonts/outfit-var.woff2` and `/fonts/inter-var.woff2` (81KB total, variable, one file per
family). They are preloaded in the HTML `<head>` and declared `@font-face` in app.css.
Loading them from fonts.googleapis.com with `display=swap` was **100% of this site's CLS** —
blocking fonts dropped it from 0.15/0.168 to exactly 0. Metric-matched fallback faces do
**not** work as a substitute: Chrome will not resolve `src: local("Arial")`.

### 4. `app.css` is a PRECOMPILED Tailwind build
It contains only the utilities already in use. `text-white/50` and `/75` exist; `/80`,
`/85`, `/40` do not, and an unused opacity utility renders as **no colour at all**,
silently. Set such colours inline instead.

### 5. Reviews: verbatim, visible, and only real ones
- `reviews-source.md` holds the 98 captured Google reviews. **Nothing goes on the site
  that is not in there.** Three invented testimonials were removed from dry-lining on
  8 Aug; publishing untraceable reviews is a civil offence under the DMCC Act.
- Publish **verbatim** — never fix spelling or grammar. The visible quote and the JSON-LD
  `reviewBody` must match each other *and* the original.
- Every review in markup must be **visible on that page**. Google requires it; seven pages
  were breaching this.
- **Never hand-edit the review count.** `python3 sync-reviews.py 108` sets it everywhere;
  `--check` reports drift. It had drifted to three different numbers across the site.

### 6. Batch edits
Use Python, not perl/sed — perl in byte mode double-encodes UTF-8 into mojibake. HTML
entities are **not** decoded inside a `<script type="application/ld+json">` block, so use a
literal `&` there and `&amp;` in the visible HTML. When sweeping a value, check for format
variants: a 28 Jul update missed 4 pages because they used `"reviewCount":"104"` with no
space after the colon.

---

## Routine checks

```bash
python3 sync-reviews.py 108 --check     # review count drift
curl -sI <url> | grep -i cache-control  # confirm what a browser will actually cache
```

Titles: judge by **pixel width**, not character count. Google truncates near 600px at
Arial 20px. Character count flags ~55 pages that are perfectly fine.

---

## State as of 9 Aug 2026

Clean: 61/61 URLs 200 with no redirects, 123 JSON-LD blocks valid, 27 reviews all shown
verbatim, CLS 0, no broken links or images, no mojibake, review count 108 everywhere.

**Open, needs Chris:**
- Review requests that name the **product and the area** — zero of 98 reviews say
  "monocouche", which is why that keyword sits out of the Map Pack while MAC Rendering
  holds it. This is the single biggest lever and nothing on the site substitutes for it.
- Weber approved-applicator form, parked until the membership renewal.
- Map Pack re-check 1 Sep, **from the same location each month** or the suburb numbers
  are not comparable.
- 57 rows in `reviews-source.md` are still truncated by Google's own panel.

**Open, small:**
- ~24 controls under 44px that need header layout changes.
- `business-card-preview`, `logo-preview`, `case-study-template` have real defects
  (overflow, broken placeholders) but are noindex and 404 in production. Deletable.
- `~/Projects/PR-Logos-00FF00/` is not under version control.


## Known cosmetic issue: broomhill-sheffield overflows 10px at 390px

Not fixed, deliberately. Diagnosed 24 Aug 2026 so nobody re-investigates from scratch:

- Isolated by hiding sections in turn: the culprit is the **final "Other Areas We Cover"
  / CTA section**. Hiding it takes scrollWidth 400 -> 390. Hiding any other section only
  gets to 393, so there are minor secondary contributors too.
- **Ruled out:** unbalanced tags (a/div/section/p all balance), wrong declared image
  dimensions (`s10-monocouche1.webp` really is 1920x1579 as declared), a long unbreakable
  word, and a missing `-m` variant.
- Measuring inside that section is awkward because everything is `.reveal` (opacity/
  visibility 0) until scrolled, so widths read as 0. Force `.reveal.visible` first.
- Note `innerText` on those anchors concatenates a CSS-uppercased label, which makes a
  button look like it wraps a whole block. It does not.

It is 10px on 1 page of 64. Do NOT paper over it with `overflow-x:hidden` — that masks
real overflow everywhere else and breaks position:sticky.


## State as of 25 Aug 2026

- **110 Google reviews, 5.0.** Change it only with `python3 sync-reviews.py <n>` using the
  number from the GBP panel — it sweeps all 66 pages, the `/projects` stat tile and
  `llms.txt`. Never derive it by adding one.
- `python3 sync-dates.py` sets each page's `dateModified` from its last **substantive** git
  commit (review-count-only commits are skipped, because bumping every date is date-spoofing).
  Run it AFTER committing content changes, then commit the dates.
- Three pages added 24 Aug: `/render-over-pebbledash-sheffield`,
  `/planning-permission-render-sheffield`, `/rendering-in-winter-sheffield`. All unproven.

### Building a new page — the checklist that stops the known faults

1. Clone the `silicone-render-vs-monocouche` shell (head, `<style>`, nav, footer) so the
   design cannot drift.
2. **Check every CSS class you used exists in that inline stylesheet.** 20 of 45 did not on
   the first attempt and would have rendered as nothing.
3. Copy `id="heroImg"` onto the hero `<img>` — a script references it and throws otherwise.
4. Add the `vercel.json` rewrite **or the clean URL 404s**, plus the sitemap entry.
5. Add inbound links. A page with none is orphaned.
6. Measure the `<title>` in **pixels**, not characters. Google truncates near 600px.
7. Render it and check: JS errors, accordion opens, 0px overflow at 390px, no mojibake.

### Editing an FAQ — this has bitten twice

Update the **JSON-LD and the visible copy**, then verify the schema text appears verbatim in
the rendered page. The visible version wraps its first sentence in `<strong>` and uses HTML
entities, so a plain-text replace updates the schema and silently misses the page.

### Still open

- **10 FAQ answers are in FAQPage schema but not visible on the page** (7 on `/faq`, 3 on
  `index.html`). Google requires FAQ content to be visible. Only known defect on the site.
- 8 pages "Crawled – currently not indexed" in GSC, unidentified; all technical causes ruled out.
- `broomhill-sheffield` 10px overflow (see the section above).
