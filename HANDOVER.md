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
- `python3 sync-dates.py` sets each page's `dateModified` **and its `sitemap.xml`
  `<lastmod>`** from its last **substantive** git commit (review-count-only commits are
  skipped, because bumping every date is date-spoofing). Run it AFTER committing content
  changes, then commit the dates. `--check` reports drift and writes nothing.
  **Both halves used to drift apart:** on 25 Aug 2026 every page was honest while **60 of 64
  sitemap entries still claimed 2026-08-06 and the homepage claimed 2026-06-23** — the
  stalest entry on the site was the most important page. `<lastmod>` is a crawl-scheduling
  signal, so understating it tells Google not to re-crawl. Do not hand-edit either one.
- Three pages added 24 Aug: `/render-over-pebbledash-sheffield`,
  `/planning-permission-render-sheffield`, `/rendering-in-winter-sheffield`. All unproven.

### Building a new page — the checklist that stops the known faults

1. Clone the `silicone-render-vs-monocouche` shell (head, `<style>`, nav, footer) so the
   design cannot drift.
2. **Check every CSS class you used exists in that inline stylesheet.** 20 of 45 did not on
   the first attempt and would have rendered as nothing. **This cuts both ways: the shell is
   self-contained and does NOT link app.css, so a class like `.tap44-btn` that is only
   defined in app.css does nothing on your new page.** On 25 Aug this left 12 links at 39px
   on `planning-permission-render-sheffield`, carrying the very class that exists to
   guarantee 44px. Measure the control in a browser; grep proves nothing here.
3. Copy `id="heroImg"` onto the hero `<img>` — a script references it and throws otherwise.
4. Add the `vercel.json` rewrite **or the clean URL 404s**, plus the sitemap entry.
5. Add inbound links. A page with none is orphaned.
6. Measure the `<title>` in **pixels**, not characters. Google truncates near 600px.
7. Render it and check: JS errors, accordion opens, 0px overflow at 390px, no mojibake.

### Editing an FAQ — this has bitten twice

Update the **JSON-LD and the visible copy**, then verify the schema text appears verbatim in
the rendered page. The visible version wraps its first sentence in `<strong>` and uses HTML
entities, so a plain-text replace updates the schema and silently misses the page.

### FAQ schema — done 25 Aug 2026

413 FAQ questions across the site, **0 with a question that is not on the page** (was 30),
answer drift 77 → 17. Fixed by realigning 21 questions and 62 answers to the **visible copy**
(the page is the source of truth — the visible wording gets improved over time and the schema
never follows), and removing 9 schema questions that had no visible counterpart at all.

The 17 remaining drifts are wording-only and were deliberately left. **When auditing this,
normalise entities, curly quotes and dashes before comparing** — exact string comparison
reports drift that does not exist.

### Alt text — audited 25 Aug 2026

355 images, 0 missing alt, 0 empty, 0 repeating the town name. Nine alt texts are over 125
chars on purpose because they are genuinely descriptive. **Do not trim those to hit a number.**

### The 10 self-contained pages — the standing blind spot

These do **not** link `app.css`, so every app.css fix silently misses them, and they are the
conversion cluster:

```
get-quote  pricing  about  how-we-apply  rendering-cost-sheffield  plastering-cost-sheffield
silicone-render-vs-monocouche  render-over-pebbledash-sheffield
planning-permission-render-sheffield  rendering-in-winter-sheffield
```

```bash
for f in *.html; do grep -q 'app\.[0-9a-f]\{8\}\.css' "$f" || echo "$f"; done
```

After any app.css rule change, and after building any new page, duplicate the rule into
these pages' own `<style>` blocks and **measure it in a browser on one of them**.

## State as of 8 Sep 2026

- **First Fulwood review published.** J Spencer, 5 star, 8 Sep, names silicone render *and*
  Fulwood unprompted. Live on `/fulwood-sheffield` as a visible card + `Review` node — that page
  had **zero** review cards before, despite 27 silicone mentions, and no review in the corpus had
  ever named Fulwood. Corpus now 101 captured.
- **Review count is still 110 and that is deliberate**, not drift. The GBP panel number was hidden
  behind the reply modal when this review came in. Read it off the profile and run
  `python3 sync-reviews.py <n>` — never derive it by adding one.
