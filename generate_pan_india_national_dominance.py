import os
import json

OUTPUT_DIR = "/Users/mac/Documents/swariya-weddings-complete-project"

# 1. 35 Major Indian Metros & High-Net-Worth Cities
INDIAN_CITIES = [
    ("Mumbai", "mumbai", "Maharashtra", "5-star luxury sea-facing ballrooms, South Mumbai heritage clubs & Alibaug villa buyouts", "Taj Mahal Palace, St. Regis Mumbai, Taj Lands End, JW Marriott Juhu", "₹4L - ₹10L"),
    ("Delhi NCR", "delhi", "Delhi NCR", "Opulent South Delhi & Chattarpur farmhouses, Aerocity 5-star ballrooms & grand productions", "The Leela Palace Chanakyapuri, ITC Grand Bharat, JW Marriott Aerocity", "₹4L - ₹10L"),
    ("Kolkata", "kolkata", "West Bengal", "Colonial heritage Rajbaris, Vedic Bengali rituals & sprawling luxury hotel ballrooms", "ITC Royal Bengal, Taj Bengal, The Oberoi Grand, Vedic Village Resort", "₹3.5L - ₹7L"),
    ("Chennai", "chennai", "Tamil Nadu", "East Coast Road (ECR) beach resorts, traditional Tamil Brahmin rituals & grand 5-star halls", "ITC Grand Chola, Taj Fisherman's Cove ECR, The Leela Palace Chennai", "₹3.5L - ₹7L"),
    ("Hyderabad", "hyderabad", "Telangana", "Royal Nizam palaces, grand Telugu celebrations & modern HITEC City convention centers", "Taj Falaknuma Palace, ITC Kohenur, Taj Krishna, Novotel HICC", "₹3.5L - ₹8L"),
    ("Pune", "pune", "Maharashtra", "Lavasa valleys, Oxford heritage clubs & luxury Baner/Koregaon Park banquet enclaves", "JW Marriott Pune, The Ritz-Carlton Pune, Conrad Pune, Oxford Golf Resort", "₹3.5L - ₹7L"),
    ("Ahmedabad", "ahmedabad", "Gujarat", "Grand SG Highway farmhouses, opulent Garba-Sangeet nights & pure vegetarian Jain banquets", "Taj Skyline, ITC Narmada, Courtyard by Marriott Sindhu Bhavan, Belvedere Golf Resort", "₹3.5L - ₹8L"),
    ("Surat", "surat", "Gujarat", "Dumas Road sprawling farmhouses, diamond merchant royal celebrations & high-production sets", "Avadh Utopia, The Grand Bhagwati Surat, Surat Marriott Hotel", "₹3.5L - ₹8L"),
    ("Jaipur", "jaipur", "Rajasthan", "Royal Rajputana fortresses, palace courtyards & high-production heritage galas", "Fairmont Jaipur, Rambagh Palace, Samode Palace, JW Marriott Kukas", "₹4L - ₹10L"),
    ("Lucknow", "lucknow", "Uttar Pradesh", "Royal Awadhi heritage havelis, Nawabi court decor & world-famous culinary feasts", "Taj Mahal Lucknow, Hyatt Regency Lucknow, The Centrum Lucknow", "₹3L - ₹6L"),
    ("Chandigarh", "chandigarh", "Punjab / Haryana", "Grand Punjabi farmhouses, Anand Karaj Gurdwaras & Zirakpur luxury resort corridor", "The Oberoi Sukhvilas, JW Marriott Chandigarh, Hyatt Regency Chandigarh", "₹3.5L - ₹8L"),
    ("Indore", "indore", "Madhya Pradesh", "Bypass road grand wedding resorts, traditional Marwari/Malwi weddings & gourmet food stalls", "Brilliant Convention Centre, Sayaji Hotel, Sheraton Grand Palace Indore", "₹3L - ₹6L"),
    ("Bhopal", "bhopal", "Madhya Pradesh", "Upper Lake luxury heritage resorts & central Indian royal celebrations", "Jehan Numa Palace Hotel, Noor-Us-Sabah Palace, Taj Lakefront Bhopal", "₹3L - ₹6L"),
    ("Nagpur", "nagpur", "Maharashtra", "Wardha Road convention resorts & grand Vidarbha community wedding celebrations", "Le Méridien Nagpur, Radisson Blu Nagpur, Hotel Centre Point", "₹3L - ₹6L"),
    ("Patna", "patna", "Bihar", "Grand traditional Bihari Shadi rituals, Ganga riverfront banquets & lavish receptions", "Hotel Maurya, Lemon Tree Premier Patna, Panache Hotel", "₹2.5L - ₹5L"),
    ("Bhubaneswar", "bhubaneswar", "Odisha", "Traditional Odia temple wedding rituals, Puri coastal getaways & luxury convention halls", "Mayfair Lagoon, Trident Bhubaneswar, Welcomhotel by ITC Hotels", "₹3L - ₹6L"),
    ("Kochi (Cochin)", "kochi", "Kerala", "Bolgatty Island luxury waterfront, Fort Kochi colonial courtyards & traditional Sadya", "Grand Hyatt Kochi Bolgatty, Brunton Boatyard, Taj Malabar Resort", "₹3.5L - ₹7L"),
    ("Coimbatore", "coimbatore", "Tamil Nadu", "Kongu Vellalar heritage rituals, Western Ghats resort venues & grand banquets", "Le Méridien Coimbatore, Welcomhotel Coimbatore, The Residency Towers", "₹3L - ₹6L"),
    ("Visakhapatnam (Vizag)", "visakhapatnam", "Andhra Pradesh", "Scenic Bay of Bengal coastal beach mandaps & grand Andhra Telugu celebrations", "The Park Visakhapatnam, Novotel Visakhapatnam Varun Beach, Radisson Blu", "₹3L - ₹6L"),
    ("Varanasi (Kashi)", "varanasi", "Uttar Pradesh", "Holy Ganges ghat aarti backdrops, Vedic Kashi Vivah rituals & heritage palace setups", "Taj Ganges Varanasi, BrijRama Palace on the Ghats, Radisson Hotel", "₹3.5L - ₹7L"),
    ("Amritsar", "amritsar", "Punjab", "Grand Golden Temple Anand Karaj, heritage havelis & energetic Bhangra/Sangeet nights", "Taj Swarna Amritsar, Radisson Blu Amritsar, Courtyard by Marriott", "₹3L - ₹7L"),
    ("Dehradun", "dehradun", "Uttarakhand", "Sal forest valleys, foothills luxury resorts & intimate mountain destination weddings", "Hyatt Regency Dehradun, JW Marriott Mussoorie Foothills, LP Vilas", "₹3.5L - ₹7L"),
    ("Agra", "agra", "Uttar Pradesh", "Taj Mahal viewing terrace lawns & Mughal-inspired royal court wedding productions", "The Oberoi Amarvilas, ITC Mughal Agra, Jaypee Palace Hotel", "₹4L - ₹8L"),
    ("Vadodara (Baroda)", "vadodara", "Gujarat", "Gaekwad royal heritage influence, Sevasi farmhouse enclaves & grand Garba nights", "Grand Mercure Vadodara Surya Palace, Vivanta Vadodara, Sayaji Hotel", "₹3L - ₹6L"),
    ("Mysore (Mysuru)", "mysore", "Karnataka", "Lalitha Mahal Palace royal setups, authentic Mysore silk mandaps & grand South feasts", "Lalitha Mahal Palace Hotel, Radisson Blu Plaza Hotel Mysore, Silent Shores Resort", "₹3L - ₹6L"),
    ("Mangalore", "mangalore", "Karnataka", "Coastal Tulunadu Bunt weddings, Arabian sea beach lawns & coastal cuisine banquets", "The Ocean Pearl, Vivanta Mangalore, Goldfinch Hotel Mangalore", "₹3L - ₹6L"),
    ("Ludhiana", "ludhiana", "Punjab", "Ferozepur Road mega luxury wedding palaces, designer Punjabi Baraats & high-tech staging", "Hyatt Regency Ludhiana, Radisson Blu Hotel, Park Plaza", "₹3.5L - ₹8L"),
    ("Kanpur", "kanpur", "Uttar Pradesh", "VIP Road grand banquets, traditional North Indian royal weddings & gourmet catering", "The Landmark Hotel, Status Club, Regenta Central The Crystal", "₹2.5L - ₹5L"),
    ("Rajkot", "rajkot", "Gujarat", "Kalawad Road luxury farmhouses, Saurashtra Patel royal celebrations & Kathiyawadi dining", "The Imperial Palace, Sayaji Hotel Rajkot, Fortune Park JPS Grand", "₹3L - ₹6L"),
    ("Gurgaon (Gurugram)", "gurgaon", "Haryana", "Golf course luxury retreats, high-end corporate families & international design staging", "ITC Grand Bharat, The Oberoi Gurgaon, The Leela Ambience Gurugram", "₹4L - ₹10L"),
    ("Noida & Greater Noida", "noida", "Uttar Pradesh", "Expressway luxury farmhouses, mega convention pavilions & high-production sangeets", "Radisson Blu MBD Hotel Noida, Crowne Plaza Greater Noida, Jaypee Greens Golf Resort", "₹3.5L - ₹8L"),
    ("Goa", "goa", "Goa", "Pristine white sand beach mandaps, sundowner sangeets & 5-star coastal resort buyouts", "The Leela Goa, Taj Exotica, W Goa, Grand Hyatt Goa, Alila Diwa", "₹4L - ₹10L"),
    ("Udaipur", "udaipur", "Rajasthan", "Lake Pichola island palaces, City Palace heritage & royal destination galas", "The Oberoi Udaivilas, Taj Lake Palace, Jagmandir Island Palace, Raffles Udaipur", "₹4L - ₹12L"),
    ("Jodhpur", "jodhpur", "Rajasthan", "Mehrangarh Fort vistas, golden sandstone palaces & royal Marwar heritage", "Umaid Bhawan Palace, ITC WelcomeHotel Jodhpur, Indana Palace", "₹4L - ₹12L"),
    ("Jaisalmer", "jaisalmer", "Rajasthan", "Golden Thar desert sand dunes, luxury havelis & starlit folk sangeet nights", "Suryagarh Jaisalmer, Jaisalmer Marriott Resort & Spa, Gorbandh Palace", "₹4L - ₹10L")
]

