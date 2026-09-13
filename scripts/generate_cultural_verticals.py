import json

CULTURAL_VERTICALS = [
    {
        "slug": "telugu-wedding-planner-bengaluru",
        "title": "Telugu Wedding Planner in Bengaluru | Traditional Andhra & Telangana Nuptials",
        "h1": "Telugu Wedding Planner in Bengaluru",
        "subtitle": "Authentic Telugu rituals, Pellikoothuru styling, Jeelakarra Bellam muhurtham precision & traditional Andhra Bhojanam hospitality.",
        "meta_desc": "Premier Telugu wedding planner in Bengaluru. Specializing in Jeelakarra Bellam, Talambralu, Pellikuthuru, mandap decor & authentic Andhra catering.",
        "rituals": [
            ("Pellikoothuru & Pellikoduku", "Pre-wedding holy mangala snanam, nalugu application, turmeric paste, and silk pattu saree styling with traditional floral jaada (braid)."),
            ("Kanyadaan & Mangalasutram", "Sacred fatherly offering, tying of the two golden sutrams (one from groom, one from maternal uncle), and the sacred Vedic agni prathistha."),
            ("Jeelakarra Bellam", "The core muhurtham moment: placing cumin and jaggery paste on each other's heads precisely at the auspicious second to symbolize inseparable union."),
            ("Talambralu", "Joyous and vibrant showering of pearls, turmeric-infused rice, and rose petals celebrating mutual respect and prosperity."),
            ("Saptapadi & Arundhati Darshanam", "Seven sacred steps around the holy fire followed by viewing the eternal twin stars symbolizing marital devotion.")
        ],
        "faqs": [
            ("Why hire Swariya Weddings for a Telugu wedding in Bengaluru?", "Swariya Weddings has planned 40+ traditional Telugu weddings across Bengaluru, with deep mastery over Vedic muhurtham timing, authentic priest coordination, floral jada styling, and authentic multi-course Andhra feasts."),
            ("Can you organize authentic Andhra Bhojanam on plantain leaves?", "Yes, we partner with premier vegetarian Telugu vanta masters to serve authentic Gongura, Avakaya, Pappu Charu, Pulihora, Poornam Boorelu, and Bobbatlu on fresh banana leaves."),
            ("Which venues in Bengaluru suit traditional Telugu weddings best?", "Venues like Gayatri Vihar Palace Grounds, The Tamarind Tree, Wiwaha, and Miraya Greens offer the grand scale and traditional ambiance ideal for Telugu mandaps and 500–1,500 guests.")
        ]
    },
    {
        "slug": "tamil-wedding-planner-bengaluru",
        "title": "Tamil Wedding Planner in Bengaluru | Iyer & Iyengar Wedding Specialists",
        "h1": "Tamil Wedding Planner in Bengaluru",
        "subtitle": "Mastery in traditional Tamil Brahmin & non-Brahmin rituals: Oonjal swing ceremonies, Kashi Yatra, Kanyadaanam & South Indian catering.",
        "meta_desc": "Expert Tamil wedding planner in Bengaluru. Iyer, Iyengar & Chettinad rituals, Oonjal swing decor, Nadaswaram ensembles & authentic plantain leaf Sadya.",
        "rituals": [
            ("Vratham & Janavasam", "Pre-nuptial fasts, ancestral blessings, and the grand evening car/chariot procession welcoming the groom with live Nadaswaram."),
            ("Kashi Yatra", "The symbolic bachelor journey to Kashi before being persuaded by the bride's father to embrace Grihastha (family life)."),
            ("Oonjal (Swing Ceremony)", "The couple is seated on an ornate decorated wooden swing while women sing traditional Oonjal songs, ward off evil spirits, and offer milk & plantains."),
            ("Kanyadaanam & Thirumangalyam", "Placing the sacred Koora saree in the bride's lap and tying the auspicious Mangalsutra to the crescendo of the 'Kettimelam' drum roll."),
            ("Saptapadi & Pori Idal", "The seven sacred steps around the sacred fire followed by offering puffed rice into the Agni for abundance and health.")
        ],
        "faqs": [
            ("Do you handle early morning 4:30 AM – 6:00 AM Brahma Muhurthams?", "Yes! Our production and hospitality crew operates 24/7 on wedding days to ensure fresh jasmine (Malli) garlands, hot filter coffee, and priest setups are ready by 3:30 AM."),
            ("Can Swariya Weddings arrange live carnatic music and Nadaswaram?", "Yes, we coordinate renowned temple Nadaswaram vidwans, Chenda Melam artists, and Carnatic acoustic ensembles for classical resonance."),
            ("What catering arrangements are made for Tamil weddings?", "We curate authentic Tamil Samayal spreads including fresh Filter Kaapi, Medu Vada, Pongal, Mor Kuzhambu, Mysore Pak, and Elai Sapadu on banana leaves.")
        ]
    },
    {
        "slug": "marwari-wedding-planner-bengaluru",
        "title": "Marwari Wedding Planner in Bengaluru | Royal Grandeur & Traditional Customs",
        "h1": "Marwari Wedding Planner in Bengaluru",
        "subtitle": "Opulent Rajasthani heritage, Mudha Tikka, high-energy Sangeet choreography, Royal Baaraat & grand multi-cuisine banqueting.",
        "meta_desc": "Leading Marwari wedding planner in Bengaluru. High-scale Rajasthani weddings, Tilak, Mayaira, Sangeet production, Royal Baaraat & 1,000+ guest hospitality.",
        "rituals": [
            ("Mudha Tikka & Godh Bharai", "Formal engagement and blessings with silver thaalis, traditional dry fruits, and bespoke Marwari sweet hampers."),
            ("Bhaat / Mayaira", "Emotional welcoming of maternal uncles bearing exquisite wedding gifts, silks, and jewelry in a vibrant musical ceremony."),
            ("Mehfil & Grand Sangeet", "High-energy musical extravaganzas with custom LED stages, celebrity DJs, professional Rajasthani folk dancers (Ghoomar), and choreographed performances."),
            ("Royal Baaraat & Toran", "Majestic groom procession with vintage convertibles or royal horses, live Dhol tasha, cold pyrotechnics, and the auspicious striking of the Toran."),
            ("Varmala & 4 Pheras", "Grand thematic revolving or floating Varmala stage followed by the traditional 4 pheras around the holy fire.")
        ],
        "faqs": [
            ("How does Swariya manage 1,000+ guest scale for Marwari weddings?", "We deploy dedicated hospitality managers, RSVP desks, luggage & room concierge, multi-counter pure vegetarian and Jain culinary zones, and separate valet routes."),
            ("Can you cater 100% Pure Vegetarian and Jain gourmet spreads?", "Yes, we partner with top royal Maharaj caterers to deliver authentic Dal Baati Churma, Ker Sangri, Gatte ki Sabzi, live Chaat bazaars, and 50+ dessert buffets."),
            ("Which venues are best for Marwari weddings in Bangalore?", "Gayatri Vihar (Palace Grounds), The Moongate, Miraya Greens, and JW Marriott Bengaluru offer the immense scale and luxury required for royal Marwari celebrations.")
        ]
    },
    {
        "slug": "nri-destination-wedding-planner-bangalore",
        "title": "NRI Destination Wedding Planner in Bangalore | 100% Remote Coordination",
        "h1": "NRI Destination Wedding Planner in Bangalore",
        "subtitle": "Seamless cross-timezone wedding planning for couples living in USA, UK, UAE, Europe, Singapore & Australia returning home to Bengaluru.",
        "meta_desc": "Top NRI wedding planner in Bangalore. Remote timezone planning, 3D visual walkthroughs, airport concierge, 5-star hotel room blocks & currency transparency.",
        "rituals": [
            ("Timezone-Synchronized Planning", "Dedicated Zoom & WhatsApp milestone reviews timed to your local working hours (PST, EST, GMT, GST, SGT, AEST)."),
            ("3D Digital Layouts & Moodboards", "Virtual walkthroughs of venue floor plans, mandap floral renders, and lighting schemes before you board your flight."),
            ("End-to-End Guest Concierge", "Kempegowda International Airport (BLR) welcome desks, private AC luxury shuttles, personalized welcome hampers, and hotel check-in desks."),
            ("Multi-Currency Budget Accounting", "Transparent INR budgets with live USD/GBP/AED/EUR equivalencies, itemized invoices, zero vendor markup, and secure payment processing."),
            ("Bridal & Groom Wardrobe Assistance", "Curated shopping appointments in Commercial Street, Indiranagar, and Jayanagar with pre-booked master tailors for instant alterations.")
        ],
        "faqs": [
            ("Can we plan our entire Bangalore wedding without visiting India before the week of the wedding?", "Yes! Over 40% of our couples plan 100% remotely. We handle venue inspections via live video calls, food tastings with local relatives, and complete digital approvals."),
            ("How do you manage airport arrivals for 100+ international guests?", "Our logistics team sets up branded welcome desks at BLR Airport Terminal 1 & 2, manages luggage handling, and dispatches luxury Mercedes/Innova fleets to partner hotels."),
            ("What payment methods and currency invoicing do you support?", "We provide transparent, itemized invoicing with direct wire transfer, international cards, and zero hidden markups.")
        ]
    }
]

