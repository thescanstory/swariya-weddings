# -*- coding: utf-8 -*-
"""
Programmatic SEO & AEO Generator for Swariya Weddings
Generates 100 High-Converting Luxury Micro-Market Landing Pages
"""

import os
import json
import urllib.parse
from micromarkets_100_data import MICROMARKETS

def generate_html(data):
    slug = data["slug"]
    category = data.get("category", "bengaluru")
    title = data["title"]
    meta_desc = data["meta_desc"]
    h1 = data["h1"]
    subtitle = data["subtitle"]
    loc_name = data["location_name"]
    city = data["city"]
    state = data["state"]
    budget = data["budget_range"]
    capacity = data["guest_capacity"]
    venues = data["venues"]
    logistics = data["logistics"]
    hero_img = data["hero_img"]
    faqs = data["faqs"]

    canonical_url = f"https://swariyaweddings.com/{slug}.html"
    
    # WhatsApp CTA prefilled text
    wa_msg = f"Hi Swariya Weddings, I'm planning a luxury wedding in {loc_name} (Budget: {budget}). I'd like to check availability and venue options."
    wa_url = f"https://wa.me/918050573382?text={urllib.parse.quote(wa_msg)}"

    # Schema 1: Service
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": f"{canonical_url}#service",
        "name": h1,
        "serviceType": "Luxury Wedding Planning & Turnkey Concierge",
        "provider": {
            "@type": "LocalBusiness",
            "name": "Swariya Weddings",
            "url": "https://swariyaweddings.com/",
            "telephone": "+91-8050573382",
            "priceRange": budget,
            "image": f"https://swariyaweddings.com/{hero_img}",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": city,
                "addressRegion": state,
                "addressCountry": "IN"
            }
        },
        "areaServed": {
            "@type": "Place",
            "name": loc_name
        },
        "description": meta_desc
    }

    # Schema 2: Breadcrumb
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://swariyaweddings.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Destinations & Corridors",
                "item": "https://swariyaweddings.com/destination-wedding-planner-india.html"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": loc_name,
                "item": canonical_url
            }
        ]
    }

    # Schema 3: FAQPage
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f["a"]
                }
            } for f in faqs
        ]
    }

    # Generate Venue Cards HTML
    venue_cards_html = ""
    for v in venues:
        venue_cards_html += f"""
                <div class="venue-card">
                    <span class="venue-tag">⭐ SIGNATURE LUXURY PARTNER</span>
                    <h3>{v}</h3>
                    <p style="font-size: 0.92rem; color: #666; line-height: 1.6;">Turnkey wedding design, stage production, room block negotiations & zero markup billing managed by Swariya.</p>
                </div>"""

    # Generate FAQ HTML
    faq_html = ""
    for f in faqs:
        faq_html += f"""
            <div class="faq-item">
                <h3>{f['q']}</h3>
                <p>{f['a']}</p>
            </div>"""

    # Full HTML Page Template
    html_content = f"""<!DOCTYPE html>
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
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="author" content="Swariya Weddings">
    <link rel="canonical" href="{canonical_url}">
    <title>{title}</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Poppins:wght@300;400;500;600&display=swap">
    <link rel="stylesheet" href="style.css?v=26">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Swariya Weddings">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="https://swariyaweddings.com/{hero_img}">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://swariyaweddings.com/{hero_img}">

    <!-- JSON-LD Schemas -->
    <script type="application/ld+json">
    {json.dumps(service_schema, indent=2)}
    </script>

    <script type="application/ld+json">
    {json.dumps(breadcrumb_schema, indent=2)}
    </script>

    <script type="application/ld+json">
    {json.dumps(faq_schema, indent=2)}
    </script>

    <style>
        .hub-hero {{
            background: linear-gradient(180deg, rgba(10, 28, 24, 0.78) 0%, rgba(10, 28, 24, 0.92) 100%), url('{hero_img}') center/cover no-repeat;
            color: #fff;
            padding: 120px 20px 80px;
            text-align: center;
        }}
        .hub-hero h1 {{
            font-size: clamp(2.2rem, 5vw, 3.4rem);
            color: #FAF6F0;
            margin-bottom: 16px;
            font-family: var(--font-heading);
            line-height: 1.2;
        }}
        .hub-hero .hub-subtitle {{
            font-size: 1.25rem;
            color: var(--accent-light, #DFC479);
            font-weight: 500;
            margin-bottom: 16px;
        }}
        .hub-hero p.hub-lead {{
            font-size: 1.12rem;
            max-width: 820px;
            margin: 0 auto 30px;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.7;
        }}
        .hub-cta-group {{
            display: flex;
            gap: 16px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .btn-gold-primary {{
            background: linear-gradient(135deg, #D4AF37 0%, #AA820A 100%);
            color: #0A1C18;
            font-weight: 700;
            padding: 15px 32px;
            border-radius: 30px;
            text-decoration: none;
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.35);
            transition: 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}
        .btn-gold-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.5);
            color: #000;
        }}
        .btn-outline-white {{
            background: transparent;
            border: 1.5px solid #fff;
            color: #fff;
            font-weight: 600;
            padding: 15px 28px;
            border-radius: 30px;
            text-decoration: none;
            transition: 0.3s;
        }}
        .btn-outline-white:hover {{
            background: rgba(255, 255, 255, 0.15);
        }}
        .hub-section {{
            padding: 60px 20px;
        }}
        .specs-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin: 30px 0;
        }}
        .spec-card {{
            background: #FAF6F0;
            border: 1px solid var(--border-gold, #DFC479);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }}
        .spec-card .label {{
            font-size: 0.8rem;
            color: #7A5B0B;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }}
        .spec-card .value {{
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--dark-luxury, #0A1C18);
        }}
        .venue-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 22px;
            margin-top: 25px;
        }}
        .venue-card {{
            background: #fff;
            border-radius: 12px;
            border: 1px solid var(--border-gold, #DFC479);
            padding: 24px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.04);
            transition: 0.3s;
        }}
        .venue-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.2);
            border-color: var(--accent, #D4AF37);
        }}
        .venue-card h3 {{
            color: var(--primary, #15382e);
            font-size: 1.2rem;
            margin-bottom: 8px;
        }}
        .venue-tag {{
            display: inline-block;
            background: rgba(212, 175, 55, 0.15);
            color: #7A5B0B;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.76rem;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        .feature-box {{
            background: linear-gradient(180deg, #FAF6F0 0%, #F5EDE0 100%);
            border-radius: 14px;
            padding: 35px 25px;
            border: 1px solid var(--border-gold, #DFC479);
            margin: 40px 0;
        }}
        .faq-item {{
            background: #fff;
            border: 1px solid var(--border-gold, #DFC479);
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 14px;
        }}
        .faq-item h3 {{
            font-size: 1.12rem;
            color: var(--dark-luxury, #0A1C18);
            margin-bottom: 8px;
        }}
        .faq-item p {{
            color: #555;
            line-height: 1.65;
            margin: 0;
        }}
    </style>
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PGH8WNPW"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

    <!-- Header Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="logo"><a href="index.html">SWARIYA</a></div>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About us</a></li>
                <li><a href="services.html">Our Services</a></li>
                <li><a href="destination-wedding-planner-india.html" class="active" style="color: var(--accent); font-weight: 500;">Destinations</a></li>
                <li><a href="venues.html">Our Venues</a></li>
                <li><a href="client-portal.html">Wedding OS</a></li>
                <li><a href="wedding-budget-calculator.html">Budget Tool</a></li>
                <li><a href="wedding-brief-builder.html">Brief Builder</a></li>
                <li><a href="reviews.html">Reviews</a></li>
                <li><a href="contact.html" class="btn-contact">Contact us</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hub-hero">
        <div class="container">
            <p class="section-label" style="color: var(--accent-light, #DFC479); letter-spacing: 2px;">✦ BESPOKE LUXURY WEDDING PRODUCTION • {city.upper()}</p>
            <h1>{h1}</h1>
            <div class="hub-subtitle">{subtitle}</div>
            <p class="hub-lead">{meta_desc}</p>
            <div class="hub-cta-group">
                <a href="{wa_url}" class="btn-gold-primary" target="_blank" rel="noopener">
                    <span>💬 Inquire on WhatsApp</span>
                </a>
                <a href="wedding-budget-calculator.html" class="btn-outline-white">Calculate {city} Wedding Budget</a>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="container hub-section">

        <!-- Micro-Market Metrics Bar -->
        <div class="specs-grid">
            <div class="spec-card">
                <div class="label">Target Micro-Market</div>
                <div class="value">{loc_name}</div>
            </div>
            <div class="spec-card">
                <div class="label">Typical Luxury Budget</div>
                <div class="value">{budget}</div>
            </div>
            <div class="spec-card">
                <div class="label">Guest Scale Managed</div>
                <div class="value">{capacity}</div>
            </div>
            <div class="spec-card">
                <div class="label">Fiduciary Guarantee</div>
                <div class="value" style="color: #2D6A4F;">0% Vendor Markups</div>
            </div>
        </div>

        <!-- The Swariya Standard & Transparency -->
        <div class="feature-box">
            <div style="max-width: 850px; margin: 0 auto; text-align: center;">
                <p class="section-label">✦ THE SWARIYA FIDUCIARY STANDARD</p>
                <h2 style="font-size: 2rem; color: var(--primary); margin-bottom: 15px;">Why Discerning Families Choose Swariya in {loc_name}</h2>
                <p style="color: #444; line-height: 1.7; font-size: 1.05rem;">
                    Unlike traditional event brokers who inflate vendor bills by 15–30%, Swariya Weddings charges an upfront professional management fee. You pay actual hotel room blocks, decorator fabrication, and catering costs directly, saving lakhs while enjoying high-touch architectural design and stress-free execution.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 30px;">
                <div style="background: white; padding: 22px; border-radius: 10px; border: 1px solid var(--border-gold);">
                    <h4 style="color: var(--primary); margin-bottom: 6px;">🏛️ 3D Architectural Decor Visualization</h4>
                    <p style="font-size: 0.92rem; color: #666; margin: 0;">Photorealistic 3D mandap and ballroom renders prior to on-ground fabrication.</p>
                </div>
                <div style="background: white; padding: 22px; border-radius: 10px; border: 1px solid var(--border-gold);">
                    <h4 style="color: var(--primary); margin-bottom: 6px;">📋 100% Financial Ledger Transparency</h4>
                    <p style="font-size: 0.92rem; color: #666; margin: 0;">Direct vendor contracts, wholesale pricing pass-through, and line-item clarity.</p>
                </div>
                <div style="background: white; padding: 22px; border-radius: 10px; border: 1px solid var(--border-gold);">
                    <h4 style="color: var(--primary); margin-bottom: 6px;">⭐ On-Ground Master Shadow Coordination</h4>
                    <p style="font-size: 0.92rem; color: #666; margin: 0;">Dedicated senior planners for the bridal couple, family VIPs, and artist timelines.</p>
                </div>
            </div>
        </div>

        <!-- Curated Venues Section -->
        <div style="margin-top: 50px;">
            <p class="section-label">✦ CURATED SIGNATURE VENUES</p>
            <h2 style="font-size: 2rem; color: var(--dark-luxury);">Premier Luxury Venues in {loc_name}</h2>
            <p style="color: #666; margin-top: 5px;">We coordinate room blocks, buyout negotiations, acoustic setups, and banquet production across these top properties:</p>
            <div class="venue-grid">
                {venue_cards_html}
            </div>
        </div>

        <!-- Regional Logistics & Weather Insights -->
        <div style="background: #FAF6F0; border-radius: 14px; border: 1px solid var(--border-gold); padding: 30px; margin-top: 50px;">
            <h3 style="color: var(--primary); font-size: 1.4rem; margin-bottom: 10px;">📍 Local Production & Logistics Overview: {loc_name}</h3>
            <p style="color: #555; line-height: 1.7; font-size: 1rem; margin: 0;">
                {logistics}
            </p>
        </div>

        <!-- FAQs -->
        <div style="margin-top: 60px;">
            <p class="section-label">✦ FREQUENTLY ASKED QUESTIONS</p>
            <h2 style="font-size: 2rem; color: var(--dark-luxury); margin-bottom: 25px;">{h1} — FAQs</h2>
            {faq_html}
        </div>

        <!-- Call to Action Banner -->
        <div style="background: radial-gradient(circle at 50% 50%, #15382e 0%, #0a1c18 100%); color: white; border-radius: 16px; padding: 45px 25px; text-align: center; margin-top: 60px; border: 1.5px solid var(--border-gold);">
            <h2 style="color: #FAF6F0; font-size: 2.2rem; margin-bottom: 12px; font-family: var(--font-heading);">Begin Planning Your {loc_name} Wedding</h2>
            <p style="max-width: 680px; margin: 0 auto 25px; opacity: 0.9; font-size: 1.05rem;">Schedule a complimentary planning consultation with Swariya's senior directors. Receive a customized venue shortlist, 3D design moodboard, and transparent budget matrix within 24 hours.</p>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="{wa_url}" class="btn-gold-primary" target="_blank" rel="noopener">
                    <span>💬 Chat with Wedding Specialist</span>
                </a>
                <a href="wedding-brief-builder.html" class="btn-outline-white">Build Your Wedding Brief</a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="site-footer" style="margin-top: 80px;">
        <div class="container footer-content">
            <div class="footer-col">
                <a href="/" class="footer-logo">Swariya <span>Weddings</span></a>
                <p>Pan-India Luxury & Destination Wedding Planners. Headquartered in Bengaluru with nationwide execution across Goa, Rajasthan, Kerala, Coorg & beyond. 150+ weddings planned with zero vendor markups.</p>
                <p style="margin-top: 10px; font-size: 0.85rem; color: #888;">📍 Atelier: HSR Layout, Bengaluru | 📞 +91 80505 73382</p>
            </div>
            <div class="footer-col">
                <h4>Destination Hubs</h4>
                <ul>
                    <li><a href="/destination-wedding-planner-india.html">Pan-India Destination Hub</a></li>
                    <li><a href="/destination-wedding-planner-in-goa.html">Goa Beachfront Weddings</a></li>
                    <li><a href="/destination-wedding-planner-in-udaipur-rajasthan.html">Rajasthan Palace Weddings</a></li>
                    <li><a href="/destination-wedding-planner-in-kerala.html">Kerala Backwater Weddings</a></li>
                    <li><a href="/destination-wedding-planner-in-coorg.html">Coorg Plantation Weddings</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Interactive Planning Tools</h4>
                <ul>
                    <li><a href="/wedding-brief-builder.html">Wedding Brief Builder</a></li>
                    <li><a href="/client-portal.html">Wedding OS Workspace</a></li>
                    <li><a href="/wedding-budget-calculator.html">Budget Calculator</a></li>
                    <li><a href="/venue-finder.html">Bangalore Venue Comparator</a></li>
                    <li><a href="/bengaluru-wedding-cost-guide-2026.html">2026 Cost Benchmark</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All Rights Reserved. • <a href="/sitemap.xml">Sitemap</a> • <a href="/reviews.html">Verified Reviews</a></p>
        </div>
    </footer>
    <script src="nav.js"></script>
</body>
</html>
"""
    return html_content

def main():
    generated_count = 0
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    print(f"Starting programmatic page generation for {len(MICROMARKETS)} micro-markets...")
    
    for item in MICROMARKETS:
        slug = item["slug"]
        html_code = generate_html(item)
        target_path = os.path.join(workspace_root, f"{slug}.html")
        
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_code)
        
        generated_count += 1
        print(f"[{generated_count}/{len(MICROMARKETS)}] Generated: {slug}.html")

    print(f"\nSUCCESS: Programmatically generated {generated_count} luxury micro-market landing pages!")

if __name__ == "__main__":
    main()
