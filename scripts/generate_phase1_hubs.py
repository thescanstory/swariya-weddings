import os
import json
import re

DATA = [
    # ----------------------------------------------------
    # 1. GOA DESTINATIONS
    # ----------------------------------------------------
    {
        "slug": "destination-wedding-planner-in-north-goa",
        "title": "Destination Wedding Planner in North Goa | Luxury Resorts & Villas - Swariya Weddings",
        "h1": "Destination Wedding Planner in North Goa",
        "category": "Destination",
        "region": "Goa",
        "subtitle": "High-energy coastal celebrations, luxury Portuguese heritage villas, and beachfront 5-star resorts in Candolim, Morjim, and Vagator with 0% vendor markups.",
        "meta_desc": "Top destination wedding planner in North Goa. Luxury villas, beach permits, sundowners in Candolim & Morjim, 3D decor & transparent 0% vendor markups.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹40 Lakhs – ₹1.2 Crores (100–250 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("W Goa, Vagator", "Dramatic cliffside beach resort with panoramic Arabian Sea views and iconic Rockpool sunset venue."),
            ("Taj Fort Aguada Resort, Candolim", "Historic coastal property overlooking Sinquerim beach with Portuguese ramparts."),
            ("Taj Holiday Village Resort & Spa, Candolim", "Charming terracotta cottages amidst lush beachfront tropical gardens."),
            ("Boutique Portuguese Mansions, Assagao", "Private heritage estates with courtyard pools for exclusive intimate buyouts.")
        ],
        "usp_points": [
            ("🌴 Zero Vendor Markups", "Direct billing on resort buyouts, sound licenses, and catering with 0% agency kickbacks."),
            ("🍹 Sundowner Sangeet Specialists", "High-energy beach pool parties, bohemian cocktail setups, and celebrity DJ curation."),
            ("📜 CRZ & Police Permits", "Complete management of Coastal Regulation Zone clearances and sound licensing.")
        ],
        "faqs": [
            ("How much does a destination wedding in North Goa cost in 2026?", "A 2-day wedding in North Goa for 100–200 guests typically ranges from ₹40L to ₹1.1Cr including 5-star resort rooms, catering, and floral production."),
            ("What is the difference between North Goa and South Goa weddings?", "North Goa is vibrant, famous for high-energy nightlife and boutique villas, while South Goa is serene, known for sprawling 5-star private beachfront resort buyouts."),
            ("Can Swariya handle sound permits for late-night music in North Goa?", "Yes. We coordinate all police and local administration licenses and design silent DJ afterparties when beach sound curfews apply.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-south-goa",
        "title": "Destination Wedding Planner in South Goa | 5-Star Beach Resorts - Swariya Weddings",
        "h1": "Destination Wedding Planner in South Goa",
        "category": "Destination",
        "region": "Goa",
        "subtitle": "Sprawling private beach resorts, peaceful white sands, and opulent ballroom celebrations in Cavelossim, Benaulim, and Majorda with 0% vendor markups.",
        "meta_desc": "Premier South Goa destination wedding planner. Luxury 5-star beachfront resorts in Cavelossim & Benaulim, private beach mandaps & 0% markup pricing.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹50 Lakhs – ₹1.5 Crores (150–350 guests)",
        "ideal_season": "November to March",
        "venues": [
            ("Taj Exotica Resort & Spa, Benaulim", "56-acre Mediterranean-inspired beachfront property with lush lawns and private beach."),
            ("ITC Grand Goa Resort & Spa, Arossim", "Indo-Portuguese village architecture with scenic lagoons and direct beach access."),
            ("The Leela Goa, Cavelossim", "75 acres of pristine lagoons, private golf course, and opulent beach pavilions."),
            ("Alila Diwa Goa, Majorda", "Contemporary Goan luxury overlooking tranquil paddy fields and infinity pool courtyards.")
        ],
        "usp_points": [
            ("🏖️ Private Beachfront Buyouts", "Exclusive private sand lawns with unobstructed sunset views for sacred pheras."),
            ("✈️ Dabolim & Mopa Airport Logistics", "Dedicated luxury coach fleets and VIP airport concierge desks for arriving guests."),
            ("📐 3D Coastal Mandap Architecture", "Engineered wind-proofed floral mandaps and canopy lighting renders before setup.")
        ],
        "faqs": [
            ("Why choose South Goa for a luxury destination wedding?", "South Goa offers untouched wide beaches, sprawling 5-star properties, and complete privacy for multi-day 150–350 guest weddings."),
            ("How far are South Goa resorts from Goa airports?", "Resorts in Cavelossim and Benaulim are 35–45 minutes from Dabolim Airport (GOI) and approximately 75 minutes from Mopa Airport (GOX)."),
            ("Does Swariya manage guest hotel room blocks?", "Yes, we negotiate guaranteed lowest room-block tariffs directly with property sales heads with zero agency commission.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-candolim-goa",
        "title": "Destination Wedding Planner in Candolim Goa | Beachfront Luxury - Swariya Weddings",
        "h1": "Destination Wedding Planner in Candolim Goa",
        "category": "Destination",
        "region": "Goa",
        "subtitle": "Bespoke beachfront nuptials, sunset cliff mandaps, and vibrant luxury celebrations in Candolim and Sinquerim.",
        "meta_desc": "Plan your luxury Candolim Goa destination wedding with Swariya Weddings. 5-star Taj resorts, private beach lawns, sound permits & 0% vendor markups.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹45 Lakhs – ₹1.2 Crores (100–250 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("Taj Fort Aguada Resort & Spa", "Panoramic sea views, historic Portuguese fort walls, and sea-facing amphitheaters."),
            ("Taj Holiday Village Resort & Spa", "Romantic Romanesque gardens, beachfront lawns, and tropical garden villas."),
            ("Novotel Goa Candolim", "Contemporary luxury with close proximity to Candolim beach and vibrant nightlife.")
        ],
        "usp_points": [
            ("🌊 Fort Rampart Backdrops", "Iconic coastal fort scenery paired with modern floral and lighting production."),
            ("🍽️ Curated Global Dining", "Goan seafood barbecues, royal Marwari counters, and authentic South Indian live feasts."),
            ("0% Vendor Markups", "Direct transparent billing on all local vendors, production, and audio-visual setups.")
        ],
        "faqs": [
            ("What makes Candolim popular for destination weddings?", "Candolim combines 5-star Taj luxury with vibrant nearby entertainment, making it effortless for guests to explore."),
            ("Can we host outdoor pheras on the beach lawn in Candolim?", "Yes, Taj Fort Aguada and Holiday Village offer manicured sea-facing lawns with direct beach proximity.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-cavelossim-goa",
        "title": "Destination Wedding Planner in Cavelossim Goa | The Leela & Radisson - Swariya Weddings",
        "h1": "Destination Wedding Planner in Cavelossim Goa",
        "category": "Destination",
        "region": "Goa",
        "subtitle": "Ultra-luxury lagoon and beachfront celebrations in Cavelossim, South Goa. 5-star resort buyouts and pristine ocean views.",
        "meta_desc": "Luxury destination wedding planner in Cavelossim Goa. Sprawling 5-star resorts, The Leela Goa & Radisson Blu, private beach mandaps & 0% markups.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹60 Lakhs – ₹1.6 Crores (150–350 guests)",
        "ideal_season": "November to March",
        "venues": [
            ("The Leela Goa, Cavelossim", "75 acres of lagoons, private beach, and grand royal ballrooms."),
            ("Radisson Blu Resort Goa Cavelossim Beach", "Vibrant Portuguese architecture with expansive lawn capacities."),
            ("Novotel Goa Dona Sylvia Resort", "Mediterranean-style villa resort with direct beach access.")
        ],
        "usp_points": [
            ("⛵ River & Ocean Frontages", "Unique duality of the Sal River on one side and the Arabian Sea on the other."),
            ("🏰 Grand Ballroom & Lawn Scale", "Accommodate up to 500 guests with complete luxury weather contingencies."),
            ("100% Transparent Billing", "Direct hotel contracts with zero agency commission.")
        ],
        "faqs": [
            ("How many guests can Cavelossim resorts accommodate?", "Properties like The Leela and Radisson Blu comfortably host 150 to 500+ residential guests across luxury villas and suites.")
        ]
    },

    # ----------------------------------------------------
    # 2. RAJASTHAN DESTINATIONS
    # ----------------------------------------------------
    {
        "slug": "destination-wedding-planner-in-jaipur-rajasthan",
        "title": "Destination Wedding Planner in Jaipur Rajasthan | Royal Palaces - Swariya Weddings",
        "h1": "Destination Wedding Planner in Jaipur Rajasthan",
        "category": "Destination",
        "region": "Rajasthan",
        "subtitle": "Regal Rajputana grandeur, iconic fort ramparts, royal elephant baaraats, and monumental palaces in Kukas and Amer with 0% vendor markups.",
        "meta_desc": "Top destination wedding planner in Jaipur. Fairmont, Chomu Palace, Jai Mahal, royal baraats, 3D architectural decor & 0% vendor markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹60 Lakhs – ₹2.5 Crores (200–600 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("Fairmont Jaipur, Kukas", "Grand Mughal palace architecture with massive ballrooms and majestic central courtyards."),
            ("Chomu Palace Hotel", "300-year-old historic royal palace with authentic Sheesh Mahal and courtyards."),
            ("Jai Mahal Palace (Taj)", "18 acres of Mughal gardens dating back to 1745 in the heart of Jaipur."),
            ("Le Méridien Jaipur Resort & Spa", "Sprawling luxury resort with huge banquet lawns and luxury pool villas.")
        ],
        "usp_points": [
            ("🐘 Royal Baaraat Logistics", "Permits for ceremonial elephants, royal camels, vintage open-top cars, and Nagada drums."),
            ("👑 0% Vendor Markups", "Direct palace hire tariffs and catering contracts with zero middleman kickbacks."),
            ("📐 3D Royal Set Fabrication", "Custom Rajputana jharokhas, carved mandap columns, and floral arches designed in 3D.")
        ],
        "faqs": [
            ("How much does a palace wedding in Jaipur cost in 2026?", "A 2 to 3-day royal wedding in Jaipur for 200–300 guests ranges from ₹60 Lakhs to ₹2.2 Crores depending on palace tier and decor scale."),
            ("How accessible is Jaipur for destination guests?", "Jaipur International Airport (JAI) connects directly to all major Indian hubs and international gateways like Dubai and Abu Dhabi."),
            ("Can Swariya coordinate royal Marwari and South Indian catering in Jaipur?", "Yes, we partner with premier royal Maharaj caterers and South Indian culinary masters for authentic multi-cuisine banquets.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-jodhpur-rajasthan",
        "title": "Destination Wedding Planner in Jodhpur Rajasthan | Sun City Palaces - Swariya Weddings",
        "h1": "Destination Wedding Planner in Jodhpur Rajasthan",
        "category": "Destination",
        "region": "Rajasthan",
        "subtitle": "Grand royal weddings beneath the iconic Mehrangarh Fort and heritage havelis of the Blue City with 0% vendor markups.",
        "meta_desc": "Royal destination wedding planner in Jodhpur. Mehrangarh backdrops, luxury palace resorts, royal baraats & transparent zero markup planning.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹55 Lakhs – ₹2.0 Crores (150–400 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("Indana Palace Jodhpur", "Opulent dome architecture and grand banquet courtyards."),
            ("Welcomhotel by ITC Hotels, Jodhpur", "Heritage Rajasthani stone architecture set against lush desert landscapes."),
            ("Radisson Jodhpur", "Modern luxury with authentic Marwari heritage banquet facilities."),
            ("Fort Khejarla / Heritage Havelis", "Authentic desert fortress settings for unforgettable boutique royal weddings.")
        ],
        "usp_points": [
            ("🏰 Mehrangarh Fort Backdrops", "Spectacular illuminated fort views for evening sangeets and pheras."),
            ("🥁 Desert Folk Ensembles", "Kalbelia dancers, Langa Manganiyar musicians, and authentic Marwari hospitality."),
            ("100% Transparent Accounting", "Real-time budget tracking via Swariya Wedding OS.")
        ],
        "faqs": [
            ("What makes Jodhpur unique for destination weddings?", "Jodhpur offers unmatched Rajputana heritage, authentic red sandstone palace architecture, and dramatic desert fort backdrops.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-jaisalmer-rajasthan",
        "title": "Destination Wedding Planner in Jaisalmer | Golden City Forts - Swariya Weddings",
        "h1": "Destination Wedding Planner in Jaisalmer",
        "category": "Destination",
        "region": "Rajasthan",
        "subtitle": "Golden sandstone palace retreats, Thar desert campfire sangeets, and unforgettable royal desert celebrations.",
        "meta_desc": "Luxury destination wedding planner in Jaisalmer. Suryagarh luxury, desert glamping, fort mandaps & 0% vendor markup planning.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹65 Lakhs – ₹2.5 Crores (150–350 guests)",
        "ideal_season": "November to February",
        "venues": [
            ("Suryagarh Jaisalmer", "World-renowned luxury fortress hotel offering iconic desert courtyard weddings."),
            ("Jaisalmer Marriott Resort & Spa", "Golden sandstone palace luxury with panoramic views of the historic fort."),
            ("Gorbandh Palace", "Royal heritage resort steeped in classic Rajputana architecture.")
        ],
        "usp_points": [
            ("✨ Desert Dunes Sangeet", "Magical candlelit desert evenings with folk musicians under starry desert skies."),
            ("👑 Full Fortress Buyouts", "Complete private property privatization for your family and guests."),
            ("Zero Middleman Commissions", "Direct pricing on all local craftsmen and palace bookings.")
        ],
        "faqs": [
            ("When is the best time for a Jaisalmer wedding?", "November through February offers pleasant daytime warmth and crisp desert evenings perfect for outdoor celebrations.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-pushkar-rajasthan",
        "title": "Destination Wedding Planner in Pushkar Rajasthan | Luxury Tented Resorts - Swariya Weddings",
        "h1": "Destination Wedding Planner in Pushkar Rajasthan",
        "category": "Destination",
        "region": "Rajasthan",
        "subtitle": "Spiritual tranquility, Aravalli mountain backdrops, and luxury heritage resorts in sacred Pushkar with 0% vendor markups.",
        "meta_desc": "Destination wedding planner in Pushkar. The Westin Pushkar, luxury heritage resorts, sacred lake ceremonies & zero markup planning.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹45 Lakhs – ₹1.2 Crores (150–350 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("The Westin Pushkar Resort & Spa", "Private plunge pool villas and expansive outdoor celebration lawns."),
            ("Ananta Spa & Resorts, Pushkar", "Lush hillside property with sprawling amphitheaters and ballrooms."),
            ("Brahma Horizon", "Boutique luxury resort nestled against the scenic Aravalli hills.")
        ],
        "usp_points": [
            ("🕉️ Sacred Vedic Rituals", "Unmatched spiritual resonance for traditional Vedic Muhurtham ceremonies."),
            ("🌿 Aravalli Valley Vistas", "Open-air lawns surrounded by dramatic mountain views."),
            ("0% Vendor Markups", "Complete transparency on resort buyouts and catering.")
        ],
        "faqs": [
            ("How accessible is Pushkar from Jaipur airport?", "Pushkar is approximately a 2.5-hour smooth expressway drive from Jaipur International Airport (JAI).")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-ranthambore-rajasthan",
        "title": "Destination Wedding Planner in Ranthambore | Royal Jungle Luxury - Swariya Weddings",
        "h1": "Destination Wedding Planner in Ranthambore",
        "category": "Destination",
        "region": "Rajasthan",
        "subtitle": "Luxury safari lodges, royal tented camps, and intimate heritage courtyard weddings on the edge of the wilderness.",
        "meta_desc": "Bespoke destination wedding planner in Ranthambore. Luxury safari lodges, Sawai Madhopur heritage & 0% markup pricing.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹40 Lakhs – ₹1.1 Crores (100–250 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("Nahargarh Ranthambore", "Palatial fortress architecture surrounded by Aravali hills with mirror-work courtyards."),
            ("The Baagh Ananta Elite", "Tranquil resort with sprawling green lawns and modern amenities."),
            ("Aman-i-Khás & Luxury Tents", "Ultra-luxury tented encampments for exclusive micro-wedding buyouts.")
        ],
        "usp_points": [
            ("🐅 Safari & Wedding Fusion", "Combine morning wilderness tiger safaris with opulent evening wedding sangeets."),
            ("0% Markup Guarantee", "Direct lodge tariffs with zero hidden agency surcharges.")
        ],
        "faqs": [
            ("Is Ranthambore suitable for wedding celebrations?", "Yes! Palatial lodges like Nahargarh provide authentic royal fort banquet setups with immense privacy.")
        ]
    },

    # ----------------------------------------------------
    # 3. KERALA DESTINATIONS
    # ----------------------------------------------------
    {
        "slug": "destination-wedding-planner-in-kumarakom-kerala",
        "title": "Destination Wedding Planner in Kumarakom Kerala | Backwater Resorts - Swariya Weddings",
        "h1": "Destination Wedding Planner in Kumarakom Kerala",
        "category": "Destination",
        "region": "Kerala",
        "subtitle": "Serene Vembanad Lake floating mandaps, luxury backwater resort buyouts, and authentic Kerala Sadhya hospitality with 0% vendor markups.",
        "meta_desc": "Top Kumarakom destination wedding planner. Vembanad lakefront resorts, Kumarakom Lake Resort, Zuri, houseboat mehendi & 0% markups.",
        "hero_img": "images/12.jpg",
        "cost_range": "₹45 Lakhs – ₹1.2 Crores (100–250 guests)",
        "ideal_season": "September to March",
        "venues": [
            ("Kumarakom Lake Resort", "Heritage pool villas, meandering pool courtyards, and lakefront celebration lawns."),
            ("The Zuri Kumarakom Kerala Resort & Spa", "18-acre lagoon luxury property with grand ballroom and lakeside lawns."),
            ("Taj Kumarakom Resort & Spa", "140-year-old colonial bungalow property nestled by bird sanctuaries and lagoons.")
        ],
        "usp_points": [
            ("⛵ Lakefront & Floating Mandaps", "Breathtaking mandaps built on water edges overlooking Vembanad Lake."),
            ("🍛 Authentic 24-Dish Sadhya", "Master chefs serving authentic Kerala Sadhyas on fresh banana leaves."),
            ("🥁 Chenda Melam & Floral Boats", "Groom and bridal entries on decorated traditional snake boats with live percussion.")
        ],
        "faqs": [
            ("How do guests reach Kumarakom?", "Kumarakom is a pleasant 90-minute drive from Cochin International Airport (COK). Swariya coordinates 24/7 airport AC coach transfers."),
            ("Can we host a mehendi on a houseboat in Kumarakom?", "Yes! We coordinate private chartered houseboat cruises complete with live acoustic music and coconut cocktails.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-kochi-kerala",
        "title": "Destination Wedding Planner in Kochi Kerala | Grand Hyatt & Fort Kochi - Swariya Weddings",
        "h1": "Destination Wedding Planner in Kochi Kerala",
        "category": "Destination",
        "region": "Kerala",
        "subtitle": "Colonial Dutch heritage lawns, Bolgatty Island 5-star grand ballrooms, and Arabian Sea waterfront weddings.",
        "meta_desc": "Premier Kochi destination wedding planner. Grand Hyatt Bolgatty, Brunton Boatyard, Fort Kochi heritage & 0% vendor markups.",
        "hero_img": "images/12.jpg",
        "cost_range": "₹40 Lakhs – ₹1.3 Crores (150–600 guests)",
        "ideal_season": "September to April",
        "venues": [
            ("Grand Hyatt Kochi Bolgatty", "Sprawling island resort with majestic waterfront lawns and huge ballrooms."),
            ("Brunton Boatyard (CGH Earth)", "Restored Victorian shipyard hotel overlooking Fort Kochi harbor."),
            ("Le Méridien Kochi", "Lush backwater setting with grand international convention facilities.")
        ],
        "usp_points": [
            ("🏛️ Historic Colonial Atmosphere", "Charming blend of Portuguese, Dutch, and traditional Kerala architecture."),
            ("✈️ Direct Global Airport Connectivity", "Cochin Airport (COK) offers non-stop flights from UAE, Singapore, Europe & India."),
            ("0% Vendor Markups", "Complete fiduciary transparency on venue rentals and catering.")
        ],
        "faqs": [
            ("Why choose Kochi for a destination wedding?", "Kochi offers international airport convenience, world-class 5-star properties, and deep coastal heritage charm.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-kovalam-kerala",
        "title": "Destination Wedding Planner in Kovalam Kerala | Cliffside Luxury - Swariya Weddings",
        "h1": "Destination Wedding Planner in Kovalam Kerala",
        "category": "Destination",
        "region": "Kerala",
        "subtitle": "Dramatic cliffside ocean panoramas, Arabian Sea beaches, and luxury beachfront resort celebrations in Kovalam.",
        "meta_desc": "Luxury destination wedding planner in Kovalam Kerala. The Leela Kovalam, Taj Green Cove, ocean cliff mandaps & 0% markup pricing.",
        "hero_img": "images/12.jpg",
        "cost_range": "₹45 Lakhs – ₹1.2 Crores (100–300 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("The Leela Kovalam, a Raviz Hotel", "Spectacular cliff-top resort with panoramic ocean views and private beach."),
            ("Taj Green Cove Resort & Spa Kovalam", "Balinese-style hillside cottages overlooking Arabian Sea backwaters."),
            ("Uday Samudra Leisure Beach Hotel", "Sprawling beachfront property with multiple lawn and pool venues.")
        ],
        "usp_points": [
            ("🌊 Cliff-Top Pheras", "Unmatched sunset ocean views high above the Arabian Sea shoreline."),
            ("0% Vendor Markups", "Transparent billing on direct resort tariffs and production.")
        ],
        "faqs": [
            ("How far is Kovalam from Trivandrum airport?", "Kovalam is just a 25-minute drive from Trivandrum International Airport (TRV).")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-alleppey-kerala",
        "title": "Destination Wedding Planner in Alleppey Kerala | Venice of the East - Swariya Weddings",
        "h1": "Destination Wedding Planner in Alleppey Kerala",
        "category": "Destination",
        "region": "Kerala",
        "subtitle": "Romantic canal waterways, palm-fringed private backwater lawns, and unforgettable houseboat celebrations.",
        "meta_desc": "Destination wedding planner in Alleppey Kerala. Venice of the East backwaters, luxury houseboat flotillas & zero markup planning.",
        "hero_img": "images/12.jpg",
        "cost_range": "₹35 Lakhs – ₹90 Lakhs (80–200 guests)",
        "ideal_season": "September to March",
        "venues": [
            ("Ramada by Wyndham Alleppey", "Waterfront property with views of the famous Punnamada Lake."),
            ("Uday Backwater Resort", "Lush backwater lawns ideal for intimate multi-day celebrations."),
            ("Luxury Houseboat Flotillas", "Chartered fleets of traditional luxury Kettuvallams.")
        ],
        "usp_points": [
            ("🌿 Ultimate Tropical Romance", "Tranquil lagoon waters, swaying palms, and intimate boutique luxury.")
        ],
        "faqs": [
            ("Can we host the main wedding ceremony on a backwater lawn in Alleppey?", "Yes, multiple resorts provide water-facing open lawns for mandaps and dinner setups.")
        ]
    },

    # ----------------------------------------------------
    # 4. KARNATAKA & HILL STATIONS
    # ----------------------------------------------------
    {
        "slug": "destination-wedding-planner-in-chikmagalur",
        "title": "Destination Wedding Planner in Chikmagalur | Coffee Estate Luxury - Swariya Weddings",
        "h1": "Destination Wedding Planner in Chikmagalur",
        "category": "Destination",
        "region": "Karnataka",
        "subtitle": "Mullayanagiri mountain vistas, private coffee estate retreats, and cozy campfire luxury sangeets in Chikmagalur.",
        "meta_desc": "Top Chikmagalur destination wedding planner. The Serai, Trivik Resorts, coffee estate weddings & transparent 0% vendor markups.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹30 Lakhs – ₹80 Lakhs (100–250 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("The Serai Chikmagalur", "Luxury private pool villas nestled inside a lush coffee plantation."),
            ("Trivik Hotels & Resorts", "Perched high on the hills with panoramic mountain valley views."),
            ("Gateway Chikmagalur (IHCL)", "Colonial-style estate cottages with expansive banquet lawns.")
        ],
        "usp_points": [
            ("☕ Estate Fresh Gastronomy", "Fresh artisanal Chikmagalur coffee stations, authentic Malnad cuisine, and live grills."),
            ("🚐 Bangalore Highway Convoys", "Coordinated chauffeur-driven fleets from Bengaluru for guests."),
            ("0% Vendor Markups", "Direct estate rental and lighting contracts.")
        ],
        "faqs": [
            ("How far is Chikmagalur from Bangalore?", "Chikmagalur is approximately a 4.5-hour smooth highway drive from Bengaluru.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-kabini",
        "title": "Destination Wedding Planner in Kabini | Riverside Wildlife Luxury - Swariya Weddings",
        "h1": "Destination Wedding Planner in Kabini",
        "category": "Destination",
        "region": "Karnataka",
        "subtitle": "Waterfront intimacy on the banks of the Kabini River, rustic luxury eco-resorts, and serene wilderness celebrations.",
        "meta_desc": "Bespoke Kabini destination wedding planner. Evolve Back Kabini, The Serai Kabini, waterfront intimacy & 0% vendor markups.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹35 Lakhs – ₹85 Lakhs (80–200 guests)",
        "ideal_season": "October to May",
        "venues": [
            ("Evolve Back, Kuruba Safari Lodge, Kabini", "Tribal-inspired luxury huts with private plunge pools on the riverbank."),
            ("The Serai Kabini", "Sprawling waterfront property with open lawns and sunset boat cruises."),
            ("Waterwoods Lodge Kabini", "Boutique colonial lodge on the edge of the wildlife reserve.")
        ],
        "usp_points": [
            ("🌿 Intimate Eco-Luxury", "Perfect for discerning couples seeking deep privacy and nature-forward aesthetics."),
            ("0% Markup Guarantee", "Direct trade rates on resort buyouts and production.")
        ],
        "faqs": [
            ("Can music be played at Kabini resorts?", "Kabini adheres to eco-acoustic guidelines; acoustic live bands and curated evening soundscapes create magical ambiance within forest norms.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-sakleshpur",
        "title": "Destination Wedding Planner in Sakleshpur | Hill Plantation Weddings - Swariya Weddings",
        "h1": "Destination Wedding Planner in Sakleshpur",
        "category": "Destination",
        "region": "Karnataka",
        "subtitle": "Misty mountain hills, spice plantations, and rustic luxury resort weddings in Sakleshpur.",
        "meta_desc": "Destination wedding planner in Sakleshpur. Western Ghats hillside resorts, coffee estate weddings & zero markup planning.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹25 Lakhs – ₹65 Lakhs (100–250 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("The Hills Resort Sakleshpur", "Swiss chalets surrounded by dense mountain foliage."),
            ("Misty Heights / Heritage Coffee Estates", "Private plantation bungalows for intimate celebrations.")
        ],
        "usp_points": [
            ("☕ Hillside Intimacy", "Cool, crisp weather and scenic Western Ghats valley backdrops.")
        ],
        "faqs": [
            ("How far is Sakleshpur from Bangalore?", "Sakleshpur is approximately a 3.5 to 4-hour scenic drive from Bangalore via the Hassan highway.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-hampi",
        "title": "Destination Wedding Planner in Hampi | UNESCO Heritage Nuptials - Swariya Weddings",
        "h1": "Destination Wedding Planner in Hampi",
        "category": "Destination",
        "region": "Karnataka",
        "subtitle": "Mythical stone temple architecture, Vijayanagara royal aesthetics, and luxury palace resort celebrations in historic Hampi.",
        "meta_desc": "Luxury destination wedding planner in Hampi. Evolve Back Kamalapura Palace, Vijayanagara architecture & 0% vendor markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹45 Lakhs – ₹1.2 Crores (100–250 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("Evolve Back, Kamalapura Palace, Hampi", "Magnificent palace resort styled after the 14th-century Vijayanagara empire."),
            ("Heritage Resort Hampi", "Eco-friendly cottage resort surrounded by dramatic boulder landscapes.")
        ],
        "usp_points": [
            ("🏛️ Regal Stone Temple Themes", "Monumental stone arches, temple brass urulis, and heritage royal decor.")
        ],
        "faqs": [
            ("How do guests travel to Hampi?", "Guests can fly into Jindal Vijayanagar Airport (VDY) or travel via luxury express trains/coaches from Bangalore.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-mysore",
        "title": "Destination Wedding Planner in Mysore | Royal Heritage Palaces - Swariya Weddings",
        "h1": "Destination Wedding Planner in Mysore",
        "category": "Destination",
        "region": "Karnataka",
        "subtitle": "Wadiyar royal heritage, Lalitha Mahal Palace, authentic Mysore Pak & Jasmine floral decor with 0% vendor markups.",
        "meta_desc": "Premier Mysore destination wedding planner. Lalitha Mahal Palace, Silent Shores, royal heritage weddings & 0% markup pricing.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹35 Lakhs – ₹95 Lakhs (150–500 guests)",
        "ideal_season": "September to March",
        "venues": [
            ("Lalitha Mahal Palace Hotel", "Italianate royal palace with grand banquet halls and majestic terraces."),
            ("Silent Shores Resort & Spa", "Sprawling lakefront resort with grand convention lawns."),
            ("Radisson Blu Plaza Hotel Mysore", "Modern luxury beneath the Chamundi Hills.")
        ],
        "usp_points": [
            ("🌺 Authentic Mysore Mallige", "World-renowned fresh Mysore jasmine garlands and royal silk styling.")
        ],
        "faqs": [
            ("How fast is travel between Bangalore and Mysore?", "Via the new Bangalore-Mysore Expressway, travel time is just 90 minutes.")
        ]
    },

    # ----------------------------------------------------
    # 5. MAHARASHTRA & NORTH HILLS
    # ----------------------------------------------------
    {
        "slug": "destination-wedding-planner-in-alibaug",
        "title": "Destination Wedding Planner in Alibaug | Luxury Beachfront Villas - Swariya Weddings",
        "h1": "Destination Wedding Planner in Alibaug",
        "category": "Destination",
        "region": "Maharashtra",
        "subtitle": "Private luxury villa buyouts, Mandwa ferry connectivity from Mumbai, and coastal beach weddings with 0% vendor markups.",
        "meta_desc": "Luxury Alibaug destination wedding planner. Private beach villas, Radisson Blu Alibaug, speedboat transfers from Mumbai & 0% markups.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹45 Lakhs – ₹1.3 Crores (100–300 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("Radisson Blu Resort & Spa Alibaug", "Sprawling luxury resort with lake courtyards and large banquet lawns."),
            ("Boutique Private Luxury Villas, Awas & Kihim", "Exclusive celebrity villas with private lawns and swimming pools.")
        ],
        "usp_points": [
            ("🛥️ Speedboat Transfers", "20-minute speedboat transfers for guests from Gateway of India, Mumbai to Mandwa.")
        ],
        "faqs": [
            ("Why is Alibaug popular for Mumbai and Pune couples?", "It offers serene beach privacy just a short catamaran ride away from South Mumbai.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-lonavala-mahabaleshwar",
        "title": "Destination Wedding Planner in Lonavala & Mahabaleshwar | Hill Resorts - Swariya Weddings",
        "h1": "Destination Wedding Planner in Lonavala & Mahabaleshwar",
        "category": "Destination",
        "region": "Maharashtra",
        "subtitle": "Sahyadri mountain valleys, strawberry farm retreats, and luxury cliffside resorts between Mumbai and Pune.",
        "meta_desc": "Top destination wedding planner in Lonavala & Mahabaleshwar. Della Resorts, Fariyas, Le Méridien Mahabaleshwar & 0% markups.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹40 Lakhs – ₹1.1 Crores (150–350 guests)",
        "ideal_season": "October to May",
        "venues": [
            ("Della Resorts, Lonavala", "High-luxury adventure resort with multiple themed banquet courtyards."),
            ("Le Méridien Mahabaleshwar Resort & Spa", "Nestled inside an evergreen forest on a cliff-edge."),
            ("Fariyas Resort Lonavala", "Scenic hillside property with grand indoor and outdoor venues.")
        ],
        "usp_points": [
            ("⛰️ Sahyadri Mountain Vistas", "Pleasant weather, scenic expressway access, and dramatic mountain valley views.")
        ],
        "faqs": [
            ("How accessible is Lonavala from Mumbai and Pune?", "Lonavala is just a 90-minute drive from both Mumbai and Pune via the Mumbai-Pune Expressway.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-mussoorie-rishikesh",
        "title": "Destination Wedding Planner in Mussoorie & Rishikesh | Ganga & Himalayas - Swariya Weddings",
        "h1": "Destination Wedding Planner in Mussoorie & Rishikesh",
        "category": "Destination",
        "region": "North",
        "subtitle": "Sacred Ganga riverbank pheras in Rishikesh and Queen of Hills mountain luxury in Mussoorie with 0% vendor markups.",
        "meta_desc": "Luxury destination wedding planner in Mussoorie & Rishikesh. JW Marriott Mussoorie, Taj Rishikesh, Ganga riverfront mandaps & 0% markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹55 Lakhs – ₹2.0 Crores (100–300 guests)",
        "ideal_season": "March to June & September to November",
        "venues": [
            ("JW Marriott Mussoorie Walnut Grove Resort & Spa", "Himalayan luxury with grand cedar tree lawns and panoramic valley views."),
            ("Taj Rishikesh Resort & Spa, Uttarakhand", "Tranquil riverbank setting on the holy Ganges with private sand beach."),
            ("The Roseate Ganges Rishikesh", "Boutique luxury villas overlooking the Himalayan foothills.")
        ],
        "usp_points": [
            ("🌊 Sacred River & Mountain Majesty", "Spiritual sanctity of Ganga Aarti integrated into the wedding festivities.")
        ],
        "faqs": [
            ("How do guests reach Rishikesh and Mussoorie?", "Guests fly into Dehradun Jolly Grant Airport (DED), located just 40 minutes from Rishikesh.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-jim-corbett",
        "title": "Destination Wedding Planner in Jim Corbett | Kosi River Resorts - Swariya Weddings",
        "h1": "Destination Wedding Planner in Jim Corbett",
        "category": "Destination",
        "region": "North",
        "subtitle": "Riverside forest luxury, Kosi riverbank mandaps, and sprawling jungle resort celebrations with 0% vendor markups.",
        "meta_desc": "Destination wedding planner in Jim Corbett. Taj Corbett, Namah, riverside forest luxury & transparent zero markup planning.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹35 Lakhs – ₹95 Lakhs (150–400 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("Taj Corbett Resort & Spa", "Sprawling Kosi riverfront property surrounded by Sal forests."),
            ("Namah Resort Jim Corbett", "Scenic riverside luxury with huge wedding lawns and ballrooms."),
            ("Aahana - The Corbett Wilderness", "Eco-luxury resort with lush organic gardens and heritage architecture.")
        ],
        "usp_points": [
            ("🌿 Serene Jungle Setting", "Immense open spaces, fresh mountain air, and high-capacity luxury resorts.")
        ],
        "faqs": [
            ("How far is Jim Corbett from Delhi NCR?", "Jim Corbett is approximately a 4.5-hour comfortable drive or direct train journey from Delhi NCR.")
        ]
    },

    # ----------------------------------------------------
    # 6. CULTURAL & COMMUNITY VERTICALS
    # ----------------------------------------------------
    {
        "slug": "gujarati-wedding-planner-bengaluru",
        "title": "Gujarati Wedding Planner in Bengaluru | Garba, Mameru & Pure Veg Feasts",
        "h1": "Gujarati Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Gol Dhana, vibrant high-energy Dandiya Raas, Mameru, Mandap Muhurat, and 100% pure vegetarian gourmet dining.",
        "meta_desc": "Leading Gujarati wedding planner in Bengaluru. Grand Garba nights, Mameru, Mandap Muhurat, pure veg/Jain catering & 0% vendor markups.",
        "hero_img": "images/4.jpg",
        "cost_range": "₹30 Lakhs – ₹1.2 Crores (250–800 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Gayatri Vihar Palace Grounds", "Massive capacity for 1,000+ guest Garba nights and multi-station feasts."),
            ("The Moongate Bangalore", "Lakefront lawns ideal for vibrant Dandiya setups and floral mandaps.")
        ],
        "usp_points": [
            ("🎉 High-Energy Garba Production", "Concert sound systems, custom Dandiya stages, and traditional Gujarati folk singers."),
            ("🍲 Authentic Gujarati & Kathiyawadi Catering", "Undhiyu, Fafda-Jalebi, live Dhokla counters, Dal Baati, and Jain gourmet menus.")
        ],
        "faqs": [
            ("Can you organize pure Jain and Swaminarayan catering in Bangalore?", "Yes, we partner with specialized Gujarati Maharaj caterers for strict Jain and pure satvik spreads.")
        ]
    },
    {
        "slug": "punjabi-sikh-wedding-planner-bengaluru",
        "title": "Punjabi & Sikh Wedding Planner in Bengaluru | Anand Karaj & Dhol Baaraat",
        "h1": "Punjabi & Sikh Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Sacred Gurudwara Anand Karaj, high-energy Jaggo nights, thunderous Dhol baaraats, and opulent cocktail receptions.",
        "meta_desc": "Expert Punjabi and Sikh wedding planner in Bengaluru. Gurudwara Anand Karaj coordination, Jaggo, Dhol, Chooda ceremony & 0% markups.",
        "hero_img": "images/4.jpg",
        "cost_range": "₹35 Lakhs – ₹1.5 Crores (200–600 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Leela Palace Bengaluru", "Grand ballroom luxury for opulent Sangeet and cocktail nights."),
            ("JW Marriott Bengaluru", "Central 5-star venue with exceptional North Indian culinary teams.")
        ],
        "usp_points": [
            ("🪔 Sacred Anand Karaj Protocol", "Respectful coordination with prominent Bangalore Gurudwaras (Ulsoor, Indiranagar)."),
            ("🥁 Thunderous Dhol Baaraat", "Live Punjabi Dhol troupes, vintage cars, and cold-pyro bridal entries.")
        ],
        "faqs": [
            ("Do you assist with Gurudwara permissions and decor in Bangalore?", "Yes, we coordinate respectful floral decor, rumala sahib offerings, and langar seating at local Gurudwaras.")
        ]
    },
    {
        "slug": "bengali-wedding-planner-bengaluru",
        "title": "Bengali Wedding Planner in Bengaluru | Saat Paake Ghomar & Biye - Swariya Weddings",
        "h1": "Bengali Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Saat Paake Ghomar, Shubho Drishti, Sindoor Daan, traditional Topor & Mukut styling, and authentic Bengali Bhoj.",
        "meta_desc": "Specialist Bengali wedding planner in Bengaluru. Saat Paake Ghomar, Bor Jatri, traditional fish and mishti catering & 0% markups.",
        "hero_img": "images/4.jpg",
        "cost_range": "₹25 Lakhs – ₹75 Lakhs (150–400 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Tamarind Tree", "Courtyard heritage setting perfectly complementing traditional Bengali rituals.")
        ],
        "usp_points": [
            ("🐟 Authentic Bengali Bhoj", "Kosha Mangsho, Bhetki Paturi, Chingri Malai Curry, Mishti Doi, and Rosogolla counters.")
        ],
        "faqs": [
            ("Can you source traditional Bengali wedding accessories in Bangalore?", "Yes, we arrange authentic Sholar Topor, Mukut, Gach Kouto, and floral Bor Mala directly.")
        ]
    },
    {
        "slug": "kerala-christian-wedding-planner-bengaluru",
        "title": "Kerala Christian Wedding Planner in Bengaluru | Cathedral Nuptials & Grand Receptions",
        "h1": "Kerala Christian Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "St. Mark's / Infant Jesus Cathedral nuptials, Manthrakodi blessing, Minnu / Thaali tying, and grand ballroom receptions.",
        "meta_desc": "Premier Kerala Christian wedding planner in Bengaluru. Church coordination, Manthrakodi, choir ensembles & grand 5-star receptions.",
        "hero_img": "images/12.jpg",
        "cost_range": "₹30 Lakhs – ₹1.2 Crores (200–600 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Taj West End Bengaluru", "Historic heritage gardens for fairytale church reception toasts."),
            ("ITC Gardenia", "Grand luxury ballrooms for 500+ guest seated multi-course banquets.")
        ],
        "usp_points": [
            ("⛪ Church Protocol Mastery", "Order of service booklets, floral aisle runners, and live choir accompaniment.")
        ],
        "faqs": [
            ("How do you manage church setup and evening reception transitions?", "Our split crews handle church floral pews in the morning and simultaneously prepare the 5-star evening ballroom.")
        ]
    },
    {
        "slug": "jain-wedding-planner-bengaluru",
        "title": "Jain Wedding Planner in Bengaluru | Chauvihar & Pure Satvik Nuptials",
        "h1": "Jain Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Khol Baroda, Lagna Lekhan, auspicious daytime Muhurthams before sunset, and strict 100% Jain gourmet catering.",
        "meta_desc": "Expert Jain wedding planner in Bengaluru. Chauvihar daytime muhurthams, strict root-vegetable-free gourmet banquets & 0% markups.",
        "hero_img": "images/4.jpg",
        "cost_range": "₹30 Lakhs – ₹1.0 Crores (200–700 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Gayatri Vihar Palace Grounds", "Dedicated separate pure veg and Jain dining halls with huge scale.")
        ],
        "usp_points": [
            ("🥕 Strict Jain Gourmet Banquets", "Zero root vegetables (onion, garlic, potato), pure cold-pressed oils, and Chauvihar service.")
        ],
        "faqs": [
            ("Do you ensure catering strictly follows Jain principles?", "Yes. We work exclusively with certified Jain Maharaj caterers who observe strict dietary standards.")
        ]
    },
    {
        "slug": "interfaith-fusion-wedding-planner-bengaluru",
        "title": "Interfaith & Fusion Wedding Planner in Bengaluru | Dual-Ceremony Specialists",
        "h1": "Interfaith & Fusion Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Harmonious two-tradition weddings, dual ceremony timelines, and multicultural hospitality executed with grace.",
        "meta_desc": "Top interfaith and fusion wedding planner in Bengaluru. Seamless dual ceremonies (e.g. South Indian & North Indian, Hindu & Christian) & 0% markups.",
        "hero_img": "images/2.jpg",
        "cost_range": "₹35 Lakhs – ₹1.5 Crores (150–500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Tamarind Tree", "Multiple distinct spaces enabling morning temple rituals and evening cocktail receptions on one property.")
        ],
        "usp_points": [
            ("🕊️ Seamless Dual Timelines", "Choreograph two distinct cultural ceremonies on the same day without guest exhaustion.")
        ],
        "faqs": [
            ("How do you design a mandap and altar for an interfaith celebration?", "We create adaptable architectural floral structures that gracefully transition between both traditions.")
        ]
    },
    {
        "slug": "luxury-intimate-wedding-planner-bengaluru",
        "title": "Luxury Intimate Wedding Planner in Bengaluru | 50 to 150 Guests - Swariya Weddings",
        "h1": "Luxury Intimate Wedding Planner in Bengaluru",
        "category": "Style",
        "region": "Bengaluru",
        "subtitle": "High-touch artisanal styling, personalized guest favors, boutique villa buyouts, and Michelin-inspired culinary banquets.",
        "meta_desc": "Luxury intimate wedding planner in Bengaluru. 50–150 guests, boutique villas, bespoke artisanal decor & 0% vendor markup pricing.",
        "hero_img": "images/13.jpg",
        "cost_range": "₹15 Lakhs – ₹45 Lakhs (50–150 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Jade 735", "Boutique party villa with pool cabanas and intimate garden lawns."),
            ("Tharavadu Mane", "Traditional Kerala wooden architecture nestled on Kanakapura Road.")
        ],
        "usp_points": [
            ("✨ High-Touch Personalization", "Handwritten guest notes, customized tasting menus, and bespoke ambient acoustic music.")
        ],
        "faqs": [
            ("Why choose an intimate wedding in Bangalore?", "It allows couples to invest heavily in ultra-luxury catering, bespoke florals, and deeply meaningful moments with closest family.")
        ]
    },

    # ----------------------------------------------------
    # 7. BENGALURU & HYDERABAD MICRO-LOCATIONS
    # ----------------------------------------------------
    {
        "slug": "wedding-planners-in-koramangala-bangalore",
        "title": "Wedding Planners in Koramangala Bangalore | Luxury Ateliers - Swariya Weddings",
        "h1": "Wedding Planners in Koramangala Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "South Bangalore's premier luxury wedding planning studio. Seamless coordination for Koramangala, HSR Layout, and Sarjapur Road couples.",
        "meta_desc": "Top wedding planners in Koramangala Bangalore. HSR studio consultation, luxury decor, venue booking & 0% vendor markups.",
        "hero_img": "images/1.jpg",
        "cost_range": "₹25 Lakhs – ₹1.2 Crores (150–500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Grand Mercure Koramangala", "Elegant central poolside lawns and ballroom banquets."),
            ("Taj MG Road / Central BLR", "5-star luxury within 15 minutes of Koramangala.")
        ],
        "usp_points": [
            ("📍 Neighboring HSR Layout Atelier", "Convenient in-person design and moodboard reviews at our HSR Sector 7 studio.")
        ],
        "faqs": [
            ("Where is Swariya Weddings located relative to Koramangala?", "Our main design atelier is located just 5 minutes away in HSR Layout Sector 7.")
        ]
    },
    {
        "slug": "wedding-planners-in-sarjapur-road-bangalore",
        "title": "Wedding Planners in Sarjapur Road Bangalore | Villa & Resort Weddings - Swariya Weddings",
        "h1": "Wedding Planners in Sarjapur Road Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Sprawling luxury villa estates, tech-corridor wedding planning, and seamless zero-markup execution on Sarjapur Road.",
        "meta_desc": "Top wedding planners in Sarjapur Road Bangalore. Resort venues, 3D mandap decor, zero vendor markups & complete event management.",
        "hero_img": "images/1.jpg",
        "cost_range": "₹25 Lakhs – ₹1.0 Crores (150–500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Tamarind Tree", "Quick access via NICE road and Kanakapura corridor."),
            ("Miraya Greens (Electronic City)", "Sprawling luxury lawns just 20 minutes from Sarjapur.")
        ],
        "usp_points": [
            ("🌿 East-South Bangalore Venue Access", "Expert management of resort venues along the Sarjapur-Varthur corridor.")
        ],
        "faqs": [
            ("Can you manage NRI family weddings on Sarjapur Road?", "Yes, over 40% of our clients in the Sarjapur tech corridor are NRI or tech leaders planning multi-day celebrations.")
        ]
    },
    {
        "slug": "wedding-planners-in-kanakapura-road-bangalore",
        "title": "Wedding Planners in Kanakapura Road Bangalore | Heritage Estate Hub - Swariya Weddings",
        "h1": "Wedding Planners in Kanakapura Road Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Bengaluru's iconic heritage wedding destination: The Tamarind Tree, Tharavadu Mane, Shankaraa Foundation, and Grape Garden.",
        "meta_desc": "Premier wedding planners on Kanakapura Road Bangalore. Tamarind Tree, Tharavadu Mane, heritage courtyard decor & 0% vendor markups.",
        "hero_img": "images/3.jpg",
        "cost_range": "₹25 Lakhs – ₹1.2 Crores (150–600 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Tamarind Tree", "Ancient banyan trees, heritage courtyards, and pond pavilions."),
            ("Tharavadu Mane", "Authentic wooden coastal Kerala estate."),
            ("Shankaraa Foundation", "Open-air terracotta cultural amphitheater.")
        ],
        "usp_points": [
            ("🌳 Heritage Corridor Pioneers", "Planned 50+ weddings across Kanakapura Road's top heritage garden properties.")
        ],
        "faqs": [
            ("What makes Kanakapura Road the most popular wedding belt in Bangalore?", "It houses Bangalore's most scenic natural heritage garden properties, offering complete tranquility away from city congestion.")
        ]
    },
    {
        "slug": "wedding-planners-in-bannerghatta-road-bangalore",
        "title": "Wedding Planners in Bannerghatta Road Bangalore | Nature & Eco Resorts - Swariya Weddings",
        "h1": "Wedding Planners in Bannerghatta Road Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Natural granite amphitheaters, eco-resort weddings, Area 83, and Royalton Leisure with 0% vendor markups.",
        "meta_desc": "Top wedding planners in Bannerghatta Road Bangalore. Area 83, Royalton Leisure, Gitanjali, eco-resort mandaps & 0% markups.",
        "hero_img": "images/14.jpg",
        "cost_range": "₹25 Lakhs – ₹90 Lakhs (150–500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Area 83", "Waterfront eco-luxury resort with lush lawns and adventure suites."),
            ("Royalton Leisure", "Natural monolithic granite amphitheater and banquet hall."),
            ("Gitanjali Wedding Venue", "Intimate natural garden setting with lush tree canopies.")
        ],
        "usp_points": [
            ("🏞️ Nature-Forward Ambience", "Scenic rocky backdrops, waterfront pavilions, and lush greenery.")
        ],
        "faqs": [
            ("How far are Bannerghatta Road venues from South Bangalore?", "Venues like Area 83 and Royalton Leisure are just 25–35 minutes from JP Nagar, Jayanagar, and HSR Layout.")
        ]
    },
    {
        "slug": "wedding-planners-in-yelahanka-bangalore",
        "title": "Wedding Planners in Yelahanka Bangalore | North Bangalore Venues - Swariya Weddings",
        "h1": "Wedding Planners in Yelahanka Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "North Bangalore's premier wedding corridor: Wiwaha, The Moongate, Royal Orchid Resort, and airport proximity.",
        "meta_desc": "Top wedding planners in Yelahanka Bangalore. Wiwaha, Moongate, Royal Orchid, airport hotel blocks & 0% vendor markups.",
        "hero_img": "images/13.jpg",
        "cost_range": "₹25 Lakhs – ₹1.2 Crores (200–800 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Wiwaha Wedding Venue", "Grand air-conditioned dining hall and 32 guest rooms."),
            ("The Moongate (Airport Road)", "10-acre lakefront lawn and amphitheater."),
            ("Royal Orchid Resort & Convention Centre", "Sprawling 8-acre convention lawn and hotel.")
        ],
        "usp_points": [
            ("✈️ Direct Kempegowda Airport Proximity", "Just 20 minutes from BLR Airport, ideal for international and outstation guests.")
        ],
        "faqs": [
            ("Why is Yelahanka ideal for destination guests?", "Guests arriving at Bangalore Airport can reach Yelahanka hotels in 20 minutes without entering city traffic.")
        ]
    },
    {
        "slug": "wedding-planners-in-nandi-hills-bangalore",
        "title": "Wedding Planners in Nandi Hills Bangalore | Mountain Amphitheaters - Swariya Weddings",
        "h1": "Wedding Planners in Nandi Hills Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Breathtaking mountain amphitheater weddings: Amita Rasa, White Mist, and foothills luxury with 0% vendor markups.",
        "meta_desc": "Top wedding planners in Nandi Hills Bangalore. Amita Rasa amphitheater, White Mist, mountain backdrops & 0% vendor markup pricing.",
        "hero_img": "images/3.jpg",
        "cost_range": "₹30 Lakhs – ₹1.1 Crores (150–600 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("Amita Rasa", "Open-air stone amphitheater with monumental Nandi Hills mountain vistas."),
            ("White Mist by Happy Retreats", "Foothill retreat with misty morning lawns and modern villas."),
            ("JW Marriott Bengaluru Prestige Golfshire Resort & Spa", "Ultra-luxury golf course resort at the base of Nandi Hills.")
        ],
        "usp_points": [
            ("⛰️ Dramatic Mountain Horizons", "Unmatched sunset backdrops behind your central wedding mandap.")
        ],
        "faqs": [
            ("How far is Nandi Hills from Bangalore Airport?", "Nandi Hills wedding properties are just 30–40 minutes from BLR International Airport.")
        ]
    },
    {
        "slug": "wedding-planners-in-gachibowli-hyderabad",
        "title": "Wedding Planners in Gachibowli Hyderabad | Financial District Luxury - Swariya Weddings",
        "h1": "Wedding Planners in Gachibowli Hyderabad",
        "category": "Local",
        "region": "Hyderabad",
        "subtitle": "Luxury hotel ballrooms, modern convention lawns, and high-tech corporate wedding planning in Gachibowli & Hitec City.",
        "meta_desc": "Premier wedding planners in Gachibowli Hyderabad. Financial District luxury hotels, 3D decor, Telugu & Marwari weddings & 0% markups.",
        "hero_img": "images/4.jpg",
        "cost_range": "₹35 Lakhs – ₹1.5 Crores (200–800 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Sheraton Hyderabad Hotel", "Opulent ballroom facilities and poolside celebration lawns."),
            ("Oakwood Residence Kapil Hyderabad", "Contemporary luxury suites for residential wedding blocks."),
            ("Boulder Hills Golf and Country Club", "Manicured green golf course lawns for grand evening receptions.")
        ],
        "usp_points": [
            ("🏙️ Financial District Scale", "Modern 5-star infrastructure with seamless airport ORR highway connectivity.")
        ],
        "faqs": [
            ("Does Swariya execute weddings in Hyderabad?", "Yes! We operate dedicated production crews in Hyderabad for Telugu, Marwari, and destination nuptials.")
        ]
    },
    {
        "slug": "wedding-planners-in-jubilee-hills-hyderabad",
        "title": "Wedding Planners in Jubilee Hills Hyderabad | Elite Heritage & Luxury - Swariya Weddings",
        "h1": "Wedding Planners in Jubilee Hills Hyderabad",
        "category": "Local",
        "region": "Hyderabad",
        "subtitle": "Bespoke high-society weddings, private luxury banquet lawns, and Telugu & Marwari grandeur in Jubilee & Banjara Hills.",
        "meta_desc": "Top wedding planners in Jubilee Hills Hyderabad. Luxury Telugu nuptials, royal decor, Taj Krishna & 0% vendor markup planning.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹45 Lakhs – ₹2.5 Crores (250–1,000 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Taj Krishna & Taj Deccan (Banjara Hills)", "Iconic heritage luxury with grand outdoor lawns and ballrooms."),
            ("JRC Convention Centre", "Massive high-tech convention facility for 1,000+ guest royal weddings."),
            ("N Convention (Madhapur)", "Waterfront luxury convention facility in the heart of the city.")
        ],
        "usp_points": [
            ("👑 Royal Hyderabadi Grandeur", "Authentic Biryani & Hyderabadi culinary curations alongside traditional Andhra Bhojanam.")
        ],
        "faqs": [
            ("Can Swariya coordinate royal Hyderabadi and Telugu weddings in Jubilee Hills?", "Yes, we handle complete priest arrangements, floral jada styling, and monumental mandap architecture.")
        ]
    },
    {
        "slug": "wedding-planners-in-ecr-chennai",
        "title": "Wedding Planners in ECR Chennai | Beachfront Luxury Resorts - Swariya Weddings",
        "h1": "Wedding Planners in ECR Chennai",
        "category": "Local",
        "region": "Chennai",
        "subtitle": "East Coast Road beachfront resorts, ocean-facing mandaps, and Tamil Brahmin & fusion luxury celebrations with 0% vendor markups.",
        "meta_desc": "Top wedding planners in ECR Chennai. Beachfront resorts, InterContinental Mahabalipuram, ocean lawns & 0% vendor markup pricing.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹35 Lakhs – ₹1.2 Crores (150–450 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("InterContinental Chennai Mahabalipuram Resort", "Luxury beachfront property with world-class banquet lawns."),
            ("Sheraton Grand Chennai Resort & Spa", "Expansive ocean lawns directly on the Bay of Bengal."),
            ("MGM Beach Resorts ECR", "Charming coastal resort with palm-fringed private beaches.")
        ],
        "usp_points": [
            ("🌊 Bay of Bengal Oceanfront", "Golden sunrise and sunset mandaps on East Coast Road's finest sands.")
        ],
        "faqs": [
            ("Why choose ECR Chennai for a destination wedding?", "ECR combines Chennai airport proximity with stunning beachfront 5-star properties and rich cultural Tamil heritage.")
        ]
    },
    {
        "slug": "wedding-planners-in-south-mumbai",
        "title": "Wedding Planners in South Mumbai | Iconic Heritage Luxury - Swariya Weddings",
        "h1": "Wedding Planners in South Mumbai",
        "category": "Local",
        "region": "Mumbai",
        "subtitle": "Taj Mahal Palace, Marine Drive luxury hotels, and high-profile society weddings in South Mumbai with 0% vendor markups.",
        "meta_desc": "Premier wedding planners in South Mumbai. Taj Mahal Palace, Marine Drive 5-star venues, Parsi & Marwari weddings & 0% markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹60 Lakhs – ₹3.0 Crores (200–800 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("The Taj Mahal Palace, Mumbai", "World-renowned historic flagship with the legendary Ballroom and Crystal Room."),
            ("The Oberoi & Trident, Nariman Point", "Panoramic Arabian Sea views along Marine Drive."),
            ("The St. Regis Mumbai (Lower Parel)", "Astor Ballroom luxury with multi-tier celebration spaces.")
        ],
        "usp_points": [
            ("🏛️ Iconic Mumbai Heritage", "Prestigious heritage architecture paired with flawless logistical precision.")
        ],
        "faqs": [
            ("How does Swariya manage luxury weddings in South Mumbai?", "We provide complete end-to-end luxury management, from 5-star hotel buyout negotiations to bespoke 3D spatial decor design.")
        ]
    },
    {
        "slug": "wedding-planners-in-bandra-mumbai",
        "title": "Wedding Planners in Bandra Mumbai | Seafront & Boutique Luxury - Swariya Weddings",
        "h1": "Wedding Planners in Bandra Mumbai",
        "category": "Local",
        "region": "Mumbai",
        "subtitle": "Taj Lands End, Bandra Bandstand seafront lawns, and chic bohemian luxury wedding coordination with 0% vendor markups.",
        "meta_desc": "Top wedding planners in Bandra Mumbai. Taj Lands End, seaside lawns, celebrity styling, cocktail nights & transparent pricing.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹50 Lakhs – ₹2.0 Crores (150–500 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("Taj Lands End, Bandra", "Seaside Lawns overlooking the Arabian Sea and Bandra-Worli Sea Link."),
            ("Grand Hyatt Mumbai", "Sprawling luxury ballrooms and outdoor courtyards.")
        ],
        "usp_points": [
            ("🌊 Sea-Link Sunset Backdrops", "Iconic Arabian Sea sunset views for cocktail sangeets and pheras.")
        ],
        "faqs": [
            ("Can you coordinate beach/seafront setups in Bandra?", "Yes, Taj Lands End seaside lawns provide direct ocean views with full 5-star amenities.")
        ]
    },
    {
        "slug": "wedding-planners-in-jp-nagar-bangalore",
        "title": "Wedding Planners in JP Nagar Bangalore | South Bangalore Weddings - Swariya Weddings",
        "h1": "Wedding Planners in JP Nagar Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "South Bangalore's cultural heritage heart: traditional Brahmin, Kannada & Telugu weddings in JP Nagar and Jayanagar with 0% vendor markups.",
        "meta_desc": "Top wedding planners in JP Nagar Bangalore. Traditional Kannada & Telugu mandap decor, plantain leaf oota & 0% vendor markups.",
        "hero_img": "images/2.jpg",
        "cost_range": "₹20 Lakhs – ₹80 Lakhs (200–600 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Tamarind Tree (Kanakapura Road)", "Just 15 minutes from JP Nagar via outer ring road."),
            ("MLR Convention Centre JP Nagar", "Modern air-conditioned convention hall with high-capacity dining.")
        ],
        "usp_points": [
            ("🌸 South Bangalore Ritual Mastery", "Expert Vedic priests, authentic plantain leaf oota, and traditional floral decor.")
        ],
        "faqs": [
            ("Do you manage traditional wedding halls in JP Nagar?", "Yes, we manage both modern AC convention centers and heritage outdoor properties around JP Nagar.")
        ]
    },
    {
        "slug": "wedding-planners-in-jayanagar-bangalore",
        "title": "Wedding Planners in Jayanagar Bangalore | Heritage & Tradition - Swariya Weddings",
        "h1": "Wedding Planners in Jayanagar Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Classic South Bengaluru elegance: traditional Kannada, Tamil, and Telugu wedding planning in Jayanagar with 0% vendor markups.",
        "meta_desc": "Premier wedding planners in Jayanagar Bangalore. Traditional Muhurtham rituals, Nadaswaram, authentic catering & transparent pricing.",
        "hero_img": "images/2.jpg",
        "cost_range": "₹20 Lakhs – ₹85 Lakhs (200–700 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Shalimar Convention Hall Jayanagar", "Classic South Bangalore central wedding venue."),
            ("Taj West End / Kanakapura Heritage", "Easily accessible from Jayanagar via central arterial roads.")
        ],
        "usp_points": [
            ("🪔 Vedic Heritage Specialists", "Deep expertise in traditional Kannada, Iyengar, and Telugu wedding customs.")
        ],
        "faqs": [
            ("How does Swariya manage early morning Muhurthams in Jayanagar?", "Our logistics crews are on-site by 3:00 AM ensuring temple flowers, hot filter coffee, and priest setups are flawless.")
        ]
    },
    {
        "slug": "wedding-planners-in-electronic-city-bangalore",
        "title": "Wedding Planners in Electronic City Bangalore | Miraya Greens & Luxury Resorts",
        "h1": "Wedding Planners in Electronic City Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Sprawling luxury garden resorts: Miraya Greens, Royal Palms, and high-capacity destination wedding planning in Electronic City.",
        "meta_desc": "Top wedding planners in Electronic City Bangalore. Miraya Greens, Royal Palms, resort weddings & 0% vendor markup pricing.",
        "hero_img": "images/13.jpg",
        "cost_range": "₹25 Lakhs – ₹1.2 Crores (250–1,000 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Miraya Greens", "Glass House, Magnolia Lawn, and 22 luxury guest rooms."),
            ("Royal Palms", "Palm-fringed celebration lawns for grand receptions.")
        ],
        "usp_points": [
            ("🏰 Sprawling Resort Capacities", "Massive open-air lawns accommodating 500 to 1,500 guests with on-site accommodation.")
        ],
        "faqs": [
            ("Can outstation guests be accommodated at Electronic City venues?", "Yes, properties like Miraya Greens offer on-site luxury villas and guest suites.")
        ]
    },
    {
        "slug": "wedding-planners-in-sadashivanagar-bangalore",
        "title": "Wedding Planners in Sadashivanagar Bangalore | Elite Luxury Nuptials - Swariya Weddings",
        "h1": "Wedding Planners in Sadashivanagar Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "High-society bespoke wedding design, Palace Grounds royal access, and 5-star hotel coordination in Sadashivanagar.",
        "meta_desc": "Premier wedding planners in Sadashivanagar Bangalore. Palace Grounds access, 5-star luxury hotels, 3D architectural decor & 0% markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹50 Lakhs – ₹2.5 Crores (300–1,500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Gayatri Vihar & Sheesh Mahal (Palace Grounds)", "Direct 5-minute access from Sadashivanagar."),
            ("Taj West End Bengaluru", "Heritage gardens on Race Course Road.")
        ],
        "usp_points": [
            ("👑 Elite High-Touch Coordination", "VIP protocol management, valet routing, and monumental floral architecture.")
        ],
        "faqs": [
            ("How close is Sadashivanagar to Palace Grounds venues?", "Sadashivanagar borders Palace Grounds directly, providing 3-minute transit to top royal venues.")
        ]
    },
    {
        "slug": "wedding-planners-in-malleshwaram-bangalore",
        "title": "Wedding Planners in Malleshwaram Bangalore | Heritage & Temple Traditions - Swariya Weddings",
        "h1": "Wedding Planners in Malleshwaram Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Vedic rituals, temple mandap decor, and authentic traditional South Indian feasts in historic Malleshwaram.",
        "meta_desc": "Expert wedding planners in Malleshwaram Bangalore. Traditional Kannada & Tamil Brahmin weddings, temple decor & 0% vendor markups.",
        "hero_img": "images/2.jpg",
        "cost_range": "₹20 Lakhs – ₹75 Lakhs (200–600 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Canara Union Malleshwaram", "Classic community cultural center."),
            ("Palace Grounds Banquets", "5 minutes from Malleshwaram.")
        ],
        "usp_points": [
            ("🌺 Temple Jasmine & Marigold Art", "Authentic torans, brass lamps, and heritage floral mandap designs.")
        ],
        "faqs": [
            ("Do you handle plantain leaf catering in Malleshwaram?", "Yes, we partner with premier traditional vanta masters for multi-course authentic oota.")
        ]
    },
    {
        "slug": "wedding-planners-in-hebbal-bangalore",
        "title": "Wedding Planners in Hebbal Bangalore | Lakefront & Airport Corridor - Swariya Weddings",
        "h1": "Wedding Planners in Hebbal Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Hebbal lakefront 5-star hotels, airport expressway connectivity, and modern luxury wedding productions.",
        "meta_desc": "Top wedding planners in Hebbal Bangalore. Courtyard by Marriott Hebbal, Palace Grounds access & transparent 0% vendor markups.",
        "hero_img": "images/13.jpg",
        "cost_range": "₹30 Lakhs – ₹1.2 Crores (200–800 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Courtyard by Marriott Bengaluru Hebbal", "Modern luxury ballroom with views of Nagavara Lake."),
            ("Four Seasons Hotel Bengaluru (Mekhri Circle)", "Ultra-luxury ballrooms and poolside terrace banquets.")
        ],
        "usp_points": [
            ("✈️ Airport Highway Connectivity", "Effortless 25-minute transit for outstation guests from BLR Airport.")
        ],
        "faqs": [
            ("Why is Hebbal popular for residential weddings?", "It connects seamlessly to both Palace Grounds and Bangalore Airport.")
        ]
    },
    {
        "slug": "wedding-planners-in-bellandur-bangalore",
        "title": "Wedding Planners in Bellandur Bangalore | TempleTree & Outer Ring Road - Swariya Weddings",
        "h1": "Wedding Planners in Bellandur Bangalore",
        "category": "Local",
        "region": "Bengaluru",
        "subtitle": "Eco-thatched open-air lawns, TempleTree Leisure, and seamless tech-corridor wedding coordination in Bellandur.",
        "meta_desc": "Top wedding planners in Bellandur Bangalore. TempleTree Leisure, Aloft, tech corridor wedding planning & 0% vendor markups.",
        "hero_img": "images/14.jpg",
        "cost_range": "₹25 Lakhs – ₹90 Lakhs (150–500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("TempleTree Leisure", "Balinese thatched courtyards and open-air lawns in the heart of Bellandur."),
            ("Aloft Bengaluru Cessna Business Park", "Modern 5-star ballrooms and poolside deck.")
        ],
        "usp_points": [
            ("🌿 Eco-Thatched Aesthetics", "Natural open-air rustic ambiance in central East-South Bangalore.")
        ],
        "faqs": [
            ("What is special about TempleTree Leisure Bellandur?", "It offers an eco-thatched resort atmosphere right inside the city without long highway travel.")
        ]
    },
    {
        "slug": "wedding-planners-in-banjara-hills-hyderabad",
        "title": "Wedding Planners in Banjara Hills Hyderabad | Royal Luxury Banquets - Swariya Weddings",
        "h1": "Wedding Planners in Banjara Hills Hyderabad",
        "category": "Local",
        "region": "Hyderabad",
        "subtitle": "Taj Krishna, Park Hyatt, and high-society Telugu and Marwari wedding celebrations in Banjara Hills with 0% vendor markups.",
        "meta_desc": "Premier wedding planners in Banjara Hills Hyderabad. Taj Krishna, Park Hyatt, royal decor & transparent zero markup planning.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹45 Lakhs – ₹2.5 Crores (250–1,000 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Taj Krishna Hyderabad", "Grand ballrooms and historic garden lawns overlooking the city."),
            ("Park Hyatt Hyderabad", "Ultra-luxury hotel in the heart of Banjara Hills Road No. 2.")
        ],
        "usp_points": [
            ("👑 Royal Hyderabadi Scale", "Monolithic floral mandaps, celebrity artist management, and 1,000+ guest dining.")
        ],
        "faqs": [
            ("Do you handle Marwari and Telugu fusion weddings in Banjara Hills?", "Yes, we specialize in multi-event high-scale celebrations.")
        ]
    },
    {
        "slug": "wedding-planners-in-shamshabad-hyderabad",
        "title": "Wedding Planners in Shamshabad Hyderabad | Palace & Airport Resorts - Swariya Weddings",
        "h1": "Wedding Planners in Shamshabad Hyderabad",
        "category": "Local",
        "region": "Hyderabad",
        "subtitle": "Falaknuma Palace corridor, Rajiv Gandhi Airport luxury resorts, and monumental royal wedding productions in Shamshabad.",
        "meta_desc": "Luxury wedding planners in Shamshabad Hyderabad. Taj Falaknuma corridor, Novotel Airport, royal baaraat & 0% markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹50 Lakhs – ₹3.0 Crores (200–1,200 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Taj Falaknuma Palace (Corridor)", "Historic 101-seat dining hall and royal palace courtyards."),
            ("Novotel Hyderabad Airport", "Massive outdoor celebration arena and convention ballrooms.")
        ],
        "usp_points": [
            ("✈️ Direct Airport Luxury", "Zero guest commute from Hyderabad International Airport (HYD).")
        ],
        "faqs": [
            ("Can you manage large destination weddings in Shamshabad?", "Yes, Novotel Airport and surrounding palace properties accommodate up to 1,500 guests.")
        ]
    },
    {
        "slug": "wedding-planners-in-mahabalipuram-chennai",
        "title": "Wedding Planners in Mahabalipuram Chennai | UNESCO Beachfront Luxury - Swariya Weddings",
        "h1": "Wedding Planners in Mahabalipuram Chennai",
        "category": "Destination",
        "region": "Chennai",
        "subtitle": "Shore Temple oceanfront scenery, 5-star beachfront resorts, and luxury coastal Tamil and fusion weddings.",
        "meta_desc": "Top wedding planners in Mahabalipuram Chennai. InterContinental, Radisson Blu Temple Bay, beach mandaps & 0% vendor markups.",
        "hero_img": "images/10.jpg",
        "cost_range": "₹40 Lakhs – ₹1.4 Crores (150–500 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("Radisson Blu Resort Temple Bay", "44-acre beachfront property with an expansive 27,000 sq ft meandering pool."),
            ("InterContinental Chennai Mahabalipuram", "World-class luxury beachfront lawns and ballrooms.")
        ],
        "usp_points": [
            ("🌊 Shore Temple Scenery", "Ancient UNESCO rock-cut temple heritage paired with modern 5-star beach luxury.")
        ],
        "faqs": [
            ("How far is Mahabalipuram from Chennai Airport?", "Mahabalipuram is approximately a 50-minute scenic drive along the East Coast Road (ECR).")
        ]
    },
    {
        "slug": "wedding-planners-in-central-delhi-ncr",
        "title": "Wedding Planners in Central Delhi NCR | Lutyens & 5-Star Heritage - Swariya Weddings",
        "h1": "Wedding Planners in Central Delhi NCR",
        "category": "Local",
        "region": "Delhi",
        "subtitle": "Taj Mahal Hotel Man Singh, The Leela Palace Chanakyapuri, and iconic luxury wedding management in Central Delhi.",
        "meta_desc": "Premier wedding planners in Central Delhi. Lutyens luxury, Taj Man Singh, Leela Chanakyapuri, royal decor & 0% vendor markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹60 Lakhs – ₹3.5 Crores (250–1,000 guests)",
        "ideal_season": "October to March",
        "venues": [
            ("The Leela Palace New Delhi (Chanakyapuri)", "Grand royal ballrooms and terrace banquet spaces."),
            ("Taj Mahal Hotel (Man Singh Road)", "Historic Delhi landmark for high-profile weddings."),
            ("The Imperial New Delhi (Janpath)", "Victorian colonial elegance and manicured lawns.")
        ],
        "usp_points": [
            ("🏛️ Lutyens Delhi Prestigious Scale", "Diplomatic enclave grandeur with world-class hospitality.")
        ],
        "faqs": [
            ("How does Swariya execute luxury weddings in Delhi?", "We dispatch senior production directors and master florists 48 hours prior to the event for flawless delivery.")
        ]
    },
    {
        "slug": "wedding-planners-in-gurgaon-ncr",
        "title": "Wedding Planners in Gurgaon NCR | The Oberoi & Heritage Resorts - Swariya Weddings",
        "h1": "Wedding Planners in Gurgaon NCR",
        "category": "Local",
        "region": "Delhi",
        "subtitle": "The Oberoi Gurgaon, ITC Grand Bharat, and modern luxury farmhouse and hotel wedding productions in Millennium City.",
        "meta_desc": "Top wedding planners in Gurgaon NCR. The Oberoi, ITC Grand Bharat, luxury farmhouse weddings & 0% vendor markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹50 Lakhs – ₹2.5 Crores (200–800 guests)",
        "ideal_season": "October to April",
        "venues": [
            ("ITC Grand Bharat (Gurgaon)", "Palatial 300-acre retreat designed after ancient Indian dynasties."),
            ("The Oberoi, Gurgaon", "Waterbody courtyard and contemporary architectural luxury."),
            ("Karma Lakelands", "Eco-luxury golf resort with sprawling banquet lawns.")
        ],
        "usp_points": [
            ("🏰 Palatial Farmhouse & Resort Scale", "Massive acreage venues ideal for 3-day residential celebrations.")
        ],
        "faqs": [
            ("Can you manage residential weddings at ITC Grand Bharat?", "Yes, we handle complete guest concierge, golf cart transfers, and multi-venue theming.")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-munnar-kerala",
        "title": "Destination Wedding Planner in Munnar Kerala | Tea Plantation Mist - Swariya Weddings",
        "h1": "Destination Wedding Planner in Munnar Kerala",
        "category": "Destination",
        "region": "Kerala",
        "subtitle": "Emerald tea garden valleys, cool mountain mist, and romantic hill-station resort celebrations in Munnar.",
        "meta_desc": "Luxury destination wedding planner in Munnar Kerala. Tea estate resorts, cool hill weather, intimate mandaps & 0% markups.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹30 Lakhs – ₹75 Lakhs (80–200 guests)",
        "ideal_season": "September to May",
        "venues": [
            ("Fragrant Nature Munnar", "Boutique luxury resort perched high above tea plantations."),
            ("The Tall Trees Munnar", "66 acres of shola trees and cardamom plantations.")
        ],
        "usp_points": [
            ("☕ Tea Estate Panoramas", "Cool highland climate and misty mountain valleys.")
        ],
        "faqs": [
            ("How do guests reach Munnar?", "Munnar is a 3-hour scenic drive from Cochin International Airport (COK).")
        ]
    },
    {
        "slug": "destination-wedding-planner-in-wayanad-kerala",
        "title": "Destination Wedding Planner in Wayanad Kerala | Rainforest Vistas - Swariya Weddings",
        "h1": "Destination Wedding Planner in Wayanad Kerala",
        "category": "Destination",
        "region": "Kerala",
        "subtitle": "Western Ghats rainforests, spice estates, and serene mountain eco-resort weddings in Wayanad.",
        "meta_desc": "Destination wedding planner in Wayanad Kerala. Vythiri Resort, rainforest eco-luxury, private villa buyouts & 0% markups.",
        "hero_img": "images/15.jpg",
        "cost_range": "₹30 Lakhs – ₹75 Lakhs (80–200 guests)",
        "ideal_season": "October to May",
        "venues": [
            ("Vythiri Resort Wayanad", "Lush rainforest property with natural streams and treehouses."),
            ("The Windflower Resorts & Spa Wayanad", "Tea estate resort with open-air celebration lawns.")
        ],
        "usp_points": [
            ("🌿 Dense Rainforest Serenity", "Total immersion in nature for unforgettable intimate ceremonies.")
        ],
        "faqs": [
            ("Which airport is closest to Wayanad?", "Calicut International Airport (CCJ) or Kannur Airport (CNN) are approximately 2 to 2.5 hours away.")
        ]
    },
    {
        "slug": "sindhi-wedding-planner-bengaluru",
        "title": "Sindhi Wedding Planner in Bengaluru | Santh, Saag & High-Octane Sangeet",
        "h1": "Sindhi Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Santh, Ghari Pooja, Navgrahi, high-energy Bollywood Sangeet, and authentic Sindhi Kadi & Sai Bhaji feasts.",
        "meta_desc": "Expert Sindhi wedding planner in Bengaluru. Santh ceremony, grand Sangeet production, royal baaraat & transparent 0% markups.",
        "hero_img": "images/4.jpg",
        "cost_range": "₹35 Lakhs – ₹1.5 Crores (250–800 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Leela Palace Bengaluru", "Grand Ballroom luxury for high-octane Sangeet productions."),
            ("JW Marriott Bengaluru", "Central location with premier cocktail and dining banquet teams.")
        ],
        "usp_points": [
            ("🎉 High-Octane Sangeet & DJ Night", "Concert lighting truss, LED walls, and celebrity DJ curation.")
        ],
        "faqs": [
            ("Can you organize authentic Sindhi cuisine?", "Yes, we curate authentic Sindhi Kadi, Sai Bhaji, Dal Pakwan, and Teyvan for lunch and dinner banquets.")
        ]
    },
    {
        "slug": "konkani-wedding-planner-bengaluru",
        "title": "Konkani Wedding Planner in Bengaluru | GSB & Mangalorean Traditions",
        "h1": "Konkani Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "GSB and Mangalorean Konkani rituals: Phool Muddi, Voddli Raat, Kanyadaan, and authentic coastal feasts.",
        "meta_desc": "Top Konkani wedding planner in Bengaluru. GSB & Mangalorean rituals, Phool Muddi, coastal cuisine & transparent zero markups.",
        "hero_img": "images/2.jpg",
        "cost_range": "₹25 Lakhs – ₹85 Lakhs (200–600 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("The Tamarind Tree", "Heritage natural setting ideal for GSB rituals."),
            ("Wiwaha Wedding Venue", "High-capacity traditional dining and mandap facilities.")
        ],
        "usp_points": [
            ("🥥 Authentic GSB & Coastal Catering", "Gajbaje, Bibbe Upkari, Dalitoy, Pathrode, and authentic coastal delicacies.")
        ],
        "faqs": [
            ("Do you handle GSB priest coordination in Bangalore?", "Yes, we coordinate experienced GSB purohits for authentic Vedic shloka recitation.")
        ]
    },
    {
        "slug": "royal-grand-wedding-planner-bengaluru",
        "title": "Royal & Grand Wedding Planner in Bengaluru | 1,000+ Guests - Swariya Weddings",
        "h1": "Royal & Grand Wedding Planner in Bengaluru",
        "category": "Style",
        "region": "Bengaluru",
        "subtitle": "Monumental Palace Grounds productions, 1,000 to 5,000+ guest hospitality, VIP security, and royal baaraat management.",
        "meta_desc": "Premier grand scale wedding planner in Bengaluru. 1,000+ guests, Palace Grounds, Gayatri Vihar, VIP logistics & 0% vendor markups.",
        "hero_img": "images/11.jpg",
        "cost_range": "₹1.2 Crores – ₹5.0 Crores+ (1,000–5,000+ guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Gayatri Vihar (Palace Grounds)", "Massive royal hall accommodating up to 3,500 guests."),
            ("Sheesh Mahal (Palace Grounds)", "Opulent glass-mosaic royal palace banquet venue.")
        ],
        "usp_points": [
            ("👑 Monumental Crowd & Valet Flow", "Separate VIP entry lanes, 500+ car valet coordination, and multi-kitchen catering hubs.")
        ],
        "faqs": [
            ("How does Swariya manage 2,000+ guest weddings without chaos?", "We deploy dedicated zonal stage managers, radio-connected security leads, and synchronized buffet replenishments.")
        ]
    },
    {
        "slug": "brahmin-traditional-wedding-planner-bengaluru",
        "title": "Brahmin Traditional Wedding Planner in Bengaluru | Vedic Shloka Precision",
        "h1": "Brahmin Traditional Wedding Planner in Bengaluru",
        "category": "Cultural",
        "region": "Bengaluru",
        "subtitle": "Vedic Homam, early morning Brahma Muhurtham, Nandi Pooja, and authentic plantain leaf Oota with 0% vendor markups.",
        "meta_desc": "Expert Brahmin wedding planner in Bengaluru. Vedic muhurtham rituals, homam setup, Malli floral decor, pure veg oota & 0% markups.",
        "hero_img": "images/2.jpg",
        "cost_range": "₹18 Lakhs – ₹65 Lakhs (150–500 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Tharavadu Mane", "Traditional wooden architecture providing deep spiritual resonance."),
            ("The Tamarind Tree", "Sacred temple pond and banyan tree mandap settings.")
        ],
        "usp_points": [
            ("🪔 4:00 AM Brahma Muhurtham Readiness", "Fresh jasmine garlands, holy fire wood (Samidha), and filter coffee ready on time.")
        ],
        "faqs": [
            ("Can you coordinate authentic Brahmin Purohits?", "Yes, we work with renowned Vedic scholars for Madhwa, Smartha, Iyer, and Iyengar traditions.")
        ]
    },
    {
        "slug": "eco-friendly-sustainable-wedding-planner-bengaluru",
        "title": "Eco-Friendly & Sustainable Wedding Planner in Bengaluru | Zero-Waste Nuptials",
        "h1": "Eco-Friendly & Sustainable Wedding Planner in Bengaluru",
        "category": "Style",
        "region": "Bengaluru",
        "subtitle": "Zero single-use plastic, seed paper wedding invitations, organic locally-sourced florals, and food donation coordination.",
        "meta_desc": "Leading eco-friendly wedding planner in Bengaluru. Zero-waste weddings, sustainable decor, seed paper invites & 0% vendor markups.",
        "hero_img": "images/3.jpg",
        "cost_range": "₹20 Lakhs – ₹80 Lakhs (100–400 guests)",
        "ideal_season": "Year-round",
        "venues": [
            ("Amita Rasa (Nandi Hills)", "Eco-luxury amphitheater designed with natural stone and solar energy."),
            ("Shankaraa Foundation", "Open-air terracotta cultural village.")
        ],
        "usp_points": [
            ("🌱 Zero-Waste Certification", "Complete composting of wet waste, reusable clay crockery, and leftover meal donation.")
        ],
        "faqs": [
            ("How do you ensure zero single-use plastic at weddings?", "We utilize copper water dispensers, glass bottles, cloth welcome bags, and compostable dining materials.")
        ]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
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
    <link rel="canonical" href="https://swariyaweddings.com/{slug}.html">
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
    <meta property="og:url" content="https://swariyaweddings.com/{slug}.html">
    <meta property="og:image" content="https://swariyaweddings.com/{hero_img}">

    <!-- JSON-LD Schemas -->
    <script type="application/ld+json">
    {json_ld_service}
    </script>

    <script type="application/ld+json">
    {json_ld_breadcrumbs}
    </script>

    <script type="application/ld+json">
    {json_ld_faqs}
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
            margin-bottom: 18px;
            font-family: var(--font-heading);
        }}
        .hub-hero p {{
            font-size: 1.15rem;
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
        }}
        .btn-gold-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.5);
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
            padding: 70px 0;
        }}
        .venue-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
            gap: 25px;
            margin-top: 35px;
        }}
        .venue-card {{
            background: #fff;
            border-radius: 12px;
            border: 1px solid var(--border-gold);
            padding: 28px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.05);
            transition: 0.3s;
        }}
        .venue-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(212, 175, 55, 0.2);
            border-color: var(--accent);
        }}
        .venue-card h3 {{
            color: var(--primary);
            font-size: 1.25rem;
            margin-bottom: 10px;
        }}
        .venue-tag {{
            display: inline-block;
            background: rgba(212, 175, 55, 0.15);
            color: #7A5B0B;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .feature-box {{
            background: linear-gradient(180deg, #FAF6F0 0%, #F5EDE0 100%);
            border-radius: 14px;
            padding: 35px;
            border: 1px solid var(--border-gold);
            margin: 40px 0;
        }}
        .faq-item {{
            background: #fff;
            border: 1px solid var(--border-gold);
            border-radius: 10px;
            padding: 22px 26px;
            margin-bottom: 15px;
        }}
        .faq-item h3 {{
            font-size: 1.15rem;
            color: var(--dark-luxury);
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
            <p class="section-label" style="color: var(--accent-light);">✦ BESPOKE WEDDING PRODUCTION • {region_upper}</p>
            <h1>{h1}</h1>
            <p>{subtitle}</p>
            <div class="hub-cta-group">
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20we%20are%20planning%20our%20wedding%20in%20{slug_escaped}!%20Can%20we%20discuss%20venues%20and%20packages?" class="btn-gold-primary" target="_blank" rel="noopener">Inquire on WhatsApp</a>
                <a href="wedding-budget-calculator.html" class="btn-outline-white">Calculate {region} Budget</a>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="container hub-section">

        <!-- Why Choose Swariya -->
        <div class="feature-box">
            <div style="max-width: 850px; margin: 0 auto; text-align: center;">
                <p class="section-label">✦ THE SWARIYA STANDARD</p>
                <h2 style="font-size: 2rem; color: var(--primary); margin-bottom: 15px;">Flawless Execution with 100% Financial Transparency</h2>
                <p style="color: #444; line-height: 1.7; font-size: 1.05rem;">
                    Swariya Weddings operates on an unbending fiduciary standard: <strong>0% vendor markups</strong>. You pay actual hotel room blocks, decorator rentals, and caterer fees directly, saving an average of 15–20% while receiving in-house 3D design and on-ground production.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 30px;">
                {usp_html}
            </div>
        </div>

        <!-- Curated Venues Section -->
        {venues_html}

        <!-- FAQs -->
        <div style="margin-top: 60px;">
            <p class="section-label">✦ FREQUENTLY ASKED QUESTIONS</p>
            <h2 style="font-size: 2rem; color: var(--dark-luxury); margin-bottom: 25px;">{h1} FAQs</h2>
            {faqs_html}
        </div>

        <!-- Call to Action Banner -->
        <div style="background: radial-gradient(circle at 50% 50%, #15382e 0%, #0a1c18 100%); color: white; border-radius: 16px; padding: 45px; text-align: center; margin-top: 60px; border: 1.5px solid var(--border-gold);">
            <h2 style="color: #FAF6F0; font-size: 2.2rem; margin-bottom: 12px; font-family: var(--font-heading);">Begin Planning Your Celebration</h2>
            <p style="max-width: 680px; margin: 0 auto 25px; opacity: 0.9; font-size: 1.05rem;">Schedule a complimentary planning consultation with Swariya's senior directors. Receive a customized venue shortlist and transparent budget breakdown within 24 hours.</p>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I%20would%20like%20to%20schedule%20a%20wedding%20consultation." class="btn-gold-primary" target="_blank" rel="noopener">Chat with Wedding Specialist</a>
                <a href="wedding-brief-builder.html" class="btn-outline-white">Build Wedding Brief</a>
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

def generate():
    print(f"Generating Phase 1: {len(DATA)} High-Impact Authority Hubs...")
    generated_urls = []

    for item in DATA:
        slug = item["slug"]
        title = item["title"]
        h1 = item["h1"]
        subtitle = item["subtitle"]
        meta_desc = item["meta_desc"]
        hero_img = item["hero_img"]
        region = item["region"]
        region_upper = region.upper()
        slug_escaped = slug.replace("-", "%20")

        # USP HTML
        usp_html = ""
        for u_title, u_desc in item.get("usp_points", []):
            usp_html += f"""
            <div style="background: white; padding: 22px; border-radius: 10px; border: 1px solid var(--border-gold);">
                <h4 style="color: var(--primary); margin-bottom: 6px;">{u_title}</h4>
                <p style="font-size: 0.92rem; color: #666; margin: 0;">{u_desc}</p>
            </div>
            """

        # Venues HTML
        venues = item.get("venues", [])
        if venues:
            venues_cards = ""
            for v_name, v_desc in venues:
                venues_cards += f"""
                <div class="venue-card">
                    <span class="venue-tag">{region_upper} • LUXURY PROPERTY</span>
                    <h3>{v_name}</h3>
                    <p style="font-size: 0.92rem; color: #666; line-height: 1.6;">{v_desc}</p>
                </div>
                """
            venues_html = f"""
            <div style="margin-top: 50px;">
                <p class="section-label">✦ CURATED SIGNATURE VENUES</p>
                <h2 style="font-size: 2rem; color: var(--dark-luxury);">Premier Venues in {region}</h2>
                <p style="color: #666; margin-top: 5px;">We coordinate room blocks, buyout negotiations, and banquet production across these top properties:</p>
                <div class="venue-grid">
                    {venues_cards}
                </div>
            </div>
            """
        else:
            venues_html = ""

        # FAQs HTML & JSON-LD
        faqs = item.get("faqs", [])
        faqs_html = ""
        faq_entities = []
        for q, a in faqs:
            faqs_html += f"""
            <div class="faq-item">
                <h3>{q}</h3>
                <p>{a}</p>
            </div>
            """
            faq_entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })

        json_ld_faqs = json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }, indent=2)

        # Service JSON-LD
        json_ld_service = json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "@id": f"https://swariyaweddings.com/{slug}.html#service",
            "name": h1,
            "serviceType": "Wedding Planning",
            "provider": {
                "@type": "Organization",
                "name": "Swariya Weddings",
                "url": "https://swariyaweddings.com/",
                "telephone": "+91-8050573382",
                "logo": "https://swariyaweddings.com/images/logo.png"
            },
            "areaServed": {"@type": "Place", "name": region},
            "description": meta_desc
        }, indent=2)

        # Breadcrumbs JSON-LD
        json_ld_breadcrumbs = json.dumps({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://swariyaweddings.com/"},
                {"@type": "ListItem", "position": 2, "name": "Destinations & Verticals", "item": "https://swariyaweddings.com/destination-wedding-planner-india.html"},
                {"@type": "ListItem", "position": 3, "name": h1, "item": f"https://swariyaweddings.com/{slug}.html"}
            ]
        }, indent=2)

        # Render HTML
        rendered = HTML_TEMPLATE.format(
            slug=slug,
            title=title,
            h1=h1,
            subtitle=subtitle,
            meta_desc=meta_desc,
            hero_img=hero_img,
            region=region,
            region_upper=region_upper,
            slug_escaped=slug_escaped,
            usp_html=usp_html,
            venues_html=venues_html,
            faqs_html=faqs_html,
            json_ld_service=json_ld_service,
            json_ld_breadcrumbs=json_ld_breadcrumbs,
            json_ld_faqs=json_ld_faqs
        )

        filename = f"{slug}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(rendered)

        generated_urls.append(f"https://swariyaweddings.com/{slug}.html")
        print(f"  -> Generated: {filename}")

    # ----------------------------------------------------
    # UPDATE SITEMAP.XML
    # ----------------------------------------------------
    print("\nUpdating sitemap.xml...")
    sitemap_path = "sitemap.xml"
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap_content = f.read()

    new_entries = []
    for u in generated_urls:
        if u not in sitemap_content:
            new_entries.append(f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-09-13</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.90</priority>
  </url>""")

    if new_entries:
        insert_point = "</urlset>"
        updated_sitemap = sitemap_content.replace(insert_point, "\n".join(new_entries) + "\n" + insert_point)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(updated_sitemap)
        print(f"Added {len(new_entries)} new URLs to sitemap.xml")
    else:
        print("All URLs already present in sitemap.xml")

    # ----------------------------------------------------
    # UPDATE LLMS.TXT
    # ----------------------------------------------------
    print("\nUpdating llms.txt and llms-full.txt...")
    with open("llms.txt", "r", encoding="utf-8") as f:
        llms_content = f.read()

    llms_entries = []
    for item in DATA:
        link_str = f"- [{item['h1']}](https://swariyaweddings.com/{item['slug']}.html): {item['meta_desc']}"
        if item['slug'] not in llms_content:
            llms_entries.append(link_str)

    if llms_entries:
        with open("llms.txt", "a", encoding="utf-8") as f:
            f.write("\n\n## Phase 1 High-Authority Hubs\n" + "\n".join(llms_entries) + "\n")
        print(f"Added {len(llms_entries)} entries to llms.txt")

    print(f"\n🎉 PHASE 1 COMPLETE! Successfully generated {len(DATA)} high-power hubs.")

if __name__ == "__main__":
    generate()
