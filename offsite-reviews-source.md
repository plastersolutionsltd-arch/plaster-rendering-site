# Off-Google reviews — source of truth

Reviews of P&R Solutions on platforms other than Google. The Google corpus is separate, in
`reviews-source.md`, and is the only thing the 109 count and the site's `aggregateRating` describe.

## Yell

Pasted by Chris on 2026-08-23 from the Yell profile
(`yell.com/biz/plaster-solutions-limited-sheffield-7579451`). Yell returns 403 to automated
fetches, so this file can only be topped up by hand.

**These are NOT Google reviews and must never be counted in the Google total.** The site's
`aggregateRating` is Google-only (109, 5.0) and is maintained by `sync-reviews.py`.

## Rules for using these — read before publishing any of them

1. **Display only. Never add a Yell review to JSON-LD.** Google's review-snippet guidance says
   *“Don't aggregate reviews or ratings from other websites”*, so third-party reviews marked up on
   your own site are ineligible for review snippets. They still earn their place as visible page
   content — AI Overviews read the page, not just the schema.
2. **Label the source on the card** (“Verified Yell review” + the yellow Y badge, not the blue
   Google G). Presenting a Yell review as a Google one is a misattribution.
3. **Verbatim, always** — including the typos (“qualty”, “resonable”, “differant”, “couteous”,
   “competative”). Never tidy them. Same rule as the Google corpus.
4. **Use the Yell handle as the name.** It is what a reader can verify on Yell, and it avoids the
   “initials” style that gave away the three fabricated dry-lining testimonials.
5. Kept off the public site by the `*.md` rule in `.vercelignore`.

| Handle | Date | Title | Service | Text | Status |
|---|---|---|---|---|---|
| AndyB-3248 | 2024-11-04 | Excellent friendly high qualty work | EWI + render | Chris has done a superb job of our external insulation and rendering. He works diligently to make sure that the job is finished to a high standard and in the shortest time. He is there when he says he will be and makes sure there isn't a mess. He doesn't "cut corners" and the finished work looks stunning. It has been a joy to have him around for the fortnight. | LIVE: /ewi-sheffield, /rendering-sheffield, /s17-ewi-case-study |
| JayneP-159 | 2022-05-29 | Plaster Solutions Limited | rendering + plastering | Had a full outside rendering of the house and plastering inside porch. A superb job was done all round. Chris's attention to detail was first class. He was punctual, clean and tidy, helpful and very friendly. I can definitely recommend Plaster Solutions Ltd. A great price and a definite 10/10.Cheers Chris. / Tony and Jayne |  |
| NeilF-296 | 2021-03-14 | Nice work left clean and tidy | plastering | Just had Chris to plaster the walls and ceiling in our spare bedroom and we are so impressed with the finish had plastering done in other rooms by differant plasteres over time but none as good as the work carried out by Chris and there's no mess not even a foot print on the stairs nice work clean and tidy Thank you | Same text as the TRUNCATED Google row 'Penny Furniss, 15 Mar 2021' - see note below |
| PaulB-3338 | 2019-10-06 | Garage rendering | rendering (garage) | I have no hesitation in recommending Plaster Solutions. The workmanship is excellent and the costs are very resonable. Chris is couteous and very reliable and works very hard to ensure that the work is completed on time and that all mess is cleaned up before he leaves site. |  |
| LisaG-258 | 2019-01-15 | Excellent workmanship | general | Fabulous work by plaster solutions and a very professional business ...Chris and the team came to my house , viewed , quoted and carried out the work to a very high spec ! Will deffo use again ! Thankyou |  |
| VijayaG | 2016-09-28 | rendered a external wall along driveway | rendering (wall) | Chris did a great job rendering the wall along my driveway.Unfortunately just as he finished work & was about to leave there was sudden heavy rain fall (earlier on it was a warm sunny day). Due to heavy rain all the work done was a complete washout. By the time rain settled it was late evening & dark with not much light and it was such a mess with cement everywhere.Chris was exhausted after busy long day & he had season tickets to take his lads to football match that evening.I asked him to return back next day but he said NO it cannot be allowed to dry in that condition & had to be finished then & there.He cancelled his plans to go to football match, stayed back & re-rendered the wall again using light from the car headlights.It was 9.30 pm by the time he could finish. He has done such an amazing job & is a thorough professional.I was left speechless with the effort he has put in.All my neighbours have complimented that the wall looks great! I would definitely recommend Chris. | Strongest story in the whole corpus |
| Piff | 2015-09-23 | Rendered house | rendering | Had Chris and team to re render the house The job was completed on time and very happy with the finished product definitely would recommend |  |
| Daddycool13 | 2013-07-04 | Insulated render | EWI | I contacted Chris to give me quote for insulated render job at my 2 storey 1930's house. There price was very competative. When they came to do the work Chris and gang were very polite and helpfull. They left a top notch job and would definitely recommend. |  |
| jay1985 | 2013-06-20 | rendered gable on house | rendering (gable) | really great job, very clean and tidy, would strongly recommend this company. / would use again thanks. |  |
| steve1313 | 2013-05-23 | rendered garden wall | rendering (wall) | a good job well done,prompt and ensured we were well informed at all times, would recommend to any one |  |