- **August full-month GSC logged** in the tracker: 109 clicks, 9.81K impressions, 4 pages with
  first impressions. Note it is a **calendar month** while the `Aug 2026` row is 28 days to 8 Aug —
  different windows, both kept.
- **Review count is 111.** Swept with `sync-reviews.py 111` from the GBP panel number. All 66
  pages agree on 111 / 5.0.
- **The 1 Sep Map Pack read still has not happened.** Sep column empty. Same location each month
  or the suburb numbers are not comparable.
- **Sep GSC (28d to 8 Sep): 99 clicks, 8.7K impressions, CTR 1.1%, average position 23.1.**
  Clicks +3% on August — flat. The 24 Aug content push has produced no measurable click growth.
  Live-crawled all 64 sitemap URLs again: 200, self-canonical, indexable, no redirects. **There is
  no technical fault.** Position is off-page, same conclusion as 23-24 Aug.
- ⛔ **Position 23.1 settles the CTR question: do NOT rewrite titles or meta descriptions.**
  `/plastering-sheffield` pulls 822 impressions and 2 clicks (0.24%), but at position 23 that is
  *expected*, not a defect. Sitewide 1.14% at position 23 is above curve. Confirmed busywork.

### Full verification pass — 8 Sep 2026, and the 4 false alarms it produced

Drove the LIVE site, not the local files. **Result: the site is sound.**

- **All 64 URLs at 390px, 768px and 1440px** — `0` JS errors at every width; `0` overflow at 768
  and 1440; **one** overflow at 390: `broomhill-sheffield` at **+3px** (was +10px in August, so it
  has improved, not regressed).
- **Both FAQ accordion implementations work on every page tested.** `.faq-btn`/`.faq-ans`
  (self-contained) and `.faq-q` (app.css). The self-contained set sets `aria-expanded`; the
  app.css set still does **not** — that is the known 413-button item, unchanged, not a regression.
- **Mobile nav** opens (2 → 12 visible links). **Projects gallery** arrows and all 64 thumbnails
  change the image, no JS errors.
- **Quote form** — 16 fields, 9 required, posts to `formspree.io/f/mvzdkwvw`. Empty submit is
  correctly blocked by validation. ⚠ **The form was NEVER submitted** — network was recorded and
  the only POST was Google Analytics. **Never submit it in a test: it lands as a real enquiry.**
- `terms` checkbox is 16px, but its **label is 42×308px and toggles it**, so the real tap target
  is 42px — 2px under, pre-existing, part of the known under-44px set.
- Private docs are safe: `*.md` is excluded from the deploy **and** `vercel.json` carries a
  deliberate `/(.*).md → /` 308. Company number, Lishmans and the Chapeltown address are absent
  from everything public.

**⚠ FOUR of my own checks cried wolf in one session. Suspect the harness first.**
1. `curl -L` on `/CITATIONS-NAP.md` reported **200 "EXPOSED"** — it was following the 308 to the
   homepage and reporting the homepage's status. **Read the body, not the final status code.**
2. Homepage "showed 110 while schema said 111" — that `110` is the EWI price **£110/m²**. Check
   the number sits next to the word "review" before calling it a review count.
3. Accordions reported **0/6 opening on every page** — the probe measured `innerText.length`, but
   these are `max-height` accordions whose text is always in the DOM. Measure the element's
   `offsetHeight`.
4. `fulwood-sheffield` measured **396px** at a 390px viewport — a `file://` artefact (fonts
   CORS-blocked, images 404). Over HTTP it is exactly 390. **Serve the directory before believing
   any width reading.**

### ⛔ KNOWN BUG in `sync-dates.py` — it wants to date-spoof 4 pages. Do not let it.

Found 8 Sep 2026. **`python3 sync-dates.py --check` currently reports 4 pages and 4 sitemap
entries as stale. All four are FALSE POSITIVES. Do not run the writer to "fix" them.**

```
rendering-sheffield  render-over-pebbledash-sheffield
planning-permission-render-sheffield  rendering-in-winter-sheffield
```

