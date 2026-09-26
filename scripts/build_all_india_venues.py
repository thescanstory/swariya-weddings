import os
import re
import json
import glob
import sys

print("Starting Master All-India Venues Generator & Interlinker...")

os.makedirs("venues", exist_ok=True)
os.makedirs("sitemaps", exist_ok=True)

sys.path.insert(0, 'scripts')
from venues_data import VENUES_DATA
from generate_phase2_venues import DESTINATION_VENUES

# Consolidate all venues into a master dictionary keyed by slug
ALL_VENUES = {}

# Add Bengaluru & Karnataka venues from venues_data
for v in VENUES_DATA:
    slug = v['slug']
    city_category = "bengaluru"
    state_val = "Karnataka"
    loc_val = v.get('location', 'Bengaluru, Karnataka')
    if 'Mysore' in v['name'] or 'Mysuru' in loc_val:
        city_category = "karnataka"
    elif 'Kabini' in v['name'] or 'Hampi' in loc_val or 'Coorg' in loc_val or 'Chikmagalur' in loc_val or 'Sakleshpur' in loc_val:
        city_category = "karnataka"

    ALL_VENUES[slug] = {
        "slug": slug,
        "name": v["name"],
        "city_category": city_category,
        "location": loc_val,
        "state": state_val,
        "tagline": v.get("tagline", f"Premier luxury wedding venue in {loc_val} featuring bespoke banquet and lawn settings."),
        "capacity": v.get("capacity", "200 – 1,000 Guests"),
        "rooms": v.get("rooms", "Available upon request"),
        "pricing": v.get("pricing", "₹2,500 – ₹4,500 per plate"),
        "hero_img": v.get("hero_img", "images/10.jpg"),
        "faqs": v.get("faqs", [
            (f"What is the guest capacity at {v['name']}?", f"{v['name']} accommodates celebrations from intimate gatherings of 150 up to 1,000+ guests depending on lawn and banquet combinations."),
            (f"Does {v['name']} permit outside decorators?", f"Yes, Swariya Weddings is an empaneled luxury decorator managing custom stage fabrication, ambient lighting, and floral styling."),
            (f"How can I book a wedding at {v['name']}?", f"Swariya Weddings provides complimentary venue walkthroughs, date holds, and contract negotiation with zero hidden markups.")
        ])
    }

# Add Destination Venues
for v in DESTINATION_VENUES:
    slug = v['slug']
    city_str = v.get('city', '')
    state_str = v.get('state', '')
    
    # Classify city category
    c_lower = (city_str + " " + state_str + " " + v['name']).lower()
    if 'goa' in c_lower:
        cat = 'goa'
    elif 'udaipur' in c_lower:
        cat = 'udaipur'
    elif 'jaipur' in c_lower or 'bishangarh' in c_lower or 'samode' in c_lower or 'chomu' in c_lower:
        cat = 'jaipur'
    elif 'jodhpur' in c_lower or 'jaisalmer' in c_lower:
        cat = 'jodhpur_jaisalmer'
    elif 'pushkar' in c_lower or 'bikaner' in c_lower or 'mount abu' in c_lower:
        cat = 'rajasthan_other'
    elif 'kerala' in c_lower or 'kochi' in c_lower or 'kumarakom' in c_lower or 'kovalam' in c_lower or 'munnar' in c_lower or 'wayanad' in c_lower or 'alleppey' in c_lower:
        cat = 'kerala'
    elif 'hyderabad' in c_lower or 'telangana' in c_lower:
        cat = 'hyderabad'
    elif 'mumbai' in c_lower or 'alibaug' in c_lower or 'lonavala' in c_lower or 'pune' in c_lower or 'maharashtra' in c_lower:
        cat = 'mumbai_alibaug'
    elif 'chennai' in c_lower or 'mahabalipuram' in c_lower or 'tamil' in c_lower or 'ooty' in c_lower or 'kodaikanal' in c_lower:
        cat = 'chennai_tamilnadu'
    elif 'delhi' in c_lower or 'gurgaon' in c_lower or 'ncr' in c_lower or 'noida' in c_lower:
        cat = 'delhi_ncr'
    elif 'rishikesh' in c_lower or 'mussoorie' in c_lower or 'corbett' in c_lower or 'uttarakhand' in c_lower or 'shimla' in c_lower or 'himalayas' in c_lower:
        cat = 'himalayas_rishikesh'
    elif 'gujarat' in c_lower or 'anand' in c_lower or 'ahmedabad' in c_lower or 'vadodara' in c_lower:
        cat = 'gujarat'
    elif 'bengaluru' in c_lower or 'bangalore' in c_lower:
        cat = 'bengaluru'
    elif 'karnataka' in c_lower or 'mysore' in c_lower or 'coorg' in c_lower or 'kabini' in c_lower or 'hampi' in c_lower or 'chikmagalur' in c_lower or 'sakleshpur' in c_lower:
        cat = 'karnataka'
    else:
        cat = 'other_india'

    ALL_VENUES[slug] = {
        "slug": slug,
        "name": v["name"],
        "city_category": cat,
        "location": f"{city_str}, {state_str}".strip(", "),
        "state": state_str,
        "tagline": v.get("tagline", f"Exclusive luxury wedding destination at {v['name']} in {city_str}, {state_str}."),
        "capacity": v.get("capacity", "150 – 800 Guests"),
        "rooms": v.get("rooms", "Luxury rooms & suites available"),
        "pricing": v.get("pricing", "₹25,00,000 – ₹75,00,000 / event buyout"),
        "hero_img": v.get("hero_img", "images/10.jpg"),
        "faqs": v.get("faqs", [
            (f"What makes {v['name']} ideal for destination weddings?", f"{v['name']} offers signature architecture, luxury accommodations, and spectacular outdoor event spaces designed for multi-day Indian weddings."),
            (f"How does Swariya Weddings coordinate weddings at {v['name']}?", f"Swariya Weddings manages guest logistics, vendor negotiations, bespoke décor styling, and on-ground coordination with zero vendor markups.")
        ])
    }