## What this corpus does and does not give us

- **No place names at all.** Not one of the ten names a suburb, so none of them can populate a
  suburb page. The Google corpus had six; this adds zero. The ask is still the only lever.
- **No product names.** Still nothing saying “monocouche”, “silicone” or a brand. “Insulated
  render” (Daddycool13) is the closest.
- **They are old.** Seven of the ten predate 2020 and four are from 2013–16. Fine as depth on a
  service page, weak as headline social proof next to 2026 Google reviews.
- **One genuinely completes a truncated Google row.** `NeilF-296` (14 Mar 2021) is word-for-word
  the review the Google panel truncates as *“Penny Furniss, 15 Mar 2021 — Just had Chris to plaster
  the walls and ceiling in our spare bedroom and we are so impressed with the finish had…”*.
  Same household posting on both platforms one day apart is the obvious reading, but **do not
  merge the two records or publish the Yell text under Penny Furniss's name** — that would be
  attributing words to a person we cannot prove wrote them. Publish it as NeilF-296, from Yell.


---

## Checkatrade

Pasted by Chris on 2026-08-23 from `checkatrade.com/trades/plasterandrenderingsolutionslimited/reviews`.
Checkatrade also returns 403 to automated fetches — hand top-up only.

**Why these are the most useful reviews we hold:** Checkatrade attaches a **job location** to every
review itself, so it does not depend on the customer thinking to name their area. These are the only
two reviews in any corpus with a location we did not have to supply. Both score **10/10**.

Checkatrade displays **no reviewer name** — the job location is the whole attribution. Do not invent
a name or initials for these cards; cite the source and the postcode district, which is what the
platform itself shows.

**Both jobs are in Barnsley, not Sheffield.** S70 is Barnsley town; S73 is Wombwell / Darfield /
Brampton. The site has no Barnsley page — `areaServed` claims Barnsley but nothing serves it.

| Score | Date posted | Title | Job location | Text |
|---|---|---|---|---|
| 10 | 10 April (year not shown by Checkatrade — confirm before publishing a year) | Excellent work | S73 (Wombwell / Darfield, Barnsley) | I recently hired plastering and rendering solutions limited for a plastering job in my home, and I couldn't be happier with the results. From the start, they were professional and communicative, providing a clear and detailed quote. The quality of their work is outstanding &ndash; smooth, even walls and ceilings that look fantastic. They were also respectful of my property, keeping the work area clean and tidy throughout the project. I highly recommend plastering and rendering solutions limited to anyone looking for a reliable and skilled plasterer. |
| 10 | 08 April (year not shown — confirm) | Rendering | S70 (Barnsley town) | Chris came to our home and provided a first class service rendering the front of our home . Clean , tidy and friendly , cannot recommend highly enough and will request his service when we want the back of our house rendering ! thank you !!! 5 star !!! |

**Same display-only rule as Yell** — these must never go in JSON-LD. Google: *"Don't aggregate
reviews or ratings from other websites."*

**Note on the first one:** it names the business in full twice, which is unusual phrasing for a
customer and reads stiffly. Checkatrade verifies reviews against the actual job, so this is a
style observation, not a traceability doubt. Publish verbatim or not at all.

**LIVE:** S73 plastering review &rarr; /plastering-sheffield. S70 rendering review &rarr; /rendering-sheffield.