for c in CULTURAL_VERTICALS:
    faq_schema = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        } for q, a in c["faqs"]
    ]

    rituals_html = "\n".join([f"""
                <div class="ritual-card">
                    <h3 class="ritual-name">✨ {name}</h3>
                    <p class="ritual-desc">{desc}</p>
                </div>""" for name, desc in c["rituals"]])

    faqs_html = "\n".join([f"""
                <div class="faq-card">
                    <h3 class="faq-q">{q}</h3>
                    <p class="faq-a">{a}</p>
                </div>""" for q, a in c["faqs"]])

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"https://swariyaweddings.com/{c['slug']}.html#service",
                "name": c["title"],
                "description": c["meta_desc"],
                "url": f"https://swariyaweddings.com/{c['slug']}.html",
                "provider": {
                    "@type": "ProfessionalService",
                    "name": "Swariya Weddings",
                    "url": "https://swariyaweddings.com/",
                    "telephone": "+91-9606822204"
                },
                "areaServed": {"@type": "City", "name": "Bengaluru"}
            },
            {
                "@type": "FAQPage",
                "@id": f"https://swariyaweddings.com/{c['slug']}.html#faq",
                "mainEntity": faq_schema
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"https://swariyaweddings.com/{c['slug']}.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://swariyaweddings.com/"},
                    {"@type": "ListItem", "position": 2, "name": c["h1"], "item": f"https://swariyaweddings.com/{c['slug']}.html"}
                ]
            }
        ]
    }, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']}</title>
    <meta name="description" content="{c['meta_desc']}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="https://swariyaweddings.com/{c['slug']}.html">

    <!-- Open Graph -->
    <meta property="og:title" content="{c['title']}">
    <meta property="og:description" content="{c['subtitle']}">
    <meta property="og:url" content="https://swariyaweddings.com/{c['slug']}.html">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://swariyaweddings.com/apple-touch-icon.png">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">

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
        .hero-banner {{ padding: 130px 20px 60px; background: linear-gradient(135deg, #fdf0f4 0%, #fffbf2 100%); text-align: center; border-bottom: 1px solid #f0e2e7; }}
        .hero-banner h1 {{ font-size: 2.8rem; margin-bottom: 15px; }}
        .hero-banner .subtitle {{ font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto 20px; }}
        
        .container {{ max-width: 1140px; margin: 0 auto; padding: 0 20px; }}
        .grid-layout {{ display: grid; grid-template-columns: 2fr 1fr; gap: 40px; margin-top: 40px; }}
        @media (max-width: 850px) {{ .grid-layout {{ grid-template-columns: 1fr; }} }}

        .content-card {{ background: var(--white); border-radius: var(--border-radius); padding: 30px; box-shadow: var(--card-shadow); border: 1px solid #f0eae5; margin-bottom: 30px; }}
        .ritual-card {{ background: #fdfbf7; border-left: 4px solid var(--accent); padding: 18px 22px; margin-bottom: 15px; border-radius: 0 8px 8px 0; }}
        .ritual-name {{ font-size: 1.25rem; margin-bottom: 6px; }}
        .ritual-desc {{ font-size: 0.96rem; color: #555; margin: 0; }}

        .faq-card {{ background: var(--white); border-radius: var(--border-radius); padding: 22px; margin-bottom: 15px; box-shadow: var(--card-shadow); border-left: 4px solid var(--primary); }}
        .faq-q {{ font-size: 1.2rem; margin-bottom: 8px; font-weight: 700; }}
        .faq-a {{ font-size: 0.98rem; color: #444; margin: 0; }}

        .lead-box {{ background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); color: white; padding: 30px; border-radius: var(--border-radius); box-shadow: var(--card-shadow); position: sticky; top: 100px; }}
        .lead-box h3 {{ color: white; margin-bottom: 10px; font-size: 1.6rem; }}
        .btn-whatsapp {{ display: flex; align-items: center; justify-content: center; gap: 10px; background: #25d366; color: white; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 700; font-size: 1rem; margin-top: 20px; }}
        .btn-whatsapp:hover {{ background: #1eb956; }}
    </style>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <header class="header">
        <div class="container nav-container">
            <a href="index.html" class="logo">
                <span class="logo-main">Swariya</span>
                <span class="logo-sub">Weddings</span>
            </a>
            <nav class="nav-menu">
                <a href="index.html" class="nav-link">Home</a>
                <a href="about.html" class="nav-link">About</a>
                <a href="services.html" class="nav-link">Services</a>
                <a href="venues.html" class="nav-link">Venues</a>
                <a href="bengaluru-wedding-cost-guide-2026.html" class="nav-link">Cost Guide 2026</a>
                <a href="ask.html" class="nav-link">Ask Q&A</a>
                <a href="reviews.html" class="nav-link">Reviews</a>
                <a href="contact.html" class="btn-primary">Plan Your Wedding</a>
            </nav>
        </div>
    </header>

    <div class="hero-banner">
        <div class="container">
            <h1>{c['h1']}</h1>
            <p class="subtitle">{c['subtitle']}</p>
        </div>
    </div>

    <main class="container">
        <div class="grid-layout">
            <div class="main-content">
                <div class="content-card">
                    <h2>Sacred Rituals & Tradition Management</h2>
                    <p>At <strong>Swariya Weddings</strong>, we honor the sacred cultural significance of every tradition. With over <strong>150+ weddings crafted across Bengaluru</strong>, our dedicated ritual coordinators work directly with high priests (Purohits/Vadhyars), family elders, and master artisans.</p>
                    <div style="margin-top:20px;">
                        {rituals_html}
                    </div>
                </div>

                <div class="content-card">
                    <h2>Frequently Asked Questions</h2>
                    {faqs_html}
                </div>
            </div>

            <aside class="sidebar">
                <div class="lead-box">
                    <h3>Plan Your Celebration</h3>
                    <p>Schedule a customized consultation with our senior ritual and venue specialists in Bengaluru.</p>
                    <a href="https://wa.me/919606822204?text=Hi%20Swariya%20Weddings,%20I%20would%20like%20to%20inquire%20about%20{c['h1'].replace(' ', '%20')}." class="btn-whatsapp" target="_blank" rel="noopener">
                        <span>💬 WhatsApp Consultation</span>
                    </a>
                </div>
            </aside>
        </div>
    </main>

    <footer class="footer" style="background:#1a1a1a; color:#fff; padding:60px 0 30px; margin-top:80px;">
        <div class="container" style="text-align:center;">
            <p><strong>Swariya Weddings</strong> — Premier Wedding Planners in Bengaluru. 150+ Weddings | 500+ Happy Clients | 4.9/5 Rating.</p>
            <p style="font-size:0.9rem; color:#aaa;">© 2026 Swariya Weddings. All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>"""

    with open(f"{c['slug']}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Cultural Vertical: {c['slug']}.html")

print("All 4 Cultural & Audience Verticals generated successfully!")