**The cause.** `TRIVIAL_LINES = 4` decides "was this a real content change?" by counting added +
deleted lines. A review-count sweep touches **1 line on most pages but 3 on these four**, because
they print the count in the hero, in a stat line *and* in the schema. Three changed lines = 6 in
numstat, over the budget, so a `110 -> 111` edit is misread as a content update and the page gets
a fresh `dateModified` **and** a fresh sitemap `<lastmod>`. That is precisely the date-spoofing
the script's own docstring exists to prevent, **and the bug scales with how prominently a page
displays its reviews** — the better the page, the more it lies.

**Do NOT "fix" it by raising TRIVIAL_LINES.** That just moves the threshold and silently starts
skipping genuine small edits.

**A content-aware rule was attempted on 8 Sep and REVERTED** — read the diff before ignoring the
lines only if they sit next to the word "review". It correctly skipped the count sweep, but it
also stopped treating `sync-dates`' **own** commits as trivial, and those commits edit the
`dateModified` line itself. The result was **37 pages and 39 sitemap entries wanting to move,
mostly backwards.** The circularity — the script's own writes are part of the history it reads —
is the real problem, and it needs a dedicated session, not a fix bolted onto a ship.

**Until then:** after a review-count sweep, run `--check`, expect those four, and **leave them.**

#### ⚠ 17 Sep 2026: that count is now **11, not 4**, and the extra 7 are the same false positive

Adding the YouTube channel to `sameAs` touched 66 blocks on 57 pages. The script reads
**added + deleted lines**, so:

| page shape | lines changed | verdict |
|---|---|---|
| **one** `sameAs` block | 1 deleted + 2 added = **3** | under budget, correctly ignored |
| **two** `sameAs` blocks | 2 deleted + 4 added = **6** | over budget, **misread as a content change** |

Same defect as the review-count case, a different trigger: it scales with **how many schema
blocks a page carries**, not with how prominently it shows reviews. The seven new ones —
`index`, `silicone-render-sheffield`, `monocouche-render-sheffield`, `dry-lining-sheffield`,
`render-repair-sheffield`, `s17-ewi-case-study`, `sandygate-silicone-render-case-study` —
all carry two blocks. **All eleven are false positives. Do not run the writer.**

**`how-we-apply` was the twelfth and it was genuine** (the video was replaced), so its
`dateModified` **and** its sitemap `<lastmod>` were set to 2026-09-17 **by hand, together**,
and it no longer appears. Hand-editing is only safe when both halves move in the same edit —
that is what stops the two drifting apart, which is the fault this whole section exists for.
The dates on disk are honest today: fulwood-sheffield is 2026-09-08 from a genuine content change;
the other four correctly still say 2026-08-24/25.

### Citations: `CITATIONS-NAP.md` is the master block — 8 Sep 2026

New file at the repo root (off the deploy via `*.md`). Every value cross-checked against the LIVE
site schema. Read it before touching any directory listing.

- ⛔ **The Companies House registered office is the ACCOUNTANT's address** —
  16-18 Station Road, Chapeltown, S35 2XH (Lishmans LLP). The trading address is
  **3 Rocher Close, Grenoside, S35 8QP**. Only the trading address goes in a citation; the other
  creates a two-suburb, two-postcode NAP conflict. Company no **09075271**, SIC 43310.
- **Chris IS an approved applicator for K-Rend, Ecorend AND Weber** (confirmed 8 Sep). The site
  claims all three in 8 places plus a homepage logo and the claim is **accurate — do not strip
  it.** It sits in FAQ schema tied to a 25-year warranty promise.
- Declined and recorded with reasons so they are not re-proposed: TrustATrader, Which?, TrustMark
  (all paid) and the Checkatrade upgrade (lead-gen decision, never recommend on SEO grounds).
- **Bing Places is the top free action** — Bing's index is what ChatGPT searches, so it is the one
  free listing that feeds AI search directly.

### Harness trap logged 8 Sep: `file://` invents overflow on this site

Measuring a page over `file://` reported `/fulwood-sheffield` at **396px** at a 390px viewport —
a 6px overflow that does not exist. The webfonts are CORS-blocked and the images 404 under
`file://`, so fallback metrics reflow the page. Served over HTTP, the pre-edit and post-edit files
both measure exactly **390**. **Serve the directory (`python3 -m http.server`) before believing any
width or overflow reading**, and diff against the unedited file rather than against the handover's
recorded number. Broomhill remains the only page of 64 that genuinely overflows.

### Still open

