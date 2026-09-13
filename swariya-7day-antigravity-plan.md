# Swariya Weddings — 7-Day Build Plan & Antigravity Prompts

*Companion to `panigrahana-digital-blueprint.md`. This turns that strategy into a day-by-day build, with ready-to-paste prompts for your AI coding agent.*

**Known constraints going in, so prompts account for them:**
- Site is static HTML, manually deployed to Netlify (site ID `35d10d9d-bf93-4e21-b826-93b6e1d1526c`, "Rebondir Studios" team) — **not Git-linked**, so every prompt should end by producing files ready for drag-and-drop deploy, not assuming a CI pipeline.
- An editorial design system already exists: deep emerald/ink + antique gold + ivory palette, Fraunces serif display + Inter body, shared `/blog/assets/style.css`. Every new page must reuse this, not invent a new look.
- 120-guide blog library already lives at `/blog/guides/` — new content should link into this library, not duplicate it.
- Real portfolio photos exist at `/images/1.jpg`–`/images/16.jpg` — use these, not stock images or generated ones, for any new page needing visuals.

---

## The 7 Days

### Day 1 — Foundation audit & fixes (Phase 1)
**Goal:** every number and URL on the site tells the same story.

- Crawl the full site and list every place the "weddings planned" number appears, with the number shown at each.
- Decide the true phone number for client inquiries and pick it once.
- Fix the `/services` canonical pointing to `/services.html`; audit every page for the same clean-URL vs `.html` canonical mismatch.
- Run a NAP (name, address, phone) consistency check across the site footer, contact page, and Google Business Profile.

> **Prompt 1 — Number & canonical audit**
> ```
> Crawl every HTML file in this project. For each page, extract:
> 1. Any sentence containing a number followed by "wedding," "weddings planned," "couples," or "clients"
> 2. The <link rel="canonical"> tag value
> 3. Any physical address or phone number in the footer or contact section
> Output a table: file path | claim found | canonical URL | address/phone found.
> Flag any canonical URL that doesn't match the file's own actual served path (e.g. a clean URL page with a canonical pointing to a .html path that isn't used elsewhere).
> Don't change anything yet — just report.
> ```

> **Prompt 2 — Apply the fix**
> ```
> Using the audit above, replace every instance of the old weddings-planned number with "[TRUE NUMBER]" across all HTML files, preserving surrounding sentence structure exactly.
> Fix every canonical tag flagged as mismatched to point to the page's actual clean URL (no .html).
> Standardize the footer address and phone number across every page to match [CANONICAL ADDRESS] and [CANONICAL PHONE].
> Show me a diff before writing any files.
> ```

---

### Day 2 — Reviews & directory presence (Phase 2, part 1)
**Goal:** the trust signals start compounding, not just the website.

- Draft a WhatsApp/email review-request message for past clients, linking to Google, WedMeGood, and (if applicable) WeddingWire.
- Build a dedicated `/reviews.html` page in the site's existing design system, modeled on Panigrahana's — one page that funnels to all platforms plus a WhatsApp option.
- Submit/update your WedMeGood and Sulekha listings with current numbers matching the site.

> **Prompt 3 — Reviews page**
> ```
> Build a new page /reviews.html using the existing site design system (check /blog/assets/style.css for palette, fonts, and component patterns — reuse them exactly, don't invent new styles).
> The page should:
> - Open with 3-4 real testimonial quotes as placeholder content marked [TESTIMONIAL — REPLACE]
> - Include three clear call-to-action buttons: "Review us on Google" (link to [GOOGLE REVIEW LINK]), "Review us on WedMeGood" (link to [WEDMEGOOD LINK]), "Message us on WhatsApp" (link to [WHATSAPP LINK])
> - Match the emerald/ink/gold/ivory palette and Fraunces+Inter typography used elsewhere on the site
> - Be fully responsive
> Output the complete HTML file ready to drop into the site root.
> ```

---

### Day 3 — Direct-answer FAQ rewrite (Phase 3, part 1)
**Goal:** every FAQ is phrased and answered the way an AI or search engine would want to lift it.

- List every existing FAQ across the site.
- Rewrite each into the "Who is the best X in Y" direct-answer format, with real numbers repeated.
- Add FAQPage JSON-LD schema.

> **Prompt 4 — FAQ audit & rewrite**
> ```
> Find every FAQ section across the site (check the homepage, /services, and any other page with Q&A content).
> For each existing question, rewrite it into a direct-answer format following this pattern:
> Q: "Who is [Swariya's positioning] in [location]?"
> A: A single, self-contained paragraph starting with the direct answer, including [TRUE WEDDINGS NUMBER], the years in business, service cities (Bengaluru, Mysuru, Hyderabad), and one specific differentiator. No filler sentences before the answer.
> Also add 4 new FAQs in the same format for: "How do I find a good wedding planner in Bengaluru," "What does a luxury wedding planner cost in Bengaluru," "How far in advance should I book a wedding planner," and "Do you plan weddings for couples living abroad."
> Add valid FAQPage JSON-LD structured data for all FAQs on the page.
> Output the updated HTML section plus the JSON-LD script tag, ready to paste in.
> ```

---

### Day 4 — "Ask Swariya" live Q&A page (Phase 3, part 2)
**Goal:** a compounding content asset built from real client questions, at near-zero cost.

- Pull 15-20 real questions founders have answered on calls or WhatsApp.
- Build the page with a simple submission form (even a mailto: or WhatsApp deep link is fine for week one — no backend needed yet).