# 2. 25 Top Destination Getaway Locations in India
DESTINATION_HUBS = [
    ("Goa Beachfront", "goa", "White sand beaches, coastal Portuguese architecture & 5-star luxury resort buyouts", "The Leela, Taj Exotica, W Goa, ITC Grand Goa, St. Regis"),
    ("Udaipur Lake Palaces", "udaipur", "Lakeside royal island palaces, private boat baaraats & regal Mewari hospitality", "Oberoi Udaivilas, Taj Lake Palace, Jagmandir, Leela Palace"),
    ("Jaipur Heritage Forts", "jaipur", "Aravalli hill forts, royal sandstone courtyards & high-production palace sangeets", "Fairmont Jaipur, Rambagh Palace, Samode Palace, Alila Fort"),
    ("Jodhpur Sun City Palaces", "jodhpur", "Iconic Art Deco royal palaces, Mehrangarh fort backdrops & Marwar royal feasts", "Umaid Bhawan Palace, Welcomhotel Jodhpur, Ajit Bhawan"),
    ("Jaisalmer Desert Dunes", "jaisalmer", "Golden sandstone fortresses, desert luxury camps & royal bonfire sangeet galas", "Suryagarh Jaisalmer, Jaisalmer Marriott, Fort Rajwada"),
    ("Kumarakom & Alleppey Backwaters", "kumarakom", "Emerald Vembanad lake views, traditional houseboat sunset cruises & Sadya feasts", "Kumarakom Lake Resort, Zuri Kumarakom, Coconut Lagoon"),
    ("Kovalam & Varkala Clifftops", "kovalam", "Arabian Sea clifftop sunset vows, private beach bays & Ayurvedic wellness retreats", "The Leela Kovalam, Taj Green Cove, Niraamaya Surya Samudra"),
    ("Coorg (Kodagu) Coffee Estates", "coorg", "Misty Western Ghats mountain ridges, aromatic coffee plantations & Kodava rituals", "The Tamara Coorg, Evolve Back Kamalapura, Club Mahindra"),
    ("Chikmagalur Hill Retreats", "chikmagalur", "Mullayanagiri mountain vistas, private waterfall villas & estate starlit weddings", "The Serai Chikmagalur, Java Rain Resort, Trivik Hotels"),
    ("Kabini Rainforest & Riverfront", "kabini", "Kapila riverfront wilderness lodges, boat safari pre-wedding shoots & serene lawns", "Evolve Back Kabini, The Serai Kabini, Waterwoods Lodges"),
    ("Mussoorie & Dhanaulti Ridges", "mussoorie", "Queen of the Hills colonial charm, Himalayan snow peak backdrops & bonfire nights", "JW Marriott Mussoorie Walnut Grove, Savoy Mussoorie, Jaypee Residency"),
    ("Jim Corbett Wilderness", "jim-corbett", "Kosi riverfront luxury safari lodges, dense sal forest canopies & acoustic starlit sangeets", "Taj Corbett Resort & Spa, The Riverview Retreat, Namah Resort"),
    ("Rishikesh Holy Ganges", "rishikesh", "Sacred riverfront Ganga aarti mandaps, Himalayan spiritual tranquility & wellness weddings", "Taj Resort & Convention Centre Rishikesh, The Roseate Ganges, Aloha On The Ganges"),
    ("Shimla & Chail Pine Forests", "shimla", "Cedar forest hills, British colonial ballroom heritage & crisp mountain air weddings", "Wildflower Hall Shimla, The Oberoi Cecil, Woodville Palace"),
    ("Alibaug Coastal Mansions", "alibaug", "Private luxury estate buyouts, speedboat charters from Gateway of India & sea lawns", "Radisson Blu Alibaug, Outpost Alibaug, Private Beachfront Villas"),
    ("Lonavala & Khandala Hills", "lonavala", "Sahyadri mountain valleys, luxury villa retreats & Mumbai/Pune weekend connectivity", "Della Resorts, Fariyas Resort, Radisson Resort & Spa Lonavala"),
    ("Mahabaleshwar & Panchgani", "mahabaleshwar", "Strawberry plantation plateaus, foggy mountain cliff vistas & boutique luxury stays", "Le Méridien Mahabaleshwar Resort, Courtyard by Marriott Mahabaleshwar"),
    ("Mahabalipuram Coastal Heritage", "mahabalipuram", "UNESCO shore temple vistas, Bay of Bengal beachfront lawns & classical Carnatic decor", "InterContinental Mahabalipuram, Taj Fisherman's Cove, Radisson Blu Resort Temple Bay"),
    ("Pondicherry French Quarter", "pondicherry", "Franco-Tamil heritage mansions, colorful bougainvillea lanes & coastal bohemian setups", "Palais de Mahé, Le Pondy Beach Resort, Promenade Hotel"),
    ("Andaman & Nicobar Islands (Havelock)", "andaman", "Radhanagar turquoise waters, pristine coral beach barefoot ceremonies & sunset cruises", "Taj Exotica Resort & Spa Andamans, Barefoot at Havelock, Symphony Palms"),
    ("Hampi UNESCO Ruins", "hampi", "14th-century Vijayanagara empire stone temples, boulder-strewn landscapes & palace luxury", "Evolve Back Kamalapura Palace, Heritage Resort Hampi"),
    ("Gokarna Clifftops", "gokarna", "Secluded Om Beach and Kudle Beach cliff lawns, tranquil bohemian aesthetic & ocean sunsets", "Kahani Paradise, SwaSwara Wellness Resort, Stone Wood Nature Resort"),
    ("Neemrana 15th Century Fort", "neemrana", "Multi-tiered heritage fort palace, hanging gardens & royal Rajasthani stepwell mandaps", "Neemrana Fort-Palace, Hill Fort Kesroli Alwar"),
    ("Ranthambore Tiger Corridors", "ranthambore", "Aristocratic wildlife safari luxury tented suites & 14th-century royal fort heritage", "Six Senses Fort Barwara, The Oberoi Vanyavilas, Aman-i-Khás"),
    ("Pushkar Holy Lake & Desert", "pushkar", "Desert dunes, royal camel caravans & sacred lake heritage pavilions", "The Westin Pushkar Resort & Spa, Ananta Spa & Resorts, Brahma Horizon")
]

