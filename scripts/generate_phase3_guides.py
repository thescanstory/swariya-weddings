import os
import json

PHASE3_GUIDES = [
    # -------------------------------------------------------------------------
    # 1. COMPREHENSIVE 2026 DESTINATION COST GUIDES
    # -------------------------------------------------------------------------
    {
        "slug": "cost-of-destination-wedding-in-goa-2026",
        "title": "Cost of a Destination Wedding in Goa (2026 Comprehensive Budget Breakdown)",
        "meta_title": "Cost of Destination Wedding in Goa 2026 | Line-by-Line Budget Guide",
        "meta_desc": "Realistic 2026 cost breakdown for a destination wedding in Goa. Real pricing for South vs North Goa 5-star resorts, beach permits, decor, sound, and 0% markup budgets.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "7 Min Read",
        "hero_img": "images/10.jpg",
        "intro": "Planning a destination wedding in Goa requires realistic financial clarity across hotel room buyouts, beach permits, coastal weatherproofing, and entertainment licensing. Below is Swariya Weddings' verified 2026 budget blueprint for 100 to 250 guest celebrations across South and North Goa.",
        "key_metrics": [
            ("Average Total Investment", "₹40 Lakhs – ₹1.2 Crores (2 Nights / 3 Days)"),
            ("5-Star Room Rates (Per Night)", "₹18,000 – ₹38,000 (Incl. Taxes & Breakfast)"),
            ("F&B Per Guest (Per Day)", "₹4,500 – ₹8,500 (Lunch, Hi-Tea, Gala Dinner)"),
            ("Mandap & 3D Spatial Decor", "₹12,00,000 – ₹30,00,000 (Across 3-4 Events)"),
            ("Sound, DJ & Artist Licenses", "₹3,50,000 – ₹8,00,000 (PPL, IPRS, Noventiq)")
        ],
        "sections": [
            {
                "heading": "1. South Goa vs North Goa: Cost & Atmosphere Dynamics",
                "content": """
                <p>Choosing between South and North Goa directly impacts your property buyout costs and guest experience:</p>
                <ul style="margin: 15px 0; padding-left: 20px; line-height: 1.8;">
                    <li><strong>South Goa (Benaulim, Cavelossim, Arossim, Majorda):</strong> Features massive 40-75 acre luxury beach resorts (Taj Exotica, The Leela, ITC Grand Goa, St. Regis). Best suited for grand, private residential weddings with expansive oceanfront lawns. Room buyouts average ₹22,000–₹38,000/night.</li>
                    <li><strong>North Goa (Vagator, Morjim, Candolim):</strong> Known for cliffside boutique luxury (W Goa, Marquis, Taj Fort Aguada). Ideal for high-energy Sangeet pool parties and sundowners. Properties are more boutique, averaging ₹18,000–₹32,000/night with closer proximity to nightlife.</li>
                </ul>
                """
            },
            {
                "heading": "2. Event-by-Event Cost Allocation Model (150 Guests / 3 Days)",
                "content": """
                <p>A standard 3-day luxury Goa wedding itinerary typically distributes investment across four primary events:</p>
                <div style="background: #FAF6F0; border: 1px solid var(--border-gold); border-radius: 10px; padding: 20px; margin: 20px 0;">
                    <p><strong>Day 1 Sundowner Welcome Party / Mehendi:</strong> ₹4,50,000 – ₹9,00,000 (Bohemian beach lounge, live acoustic band, craft cocktail bars).</p>
                    <p><strong>Day 2 Sangeet & After-Party:</strong> ₹8,00,000 – ₹18,00,000 (Truss lighting, concert sound, LED screens, DJ, late-night acoustic indoor ballroom).</p>
                    <p><strong>Day 3 Sunset Beach Mandap & Royal Banquet:</strong> ₹10,00,000 – ₹22,00,000 (CRZ-compliant floral mandap on beachfront lawn, live Shehnai/flute, multi-tier gala dinner).</p>
                </div>
                """
            },
            {
                "heading": "3. The Swariya Zero Markup Advantage in Goa",
                "content": """
                <p>Unlike traditional agencies that mark up Goan sound vendors, florists, and generator rentals by 20% to 40%, Swariya operates with an unyielding <strong>0% vendor markup guarantee</strong>. You review original vendor invoices, contract directly at wholesale B2B rates, and pay only our transparent fixed management fee.</p>
                """
            }
        ],
        "faqs": [
            ("What is the cost of beach wedding permits in Goa?", "Beach lawn setups inside private 5-star properties do not require separate municipal beach permits, but public beach setups require Coastal Regulation Zone (CRZ) and local Panchayat NOCs costing between ₹50,000 to ₹1,50,000."),
            ("What is the best month to host a destination wedding in Goa?", "November through February offers pleasant 24°C–28°C weather with zero rain. Early March and late October offer great shoulder-season tariff savings of 20-30%."),
            ("How do we book hotel room blocks in Goa at the best rates?", "Swariya initiates room block negotiations 10-12 months in advance, locking in corporate MICE/wedding buyout slabs with complimentary upgrades and flexible attrition clauses.")
        ]
    },
    {
        "slug": "cost-of-udaipur-palace-wedding-2026",
        "title": "Cost of a Palace Wedding in Udaipur (2026 Investment Guide)",
        "meta_title": "Cost of Udaipur Palace Wedding 2026 | Royal Heritage Budget Guide",
        "meta_desc": "Line-by-line cost guide for an Udaipur royal palace wedding in 2026. Realistic pricing for Jagmandir, Udaivilas, Leela Palace, Shiv Niwas, and 0% markup management.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "8 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "Udaipur represents the pinnacle of royal Indian destination weddings. From private island palaces like Jagmandir to iconic lakeside heritage properties like The Oberoi Udaivilas and The Leela Palace, here is an executive financial blueprint for planning an unforgettable Mewari royal celebration in 2026.",
        "key_metrics": [
            ("Average Total Investment", "₹65 Lakhs – ₹2.5 Crores (2 Nights / 3 Days)"),
            ("Palace Room Rates (Per Night)", "₹28,000 – ₹65,000 (Lake View Heritage Suites)"),
            ("F&B Per Guest (Royal Thalis)", "₹6,000 – ₹12,000 (Mewari & Global Banquets)"),
            ("Boat Transfers & Lake Logistics", "₹3,00,000 – ₹7,50,000 (Private Decorated Shikaras)"),
            ("Royal Mandap & Floral Architecture", "₹18,00,000 – ₹45,00,000 (Heritage Courtyard Sets)")
        ],
        "sections": [
            {
                "heading": "1. Venue Tiers: Island Palaces vs Lakefront Luxury vs Heritage Hilltops",
                "content": """
                <p>Udaipur properties categorize into distinct operational tiers:</p>
                <ul style="margin: 15px 0; padding-left: 20px; line-height: 1.8;">
                    <li><strong>Tier 1 Ultra-Luxury Island & Palatial Flags (Jagmandir, The Oberoi Udaivilas, The Leela Palace, Taj Lake Palace):</strong> Flagship royal venues requiring full buyouts or premium per-event venue fees (₹15L–₹35L event fee plus rooms). Budget: ₹1.2 Cr – ₹2.5 Cr+.</li>
                    <li><strong>Tier 2 Heritage Palaces inside City Palace (Shiv Niwas, Fateh Prakash Palace, Zenana Mahal):</strong> Historic Mewari royal settings managed by HRH Group. Budget: ₹75L – ₹1.5 Cr.</li>
                    <li><strong>Tier 3 Hilltop & Boutique Palaces (Fateh Garh, RAAS Devigarh, Aurika, Radisson Blu Udaipur):</strong> Panoramic lake and mountain views with grand ballrooms and larger room counts. Budget: ₹50L – ₹95L.</li>
                </ul>
                """
            },
            {
                "heading": "2. Lake Pichola Logistics & Heritage Permissions",
                "content": """
                <p>Hosting events on Lake Pichola requires synchronized water logistics: private ferry charters for 200+ guests, jetty security, sound curfews (10:00 PM for outdoor lakefront spaces with transition to soundproof indoor Darbar halls), and custom heritage lighting.</p>
                """
            }
        ],
        "faqs": [
            ("Can we host a wedding at Jagmandir Island Palace without staying there?", "Yes, Jagmandir Island Palace can be booked for evening Sangeet or Wedding ceremonies with private boat transfers, while guests stay at mainland luxury properties like Trident, Radisson Blu, or Leela."),
            ("How far in advance should we book Udaipur palace venues?", "Due to international demand and peak winter Muhurtham dates, booking 10 to 14 months in advance is essential to secure primary weekend dates.")
        ]
    },
    {
        "slug": "cost-of-jaipur-royal-wedding-2026",
        "title": "Cost of a Royal Destination Wedding in Jaipur (2026 Budget Breakdown)",
        "meta_title": "Cost of Jaipur Royal Wedding 2026 | Palace & Heritage Budget Guide",
        "meta_desc": "Complete 2026 cost guide for Jaipur destination weddings. Detailed budgeting for Rambagh Palace, Fairmont, Jai Mahal, Samode, Alila Fort Bishangarh, and 0% markup execution.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "7 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "Jaipur offers the greatest diversity of royal wedding architecture in India—from authentic 200-year-old Rajput forts to massive 5-star palatial convention resorts. Here is our 2026 cost breakdown for hosting 150 to 400 guest royal celebrations in the Pink City.",
        "key_metrics": [
            ("Average Total Investment", "₹45 Lakhs – ₹1.8 Crores (2 Nights / 3 Days)"),
            ("5-Star Heritage Rooms (Per Night)", "₹16,000 – ₹45,000 (Palace & Luxury Rooms)"),
            ("Royal Rajputana Banquets", "₹4,500 – ₹9,500 / guest / meal"),
            ("Monumental Decor & Lighting", "₹15,00,000 – ₹38,00,000"),
            ("Elephant & Royal Camel Baraat", "₹1,50,000 – ₹4,00,000 (Permits & Procession)")
        ],
        "sections": [
            {
                "heading": "1. Palace Heritage vs Kukas Luxury Convention Resorts",
                "content": """
                <p>Jaipur wedding venues split into two primary operational models:</p>
                <ul style="margin: 15px 0; padding-left: 20px; line-height: 1.8;">
                    <li><strong>City Heritage Palaces (Rambagh Palace, Jai Mahal Palace, Rajvilas):</strong> Located in central Jaipur with manicured Mughal gardens and antique palace suites. Premium intimacy and royal prestige.</li>
                    <li><strong>Kukas & Delhi-Jaipur Highway Palatial Resorts (Fairmont Jaipur, Le Méridien, Shiv Vilas, Alila Fort Bishangarh):</strong> Feature massive pillarless ballrooms, 150+ room inventories, and grand courtyards capable of hosting 500+ guests without room dispersion.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Can live elephants and royal camels be included in the Baraat in Jaipur?", "Yes, Jaipur has established heritage protocols for decorated elephant and camel processions with royal Chhatri flags and Dholak troupes, provided local municipal animal welfare permissions are coordinated.")
        ]
    },
    {
        "slug": "kerala-backwater-wedding-cost-guide-2026",
        "title": "Kerala Backwater & Beach Destination Wedding Cost Guide (2026)",
        "meta_title": "Kerala Wedding Cost 2026 | Kumarakom & Kochi Backwater Budget Guide",
        "meta_desc": "Realistic cost breakdown for a Kerala backwater or coastal wedding in 2026. Pricing for Kumarakom, Kochi, Kovalam resorts, houseboat catering, and zero markup planning.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "6 Min Read",
        "hero_img": "images/12.jpg",
        "intro": "From serene backwater resorts in Kumarakom and luxury private islands in Kochi to seaside cliffs in Kovalam, Kerala delivers lush tropical elegance. Here is the verified 2026 budget blueprint for planning a destination wedding in God's Own Country.",
        "key_metrics": [
            ("Average Total Investment", "₹35 Lakhs – ₹85 Lakhs (2 Nights / 3 Days)"),
            ("Resort Villa Rates (Per Night)", "₹14,000 – ₹30,000 (Lakeside Heritage Villas)"),
            ("Authentic Kerala Sadhya & Banquets", "₹3,500 – ₹6,500 / guest / day"),
            ("Houseboat & Shikara Charters", "₹2,50,000 – ₹6,00,000 (Guest Cruises)"),
            ("Eco-Tropical Floral Mandaps", "₹8,00,000 – ₹20,00,000")
        ],
        "sections": [
            {
                "heading": "1. Backwaters (Kumarakom/Alleppey) vs Coastal (Kochi/Kovalam)",
                "content": """
                <p>Kerala offers distinct destination wedding landscapes:</p>
                <ul style="margin: 15px 0; padding-left: 20px; line-height: 1.8;">
                    <li><strong>Kumarakom & Alleppey Backwaters:</strong> Kumarakom Lake Resort, Coconut Lagoon, and The Zuri provide tranquil lakefront lawns, houseboats, and traditional Chenda Melam ceremonies.</li>
                    <li><strong>Kochi Waterfront & Heritage:</strong> Grand Hyatt Kochi Bolgatty and Brunton Boatyard Fort Kochi offer urban island scale, modern ballroom infrastructure, and Dutch colonial charm.</li>
                    <li><strong>Kovalam Cliffside & Beaches:</strong> The Leela Kovalam and Taj Green Cove offer dramatic sea-cliff mandap ceremonies overlooking the Arabian Sea.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Can a traditional 24-item Kerala Sadhya be served on banana leaves for 200+ guests?", "Yes! Authentic Sadhya masters prepare traditional banana-leaf feasts with payasam varieties, fully coordinated with five-star resort banquet teams.")
        ]
    },
    {
        "slug": "coorg-destination-wedding-cost-guide-2026",
        "title": "Coorg & Western Ghats Plantation Wedding Cost Guide (2026)",
        "meta_title": "Coorg Destination Wedding Cost 2026 | Coffee Plantation Budget Guide",
        "meta_desc": "Complete budget guide for a coffee estate destination wedding in Coorg, Kabini, and Chikmagalur. Realistic costs for Taj Madikeri, Tamara, Evolve Back, and 0% markup planning.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "6 Min Read",
        "hero_img": "images/15.jpg",
        "intro": "Misty hills, 200-acre coffee plantations, and temperate weather make Coorg and Chikmagalur the prime nature-luxury destination wedding choice for South India. Here is our 2026 cost and logistics breakdown.",
        "key_metrics": [
            ("Average Total Investment", "₹30 Lakhs – ₹75 Lakhs (2 Nights / 3 Days)"),
            ("Plantation Villa Rates (Per Night)", "₹15,000 – ₹32,000 (Private Pool Cottages)"),
            ("Kodava & Multi-Cuisine Banquets", "₹3,500 – ₹6,000 / guest / day"),
            ("Weatherproof Glass & Hill Mandaps", "₹7,50,000 – ₹18,00,000"),
            ("Bengaluru / Mangalore Coach Transfers", "₹1,50,000 – ₹3,50,000")
        ],
        "sections": [
            {
                "heading": "1. Logistics & Weather Considerations in the Hills",
                "content": """
                <p>Coorg weddings require proactive weatherproofing: temperature-controlled indoor-outdoor transitional marquees, mist-resistant lighting, and coordinated luxury coach transfers from Bengaluru (4.5 hrs) or Kannur International Airport (2 hrs).</p>
                """
            }
        ],
        "faqs": [
            ("What is the best airport to fly guests in for a Coorg wedding?", "Kannur International Airport (CNN) is only 2 hours away by road, while Bengaluru International Airport (BLR) offers widespread direct international flights with luxury 4.5-hour AC bus convoys.")
        ]
    },

    # -------------------------------------------------------------------------
    # 2. CULTURAL CEREMONY PROTOCOLS & COMMUNITY-SPECIFIC GUIDES
    # -------------------------------------------------------------------------
    {
        "slug": "marwari-destination-wedding-planner-guide",
        "title": "Marwari Destination Wedding Traditions & Planning Blueprint",
        "meta_title": "Marwari Destination Wedding Planner India | Traditions & Grand Sangeet",
        "meta_desc": "Expert planning guide for Marwari royal destination weddings. Protocols for Mayra/Bhaat, Pithi Dastoor, grand Sangeet stage design, pure Jain/veg catering, and 0% markup.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "8 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "Marwari weddings are renowned worldwide for their grand hospitality, intricate Vedic rituals, high-voltage Sangeet productions, and lavish pure vegetarian feasts. Swariya Weddings details the essential traditions and production requirements for destination Marwari weddings.",
        "key_metrics": [
            ("Key Rituals", "Mudha Tikka, Godh Bharai, Pithi Dastoor, Mayra / Bhaat, Toran Pheras"),
            ("Culinary Mandate", "Pure Vegetarian, Dedicated Maharaj Kitchens, Jain Counter Separation"),
            ("Production Highlights", "Multi-Tier Concert Sangeet Stage, Royal Elephant/Vintage Car Baraat"),
            ("Average Guest Count", "200 – 600 Residential Guests"),
            ("Recommended Hubs", "Jaipur, Udaipur, Jodhpur, Jaisalmer, Goa Beach Resorts")
        ],
        "sections": [
            {
                "heading": "1. Mayra / Bhaat: The Maternal Uncle's Grand Welcome",
                "content": """
                <p>The Mayra (or Bhaat) ceremony is one of the emotional centerpieces of a Marwari wedding. Swariya designs royal royal canopy entrances with live Nagada drummers and floral umbrellas where the maternal family presents traditional gifts, silks, and gold ornaments to the bride/groom's mother.</p>
                """
            },
            {
                "heading": "2. High-Tech Sangeet Production & Live Concert Stages",
                "content": """
                <p>Marwari Sangeets are large-scale performances. We coordinate 40-foot wide LED kinetic backdrops, calibrated line-array sound systems, specialized choreography rehearsals, and celebrity artist hospitality.</p>
                """
            },
            {
                "heading": "3. Strict Pure Vegetarian & Jain Gastronomy Management",
                "content": """
                <p>We work directly with traditional Marwari Maharaj chefs and 5-star executive culinary teams to curate authentic Ker Sangri, Dal Baati Churma, Gatte ki Sabzi, live Halwai stations, and separate 100% root-free Jain live counters.</p>
                """
            }
        ],
        "faqs": [
            ("Can 5-star hotels accommodate pure vegetarian Maharaj cooking teams?", "Yes! Swariya negotiates dedicated Maharaj kitchen annexes with independent utensil sets and pure vegetarian storage in luxury destination hotels.")
        ]
    },
    {
        "slug": "gujarati-destination-wedding-traditions-guide",
        "title": "Gujarati Destination Wedding Traditions & Planning Guide",
        "meta_title": "Gujarati Destination Wedding Planner | Garba Night, Mandvo & Mameru",
        "meta_desc": "Comprehensive guide for planning Gujarati destination weddings. Traditions including Gol Dhana, Mandvo, Mameru, high-energy Garba-Raas staging, and pure vegetarian banquets.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "7 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "From the rhythmic joy of Raas-Garba under fairy-lit open skies to the sacred solemnity of the Mandvo and Kanyadaan, Gujarati destination weddings blend infectious energy with deep family warmth.",
        "key_metrics": [
            ("Core Rituals", "Gol Dhana, Mandvo, Griha Shanti, Mameru / Mosalu, Jaan Aagman, Pheras"),
            ("Signature Event", "Grand Open-Air Raas Garba Night with Live Dholak & Folk Singers"),
            ("Catering Highlights", "Undhiyu, Gujarati Kadhi, Basundi, Jalebi Fafda & Global Live Street Food"),
            ("Recommended Hubs", "Goa, Udaipur, Jaipur, Anand (Madhubhan), Mumbai / Alibaug")
        ],
        "sections": [
            {
                "heading": "1. The Grand Garba & Dandiya Night Production",
                "content": """
                <p>A Gujarati Sangeet is synonymous with Garba. We construct expansive circular wooden dance floors, vibrant colorful umbrella canopies (Chattris), and provide personalized Dandiya sticks for all guests alongside live Gujarati folk bands.</p>
                """
            }
        ],
        "faqs": [
            ("How are morning Mandvo and Griha Shanti ceremonies coordinated at destination resorts?", "We arrange private morning courtyard setups with traditional copper havan kunds, pure ghee, and auspicious mango leaf torans before the evening festivities.")
        ]
    },
    {
        "slug": "punjabi-sikh-destination-wedding-planner",
        "title": "Punjabi & Sikh Destination Wedding Planning Blueprint",
        "meta_title": "Punjabi & Sikh Destination Wedding Planner | Anand Karaj & Jaggo",
        "meta_desc": "Specialized planning guide for Punjabi & Sikh destination weddings in India. Anand Karaj Gurudwara coordination, high-energy Jaggo, Dhol Baraats, and 0% markup management.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "8 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "Punjabi and Sikh weddings are iconic celebrations filled with boundless joy, heartfelt spirituality during the sacred Anand Karaj, and high-energy Jaggo and Sangeet nights.",
        "key_metrics": [
            ("Core Ceremonies", "Roka, Kurmai, Jaggo Night, Chooda & Kalire, Anand Karaj, Grand Reception"),
            ("Sacred Protocol", "Anand Karaj inside historic Gurudwara or compliant indoor Diwan Hall"),
            ("Baraat Highlights", "Live Punjabi Dhol Troupes, Decorated Open Jeep / Vintage Cars"),
            ("Recommended Hubs", "Goa, Jaipur, Jim Corbett, Delhi NCR, Chandigarh")
        ],
        "sections": [
            {
                "heading": "1. Sacred Anand Karaj Execution & Protocols",
                "content": """
                <p>The Anand Karaj (Ceremony of Bliss) is conducted strictly in accordance with Sikh Rehat Maryada. Swariya coordinates with local Gurudwaras or establishes compliant Diwan setups with pristine white floor seating, Guru Granth Sahib Prakash, and Langar seva.</p>
                """
            }
        ],
        "faqs": [
            ("Can Anand Karaj be performed at outdoor beach lawns?", "In accordance with Akal Takht edicts, Anand Karaj ceremonies are respectfully held inside Gurudwaras or dedicated consecrated indoor Diwan halls, followed by outdoor receptions.")
        ]
    },
    {
        "slug": "telugu-destination-wedding-planner-guide",
        "title": "Telugu Destination Wedding Traditions & Muhurtham Blueprint",
        "meta_title": "Telugu Destination Wedding Planner | Pelli Sandadi & Jeelakarra Bellam",
        "meta_desc": "Expert guide to Telugu destination weddings across India. Detailed timelines for Mangala Snanam, Pelli Sandadi, Jeelakarra Bellam, and traditional Andhra/Rayalaseema catering.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "7 Min Read",
        "hero_img": "images/10.jpg",
        "intro": "Telugu weddings are steeped in ancient Vedic rituals, auspicious astronomical Muhurtham timings, vibrant Pelli Sandadi celebrations, and rich handwoven Kanjeevaram aesthetics.",
        "key_metrics": [
            ("Core Ceremonies", "Nischitartham, Pellikoothuru / Pellikkoduku, Mangala Snanam, Jeelakarra Bellam, Talambralu"),
            ("Muhurtham Precision", "Strict astrological timing coordination (frequently late-night / dawn)"),
            ("Decor Aesthetics", "Temple Brass Vilakkus, Fresh Mallipoo & Marigold Pillars, Lotus Ponds"),
            ("Recommended Hubs", "Hyderabad Palaces, Chennai ECR Beachfronts, Goa, Bengaluru Heritage")
        ],
        "sections": [
            {
                "heading": "1. Executing Late-Night & Dawn Muhurtham Timings",
                "content": """
                <p>Telugu Muhurthams frequently fall in early dawn or midnight hours. Swariya ensures seamless 24-hour hotel operational coordination, continuous hot filter coffee stations, and fresh breakfast banquets following the Talambralu.</p>
                """
            }
        ],
        "faqs": [
            ("How does Swariya manage traditional Andhra & Telangana catering at destination resorts?", "We collaborate with specialist culinary masters for authentic Gongura dishes, Avakaya, Pulihora, Gutti Vankaya, and traditional sweet Pootharekulu.")
        ]
    },
    {
        "slug": "tamil-brahmin-destination-wedding-guide",
        "title": "Tamil Brahmin (Tambrahm) Destination Wedding Guide",
        "meta_title": "Tamil Brahmin Destination Wedding Guide | Vratham, Oonjal & Sadhya",
        "meta_desc": "Comprehensive planning guide for Tamil Brahmin destination weddings. Step-by-step coordination for Vratham, Kasi Yatra, Oonjal swing ceremony, and authentic 2-day Sadhya banquets.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "7 Min Read",
        "hero_img": "images/1.jpg",
        "intro": "Tamil Brahmin weddings are magnificent tapestries of classical Carnatic music, Nadaswaram melodies, sacred Vedic chantings, playful Oonjal swing rituals, and exquisite banana-leaf Sadhyas.",
        "key_metrics": [
            ("Core Ceremonies", "Vratham, Jaanavasam (Baraat), Kasi Yatra, Oonjal, Kanyadaanam, Muhurtham, Nalangu"),
            ("Musical Landscape", "Classical Live Nadaswaram & Thavil Troupes, Carnatic Kutcheri"),
            ("Dining Mandate", "Strict Pure Vegetarian Madi/Traditional Kitchens, 24-Dish Banana Leaf Sadhya"),
            ("Recommended Hubs", "Chennai ECR, Bengaluru Heritage Mantapas, Kumbakonam, Kerala Backwaters")
        ],
        "sections": [
            {
                "heading": "1. The Oonjal (Swing Ceremony) & Floral Artistry",
                "content": """
                <p>The Oonjal ceremony represents the couple weathering life's ups and downs together on a flower-bedecked swing. Swariya crafts heirloom teakwood swings draped in fragrant Madurai Malli, accompanied by traditional Oonjal songs sung by family elders.</p>
                """
            }
        ],
        "faqs": [
            ("Can morning breakfast and lunch Sadhyas be served strictly on banana leaves at 5-star destination hotels?", "Yes! We coordinate dedicated banana-leaf dining halls with low or high seating and traditional silver/brass servers.")
        ]
    },
    {
        "slug": "nri-destination-wedding-planner-india",
        "title": "NRI Destination Wedding in India (Comprehensive Remote Planning Guide)",
        "meta_title": "NRI Destination Wedding Planner India | US, UK, UAE & Global Couples",
        "meta_desc": "Complete remote planning playbook for NRI couples in USA, UK, UAE, Canada, and Singapore. 3D visual walkthroughs, transparent multi-currency accounts, and zero markup management.",
        "category": "NRI & CROSS-BORDER WEDDING BLUEPRINTS",
        "read_time": "9 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "Planning a dream destination wedding in India while living thousands of miles away across different time zones requires absolute transparency, proactive communication, and digital-first event management.",
        "key_metrics": [
            ("Client Locations", "USA, UK, UAE, Canada, Singapore, Australia, Europe"),
            ("Planning Process", "Virtual 3D Spatial Walkthroughs, Digital Brief Builder & WhatsApp Portals"),
            ("Financial Security", "Multi-Currency Wire Support, Direct Vendor Contracts, 0.00% Markup Guarantee"),
            ("Logistics Handled", "Airport Meet & Greet, Visa Support Letters, Luxury Coach Convoys, 24/7 Concierge"),
            ("Average Planning Horizon", "9 – 16 Months in Advance")
        ],
        "sections": [
            {
                "heading": "1. Remote Planning with 3D Architectural Visualizations",
                "content": """
                <p>You don't need to fly to India multiple times for site visits. Swariya provides accurate 3D CAD visual walkthroughs of your mandap, stage lighting, and table scapes before a single deposit is paid.</p>
                """
            },
            {
                "heading": "2. Time Zone Aligned Communication & Dedicated Project Directors",
                "content": """
                <p>We assign a senior wedding director who schedules weekly video syncs aligned with your local time zone (EST, PST, GMT, GST, SGT) with full access to our digital Wedding OS portal.</p>
                """
            }
        ],
        "faqs": [
            ("How do overseas NRI couples pay hotel deposits and local vendors?", "You pay 5-star hotels directly via international wire or corporate payment links in your preferred currency. Swariya provides itemized master payment schedules with zero hidden exchange fees."),
            ("Can Swariya coordinate airport pickups for 100+ international guests landing at different times?", "Yes! Our dedicated airport logistics team manages flight tracking, personalized placard meet-and-greets, luxury car fleets, and luggage tracking from arrival to resort check-in.")
        ]
    },
    {
        "slug": "hyderabad-nizami-wedding-cost-guide-2026",
        "title": "Cost of a Royal Nizami Wedding in Hyderabad (2026 Budget Guide)",
        "meta_title": "Hyderabad Palace Wedding Cost 2026 | Falaknuma & ITC Kohenur Budgets",
        "meta_desc": "Realistic cost breakdown for a royal Nizami wedding in Hyderabad. Real pricing for Taj Falaknuma Palace, ITC Kohenur, Banjara Hills lawns, and 0% markup management.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "7 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "From the hilltop grandeur of Taj Falaknuma Palace to the modern glass ballrooms of ITC Kohenur, Hyderabad represents royal Deccani grandeur. Here is our 2026 cost analysis.",
        "key_metrics": [
            ("Average Total Investment", "₹45 Lakhs – ₹2.0 Crores (2 Nights / 3 Days)"),
            ("5-Star Room Rates (Per Night)", "₹14,000 – ₹45,000 (Luxury Rooms & Palace Suites)"),
            ("Nizami Banquets & Dum Biryani", "₹4,000 – ₹8,500 / guest / meal"),
            ("Chandelier & Spatial Floral Decor", "₹14,00,000 – ₹35,00,000"),
            ("Horse Carriage & Royal Welcomes", "₹2,00,000 – ₹5,00,000")
        ],
        "sections": [
            {
                "heading": "1. Heritage Palace Buyouts vs HITEC City Modern Ballrooms",
                "content": """
                <p>Taj Falaknuma Palace requires full palace buyouts for private celebrations, while properties in Banjara Hills and HITEC City (ITC Kohenur, Taj Krishna, Park Hyatt) offer massive 1,000+ guest pillarless ballrooms with expansive guest accommodations.</p>
                """
            }
        ],
        "faqs": [
            ("What is the venue buyout cost for Taj Falaknuma Palace?", "A complete residential palace buyout at Taj Falaknuma typically ranges from ₹60 Lakhs to ₹1.5 Crores per day depending on dates and room allocation.")
        ]
    },
    {
        "slug": "chennai-ecr-beach-wedding-cost-guide-2026",
        "title": "Chennai ECR & Mahabalipuram Beach Wedding Cost Guide (2026)",
        "meta_title": "Chennai ECR Beach Wedding Cost 2026 | Mahabalipuram Budget Guide",
        "meta_desc": "Complete cost guide for a luxury beach destination wedding along Chennai's East Coast Road and Mahabalipuram. InterContinental, Taj Fisherman's Cove, and 0% markup planning.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "6 Min Read",
        "hero_img": "images/10.jpg",
        "intro": "The scenic East Coast Road (ECR) connecting Chennai to Mahabalipuram features pristine Coromandel beachfronts, temple-inspired architecture, and breezy coastal lawns.",
        "key_metrics": [
            ("Average Total Investment", "₹32 Lakhs – ₹75 Lakhs (2 Nights / 3 Days)"),
            ("Beach Resort Rooms (Per Night)", "₹12,000 – ₹26,000 (Sea View Rooms & Cottages)"),
            ("Chettinad & Coastal Banquets", "₹3,200 – ₹6,500 / guest / day"),
            ("Oceanfront Beach Mandap Decor", "₹8,00,000 – ₹20,00,000"),
            ("Airport Transit & Shuttles", "₹1,20,000 – ₹2,80,000")
        ],
        "sections": [
            {
                "heading": "1. Coromandel Coast Weather & Seasonality",
                "content": """
                <p>The ideal season for an ECR beach wedding is November through February when coastal breezes are cool and dry. Avoid late October to mid-November during Northeast monsoon cycles.</p>
                """
            }
        ],
        "faqs": [
            ("How far are ECR wedding resorts from Chennai Airport?", "Most premier resorts in Mahabalipuram and Covelong are a comfortable 45 to 60-minute drive along the scenic coastal highway from Chennai International Airport (MAA).")
        ]
    },
    {
        "slug": "mussoorie-jim-corbett-wedding-cost-guide-2026",
        "title": "Mussoorie & Jim Corbett Mountain Destination Wedding Cost (2026)",
        "meta_title": "Mussoorie & Jim Corbett Wedding Cost 2026 | Mountain Resort Guide",
        "meta_desc": "Realistic budget breakdown for a mountain or riverfront destination wedding in Mussoorie and Jim Corbett. Pricing for JW Marriott, Taj Corbett, river lawns, and 0% markup.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "7 Min Read",
        "hero_img": "images/15.jpg",
        "intro": "For couples seeking misty Himalayan ridges or wild jungle riverbanks, Uttarakhand offers spectacular natural backdrops just a short journey from Delhi NCR.",
        "key_metrics": [
            ("Average Total Investment", "₹38 Lakhs – ₹95 Lakhs (2 Nights / 3 Days)"),
            ("Himalayan 5-Star Rooms (Per Night)", "₹16,000 – ₹38,000"),
            ("Garhwali & Multi-Cuisine Banquets", "₹3,800 – ₹7,000 / guest / day"),
            ("Riverside & Hilltop Mandap Decor", "₹9,00,000 – ₹22,00,000"),
            ("Delhi NCR Coach Transfers", "₹2,00,000 – ₹4,50,000")
        ],
        "sections": [
            {
                "heading": "1. Mountain Logistics & Road Connectivity",
                "content": """
                <p>Mussoorie requires coordination from Dehradun Jolly Grant Airport (90 mins), while Jim Corbett is easily reached via a 4.5-hour expressway drive from Delhi NCR or Ramnagar direct railway station.</p>
                """
            }
        ],
        "faqs": [
            ("What is the best season for a Jim Corbett riverside wedding?", "October through April offers crisp sunny days, pleasant 20°C weather, and clear starry jungle nights.")
        ]
    },
    {
        "slug": "luxury-intimate-50-guest-destination-wedding-cost",
        "title": "Cost of an Intimate 50-Guest Luxury Destination Wedding (2026)",
        "meta_title": "50-Guest Luxury Destination Wedding Cost 2026 | Micro-Wedding Guide",
        "meta_desc": "Complete budget and planning blueprint for an ultra-luxury intimate 50-guest micro-wedding in India. Boutique palace buyouts, bespoke Michelin dining, and 0% markup management.",
        "category": "COST BREAKDOWN & FINANCIAL PLANNING",
        "read_time": "6 Min Read",
        "hero_img": "images/11.jpg",
        "intro": "The luxury micro-wedding revolution allows couples to reallocate large guest catering budgets into ultra-exclusive boutique palace buyouts, personalized culinary tasting menus, and bespoke guest experiences.",
        "key_metrics": [
            ("Average Total Investment", "₹25 Lakhs – ₹55 Lakhs (2 Nights / 3 Days for 50 Pax)"),
            ("Boutique Heritage Buyout", "₹12,00,000 – ₹28,00,000 (Entire 20-25 Room Property)"),
            ("Plated Fine Dining / Tasting Menu", "₹5,000 – ₹10,000 / guest / meal"),
            ("Bespoke Spatial Floral Styling", "₹6,00,000 – ₹14,00,000"),
            ("Personalized Luxury Gifting", "₹2,50,000 – ₹5,00,000")
        ],
        "sections": [
            {
                "heading": "1. Why Micro-Weddings Deliver Unrivaled Luxury",
                "content": """
                <p>With 50 close family and friends, you can buy out properties like RAAS Devigarh, Samode Palace, or Carnoustie Kerala entirely for your inner circle, ensuring complete privacy, zero outsider presence, and bespoke service.</p>
                """
            }
        ],
        "faqs": [
            ("Can small boutique properties be booked exclusively for 50 guests?", "Yes! Boutique heritage hotels with 20 to 30 rooms offer complete property buyouts, giving your wedding party exclusive private run of the entire estate.")
        ]
    },
    {
        "slug": "eco-friendly-sustainable-destination-wedding-guide",
        "title": "Eco-Friendly & Sustainable Destination Wedding Guide in India",
        "meta_title": "Eco-Friendly Destination Wedding India | Zero Waste & Sustainable Decor",
        "meta_desc": "The complete playbook for planning a zero-waste, eco-luxury destination wedding in India. Biodegradable florals, solar sound, farm-to-table menus, and zero single-use plastics.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "7 Min Read",
        "hero_img": "images/12.jpg",
        "intro": "Celebrate your union in harmony with nature. Swariya Weddings pioneers conscious luxury—combining breathtaking aesthetic beauty with zero single-use plastics, local floral sourcing, and biodegradable event design.",
        "key_metrics": [
            ("Sustainability Pillars", "Zero Single-Use Plastics, Local Seasonal Florals, Clay Tandoors, Solar Battery Sound"),
            ("Waste Management", "100% Composting of Floral & Organic Food Waste, Local Farm Partnerships"),
            ("Stationery & Favors", "Plantable Seed Paper Invites, Handcrafted Terracotta & Brass Souvenirs"),
            ("Recommended Hubs", "Marari Beach Kerala, Coorg Plantations, Kabini, Alibaug Organic Estates")
        ],
        "sections": [
            {
                "heading": "1. Sustainable Mandap Architecture & Local Floristry",
                "content": """
                <p>We replace single-use floral foam (oasis) with natural water troughs, bamboo scaffolding, potted living plants that are replanted post-wedding, and locally grown marigolds, tuberoses, and coconut fronds.</p>
                """
            }
        ],
        "faqs": [
            ("Does an eco-friendly wedding compromise on luxury aesthetics?", "Not at all. Conscious luxury utilizes natural linen drapes, hand-carved terracotta, heirloom brass lamps, and living botanical installations that feel far more organic and sophisticated than artificial synthetic sets.")
        ]
    },
    {
        "slug": "kerala-christian-destination-wedding-guide",
        "title": "Kerala Christian Destination Wedding Traditions & Reception Guide",
        "meta_title": "Kerala Christian Destination Wedding Guide | Madhuramveppu & Receptions",
        "meta_desc": "Expert planning guide for Syrian Christian, Latin Catholic, and Mar Thoma destination weddings in Kerala. Historic church coordination, Madhuramveppu, and coastal receptions.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "7 Min Read",
        "hero_img": "images/12.jpg",
        "intro": "From the solemn beauty of historic Portuguese and Syrian Christian church ceremonies to the joyful sweetness of Madhuramveppu and evening backwater gala receptions.",
        "key_metrics": [
            ("Key Rituals", "Manasammatham (Betrothal), Madhuramveppu (Sweet Blessing), Minnu Kettu / Thaali, Crowning"),
            ("Ceremony Venues", "Historic Fort Kochi Churches or Waterfront Chapel Pavilions"),
            ("Reception Highlights", "Live Western & Fusion Bands, Roast Duck & Appam Banquets, Champagne Toasts"),
            ("Recommended Hubs", "Kochi Waterfront, Kumarakom Backwaters, Kovalam Seaside")
        ],
        "sections": [
            {
                "heading": "1. Madhuramveppu Eve Celebrations",
                "content": """
                <p>Held the night before the wedding, the Madhuramveppu involves the couple being fed sweet milk and bananas by their maternal uncles and godparents amidst traditional singing and laughter.</p>
                """
            }
        ],
        "faqs": [
            ("Can church ceremonies and resort receptions be coordinated seamlessly in Kochi?", "Yes, we arrange luxury AC guest coach convoys connecting historic Fort Kochi churches with waterfront reception resorts in Bolgatty and Maradu.")
        ]
    },
    {
        "slug": "bengali-destination-wedding-planner-guide",
        "title": "Bengali Destination Wedding Traditions & Planning Guide",
        "meta_title": "Bengali Destination Wedding Planner | Gaye Holud, Saat Paake & Banquets",
        "meta_desc": "Complete guide to planning a Bengali destination wedding. Traditions including Gaye Holud, Bor Jatri, Saat Paake Ghori, Shubho Drishti, and authentic Bengali catering.",
        "category": "CULTURAL TRADITIONS & RITUAL BLUEPRINTS",
        "read_time": "7 Min Read",
        "hero_img": "images/1.jpg",
        "intro": "Bengali weddings are rich in ancient folklore, soulful Shehnai melodies, the auspicious sound of the Shankha (conch shell), joyful Gaye Holud festivities, and legendary culinary banquets.",
        "key_metrics": [
            ("Core Ceremonies", "Ashirbaad, Gaye Holud, Bor Boron, Saat Paake Ghori, Shubho Drishti, Mala Bodol, Sindoor Daan"),
            ("Aesthetic Highlights", "Sholar Mukut, Topor, Betel Leaf Shubho Drishti, Red & White Alpana Art"),
            ("Culinary Mandate", "Authentic Kosha Mangsho, Chingri Malai Curry, Bhetki Paturi, Rosogolla, Mishti Doi"),
            ("Recommended Hubs", "Goa Beachfronts, Jaipur Heritage Palaces, Kolkata Heritage, Puri Coastal")
        ],
        "sections": [
            {
                "heading": "1. Saat Paake Ghori & Shubho Drishti Coordination",
                "content": """
                <p>The bride is carried on a wooden Piri by her brothers, circling the groom seven times while covering her face with sacred betel leaves before the dramatic, romantic Shubho Drishti first look.</p>
                """
            }
        ],
        "faqs": [
            ("Can authentic Bengali catering be prepared at destination resorts in Goa or Rajasthan?", "Yes! Swariya brings in specialist Bengali master chefs for authentic Mustard Bhetki Paturi, Chingri Malai Curry, and fresh Kolkata Mishti.")
        ]
    },
    {
        "slug": "3-day-destination-wedding-itinerary-template",
        "title": "3-Day Destination Wedding Master Itinerary (Run-Sheet Template)",
        "meta_title": "3-Day Destination Wedding Itinerary Template | Run-Sheet & Timelines",
        "meta_desc": "Downloadable master 3-day destination wedding itinerary template for couples and families. Minute-by-minute run-sheets for Welcome Dinners, Mehendi, Sangeet, and Pheras.",
        "category": "OPERATIONAL TIMELINES & RUN-SHEETS",
        "read_time": "8 Min Read",
        "hero_img": "images/10.jpg",
        "intro": "The secret to a stress-free luxury destination wedding is an airtight, well-buffered master itinerary. Below is Swariya Weddings' battle-tested 3-day timeline used across 150+ celebrations.",
        "key_metrics": [
            ("Duration", "2 Nights / 3 Days"),
            ("Event Count", "4 – 5 Curated Functions"),
            ("Buffer Allowance", "30-45 minutes built into hair/makeup and transportation"),
            ("Guest Rest Windows", "Mandatory 2-hour afternoon relaxation windows between events")
        ],
        "sections": [
            {
                "heading": "1. Day 1: Arrivals, Welcome High Tea & Sunset Cocktail Party",
                "content": """
                <p><strong>12:00 PM – 03:00 PM:</strong> Guest check-in, personalized welcome hampers, and room orientation.<br>
                <strong>04:30 PM – 06:30 PM:</strong> Sunset Sundowner Welcome Party with live acoustic music and refreshing coastal coolers.<br>
                <strong>07:30 PM – 11:30 PM:</strong> Glamorous Welcome Dinner / Sufi Night with open bar and live barbecue stations.</p>
                """
            },
            {
                "heading": "2. Day 2: Poolside Mehendi & Grand Sangeet Concert",
                "content": """
                <p><strong>11:00 AM – 02:30 PM:</strong> Vibrant Poolside Mehendi & Haldi with Dholak, flower showers, and live street chaat.<br>
                <strong>03:00 PM – 06:00 PM:</strong> Rest and evening glam preparation for bridal party and guests.<br>
                <strong>07:30 PM – 01:00 AM:</strong> Grand Sangeet & After-Party: Choreographed family performances, concert audio, DJ, and late-night snacks.</p>
                """
            },
            {
                "heading": "3. Day 3: Baraat, Sacred Muhurtham & Royal Gala Reception",
                "content": """
                <p><strong>03:30 PM – 05:00 PM:</strong> Royal Baraat procession with live percussion and vintage open cars.<br>
                <strong>05:30 PM – 07:15 PM:</strong> Sunset Mandap Ceremony & Sacred Pheras with live classical flute/sitar.<br>
                <strong>08:30 PM – Midnight:</strong> Royal Gala Reception & Sit-Down Banquet dinner under the stars.</p>
                """
            }
        ],
        "faqs": [
            ("How do we keep guests on schedule without creating stress?", "Swariya's on-ground guest experience team sends gentle WhatsApp itinerary reminders 45 minutes before each function and coordinates golf carts to escort guests from their villas.")
        ]
    }
]

GUIDE_TEMPLATE = """<!DOCTYPE html>
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
    <title>{meta_title} | Swariya Weddings</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://swariyaweddings.com/{slug}.html">
    <link rel="stylesheet" href="style.css?v=26">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{meta_title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://swariyaweddings.com/{slug}.html">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://swariyaweddings.com/{hero_img}">
    
    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
    {json_ld_schema}
    </script>
    
    <style>
        .guide-hero {{
            background: linear-gradient(rgba(10, 28, 24, 0.82), rgba(10, 28, 24, 0.9)), url('{hero_img}') center/cover no-repeat;
            color: #fff;
            padding: 130px 0 70px;
            text-align: center;
        }}
        .guide-hero h1 {{
            font-family: var(--font-heading);
            font-size: clamp(2rem, 4.2vw, 3rem);
            color: #FDFBF7;
            max-width: 950px;
            margin: 0 auto 18px;
            line-height: 1.25;
        }}
        .guide-hero p.subtitle {{
            font-size: 1.1rem;
            color: #E2D7C5;
            max-width: 780px;
            margin: 0 auto 25px;
            line-height: 1.65;
        }}
        .metric-strip {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 40px 0;
        }}
        .metric-box {{
            background: #fff;
            border: 1px solid var(--border-gold);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03);
            text-align: center;
        }}
        .metric-box h4 {{
            color: var(--primary);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }}
        .metric-box p {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--dark-luxury);
            margin: 0;
        }}
        .guide-article {{
            font-size: 1.05rem;
            line-height: 1.8;
            color: #333;
        }}
        .guide-article h2 {{
            font-family: var(--font-heading);
            font-size: 1.7rem;
            color: var(--primary);
            margin: 35px 0 15px;
        }}
        .faq-box {{
            background: #fff;
            border: 1px solid var(--border-gold);
            border-radius: 10px;
            padding: 22px 26px;
            margin-bottom: 15px;
        }}
        .faq-box h3 {{
            font-size: 1.15rem;
            color: var(--dark-luxury);
            margin-bottom: 8px;
        }}
        .faq-box p {{
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

    <nav class="navbar">
        <div class="container">
            <div class="logo"><a href="index.html">SWARIYA</a></div>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About us</a></li>
                <li><a href="services.html">Our Services</a></li>
                <li><a href="destination-wedding-planner-india.html">Destinations</a></li>
                <li><a href="venues.html">Venues</a></li>
                <li><a href="client-portal.html">Wedding OS</a></li>
                <li><a href="wedding-budget-calculator.html">Budget Tool</a></li>
                <li><a href="wedding-brief-builder.html">Brief Builder</a></li>
                <li><a href="reviews.html">Reviews</a></li>
                <li><a href="contact.html" class="btn-contact">Contact us</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero -->
    <section class="guide-hero">
        <div class="container">
            <p class="section-label" style="color: var(--accent-light);">✦ {category} • {read_time}</p>
            <h1>{title}</h1>
            <p class="subtitle">{intro}</p>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="wedding-budget-calculator.html" class="btn-primary" style="background: linear-gradient(135deg, #D4AF37 0%, #AA820A 100%); color: #0A1C18; font-weight: 700; border: none; padding: 14px 28px; border-radius: 30px; text-decoration: none;">Launch Budget Calculator</a>
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I'm%20planning%20a%20destination%20wedding%20and%20would%20like%20to%20consult%20on%20budget%20and%20venue%20availability." class="btn-secondary" style="background: transparent; border: 1.5px solid #fff; color: #fff; font-weight: 600; padding: 14px 26px; border-radius: 30px; text-decoration: none;" target="_blank" rel="noopener">WhatsApp Our Directors</a>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="container" style="padding: 50px 0; max-width: 900px;">
        <!-- Metrics -->
        <div class="metric-strip">
            {metrics_html}
        </div>

        <!-- Article Body -->
        <article class="guide-article">
            {sections_html}
        </article>

        <!-- Fiduciary Banner -->
        <div style="background: linear-gradient(180deg, #FAF6F0 0%, #F5EDE0 100%); border-radius: 14px; padding: 35px; border: 1px solid var(--border-gold); margin: 50px 0;">
            <h3 style="color: var(--primary); font-size: 1.5rem; margin-bottom: 12px;">The Swariya Fiduciary Guarantee</h3>
            <p style="color: #444; line-height: 1.7; font-size: 1.02rem; margin-bottom: 20px;">
                Swariya Weddings manages your celebration with an unbending <strong>0.00% vendor markup guarantee</strong>. You contract directly with 5-star properties, sound teams, and florists at genuine wholesale trade pricing while our in-house directors manage design, negotiation, and production run-sheets.
            </p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                <a href="wedding-brief-builder.html" class="btn-primary" style="padding: 12px 24px; border-radius: 25px; text-decoration: none;">Start Your Wedding Brief</a>
                <a href="bengaluru-wedding-cost-guide-2026.html" style="color: var(--primary); font-weight: 600; padding: 12px 20px; text-decoration: underline;">View Bangalore Benchmarks →</a>
            </div>
        </div>

        <!-- FAQs -->
        <div style="margin-top: 50px;">
            <p class="section-label">✦ FREQUENTLY ASKED QUESTIONS</p>
            <h2 style="font-size: 1.8rem; color: var(--dark-luxury); margin-bottom: 25px;">Expert Planning Answers</h2>
            {faq_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="site-footer" style="margin-top: 80px;">
        <div class="container footer-content">
            <div class="footer-col">
                <a href="index.html" class="footer-logo">Swariya <span>Weddings</span></a>
                <p>Pan-India Luxury & Destination Wedding Planners. Headquartered in Bengaluru with nationwide execution across Goa, Rajasthan, Kerala, Coorg & beyond. 150+ weddings planned with zero vendor markups.</p>
                <p style="margin-top: 10px; font-size: 0.85rem; color: #888;">📍 Atelier: HSR Layout, Bengaluru | 📞 +91 80505 73382</p>
            </div>
            <div class="footer-col">
                <h4>Popular Destination Hubs</h4>
                <ul>
                    <li><a href="destination-wedding-goa.html">Goa Destination Weddings</a></li>
                    <li><a href="destination-wedding-udaipur.html">Udaipur Palace Weddings</a></li>
                    <li><a href="destination-wedding-jaipur.html">Jaipur Royal Weddings</a></li>
                    <li><a href="destination-wedding-kerala.html">Kerala Backwater Weddings</a></li>
                    <li><a href="destination-wedding-coorg.html">Coorg Plantation Weddings</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Planning Tools & Portals</h4>
                <ul>
                    <li><a href="wedding-budget-calculator.html">Budget Calculator</a></li>
                    <li><a href="wedding-brief-builder.html">Brief Builder</a></li>
                    <li><a href="client-portal.html">Wedding OS</a></li>
                    <li><a href="venues.html">All 100+ Venues</a></li>
                    <li><a href="reviews.html">Verified Reviews</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All Rights Reserved. • <a href="sitemap.xml">Sitemap</a></p>
        </div>
    </footer>
    <script src="nav.js"></script>
</body>
</html>
"""

def generate():
    print(f"Generating Phase 3: {len(PHASE3_GUIDES)} Cost Breakdowns & Cultural Tradition Guides...")
    generated_urls = []

    for g in PHASE3_GUIDES:
        slug = g["slug"]
        title = g["title"]
        meta_title = g["meta_title"]
        meta_desc = g["meta_desc"]
        category = g["category"]
        read_time = g["read_time"]
        hero_img = g["hero_img"]
        intro = g["intro"]

        # Metrics HTML
        metrics_html = "\n".join([f"""
        <div class="metric-box">
            <h4>{k}</h4>
            <p>{v}</p>
        </div>""" for k, v in g["key_metrics"]])

        # Sections HTML
        sections_html = "\n".join([f"""
        <section style="margin-bottom: 30px;">
            <h2>{s["heading"]}</h2>
            {s["content"]}
        </section>""" for s in g["sections"]])

        # FAQs
        faqs_schema = [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            } for q, a in g["faqs"]
        ]

        faq_html = "\n".join([f"""
        <div class="faq-box">
            <h3>{q}</h3>
            <p>{a}</p>
        </div>""" for q, a in g["faqs"]])

        json_ld_schema = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Article",
                    "@id": f"https://swariyaweddings.com/{slug}.html#article",
                    "headline": title,
                    "description": meta_desc,
                    "image": f"https://swariyaweddings.com/{hero_img}",
                    "author": {
                        "@type": "Organization",
                        "name": "Swariya Weddings",
                        "url": "https://swariyaweddings.com/"
                    },
                    "publisher": {
                        "@type": "Organization",
                        "name": "Swariya Weddings",
                        "logo": {
                            "@type": "ImageObject",
                            "url": "https://swariyaweddings.com/images/1.jpg"
                        }
                    },
                    "datePublished": "2026-09-13",
                    "dateModified": "2026-09-13"
                },
                {
                    "@type": "FAQPage",
                    "@id": f"https://swariyaweddings.com/{slug}.html#faq",
                    "mainEntity": faqs_schema
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"https://swariyaweddings.com/{slug}.html#breadcrumb",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://swariyaweddings.com/"},
                        {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://swariyaweddings.com/destination-wedding-planner-india.html"},
                        {"@type": "ListItem", "position": 3, "name": title, "item": f"https://swariyaweddings.com/{slug}.html"}
                    ]
                }
            ]
        }, indent=2)

        rendered = GUIDE_TEMPLATE.format(
            slug=slug,
            title=title,
            meta_title=meta_title,
            meta_desc=meta_desc,
            category=category,
            read_time=read_time,
            hero_img=hero_img,
            intro=intro,
            metrics_html=metrics_html,
            sections_html=sections_html,
            faq_html=faq_html,
            json_ld_schema=json_ld_schema
        )

        filepath = f"{slug}.html"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(rendered)

        generated_urls.append(f"https://swariyaweddings.com/{slug}.html")
        print(f"  -> Generated: {filepath}")

    # Update sitemap.xml
    print("\nUpdating sitemap.xml with Phase 3 guide pages...")
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
        print(f"Added {len(new_entries)} guide URLs to sitemap.xml")

    # Update llms.txt
    print("\nUpdating llms.txt...")
    with open("llms.txt", "r", encoding="utf-8") as f:
        llms_content = f.read()

    llms_entries = []
    for g in PHASE3_GUIDES:
        link_str = f"- [{g['title']}](https://swariyaweddings.com/{g['slug']}.html): {g['meta_desc']}"
        if g['slug'] not in llms_content:
            llms_entries.append(link_str)

    if llms_entries:
        with open("llms.txt", "a", encoding="utf-8") as f:
            f.write("\n\n## Phase 3 Cost Breakdowns & Cultural Tradition Guides\n" + "\n".join(llms_entries) + "\n")
        print(f"Added {len(llms_entries)} entries to llms.txt")

    print(f"\n🎉 PHASE 3 COMPLETE! Successfully generated {len(PHASE3_GUIDES)} authority guides.")

if __name__ == "__main__":
    generate()
