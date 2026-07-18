# AI Search Optimisation Project
**Site:** plasterandrenderingsolutions.co.uk  
**Started:** June 2026  
**Goal:** Get cited in Google AI Overviews, Bing Copilot, and AI Mode for Sheffield plastering searches

---

## Current Baseline (Bing Webmaster Tools — 3 months to June 2026)

| Metric | Value |
|---|---|
| Total Clicks (Bing) | 2 |
| Total Impressions (Bing) | 13 |
| Avg. CTR | 15.38% |
| Copilot AI Citations (3M) | 2 |
| Avg. Cited Pages | 0 |

**Top Bing Keywords:** "plaster and rendering solutions" (pos 15), "plasterer & renderer" (pos 1), "venetian plaster sheffield" (pos 31)  
**Best Bing Page:** Spray rendering blog post — 3 impressions, pos 4 (most promising for AI citations)

---

## What Changed at Google I/O 2025

Google fundamentally shifted search with two announcements:

1. **AI Overviews** — now showing in 40%+ of all queries. These are AI-generated summaries above the blue links. For local service searches ("plasterer Sheffield", "render cost Sheffield"), AI Overviews pull from trusted pages and Google Business Profiles. Getting into the Overview = getting seen before anyone else.

2. **AI Mode** — a full conversational search experience (rolling out globally). Instead of 10 blue links, users get a synthesised answer with citations. Local queries show a summary + a Business Profile carousel. The traditional "Position 1" matters less. Being cited in the AI answer matters most.

**What this means for local trades:** Google's AI now answers "who's the best plasterer in Sheffield?" directly. If your site and GBP aren't set up to feed the AI, you're invisible to those searchers.

---

## Site Audit Summary

### Strengths
- 62 pages total, 48 suburb/location pages (strong local coverage)
- 58/62 pages have schema markup (well above average)
- Schema types already used: FAQPage, HowTo, Service, LocalBusiness, AggregateRating, BreadcrumbList, GeoCoordinates
- 100+ Google reviews at 5.0 stars — major E-E-A-T signal
- FAQ page with strong conversational questions (silicone render, EWI, monocouche)
- Pricing page and how-we-apply page exist

### Gaps (Priority Order)
1. **No `Speakable` schema** — used by <10% of sites, big AI citation signal
2. **No About / Team page** — AI engines need E-E-A-T proof (who is doing the work)
3. **Only 2-3 blog posts** — needs ongoing "capsule answer" content for question queries
4. **No `Review` schema on individual pages** — suburb pages lack review evidence
5. **Missing trade body / directory citations** — Checkatrade, Which?, FMB, etc.
6. **GBP not audited** — completeness score unknown; this is #1 AI signal
7. **No `Speakable` or `Article` schema on blog posts**
8. **Bing indexing may be partial** — only 6 pages showing in Bing; 56 pages invisible

---

## Action Plan

### PHASE 1 — Fix the Foundation (Do First, Highest Impact)
*Target: weeks 1–2*

- [x] **1.1 — GBP audit** ✅ Done 10 Jun 2026
  - Categories confirmed: Plasterer (primary) + Stucco contractor + Dry Wall Contractor + Insulation Contractor + Building contractor (added)
  - Business description rewritten: 748/750 chars, fixed cut-off ending, added 103 reviews + 25-year warranty + free quote CTA
  - Products section reviewed — well set up with photos, descriptions, landing page URLs
  - Posts already running weekly ✅
  - Opening date June 2012 confirmed ✅
  - ⚠️ Watch: interactions declining (78 in Mar → 20 in Jun) — check Calls tab monthly
  - Still to do: add Q&A section (4 questions from action plan), photo count audit (target 100+)

- [x] **1.2 — Submit all 57 pages to Bing IndexNow** ✅ Done 10 Jun 2026
  - IndexNow key deployed, all 57 URLs submitted via API (HTTP 202)
  - `.co.uk` property added and verified in Bing Webmaster Tools
  - Sitemap submitted — full index expected within 48–72 hours

- [x] **1.3 — Add `Speakable` schema to homepage and FAQ page** ✅ Done 10 Jun 2026
  - Homepage: targets `#hero-sect h1`, `#hero-sect p`, `.faq-q`, `.faq-ans`
  - FAQ page: targets `#hero-sect h1`, `.faq-body p`
  - Mark the most important Q&A answers as `speakable: true`
  - Speakable tells AI assistants exactly which text to read aloud/cite
  - *Why: Used by <10% of sites — immediate competitive advantage*

- [ ] **1.4 — Claim and optimise directory listings**
  - Checkatrade (if not done) — most important UK trades signal
  - Yell.com — explicitly cited by AI Mode local results
  - Yelp UK — cited in Bing/Copilot local results
  - Which? Trusted Traders
  - TrustMark
  - FMB (Federation of Master Builders) if eligible
  - *Why: AI cites "trusted directories" as credibility signals for local businesses*