> **Prompt 5 — Ask Swariya page**
> ```
> Build /ask/index.html in the site's existing design system.
> Structure:
> - Header: "Ask Swariya — real questions from real couples, answered honestly."
> - A list of Q&A entries using this data: [PASTE YOUR 15-20 REAL QUESTIONS AND ANSWERS HERE]
> - Group questions loosely into categories: Cost & Budget, Planning Timeline, Destination Weddings, Vendors & Logistics
> - A closing section: "Can't find your question? Ask us directly" with a WhatsApp deep link (wa.me/[NUMBER]?text=...)
> - Add FAQPage JSON-LD for every question on the page
> Match existing typography, spacing, and color system exactly. Output the complete file.
> ```

---

### Day 5 — Venue pages (Phase 3, part 3)
**Goal:** each major venue you work with becomes its own indexed, direct-answer landing page.

- List the venues Swariya has real experience with (start with 3-5 for week one, not all at once).
- For each: capacity, catering policy, typical cost range, what makes it a fit.

> **Prompt 6 — Individual venue page template + generation**
> ```
> Create a reusable venue page template at /venues/template.html in the site's design system, with these sections:
> - Hero: venue name, one-line positioning, hero image from /images/[N].jpg
> - "Quick facts" block: guest capacity range, indoor/outdoor, on-site rooms if any, typical cost band
> - 3-4 direct-answer FAQs specific to this venue (e.g. "What is the guest capacity at [venue]?", "Does [venue] allow outside caterers?", "How far in advance should I book [venue]?")
> - A closing CTA to enquire with Swariya about this venue
> - FAQPage JSON-LD for the venue-specific FAQs
> Then generate individual pages at /venues/[venue-slug].html for these venues: [LIST YOUR 3-5 VENUES WITH THEIR REAL DETAILS HERE]
> Reuse the shared CSS, don't duplicate styles inline.
> ```

---

### Day 6 — Niche-community page + cost-guide asset (Phase 3, part 4)
**Goal:** claim one high-relevance, low-competition search niche outright.

- Pick the one community Swariya serves most (e.g. Kannada, Tamil Brahmin, or another specific tradition).
- Build the community-specific page.
- Extend the existing 120-guide library into one flagship, citable cost-guide page for Bengaluru/Mysuru/Hyderabad.

> **Prompt 7 — Niche community page**
> ```
> Build /[community-name]-wedding-planner-bengaluru.html in the site's design system.
> Content should cover, in the direct-answer FAQ style used elsewhere on the site:
> - The specific ritual sequence for a [COMMUNITY] wedding: [LIST RITUALS, e.g. Tilak, Sagai, Sangeet, Baaraat, Phere — fill in for your actual community]
> - Typical guest count range Swariya has handled for this community
> - Aesthetic/decor conventions specific to this tradition
> - A direct-answer FAQ: "Who is the best [community] wedding planner in Bengaluru?"
> Link to 2-3 relevant existing guides from /blog/guides/ where topically related.
> Output the complete file.
> ```

> **Prompt 8 — Flagship cost guide**
> ```
> Create /bengaluru-wedding-cost-guide-2026.html, a comprehensive, citable cost reference in the site's design system.
> Structure:
> - Cost breakdown by guest count band (intimate 50-150, mid 150-400, large 400+) covering venue, catering per plate, decor, and photography ranges for Bengaluru, Mysuru, and Hyderabad separately
> - A short methodology note ("based on Swariya's [TRUE NUMBER] weddings planned since [YEAR]")
> - Include a simple downloadable/printable structure (a clean print stylesheet is enough for week one, a PDF export can come later)
> - End with a CTA to get a personalized estimate
> This page is meant to be the kind of asset other sites and blogs would link to — keep the data specific and well-organized, not vague.
> ```

---

### Day 7 — QA pass, deploy, and measurement setup
**Goal:** ship everything live and start tracking whether it's working.

- Full site crawl to confirm number/canonical consistency held after all new pages were added.
- Manually deploy the full build to Netlify (drag-and-drop or CLI, given the site is not Git-linked).
- Set up/verify Google Search Console and note current indexed page count as the baseline.
- Note current ranking position for 3-4 target phrases to track weekly going forward.

> **Prompt 9 — Final QA pass**
> ```
> Do a final crawl of the entire site including all new pages built this week.
> Verify:
> 1. The weddings-planned number is identical everywhere it appears
> 2. Every canonical tag matches its actual served URL
> 3. Every new page includes valid FAQPage JSON-LD (validate the JSON syntax)
> 4. Every new page links back to at least one existing page (no orphan pages) and the homepage links to every new page
> 5. All new pages use the shared CSS file rather than duplicated inline styles
> Report any failures found, then fix them.
> ```

---

## What to track from Day 8 onward
- Indexed page count in Search Console (baseline set Day 7)
- Ranking position for: "wedding planner Bengaluru," "destination wedding planner Bengaluru," your top venue name, your niche-community phrase
- Google + WedMeGood review count trend
- Which of the new pages (Ask Swariya, venue pages, cost guide) get the most organic traffic after 30 days — that tells you which pattern to double down on next

## What's deliberately left out of week one
The proprietary couple portal, a daily publishing cadence, and a 90+ review base are the long-term moat pieces from the blueprint — not achievable in a week and not the point of this sprint. This week is entirely about closing the foundation gap and copying the patterns that are copyable now, so that whatever content and outreach effort comes next actually compounds instead of fighting an inconsistent, under-indexed site.