print(f"Total Unique Indian Venues Compiled: {len(ALL_VENUES)}")

# 2. GENERATE / REFRESH EACH INDIVIDUAL VENUE PAGE
for slug, v in ALL_VENUES.items():
    related = [rv for rslug, rv in ALL_VENUES.items() if rslug != slug and (rv['city_category'] == v['city_category'] or rv['state'] == v['state'])][:6]
    if len(related) < 4:
        related += [rv for rslug, rv in ALL_VENUES.items() if rslug != slug and rv not in related][:6 - len(related)]

    faqs_schema = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        } for q, a in v["faqs"]
    ]

    faq_html = "\n".join([f"""
            <div class="faq-item" style="margin-bottom: 16px; border: 1px solid #E0E0E0; border-radius: 8px; padding: 20px 24px; background: #fff;">
                <h4 style="margin: 0 0 8px; color: #8B1A1A; cursor: pointer; font-size: 1.05rem; display: flex; justify-content: space-between;">{q} <span>+</span></h4>
                <p style="margin: 0; color: #555; line-height: 1.6; font-size: 0.95rem;">{a}</p>
            </div>""" for q, a in v["faqs"]])

    related_links_html = "".join([f'<a href="/venues/{rv["slug"]}" style="display: inline-block; margin: 4px 6px; padding: 7px 14px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 20px; font-size: 0.85rem; color: #2C2723; text-decoration: none; font-weight: 500;">{rv["name"]} ({rv["location"]})</a>' for rv in related])

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "EventVenue",
                "@id": f"https://swariyaweddings.com/venues/{slug}#venue",
                "name": f"{v['name']} - Luxury Wedding Venue",
                "description": v["tagline"],
                "url": f"https://swariyaweddings.com/venues/{slug}",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": v["location"],
                    "addressCountry": "IN"
                },
                "maximumAttendeeCapacity": v["capacity"].split("–")[-1].replace("Guests", "").strip() if "–" in v["capacity"] else "800",
                "priceRange": v["pricing"]
            },
            {
                "@type": "FAQPage",
                "@id": f"https://swariyaweddings.com/venues/{slug}#faq",
                "mainEntity": faqs_schema
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"https://swariyaweddings.com/venues/{slug}#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://swariyaweddings.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Venues", "item": "https://swariyaweddings.com/venues"},
                    {"@type": "ListItem", "position": 3, "name": v["name"], "item": f"https://swariyaweddings.com/venues/{slug}"}
                ]
            }
        ]
    }, indent=2)

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) - GA4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4SKRDGSHGF"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-4SKRDGSHGF');
      gtag('config', 'AW-16941717881');
    </script>
    <meta name="google-site-verification" content="yzEXJ6aZqKbrVXZNEsuVjiSuXGsZAGy4ZLqUfqFkjzY" />
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-PGH8WNPW');</script>
    <!-- End Google Tag Manager -->
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{v['name']} Wedding Cost, Capacity & Planning Guide | Swariya Weddings</title>
    <meta name="description" content="{v['name']} in {v['location']}: Guest capacity ({v['capacity']}), {v['rooms']}, rental & catering pricing, and wedding planning with Swariya Weddings.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://swariyaweddings.com/venues/{slug}">

    <!-- Open Graph -->
    <meta property="og:title" content="{v['name']} Wedding Guide | Swariya Weddings">
    <meta property="og:description" content="{v['tagline']}">
    <meta property="og:url" content="https://swariyaweddings.com/venues/{slug}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://swariyaweddings.com/images/10.jpg">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Poppins:wght@300;400;500;600&display=swap">
    <link rel="stylesheet" href="../style.css?v=26">

    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PGH8WNPW" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="logo"><a href="/">SWARIYA</a></div>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="/">Home</a></li>
                <li><a href="/about">About us</a></li>
                <li><a href="/services">Our Services</a></li>
                <li><a href="/venues" class="active" style="color: var(--accent); font-weight: 500;">Our Venues</a></li>
                <li><a href="/gallery">Gallery</a></li>
                <li><a href="/reviews">Reviews</a></li>
                <li><a href="/ask">Ask Swariya</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/contact" class="btn-contact">Contact Us</a></li>
            </ul>
        </div>
    </nav>

    <!-- Venue Hero Header -->
    <header style="background: linear-gradient(135deg, #0a1c18 0%, #16362d 100%); color: #FFF8F0; padding: 70px 20px; text-align: center; border-bottom: 1px solid rgba(212,175,55,0.3);">
        <div class="container" style="max-width: 900px;">
            <p style="color: #D4AF37; font-size: 0.85rem; letter-spacing: 2.5px; text-transform: uppercase; font-weight: 600; margin-bottom: 12px;">✦ SIGNATURE INDIAN WEDDING VENUE ✦</p>
            <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4vw, 3.2rem); color: #FFF8F0; margin-bottom: 16px; line-height: 1.2;">{v['name']}</h1>
            <p style="font-size: 1.1rem; color: #e0d8cc; line-height: 1.6; margin-bottom: 24px;">{v['tagline']}</p>
            <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                <span style="background: rgba(255,255,255,0.1); border: 1px solid rgba(212,175,55,0.4); padding: 6px 16px; border-radius: 20px; font-size: 0.88rem;">📍 {v['location']}</span>
                <span style="background: rgba(255,255,255,0.1); border: 1px solid rgba(212,175,55,0.4); padding: 6px 16px; border-radius: 20px; font-size: 0.88rem;">👥 {v['capacity']}</span>
                <span style="background: rgba(255,255,255,0.1); border: 1px solid rgba(212,175,55,0.4); padding: 6px 16px; border-radius: 20px; font-size: 0.88rem;">💰 {v['pricing']}</span>
            </div>
        </div>
    </header>

    <!-- Breadcrumbs -->
    <div class="container" style="padding: 16px 20px;">
        <ul class="breadcrumb" style="display: flex; gap: 8px; list-style: none; font-size: 0.88rem; color: #777; margin: 0;">
            <li><a href="/" style="color: #8B1A1A; text-decoration: none;">Home</a> &gt;</li>
            <li><a href="/venues" style="color: #8B1A1A; text-decoration: none;">All Venues</a> &gt;</li>
            <li aria-current="page" style="color: #444; font-weight: 500;">{v['name']}</li>
        </ul>
    </div>

    <!-- Main Content -->
    <main class="container" style="padding: 30px 20px 60px;">
        <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start;">
            <div>
                <section style="background: #fff; border: 1px solid #E8E2D8; border-radius: 12px; padding: 35px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); margin-bottom: 40px;">
                    <h2 style="font-family: 'Playfair Display', serif; color: #8B1A1A; font-size: 1.8rem; margin-bottom: 20px;">Venue Overview & Key Specifications</h2>
                    <p style="font-size: 1.05rem; line-height: 1.8; color: #444; margin-bottom: 25px;">
                        <strong>{v['name']}</strong> is widely celebrated as one of India's premier wedding destinations in {v['location']}. Whether hosting an intimate royal ceremony or a grand multi-day luxury celebration, the property delivers unmatched grandeur, hospitality, and unforgettable visual backdrops.
                    </p>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; background: #FAF7F2; padding: 25px; border-radius: 8px; border: 1px solid #EAE3D9;">
                        <div>
                            <strong style="color: #8B1A1A; display: block; font-size: 0.85rem; text-transform: uppercase;">Guest Capacity</strong>
                            <span style="font-size: 1rem; color: #333; font-weight: 600;">{v['capacity']}</span>
                        </div>
                        <div>
                            <strong style="color: #8B1A1A; display: block; font-size: 0.85rem; text-transform: uppercase;">Room Accommodations</strong>
                            <span style="font-size: 1rem; color: #333; font-weight: 600;">{v['rooms']}</span>
                        </div>
                        <div>
                            <strong style="color: #8B1A1A; display: block; font-size: 0.85rem; text-transform: uppercase;">Estimated Pricing</strong>
                            <span style="font-size: 1rem; color: #333; font-weight: 600;">{v['pricing']}</span>
                        </div>
                        <div>
                            <strong style="color: #8B1A1A; display: block; font-size: 0.85rem; text-transform: uppercase;">Planning Partner</strong>
                            <span style="font-size: 1rem; color: #333; font-weight: 600;">Swariya Weddings (0% Markups)</span>
                        </div>
                    </div>
                </section>

                <section style="margin-bottom: 40px;">
                    <h2 style="font-family: 'Playfair Display', serif; color: #8B1A1A; font-size: 1.8rem; margin-bottom: 20px;">Frequently Asked Questions</h2>
                    {faq_html}
                </section>
            </div>

            <!-- Lead Capture Card -->
            <aside style="background: linear-gradient(135deg, #8B1A1A 0%, #5E1212 100%); color: #fff; padding: 32px 28px; border-radius: 12px; position: sticky; top: 100px; box-shadow: 0 10px 30px rgba(139,26,26,0.25);">
                <span style="color: #D4AF37; font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 600;">✦ BESPOKE WEDDING PLANNING</span>
                <h3 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #FFF8F0; margin: 10px 0 12px;">Plan Your Wedding at {v['name']}</h3>
                <p style="font-size: 0.92rem; color: rgba(255,255,255,0.9); line-height: 1.6; margin-bottom: 24px;">
                    Get transparent estimates, date holds, and complete decor styling with Swariya Weddings.
                </p>
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I%20am%20interested%20in%20planning%20a%20wedding%20at%20{v['name'].replace(' ', '%20')}" target="_blank" rel="noopener noreferrer" style="display: block; text-align: center; background: #25D366; color: #fff; padding: 12px; border-radius: 6px; font-weight: 600; text-decoration: none; margin-bottom: 12px;">Chat on WhatsApp ↗</a>
                <a href="/contact" style="display: block; text-align: center; background: #D4AF37; color: #0a1c18; padding: 12px; border-radius: 6px; font-weight: 600; text-decoration: none;">Book Consultation Call</a>
            </aside>
        </div>

        <!-- Backlink to All Venues Directory & Crosslinks -->
        <section style="margin-top: 50px; padding: 30px; background: #FAF6F0; border: 1px solid #E8DFD5; border-radius: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 18px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; margin: 0; color: #1C1917;">Explore Related Signature Venues in {v['state'] or 'India'}</h3>
                <a href="/venues" style="color: #8B1A1A; font-weight: 600; text-decoration: underline; font-size: 0.92rem;">← Back to All India Venues Directory</a>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {related_links_html}
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-section">
                <h3>Swariya Weddings</h3>
                <p>#343, 9th Main, 22nd Cross Rd<br>7th Sector, HSR Layout<br>Bengaluru - 560102</p>
                <p><strong>Phone:</strong> <a href="tel:+918050573382">+91 8050573382</a></p>
            </div>
            <div class="footer-section">
                <h3>Explore Pan-India</h3>
                <ul>
                    <li><a href="/venues"><strong>All India Venues Directory</strong></a></li>
                    <li><a href="/destinations-directory">3,000+ Destination Guides</a></li>
                    <li><a href="/wedding-budget-calculator">Wedding Budget Calculator</a></li>
                    <li><a href="/bengaluru-wedding-cost-guide-2026">2026 Wedding Cost Guide</a></li>
                </ul>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All rights reserved.</p>
        </div>
    </footer>

    <script src="../nav.js"></script>
