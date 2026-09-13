import os
import json
from venues_data import VENUES_DATA

os.makedirs("venues", exist_ok=True)

# 1. GENERATE ALL 20 VENUE PAGES
def generate_venue_page(v):
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
                <div class="faq-card">
                    <h3 class="faq-question">{q}</h3>
                    <p class="faq-answer">{a}</p>
                </div>""" for q, a in v["faqs"]])

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "EventVenue",
                "@id": f"https://swariyaweddings.com/venues/{v['slug']}.html#venue",
                "name": f"{v['name']} - Wedding Venue Bangalore",
                "description": v["tagline"],
                "url": f"https://swariyaweddings.com/venues/{v['slug']}.html",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Bengaluru",
                    "addressRegion": "Karnataka",
                    "addressCountry": "IN"
                },
                "maximumAttendeeCapacity": v["capacity"].split("–")[-1].replace("Guests", "").strip() if "–" in v["capacity"] else "1000",
                "priceRange": v["pricing"]
            },
            {
                "@type": "FAQPage",
                "@id": f"https://swariyaweddings.com/venues/{v['slug']}.html#faq",
                "mainEntity": faqs_schema
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"https://swariyaweddings.com/venues/{v['slug']}.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://swariyaweddings.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Venues", "item": "https://swariyaweddings.com/venues.html"},
                    {"@type": "ListItem", "position": 3, "name": v["name"], "item": f"https://swariyaweddings.com/venues/{v['slug']}.html"}
                ]
            }
        ]
    }, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{v['name']} Bangalore Wedding Cost, Capacity & Planning | Swariya Weddings</title>
    <meta name="description" content="{v['name']} in {v['location']}: Capacity ({v['capacity']}), {v['rooms']}, rental cost & decor guidelines. Plan your dream wedding with Swariya Weddings.">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="https://swariyaweddings.com/venues/{v['slug']}.html">

    <!-- Open Graph -->
    <meta property="og:title" content="{v['name']} Bangalore Wedding Guide | Swariya Weddings">
    <meta property="og:description" content="{v['tagline']}">
    <meta property="og:url" content="https://swariyaweddings.com/venues/{v['slug']}.html">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://swariyaweddings.com/apple-touch-icon.png">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">

    <style>
        :root {{
            --primary: #9d2551;
            --primary-dark: #7a1c3e;
            --primary-light: #fbebf1;
            --accent: #d4af37;
            --text-main: #2b2b2b;
            --text-muted: #666666;
            --bg-light: #faf9f6;
            --white: #ffffff;
            --card-shadow: 0 10px 30px rgba(0,0,0,0.06);
            --border-radius: 12px;
        }}
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; color: var(--text-main); background: var(--bg-light); line-height: 1.6; }}
        h1, h2, h3, h4 {{ font-family: 'Playfair Display', serif; color: var(--primary-dark); }}
        .venue-hero {{ padding: 130px 20px 60px; background: linear-gradient(135deg, #fceef3 0%, #fff9f0 100%); text-align: center; border-bottom: 1px solid #f0e2e7; }}
        .venue-hero h1 {{ font-size: 2.8rem; margin-bottom: 15px; }}
        .venue-hero .tagline {{ font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto 20px; }}
        .venue-meta-badge {{ display: inline-flex; align-items: center; gap: 8px; background: var(--primary-light); color: var(--primary); padding: 8px 18px; border-radius: 30px; font-weight: 600; font-size: 0.95rem; }}
        
        .container {{ max-width: 1140px; margin: 0 auto; padding: 0 20px; }}
        .venue-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 40px; margin-top: 40px; }}
        @media (max-width: 850px) {{ .venue-grid {{ grid-template-columns: 1fr; }} }}

        .spec-box {{ background: var(--white); border-radius: var(--border-radius); padding: 30px; box-shadow: var(--card-shadow); border: 1px solid #f0eae5; margin-bottom: 30px; }}
        .spec-item {{ display: flex; justify-content: space-between; padding: 14px 0; border-bottom: 1px dashed #eee; font-size: 1rem; }}
        .spec-item:last-child {{ border-bottom: none; }}
        .spec-label {{ font-weight: 600; color: var(--text-muted); }}
        .spec-val {{ font-weight: 700; color: var(--primary-dark); text-align: right; }}

        .lead-card {{ background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); color: white; padding: 30px; border-radius: var(--border-radius); box-shadow: var(--card-shadow); position: sticky; top: 100px; }}
        .lead-card h3 {{ color: white; margin-bottom: 10px; font-size: 1.6rem; }}
        .lead-card p {{ opacity: 0.9; font-size: 0.95rem; margin-bottom: 20px; }}
        .btn-whatsapp {{ display: flex; align-items: center; justify-content: center; gap: 10px; background: #25d366; color: white; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 700; font-size: 1rem; transition: 0.2s; margin-bottom: 12px; }}
        .btn-whatsapp:hover {{ background: #1eb956; }}
        .btn-contact {{ display: block; text-align: center; background: white; color: var(--primary-dark); text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 700; font-size: 1rem; }}

        .faq-section {{ margin-top: 40px; }}
        .faq-card {{ background: var(--white); border-radius: var(--border-radius); padding: 22px 26px; margin-bottom: 15px; box-shadow: var(--card-shadow); border-left: 4px solid var(--primary); }}
        .faq-question {{ font-size: 1.2rem; margin-bottom: 8px; font-weight: 700; }}
        .faq-answer {{ font-size: 0.98rem; color: #444; margin: 0; }}

        .breadcrumb {{ padding: 15px 0; font-size: 0.9rem; color: #888; }}
        .breadcrumb a {{ color: var(--primary); text-decoration: none; }}
    </style>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <!-- Navbar -->
    <header class="header">
        <div class="container nav-container">
            <a href="../index.html" class="logo">
                <span class="logo-main">Swariya</span>
                <span class="logo-sub">Weddings</span>
            </a>
            <nav class="nav-menu">
                <a href="../index.html" class="nav-link">Home</a>
                <a href="../about.html" class="nav-link">About</a>
                <a href="../services.html" class="nav-link">Services</a>
                <a href="../venues.html" class="nav-link active">Venues</a>
                <a href="../bengaluru-wedding-cost-guide-2026.html" class="nav-link">Cost Guide 2026</a>
                <a href="../ask.html" class="nav-link">Ask Q&A</a>
                <a href="../reviews.html" class="nav-link">Reviews</a>
                <a href="../contact.html" class="btn-primary">Plan Your Wedding</a>
            </nav>
        </div>
    </header>

    <div class="venue-hero">
        <div class="container">
            <div class="breadcrumb">
                <a href="../index.html">Home</a> &gt; <a href="../venues.html">Venues</a> &gt; <span>{v['name']}</span>
            </div>
            <span class="venue-meta-badge">📍 {v['location']}</span>
            <h1>{v['name']}</h1>
            <p class="tagline">{v['tagline']}</p>
        </div>
    </div>

    <main class="container">
        <div class="venue-grid">
            <div class="venue-main">
                <div class="spec-box">
                    <h2>Venue Blueprint & Specifications</h2>
                    <div class="spec-item">
                        <span class="spec-label">Guest Capacity</span>
                        <span class="spec-val">{v['capacity']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">On-Site Accommodation</span>
                        <span class="spec-val">{v['rooms']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Event Zones & Spaces</span>
                        <span class="spec-val">{v['spaces']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Typical Rental / Packages</span>
                        <span class="spec-val">{v['pricing']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Catering Policy</span>
                        <span class="spec-val">{v['catering']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Decor & Production Policy</span>
                        <span class="spec-val">{v['decor']}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Recommended Booking Window</span>
                        <span class="spec-val">{v['lead_time']}</span>
                    </div>
                </div>

                <div class="spec-box">
                    <h2>Swariya Weddings at {v['name']}</h2>
                    <p>Having planned and executed over <strong>150+ bespoke celebrations in Bengaluru</strong>, Swariya Weddings brings specialized layout engineering, vendor management, and decor fabrication experience to <strong>{v['name']}</strong>.</p>
                    <p>From custom acoustic management and ambient tree illumination to traditional banana leaf Oota seating and luxury bridal concierge, our on-site team ensures your celebration is flawlessly orchestrated.</p>
                </div>

                <div class="faq-section">
                    <h2>Frequently Asked Questions — {v['name']}</h2>
                    {faq_html}
                </div>
            </div>

            <aside class="venue-sidebar">
                <div class="lead-card">
                    <h3>Check Date Availability</h3>
                    <p>Planning a wedding at {v['name']}? Inquire with our team for exclusive decor portfolios, date availability, and consolidated pricing.</p>
                    <a href="https://wa.me/919606822204?text=Hi%20Swariya%20Weddings,%20I%20am%20interested%20in%20planning%20my%20wedding%20at%20{v['name'].replace(' ', '%20')}." class="btn-whatsapp" target="_blank" rel="noopener">
                        <span>💬 WhatsApp Venue Concierge</span>
                    </a>
                    <a href="../contact.html" class="btn-contact">Book Free Consultation</a>
                </div>
            </aside>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer" style="background:#1a1a1a; color:#fff; padding:60px 0 30px; margin-top:80px;">
        <div class="container" style="text-align:center;">
            <p><strong>Swariya Weddings</strong> — Premier Wedding Planners in Bengaluru. 150+ Weddings | 500+ Happy Clients | 4.9/5 Rating.</p>
            <p style="font-size:0.9rem; color:#aaa;">© 2026 Swariya Weddings. All Rights Reserved. <a href="../venues.html" style="color:#d4af37;">Explore All Bangalore Venues</a></p>
        </div>
    </footer>
</body>
</html>"""
    
    with open(f"venues/{v['slug']}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated venue: venues/{v['slug']}.html")

for v in VENUES_DATA:
    generate_venue_page(v)

print(f"Successfully generated all {len(VENUES_DATA)} venue pages!")