- **"Crawled – currently not indexed": IDENTIFIED 25 Aug 2026, and smaller than it looked.**
  The 8 URLs are **five dead Wix URLs with trailing slashes** — `/silicone-render/`,
  `/monocouche-render/`, `/external-wall-insulation/`, `/contact/`, `/pricing/` — which all
  308 to the live page and *should* be unindexed, plus **three real suburb pages**:
  `norton-sheffield`, `nether-edge-sheffield`, `totley-sheffield`. **No service page is
  missing from the index.**
  **The internal-link theory was WRONG and is dropped:** norton has **38** inbound links and
  totley **33**, near the top of the range, while `lodge-moor` and `parson-cross` sit on 3
  each and are indexed fine. Word counts are all at the median. Link thinness explains
  nothing — do not re-open that line of enquiry.
  All three were last crawled in **May/June**, so Google's judgement predates every bit of
  the August work. The stale sitemap `<lastmod>` that was suppressing re-crawls is fixed;
  **the remaining action is owner-side — request indexing on those three in URL Inspection.**
  The legacy URLs take **two redirect hops** (`/silicone-render/` → `/silicone-render` →
  `/silicone-render-sheffield`). Harmless, collapsible to one if ever worth the churn.
- `broomhill-sheffield` 10px overflow (see the section above). Re-measured 25 Aug: still
  exactly 10px, and still the only page of 64 that overflows at 390px.
- FAQ answers on the self-contained pages are capped `max-height:400px` (the app.css pages
  use 1000px). Nothing clips today, but `planning-permission`'s tallest answer is **363px at
  390px — 91% of the cap**. One more sentence and it truncates silently.
- 413 FAQ buttons have no `aria-expanded`. There are **two accordion implementations**:
  app.css pages use `.faq-body`, the self-contained pages use `.faq-btn`/`.faq-ans` and do
  set the ARIA. Neither uses `<details>` — a harness looking for that finds nothing.
- `monocouche-render-sheffield` preloads a **164KB** desktop hero with no `-m` variant. The
  other nine without one are 16–76KB and are fine; do not spend a session on them.


## State as of 18 Sep 2026

- **113 reviews? No — 112.** Read off the GBP panel and swept with `sync-reviews.py 112`.
  Libbi Mellors, 18 Sep, is the **first review in the corpus to name Southey**, and it names
  silicone rendering too. Published on `/southey-sheffield` as a visible card + `Review` node —
  that page had 28 silicone mentions and **zero** review cards, the same shape Fulwood was in
  before 8 Sep. Corpus now 102 captured.
  ⚠ **The GBP notification email TRUNCATES the review** ("...area of Sheffield....") — the full
  wording only exists in the reviews panel. Never publish from the email.
  Published verbatim including **"on there house"** and lowercase **"Southey green"**. The
  original has a line break before "He was recommended"; it is published as one flowing
  paragraph so the visible quote and the `reviewBody` are byte-identical to each other.

### ⛔ The YouTube channel exists, and the site had never claimed it

`@PandRSheffield` — "P&R Solutions Sheffield", 1 video, links to the site in its About. The
site linked back **nowhere**: no channel URL in any HTML/MD/XML, and `sameAs` listed only
Facebook, Instagram and X. A backlink Google cannot tie to you is worth less than one it can.
Now on every business node.

### ⛔ `how-we-apply` was running a SUPPLIER'S video as our own

The embed was `o4SN4Qq7v9g`, captioned *"P&R Solutions — spraying silicone top coat Sheffield"*.
Checked via YouTube's oEmbed endpoint: that video is **"The Predator Pro Spray"** on the channel
**Direct Building Products**. A machine promo presented as our process footage, on the page whose
whole job is explaining our process. Replaced with `BiT_kvAQ6Ng` (Ecorend silicone, Sandygate,
before/after) which is genuinely ours. The 9:16 frame was built for a vertical Short and
letterboxed the landscape replacement, so both players are now 16:9.

**How to check a video is yours:** `curl -s "https://www.youtube.com/oembed?url=<watch-url>&format=json"`
returns `author_name` and `author_url`. Do not assume from the caption.

### ⚠ A grep of the repo is not a check of the site — 8 pages proved it

