import os
import json

OUTPUT_DIR = "/Users/mac/Documents/swariya-weddings-complete-project"

PAN_INDIA_PILLARS = [
    {
        "city": "Goa",
        "slug": "wedding-planners-in-goa",
        "title": "Wedding Planners in Goa | Luxury Beach Weddings | Swariya",
        "h1": "Luxury Wedding Planners in Goa & Beachfront Celebrations",
        "meta_desc": "Looking for the best wedding planners in Goa? Swariya Weddings crafts turnkey beachfront celebrations across North & South Goa luxury resorts with 0% markups.",
        "desc": "From pristine white sand beaches in South Goa (Cavelossim, Benaulim, Majorda) to vibrant clifftop bohemian sunsets in North Goa (Vagator, Anjuna, Ashwem), Swariya Weddings delivers seamless turnkey beach wedding planning with in-house mandap fabrication and 0% vendor markups.",
        "fee_range": "₹3.5L - ₹8L",
        "venues": ["The Leela Goa (Cavelossim)", "Taj Exotica Resort & Spa (Benaulim)", "W Goa (Vagator)", "Grand Hyatt Goa (Bambolim)", "ITC Grand Goa (Arossim)", "Alila Diwa Goa (Majorda)", "The St. Regis Goa Resort (Mobor)"],
        "faqs": [
            {"q": "What is the average cost of a destination wedding in Goa?", "a": "A 2 to 3-day luxury destination wedding in Goa for 100-150 guests typically ranges from ₹30 Lakhs to ₹75 Lakhs including 5-star beachfront resort stay, curated meals, beach permits, sound clearances, and turnkey decor."},
            {"q": "Do we need CRZ permissions for beach wedding mandaps in Goa?", "a": "Yes, beach ceremonies require coastal regulation clearances and police/sound permissions. Swariya Weddings manages all government permits and sound cutoff protocols directly."},
            {"q": "What is the best season for a beach wedding in Goa?", "a": "November through March offers ideal balmy coastal weather with clear skies and spectacular sunsets. October and April are great for shoulder-season luxury resort deals."}
        ]
    },
    {
        "city": "Udaipur",
        "slug": "wedding-planners-in-udaipur",
        "title": "Wedding Planners in Udaipur | Royal Palace Weddings | Swariya",
        "h1": "Royal Wedding Planners in Udaipur | Lake & Palace Celebrations",
        "meta_desc": "Plan your dream royal palace wedding in Udaipur with Swariya Weddings. Luxury lakeside decor, Jagmandir & Oberoi Udaivilas coordination & 0% markups.",
        "desc": "The City of Lakes is the pinnacle of regal Indian destination weddings. Swariya Weddings executes breathtaking royal celebrations across Lake Pichola, private island palaces, and heritage forts with authentic Rajasthani hospitality, royal royal baraat coordination, and transparent 0% vendor markups.",
        "fee_range": "₹4L - ₹10L",
        "venues": ["The Oberoi Udaivilas", "Taj Lake Palace", "Jagmandir Island Palace", "The Leela Palace Udaipur", "Fateh Prakash Palace", "Shiv Niwas Palace", "Raffles Udaipur"],
        "faqs": [
            {"q": "How much does a royal destination wedding cost in Udaipur?", "a": "A 3-day palace wedding in Udaipur for 100 to 200 guests generally ranges from ₹45 Lakhs to ₹1.5+ Crores depending on whether you choose heritage palace grounds or 5-star luxury lakefront resorts."},
            {"q": "How do boat transfers work for Jagmandir Island Palace weddings?", "a": "Swariya Weddings coordinates private royal jetty transfers from City Palace for all guests, with welcome folk musicians and luggage logistics on dedicated supply boats."},
            {"q": "Can you arrange traditional royal Rajasthani welcome and folk artists?", "a": "Yes, we curate authentic Kalbelia dancers, Langa musicians, royal elephant/horse baraats, fire dancers, and customized Mewari royal feasts."}
        ]
    },
    {
        "city": "Jaipur",
        "slug": "wedding-planners-in-jaipur",
        "title": "Wedding Planners in Jaipur | Grand Heritage Forts | Swariya",
        "h1": "Luxury Wedding Planners in Jaipur | Fort & Palace Celebrations",
        "meta_desc": "Top wedding planners in Jaipur for grand heritage fort and palace weddings. Fairmont, Rambagh Palace & Samode Palace specialists with 0% vendor markups.",
        "desc": "Celebrate your love story amidst royal sandstone courtyards, majestic fortresses, and palatial ballrooms in the Pink City. Swariya Weddings brings master-level architectural decor fabrication, celebrity entertainment, and end-to-end luxury management across Jaipur's most prestigious royal venues.",
        "fee_range": "₹4L - ₹10L",
        "venues": ["Fairmont Jaipur (Kukas)", "Rambagh Palace (Jaipur Central)", "JW Marriott Jaipur Resort & Spa", "The Oberoi Rajvilas", "Samode Palace & Bagh", "Alila Fort Bishangarh", "ITC Rajputana"],
        "faqs": [
            {"q": "What is the typical budget for a luxury wedding in Jaipur?", "a": "A 3-day destination wedding in Jaipur for 150-250 guests typically ranges from ₹40 Lakhs to ₹1.2 Crores covering luxury accommodations, fort banquets, Royal Sangeet production, and grand Jai Mala staging."},
            {"q": "Are fireworks and late-night music allowed in Jaipur heritage venues?", "a": "Most palace venues permit outdoor music till 10:00 PM and transition to soundproof indoor royal ballrooms for after-parties. Cold pyro and aerial fireworks are coordinated with local authorities."},
            {"q": "How do you manage guest transport across Jaipur?", "a": "We operate a dedicated luxury fleet with uniformed drivers, airport welcome desks at Jaipur International Airport, and scheduled shuttles to fort venues."}
        ]
    },
    {
        "city": "Mumbai",
        "slug": "wedding-planners-in-mumbai",
        "title": "Wedding Planners in Mumbai | Top Luxury Planners | Swariya",
        "h1": "Premier Wedding Planners in Mumbai & Alibaug Destinations",
        "meta_desc": "Looking for top wedding planners in Mumbai? Swariya Weddings delivers high-production luxury weddings, 3D decor renders & 0% markups across Mumbai & Alibaug.",
        "desc": "From grand ballrooms overlooking the Arabian Sea in South Mumbai and Bandra to exclusive private sea-facing villa estates in Alibaug, Swariya Weddings provides world-class turnkey production, celebrity artist curation, and flawless logistical management for Mumbai's discerning couples.",
        "fee_range": "₹4L - ₹10L",
        "venues": ["The Taj Mahal Palace (Colaba)", "The St. Regis Mumbai (Lower Parel)", "Taj Lands End (Bandra West)", "JW Marriott Mumbai Juhu", "Four Seasons Hotel Mumbai", "The Oberoi Mumbai", "Alibaug Luxury Beachfront Villas"],
        "faqs": [
            {"q": "What are wedding planning costs in Mumbai?", "a": "Turnkey wedding management in Mumbai starts from ₹3.5L for day-of coordination to ₹6L–₹12L for multi-day luxury productions with 0% vendor markups."},
            {"q": "Do you plan speedboat transfers and villa buyouts in Alibaug?", "a": "Yes! We manage Ro-Pax ferry and private speedboat charters from Gateway of India to Mandwa, alongside full estate staging and guest hospitality in Alibaug."},
            {"q": "Can Swariya handle high-profile celebrity and corporate guest management?", "a": "Yes, our team has extensive experience managing VIP security protocol, NDAs, personalized concierge desks, and private green rooms for artists."}
        ]
    },
    {
        "city": "Delhi NCR",
        "slug": "wedding-planners-in-delhi",
        "title": "Wedding Planners in Delhi NCR | Grand Luxury Weddings | Swariya",
        "h1": "Grand Wedding Planners in Delhi NCR, Gurgaon & Neemrana",
        "meta_desc": "Top luxury wedding planners in Delhi NCR. Turnkey 3D decor, Aerocity 5-star ballrooms, grand farmhouse weddings & 0% hidden markups.",
        "desc": "Delhi NCR is legendary for its grandeur, opulent farmhouse setups, and world-class 5-star hospitality. Swariya Weddings executes breathtaking mega-productions across South Delhi farmhouses, Aerocity luxury hotel corridors, Gurgaon golf retreats, and Neemrana Fort.",
        "fee_range": "₹4L - ₹10L",
        "venues": ["The Leela Palace New Delhi (Chanakyapuri)", "ITC Grand Bharat (Gurgaon)", "JW Marriott Hotel New Delhi Aerocity", "The Oberoi Gurgaon", "Neemrana Fort-Palace", "Tivoli Grand Resort", "Chattarpur Luxury Farmhouses"],
        "faqs": [
            {"q": "How do you coordinate large-scale farmhouse weddings in South Delhi / Chattarpur?", "a": "We handle total infrastructure buildouts: custom weatherproof German hangar tents, mega air-conditioning plants, 360-degree LED stage production, and dedicated valet parking teams for 1,000+ cars."},
            {"q": "What are your wedding planner fees in Delhi NCR?", "a": "Our turnkey management fee ranges from ₹3.5L to ₹8L with transparent zero-commission pricing, passing all bulk vendor discounts directly to you."},
            {"q": "Do you manage both North Indian and cross-cultural ceremonies in Delhi?", "a": "Yes! We coordinate traditional Punjabi, Marwari, UP, Bengali, and fusion ceremonies with authentic priests and custom-themed decor."}
        ]
    },
    {
        "city": "Hyderabad",
        "slug": "wedding-planners-in-hyderabad",
        "title": "Wedding Planners in Hyderabad | Royal Nizam Palaces | Swariya",
        "h1": "Royal Wedding Planners in Hyderabad | Falaknuma & Luxury Banquets",
        "meta_desc": "Top royal wedding planners in Hyderabad. Taj Falaknuma Palace, ITC Kohenur & luxury Banjara Hills weddings with 0% vendor markups.",
        "desc": "From the 101-seat dining table grandeur of Taj Falaknuma Palace to contemporary luxury ballrooms in HITEC City and Banjara Hills, Swariya Weddings provides unmatched royal Telugu, Hyderabadi, and destination wedding management with in-house 3D decor fabrication.",
        "fee_range": "₹3.5L - ₹8L",
        "venues": ["Taj Falaknuma Palace", "ITC Kohenur (HITEC City)", "Taj Krishna (Banjara Hills)", "Novotel Hyderabad Convention Centre", "Park Hyatt Hyderabad", "Fort Grand Shamshabad", "Golconda Resorts & Spa"],
        "faqs": [
            {"q": "How much does a royal wedding at Taj Falaknuma Palace cost?", "a": "A signature 2-day royal celebration at Taj Falaknuma Palace typically ranges from ₹60 Lakhs to ₹1.8 Crores including palace rooms, royal horse carriage entries, and 7-course Nizami feasts."},
            {"q": "Do you handle traditional Telugu wedding rituals in Hyderabad?", "a": "Yes, we specialize in authentic Telugu ceremonies: Pellikuthuru, Snathakam, Jeelakarra Bellam, Talambralu, and authentic Andhra/Telangana culinary banquets."},
            {"q": "What is Swariya's vendor pricing policy in Hyderabad?", "a": "We operate with a strict 0% vendor markup guarantee. You pay actual vendor costs directly and get itemized transparent invoicing."}
        ]
    },
    {
        "city": "Chennai",
        "slug": "wedding-planners-in-chennai",
        "title": "Wedding Planners in Chennai | ECR Beach & Heritage | Swariya",
        "h1": "Luxury Wedding Planners in Chennai & ECR Coastal Celebrations",
        "meta_desc": "Top wedding planners in Chennai & ECR beach resorts. Traditional Tamil Brahmin, Chettinad & beachside mandaps with 0% vendor markups.",
        "desc": "From historic East Coast Road (ECR) beach resorts in Mahabalipuram to majestic luxury city hotels in Guindy and Nungambakkam, Swariya Weddings crafts traditional Tamil Brahmin, Chettiar, and contemporary coastal fusion weddings with pristine Vedic authenticity and 0% markups.",
        "fee_range": "₹3.5L - ₹7L",
        "venues": ["ITC Grand Chola (Guindy)", "Taj Fisherman's Cove Resort & Spa (ECR)", "The Leela Palace Chennai", "InterContinental Chennai Mahabalipuram Resort", "Sheraton Grand Chennai Resort & Spa", "Taj Coromandel", "MGM Beach Resorts ECR"],
        "faqs": [
            {"q": "What is the cost of a beach wedding along ECR Chennai / Mahabalipuram?", "a": "A 2-day beach destination wedding on ECR for 100-150 guests typically ranges from ₹25 Lakhs to ₹55 Lakhs including sea-facing resort rooms, lawn mandap, and multi-cuisine catering."},
            {"q": "Do you specialize in authentic Tamil Brahmin (Iyer/Iyengar) and Chettinad weddings?", "a": "Yes! We coordinate complete Nadaswaram troupes, Oonjal swings, Vratham arrangements, Kanyadaanam protocols, and traditional banana leaf feasts with master caterers."},
            {"q": "Can you design indoor air-conditioned mandaps for hot summer months?", "a": "Yes, we provide fully air-conditioned pillarless glasshouse and dome structures for comfortable daytime Muhurtham ceremonies."}
        ]
    },
    {
        "city": "Kerala",
        "slug": "wedding-planners-in-kerala",
        "title": "Wedding Planners in Kerala | Backwater & Clifftop | Swariya",
        "h1": "Destination Wedding Planners in Kerala | Backwaters & Beach Resorts",
        "meta_desc": "Plan your dream destination wedding in Kerala with Swariya Weddings. Kumarakom backwaters, Kovalam clifftops, Kochi heritage & 0% markups.",
        "desc": "Experience God's Own Country for your dream destination wedding. Swariya Weddings designs enchanting backwater ceremonies in Kumarakom, clifftop sunset vows in Kovalam, and historic colonial weddings in Fort Kochi with traditional houseboats, Kathakali artists, and 0% vendor markups.",
        "fee_range": "₹3.5L - ₹8L",
        "venues": ["Kumarakom Lake Resort", "The Leela Kovalam, A Raviz Hotel", "Grand Hyatt Kochi Bolgatty", "Taj Malabar Resort & Spa (Cochin)", "Taj Green Cove Resort & Spa (Kovalam)", "Brunton Boatyard (Fort Kochi)", "Niraamaya Surya Samudra (Kovalam)"],
        "faqs": [
            {"q": "What is the cost of a backwater destination wedding in Kumarakom / Alleppey?", "a": "A 2 to 3-day luxury backwater wedding in Kerala for 80-150 guests generally ranges from ₹25 Lakhs to ₹60 Lakhs including luxury resort cottage stays, houseboat cruises, and authentic Sadya catering."},
            {"q": "Can we arrange a houseboat pre-wedding sunset cruise for our guests?", "a": "Yes! Swariya arranges customized luxury double-decker houseboats with live Kerala musicians, tender coconut bars, and traditional coastal appetizers."},
            {"q": "Do you coordinate Kerala Christian (Syrian Catholic / Orthodox) and Nair ceremonies?", "a": "Yes, we manage Manthrakodi rituals, Minnu tying, church choirs, and traditional Nair Thalikettu ceremonies with authentic Nilavilakku setups."}
        ]
    },
    {
        "city": "Pan-India",
        "slug": "destination-wedding-planner-in-india",
        "title": "Destination Wedding Planner in India | Top Luxury Agency | Swariya",
        "h1": "Premier Destination Wedding Planner in India | 150+ Celebrations",
        "meta_desc": "Looking for the top destination wedding planner in India? Swariya Weddings executes luxury weddings across Goa, Rajasthan, Kerala & Bangalore with 0% markups.",
        "desc": "Headquartered in Bengaluru with operational nationwide hubs across Goa, Udaipur, Jaipur, Mumbai, Delhi, Hyderabad, Chennai, and Kerala. With 150+ luxury destination weddings planned and 500+ couples served, Swariya Weddings provides turnkey 3D design, strict 0% vendor markups, and end-to-end guest concierge.",
        "fee_range": "₹4L - ₹12L",
        "venues": ["Rajasthan Royal Palaces (Udaipur, Jaipur, Jodhpur)", "Goa Beachfront 5-Star Resorts", "Kerala Backwaters & Clifftops", "Bangalore Heritage Grounds & Golf Resorts", "Coorg & Chikmagalur Coffee Plantations", "Jim Corbett & Mussoorie Mountain Ridges"],
        "faqs": [
            {"q": "How does Swariya manage destination weddings across different states in India?", "a": "We maintain pre-negotiated direct partnerships with 200+ 5-star luxury venues across India. Our core senior director and technical decor crew travels to your chosen destination to oversee on-ground production and logistics."},
            {"q": "What is the 0% vendor markup guarantee?", "a": "Unlike traditional middleman agencies that inflate vendor quotes by 20–40%, Swariya passes 100% of vendor bills directly to you with zero hidden commissions. You only pay our flat, agreed management fee."},
            {"q": "Do you provide full hospitality and airport transfer logistics for NRI weddings?", "a": "Yes! We specialize in NRI destination weddings, providing 24/7 RSVP desks, airport fleet dispatch, bespoke welcome hampers, and multi-camera 4K live streaming for family worldwide."}
        ]
    }
]