---

### BACKLINK AUDIT — 10 Jun 2026

#### ⚠️ URGENT: The .com domain issue

`plasterandrenderingsolutions.com` is showing up LIVE in Google with multiple pages (home, applying-render, plastering-services, services, about-us). This is a separate website competing with `.co.uk` for the same keywords. It is splitting link equity and confusing Google about which domain is canonical — likely a major reason for being stuck on page 2.

**Action required:** Find out who owns `plasterandrenderingsolutions.com`. If you own it, set up 301 redirects from all `.com` pages to the matching `.co.uk` pages, or take the site down. If you don't own it, seek domain/legal advice.

#### Backlink status by source

| Source | Status | Action |
|---|---|---|
| Yell.com | Listed but as **"Plaster solutions ltd"** — wrong name, likely thin content | Log in and correct name + add full description + website URL |
| Checkatrade | **Cannot find profile** in search — may be under wrong name | Find your login, confirm profile URL, ensure website field = `.co.uk` |
| K-Rend approved applicator | **Not listed** — competitors (MAC Rendering) are | Email `info@k-rend.co.uk` — ask to be added to their applicator finder |
| Weber contractor finder | **Not listed** — they have "Recognised" and "Recommended" tiers | Submit via `uk.weber/form/enquiries/find-a-contractor` |
| Ecorend / Parex | Not checked | Email their technical team — same approach as K-Rend |
| TrustATrader | **Not found** — EDC Render Plaster IS listed here | Paid annual membership (non-refundable, 12-month min) — call 01438 870097 for pricing before committing |

#### Why manufacturer backlinks matter most

K-Rend, Weber, and Ecorend are high-authority brand domains. A listing on their "find an approved applicator" pages is:
- A do-follow backlink from a trusted domain (direct ranking signal)
- Proof of expertise that AI engines read as E-E-A-T
- How customers actively search for approved installers ("K-Rend approved contractor Sheffield")

Competitors MAC Rendering and EDC Render Plaster are already listed on these pages — this is a gap to close immediately.

#### Priority order this week

1. Resolve `.com` domain situation
2. Email K-Rend (`info@k-rend.co.uk`) — 1 email, free, high authority backlink
3. Submit Weber contractor enquiry form (`uk.weber/new-contractor-selection-criteria`)
4. Email Ecorend/Parex technical team
5. Fix Yell.com profile — correct name, add full description
6. Find and verify Checkatrade profile is complete and links to `.co.uk`
7. Register on TrustATrader (paid — get quote first, call 01438 870097)

---

### PHASE 2 — Content That AI Will Cite (Medium Term)
*Target: weeks 3–6*

