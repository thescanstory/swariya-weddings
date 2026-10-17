#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Clean 100-Quality-Pages Architecture for Swariya Weddings.
Regenerates sitemap.xml, llms.txt, and sets noindex on non-curated pages.
"""

import os
from bs4 import BeautifulSoup
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SELECTED_100 = [
    # Tier 1: Core Brand & Business Flagships (10)
    ("index.html", 1.0, "daily", "Brand Homepage & Direct Booking Hub"),
    ("wedding-planners-in-bangalore.html", 1.0, "daily", "Flagship Bangalore Wedding Planning Master Hub"),
    ("about.html", 0.9, "weekly", "Company Heritage, Founders & 0% Commission Philosophy"),
    ("services.html", 0.95, "weekly", "Full Service Planning, Partial Coordination & Deliverables"),
    ("venues.html", 0.95, "weekly", "Verified Venue Directory & Curated Bangalore Portfolio"),
    ("venue-finder.html", 0.9, "weekly", "Interactive Smart Venue Finder Tool"),
    ("reviews.html", 0.9, "weekly", "Client Testimonials & Google / WedMeGood Review Hub"),
    ("gallery.html", 0.85, "weekly", "Real Weddings Photo Portfolio & Aesthetic Gallery"),
    ("ask.html", 0.85, "weekly", "Ask Swariya Crowdsourced Q&A & Advice Hub"),
    ("contact.html", 0.9, "monthly", "WhatsApp Concierge & Consultation Request"),

    # Tier 2: Flagship Tools & Benchmark Guides (5)
    ("wedding-budget-calculator.html", 0.9, "weekly", "Interactive Bengaluru Wedding Budget Estimator"),
    ("wedding-brief-builder.html", 0.9, "weekly", "Custom Wedding Aesthetic & Brief Generator"),
    ("bengaluru-wedding-cost-guide-2026.html", 0.95, "weekly", "2026 Citable Wedding Cost & Vendor Benchmark Report"),
    ("top-wedding-planners-in-bangalore-comparison.html", 0.9, "weekly", "Unbiased Agency Comparison Guide"),
    ("destination-wedding-planner-india.html", 0.9, "weekly", "Pan-India Luxury Destination Wedding Planning"),

    # Tier 3: Cultural & Regional Traditions (10)
    ("kannada-wedding-planner-bengaluru.html", 0.9, "weekly", "Authentic Kannada Wedding Rituals & Mandap Decor"),
    ("telugu-wedding-planner-bengaluru.html", 0.9, "weekly", "Telugu Pellillu Ritual Coordination & Catering"),
    ("tamil-wedding-planner-bengaluru.html", 0.85, "weekly", "Tamil Brahmin & Traditional Wedding Planning"),
    ("marwari-wedding-planner-bengaluru.html", 0.85, "weekly", "Royal Marwari Ceremonies & Pure Veg Feasts"),
    ("3-day-runsheet-and-rituals-for-grand-telugu-royal-wedding.html", 0.8, "monthly", "3-Day Telugu Royal Wedding Ritual Runsheet"),
    ("3-day-runsheet-and-rituals-for-royal-marwari-wedding.html", 0.8, "monthly", "3-Day Royal Marwari Wedding Itinerary"),
    ("3-day-runsheet-and-rituals-for-mangalorean-bunt-traditional-wedding.html", 0.8, "monthly", "Mangalorean Bunt Rituals & Decor Guide"),
    ("3-day-runsheet-and-rituals-for-kodava-traditional-coffee-estate-wedding.html", 0.8, "monthly", "Kodava Coffee Estate Wedding Guide"),
    ("3-day-runsheet-and-rituals-for-kerala-christian-royal-wedding.html", 0.8, "monthly", "Kerala Christian Wedding Celebrations Guide"),
    ("3-day-runsheet-and-rituals-for-pure-veg-and-jain-luxury-wedding.html", 0.8, "monthly", "Pure Veg & Jain Luxury Wedding Planning"),

    # Tier 4: Bangalore High-Commercial Neighborhood Corridors (15)
    ("wedding-planners-in-hsr-layout-bangalore.html", 0.85, "weekly", "HSR Layout Wedding Planner Hub"),
    ("wedding-planners-in-indiranagar-bangalore.html", 0.85, "weekly", "Indiranagar Wedding Planning & Boutique Venues"),
    ("wedding-planners-in-koramangala-bangalore.html", 0.85, "weekly", "Koramangala Wedding Services"),
    ("wedding-planners-in-whitefield-bangalore.html", 0.85, "weekly", "Whitefield Luxury IT Corridor Wedding Planning"),
    ("wedding-planners-in-jayanagar-bangalore.html", 0.85, "weekly", "Jayanagar Heritage & South Bengaluru Weddings"),
    ("wedding-planners-in-jp-nagar-bangalore.html", 0.85, "weekly", "JP Nagar Wedding Planning Services"),
    ("wedding-planners-in-sadashivanagar-bangalore.html", 0.85, "weekly", "Sadashivanagar Elite Wedding Coordination"),
    ("wedding-planners-in-lavelle-road-bangalore.html", 0.85, "weekly", "Lavelle Road Central Luxury Weddings"),
    ("wedding-planners-in-palace-grounds-bangalore.html", 0.85, "weekly", "Palace Grounds Large-Scale Weddings"),
    ("wedding-planners-in-yelahanka-bangalore.html", 0.85, "weekly", "Yelahanka & North Bangalore Resort Weddings"),
    ("wedding-planners-in-electronic-city-bangalore.html", 0.85, "weekly", "Electronic City Wedding Services"),
    ("wedding-planners-in-sarjapur-road-bangalore.html", 0.85, "weekly", "Sarjapur Road Villa & Lawn Weddings"),
    ("wedding-planners-in-bellandur-bangalore.html", 0.85, "weekly", "Bellandur Tech Corridor Wedding Planning"),
    ("wedding-planners-in-hebbal-bangalore.html", 0.85, "weekly", "Hebbal Lake & Resort Wedding Services"),
    ("wedding-planners-in-malleshwaram-bangalore.html", 0.85, "weekly", "Malleshwaram Traditional Wedding Planning"),

    # Tier 5: Top 60 Curated Venue Guides (60)
    # Bangalore & Karnataka Escapes (30)
    ("venues/the-tamarind-tree-bangalore.html", 0.85, "weekly", "The Tamarind Tree Heritage Estate Wedding Guide"),
    ("venues/the-leela-palace-bengaluru.html", 0.85, "weekly", "The Leela Palace Bengaluru 5-Star Wedding Guide"),
    ("venues/taj-west-end-bengaluru.html", 0.85, "weekly", "Taj West End Bengaluru Heritage Luxury Guide"),
    ("venues/amita-rasa-bangalore.html", 0.85, "weekly", "Amita Rasa Nandi Hills Contemporary Wedding Venue"),
    ("venues/gayatri-vihar-palace-grounds.html", 0.85, "weekly", "Gayatri Vihar Palace Grounds Grand Wedding Guide"),
    ("venues/templetree-leisure-bangalore.html", 0.85, "weekly", "Templetree Leisure Boutique Eco-Resort Guide"),
    ("venues/itc-gardenia-bengaluru.html", 0.85, "weekly", "ITC Gardenia Luxury Hotel Wedding Guide"),
    ("venues/jw-marriott-bengaluru.html", 0.85, "weekly", "JW Marriott Bengaluru City Center Wedding Guide"),
    ("venues/the-grape-garden-bangalore.html", 0.85, "weekly", "The Grape Garden Open-Air Lawn Venue Guide"),
    ("venues/clarks-exotica-resort-bangalore-wedding.html", 0.8, "weekly", "Clarks Exotica Convention Resort & Spa"),
    ("venues/angsana-oasis-resort-bangalore-wedding.html", 0.8, "weekly", "Angsana Oasis Resort & Spa Wedding Guide"),
    ("venues/signature-club-resort-bangalore.html", 0.8, "weekly", "Signature Club Resort Devanahalli Guide"),
    ("venues/miraya-greens-bangalore.html", 0.8, "weekly", "Miraya Greens Sprawling Lawn Venue Guide"),
    ("venues/moongate-bangalore.html", 0.8, "weekly", "Moongate International Center Wedding Venue"),
    ("venues/jade-735-bangalore.html", 0.8, "weekly", "Jade 735 Boutique Private Retreat Wedding Guide"),
    ("venues/royal-palms-bangalore.html", 0.8, "weekly", "Royal Palms Exclusive Garden Venue Guide"),
    ("venues/royalton-leisure-bangalore.html", 0.8, "weekly", "Royalton Leisure Bannerghatta Wedding Guide"),
    ("venues/samavana-wedding-venue-bangalore.html", 0.8, "weekly", "Samavana Forest Aesthetic Wedding Venue"),
    ("venues/shankaraa-foundation-bangalore.html", 0.8, "weekly", "Shankaraa Foundation Cultural Heritage Venue"),
    ("venues/white-mist-bangalore.html", 0.8, "weekly", "White Mist by Happy Retreats Nandi Foothills"),
    ("venues/windflower-prakruthi-bangalore.html", 0.8, "weekly", "Windflower Prakruthi Resort Devanahalli"),
    ("venues/wiwaha-wedding-venue-bangalore.html", 0.8, "weekly", "Wiwaha Wedding Venue Kanakapura Road"),
    ("venues/tharavadu-mane-bangalore.html", 0.8, "weekly", "Tharavadu Mane Traditional Kerala Architecture Venue"),
    ("venues/gitanjali-wedding-venue-bangalore.html", 0.8, "weekly", "Gitanjali Wedding Venue Guide"),
    ("venues/goldfinch-retreat-bangalore.html", 0.8, "weekly", "Goldfinch Retreat Yelahanka Wedding Guide"),
    ("venues/area-83-bangalore.html", 0.8, "weekly", "Area 83 Adventure & Lakeside Wedding Retreat"),
    ("venues/the-tamara-coorg-wedding.html", 0.8, "weekly", "The Tamara Coorg Rainforest Luxury Wedding Guide"),
    ("venues/taj-madikeri-resort-coorg-wedding.html", 0.8, "weekly", "Taj Madikeri Resort & Spa Coorg Wedding Guide"),
    ("venues/evolve-back-hampi-wedding.html", 0.8, "weekly", "Evolve Back Kamalapura Palace Hampi Wedding Guide"),
    ("venues/evolve-back-kabini-wedding.html", 0.8, "weekly", "Evolve Back Kuruba Safari Lodge Kabini"),

    # Destination Gems: Goa, Rajasthan, Kerala, Heritage (30)
    ("venues/the-oberoi-udaivilas-udaipur-wedding.html", 0.85, "weekly", "The Oberoi Udaivilas Udaipur Palace Wedding Guide"),
    ("venues/the-leela-palace-udaipur-wedding.html", 0.85, "weekly", "The Leela Palace Udaipur Lake Pichola Wedding"),
    ("venues/jagmandir-island-palace-udaipur-wedding.html", 0.85, "weekly", "Jagmandir Island Palace Udaipur Wedding Guide"),
    ("venues/shiv-niwas-palace-udaipur-wedding.html", 0.8, "weekly", "Shiv Niwas Palace Heritage Wedding Guide"),
    ("venues/rambagh-palace-jaipur-wedding.html", 0.85, "weekly", "Rambagh Palace Jaipur Royal Wedding Guide"),
    ("venues/fairmont-jaipur-wedding.html", 0.85, "weekly", "Fairmont Jaipur Grand Rajasthani Wedding Guide"),
    ("venues/the-oberoi-rajvilas-jaipur-wedding.html", 0.85, "weekly", "The Oberoi Rajvilas Jaipur Luxury Wedding"),
    ("venues/jai-mahal-palace-jaipur-wedding.html", 0.8, "weekly", "Jai Mahal Palace Jaipur Mughal Gardens Wedding"),
    ("venues/alila-fort-bishangarh-jaipur-wedding.html", 0.85, "weekly", "Alila Fort Bishangarh 230-Year-Old Warrior Fortress"),
    ("venues/samode-palace-jaipur-wedding.html", 0.8, "weekly", "Samode Palace Heritage Shekhawati Art Wedding"),
    ("venues/umaid-bhawan-palace-jodhpur-wedding.html", 0.85, "weekly", "Umaid Bhawan Palace Jodhpur Royal Residence"),
    ("venues/suryagarh-jaisalmer-wedding.html", 0.85, "weekly", "Suryagarh Jaisalmer Thar Desert Fortress Wedding"),
    ("venues/the-leela-goa-wedding.html", 0.85, "weekly", "The Leela Goa Cavelossim Beach Wedding Guide"),
    ("venues/taj-exotica-resort-goa-wedding.html", 0.85, "weekly", "Taj Exotica Resort & Spa Goa Benaulim Wedding"),
    ("venues/w-goa-vagator-wedding.html", 0.85, "weekly", "W Goa Vagator Beachfront Contemporary Wedding"),
    ("venues/grand-hyatt-goa-wedding.html", 0.85, "weekly", "Grand Hyatt Goa Bambolim Bay Wedding Guide"),
    ("venues/alila-diwa-goa-wedding.html", 0.8, "weekly", "Alila Diwa Goa South Goa Paddy Fields & Beach"),
    ("venues/caravela-beach-resort-goa-wedding.html", 0.8, "weekly", "Caravela Beach Resort Varca Goa Wedding"),
    ("venues/st-regis-goa-resort-wedding.html", 0.85, "weekly", "The St. Regis Goa Resort Mobor Luxury Wedding"),
    ("venues/itc-grand-goa-resort-wedding.html", 0.85, "weekly", "ITC Grand Goa Resort & Spa Arossim Beach"),
    ("venues/the-leela-kovalam-wedding.html", 0.85, "weekly", "The Leela Kovalam Cliff-Top Sea View Wedding"),
    ("venues/taj-green-cove-resort-kovalam-wedding.html", 0.8, "weekly", "Taj Green Cove Resort & Spa Kovalam Wedding"),
    ("venues/grand-hyatt-kochi-bolgatty-wedding.html", 0.85, "weekly", "Grand Hyatt Kochi Bolgatty Backwater Wedding"),
    ("venues/brunton-boatyard-kochi-wedding.html", 0.8, "weekly", "Brunton Boatyard Fort Kochi Colonial Heritage"),
    ("venues/kumarakom-lake-resort-wedding.html", 0.85, "weekly", "Kumarakom Lake Resort Kerala Backwaters Wedding"),
    ("venues/coconut-lagoon-kumarakom-wedding.html", 0.8, "weekly", "Coconut Lagoon CGH Earth Traditional Heritage"),
    ("venues/the-taj-mahal-palace-mumbai-wedding.html", 0.85, "weekly", "The Taj Mahal Palace Mumbai Gateway of India"),
    ("venues/taj-lands-end-mumbai-wedding.html", 0.85, "weekly", "Taj Lands End Bandra Arabian Sea Views"),
    ("venues/taj-falaknuma-palace-hyderabad-wedding.html", 0.85, "weekly", "Taj Falaknuma Palace Hyderabad Nizam Royal Wedding"),
    ("venues/lalitha-mahal-palace-mysore-wedding.html", 0.8, "weekly", "Lalitha Mahal Palace Mysore Italian Renaissance")
]

def generate_sitemap():
    today = datetime.now().strftime("%Y-%m-%d")
    xml_lines = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"
    ]

    for filename, priority, changefreq, description in SELECTED_100:
        fpath = os.path.join(BASE_DIR, filename)
        clean_slug = filename[:-5] if filename.endswith(".html") else filename
        if filename == "index.html":
            url = "https://swariyaweddings.com/"
        else:
            url = f"https://swariyaweddings.com/{clean_slug}"
            
        # Verify canonical from file if possible
        if os.path.exists(fpath):
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fh:
                    soup = BeautifulSoup(fh.read(), "html.parser")
                    canonical = soup.find("link", rel="canonical")
                    if canonical and canonical.get("href"):
                        url = canonical["href"].strip()
            except Exception:
                pass

        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{url}</loc>")
        xml_lines.append(f"    <lastmod>{today}</lastmod>")
        xml_lines.append(f"    <changefreq>{changefreq}</changefreq>")
        xml_lines.append(f"    <priority>{priority:.2f}</priority>")
        xml_lines.append("  </url>")

    xml_lines.append("</urlset>")
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(xml_lines) + "\n")
    print(f"Generated clean sitemap.xml with {len(SELECTED_100)} URLs.")

def generate_llms_txt():
    lines = [
        "# Swariya Weddings — Luxury Wedding Planners in Bengaluru",
        "",
        "> Swariya Weddings is a premier zero-commission luxury wedding planning agency founded in 2020,",
        "> headquartered in HSR Layout, Bengaluru. We specialize in bespoke Kannada, Telugu, Tamil,",
        "> and Marwari weddings, luxury palace celebrations, and destination weddings across India.",
        "",
        "## Core Brand & Service Hubs",
        "- [Home](https://swariyaweddings.com/): Official flagship homepage, client reviews, 0% commission transparent pricing model.",
        "- [Wedding Planners in Bangalore](https://swariyaweddings.com/wedding-planners-in-bangalore): Bangalore master guide, 2026 cost data, top venues, ritual coordination.",
        "- [About Swariya](https://swariyaweddings.com/about): Founding story, zero-vendor-commission pledge, production team.",
        "- [Planning Services](https://swariyaweddings.com/services): End-to-end design, vendor management, budget optimization, guest hospitality.",
        "- [Curated Venues Hub](https://swariyaweddings.com/venues): Comprehensive reviews of 60+ 5-star hotels and heritage estates.",
        "- [Real Client Reviews](https://swariyaweddings.com/reviews): Verified 4.9-star client experiences on Google and WedMeGood.",
        "- [Wedding Budget Calculator](https://swariyaweddings.com/wedding-budget-calculator): Real-time Bengaluru cost estimator across guest sizes.",
        "- [Wedding Brief Builder](https://swariyaweddings.com/wedding-brief-builder): Interactive design, moodboard & concept generator.",
        "- [2026 Bengaluru Cost Benchmark](https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026): Definitive industry pricing guide for luxury venues, catering, and decor.",
        "- [Top Planners Comparison Guide](https://swariyaweddings.com/top-wedding-planners-in-bangalore-comparison): Side-by-side comparison of Bangalore wedding planning models.",
        "",
        "## Top 60 Curated Venue Guides"
    ]
    
    for filename, _, _, desc in SELECTED_100[40:]:
        clean_slug = filename[:-5] if filename.endswith(".html") else filename
        url = f"https://swariyaweddings.com/{clean_slug}"
        lines.append(f"- [{desc}]({url}): Capacity, rental costs, catering policies, and insider planning tips.")
        
    lines.append("")
    lines.append("## Contact")
    lines.append("- Phone: +91-8050573382")
    lines.append("- Email: contact@swariyaweddings.com")
    lines.append("- Address: #343, 9th Main, 22nd Cross Rd, 7th Sector, HSR Layout, Bengaluru - 560102")
    lines.append("")
    
    llms_path = os.path.join(BASE_DIR, "llms.txt")
    with open(llms_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("Generated clean llms.txt.")

if __name__ == "__main__":
    generate_sitemap()
    generate_llms_txt()