# 3. National Comparison & Authority Flagship Hubs
NATIONAL_FLAGSHIPS = [
    {
        "slug": "top-wedding-planners-in-india",
        "title": "Top 10 Best Wedding Planners in India (2026 Reviews & Pricing)",
        "h1": "Top 10 Best Luxury Wedding Planners in India | 2026 Comparison",
        "meta_desc": "Looking for the best wedding planners in India? Compare top luxury agencies in Mumbai, Delhi & Bangalore on fee structures, decor fabrication & 0% markups.",
        "desc": "An unbiased, comprehensive 2026 guide evaluating India's top luxury wedding planning agencies (Wedniksha, Shaadi Squad, Motwane, Swariya Weddings, etc.) on pricing transparency, in-house decor capabilities, and multi-day destination execution across Goa, Rajasthan, and Kerala."
    },
    {
        "slug": "cost-of-destination-wedding-in-india-2026",
        "title": "Cost of Destination Wedding in India 2026 (Full Budget Breakdown)",
        "h1": "Complete Cost Guide for Destination Weddings in India | 2026 Price Matrix",
        "meta_desc": "How much does a destination wedding in India cost? Detailed 2026 price guide for Goa, Udaipur, Jaipur, Kerala & Coorg with 100 to 250 guest cost breakdowns.",
        "desc": "A master financial planning guide breaking down real costs for 2-day and 3-day luxury destination weddings in India across 50, 100, 200, and 500 guest tiers. Includes venue buyouts, catering rates, decor fabrication, liquor licenses, and 0% vendor markup savings."
    },
    {
        "slug": "best-destination-wedding-places-in-india",
        "title": "25 Best Destination Wedding Places in India (Palaces, Beaches, Hills)",
        "h1": "25 Best Destination Wedding Locations in India | 2026 Curated Guide",
        "meta_desc": "Discover the 25 best destination wedding locations in India. From royal Udaipur palaces & Goa beaches to Kerala backwaters & Mussoorie hills.",
        "desc": "Explore India's most breathtaking wedding destinations ranked by seasonal weather, luxury 5-star resort capacity, airport connectivity, and romantic backdrops."
    },
    {
        "slug": "nri-destination-wedding-planner-in-india",
        "title": "NRI Destination Wedding Planner in India | USA, UK, UAE Couples",
        "h1": "NRI Destination Wedding Planning in India | Remote Concierge & 0% Markups",
        "meta_desc": "Specialized NRI destination wedding planning in India for couples in USA, UK, Canada & UAE. 3D virtual design, airport fleet logistics & trusted fiduciary management.",
        "desc": "Planning an Indian destination wedding from overseas? Swariya Weddings provides US/UK time zone coordination, photorealistic 3D decor walk-throughs, 24/7 guest hospitality desks, and transparent direct vendor billing with zero hidden middleman commissions."
    }
]