- [x] **2.1 — Create an About / Who We Are page** ✅ Done 20 Jun 2026
  - Built `/about` (about.html) matching how-we-apply template chrome
  - Founder: Chris Glover, full NVQ, 25+ yrs in trade; company founded 2012
  - `Person` schema (#chris-glover) with `knowsAbout`, `hasCredential` (NVQ), `jobTitle`, linked as business `founder`/`employee`; LocalBusiness now has `foundingDate:2012`; page typed `AboutPage` with `mainEntity` = Chris; FAQPage + Breadcrumb + Speakable also added
  - Real credential logos shown (K-Rend, Ecorend, CHAS) — all assets verified to exist
  - Linked from homepage desktop nav + mobile nav + footer; added to sitemap.xml
  - ⚠️ TODO: replace "CG" monogram with a real photo of Chris when supplied (bigger E-E-A-T boost) — swap `.person-monogram` block in about.html for `<img>`
  - All 3 JSON-LD blocks validated; tag balance checked

- [ ] **2.2 — Rewrite FAQ page with "capsule answers"**
  - Each answer: lead with a 40–60 word direct answer, then evidence
  - Format: Question (H2) → 1-paragraph direct answer → supporting detail
  - This is the exact format AI Overviews extract from
  - Add `Speakable` markup to top answers

- [ ] **2.3 — Write 4 targeted blog posts (AI-citation format)**
  Each post answers one high-intent question:
  - "How much does silicone render cost in Sheffield? [2026 guide]" — target pos 4 blog post currently getting Bing impressions, improve it
  - "What's the difference between silicone render and monocouche?" — already ranking, expand
  - "How long does external rendering take on a Sheffield semi?" — process + timeline, very AI-citeable
  - "What is EWI and does it need planning permission?" — FAQ already exists, turn into full post
  - Format for each: 800–1200 words, H2 structure, capsule answers, HowTo or FAQ schema

- [ ] **2.4 — Add `Review` quotes to suburb pages**
  - Each suburb page: add 1–2 real customer review quotes with the suburb mentioned
  - Add `Review` schema with `author`, `datePublished`, `reviewBody`, `reviewRating`
  - *Why: Reviews with location keywords = local AI citation signal*

- [ ] **2.5 — Add `Article` schema to all blog posts**
  - Include: `author`, `datePublished`, `dateModified`, `headline`, `description`
  - Author should link to the About page person entity

---

### PHASE 3 — Authority Building (Ongoing)
*Target: months 2–3+*

- [ ] **3.1 — Build external citations (local press, supplier links)**
  - Contact Sheffield local news (The Star) about cost-of-living / insulation grants stories
  - Reach out to render suppliers (Weber, K-Rend) about being listed as approved applicator
  - Get listed on Sheffield City Council or South Yorkshire green homes grant pages (EWI)
  - *Why: AI engines weight earned external links above self-published content*

- [ ] **3.2 — Google review velocity strategy**
  - Text customers after job completion with a review link
  - Target 5+ new reviews per month (consistency > bursts)
  - Respond to all reviews (response rate is tracked by GBP algorithm)
  - Keywords to encourage in reviews: "Sheffield", service name (e.g. "silicone render"), suburb name

- [ ] **3.3 — Photo strategy for GBP and site**
  - Before/after photos for each service type (render, EWI, plastering, Venetian plaster)
  - Tag photos with location when uploading to GBP
  - Businesses with 100+ photos get 520% more calls and 1,065% more website clicks

- [ ] **3.4 — Sitemap with `lastmod` dates**
  - Ensure sitemap.xml has `<lastmod>` dates on all pages
  - Update `lastmod` whenever a page is edited (signals freshness to crawlers)
  - Resubmit to both Google Search Console and Bing after any batch update

---

## Schema Quick Reference — Types Already in Use

| Schema Type | Pages | Notes |
|---|---|---|
| LocalBusiness | All | Good — check `priceRange`, `areaServed` filled |
| Service | All | Good |
| FAQPage | 41 | Good — add Speakable to top answers |
| HowTo | 41 | Good |
| AggregateRating | 50 | Good — 5.0, 100 reviews |
| BreadcrumbList | 41 | Good |
| GeoCoordinates | 49 | Good |

## Schema to Add

| Schema Type | Priority | Pages |
|---|---|---|
| `Speakable` | HIGH | index.html, faq.html, blog posts |
| `Article` | HIGH | blog posts |
| `Person` | MEDIUM | new about.html |
| `Review` (individual) | MEDIUM | suburb pages |
| `ImageObject` (expand) | LOW | all pages |

---

## Tracking Log

| Date | Action | Result |
|---|---|---|
| 18 Jul 2026 | **.com RECLAIMED + redirecting (REVERSES 20 Jun "let it delete" decision)** | Ghost .com found STILL on Google page 1 for "rendering sheffield" 3 months after expiry — competing with .co.uk for its own money keyword. Verisign showed domain fully dropped = fresh-registerable. Owner bought it via Vercel Domains ($11.25/yr, renews same — NOT 123-Reg's £80 recovery fee) into the same team as the site project. Both apex + www attached to plaster-rendering-site; vercel.json host-based 301s live and verified: /about-us→/about, /plastering-services→/plastering-sheffield, /applying-render→/how-we-apply, /services→/, catch-all path-preserve, explicit "/" rule (GOTCHA: Vercel `/:path*` catch-all does NOT match root "/" — needs its own rule). All single-hop. KEEP RENEWING ~£9/yr as redirect+squatter insurance. Owner must click ICANN verification email (Vercel account inbox) or domain suspends in ~15 days. Optional next: verify .com in GSC (DNS TXT via Vercel) + Change of Address tool to speed equity transfer. |
| 23 Jun 2026 | **Full-site ranking audit + fixes** | Hard-data audit of all 62 pages (titles, meta, H1, schema, canonicals, internal-link graph, orphans, sitemap, capsules, alt). Site already very clean: 0 broken links, 0 invalid JSON-LD (118 blocks), 1 H1/page, no dup titles/metas, GA4 everywhere. **FIXED: (1)** S17 EWI case study was `noindex,nofollow` despite being sitemapped + homepage-featured &rarr; set `index,follow` (unlocked a whole case study). **(2)** Added AEO "Quick Answer" capsules + Speakable schema to the 2 indexable pages missing them: `sand-cement-render-sheffield` + `silicone-render-vs-monocouche` (capsule matches page verdict: monocouche = best value for most). **(3)** Internal-link equity: added "About Us" to footer of 48 pages (about inbound **1&rarr;50**, fixes E-E-A-T starvation); added "Sand &amp; Cement Render" to footer services on 45 pages (inbound **3&rarr;46**); added plastering-cost-guide link on pricing.html (inbound 2&rarr;3). **(4)** Trimmed 2 truncating metas (about 170&rarr;~150c, ewi 164&rarr;~154c). All re-validated: 0 broken links, all JSON-LD valid, no mojibake. |
| 23 Jun 2026 | **Website&rarr;GBP entity linking (index.html)** | Strengthened the site&harr;Google Business Profile connection. (1) `hasOfferCatalog` rebuilt from a flat 5-item text list &rarr; **7 Services, each with `url` + `serviceType` + provider `@id`** linking to its dedicated page (silicone/monocouche/EWI/sand-cement/render-repair/internal-plastering/dry-lining); silicone now names K-Rend/Eco-Rend/Weber. (2) **Embedded GBP Google Map** iframe in the reviews section (crawlable site&rarr;GBP signal). (3) **One-tap "Leave a review" button** added next to the map using the real GBP review link `https://g.page/r/Cbo-hCRK6i41EBM/review` (from GBP &rarr; Get more reviews). All 6 JSON-LD blocks validated. Confirmed GBP NAP (3 Rocher Cl, Grenoside, S35 8QP / 07595 399525 / closes 8pm) matches site schema exactly. |
| 10 Jun 2026 | Baseline audit | 13 Bing impressions, 2 Copilot citations (3M Bing data) |
| 10 Jun 2026 | Generated IndexNow key `ea3ba62784952703fc4172e2c2474908` | Key file live at root, pushed to GitHub |
| 10 Jun 2026 | Submitted all 57 URLs to IndexNow API (`api.indexnow.org`) | HTTP 202 — accepted by Bing/Yandex |
| 10 Jun 2026 | Added `.co.uk` property to Bing Webmaster Tools | Verified via `BingSiteAuth.xml`, pushed to GitHub |
| 10 Jun 2026 | Submitted sitemap to Bing Webmaster Tools (.co.uk property) | Accepted — data populates within 48 hours |
| 10 Jun 2026 | GBP audit completed | Categories updated (added Building contractor), description approved — suburb names, warranty, Chris name, approved applicator status |
| 10 Jun 2026 | Added Speakable schema to index.html and faq.html | Targets H1, hero intro, FAQ questions and answers |
| 10 Jun 2026 | Backlink audit completed | Yell listed (correct name, website linked ✅), Checkatrade profile confirmed ✅, K-Rend/Ecorend have no installer directory pages, INCA not a current member |
| 10 Jun 2026 | INCA membership claims removed | Removed INCA logo from index.html, removed all INCA membership text from index.html and ewi-sheffield.html — replaced with CHAS/Ecorend/K-Rend references |
| 10 Jun 2026 | `.com` domain investigation | Domain expired Apr 2026, now taken by third party. Cannot redirect. Google will naturally de-index old pages. No action needed. |
| 20 Jun 2026 | `.com` re-checked — EARLIER NOTE WAS WRONG | WHOIS: expired 26 Apr 2026, registrar 123-Reg, NO live site (DNS does not resolve). NOT taken by a third party — just unclaimed. Old `.com` pages still appear as stale ghosts in Google. **Likely still recoverable in redemption window (~until late July 2026).** ACTION: log into 123-Reg, renew it, then 301-redirect every `.com` page → matching `.co.uk` page (recovers link equity + kills duplicate). Fallback if not recovered: GSC Removals tool on the `.com` property + let DNS-dead pages de-index naturally. |
| 20 Jun 2026 | `.com` DECISION — let it delete | Owner chose NOT to recover the `.com`. Leave it to expire/delete. Domain is DNS-dead so Google will drop the stale ghost pages naturally over the coming weeks. **No further action on the .com — do not revisit.** |
| 20 Jun 2026 | About page deployed LIVE | `/about` pushed to main, Vercel live (HTTP 200). Required adding an explicit `/about → /about.html` rewrite to vercel.json (site has no catch-all clean-URL rule — every new page needs its own rewrite entry or it 404s). Photo, K-Rend/Ecorend/CHAS logos all verified serving. |
| 20 Jun 2026 | About page photo added | Chris Glover photo (from his Desktop IMG_0913) optimised to `images/chris-glover.webp` (Pillow, 750x1000, ~110KB) — repo ignores jpg/png, webp only. Added to Person schema `image`. |
| 20 Jun 2026 | **AEO — Answer-First Capsules rolled out (9 pages LIVE)** | Added a "Quick Answer" capsule (40–60 word direct answer, marked `speakable`) to the top of: plastering-cost, rendering-cost, silicone-render, monocouche-render, ewi, plastering, dry-lining, render-repair, **homepage**. This is the format Google AI Overviews extract (~55% of AI citations come from top 30% of a page). Reusable block: `.answer-capsule` div w/ inline styles + green left-border. Facts/prices pulled from each page's own data (no invented numbers). **GOTCHA for batch edits:** must use HTML entities (&#163; &#8211; &#178; &#39;) NOT literal UTF-8 chars — perl byte-mode double-encodes literal UTF-8 into mojibake. Verified zero mojibake on all 9. |
| 20 Jun 2026 | `.com` DECISION confirmed | Owner: do NOT recover, let it delete. No action. |
| 21 Jun 2026 | **Suburb capsules DONE — 40 pages** | Localised answer-first capsule added to all 40 suburb/area pages ("Looking for a plasterer or renderer in {Suburb}? …covers {Suburb} ({postcode})…"). Names derived from filename (titlecase) — postcode from page eyebrow. Byte-safe perl (entities only), zero mojibake, all schema valid. Anchor was `<section id="services-sect">` (suburb template differs from service pages — no `About Our Service` eyebrow, no speakable block). **Total AEO capsule coverage now 49 pages.** |
| 21 Jun 2026 | **BUG FIXED — two public pages were 404ing** | `plastering-cost-sheffield` and `silicone-render-vs-monocouche` had NO rewrite in vercel.json (pre-existing) — both in sitemap + internally linked but dead live. Added rewrites; both now HTTP 200. Lesson reinforced: every page needs its own vercel.json rewrite. |
| 21 Jun 2026 | **BUG FIXED — wrong suburb name in headings** | parson-cross, wadsley, wincobank pages had leftover "Southey" in their "All Services in / Rendering & Plastering in / Get a Free Survey in" headings (template duplication). Corrected to the right suburb. Legit nearby-area cross-links + areaServed schema entries left intact. |
| 21 Jun 2026 | Owner confirmed GSC "Request Indexing" done for /about | ✅ |
| 21 Jun 2026 | **Full-site audit — every page checked** | Live HTTP sweep: all pages HTTP 200 (zero 404s). No duplicate titles/meta, no broken internal links, all canonicals correct, 1 H1/page, sitemap clean, all JSON-LD valid. FIXED: (1) `plastering-cost-sheffield` referenced nonexistent `plastering-service.webp` for hero+og+twitter → repointed to `plasteringhero.webp`; (2) About meta desc 217→160 chars. |
| 21 Jun 2026 | **Speakable added to all 40 suburb pages** | Injected `SpeakableSpecification` (.answer-capsule, h1, h2) into each suburb WebPage node (they had none). Schema valid, zero mojibake. |
| 21 Jun 2026 | **5 meta descriptions trimmed** | index, plastering-cost, plastering-sheffield, silicone-render, silicone-render-vs-monocouche trimmed from 167–176 to 149–159 chars (were truncating in SERPs). ASCII-only edits. |
| 21 Jun 2026 | ⚠️ REMINDER (hit the bug AGAIN) | Trimming About meta, used perl `\x{2014}` (em-dash codepoint) in byte mode → re-corrupted about.html. Reverted from git, redid with `&#8212;`. **RULE: in perl/sed batch edits NEVER use literal UTF-8 or `\x{}` wide chars — use HTML entities only (&#8212; em, &#8211; en, &#163; £, &#178; ², &#39; ').** The Edit tool handles UTF-8 fine; only perl/sed byte-mode is the trap. |
| 21 Jun 2026 | Deep AI/SEO gap research + 2 of 4 gaps shipped | Researched 2026 AI/SEO (llms.txt, AI-crawler robots.txt, underused schema). VERDICT: site already top-tier. **Skip llms.txt** — Google confirmed (Jun 2026) zero ranking benefit. SHIPPED: `knowsAbout` added to 5 Organization nodes; `dateModified: 2026-06-21` added to 43 WebPage nodes (freshness). robots.txt allow-all = correct (we WANT AI crawlers). |
| | **BLOCKED — needs owner input (do NOT fabricate):** (1) **VideoObject schema** for how-we-apply YouTube clip (o4SN4Qq7v9g) + local MOV — need real uploadDate + duration (YouTube scrape failed; ask owner or YouTube Studio). (2) **Review schema on 40 suburb + 2 cost pages** — must use REAL Google reviews (7 service pages already have real ones e.g. "Edward Watchorn"). Do NOT invent fake reviews/authors (Google policy + integrity). Ask owner to paste 3–5 real reviews, ideally mentioning an area. |
| 21 Jun 2026 | **Mobile performance — responsive heroes** | PageSpeed mobile homepage was 69 (LCP 5.4s) — cause: hero images served full-size (400–490KB) to phones. Fixed homepage hero → **69→75, LCP 5.4s→4.5s**. Then batched 30 suburb pages: generated 900px `-m.webp` variants (Pillow, q78) for heavy heroes (>150KB), wrapped in `<picture>` + responsive preload + width/height. Service pages were already responsive; small heroes (<150KB) left alone. METHOD: did it in Python (writes UTF-8 natively — no perl mojibake risk). CLS already 0, TBT green — only loading was weak. |
| | **PERF — remaining bottleneck:** FCP ~3.3s (render-blocking) now gates LCP, not the image. Next perf lever = font/render-blocking optimisation (affects all pages incl homepage). Heavier work, diminishing returns — optional. |
| 21 Jun 2026 | **FAQ "rewrite" done (capsule emphasis)** | Audited all 28 FAQ answers — already excellent answer-first shape (40–75w leads). So did NOT rewrite good copy; instead bolded the lead direct-answer sentence of each (scannable capsule + emphasis signal). Speakable already targets `.faq-body p`. 28/28 done, schema valid. |
| 22 Jun 2026 | **2nd case study LIVE — S17 EWI** | Built `/s17-ewi-case-study` from case-study-template using owner's real job photos (45 converted JPEG→webp via Pillow w/ EXIF-transpose; curated to 11 + hero -m). Full EWI: 150mm EPS + silicone, S17 near Millhouses, 3 weeks. 5-stage carousel, HowTo+FAQ+WebPage schema, capsule, responsive hero. Review handled HONESTLY — states the real 5★ Yell review, NO fabricated quote/author (removed Review JSON-LD). Routed, sitemap, linked from projects + ewi-sheffield. GOTCHA: template schema reuses space-tokens (STAGE 1 TITLE) + FAQ_ANSWER in both HTML & JSON — first build broke FAQ JSON with `[^<]*`; fixed with `[^<"]*` + handling space-tokens separately. Built in Python (UTF-8 safe). |
| 22 Jun 2026 | S17 EWI case study — corrections | Fixed wrong-captioned base-board image (reordered to correct EWI sequence: Before→Damp-Proof Base→Insulation→Detailing→Finished); added Andy B.'s real 5★ Yell review (04 Nov 2024, verbatim) + Review schema; hero image opacity .6→.9 + lighter overlays; featured on homepage (2nd featured case study). NOTE: Andy's review says 'fortnight' but stated duration is 3 weeks — confirm with owner. |
| 22 Jun 2026 | Case study heroes + discoverability | Brightened both case study heroes (opacity .6/.9→.92, overlays fade to clear by ~50%, dark tinge only at bottom) + fixed case-study-template default. Audited ALL heroes site-wide: only the 3 cost/comparison pages are very dark (0.13) but that's an intentional faint-bg text-hero design — left as-is. Added a featured 'Case Studies' two-card section at top of /projects (both Sandygate + S17 EWI); homepage nav 'Case Study'→'Case Studies'/projects; both studies featured on homepage. EWI study now reachable from every Case Studies/More Projects link. |
| 22 Jun 2026 | S17 EWI case study — current state + PENDING (new chat handoff) | **DONE & LIVE:** /s17-ewi-case-study with correct stage order (Before→Damp-Proof Base→Insulation→Detailing→Finished→**Stage 06 Flue Extension/BBA**), Andy B. real 5★ Yell review + schema, brightened heroes (.92 + tinge-at-bottom overlays), featured on homepage + /projects. Hero = millhouses-ewi-hero.webp (IMG_4033). Diversified reused images (after-16 was 12x). Flue stage uses millhouses-ewi-flue.webp (IMG_4022). **Converted source photos:** `~/Desktop/before ` + `~/Desktop/after ` (NOTE trailing space in folder names!). Converted webp kept in images/case-studies/millhouses-ewi-*. **PENDING (owner flagged mistakes, starting new chat):** owner wants (1) the Before/After section to show the DOOR (before vs after) and (2) hero swapped to "the other" finished shot. DO NOT GUESS image placement — ask owner for the exact IMG filenames for each slot first. Current: hero=IMG_4033, before/after-before=before-01, before/after-after=after-20. Also unconfirmed: Andy review says "fortnight" vs stated 3 weeks. CTA bg (after-26) is a darkish side-passage shot — may want a brighter finished shot there too. |
| 22 Jun 2026 | **S17 EWI — pending items resolved + LIVE (commit 1a482fc)** | Cleared the prior handoff's PENDING list. (1) **Before/After section now shows the DOOR** — owner-confirmed pair: before `millhouses-ewi-door-before.webp` (IMG_2076, grey door in bare brick) → after `millhouses-ewi-door-after.webp` (IMG_4026, same door + cream render + grey window). New webp files (Pillow EXIF-transpose, 900px/1200px). The old before-01/after-20 still used in the STAGE carousel + JSON-LD — left intact; only the comparison slider (lines ~1171/1178) repointed. (2) **Duration corrected 3 weeks → 2 weeks** everywhere: schema `totalTime` now valid ISO `P2W`, both stat badges, FAQ+HowTo prose ("around two weeks"). Andy B.'s "fortnight" review now consistent, left verbatim. (3) **Hero NOT swapped** — owner reviewed all 45 source photos with me, briefly chose IMG_4028 then decided to KEEP original IMG_4033 hero at opacity:.92. (4) **CTA bg left as-is** — owner aware after-26 is a darkish side-passage shot but chose not to change it. NOTE: the "two render colours" worry is a non-issue — it's ONE house; warm off-white render just photographs olive-green in overcast light (grey windows/plinth + gable/wall/solar consistent across all shots). All 5 JSON-LD blocks valid, zero mojibake, all 4 referenced webp exist. Pushed to main → Vercel. |
| | **RESUME NEXT:** (a) more case studies (template proven; ask owner for job photos+facts) — blog posts NOT worth it (see 2026 research); (b) Review schema needs real review text from owner; (c) off-site citations/reviews = #1 lever. — silicone-render-cost-Sheffield first (capsule format, FAQ/HowTo schema, link to /silicone-render-sheffield + /rendering-cost-sheffield). (b) Pending owner data: VideoObject (YouTube upload date/duration), Review schema on suburb pages (real Google reviews only — never fabricate). (c) Optional: homepage trust-badge bar. Off-site citations/reviews remain the #1 ranking lever. Also offered, not yet built: homepage trust-badge bar (manufacturer + CHAS logos up front, mirrors MAC/EDC). Owner has resubmitted sitemap + requested indexing for /about. Site is fully clean as of 21 Jun (no 404s, no broken links/images, no dup/missing metadata, 49 AEO capsules live, 40 suburb pages have Speakable). All capsule prices accurate as of 20–21 Jun. |
| 10 Jun 2026 | GBP service areas expanded | Added 11 new areas. Pending Google approval. |
| 11 Jun 2026 | GBP service area rejections | 10 of 11 new areas NOT APPROVED: Rotherham, Loxley, Walkley, Ecclesfield, Nether Edge, High Green, Crookes, Hillsborough, Stocksbridge, Stannington. Approved areas: Sheffield, South Yorkshire, Dore, Grenoside, Bradway, Chapeltown, Fulwood, Crosspool, Totley Brook. Fix: remove rejected, re-add 2/week in simple format (no postcodes). Leave Rotherham out. |
| 11 Jun 2026 | K-Rend applicator programme | No public finder directory — requires £75+VAT training course. Email route not viable. Focus on Weber instead. |
| 11 Jun 2026 | GBP "12 weeks ago" flag | FIXED — edited business info field, timestamp reset. |
| 11 Jun 2026 | GBP duplicate listing removed | "Plaster solutions limted" duplicate (years old, same address) removed via business.google.com. Was splitting authority. Now 1 business, 100% verified. |
| 11 Jun 2026 | GBP booking link added | Added https://www.plasterandrenderingsolutions.co.uk/get-quote as booking URL |
| 11 Jun 2026 | GBP photos updated | New photos added — last upload had been 62 days ago. "Get noticed" prompt cleared. |
| 11 Jun 2026 | GBP Instagram confirmed | Already connected ✅ |
| 12 Jun 2026 | GBP Performance snapshot | 3,079 profile views, 338 searches showed profile. Top search terms: "plaster" (116), "plasterers sheffield" (114), "rendering" (65), "plasterer sheffield" (43), "artistic wall plastering sheffield" (<15). Platform: 89% Google Search (66% mobile), 10% Maps. Notable: "artistic wall plastering sheffield" appearing in top 5 unprompted — niche demand worth targeting with content. |
| 12 Jun 2026 | GBP service area — CLOSED | Ecclesfield + High Green rejected again ("Your edit was not approved"). Google won't approve suburbs that fall within the already-approved "Sheffield, UK" / "South Yorkshire, UK" broad areas — treats them as redundant. Stop attempting further additions. Suburb coverage is better served by the website location pages. Current 9 approved areas are sufficient. |
| 12 Jun 2026 | GA4 set up and deployed | Created GA4 property (G-1DSC8GHLQ0), added tracking snippet to all 62 pages, tag verified live. Search Console linked to GA4 — keyword + traffic data will flow within 48hrs. GBP↔GA4 link no longer exists in GA4 product links (Google removed it). |
| | **Next:** Phase 2 content work (FAQ rewrite, blog posts). | |
| 10 Jun 2026 | GBP services confirmed | All key services already listed: Monocouche rendering, Silicone render, EWI, Plastering, Dry Lining, Cement Rendering, Internal Walls plastering, Ceiling skimming ✅ |
| 10 Jun 2026 | GBP Q&A not available | Q&A section not showing on profile — Google has restricted it for this business type. Drafted Q&A content saved below for future use if it becomes available. |
| 12 Jun 2026 | Google Search Console — "Page with redirect" fully resolved | Validation started 4 Apr 2026, passed 6 Jun 2026. 0 affected pages remaining (peaked at ~5 in April). All redirect-blocked pages are now clean and indexable. |
| 12 Jun 2026 | Google Search Console — Page indexing audit | 55 indexed ✅, 7 not indexed. Active issues: (1) **Redirect error** — 2 pages (`/portfolio/`, `/faq/`), last crawled Apr 25; (2) **Crawled - currently not indexed** — 5 pages, Google's choice (thin/duplicate content). |
| 12 Jun 2026 | Redirect error investigation | `/portfolio/` and `/faq/` redirect chains are correct in vercel.json (both destination files exist). Stale issue — Google last crawled Apr 25 before fixes were in place. Fix: click "Validate Fix" in GSC → Page indexing → Redirect error. No code change needed. |
| | **Next:** Click "Validate Fix" in GSC for Redirect error. TrustATrader free listing. Phase 2 content work (FAQ rewrite, blog posts). | |

---

## GBP Q&A Drafts (add if Q&A becomes available)

**Q: Do you install silicone render in Sheffield?**
> Yes — silicone render is our most popular external finish across Sheffield. We install silicone render systems across all S postcodes, from detached homes in Fulwood and Dore to terraces in Hillsborough and Chapeltown. We're approved applicators for K-Rend and Ecorend silicone systems, both carrying a 25-year manufacturer warranty. Colours matched to any RAL or BS shade. Free site survey with no deposit required — call 07595 399525.

**Q: Do you install monocouche render in Sheffield?**
> Yes — we apply monocouche render across Sheffield and South Yorkshire. Monocouche is a single-coat through-coloured render popular on older Sheffield properties in S10, S11, S17, and conservation areas including Nether Edge and Broomhill. We use K-Rend and Ecorend monocouche systems with a 25-year warranty. Ideal for properties where planning requires a traditional stone-textured finish. Free survey, no deposit — call 07595 399525.

**Q: Do you install External Wall Insulation (EWI) in Sheffield?**
> Yes — we install full EWI systems across Sheffield, including silicone render and monocouche finish coats. EWI typically improves EPC ratings by two full bands and saves £300–£600 per year on heating. We're approved applicators for Ecorend and K-Rend EWI systems and can advise on ECO4 and Great British Insulation Scheme grants. CHAS accredited, 100+ five-star Google reviews. Free survey — call 07595 399525.

**Q: What areas of Sheffield do you cover for plastering and rendering?**
> We cover every Sheffield postcode from S1 to S36, including Crookes, Walkley, Hillsborough, Chapeltown, Ecclesfield, Grenoside, Dore, Fulwood, Crosspool, Nether Edge, Broomhill, Sharrow, Meersbrook, Woodseats, Stannington, Stocksbridge, and all surrounding areas. We also cover Rotherham and wider South Yorkshire. Same-day site visits available — call 07595 399525 or visit plasterandrenderingsolutions.co.uk.

---

## Resources

- [Google I/O 2025 — AI Search Impact (Dock.co.uk)](https://dock.co.uk/blog/google-io-2025-how-ai-is-reshaping-search-visibility-and-seo-strategy)
- [How AI Mode Impacts Local SEO (Search Engine Journal)](https://www.searchenginejournal.com/how-will-ai-mode-impact-local-seo/561002/)
- [Google I/O 2025 + GBP Features (BrightLocal)](https://www.brightlocal.com/blog/google-io-2025/)
- [GEO Complete Playbook 2025 (SEOTuners)](https://seotuners.com/blog/seo/generative-engine-optimization-geo-in-2025-the-complete-playbook-to-win-ai-overviews-chatgpt-copilot-perplexity/)
- [Schema Markup for AI Search (WordStream)](https://www.wordstream.com/blog/schema-markup-for-ai)
- [How to Rank in AI Overviews — Local (GrowthProAI)](https://growthproai.com/blog/rank-google-ai-overviews-guide-2025)
- [GEO for Bing Copilot (SEOTuners)](https://seotuners.com/blog/seo/blog-geo-for-bing-copilot/)
- [Bing Copilot Citation Guide (Lawrence Hitches)](https://www.lawrencehitches.com/copilot-search-optimization/)