</body>
</html>"""

    with open(f"venues/{slug}.html", "w", encoding="utf-8") as f:
        f.write(page_html)

print(f"Generated {len(ALL_VENUES)} individual venue HTML pages in venues/")

# 3. BUILD MASTER /venues.html
city_filters = [
    ("all", "All India", len(ALL_VENUES)),
    ("bengaluru", "Bengaluru", len([v for v in ALL_VENUES.values() if v['city_category'] == 'bengaluru'])),
    ("goa", "Goa", len([v for v in ALL_VENUES.values() if v['city_category'] == 'goa'])),
    ("udaipur", "Udaipur", len([v for v in ALL_VENUES.values() if v['city_category'] == 'udaipur'])),
    ("jaipur", "Jaipur", len([v for v in ALL_VENUES.values() if v['city_category'] == 'jaipur'])),
    ("jodhpur_jaisalmer", "Jodhpur & Jaisalmer", len([v for v in ALL_VENUES.values() if v['city_category'] == 'jodhpur_jaisalmer'])),
    ("kerala", "Kerala", len([v for v in ALL_VENUES.values() if v['city_category'] == 'kerala'])),
    ("hyderabad", "Hyderabad", len([v for v in ALL_VENUES.values() if v['city_category'] == 'hyderabad'])),
    ("mumbai_alibaug", "Mumbai & Alibaug", len([v for v in ALL_VENUES.values() if v['city_category'] == 'mumbai_alibaug'])),
    ("chennai_tamilnadu", "Chennai & Mahabalipuram", len([v for v in ALL_VENUES.values() if v['city_category'] == 'chennai_tamilnadu'])),
    ("delhi_ncr", "Delhi NCR", len([v for v in ALL_VENUES.values() if v['city_category'] == 'delhi_ncr'])),
    ("himalayas_rishikesh", "Himalayas & Rishikesh", len([v for v in ALL_VENUES.values() if v['city_category'] == 'himalayas_rishikesh'])),
    ("karnataka", "Karnataka Regions", len([v for v in ALL_VENUES.values() if v['city_category'] == 'karnataka'])),
    ("gujarat", "Gujarat & Central India", len([v for v in ALL_VENUES.values() if v['city_category'] in ['gujarat', 'rajasthan_other', 'other_india']]))
]

filter_buttons_html = "\n".join([f'<button class="venue-filter-pill {"active" if cat=="all" else ""}" data-category="{cat}">{label} ({cnt})</button>' for cat, label, cnt in city_filters if cnt > 0])

venue_cards_html = []
for slug, v in ALL_VENUES.items():
    cat = v['city_category']
    if cat in ['gujarat', 'rajasthan_other', 'other_india']:
        filter_cat = 'gujarat'
    else:
        filter_cat = cat

    card = f"""
        <div class="venue-directory-card" data-category="{filter_cat}" data-name="{v['name'].lower()}" data-location="{v['location'].lower()}">
            <div class="venue-card-img-wrap" style="position: relative; overflow: hidden; height: 210px; border-radius: 10px 10px 0 0;">
                <img src="/images/10.jpg" alt="{v['name']} Wedding Venue {v['location']}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;">
                <span style="position: absolute; top: 12px; left: 12px; background: rgba(10,28,24,0.85); color: #D4AF37; padding: 4px 10px; border-radius: 14px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; border: 1px solid rgba(212,175,55,0.4);">📍 {v['location']}</span>
            </div>
            <div style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1; background: #fff; border-radius: 0 0 10px 10px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 1.25rem; color: #8B1A1A; margin: 0 0 8px; line-height: 1.3;">{v['name']}</h3>
                <p style="font-size: 0.88rem; color: #666; line-height: 1.5; margin-bottom: 16px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{v['tagline']}</p>
                <div style="border-top: 1px solid #f0eae1; padding-top: 12px; margin-bottom: 16px; font-size: 0.82rem; color: #444; display: flex; justify-content: space-between;">
                    <span><strong>Capacity:</strong> {v['capacity'].split('–')[-1].strip()}</span>
                    <span><strong>Pricing:</strong> {v['pricing'].split('–')[0].strip()}</span>
                </div>
                <a href="/venues/{v['slug']}" style="display: block; text-align: center; background: linear-gradient(135deg, #8B1A1A 0%, #641212 100%); color: #fff; padding: 10px; border-radius: 6px; font-weight: 600; font-size: 0.88rem; text-decoration: none; transition: 0.2s;">Explore Venue & Costs →</a>
            </div>
        </div>
    """
    venue_cards_html.append(card)

cards_joined = "\n".join(venue_cards_html)

itemlist_schema = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Pan-India Luxury Wedding Venues Directory",
    "description": "Comprehensive list of 100+ top palace, resort, and beach wedding venues across India curated by Swariya Weddings.",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": {
                "@type": "EventVenue",
                "name": v['name'],
                "url": f"https://swariyaweddings.com/venues/{v['slug']}",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": v['location'],
                    "addressCountry": "IN"
                }
            }
        } for idx, v in enumerate(ALL_VENUES.values())
    ]
}

venues_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) - GA4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4SKRDGSHGF"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-4SKRDGSHGF');
      gtag('config', 'AW-16941717881');
    </script>
    <meta name="google-site-verification" content="yzEXJ6aZqKbrVXZNEsuVjiSuXGsZAGy4ZLqUfqFkjzY" />
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-PGH8WNPW');</script>
    <!-- End Google Tag Manager -->
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Discover 100+ premier luxury wedding venues across India. Palaces in Rajasthan, beach resorts in Goa & Kerala, heritage lawns in Bengaluru & beyond.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://swariyaweddings.com/venues">
    <title>Top Luxury Wedding Venues in India (100+ Palaces & Resorts) | Swariya</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Poppins:wght@300;400;500;600&display=swap">
    <link rel="stylesheet" href="/style.css?v=26">

    <style>
        .venue-filter-pill {{
            background: #fff;
            border: 1px solid #D8CEBE;
            color: #4A4A4A;
            padding: 8px 18px;
            border-radius: 25px;
            font-size: 0.88rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.25s ease;
            white-space: nowrap;
        }}
        .venue-filter-pill:hover {{
            border-color: #8B1A1A;
            color: #8B1A1A;
        }}
        .venue-filter-pill.active {{
            background: #8B1A1A;
            color: #fff;
            border-color: #8B1A1A;
            box-shadow: 0 4px 12px rgba(139,26,26,0.25);
        }}
        .venues-grid-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 28px;
            margin-top: 35px;
        }}
        .venue-directory-card {{
            border: 1px solid #E8E2D8;
            border-radius: 12px;
            background: #fff;
            box-shadow: 0 4px 15px rgba(0,0,0,0.04);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .venue-directory-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(10,28,24,0.1);
        }}
        .venue-search-box {{
            width: 100%;
            max-width: 500px;
            padding: 14px 22px;
            border: 1px solid #D8CEBE;
            border-radius: 30px;
            font-size: 0.95rem;
            outline: none;
            box-shadow: 0 2px 10px rgba(0,0,0,0.03);
            transition: border-color 0.25s ease;
            font-family: inherit;
        }}
        .venue-search-box:focus {{
            border-color: #8B1A1A;
        }}
    </style>

    <script type="application/ld+json">
{json.dumps(itemlist_schema, indent=2)}
    </script>
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PGH8WNPW" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="logo"><a href="/">SWARIYA</a></div>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="/">Home</a></li>
                <li><a href="/about">About us</a></li>
                <li><a href="/services">Our Services</a></li>
                <li><a href="/venues" class="active" style="color: var(--accent); font-weight: 500;">Our Venues</a></li>
                <li><a href="/gallery">Gallery</a></li>
                <li><a href="/reviews">Reviews</a></li>
                <li><a href="/ask">Ask Swariya</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/contact" class="btn-contact">Contact Us</a></li>
            </ul>
        </div>
    </nav>

    <!-- Header Section -->
    <div class="page-header" style="background: linear-gradient(135deg, #0a1c18 0%, #16362d 100%); color: #FFF8F0; padding: 75px 20px; text-align: center;">
        <p class="section-label" style="color: #D4AF37; letter-spacing: 3px; font-weight: 600;">✦ CURATED PAN-INDIA VENUES DIRECTORY ✦</p>
        <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(2.2rem, 4.5vw, 3.4rem); color: #FFF8F0; margin: 12px 0 16px;">Top Luxury & Destination Wedding Venues in India</h1>
        <p class="subtitle" style="max-width: 800px; margin: 0 auto 25px; color: #e0d8cc; font-size: 1.1rem; line-height: 1.6;">
            Explore 100+ handpicked 5-star palace hotels, beachfront resorts, heritage estates, and luxury convention grounds across Bengaluru, Goa, Rajasthan, Kerala, and Nationwide.
        </p>
        
        <!-- Live Search Bar -->
        <div style="margin-top: 20px;">
            <input type="text" id="venueSearchInput" class="venue-search-box" placeholder="🔍 Search venue by name, city, or state (e.g. Leela, Goa, Udaipur)...">
        </div>
    </div>

    <!-- Main Directory Section -->
    <div class="container" style="padding: 45px 20px 80px;">
        <!-- Filter Pills Bar -->
        <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; margin-bottom: 25px;" id="filterPillsContainer">
            {filter_buttons_html}
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E8E2D8; padding-bottom: 12px; margin-bottom: 20px;">
            <span style="font-size: 0.95rem; color: #666;" id="resultsCountText">Showing all {len(ALL_VENUES)} luxury venues across India</span>
            <a href="/contact" style="font-size: 0.9rem; color: #8B1A1A; font-weight: 600; text-decoration: underline;">Request Multi-Venue Comparison Sheet →</a>
        </div>

        <!-- Venue Cards Grid -->
        <div class="venues-grid-container" id="venuesGrid">
            {cards_joined}
        </div>
    </div>

    <!-- Crosslink Hub Section -->
    <section class="related-guides-grid" style="margin: 40px auto 70px; max-width: 1200px; padding: 35px 30px; background: #FAF6F0; border: 1px solid #E8DFD5; border-radius: 12px;">
        <h3 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 14px; color: #1C1917;">Explore Related Pan-India Destination Guides & Planning Tools</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
            <a href="/destination-wedding-planner-india" style="display: inline-block; padding: 7px 15px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 20px; font-size: 0.88rem; color: #2C2723; text-decoration: none; font-weight: 500;">Pan-India Destinations Hub</a>
            <a href="/destinations-directory" style="display: inline-block; padding: 7px 15px; background: #C5A059; color: #FFF; border-radius: 20px; font-size: 0.88rem; text-decoration: none; font-weight: 600;">3,000+ Micromarket Directory ↗</a>
            <a href="/wedding-budget-calculator" style="display: inline-block; padding: 7px 15px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 20px; font-size: 0.88rem; color: #2C2723; text-decoration: none; font-weight: 500;">Interactive Budget Calculator</a>
            <a href="/bengaluru-wedding-cost-guide-2026" style="display: inline-block; padding: 7px 15px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 20px; font-size: 0.88rem; color: #2C2723; text-decoration: none; font-weight: 500;">2026 Wedding Cost Benchmarks</a>
            <a href="/kannada-wedding-planner-bengaluru" style="display: inline-block; padding: 7px 15px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 20px; font-size: 0.88rem; color: #2C2723; text-decoration: none; font-weight: 500;">Kannada Traditional Weddings</a>
            <a href="/telugu-destination-wedding-planner-guide" style="display: inline-block; padding: 7px 15px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 20px; font-size: 0.88rem; color: #2C2723; text-decoration: none; font-weight: 500;">Telugu Royal Weddings</a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-section">
                <h3>Swariya Weddings</h3>
                <p>#343, 9th Main, 22nd Cross Rd<br>7th Sector, HSR Layout<br>Bengaluru - 560102</p>
                <p><strong>Pan-India & Global Destinations:</strong> Bengaluru, Goa, Udaipur, Jaipur, Jodhpur, Kerala, Coorg, Chennai, Hyderabad, Mumbai, Delhi NCR</p>
            </div>
            <div class="footer-section">
                <h3>Navigate</h3>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About Us</a></li>
                    <li><a href="/venues"><strong>All India Venues</strong></a></li>
                    <li><a href="/services">Services</a></li>
                    <li><a href="/gallery">Gallery</a></li>
                    <li><a href="/reviews">Client Reviews</a></li>
                    <li><a href="/ask">Ask Swariya</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Contact</h3>
                <p>📞 <a href="tel:+918050573382">(+91) 8050573382</a></p>
                <p>💬 <a href="https://wa.me/918050573382">WhatsApp</a></p>
                <p>📧 info@swariyaweddings.com</p>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All rights reserved.</p>
        </div>
    </footer>

    <script src="/nav.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const pills = document.querySelectorAll('.venue-filter-pill');
            const cards = document.querySelectorAll('.venue-directory-card');
            const searchInput = document.getElementById('venueSearchInput');
            const countText = document.getElementById('resultsCountText');

            let currentCategory = 'all';
            let currentSearch = '';

            function filterVenues() {{
                let visibleCount = 0;
                cards.forEach(card => {{
                    const cardCat = card.dataset.category;
                    const cardName = card.dataset.name || '';
                    const cardLoc = card.dataset.location || '';

                    const matchesCat = (currentCategory === 'all' || cardCat === currentCategory);
                    const matchesSearch = (!currentSearch || cardName.includes(currentSearch) || cardLoc.includes(currentSearch));

                    if (matchesCat && matchesSearch) {{
                        card.style.display = 'flex';
                        visibleCount++;
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});

                countText.textContent = `Showing ${{visibleCount}} of ${{cards.length}} luxury venues`;
            }}

            pills.forEach(pill => {{
                pill.addEventListener('click', () => {{
                    pills.forEach(p => p.classList.remove('active'));
                    pill.classList.add('active');
                    currentCategory = pill.dataset.category;
                    filterVenues();
                }});
            }});

            searchInput.addEventListener('input', (e) => {{
                currentSearch = e.target.value.toLowerCase().trim();
                filterVenues();
            }});
        }});
    </script>
</body>
</html>"""