def generate_city_page(city, slug, state, desc, top_venues, fee):
    canonical_url = f"https://swariyaweddings.com/wedding-planners-in-{slug}"
    title = f"Wedding Planners in {city} | Top Luxury Planners | Swariya"
    h1 = f"Luxury Wedding Planners in {city}, {state}"
    meta_desc = f"Looking for top wedding planners in {city}? Swariya Weddings delivers turnkey luxury decor, 3D renders & 0% vendor markups across {city} venues."
    
    local_schema = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{canonical_url}#service",
        "name": f"Swariya Weddings - Wedding Planners in {city}",
        "url": canonical_url,
        "image": "https://swariyaweddings.com/images/16.jpg",
        "telephone": "+91-8050573382",
        "priceRange": "₹₹₹",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Pan-India Operations HQ",
            "addressLocality": city,
            "addressRegion": state,
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
                "name": f"What is the average cost of hiring a wedding planner in {city}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Wedding planning fees in {city} typically range from ₹1.5L for day-of coordination to {fee} for full turnkey multi-day production with 0% vendor markups."
                }
            },
            {
                "@type": "Question",
                "name": f"What top luxury venues do you manage in and around {city}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"We manage leading luxury venues including {top_venues}, alongside private farmhouses and heritage estates."
                }
            },
            {
                "@type": "Question",
                "name": f"How does Swariya's 0% markup model save money for {city} couples?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Unlike traditional event brokers who inflate vendor bills by 20–40%, Swariya passes 100% of vendor quotes and negotiated discounts directly to you with complete itemized billing."
                }
            }
        ]
    }

    return f"""<!DOCTYPE html>
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
        .city-hero {{ background: linear-gradient(135deg, #FAF7F2 0%, #F5EFEB 100%); padding: 60px 0 40px; border-bottom: 1px solid #EBE4D8; }}
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
        .venue-pill {{ background: #FAF7F2; border: 1px solid #EBE4D8; padding: 12px 18px; border-radius: 6px; font-size: 14px; font-weight: 500; color: #2C2C2C; }}
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
                <li><a href="/destination-wedding-planner-in-india">Pan-India Hub</a></li>
                <li><a href="/wedding-planners-in-bangalore">Bangalore HQ</a></li>
                <li><a href="/top-wedding-planners-in-india">Compare Planners</a></li>
                <li><a href="/reviews">Reviews</a></li>
                <li><a href="/contact" class="btn-contact">Get Free Quote</a></li>
            </ul>
        </div>
    </nav>

    <header class="city-hero">
        <div class="container">
            <p class="section-label" style="color: #8B1A1A; font-weight: 600;">✦ PAN-INDIA LUXURY WEDDING SPECIALISTS</p>
            <h1 style="font-family: 'Playfair Display', serif; font-size: 38px; color: #2C2C2C; margin: 12px 0 16px; line-height: 1.2;">{h1}</h1>
            <p style="font-size: 16px; color: #555; max-width: 800px; line-height: 1.7;">{desc}. Swariya Weddings brings precision production, 3D photorealistic decor walk-throughs, and transparent 0% markup management to {city}.</p>
            <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 24px;">
                <a href="#quote" class="btn-primary">Book Consultation Call</a>
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I%20am%20looking%20for%20a%20wedding%20planner%20in%20{city.replace(' ', '%20')}" class="btn-primary" style="background: #25D366; border-color: #25D366;">WhatsApp Senior Director 💬</a>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Trust Metrics -->
        <section class="content-box">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; text-align: center;">
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">0%</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Vendor Kickbacks or Hidden Margins</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">4.9 ★</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Rated by 500+ Couples Pan-India</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">150+</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Weddings Successfully Executed</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">100%</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Custom 3D Decor Pre-Visualization</p>
                </div>
            </div>
        </section>

        <!-- Venues in City -->
        <section class="content-box">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 24px; color: #2C2C2C; margin-bottom: 12px;">Premier Venues Managed in {city}</h2>
            <p style="color: #666; margin-bottom: 20px;">We maintain direct on-ground partnerships and sound/decor clearances across {city}'s top 5-star properties and banquet resorts:</p>
            <div class="venue-pill">🏛️ {top_venues}</div>
        </section>

        <!-- Pricing Breakdown -->
        <section style="margin: 40px 0;">
            <div style="text-align: center; margin-bottom: 30px;">
                <p class="section-label">✦ 2026 TRANSPARENT ESTIMATES</p>
                <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #2C2C2C;">Turnkey Planning & Decor Fee Tiers in {city}</h2>
                <p style="color: #666; max-width: 650px; margin: 8px auto 0;">Enjoy honest, itemized pricing with direct vendor contracting and in-house technical fabrication.</p>
            </div>

            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>Day-Of Production Coordination</h3>
                    <div class="price">₹1.5 - ₹2.5 Lakhs <span style="font-size: 14px; font-weight: 400; color: #777;">/ 1-2 Days</span></div>
                    <ul>
                        <li>Full vendor timeline alignment</li>
                        <li>Shadow coordinators for Bride & Groom</li>
                        <li>Guest seating & gift reception desk</li>
                        <li>Pooja samagri & priest flow coordination</li>
                        <li>Audio/Visual cues & DJ sync</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Select Plan</a>
                </div>

                <div class="pricing-card featured">
                    <h3>Complete Turnkey Management</h3>
                    <div class="price">{fee} <span style="font-size: 14px; font-weight: 400; color: #777;">/ Multi-Day</span></div>
                    <ul>
                        <li>End-to-end 3D decor concept renders</li>
                        <li>Direct vendor contracting (0% markup)</li>
                        <li>Venue layout & sound clearance logistics</li>
                        <li>Sangeet production & artist booking</li>
                        <li>Guest logistics, room blocks & RSVP desk</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Most Popular</a>
                </div>

                <div class="pricing-card">
                    <h3>Royal Palace & Bespoke Luxe</h3>
                    <div class="price">₹7 - ₹12 Lakhs <span style="font-size: 14px; font-weight: 400; color: #777;">/ Ultra-Luxe</span></div>
                    <ul>
                        <li>Full architectural pavilion staging</li>
                        <li>Celebrity artist curation & staging</li>
                        <li>24/7 guest concierge & fleet dispatch</li>
                        <li>Exotic floral imports & bespoke fabrication</li>
                        <li>Executive team of 15+ dedicated planners</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Select Plan</a>
                </div>
            </div>
        </section>

        <!-- FAQs -->
        <section class="content-box">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 28px; color: #2C2C2C; margin-bottom: 20px;">Frequently Asked Questions</h2>
            <div class="faq-accordion">
                <div class="faq-item">
                    <h4>What is the average cost of hiring a wedding planner in {city}? <span>+</span></h4>
                    <div class="faq-ans">Wedding planning fees in {city} typically range from ₹1.5L for day-of coordination to {fee} for full turnkey multi-day production with 0% vendor markups.</div>
                </div>
                <div class="faq-item">
                    <h4>What top luxury venues do you manage in and around {city}? <span>+</span></h4>
                    <div class="faq-ans">We manage leading luxury venues including {top_venues}, alongside private farmhouses and heritage estates.</div>
                </div>
                <div class="faq-item">
                    <h4>How does Swariya's 0% markup model save money for {city} couples? <span>+</span></h4>
                    <div class="faq-ans">Unlike traditional event brokers who inflate vendor bills by 20–40%, Swariya passes 100% of vendor quotes and negotiated discounts directly to you with complete itemized billing.</div>
                </div>
            </div>
        </section>

        <!-- Contact CTA -->
        <section id="quote" class="content-box" style="background: linear-gradient(135deg, #8B1A1A 0%, #5E0E0E 100%); color: #fff; text-align: center; padding: 45px 20px;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #D9B872; margin-bottom: 12px;">Plan Your Perfect Celebration in {city}</h2>
            <p style="max-width: 600px; margin: 0 auto 24px; color: #F5EFEB; font-size: 15px;">Talk to our senior wedding directors today for a custom moodboard, 3D decor layout, and honest itemized cost breakdown.</p>
            <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <a href="tel:+918050573382" class="btn-primary" style="background: #D9B872; color: #2C2C2C; font-weight: 600;">Call Us: +91 80505 73382</a>
                <a href="/contact" class="btn-primary" style="background: transparent; border: 1.5px solid #D9B872; color: #D9B872;">Request Custom Proposal</a>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-section">
                <h3>Swariya Weddings</h3>
                <p>Pan-India Luxury Wedding Planners. Operations in {city}, Bangalore, Mumbai, Delhi, Goa, Rajasthan & Kerala.</p>
                <p>Phone: +91 80505 73382 | Email: hello@swariyaweddings.com</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="/destination-wedding-planner-in-india">Pan-India Master Hub</a></li>
                    <li><a href="/wedding-planners-in-bangalore">Bangalore Headquarters</a></li>
                    <li><a href="/top-wedding-planners-in-india">Top Planners Comparison</a></li>
                    <li><a href="/cost-of-destination-wedding-in-india-2026">2026 National Cost Guide</a></li>
                    <li><a href="/sitemap.html">Complete Sitemap Directory</a></li>
                </ul>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""

# Generate all 35 City Pillars
PAN_INDIA_GENERATED_PAGES = []
for city, slug, state, desc, top_venues, fee in INDIAN_CITIES:
    page_slug = f"wedding-planners-in-{slug}"
    html_code = generate_city_page(city, slug, state, desc, top_venues, fee)
    with open(os.path.join(OUTPUT_DIR, f"{page_slug}.html"), "w", encoding="utf-8") as f:
        f.write(html_code)
    PAN_INDIA_GENERATED_PAGES.append({"title": f"Wedding Planners in {city}", "slug": page_slug, "category": "Major Indian Metros"})
    print(f"Generated Metro Hub: {page_slug}.html")

# Generate 25 Destination Hubs
for dest_name, slug, desc, venues in DESTINATION_HUBS:
    page_slug = f"destination-wedding-in-{slug}"
    title = f"Destination Wedding in {dest_name} | Planners & Cost Guide | Swariya"
    h1 = f"Luxury Destination Weddings in {dest_name}"
    meta_desc = f"Planning a destination wedding in {dest_name}? Swariya Weddings provides full resort buyouts, 3D decor renders & 0% vendor markups."
    html_code = generate_city_page(dest_name, f"destination-{slug}", "India", desc, venues, "₹4L - ₹10L")
    with open(os.path.join(OUTPUT_DIR, f"{page_slug}.html"), "w", encoding="utf-8") as f:
        f.write(html_code)
    PAN_INDIA_GENERATED_PAGES.append({"title": f"Destination Wedding in {dest_name}", "slug": page_slug, "category": "Top Indian Destinations"})
    print(f"Generated Destination Hub: {page_slug}.html")

# Generate 4 National Flagship Pages
for item in NATIONAL_FLAGSHIPS:
    slug = item["slug"]
    title = item["title"]
    h1 = item["h1"]
    meta_desc = item["meta_desc"]
    desc = item["desc"]
    html_code = generate_city_page(title, slug, "Pan-India", desc, "Fairmont Jaipur, Taj Lake Palace, The Leela Goa, ITC Grand Chola, Kumarakom Lake Resort", "₹4L - ₹12L")
    with open(os.path.join(OUTPUT_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html_code)
    PAN_INDIA_GENERATED_PAGES.append({"title": title, "slug": slug, "category": "National Flagships"})
    print(f"Generated National Flagship: {slug}.html")

# Create Dedicated XML Sitemap for Pan-India Dominance
sitemap_pan_india_path = os.path.join(OUTPUT_DIR, "sitemap-pan-india-national.xml")
sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in PAN_INDIA_GENERATED_PAGES:
    sitemap_content.append(f'''  <url>
    <loc>https://swariyaweddings.com/{p["slug"]}</loc>
    <lastmod>2026-09-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>''')
sitemap_content.append('</urlset>')

with open(sitemap_pan_india_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))
print(f"Created sitemap-pan-india-national.xml with {len(PAN_INDIA_GENERATED_PAGES)} URLs.")

# Update root sitemap.xml
main_sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
with open(main_sitemap_path, "r", encoding="utf-8") as f:
    main_sitemap = f.read()

if "sitemap-pan-india-national.xml" not in main_sitemap:
    entry = """  <sitemap>
    <loc>https://swariyaweddings.com/sitemap-pan-india-national.xml</loc>
    <lastmod>2026-09-28</lastmod>
  </sitemap>