After sweeping `sameAs` across 57 pages and reporting it done, **crawling all 64 live URLs found
8 with no channel**. They were not missed by a faulty sweep: the script only appends to an array
already holding our own Facebook URL, and those 8 had no such array. All 8 carry a business node;
**seven had no `sameAs` at all** and had never advertised a single social profile, and
`plastering-sheffield` had one holding only two Google Maps URLs. A pre-existing gap that was
invisible to grep and only showed up under a crawl. Closed by `add-social-sameas.py`, which parses
each block and edits the business nodes rather than regex-inserting into eight differently shaped
documents. Existing entries are kept.

⚠ Re-serialising JSON-LD can break a sweep that depends on formatting. Checked afterwards:
`sync-reviews --check` still agrees on 112, 125 blocks parse, no mojibake, all 8 render clean.

### VideoObject removed from `rendering-in-winter-sheffield` — 18 Sep

GSC reported *"Some fixes failed for Video indexing — Video isn't on a watch page"*. **It was
right and the fix could never have worked.** The clip is a 14-second supporting shot at line 619
of an 852-line article about winter rendering; Google requires the video be the page's **main
content**. Re-requesting validation would fail every time. The `VideoObject` node is gone and the
`<video>` still plays for visitors — the only thing lost is eligibility for a rich result the page
could never qualify for. **Do not re-add it** unless the clip gets its own dedicated page.

### Two photo gaps, and they are the same gap

There is **no sand-and-cement photo and no render-repair photo anywhere in the image library**.
The sand-and-cement page currently runs a *monocouche* photo; the repair page runs *silicone* job
photos. One scratch-coat shot and one cracked-wall before/after off Chris's phone would fix two
live pages and two FreeIndex service entries. **Do not paper over it by reusing a finished-render
photo** — the Sandygate house is grey brick with white thin-coat panels and contradicts both.

### Still open
- `sync-dates.py --check` reports **11** false positives (see the section above). Leave them.
- 45 of the 53 suburb pages have no review naming them.
- `business-card-preview`, `logo-preview`, `case-study-template` still present. Unreachable
  (308 to home, excluded from the deploy) and harmless. Deletable but deliberately not deleted —
  they are design artefacts, not defects.


### ⛔ Six heroes were invisible — `opacity:0.13` — found 18 Sep 2026

Chris: *"the hero images were all supposed to have been checked for this too dark"*. He was right,
and it was measurable.

The six **self-contained** pages cloned from the `silicone-render-vs-monocouche` shell carried
`.hero-img { opacity:0.13 }` **on top of** a `.hero-overlay` gradient of
`rgba(0,0,0,0.90) → rgba(0,15,0,0.35)`. Double-darkened: the photo at 13% *and* a 90% black scrim.
The other 53 pages have no opacity on `.hero-img` at all and let the gradient do the work.

Mean luminance of the hero band, same method on every page:

| | before | after | rest of site |
|---|---|---|---|
| the six | **32–40** | **58–63** | 54–100 |

Fixed to `opacity:0.85`. ⚠ **Text contrast was measured before and after, not assumed** — the
heading sits in the 0.90-black corner of the gradient, so white-on-backdrop is **16.0:1 at
1280px and 17.4:1 at 390px**, against a WCAG AA requirement of 4.5:1. Raising the image did not
touch the text.

Affected: `planning-permission-render-sheffield`, `plastering-cost-sheffield`,
`render-over-pebbledash-sheffield`, `rendering-cost-sheffield`, `rendering-in-winter-sheffield`,
`silicone-render-vs-monocouche`.

⛔ **The shell still has to be checked when cloning.** This is the same trap as the `.tap44-btn`
one: the shell is self-contained, so a value inside it propagates to every page built from it and
never shows up in an app.css diff.

### Full image audit — 18 Sep 2026, 69 pages, 439 `<img>`

| check | result |
|---|---|
| HTTP 4xx image requests | **0** |
| missing or empty `alt` | **0** |
| distorted / stretched | **0** |
| broken / not loading | **14 — all on `case-study-template`** (placeholder paths, unreachable) |
| no `width`/`height` | 65, **all on `projects`** — and **measured CLS is 0.0000** at 390 and 1280, so it is not causing shift. Left alone. |

`case-study-template` is the only page with a dark hero left (mean 30.6) and its `JOB_HERO_IMG`
placeholder is why. It 308s to the homepage and is off the deploy. Not a live fault.