def generate_pillar_html(pillar):
    city = pillar["city"]
    slug = pillar["slug"]
    title = pillar["title"]
    h1 = pillar["h1"]
    meta_desc = pillar["meta_desc"]
    desc = pillar["desc"]
    fee_range = pillar["fee_range"]
    venues = pillar["venues"]
    faqs = pillar["faqs"]
    canonical_url = f"https://swariyaweddings.com/{slug}"

    local_schema = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{canonical_url}#service",
        "name": f"Swariya Weddings - {title}",
        "url": canonical_url,
        "image": "https://swariyaweddings.com/images/16.jpg",
        "telephone": "+91-8050573382",
        "priceRange": "₹₹₹",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "HSR Layout Sector 2",
            "addressLocality": "Bengaluru",
            "addressRegion": "Karnataka",
            "postalCode": "560102",
            "addressCountry": "IN"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "500"
        }
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"]
                }
            } for item in faqs
        ]
    }

    venues_list_html = "".join([f'<li style="margin-bottom: 8px; font-weight: 500; color: #2C2C2C;">🏛️ {v}</li>' for v in venues])

    html = f"""<!DOCTYPE html>
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

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Swariya Weddings">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="https://swariyaweddings.com/images/16.jpg">
    <meta property="og:locale" content="en_IN">

    <!-- Schema Structured Data -->
    <script type="application/ld+json">
    {json.dumps(local_schema, indent=4)}
    </script>
    <script type="application/ld+json">
    {json.dumps(faq_schema, indent=4)}
    </script>

    <style>
        .pillar-hero {{ background: linear-gradient(135deg, #FAF7F2 0%, #F5EFEB 100%); padding: 60px 0 40px; border-bottom: 1px solid #EBE4D8; }}
        .pricing-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin: 30px 0; }}
        .pricing-card {{ background: #fff; border: 1px solid #EBE4D8; border-radius: 8px; padding: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }}
        .pricing-card.featured {{ border: 2px solid #8B1A1A; position: relative; }}
        .pricing-card.featured::before {{ content: "MOST POPULAR"; position: absolute; top: -12px; right: 20px; background: #8B1A1A; color: #fff; font-size: 11px; padding: 2px 10px; font-weight: 600; border-radius: 12px; }}
        .pricing-card h3 {{ font-family: 'Playfair Display', serif; font-size: 20px; color: #2C2C2C; margin-bottom: 8px; }}
        .pricing-card .price {{ font-size: 26px; font-weight: 700; color: #8B1A1A; margin-bottom: 12px; }}
        .pricing-card ul {{ list-style: none; padding: 0; margin: 0 0 20px; font-size: 14px; line-height: 1.8; color: #555; }}
        .pricing-card ul li::before {{ content: "✓ "; color: #2E7D32; font-weight: bold; }}
        .content-box {{ background: #fff; border: 1px solid #EBE4D8; border-radius: 8px; padding: 32px; margin: 30px 0; }}
        .faq-accordion {{ margin: 30px 0; }}
        .faq-item {{ border: 1px solid #EBE4D8; border-radius: 6px; margin-bottom: 12px; overflow: hidden; background: #fff; }}
        .faq-item h4 {{ padding: 18px 24px; margin: 0; font-size: 16px; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: #2C2C2C; }}
        .faq-item .faq-ans {{ padding: 0 24px 18px; color: #555; font-size: 14px; line-height: 1.7; display: block; }}
        .venue-grid-box {{ background: #FAF7F2; border: 1px solid #EBE4D8; border-radius: 8px; padding: 24px; margin: 24px 0; }}
    </style>
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PGH8WNPW"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <nav class="navbar">
        <div class="container">
            <div class="logo"><a href="/">SWARIYA</a></div>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/about">About Us</a></li>
                <li><a href="/wedding-planners-in-bangalore">Bangalore Hub</a></li>
                <li><a href="/destination-wedding-planner-in-india">Pan-India Destinations</a></li>
                <li><a href="/top-wedding-planners-in-bangalore-comparison">Compare Planners</a></li>
                <li><a href="/reviews">Reviews</a></li>
                <li><a href="/contact" class="btn-contact">Get Free Quote</a></li>
            </ul>
        </div>
    </nav>

    <header class="pillar-hero">
        <div class="container">
            <p class="section-label" style="color: #8B1A1A; font-weight: 600;">✦ PAN-INDIA LUXURY WEDDING DIRECTORS</p>
            <h1 style="font-family: 'Playfair Display', serif; font-size: 38px; color: #2C2C2C; margin: 12px 0 16px; line-height: 1.2;">{h1}</h1>
            <p style="font-size: 16px; color: #555; max-width: 820px; line-height: 1.7;">{desc}</p>
            <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 24px;">
                <a href="#quote" class="btn-primary">Book Consultation Call</a>
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I%20am%20planning%20a%20wedding%20in%20{city.replace(' ', '%20')}" class="btn-primary" style="background: #25D366; border-color: #25D366;">WhatsApp Senior Director 💬</a>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Trust Metrics -->
        <section class="content-box">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; text-align: center;">
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">0%</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Vendor Commissions or Kickbacks</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">4.9 ★</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Rated by 500+ Couples Nationwide</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">150+</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Destination Celebrations Executed</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">100%</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Photorealistic 3D Decor Renders</p>
                </div>
            </div>
        </section>

        <!-- Top Venues -->
        <section class="venue-grid-box">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 24px; color: #2C2C2C; margin-bottom: 16px;">Top Luxury Venues & Resorts Managed in {city}</h2>
            <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 10px;">
                {venues_list_html}
            </ul>
        </section>

        <!-- Pricing Tiers -->
        <section style="margin: 40px 0;">
            <div style="text-align: center; margin-bottom: 30px;">
                <p class="section-label">✦ 2026 TRANSPARENT FEE STRUCTURE</p>
                <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #2C2C2C;">Turnkey Planning & Management Tiers</h2>
                <p style="color: #666; max-width: 650px; margin: 8px auto 0;">Enjoy full fiduciary transparency with direct-to-vendor billing and in-house technical production.</p>
            </div>

            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>Day-Of Production Coordination</h3>
                    <div class="price">₹1.5 - ₹2.5 Lakhs <span style="font-size: 14px; font-weight: 400; color: #777;">/ 1-2 Days</span></div>
                    <ul>
                        <li>Full vendor contract & runsheet alignment</li>
                        <li>Shadow managers for Bride, Groom & Parents</li>
                        <li>Seating & guest reception management</li>
                        <li>Priest, samagri & ritual flow synchronization</li>
                        <li>Audio/Visual & DJ cue management</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Inquire Now</a>
                </div>

                <div class="pricing-card featured">
                    <h3>Turnkey Destination Execution</h3>
                    <div class="price">{fee_range} <span style="font-size: 14px; font-weight: 400; color: #777;">/ Multi-Day</span></div>
                    <ul>
                        <li>Complete 3D decor renders & spatial layouts</li>
                        <li>Direct vendor contracting (0% markup guarantee)</li>
                        <li>Resort room block & guest hospitality desk</li>
                        <li>Bespoke Sangeet, Haldi & Pheras design</li>
                        <li>Government permissions, permits & sound clearings</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Most Popular</a>
                </div>

                <div class="pricing-card">
                    <h3>Royal Palace & Mega Production</h3>
                    <div class="price">₹8 - ₹15 Lakhs <span style="font-size: 14px; font-weight: 400; color: #777;">/ Ultra-Luxe</span></div>
                    <ul>
                        <li>Custom architectural pavilions & glasshouses</li>
                        <li>Celebrity artist curation & staging</li>
                        <li>24/7 dedicated guest concierge & transit fleet</li>
                        <li>Exotic floral imports & bespoke fabrication</li>
                        <li>Senior director team of 20+ dedicated planners</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Inquire Now</a>
                </div>
            </div>
        </section>

        <!-- FAQs -->
        <section class="content-box">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 28px; color: #2C2C2C; margin-bottom: 20px;">Frequently Asked Questions — {city} Weddings</h2>
            <div class="faq-accordion">
                {"".join([f'''<div class="faq-item">
                    <h4>{item["q"]} <span>+</span></h4>
                    <div class="faq-ans">{item["a"]}</div>
                </div>''' for item in faqs])}
            </div>
        </section>

        <!-- Contact CTA -->
        <section id="quote" class="content-box" style="background: linear-gradient(135deg, #8B1A1A 0%, #5E0E0E 100%); color: #fff; text-align: center; padding: 45px 20px;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #D9B872; margin-bottom: 12px;">Start Planning Your Dream {city} Wedding</h2>
            <p style="max-width: 600px; margin: 0 auto 24px; color: #F5EFEB; font-size: 15px;">Speak directly with our Pan-India destination directors for honest cost estimators, venue availability, and bespoke 3D design concepts.</p>
            <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <a href="tel:+918050573382" class="btn-primary" style="background: #D9B872; color: #2C2C2C; font-weight: 600;">Call Us: +91 80505 73382</a>
                <a href="/contact" class="btn-primary" style="background: transparent; border: 1.5px solid #D9B872; color: #D9B872;">Request Itemized Estimate</a>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-section">
                <h3>Swariya Weddings</h3>
                <p>Pan-India Luxury Wedding & Destination Planning. Registered Office: Bengaluru. Operations across Goa, Rajasthan, Kerala, Mumbai, Delhi & Hyderabad.</p>
                <p>Phone: +91 80505 73382 | Email: hello@swariyaweddings.com</p>
            </div>
            <div class="footer-section">
                <h3>Destination Hubs</h3>
                <ul>
                    <li><a href="/wedding-planners-in-goa">Goa Beach Weddings</a></li>
                    <li><a href="/wedding-planners-in-udaipur">Udaipur Palace Weddings</a></li>
                    <li><a href="/wedding-planners-in-jaipur">Jaipur Fort Weddings</a></li>
                    <li><a href="/wedding-planners-in-mumbai">Mumbai & Alibaug</a></li>
                    <li><a href="/wedding-planners-in-delhi">Delhi NCR Farmhouses</a></li>
                    <li><a href="/wedding-planners-in-hyderabad">Hyderabad Royal Weddings</a></li>
                    <li><a href="/wedding-planners-in-chennai">Chennai ECR Coastal</a></li>
                    <li><a href="/wedding-planners-in-kerala">Kerala Backwaters</a></li>
                    <li><a href="/sitemap.html">Complete Directory</a></li>
                </ul>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    return html

for pillar in PAN_INDIA_PILLARS:
    html_content = generate_pillar_html(pillar)
    file_path = os.path.join(OUTPUT_DIR, f"{pillar['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated Pan-India pillar: {pillar['slug']}.html")

# Update sitemap-main.xml with these core Pan-India pillars
sitemap_main_path = os.path.join(OUTPUT_DIR, "sitemap-main.xml")
with open(sitemap_main_path, "r", encoding="utf-8") as f:
    sitemap_main = f.read()

entries = []
for p in PAN_INDIA_PILLARS:
    url_tag = f"https://swariyaweddings.com/{p['slug']}"
    if url_tag not in sitemap_main:
        entries.append(f"""  <url>
    <loc>{url_tag}</loc>
    <lastmod>2026-09-28</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

if entries:
    sitemap_main = sitemap_main.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    with open(sitemap_main_path, "w", encoding="utf-8") as f:
        f.write(sitemap_main)
    print(f"Added {len(entries)} Pan-India pillar URLs to sitemap-main.xml")