</sitemapindex>"""
    main_sitemap = main_sitemap.replace("</sitemapindex>", entry)
    with open(main_sitemap_path, "w", encoding="utf-8") as f:
        f.write(main_sitemap)
    print("Added sitemap-pan-india-national.xml to root sitemap.xml index.")

# Update sitemap.html
sitemap_html_path = os.path.join(OUTPUT_DIR, "sitemap.html")
with open(sitemap_html_path, "r", encoding="utf-8") as f:
    sitemap_html = f.read()

metros_links = "".join([f'<li><a href="/{p["slug"]}">{p["title"]}</a></li>\n' for p in PAN_INDIA_GENERATED_PAGES if p["category"] == "Major Indian Metros"])
dests_links = "".join([f'<li><a href="/{p["slug"]}">{p["title"]}</a></li>\n' for p in PAN_INDIA_GENERATED_PAGES if p["category"] == "Top Indian Destinations"])
flagships_links = "".join([f'<li><a href="/{p["slug"]}">{p["title"]}</a></li>\n' for p in PAN_INDIA_GENERATED_PAGES if p["category"] == "National Flagships"])

new_cards = f"""
            <div class="directory-card" style="border: 2px solid #8B1A1A;">
                <h2 style="color: #8B1A1A;">National Flagship Authority Guides ✦</h2>
                <ul>
                    {flagships_links}
                </ul>
            </div>

            <div class="directory-card">
                <h2>Top 35 Major Indian Metros & Cities</h2>
                <ul>
                    {metros_links}
                </ul>
            </div>

            <div class="directory-card">
                <h2>Top 25 Destination Getaways in India</h2>
                <ul>
                    {dests_links}
                </ul>
            </div>
"""

if '<div class="directory-grid">' in sitemap_html:
    sitemap_html = sitemap_html.replace('<div class="directory-grid">', f'<div class="directory-grid">\n{new_cards}')
    with open(sitemap_html_path, "w", encoding="utf-8") as f:
        f.write(sitemap_html)
    print("Injected all Pan-India national hubs into sitemap.html master directory.")
