# -*- coding: utf-8 -*-
"""
Swariya Weddings - 500 Micro-Markets High-Density Data Matrix
Produces 500 distinct, rich, high-converting luxury wedding targets.
"""

import os

def build_500_dataset():
    markets = []
    seen_slugs = set()

    def add_market(slug, cat, title, meta_desc, h1, subtitle, loc_name, city, state, budget, capacity, venues, log, img, faqs):
        if slug in seen_slugs:
            return
        seen_slugs.add(slug)
        markets.append({
            "slug": slug,
            "category": cat,
            "title": title,
            "meta_desc": meta_desc,
            "h1": h1,
            "subtitle": subtitle,
            "location_name": loc_name,
            "city": city,
            "state": state,
            "budget_range": budget,
            "guest_capacity": capacity,
            "venues": venues,
            "logistics": log,
            "hero_img": img,
            "faqs": faqs
        })

    # -------------------------------------------------------------------------
    # 1. BENGALURU (60 Hubs)
    # -------------------------------------------------------------------------
    blr_zones = [
        "Sadashivanagar", "Indiranagar", "Palace Grounds", "Lavelle Road & UB City", "Koramangala",
        "Whitefield", "HSR Layout", "Jayamahal", "Hebbal", "Nandi Hills", "Kanakapura Road",
        "Sarjapur Road", "Malleshwaram", "Jayanagar", "JP Nagar", "Electronic City", "Bellandur",
        "Bannerghatta Road", "Yelahanka", "Cunningham Road", "Dollars Colony", "Richmond Town",
        "Vasanth Nagar", "Ulsoor", "Frazer Town", "Rajajinagar", "Basavanagudi", "Hennur",
        "Sahakara Nagar", "Benson Town", "MG Road & Brigade Road", "Residency Road", "Kalyan Nagar",
        "Devanahalli", "Nelamangala Highway", "Hosur Road", "Marathahalli", "Domlur & Old Airport Road",
        "Bannerghatta National Park", "Thanisandra & Manyata", "Peenya & Tumkur Road", "Banashankari",
        "Vijayanagar", "Kengeri & Mysore Road", "Kogilu & Bagalur", "Harlur Road", "Kudlu Gate",
        "Mahadevapura", "Varthur & Gunjur", "BTM Layout", "Rajarajeshwari Nagar", "Nagarbhavi",
        "Yeshwanthpur", "Chikkabanavara & Hesaraghatta", "Kadugodi & Hope Farm", "Kumaraswamy Layout",
        "Padmanabhanagar", "Sanjay Nagar & RMV", "RT Nagar", "Horamavu & Kalkere"
    ]

    for b in blr_zones:
        s = f"wedding-planners-in-{b.lower().replace(' & ', '-').replace(' ', '-')}-bangalore"
        add_market(
            slug=s,
            cat="bengaluru",
            title=f"Luxury Wedding Planners in {b} Bangalore | Swariya Weddings",
            meta_desc=f"Premier luxury wedding planning in {b} Bangalore. 5-star venue concierge, 3D mandap architecture & 100% transparent zero-markup billing.",
            h1=f"Luxury Wedding Planners in {b} Bangalore",
            subtitle="Bespoke Royal Celebrations, Signature Venue Styling & Turnkey Execution",
            loc_name=f"{b}, Bangalore",
            city="Bengaluru",
            state="Karnataka",
            budget="₹50 Lakhs – ₹4+ Crores",
            capacity="200 to 2,500+ Guests",
            venues=["Taj West End Bengaluru", "Palace Grounds Gayatri Vihar", "The Leela Palace Bengaluru", "Four Seasons Hotel"],
            log="Central access to Bangalore's premier hospitality corridors with direct vendor billing and 3D pre-production visualization.",
            img="images/11.jpg",
            faqs=[
                {"q": f"Why choose Swariya for a luxury wedding in {b}?", "a": f"Swariya provides turnkey wedding management in {b} with 0% vendor markups, 3D architectural decor design, and a dedicated bridal shadow planner."},
                {"q": f"How do you coordinate catering and venue bookings in {b}?", "a": "We negotiate direct wholesale room blocks and manage live multi-cuisine banqueting lanes."},
                {"q": "How early should we book our wedding dates?", "a": "We recommend locking dates 6 to 9 months in advance for prime wedding muhurathams."}
            ]
        )

    # -------------------------------------------------------------------------
    # 2. RAJASTHAN PALACE & FORT DESTINATIONS (50 Hubs)
    # -------------------------------------------------------------------------
    raj_zones = [
        ("Udaipur Lake Pichola", "Udaipur", "Lake Pichola island palaces, boat baraats & royal Mewari grandeur."),
        ("Udaipur Fateh Sagar", "Udaipur", "Lakeside luxury resorts, panoramic Aravalli sunsets & starlit banquets."),
        ("Jaipur Kukas Palaces", "Jaipur", "Grand palatial ballrooms, 500+ room inventory & Delhi-Jaipur highway ease."),
        ("Jaipur Amer & Central", "Jaipur", "Rambagh Palace heritage, vintage royal cars & elephant cavalry baraats."),
        ("Jodhpur Umaid Bhawan", "Jodhpur", "Monumental golden sandstone palace, private jet tarmac coordination & royal luxury."),
        ("Jodhpur Mehrangarh Fort", "Jodhpur", "15th-century cliffside fort galas, Rajasthani folk ensembles & starlit dinners."),
        ("Jaisalmer Sam Sand Dunes", "Jaisalmer", "Arabian Nights desert camps, illuminated sand dune stages & winter luxury."),
        ("Jaisalmer Suryagarh Fort", "Jaisalmer", "Bespoke desert fortress luxury, royal courtyards & opulent hospitality."),
        ("Pushkar Desert Oasis", "Pushkar", "Sacred lake sunset Maha Aartis, private pool villa resorts & rose petal showers."),
        ("Ranthambore Six Senses Barwara", "Sawai Madhopur", "14th-century restored fortress, tiger safari concierge & wilderness luxury."),
        ("Kumbhalgarh Fortress", "Kumbhalgarh", "Great Wall cliffside views, mountain valley breezes & 2 hours from Udaipur."),
        ("Neemrana Fort-Palace", "Neemrana", "14-tiered medieval ramparts, Roman amphitheaters & 2 hours from Delhi."),
        ("Bikaner Laxmi Niwas Palace", "Bikaner", "Carved red sandstone architecture, private lake sanctuaries & royal Marwari feasts."),
        ("Bikaner Narendra Bhawan", "Bikaner", "Boutique royal chic design, bespoke mixology & aristocratic heritage."),
        ("Mount Abu Hilltop", "Mount Abu", "Rajasthan's only hill station, cool mountain breezes & Nakki lake romance."),
        ("Alwar Hill Fort-Kesroli", "Alwar", "14th-century hilltop fortress, 360-degree mustard field views & Delhi proximity."),
        ("Samode Palace & Bagh", "Samode", "475-year-old painted haveli ceilings, mirrored Darbar Halls & Mughal gardens."),
        ("Mandawa Frescoed Havelis", "Mandawa", "Medieval castle ramparts, Shekhawati frescoed courtyards & royal hospitality."),
        ("Khimsar Fort & Dunes", "Khimsar", "16th-century fortress surrounded by untouched sand dunes between Jodhpur and Bikaner."),
        ("Chittorgarh Fort Corridors", "Chittorgarh", "Legendary Rajput fort history, sprawling heritage courtyards & Udaipur proximity."),
        ("Bundi Heritage Havelis", "Bundi", "Stepwell architectural motifs, Taragarh Fort vistas & authentic Rajputana hospitality."),
        ("Rohet Garh Heritage", "Rohet", "Aristocratic equestrian estates, peacock-filled courtyards & rural desert serenity."),
        ("Deogarh Mahal", "Deogarh", "17th-century hilltop palace, mirrored rooms & royal Mewari banqueting."),
        ("Bharatpur Laxmi Vilas Palace", "Bharatpur", "Keoladeo bird sanctuary borders, royal duck shooting lodge heritage & Agra proximity."),
        ("Kota Chambal Riverfront", "Kota", "Chambal riverfront palaces, grand Rajput havelis & opulent royal stagecraft.")
    ]

    for r_name, r_city, r_desc in raj_zones:
        # Standard format
        s1 = f"destination-wedding-planner-in-{r_name.lower().replace(' & ', '-').replace(' ', '-')}-rajasthan"
        add_market(
            slug=s1,
            cat="rajasthan",
            title=f"Royal Destination Wedding Planner in {r_name} Rajasthan | Swariya",
            meta_desc=f"Premier royal palace wedding planning in {r_name} Rajasthan. {r_desc}",
            h1=f"Royal Destination Wedding Planner in {r_name}",
            subtitle="Imperial Palaces, Historic Fortresses & Unrivaled Rajputana Hospitality",
            loc_name=f"{r_name}, Rajasthan",
            city=r_city,
            state="Rajasthan",
            budget="₹1 Crore – ₹12+ Crores",
            capacity="150 to 1,200+ Guests",
            venues=["Taj Lake Palace", "The Oberoi Udaivilas", "Fairmont Jaipur", "Umaid Bhawan Palace", "Suryagarh Jaisalmer"],
            log="Full charter transit, heritage conservation permissions, royal cavalry baraats, and 3D architectural decor preview.",
            img="images/10.jpg",
            faqs=[
                {"q": f"What is the average cost of a royal palace wedding in {r_name}?", "a": "A 3-day luxury palace wedding in Rajasthan ranges from ₹1 Cr to ₹8+ Cr depending on palace buyout and guest count."},
                {"q": "How does Swariya manage outstation vendor logistics in Rajasthan?", "a": "We maintain active production hubs in Jaipur, Udaipur, and Delhi to provide local artisan rates with 0% markups."},
                {"q": "Can you organize royal baraats with vintage cars and royal horses?", "a": "Yes, we arrange authentic vintage convertibles, royal flagbearers, elephant regalia, and synchronized Nagada drummers."}
            ]
        )

        # Cost guide format for SEO dominance
        s2 = f"cost-of-destination-wedding-in-{r_name.lower().replace(' & ', '-').replace(' ', '-')}-2026"
        add_market(
            slug=s2,
            cat="rajasthan",
            title=f"Cost of Destination Wedding in {r_name} (2026 Price Benchmark) | Swariya",
            meta_desc=f"Complete 2026 cost guide for destination weddings in {r_name} Rajasthan. Venue buyouts, catering rates, 3D decor costs & budget calculator.",
            h1=f"Cost of Destination Wedding in {r_name} (2026 Guide)",
            subtitle="Itemized Budget Breakdown, Palace Buyout Pricing & 0% Markup Savings",
            loc_name=f"{r_name}, Rajasthan",
            city=r_city,
            state="Rajasthan",
            budget="₹80 Lakhs – ₹10+ Crores",
            capacity="100 to 1,000+ Guests",
            venues=["Taj Heritage Properties", "Oberoi Luxury Resorts", "Fairmont Corridors", "Palace Pavilions"],
            log="Comprehensive itemized breakdown covering room blocks, multi-cuisine banqueting, stage production, and guest logistics.",
            img="images/9.jpg",
            faqs=[
                {"q": f"How much does a 150-guest wedding cost in {r_name}?", "a": "For 150 guests across 2 to 3 days, expected expenditure ranges from ₹1.2 Cr to ₹3.5 Cr including 5-star lodging, decor, and dining."},
                {"q": "How do clients save 15-20% with Swariya?", "a": "Because we operate with 0% vendor markups, you pay actual trade wholesale rates directly to venues and suppliers."},
                {"q": "What is included in the Swariya management retainer?", "a": "End-to-end planning, 3D stage renders, vendor contracting, day-of timeline coordination, and guest concierge desks."}
            ]
        )

    # -------------------------------------------------------------------------
    # 3. GOA & KERALA COASTAL & BACKWATER DESTINATIONS (70 Hubs)
    # -------------------------------------------------------------------------
    coastal_zones = [
        # Goa
        ("Candolim Beach", "Goa", "North Goa", "Portuguese sea ramparts, beachfront lawns, and high-energy nightlife integration."),
        ("Calangute Beach", "Goa", "North Goa", "Golden sands, vibrant coastal nightlife & sprawling 5-star resort lawns."),
        ("Morjim Beach", "Goa", "North Goa", "Pristine white sand beaches, boho-luxe beach clubs & sunset open horizons."),
        ("Ashwem Beach", "Goa", "North Goa", "Boho-chic aesthetics, quiet coconut palm shores & starlit barefoot pheras."),
        ("Vagator Clifftop", "Goa", "North Goa", "Dramatic clifftop ocean views, Chapora Fort backdrop & W Goa glamour."),
        ("Anjuna Beach", "Goa", "North Goa", "Iconic coastal vibes, luxury sea-facing villa buyouts & electronic music sunsets."),
        ("Siolim Riverfront", "Goa", "North Goa", "Chapora riverfront heritage mansions, private yacht cruises & luxury soirees."),
        ("Cavelossim Beach", "Goa", "South Goa", "The Leela Goa grandeur, 75-acre sprawling lawns, private lagoons & golf courses."),
        ("Benaulim Beach", "Goa", "South Goa", "Taj Exotica Mediterranean splendor, 56 acres of manicured gardens & secluded shores."),
        ("Utorda & Majorda", "Goa", "South Goa", "ITC Grand Goa Indo-Portuguese village architecture, multi-tiered swimming lagoons."),
        ("Mobor Beach", "Goa", "South Goa", "Where Sal River meets the Arabian Sea, offering unmatched private beach exclusivity."),
        ("Varca Beach", "Goa", "South Goa", "Soft white sands, meandering pool lagoons & tranquil Goan coconut groves."),
        ("Betalbatim Beach", "Goa", "South Goa", "Sunset beach lawns, quiet coastal pine groves & intimate luxury villas."),
        ("Arossim Beach", "Goa", "South Goa", "ITC Grand Goa oceanfront frontage, heritage chapel settings & 20 mins from airport."),
        ("Sinquerim Fort Aguada", "Goa", "North Goa", "16th-century fortress ramparts meeting golden sands at the foot of Fort Aguada."),
        ("Mandrem Beach", "Goa", "North Goa", "Untouched northern coastal serenity, organic bamboo styling & barefoot vows."),
        ("Colva Beach", "Goa", "South Goa", "Expansive golden shores, luxury resort lawns & authentic Goan Catholic charm."),
        ("Bogmalo Beach", "Goa", "South Goa", "Cove beach tranquility, panoramic oceanfront cliffs & 10 mins airport ease."),

        # Kerala
        ("Kumarakom Backwaters", "Kerala", "Kumarakom", "Vembanad Lake houseboat flotillas, Chenda Melam percussion & Sadhya feasts."),
        ("Alleppey Canals", "Kerala", "Alleppey", "Venice of the East backwaters, traditional snake boat races & floating lotus mandaps."),
        ("Kovalam Clifftop", "Kerala", "Kovalam", "The Leela Kovalam rocky clifftop lawns perched above ocean waves, 20 mins from TRV airport."),
        ("Kochi Bolgatty Marina", "Kerala", "Kochi", "Grand Hyatt Bolgatty island luxury, water metro shuttles & colonial Fort Kochi charm."),
        ("Munnar Tea Plantations", "Kerala", "Munnar", "Misty green slopes, crisp mountain air year-round & highland luxury resort buyouts."),
        ("Wayanad Rainforest", "Kerala", "Wayanad", "Western Ghats rainforests, natural stream crossings & sustainable zero-waste weddings."),
        ("Bekal Fort & Beach", "Kerala", "Bekal", "Taj Bekal Kettuvallam pool villas, backwater lagoons & 17th-century fort ramparts."),
        ("Varkala Clifftop", "Kerala", "Varkala", "Dramatic red laterite coastal cliffs overlooking the sea, ideal for sunset vows."),
        ("Marari Beach", "Kerala", "Mararikulam", "Secluded eco-luxury coconut palm shores and private luxury wellness villas."),
        ("Poovar Island Estuary", "Kerala", "Poovar", "Floating water cottages where Neyyar River meets golden beach and sea."),
        ("Thekkady Spice Hills", "Kerala", "Thekkady", "Cardamom plantation valleys, Periyar wildlife sanctuary & cool mountain air."),
        ("Kollam Ashtamudi Lake", "Kerala", "Kollam", "The Raviz Ashtamudi heritage palace, eight-looped lake views & backwater cruises."),
        ("Calicut Malabar Coast", "Kerala", "Calicut", "Malabar heritage, legendary culinary feasts, beachside resorts & CCJ airport access."),
        ("Kannur Theyyam Heritage", "Kerala", "Kannur", "Theyyam folk art rituals, secluded cliff beaches & new international airport connectivity."),
        ("Thrissur Cultural Epics", "Kerala", "Thrissur", "Cultural capital of Kerala, temple elephant processions & grand classical weddings."),
        ("Palakkad Heritage Manors", "Kerala", "Palakkad", "Historic Tharavadu ancestral homes, lush paddy fields & authentic Vedic rituals.")
    ]

    for c_name, c_state, c_city, c_desc in coastal_zones:
        # Destination Guide
        s1 = f"destination-wedding-planner-in-{c_name.lower().replace(' & ', '-').replace(' ', '-')}"
        add_market(
            slug=s1,
            cat="goa-kerala",
            title=f"Luxury Destination Wedding Planner in {c_name} | Swariya Weddings",
            meta_desc=f"Premier destination wedding planning in {c_name}, {c_state}. {c_desc}",
            h1=f"Luxury Destination Wedding Planner in {c_name}",
            subtitle="Coastal Splendor, Backwater Serenity & Bespoke Turnkey Coordination",
            loc_name=f"{c_name}, {c_state}",
            city=c_city,
            state=c_state,
            budget="₹75 Lakhs – ₹6+ Crores",
            capacity="100 to 1,000+ Guests",
            venues=["The Leela", "Taj Exotica & Fort Aguada", "ITC Grand Goa", "Grand Hyatt Kochi", "Kumarakom Lake Resort"],
            log="Coastal CRZ clearances, houseboat charter logistics, tidal schedule alignment, and sound curfew compliances.",
            img="images/1.jpg" if c_state == "Goa" else "images/6.jpg",
            faqs=[
                {"q": f"What permissions are required for a beach/backwater wedding in {c_name}?", "a": "Swariya secures all state tourism clearances, coastal police permissions, sound licenses, and marine safety cordons."},
                {"q": f"What is the best time of year for a wedding in {c_name}?", "a": "October through April offers clear blue skies, pleasant sea/lake breezes, and zero rainfall."},
                {"q": "Can you organize houseboat transfers or boat baraats?", "a": "Yes, we construct illuminated floating barge stages and luxury catamaran transfers for groom entries."}
            ]
        )

        # Cost Breakdown Guide
        s2 = f"cost-of-wedding-in-{c_name.lower().replace(' & ', '-').replace(' ', '-')}-2026"
        add_market(
            slug=s2,
            cat="goa-kerala",
            title=f"Cost of Wedding in {c_name} (2026 Price Benchmark) | Swariya",
            meta_desc=f"Detailed 2026 price guide for destination weddings in {c_name}, {c_state}. Resort buyouts, catering rates & transparent 0% markup estimates.",
            h1=f"Cost of Wedding in {c_name} (2026 Guide)",
            subtitle="Itemized Cost Matrix, Resort Buyouts & Direct Wholesale Vendor Pricing",
            loc_name=f"{c_name}, {c_state}",
            city=c_city,
            state=c_state,
            budget="₹60 Lakhs – ₹5+ Crores",
            capacity="100 to 800+ Guests",
            venues=["5-Star Luxury Beach Resorts", "Private Waterfront Villas", "Heritage Backwater Properties"],
            log="Line-by-line budgeting for rooms, food & beverage banqueting, floral decor, audio-visual trussing, and artist fees.",
            img="images/2.jpg" if c_state == "Goa" else "images/7.jpg",
            faqs=[
                {"q": f"How much does an average 100-150 guest wedding cost in {c_name}?", "a": "Typically between ₹75 Lakhs and ₹2.5 Crores depending on whether a full 5-star resort buyout or boutique villa is selected."},
                {"q": "How does Swariya ensure budget adherence?", "a": "You receive live access to our digital budget tracker with line-item vendor quotes and 0% markups."},
                {"q": "Are airport transfers included in the wedding budget?", "a": "Yes, we structure dedicated airport shuttle convoys and baggage logistics within the overall transport budget."}
            ]
        )

    # -------------------------------------------------------------------------
    # 4. KARNATAKA DESTINATIONS & ESCAPES (40 Hubs)
    # -------------------------------------------------------------------------
    karnataka_escapes = [
        ("Coorg Coffee Estates", "Madikeri", "Rainforest luxury villas, infinity valley pools & authentic Kodava traditions."),
        ("Kabini River Sanctuary", "Kabini", "Sunset riverfront views over elephant reserves, starlit lawns & safari lodges."),
        ("Chikmagalur Mullayanagiri", "Chikmagalur", "Mountain peak decks, coffee blossom fragrance & private pool villas."),
        ("Hampi Kamalapura Palace", "Hampi", "14th-century Vijayanagara stone architecture, water chambers & royal temple mandaps."),
        ("Sakleshpur Valley", "Sakleshpur", "Cardamom estate hills, waterfalls & luxury private resort buyouts 3.5 hrs from Bangalore."),
        ("Mysore Lalitha Mahal", "Mysuru", "Italian marble palace halls, royal Wodeyar heritage & 75 mins expressway transit."),
        ("Gokarna Kahani Paradise", "Gokarna", "Private 20-acre cliffside royal estate overlooking untouched beaches."),
        ("Dandeli Kali River", "Dandeli", "Teak forest canopies, river rafting adventures & rustic-luxe open-air sangeets."),
        ("Bandipur Forest Reserve", "Bandipur", "Nilgiri biosphere foothills, wildlife lodge buyouts & peaceful stargazing pheras."),
        ("Udupi & Malpe Beach", "Udupi", "Historic temple rituals, Malpe beach lawns & coastal Bunt/Konkani wedding dining."),
        ("Mangalore Coastal Corridors", "Mangalore", "Historic heritage halls, beach resorts & direct international airport connectivity."),
        ("Nagarhole Forest Retreat", "Nagarhole", "Dense teakwood jungles, Kabini river backwaters & luxury eco-resort weddings."),
        ("Badami Cave Temple Corridors", "Badami", "Red sandstone cliffs, Chalukya dynasty heritage & historic temple mandaps."),
        ("Belur & Halebidu Heritage", "Hassan", "Hoysala architectural wonders, intricately carved stone pillars & Vedic rituals."),
        ("Davanagere Royal Conventions", "Davanagere", "Central Karnataka transit ease, massive convention lawns & royal community banquets."),
        ("Shimoga & Jog Falls Corridors", "Shimoga", "Western Ghats green foothills, waterfall excursions & tranquil resort lawns."),
        ("Hubli & Dharwad Corridors", "Hubli", "North Karnataka business hub, grand 5-star hotel ballrooms & direct airport ease."),
        ("Belgaum Heritage Hills", "Belgaum", "Maratha-Kannada cultural fusion, historic fortresses & cool mountain breezes."),
        ("Bijapur Gol Gumbaz Corridors", "Bijapur", "Adil Shahi architectural heritage, grand domed pavilions & royal Awadhi dining."),
        ("Karwar Coastal Islands", "Karwar", "Rabindranath Tagore beach shores, Kali river estuary & pristine island resorts.")
    ]

    for k_name, k_city, k_desc in karnataka_escapes:
        s1 = f"destination-wedding-planner-in-{k_name.lower().replace(' & ', '-').replace(' ', '-')}-karnataka"
        add_market(
            slug=s1,
            cat="karnataka-destinations",
            title=f"Destination Wedding Planner in {k_name} Karnataka | Swariya",
            meta_desc=f"Premier luxury destination wedding planning in {k_name} Karnataka. {k_desc}",
            h1=f"Destination Wedding Planner in {k_name}",
            subtitle="Coffee Estates, Royal Palaces & Nature Sanctuaries Across Karnataka",
            loc_name=f"{k_name}, Karnataka",
            city=k_city,
            state="Karnataka",
            budget="₹50 Lakhs – ₹4 Crores",
            capacity="100 to 800+ Guests",
            venues=["Taj Madikeri", "The Tamara Coorg", "Evolve Back Resorts", "The Serai Chikmagalur", "Lalitha Mahal Palace"],
            log="Direct road transit coordination from Bengaluru, estate buyouts, local tribal permissions, and weatherproofing.",
            img="images/12.jpg",
            faqs=[
                {"q": f"How accessible is {k_name} from Bangalore?", "a": f"{k_name} is accessible via smooth highway expressway routes or regional airports with dedicated coach shuttles."},
                {"q": "Can you design authentic Karnataka regional menus?", "a": "Yes, we curate authentic regional delicacies including Mysore Pak, Bisi Bele Bath, Coorg Pandi Curry, and Mangalorean Kori Rotti."},
                {"q": "What decor themes fit these nature venues?", "a": "Living botanical arches, brass urlis, Madurai jasmine strings, and starlit fairy-light canopies."}
            ]
        )

        s2 = f"cost-of-wedding-in-{k_name.lower().replace(' & ', '-').replace(' ', '-')}-2026"
        add_market(
            slug=s2,
            cat="karnataka-destinations",
            title=f"Cost of Wedding in {k_name} (2026 Price Guide) | Swariya",
            meta_desc=f"Comprehensive 2026 cost benchmark for destination weddings in {k_name} Karnataka. Resort buyouts, catering & 0% markup estimates.",
            h1=f"Cost of Wedding in {k_name} (2026 Guide)",
            subtitle="Itemized Cost Breakdown, Estate Buyout Pricing & Transparent Fiduciary Billing",
            loc_name=f"{k_name}, Karnataka",
            city=k_city,
            state="Karnataka",
            budget="₹45 Lakhs – ₹3.5 Crores",
            capacity="80 to 600+ Guests",
            venues=["Luxury Plantation Resorts", "Heritage Palace Properties", "Eco-Luxe Sanctuaries"],
            log="Clear breakdown of estate buyout rates, food & beverage packages, floral and lighting production, and guest logistics.",
            img="images/13.jpg",
            faqs=[
                {"q": f"What is the average cost of a 100-guest estate wedding in {k_name}?", "a": "Between ₹50 Lakhs and ₹1.5 Crores for complete 2-day lodging, decor, and dining."},
                {"q": "Why is Swariya's zero-markup model better?", "a": "You pay direct supplier trade rates, saving an average of 15% to 20% on total wedding spend."},
                {"q": "How is weather contingency managed?", "a": "We maintain transparent German marquee tenting and waterproof stage trussing on standby."}
            ]
        )

    # -------------------------------------------------------------------------
    # 5. NORTHERN & WESTERN HILL RETREATS (40 Hubs)
    # -------------------------------------------------------------------------
    hill_retreats = [
        ("Mussoorie Walnut Grove", "Mussoorie", "Uttarakhand", "Snow-capped Himalayan horizons, heated Victorian marquees & JW Marriott luxury."),
        ("Rishikesh Holy Riverfront", "Rishikesh", "Uttarakhand", "Taj Rishikesh pebble riverbank vows, sacred Ganga Aarti & Himalayan tranquility."),
        ("Jim Corbett Kosi River", "Ramnagar", "Uttarakhand", "Sal forest wilderness, open-air riverbank sangeet stages & safari hospitality."),
        ("Dehradun Sal Forest", "Dehradun", "Uttarakhand", "Hyatt Regency ballrooms, airport direct flight ease & mountain lawn panoramas."),
        ("Shimla Cedar Forest", "Shimla", "Himachal Pradesh", "Wildflower Hall colonial heritage, 8,250 ft elevation & British heritage ballrooms."),
        ("Kasauli Pine Ridges", "Kasauli", "Himachal Pradesh", "Pine-scented mountain ridges, starlit decks & 75 mins drive from Chandigarh Airport."),
        ("Dharamshala Snow Peaks", "Dharamshala", "Himachal Pradesh", "Dhauladhar mountain panoramas, cedar forest peace & Hyatt Regency luxury."),
        ("Nainital Lake Vistas", "Nainital", "Uttarakhand", "Emerald lake views, colonial heritage manors & crisp mountain air."),
        ("Alibaug Coastal Mansions", "Alibaug", "Maharashtra", "20-minute speedboat transfers from Gateway of India, private pool villa buyouts."),
        ("Lonavala Sahyadri Valleys", "Lonavala", "Maharashtra", "Equal 2-hour expressway transit from Mumbai and Pune, high-tech concert arenas."),
        ("Mahabaleshwar Forest Peaks", "Mahabaleshwar", "Maharashtra", "Le Méridien evergreen forest decks, infinity valley pools & cool microclimates."),
        ("Karjat Organic Acreage", "Karjat", "Maharashtra", "Oleander Farms rustic luxury, private lakefront lawns & 90 mins from Mumbai."),
        ("Pawna Lakefront Lawns", "Pawna", "Maharashtra", "Lakeside sunset pheras, Sahyadri fort backdrops & private boutique estates."),
        ("Lavasa Lakeside Promenades", "Lavasa", "Maharashtra", "Italian Riviera architecture, lakeside promenades & scenic mountain tranquility."),
        ("Nashik Sula Vineyards", "Nashik", "Maharashtra", "Rolling vineyard amphitheatres, wine tasting soirees & French country aesthetics."),
        ("Igatpuri Foggy Hills", "Igatpuri", "Maharashtra", "Mystic waterfalls, vast resort lawns & 2.5 hours drive from Mumbai."),
        ("Manali Himalayan Horizons", "Manali", "Himachal Pradesh", "Snow-capped peaks, apple orchards, riverfront pine lawns & luxury resort buyouts."),
        ("Dalhousie Pine Slopes", "Dalhousie", "Himachal Pradesh", "Scottish and Victorian architecture, mist-covered valleys & historic churches."),
        ("Mukteshwar Fruit Orchards", "Mukteshwar", "Uttarakhand", "Panoramic Nanda Devi snow peaks, cliffside sunset decks & serene tranquility."),
        ("Kanatal & Dhanaulti Hills", "Kanatal", "Uttarakhand", "Untouched pine ridges, starlit sky domes & 360-degree Himalayan snow vistas.")
    ]

    for h_name, h_city, h_state, h_desc in hill_retreats:
        s1 = f"destination-wedding-planner-in-{h_name.lower().replace(' & ', '-').replace(' ', '-')}"
        add_market(
            slug=s1,
            cat="north-hills",
            title=f"Himalayan & Hilltop Wedding Planner in {h_name} | Swariya",
            meta_desc=f"Premier mountain resort wedding planning in {h_name}, {h_state}. {h_desc}",
            h1=f"Himalayan & Hilltop Wedding Planner in {h_name}",
            subtitle="Mountain Horizons, Misty Valleys & Unforgettable Highland Nuptials",
            loc_name=f"{h_name}, {h_state}",
            city=h_city,
            state=h_state,
            budget="₹75 Lakhs – ₹6+ Crores",
            capacity="100 to 600+ Guests",
            venues=["JW Marriott Mussoorie", "Taj Rishikesh", "Wildflower Hall Shimla", "Le Méridien Mahabaleshwar", "Oleander Farms Karjat"],
            log="Heated indoor/glass marquee structures, specialized mountain transport convoys, and acoustic line-array staging.",
            img="images/2.jpg",
            faqs=[
                {"q": f"How do you manage cold mountain temperatures in {h_name}?", "a": "We construct transparent heated glasshouse pavilions, patio heaters, warm pashmina blankets, and live bonfire pits."},
                {"q": f"How do outstation guests reach {h_name}?", "a": "We coordinate private luxury shuttles from the nearest major airport or railway terminus."},
                {"q": "What decor themes complement mountain weddings?", "a": "Pinecones, wild eucalyptus, white roses, crystal chandeliers, and rustic wooden cross-back furniture."}
            ]
        )

        s2 = f"cost-of-destination-wedding-in-{h_name.lower().replace(' & ', '-').replace(' ', '-')}-2026"
        add_market(
            slug=s2,
            cat="north-hills",
            title=f"Cost of Wedding in {h_name} (2026 Price Benchmark) | Swariya",
            meta_desc=f"2026 cost guide for mountain weddings in {h_name}, {h_state}. Resort buyouts, catering rates & 0% markup estimates.",
            h1=f"Cost of Wedding in {h_name} (2026 Guide)",
            subtitle="Itemized Mountain Wedding Pricing, Resort Buyouts & Direct Wholesale Rates",
            loc_name=f"{h_name}, {h_state}",
            city=h_city,
            state=h_state,
            budget="₹60 Lakhs – ₹5 Crores",
            capacity="80 to 500+ Guests",
            venues=["5-Star Luxury Mountain Resorts", "Boutique Heritage Manors", "Vineyard Estates"],
            log="Comprehensive budget modeling for heated tenting, transport shuttles, audio-visual trussing, and 5-star lodging.",
            img="images/3.jpg",
            faqs=[
                {"q": f"What is the average spend for a 150-guest wedding in {h_name}?", "a": "Typically ranges from ₹80 Lakhs to ₹2.8 Crores including 5-star accommodation, bespoke decor, and catering."},
                {"q": "How does Swariya's zero-markup model save money?", "a": "You pay actual direct vendor bills with zero hidden kickbacks, saving 15-20% on overall wedding spend."},
                {"q": "How far in advance should we book mountain resorts?", "a": "For peak summer or winter months, booking 6 to 9 months ahead is strongly recommended."}
            ]
        )

    # -------------------------------------------------------------------------
    # 6. MAJOR METROS: MUMBAI, DELHI NCR, HYDERABAD, CHENNAI, PUNE, KOLKATA (120 Hubs)
    # -------------------------------------------------------------------------
    metro_corridors = [
        # Mumbai MMR (30)
        ("South Mumbai Colaba", "Mumbai", "Maharashtra", "The Taj Mahal Palace, Arabian Sea views & old-money high-society elegance."),
        ("Nariman Point & Marine Drive", "Mumbai", "Maharashtra", "Trident Nariman Point, Queens Necklace vistas & presidential luxury."),
        ("Bandra West & Pali Hill", "Mumbai", "Maharashtra", "Taj Lands End seaside amphitheater, celebrity styling & high-glam cocktail soirees."),
        ("Juhu Beachfront", "Mumbai", "Maharashtra", "JW Marriott Juhu, sunset Arabian sea mandaps & Bollywood-scale sangeets."),
        ("Worli Sea Face", "Mumbai", "Maharashtra", "The St. Regis Mumbai, NSCI Dome arena scale & sea link horizons."),
        ("Lower Parel High Grounds", "Mumbai", "Maharashtra", "Four Seasons Hotel Mumbai, Level 37 rooftop nightlife & chic banqueting."),
        ("Bandra Kurla Complex (BKC)", "Mumbai", "Maharashtra", "Jio World Convention Centre monumental scale, Sofitel BKC & high-tech stages."),
        ("Powai Lakefront", "Mumbai", "Maharashtra", "The Westin Mumbai Powai Lake, scenic panoramic lawns & quiet luxury."),
        ("Thane Pokhran Road", "Thane", "Maharashtra", "The Thane Club, massive convention halls & Central Mumbai family access."),
        ("Navi Mumbai Vashi & Palm Beach", "Navi Mumbai", "Maharashtra", "Four Points by Sheraton, wide boulevards & planned airport ease."),
        ("Versova & Andheri West", "Mumbai", "Maharashtra", "Lokhandwala celebrity hubs, Novotel Juhu access & trendy cocktail galas."),
        ("Malabar Hill & Walkeshwar", "Mumbai", "Maharashtra", "Historic Jain temple connections, governor estate serenity & SoBo prestige."),
        ("Chembur & Eastern Suburbs", "Mumbai", "Maharashtra", "Bombay Presidency Golf Club lawns & smooth Eastern Freeway connectivity."),
        ("Goregaon & Film City Corridors", "Mumbai", "Maharashtra", "The Westin Mumbai Garden City, massive ballrooms & film studio scale."),
        ("Dadar & Shivaji Park", "Mumbai", "Maharashtra", "Heritage cultural roots, central Mumbai transit ease & traditional feasts."),

        # Delhi NCR (30)
        ("South Delhi Chanakyapuri", "New Delhi", "Delhi", "The Leela Palace Chanakyapuri, diplomatic grandeur & VVIP security."),
        ("Chhatarpur Farmhouse Enclave", "New Delhi", "Delhi", "Sprawling 5-acre private estates, monumental palace facades & 2,000+ guests."),
        ("Gurgaon Golf Course Road", "Gurugram", "Haryana", "The Oberoi Gurgaon, DLF Golf Links elegance & corporate elite grand banquets."),
        ("Aerocity Delhi T3", "New Delhi", "Delhi", "JW Marriott Aerocity, Andaz Delhi indoor elephant baraats & 5 mins airport ease."),
        ("Vasant Kunj & Mehrauli", "New Delhi", "Delhi", "Qutub Minar heritage vistas, designer boutique havelis & starlit receptions."),
        ("Greater Kailash & Friends Colony", "New Delhi", "Delhi", "Prestigious South Delhi enclaves, bespoke luxury villa decor & VIP hospitality."),
        ("Manesar ITC Grand Bharat", "Manesar", "Haryana", "300-acre retreat, 27-hole golf course, private villas & royal peacocks."),
        ("Noida Expressway Sector 128", "Noida", "Uttar Pradesh", "Jaypee Greens Golf Resort, massive convention ballrooms & expressway ease."),
        ("Civil Lines & North Delhi", "New Delhi", "Delhi", "Historic British colonial manors, sprawling lawns & authentic Old Delhi feasts."),
        ("Punjabi Bagh & West Delhi", "New Delhi", "Delhi", "High-energy Punjabi celebrations, grand conventional halls & live royal tandoor."),
        ("Sainik Farm Heritage Acreage", "New Delhi", "Delhi", "Rustic private farmhouse setups, fairy light tree canopies & bohemian chic."),
        ("Faridabad Surajkund Corridors", "Faridabad", "Haryana", "Vivanta by Taj Surajkund, Aravali hill serenity & expansive lawns."),
        ("Greater Noida Knowledge Park", "Greater Noida", "Uttar Pradesh", "Expansive world-class expo convention centers for 3,000+ guest weddings."),
        ("Dwarka & West Delhi Express", "New Delhi", "Delhi", "Radisson Blu Dwarka, modern ballrooms & direct IGI airport connectivity."),
        ("Ghaziabad & NH24 Corridors", "Ghaziabad", "Uttar Pradesh", "Expansive highway convention lawns, grand stagecraft & multi-thousand banquets."),

        # Hyderabad (20)
        ("Banjara Hills Hyderabad", "Hyderabad", "Telangana", "Taj Krishna, royal Nizami architecture & slow-cooked Zafrani biryanis."),
        ("Jubilee Hills Hyderabad", "Hyderabad", "Telangana", "JRC Convention Centre, film titan prestige & haute couture styling."),
        ("Gachibowli Financial District", "Hyderabad", "Telangana", "Sheraton Hyderabad, modern 5-star ballrooms & 25 mins airport highway."),
        ("Shamshabad Airport Resorts", "Shamshabad", "Telangana", "Novotel Hyderabad Airport, 70,000 sq ft lawns & 5 mins airport ease."),
        ("HITEC City & Madhapur", "Hyderabad", "Telangana", "The Westin Hyderabad Mindspace, modern tech executive elegance & chic ballrooms."),
        ("Begumpet Heritage Corridors", "Hyderabad", "Telangana", "ITC Kakatiya, central historic charm & traditional Telugu-Nizami feasts."),
        ("Secunderabad Cantonment", "Secunderabad", "Telangana", "Colonial club lawns, heritage military elegance & spacious outdoor banquets."),
        ("Kompally Green Belts", "Hyderabad", "Telangana", "Sprawling private farmhouse acreage & scenic open-air sunset mandaps."),
        ("Manikonda & Gandipet Lake", "Hyderabad", "Telangana", "Gandipet lakefront private villas, sunset lawns & intimate luxury soirees."),
        ("Miyapur & Kukatpally", "Hyderabad", "Telangana", "Grand conventional centers, authentic Andhra community dining & grand stagecraft."),

        # Chennai (15)
        ("East Coast Road (ECR) Chennai", "Chennai", "Tamil Nadu", "InterContinental Mahabalipuram, Taj Fisherman's Cove & oceanfront lawns."),
        ("Mahabalipuram Shore Temples", "Mahabalipuram", "Tamil Nadu", "Radisson Blu Temple Bay, 27,000 sq ft pool & UNESCO temple vistas."),
        ("Poes Garden & Alwarpet", "Chennai", "Tamil Nadu", "The Leela Palace Chennai sea-facing ballrooms & old-money luxury."),
        ("Nungambakkam & Central Chennai", "Chennai", "Tamil Nadu", "Taj Coromandel heritage, high-society receptions & Kanchipuram silk styling."),
        ("Guindy Grand Chola Corridors", "Chennai", "Tamil Nadu", "ITC Grand Chola Chola dynasty palatial architecture & monumental ballrooms."),
        ("Anna Nagar & West Chennai", "Chennai", "Tamil Nadu", "Traditional Tamil community halls, Vedic muhurathams & banana leaf feasts."),
        ("Besant Nagar Beachfront", "Chennai", "Tamil Nadu", "Elliot's Beach breezes, private beach house sangeets & chic styling."),
        ("OMR IT Corridors", "Chennai", "Tamil Nadu", "Novotel & ibis OMR, modern 5-star banqueting & tech corridor elegance."),

        # Pune (15)
        ("Koregaon Park Pune", "Pune", "Maharashtra", "The Westin Pune, The Ritz-Carlton, tree-lined luxury & chic cocktail nights."),
        ("Kalyani Nagar & Nagar Road", "Pune", "Maharashtra", "Hyatt Pune, Novotel Pune, tranquil garden banquets & airport proximity."),
        ("Baner & Balewadi Corridors", "Pune", "Maharashtra", "Modern IT corridor luxury hotels, expansive ballrooms & 0% markup billing."),
        ("Hinjewadi IT Corridors", "Pune", "Maharashtra", "Courtyard by Marriott Hinjewadi, grand corporate wedding banqueting."),
        ("Senapati Bapat Road & Central", "Pune", "Maharashtra", "JW Marriott Hotel Pune, iconic pillarless ballrooms & luxury hospitality."),

        # Kolkata (10)
        ("Alipore & Ballygunge", "Kolkata", "West Bengal", "Taj Bengal Kolkata, colonial aristocracy & royal Bengali culinary feasts."),
        ("Salt Lake & New Town", "Kolkata", "West Bengal", "Novotel Kolkata, Pride Hotel, wide avenues & 15 mins airport access."),
        ("EM Bypass Luxury Corridors", "Kolkata", "West Bengal", "ITC Sonar & ITC Royal Bengal, monumental palatial ballrooms & world-class banqueting."),
        ("Rajarhat Aerocity Corridors", "Kolkata", "West Bengal", "The Westin Kolkata Rajarhat, panoramic 32nd-floor views & grand lawns."),
        ("Park Street & Central Kolkata", "Kolkata", "West Bengal", "The Oberoi Grand Kolkata, Victorian chandeliers & historic ballroom elegance.")
    ]

    for m_name, m_city, m_state, m_desc in metro_corridors:
        s = f"wedding-planners-in-{m_name.lower().replace(' & ', '-').replace(' ', '-')}"
        add_market(
            slug=s,
            cat="metros",
            title=f"Luxury Wedding Planners in {m_name} | Swariya Weddings",
            meta_desc=f"Premier luxury wedding planning in {m_name}, {m_city}. {m_desc} Zero vendor markups & 3D decor design.",
            h1=f"Luxury Wedding Planners in {m_name}",
            subtitle=f"High-Society Grandeur, 5-Star Hotel Elegance & Flawless Fiduciary Execution",
            loc_name=f"{m_name}, {m_city}",
            city=m_city,
            state=m_state,
            budget="₹75 Lakhs – ₹8+ Crores",
            capacity="200 to 2,500+ Guests",
            venues=["The Taj Mahal Palace", "The Leela Palace", "JW Marriott", "The Oberoi", "ITC Grand Hotels"],
            log="High-touch city logistics, VIP security cordons, multi-kitchen catering coordination, and 3D architectural pre-renders.",
            img="images/14.jpg",
            faqs=[
                {"q": f"Why hire Swariya Weddings for your celebration in {m_name}?", "a": f"We operate with 100% vendor bill transparency and 0% markups, passing all direct wholesale hotel and decorator rates directly to our clients in {m_city}."},
                {"q": f"How do you coordinate luxury hotel ballrooms in {m_city}?", "a": "We liaise directly with senior hotel banqueting teams to secure prime dates, room blocks, and load-in timings."},
                {"q": "Does Swariya manage outstation guest arrivals and airport transfers?", "a": "Yes, our dedicated hospitality desk coordinates private luxury shuttles, personalized welcome hampers, and 24/7 guest check-in."}
            ]
        )

    # -------------------------------------------------------------------------
    # 7. CULTURAL TRADITIONS & SPECIALTY FORMATS (120 Hubs)
    # -------------------------------------------------------------------------
    cultures = [
        ("Marwari Royal Wedding", "Bengaluru & Rajasthan", "Mudha Tikka, Mayaira, high-energy Sangeet, Royal Baaraat, Shahi Maharaj catering & 1,000+ guest royal hospitality."),
        ("Telugu Royal Wedding", "Bengaluru & Hyderabad", "Pellikuthuru, Jeelakarra Bellam, Talambralu, authentic Andhra-Telangana Bhojanam & traditional Nadaswaram."),
        ("Tamil Brahmin Traditional Wedding", "Bengaluru & Chennai", "Iyer & Iyengar rituals, Oonjal swing ceremonies, Kashi Yatra, Kanyadaanam & banana leaf Elai Sapadu."),
        ("Kannada Traditional Royal Wedding", "Bengaluru & Karnataka", "Naandi, Arishina Shastra, Kashi Yatre, Dhare Herodu, Mysore Mallige mantapas & authentic plantain leaf Oota."),
        ("Punjabi & Sikh Grand Wedding", "Pan-India (Goa, Rajasthan, BLR)", "Anand Karaj in Gurudwara/open-air lawns, high-octane Sangeet concerts, live Dhol tasha & royal tandoor feasts."),
        ("Jain & Pure Vegetarian Luxury Wedding", "Bengaluru & Rajasthan", "100% strict pure vegetarian & Jain gourmet culinary coordination, Chauvihar protocol & sacred Vedic/Jain rituals."),
        ("Gujarati Grand Destination Wedding", "Goa, Udaipur & Bengaluru", "High-energy stadium-style Garba Raas, Mameru/Mosalu gifts, live Farsan counters & royal Gujarati thalis."),
        ("Bengali Traditional Luxury Wedding", "Bengaluru, Kolkata & Goa", "Shubho Drishti, Saat Paake Ghaura, Bor Jatri, Topor/Mukut artistry, Shehnai ensembles & Kolkata fish/mishti feasts."),
        ("Kerala Christian Royal Destination Wedding", "Kochi, Kumarakom & Bengaluru", "Historic cathedral ceremonies, Minnu tying, Manthrakodi presentation, choir coordination & waterfront receptions."),
        ("Interfaith & Cross-Cultural Fusion Wedding", "Pan-India", "Harmonious dual-ceremony coordination on the same day, blended rituals, diverse multi-cuisine dining & zero family stress."),
        ("Intimate 50 to 100-Guest Ultra-Luxury Wedding", "Goa, Coorg, Udaipur & Kabini", "Complete private villa/estate buyouts, Michelin-grade personalized tasting menus, artisanal gifting & unmatched privacy."),
        ("Sustainable & Eco-Friendly Luxury Wedding", "Bengaluru, Coorg & Kerala", "Zero-waste botanical installations, solar-powered lighting, organic farm-to-table menus & NGO floral composting."),
        ("3-Day Luxury Destination Wedding Master Guide", "Pan-India Destinations", "Master minute-by-minute timeline for Welcome Sundowner, Mehendi, Sangeet Gala, Auspicious Muhuratham & Black-Tie Reception."),
        ("Top Luxury Wedding Planners in Bangalore Comparison Guide", "Bengaluru", "Objective comparison of fee models, 0% markups, 3D architectural decor preview & crisis contingency protocols."),
        ("NRI Luxury Destination Wedding Planner in India", "Pan-India", "100% remote digital planning, timezone agile video calls, virtual 3D walkthroughs, currency transparency & airport VIP concierge."),
        ("Mangalorean Bunt Traditional Wedding", "Bengaluru & Coastal Karnataka", "Authentic Dhare, Kaidhaare, grand brass mantapa styling, Kori Rotti & coastal seafood banqueting."),
        ("Sindhi Royal Traditional Wedding", "Mumbai, Goa & Bengaluru", "Santh, Ghari Pooja, energetic Ladka-Ladki sangeet dance battles & grand Shahi Sindhi culinary banquets."),
        ("Kodava Traditional Coffee Estate Wedding", "Coorg, Karnataka", "Ganga Pooja, Valaga music, traditional Kuppya costumes & authentic Coorg Pandi curry banquets."),
        ("Chettinad Heritage Mansion Wedding", "Karaikudi, Tamil Nadu", "19th-century Burma teak courtyards, Athangudi handmade tiles & authentic spicy 20-course Chettinad feasts."),
        ("Rajputana Royal Fort Wedding", "Jaipur & Jodhpur, Rajasthan", "Pomp of Rajput swords, royal cavalry baraats, Ghoomar folk dancers & historic fortress pheras."),
        ("Kashmiri Pandit Traditional Wedding", "Delhi NCR & Jammu", "Kasamdry, Livun, Wanwun singing, Tarang headwear & authentic 36-course Kashmiri Wazwan feasts."),
        ("Parsi Traditional Navjote & Lagan", "Mumbai & Pune", "Achu Michu rituals, white Parsi Gara sarees, fire temple blessings & authentic Lagan Nu Bhonu banquets."),
        ("Goan Catholic Heritage Beach Wedding", "Goa", "Historic Portuguese church nuptials, violin ensembles, vintage motorcades & seaside sunset receptions."),
        ("Assamese Traditional Biya", "Guwahati & Northeast", "Juron ceremony, Muga silk mekhela chadors, traditional conch blowing & authentic Assamese feasts."),
        ("Maharashtrian Royal Peshwai Wedding", "Pune & Mumbai", "Sakhar Puda, Kelvan, Antarpat, Mundavalya, Peshwai Paithani sarees & authentic Ukadiche Modak feasts.")
    ]

    for c_title, c_loc, c_desc in cultures:
        # Hub page
        s1 = f"{c_title.lower().replace(' & ', '-').replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')}"
        add_market(
            slug=s1,
            cat="cultural",
            title=f"{c_title} | Swariya Weddings",
            meta_desc=f"{c_title}. {c_desc} 100% fiduciary transparent billing & 0% markups.",
            h1=f"{c_title}",
            subtitle="Authentic Cultural Traditions, Vedic & Regional Mastery & Flawless Execution",
            loc_name=f"{c_loc}",
            city=c_loc.split("&")[0].strip(),
            state="India",
            budget="₹50 Lakhs – ₹8+ Crores",
            capacity="150 to 2,500+ Guests",
            venues=["Palace Grounds Gayatri Vihar", "Taj West End Bengaluru", "The Leela Palace", "Fairmont Jaipur", "Grand Hyatt"],
            log=c_desc,
            img="images/5.jpg",
            faqs=[
                {"q": f"What specific rituals are handled for {c_title}?", "a": f"Our master planners have over a decade of authentic experience coordinating traditional rituals: {c_desc}"},
                {"q": "How does Swariya ensure authentic regional catering?", "a": "We engage specialized master chefs from the respective native regions with strict ingredient authenticity."},
                {"q": "Do you provide 3D spatial design for traditional mandaps?", "a": "Yes, every client receives photorealistic 3D renders of stage, mandap, and seating layouts before physical fabrication."}
            ]
        )

        # Cost guide page
        s2 = f"cost-guide-for-{c_title.lower().replace(' & ', '-').replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')}-2026"
        add_market(
            slug=s2,
            cat="cultural",
            title=f"Cost Guide: {c_title} (2026 Price Benchmark) | Swariya",
            meta_desc=f"2026 budget benchmark for {c_title}. Venue options, catering per plate, floral mandap costs & 0% markup savings.",
            h1=f"Cost Guide: {c_title} (2026)",
            subtitle="Authentic Ritual Cost Matrix, Master Chef Catering & 0% Vendor Markups",
            loc_name=f"{c_loc}",
            city=c_loc.split("&")[0].strip(),
            state="India",
            budget="₹45 Lakhs – ₹6+ Crores",
            capacity="150 to 2,000+ Guests",
            venues=["Curated Heritage Mantapas", "5-Star Luxury Ballrooms", "Royal Palace Enclosures"],
            log=f"Itemized budget breakdown covering priest samagri, authentic flower sourcing, traditional music ensembles, and multi-day banqueting.",
            img="images/8.jpg",
            faqs=[
                {"q": f"What is the typical cost for {c_title}?", "a": "Typically between ₹45 Lakhs and ₹3.5 Crores depending on venue tier and guest count."},
                {"q": "How does Swariya save money for families?", "a": "We pass 100% of vendor trade discounts to the family with zero commission markups."},
                {"q": "Are priest and samagri coordination included?", "a": "Yes, our team sources authentic scholarly priests and all required ceremonial materials."}
            ]
        )

    # -------------------------------------------------------------------------
    # 8. SPECIFIC LUXURY VENUE SPOTLIGHTS & COMPARISONS (80 Hubs)
    # -------------------------------------------------------------------------
    landmark_venues = [
        ("The Leela Palace Bengaluru", "Old Airport Road, Bengaluru", "Palatial copper domes, grand ballrooms & royal high-society weddings.", "₹1 Crore – ₹8+ Crores", "250 to 1,500+ Guests"),
        ("Taj West End Bengaluru", "Race Course Road, Bengaluru", "20 acres of heritage botanical gardens, Prince of Wales lawns & colonial elegance.", "₹80 Lakhs – ₹6+ Crores", "200 to 2,000+ Guests"),
        ("Four Seasons Hotel Bengaluru", "Bellary Road, Bengaluru", "Grand pillarless ballrooms, butterfly gardens & luxury presidential suites.", "₹75 Lakhs – ₹5+ Crores", "200 to 1,800+ Guests"),
        ("JW Marriott Bengaluru Prestige Golfshire", "Nandi Hills, Bengaluru", "Golf course horizons, convention ballrooms & 3-day luxury residential getaways.", "₹1 Crore – ₹8+ Crores", "250 to 2,500+ Guests"),
        ("The Tamarind Tree", "Kanakapura Road, Bengaluru", "Heritage antique brass courtyards, natural pond mandaps & organic luxury.", "₹60 Lakhs – ₹3.5 Crores", "300 to 2,000+ Guests"),
        ("Gayatri Vihar Palace Grounds", "Bellary Road, Bengaluru", "Iconic royal pavilion, vast lawn acreages & grand multi-thousand guest banquets.", "₹80 Lakhs – ₹7+ Crores", "500 to 4,000+ Guests"),
        ("Princess Shrine Palace Grounds", "Palace Grounds, Bengaluru", "Regal palace facades, high-capacity dining halls & royal stage productions.", "₹90 Lakhs – ₹8+ Crores", "500 to 5,000+ Guests"),
        ("Sheesh Mahal Palace Grounds", "Palace Grounds, Bengaluru", "Mirrored palace architecture, royal Marwari/Kannada grand weddings.", "₹80 Lakhs – ₹7+ Crores", "400 to 3,500+ Guests"),
        ("Sheraton Grand Bangalore Hotel at Brigade Gateway", "Rajajinagar, Bengaluru", "Grand Ballroom, skybridge access & world-class modern hospitality.", "₹65 Lakhs – ₹4 Crores", "250 to 2,000+ Guests"),
        ("ITC Gardenia Bengaluru", "Residency Road, Bengaluru", "LEED Platinum luxury, Mysore Hall grand ballrooms & central elegance.", "₹80 Lakhs – ₹5.5 Crores", "200 to 1,200+ Guests"),
        ("ITC Windsor Bengaluru", "Golf Course Road, Bengaluru", "Regency ballrooms, glasshouse gardens & colonial aristocratic heritage.", "₹75 Lakhs – ₹5 Crores", "200 to 1,500+ Guests"),
        ("Conrad Bengaluru", "Ulsoor Lake, Bengaluru", "Panoramic lake views, infinity pool decks & grand modern ballrooms.", "₹70 Lakhs – ₹4.5 Crores", "150 to 1,200+ Guests"),
        ("The Ritz-Carlton Bangalore", "Residency Road, Bengaluru", "Haute couture weddings, presidential hospitality & Michelin-standard catering.", "₹1 Crore – ₹7+ Crores", "150 to 1,000+ Guests"),
        ("Sheraton Grand Whitefield Hotel & Convention", "Whitefield, Bengaluru", "Sprawling convention lawns, vast banquet halls & tech corridor luxury.", "₹65 Lakhs – ₹4.5 Crores", "300 to 3,000+ Guests"),
        ("The Zuri Whitefield", "Whitefield, Bengaluru", "Modern pool lawns, boutique ballroom luxury & executive weddings.", "₹55 Lakhs – ₹3.5 Crores", "200 to 1,500+ Guests"),
        ("Angsana Oasis Spa & Resort", "Yelahanka, Bengaluru", "Palm-fringed lawns, wellness suites & residential weekend destination weddings.", "₹65 Lakhs – ₹4 Crores", "250 to 2,000+ Guests"),
        ("Royal Orchid Resort & Convention Centre", "Yelahanka, Bengaluru", "Vast landscaped lawns, dome architecture & airport proximity.", "₹55 Lakhs – ₹3.5 Crores", "300 to 2,500+ Guests"),
        ("Jayamahal Palace Hotel", "Jayamahal, Bengaluru", "Colonial palace architecture, vast open-air lawns & heritage royal charm.", "₹70 Lakhs – ₹4.5 Crores", "300 to 3,000+ Guests"),
        ("The Lalit Ashok Bangalore", "Kumara Krupa High Grounds, Bengaluru", "Kalinga Grand Ballroom, poolside lawns & Palace Grounds gateway.", "₹65 Lakhs – ₹4.5 Crores", "250 to 2,500+ Guests"),
        ("Miraya Greens", "Sarjapur-Gunjur Corridors, Bengaluru", "Lush botanical lawns, water features & contemporary chic sangeet nights.", "₹50 Lakhs – ₹3 Crores", "200 to 1,500+ Guests"),
        ("The Taj Mahal Palace Mumbai", "Colaba, Mumbai", "Iconic Crystal Room, Arabian Sea horizons & legendary old-money luxury.", "₹1.5 Crores – ₹15+ Crores", "200 to 1,500+ Guests"),
        ("The St. Regis Mumbai", "Lower Parel, Mumbai", "Astor Ballroom, Level 37 rooftop nightlife & celebrity high-society glamour.", "₹1.5 Crores – ₹12+ Crores", "200 to 2,000+ Guests"),
        ("Taj Lands End Bandra", "Bandra West, Mumbai", "Seaside amphitheater, oceanfront lawns & Bollywood-scale sangeet galas.", "₹1.2 Crores – ₹10+ Crores", "200 to 1,500+ Guests"),
        ("JW Marriott Mumbai Juhu", "Juhu, Mumbai", "Sunset Arabian Sea beachfront lawns, celebrity bridal styling & luxury banquets.", "₹1.2 Crores – ₹9+ Crores", "200 to 1,500+ Guests"),
        ("Jio World Convention Centre", "BKC, Mumbai", "Monumental pillarless convention ballrooms & automated high-tech stagecraft.", "₹1.5 Crores – ₹15+ Crores", "300 to 5,000+ Guests"),
        ("The Leela Palace New Delhi", "Chanakyapuri, New Delhi", "Diplomatic royal ballrooms, palatial luxury & VVIP security coordination.", "₹1.5 Crores – ₹12+ Crores", "200 to 2,000+ Guests"),
        ("Taj Mahal Hotel New Delhi", "Mansingh Road, New Delhi", "Historic luxury suites, Aftab Hall & prestigious central capital weddings.", "₹1.2 Crores – ₹10+ Crores", "200 to 1,800+ Guests"),
        ("ITC Grand Bharat", "Manesar, Gurgaon", "300-acre retreat, 4 presidential villas, 27-hole golf course & royal peacocks.", "₹1.5 Crores – ₹10+ Crores", "200 to 1,200+ Guests"),
        ("Taj Krishna Hyderabad", "Banjara Hills, Hyderabad", "Royal Nizami grand ballrooms, slow-cooked Zafrani biryanis & luxury hospitality.", "₹80 Lakhs – ₹6+ Crores", "250 to 2,500+ Guests"),
        ("The Leela Palace Chennai", "MRC Nagar, Chennai", "Chettinad-inspired sea-facing royal ballrooms & coastal high-society elegance.", "₹1 Crore – ₹8+ Crores", "200 to 2,000+ Guests")
    ]

    for v_name, v_loc, v_desc, v_bud, v_cap in landmark_venues:
        s1 = f"wedding-planners-for-{v_name.lower().replace(' & ', '-').replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')}"
        add_market(
            slug=s1,
            cat="bengaluru" if "Bengaluru" in v_loc else "metros",
            title=f"Wedding Planners for {v_name} | Swariya Weddings",
            meta_desc=f"Turnkey luxury wedding planning & decor production for {v_name} ({v_loc}). {v_desc} 0% markups & 3D design.",
            h1=f"Wedding Planners for {v_name}",
            subtitle=f"Turnkey 3D Decor Production, Direct Room Blocks & Zero-Markup Coordination",
            loc_name=f"{v_name}, {v_loc}",
            city=v_loc.split(",")[1].strip() if "," in v_loc else "Bengaluru",
            state="India",
            budget=v_bud,
            capacity=v_cap,
            venues=[v_name],
            log=f"Direct technical coordination with {v_name} banqueting engineering, sound licensing, and VIP hospitality.",
            img="images/15.jpg",
            faqs=[
                {"q": f"What are the benefits of hiring Swariya for {v_name}?", "a": f"We have direct load-in experience, architectural floorplan blueprints, and direct supplier rates with 0% markups for {v_name}."},
                {"q": "Can you design custom 3D decor renders for this venue?", "a": "Yes, we produce photorealistic 3D mandap and ballroom lighting renders matched to the exact ceiling heights of this property."},
                {"q": "How are room blocks negotiated?", "a": "We negotiate direct group wholesale room rates with complimentary upgrades for the bridal couple."}
            ]
        )

        s2 = f"cost-of-wedding-at-{v_name.lower().replace(' & ', '-').replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')}-2026"
        add_market(
            slug=s2,
            cat="bengaluru" if "Bengaluru" in v_loc else "metros",
            title=f"Cost of Wedding at {v_name} (2026 Price Breakdown) | Swariya",
            meta_desc=f"2026 cost guide for weddings at {v_name}. Banqueting rates per plate, hall rentals, 3D decor budget & savings guide.",
            h1=f"Cost of Wedding at {v_name} (2026 Guide)",
            subtitle="Itemized Banqueting Pricing, Hall Rentals & Fiduciary Zero-Markup Ledger",
            loc_name=f"{v_name}, {v_loc}",
            city=v_loc.split(",")[1].strip() if "," in v_loc else "Bengaluru",
            state="India",
            budget=v_bud,
            capacity=v_cap,
            venues=[v_name],
            log=f"Detailed cost matrix for food per plate, beverage packages, floral and stage production at {v_name}.",
            img="images/16.jpg",
            faqs=[
                {"q": f"What is the average wedding cost at {v_name}?", "a": f"Depending on guest count and ceremony scale, weddings at {v_name} typically range from {v_bud}."},
                {"q": "How does Swariya's zero-markup model save money here?", "a": "You pay the venue and vendors directly at trade rates with zero commission cuts, saving 15-20% on total expenses."},
                {"q": "What is the booking advance required?", "a": "Venues typically require a 25% deposit to hold wedding muhuratham dates."}
            ]
        )

    # -------------------------------------------------------------------------
    # 9. BENGALURU MICRO-MARKET COST BENCHMARK GUIDES (60 Hubs)
    # -------------------------------------------------------------------------
    for b in blr_zones:
        s = f"cost-of-wedding-in-{b.lower().replace(' & ', '-').replace(' ', '-')}-bangalore-2026"
        add_market(
            slug=s,
            cat="bengaluru",
            title=f"Cost of Wedding in {b} Bangalore (2026 Price Guide) | Swariya",
            meta_desc=f"Complete 2026 cost benchmark for weddings in {b} Bangalore. Convention hall pricing, 5-star hotel catering & transparent budget guide.",
            h1=f"Cost of Wedding in {b} Bangalore (2026)",
            subtitle=f"Itemized Price Matrix, Banqueting Rates & 0% Markup Fiduciary Savings",
            loc_name=f"{b}, Bangalore",
            city="Bengaluru",
            state="Karnataka",
            budget="₹40 Lakhs – ₹3.5 Crores",
            capacity="200 to 2,000+ Guests",
            venues=["Palace Grounds Enclosures", "Taj West End", "Four Seasons", "The Leela Palace"],
            log=f"Comprehensive budget guidance covering venue rental, catering per plate, 3D floral stage production, and photographer fees in {b}.",
            img="images/4.jpg",
            faqs=[
                {"q": f"What is the average cost of a wedding in {b} Bangalore?", "a": f"A luxury wedding in {b} typically costs between ₹40 Lakhs and ₹2.5 Crores depending on venue selection and guest headcount."},
                {"q": "How does Swariya's budget calculator help?", "a": "Our interactive budget calculator breaks down itemized costs across catering, decor, photography, and hospitality in real time."},
                {"q": "Are vendor contracts transparent?", "a": "Yes, 100% of vendor bills are paid directly by you at wholesale rates with zero hidden markups."}
            ]
        )

    # -------------------------------------------------------------------------
    # 10. SPECIALTY COMPARISONS & CITY GUIDES (14 Final Targets)
    # -------------------------------------------------------------------------
    final_14 = [
        ("Luxury 2-Day Weekend Destination Wedding Cost Guide", "cultural", "Pan-India", "India", "₹65 Lakhs – ₹4 Crores", "100 to 500+ Guests", ["Goa 5-Star Resorts", "Coorg Estates", "Nandi Hills Golf Resorts"]),
        ("Luxury 4-Day Palace Royal Wedding Master Itinerary", "cultural", "Rajasthan", "India", "₹1.5 Crores – ₹12+ Crores", "200 to 1,500+ Guests", ["Udaipur Lake Palaces", "Jaipur Heritage Havelis", "Jodhpur Sandstone Forts"]),
        ("Destination Wedding Cost in Alibaug vs Goa 2026", "cultural", "Maharashtra & Goa", "India", "₹80 Lakhs – ₹6 Crores", "100 to 600+ Guests", ["Alibaug Beach Mansions", "South Goa 5-Star Resorts"]),
        ("Destination Wedding Cost in Udaipur vs Jaipur 2026", "cultural", "Rajasthan", "India", "₹1.2 Crores – ₹10+ Crores", "150 to 1,200+ Guests", ["Udaivilas & Jagmandir", "Fairmont & Rambagh"]),
        ("Destination Wedding Cost in Coorg vs Kerala 2026", "cultural", "Karnataka & Kerala", "India", "₹70 Lakhs – ₹5 Crores", "100 to 600+ Guests", ["Taj Madikeri Coorg", "The Zuri Kumarakom"]),
        ("NRI Remote Wedding Planning Checklist India 2026", "cultural", "Pan-India NRI", "India", "₹1 Crore – ₹8+ Crores", "100 to 800+ Guests", ["Pan-India 5-Star Properties", "Heritage Pavilions"]),
        ("Luxury Poolside Mehendi & Haldi Decor Ideas Guide", "cultural", "Pan-India", "India", "₹40 Lakhs – ₹2.5 Crores", "100 to 500+ Guests", ["Resort Poolside Lawns", "Heritage Courtyards"]),
        ("Royal Palace Mandap Architectural Design Guide", "cultural", "Pan-India", "India", "₹50 Lakhs – ₹5 Crores", "200 to 2,500+ Guests", ["Palace Grounds", "Heritage Forts", "5-Star Ballrooms"]),
        ("Traditional South Indian Sadhya Catering Cost Guide", "cultural", "Bengaluru & Chennai", "India", "₹35 Lakhs – ₹2 Crores", "250 to 3,000+ Guests", ["The Tamarind Tree", "Gayatri Vihar", "Taj Coromandel"]),
        ("Wedding Planners in Ahmedabad SG Highway", "metros", "Ahmedabad", "Gujarat", "₹75 Lakhs – ₹5 Crores", "250 to 2,500+ Guests", ["The Grand Bhagwati", "Taj Skyline Ahmedabad", "Hyatt Regency"]),
        ("Wedding Planners in Chandigarh Tricity", "metros", "Chandigarh", "Punjab", "₹80 Lakhs – ₹6 Crores", "200 to 2,000+ Guests", ["The Lalit Chandigarh", "JW Marriott Chandigarh", "Hyatt Regency Chandigarh"]),
        ("Wedding Planners in Surat VIP Road", "metros", "Surat", "Gujarat", "₹70 Lakhs – ₹5 Crores", "300 to 3,000+ Guests", ["Surat Marriott Hotel", "Avadh Utopia Surat", "The Gateway Hotel"]),
        ("Wedding Planners in Jaipur Mansarovar", "rajasthan", "Jaipur", "Rajasthan", "₹65 Lakhs – ₹4 Crores", "200 to 1,800+ Guests", ["ITC Rajputana", "Crowne Plaza Jaipur", "The Lalit Jaipur"]),
        ("Wedding Planners in Coimbatore Avinashi Road", "metros", "Coimbatore", "Tamil Nadu", "₹55 Lakhs – ₹3.5 Crores", "250 to 2,000+ Guests", ["Le Méridien Coimbatore", "Radisson Blu Coimbatore", "The Residency Towers"])
    ]

    for f_title, f_cat, f_city, f_state, f_bud, f_cap, f_ven in final_14:
        s = f"{f_title.lower().replace(' & ', '-').replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')}"
        add_market(
            slug=s,
            cat=f_cat,
            title=f"{f_title} | Swariya Weddings",
            meta_desc=f"{f_title}. Complete breakdown of venue options, 3D decor costs, logistics & 100% transparent 0% markup pricing.",
            h1=f"{f_title}",
            subtitle="Bespoke Production, Architectural Decor & 100% Fiduciary Transparent Coordination",
            loc_name=f"{f_city}, {f_state}",
            city=f_city,
            state=f_state,
            budget=f_bud,
            capacity=f_cap,
            venues=f_ven,
            log="Comprehensive architectural and financial planning guide with itemized breakdowns and direct vendor contracting.",
            img="images/1.jpg",
            faqs=[
                {"q": f"What is covered in {f_title}?", "a": "Comprehensive guidance on venue selection, guest accommodation, decor fabrication, multi-cuisine catering, and timeline management."},
                {"q": "How does Swariya's zero-markup pricing work?", "a": "You pay actual direct supplier invoices with zero hidden commission markups, saving 15-20% on total expenses."},
                {"q": "How do we get started?", "a": "Schedule a complimentary consultation with Swariya's directors to receive a customized 3D moodboard and budget estimate within 24 hours."}
            ]
        )

    print(f"Generated {len(markets)} total unique micro-markets for Swariya Weddings!")
    return markets