with open("venues.html", "w", encoding="utf-8") as f:
    f.write(venues_index_html)

with open("venues/index.html", "w", encoding="utf-8") as f:
    f.write(venues_index_html)

print("Generated venues.html and venues/index.html")

# 4. REBUILD SITEMAP_VENUES.XML & MASTER SITEMAP.XML
venue_sitemap_urls = []
venue_sitemap_urls.append("""  <url>
    <loc>https://swariyaweddings.com/venues</loc>
    <lastmod>2026-09-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.95</priority>
  </url>""")

for slug in ALL_VENUES.keys():
    venue_sitemap_urls.append(f"""  <url>
    <loc>https://swariyaweddings.com/venues/{slug}</loc>
    <lastmod>2026-09-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>""")

joined_urls = "\n".join(venue_sitemap_urls)
venues_xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{joined_urls}
</urlset>"""

with open("sitemaps/sitemap_venues.xml", "w", encoding="utf-8") as f:
    f.write(venues_xml_content)

print(f"Generated sitemaps/sitemap_venues.xml with {len(venue_sitemap_urls)} clean URLs")

with open("sitemap.xml", "r", encoding="utf-8") as f:
    master_sitemap = f.read()

if "sitemaps/sitemap_venues.xml" not in master_sitemap:
    master_sitemap = master_sitemap.replace("</sitemapindex>", """  <sitemap>
    <loc>https://swariyaweddings.com/sitemaps/sitemap_venues.xml</loc>
    <lastmod>2026-09-21</lastmod>
  </sitemap>
</sitemapindex>""")
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(master_sitemap)
    print("Updated master sitemap.xml with sitemaps/sitemap_venues.xml")

print("All tasks completed successfully!")
