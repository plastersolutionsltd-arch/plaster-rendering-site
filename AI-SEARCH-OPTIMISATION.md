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

- [ ] **1.1 — GBP audit and complete to 100%**
  - Fill every field: services with descriptions, categories (primary + secondary), business description using keywords, Q&A section, opening hours, service area
  - Add 10+ photos of real jobs (before/after renders, EWI installs)
  - Post at least 1 Google update per week going forward
  - Add all services as individual GBP service entries with descriptions
  - *Why: Businesses with 100% complete GBP are 3.2x more likely in AI Overviews*

- [x] **1.2 — Submit all 57 pages to Bing IndexNow** ✅ Done 10 Jun 2026
  - IndexNow key deployed, all 57 URLs submitted via API (HTTP 202)
  - `.co.uk` property added and verified in Bing Webmaster Tools
  - Sitemap submitted — full index expected within 48–72 hours

- [ ] **1.3 — Add `Speakable` schema to homepage and FAQ page**
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

### PHASE 2 — Content That AI Will Cite (Medium Term)
*Target: weeks 3–6*

- [ ] **2.1 — Create an About / Who We Are page**
  - Name of founder/director, years in trade, qualifications, areas served
  - Photo of the team (real people = E-E-A-T)
  - Professional memberships (Checkatrade, TrustMark etc.)
  - Add `Person` schema with `knowsAbout` properties
  - *Why: AI engines prefer identifiable experts over anonymous brands*

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
| 10 Jun 2026 | Baseline audit | 13 Bing impressions, 2 Copilot citations (3M Bing data) |
| 10 Jun 2026 | Generated IndexNow key `ea3ba62784952703fc4172e2c2474908` | Key file live at root, pushed to GitHub |
| 10 Jun 2026 | Submitted all 57 URLs to IndexNow API (`api.indexnow.org`) | HTTP 202 — accepted by Bing/Yandex |
| 10 Jun 2026 | Added `.co.uk` property to Bing Webmaster Tools | Verified via `BingSiteAuth.xml`, pushed to GitHub |
| 10 Jun 2026 | Submitted sitemap to Bing Webmaster Tools (.co.uk property) | Accepted — data populates within 48 hours |
| | Next: Phase 1.1 — GBP audit | |

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
