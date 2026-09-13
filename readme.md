# Swariya Weddings — Website Project

Static HTML/CSS site for [swariyaweddings.com](https://swariyaweddings.com), currently live on Netlify.

## Structure

- `index.html` — Homepage (hero, stats, timeline, wedding styles, testimonials, venues preview, direct-answer FAQ, blog preview, budget estimator, contact form)
- `about.html` — Company story, timeline, values, direct-answer FAQ
- `services.html` — Service breakdown, day-of vs full planning, pricing overview, and FAQs
- `venues.html` — Venue grid with filters and links to dedicated venue spotlights
- `reviews.html` — Client reviews funnel (Google, WedMeGood, WhatsApp) and testimonials
- `ask.html` / `ask/index.html` — "Ask Swariya" crowdsourced Q&A hub
- `bengaluru-wedding-cost-guide-2026.html` — 2026 flagship citable cost benchmark report with print stylesheet
- `kannada-wedding-planner-bengaluru.html` — Traditional Kannada ritual breakdown, decor & catering vertical
- `venues/the-tamarind-tree-bangalore.html` — Dedicated Tamarind Tree venue guide
- `venues/the-leela-palace-bengaluru.html` — Dedicated Leela Palace venue guide
- `venues/taj-west-end-bengaluru.html` — Dedicated Taj West End venue guide
- `venues/amita-rasa-bangalore.html` — Dedicated Amita Rasa venue guide
- `venues/the-grape-garden-bangalore.html` — Dedicated Grape Garden venue guide
- `gallery.html` — Real Weddings photo gallery with category filters and lightbox
- `blog.html` — Blog post previews
- `contact.html` — Contact form and details
- `style.css` — Single shared stylesheet (burgundy/gold luxury theme, Playfair Display + Poppins fonts)
- `sitemap.xml`, `robots.txt`, `llms.txt` — SEO / AEO files

## Deployment

The site is live on Netlify under project `swariya-weddings-live` (site ID `35d10d9d-bf93-4e21-b826-93b6e1d1526c`, Rebondir Studios team), connected to the custom domain `swariyaweddings.com`.

To deploy manually via Netlify CLI:

```bash
npx netlify-cli deploy --prod --dir=. --site=35d10d9d-bf93-4e21-b826-93b6e1d1526c
```

## Content notes

- Founding year is 2020 (used consistently across timeline text and schema.org markup — keep this in sync if it's edited).
- Phone: +91-8050573382. Address: #343, 9th Main, 22nd Cross Rd, 7th Sector, HSR Layout, Bengaluru - 560102.
- All 6 pages carry schema.org JSON-LD (Organization, LocalBusiness, FAQPage, Service, ItemList, ContactPage, Blog, ImageGallery, BreadcrumbList) for SEO/AEO.
