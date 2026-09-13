import os
import json

DESTINATION_VENUES = [
    # ----------------------------------------------------
    # 1. GOA LUXURY VENUES
    # ----------------------------------------------------
    {
        "slug": "taj-exotica-resort-goa-wedding",
        "name": "Taj Exotica Resort & Spa Goa",
        "city": "Benaulim, South Goa",
        "state": "Goa",
        "tagline": "56 acres of Mediterranean-inspired coastal luxury on the pristine white sands of Benaulim, featuring expansive ocean-facing lawns and grand ballrooms.",
        "capacity": "150 – 800 Guests",
        "rooms": "140 Luxury Rooms, Suites & Plunge Pool Villas",
        "spaces": "Sala Grande Ballroom (450 pax), Ocean Lawns (800 pax), Beach Frontage (300 pax)",
        "pricing": "₹25,00,000 – ₹65,00,000 / day event buyout",
        "catering": "Taj culinary team specializing in Goan seafood, coastal specialties, and international banquets",
        "decor": "Open decor policy for empaneled luxury planners like Swariya Weddings",
        "lead_time": "9 – 14 months for winter dates",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What is the maximum guest capacity for weddings at Taj Exotica Goa?", "Taj Exotica comfortably hosts celebrations from 150 residential guests up to 800 guests across its sprawling sea-facing lawns and grand pillarless ballroom."),
            ("Can we host a beach mandap ceremony at Taj Exotica?", "Yes, the property features a direct private beach lawn providing unobstructed sunset views of the Arabian Sea."),
            ("How does Swariya Weddings coordinate weddings at Taj Exotica?", "Swariya handles luxury room-block negotiation, CRZ and sound permits, 3D architectural floral mandap design, airport transfers from Dabolim/Mopa, and zero markup vendor management.")
        ]
    },
    {
        "slug": "itc-grand-goa-resort-wedding",
        "name": "ITC Grand Goa Resort & Spa",
        "city": "Arossim Beach, South Goa",
        "state": "Goa",
        "tagline": "Sprawling 45-acre village-style Indo-Portuguese resort with shimmering lagoons, private coconut groves, and direct Arossim beach access.",
        "capacity": "150 – 650 Guests",
        "rooms": "252 Luxury Rooms & Suites with outdoor rain showers",
        "spaces": "Arossim Beach Lawn (600 pax), Salcete Ballroom (350 pax), Seaside Lawns (400 pax)",
        "pricing": "₹22,00,000 – ₹55,00,000 / day event buyout",
        "catering": "ITC master chefs famous for Bukhara and Dum Pukht royal banqueting and coastal Goan feasts",
        "decor": "Flexible outdoor decor protocols with complete weatherproofing",
        "lead_time": "8 – 12 months in advance",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("Why is ITC Grand Goa popular for luxury weddings?", "Its unique village-style architecture connected by serene waterways and bridge walkways creates an enchanting backdrop for multi-day celebrations."),
            ("How close is ITC Grand Goa to the airport?", "It is just a 20-minute drive from Dabolim International Airport (GOI), making guest arrivals effortless.")
        ]
    },
    {
        "slug": "the-leela-goa-wedding",
        "name": "The Leela Goa",
        "city": "Cavelossim, South Goa",
        "state": "Goa",
        "tagline": "75 acres of royal Vijayanagara and Portuguese palace architecture surrounded by 12-hole golf courses, lagoons, and private Mobor Beach.",
        "capacity": "200 – 750 Guests",
        "rooms": "206 Lagoon Suites, Conservatories & Royal Villas",
        "spaces": "Aparanta Grand Ballroom (400 pax), Hawa Mahal Lawns (650 pax), Mobor Beach Deck (300 pax)",
        "pricing": "₹30,00,000 – ₹80,00,000 / day",
        "catering": "Award-winning Leela culinary dining with global live stations and royal Indian banquets",
        "decor": "Empaneled luxury designer access with 3D set fabrication",
        "lead_time": "10 – 14 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What makes The Leela Goa one of India's premier wedding destinations?", "The unique meeting of the River Sal and the Arabian Sea creates unrivaled lagoon and beachfront settings with opulent palatial luxury.")
        ]
    },
    {
        "slug": "w-goa-vagator-wedding",
        "name": "W Goa",
        "city": "Vagator, North Goa",
        "state": "Goa",
        "tagline": "Bold, vibrant luxury perched on the cliffs of Vagator beach beneath Chapora Fort, featuring the iconic Rockpool sundowner venue.",
        "capacity": "100 – 400 Guests",
        "rooms": "121 Luxury Rooms, Chalets & Marvelous Villas",
        "spaces": "The Rockpool Deck (350 pax), Great Room Ballroom (250 pax), Horizon Lawns (300 pax)",
        "pricing": "₹28,00,000 – ₹70,00,000 / day buyout",
        "catering": "Avant-garde global fusion cuisine, live grills, craft cocktail mixology",
        "decor": "High-fashion bohemian, neon glam, and contemporary floral art",
        "lead_time": "8 – 12 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What style of weddings suit W Goa best?", "High-energy Sangeet pool parties, chic sundowner cocktail celebrations, and modern bohemian luxury weddings.")
        ]
    },
    {
        "slug": "alila-diwa-goa-wedding",
        "name": "Alila Diwa Goa (Hyatt)",
        "city": "Majorda, South Goa",
        "state": "Goa",
        "tagline": "Tranquil contemporary Goan sanctuary overlooking emerald paddy fields with infinity pool decks and private banqueting wings.",
        "capacity": "100 – 350 Guests",
        "rooms": "153 Luxury Rooms & The Diwa Club exclusive wing",
        "spaces": "Alila Ballroom (250 pax), Udhyan Lawns (350 pax), Courtyard (150 pax)",
        "pricing": "₹15,00,000 – ₹38,00,000 / day",
        "catering": "Authentic Spice Studio coastal cuisine and multi-cuisine banquets",
        "decor": "Nature-forward, warm fairy lights, cane & botanical styling",
        "lead_time": "6 – 10 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("Can couples buy out the exclusive Diwa Club wing?", "Yes, The Diwa Club offers a private resort-within-a-resort experience with dedicated lap pool and suites.")
        ]
    },
    {
        "slug": "taj-fort-aguada-goa-wedding",
        "name": "Taj Fort Aguada Resort & Spa",
        "city": "Candolim, North Goa",
        "state": "Goa",
        "tagline": "Historic 16th-century Portuguese coastal fort property perched on Sinquerim beach with dramatic sea-facing amphitheaters.",
        "capacity": "150 – 500 Guests",
        "rooms": "143 Sea-View Rooms & Luxury Cottages",
        "spaces": "Bay View Lawns (500 pax), Aguada Ballroom (200 pax)",
        "pricing": "₹20,00,000 – ₹50,00,000 / day",
        "catering": "Taj signature coastal and international banquets",
        "decor": "Heritage fort lighting, coastal floral arches, and canopy setups",
        "lead_time": "8 – 12 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What is the visual highlight of weddings at Taj Fort Aguada?", "The ramparts of the historic Portuguese fort overlooking the Arabian Sea provide an unmatched historic backdrop.")
        ]
    },

    # ----------------------------------------------------
    # 2. RAJASTHAN PALACE VENUES
    # ----------------------------------------------------
    {
        "slug": "jagmandir-island-palace-udaipur-wedding",
        "name": "Jagmandir Island Palace Udaipur",
        "city": "Lake Pichola, Udaipur",
        "state": "Rajasthan",
        "tagline": "The world-famous 17th-century island palace in the center of Lake Pichola, featuring grand marble elephant pavilions and royal courtyards.",
        "capacity": "200 – 800 Guests",
        "rooms": "7 Heritage Palace Suites on island (plus City Palace & hotel room blocks)",
        "spaces": "Garden Courtyard (600 pax), Kunwarpada Lawns (800 pax), Marble Pavilion (200 pax)",
        "pricing": "₹35,00,000 – ₹90,00,000 / night event hire",
        "catering": "HRH Group of Hotels royal Mewari banqueting, silver service, and global feasts",
        "decor": "Heritage protection compliant monumental floral architecture",
        "lead_time": "12 – 18 months for peak winter dates",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("How do wedding guests reach Jagmandir Island Palace?", "Guests are transported via private royal boat barges from Rameshwar Ghat jetty across Lake Pichola. Swariya coordinates dedicated jetty desks and synchronized boarding."),
            ("Can fireworks and drone photography be done at Jagmandir?", "Yes, with pre-approved local collectorate permits, dramatic fireworks displays over Lake Pichola create breathtaking finales.")
        ]
    },
    {
        "slug": "the-oberoi-udaivilas-udaipur-wedding",
        "name": "The Oberoi Udaivilas",
        "city": "Haridas Ji Ki Magri, Udaipur",
        "state": "Rajasthan",
        "tagline": "Rated among the world's top luxury hotels, featuring majestic domes, hand-painted frescoes, reflection pools, and 50 acres of royal Mewari gardens.",
        "capacity": "150 – 400 Guests",
        "rooms": "87 Luxury Rooms & Kohinoor Suites with semi-private pools",
        "spaces": "Chandra Mahal Courtyard (350 pax), Front Lawns (400 pax), Poolside Terrace (200 pax)",
        "pricing": "₹60,00,000 – ₹1.5 Crores / day total buyout",
        "catering": "Oberoi Michelin-caliber culinary excellence across royal Indian and international cuisines",
        "decor": "Sophisticated antique brass, gold leaf, and imported floral artistry",
        "lead_time": "12 – 18 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Is a full resort buyout required for weddings at The Oberoi Udaivilas?", "Yes, for complete privacy and outdoor musical events, Udaivilas generally requires a full property residential buyout.")
        ]
    },
    {
        "slug": "the-leela-palace-udaipur-wedding",
        "name": "The Leela Palace Udaipur",
        "city": "Lake Pichola, Udaipur",
        "state": "Rajasthan",
        "tagline": "Modern royal palace hotel on Lake Pichola with majestic views of the City Palace, ornate Mewari domes, and guava garden banquets.",
        "capacity": "100 – 350 Guests",
        "rooms": "80 Luxury Lake-View Rooms & Royal Suites",
        "spaces": "Guava Garden (300 pax), Marwar Hall (150 pax), Outer Courtyard (250 pax)",
        "pricing": "₹45,00,000 – ₹1.1 Crores / day buyout",
        "catering": "Sheesh Mahal royal fine dining and grand multi-cuisine wedding buffets",
        "decor": "Regal crystal chandeliers, antique silver, and velvet draping",
        "lead_time": "10 – 14 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("How does Swariya Weddings plan arrivals at The Leela Palace Udaipur?", "Guests arrive by decorated private boats with traditional Rajasthani folk artists and flower petal showers at the palace jetty.")
        ]
    },
    {
        "slug": "fairmont-jaipur-wedding",
        "name": "Fairmont Jaipur",
        "city": "Kukas, Jaipur",
        "state": "Rajasthan",
        "tagline": "Grand Mughal and Rajput palace architecture nestled in the Aravalli hills, featuring massive pillarless ballrooms and majestic central courtyards.",
        "capacity": "250 – 1,000 Guests",
        "rooms": "245 Palatial Guest Rooms & Suites",
        "spaces": "Grand Ballroom (800 pax), Central Charbagh Courtyard (1,000 pax), Aviary Lawns (400 pax)",
        "pricing": "₹35,00,000 – ₹95,00,000 / day",
        "catering": "Zarin Indo-Persian culinary masters and expansive multi-counter wedding feasts",
        "decor": "Monumental royal stages, custom trussing, and 3D architectural sets",
        "lead_time": "9 – 14 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Can Fairmont Jaipur host large 800+ guest royal weddings?", "Yes! Fairmont Jaipur is one of Rajasthan's top high-capacity luxury palace hotels designed specifically for grand multi-day weddings.")
        ]
    },
    {
        "slug": "chomu-palace-hotel-jaipur-wedding",
        "name": "Chomu Palace Hotel",
        "city": "Chomu, Jaipur",
        "state": "Rajasthan",
        "tagline": "300-year-old authentic historic royal palace with exquisite Sheesh Mahal mirror work, Darbar Hall, and heritage courtyards.",
        "capacity": "150 – 600 Guests",
        "rooms": "70 Historic Palace Heritage Suites",
        "spaces": "Moti Mahal Lawn (500 pax), Sheesh Mahal Courtyard (200 pax), Poolside Lawn (300 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day buyout",
        "catering": "Royal Marwari, Rajasthani royal feasts, and customized multi-cuisine spreads",
        "decor": "Heritage palace styling with brass diyas and marigold cascades",
        "lead_time": "6 – 12 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Is Chomu Palace an authentic heritage fort?", "Yes, it is a genuine 300-year-old fortified palace that hosted royal dynasties, offering deep historic charm.")
        ]
    },
    {
        "slug": "suryagarh-jaisalmer-wedding",
        "name": "Suryagarh Jaisalmer",
        "city": "Kahala Phata, Jaisalmer",
        "state": "Rajasthan",
        "tagline": "The golden fortress of the Thar Desert, renowned worldwide for magical desert courtyards, dunes sangeet nights, and regal hospitality.",
        "capacity": "150 – 400 Guests",
        "rooms": "83 Luxury Palace Rooms, Haveli Suites & Desert Villas",
        "spaces": "Central Sun Courtyard (350 pax), Lakeside Garden (400 pax), Sand Dunes Arena (300 pax)",
        "pricing": "₹40,00,000 – ₹1.2 Crores / day buyout",
        "catering": "Royal Halwai feasts, Rajasthani Thar delicacies, and global live grills",
        "decor": "Golden sandstone lighting, thousands of mitti diyas, and desert tenting",
        "lead_time": "10 – 16 months for winter dates",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Can we host a sangeet in the Thar Desert dunes with Suryagarh?", "Yes! Suryagarh curates private dune setups with campfire seating, folk musicians, and starry desert skies.")
        ]
    },

    # ----------------------------------------------------
    # 3. KERALA BACKWATER & COASTAL VENUES
    # ----------------------------------------------------
    {
        "slug": "kumarakom-lake-resort-wedding",
        "name": "Kumarakom Lake Resort",
        "city": "Kumarakom, Kottayam",
        "state": "Kerala",
        "tagline": "Traditional 16th-century reconstructed ancestral Kerala villas on the banks of Vembanad Lake, featuring meandering pool courtyards and water pavilions.",
        "capacity": "100 – 350 Guests",
        "rooms": "65 Heritage Luxury Villas with private plunge pools",
        "spaces": "Main Backwater Lawn (350 pax), Poolside Courtyard (200 pax), Houseboat Flotilla (150 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day buyout",
        "catering": "Authentic 24-dish Kerala Sadhya on banana leaf, Karimeen Pollichathu, and continental banquets",
        "decor": "Traditional brass urulis, floating lotus petals, coconut palm structures, and tropical floral mandaps",
        "lead_time": "8 – 12 months",
        "hero_img": "images/12.jpg",
        "faqs": [
            ("What makes Kumarakom Lake Resort legendary for weddings?", "Its architectural authenticity, lush lagoon waterways, and direct access to Vembanad Lake for floating mandaps and boat entries.")
        ]
    },
    {
        "slug": "grand-hyatt-kochi-bolgatty-wedding",
        "name": "Grand Hyatt Kochi Bolgatty",
        "city": "Mulavukad, Kochi",
        "state": "Kerala",
        "tagline": "Ultra-luxury waterfront resort on Bolgatty Island with panoramic backwater views, massive international convention ballrooms, and marina lawns.",
        "capacity": "200 – 1,500 Guests",
        "rooms": "264 Luxury Rooms, Suites & 4 Waterfront Private Villas",
        "spaces": "Lulu Grand Ballroom (1,200 pax), Marina Lawns (1,500 pax), Waterfront Deck (400 pax)",
        "pricing": "₹25,00,000 – ₹70,00,000 / day",
        "catering": "World-class Hyatt banqueting across Malabar, Pan-Asian, and North Indian cuisines",
        "decor": "Monumental contemporary floral architecture and waterfront stages",
        "lead_time": "8 – 14 months",
        "hero_img": "images/12.jpg",
        "faqs": [
            ("Can Grand Hyatt Kochi accommodate 1,000+ guests?", "Yes! It features Kerala's largest luxury convention ballroom and expansive outdoor marina lawns.")
        ]
    },
    {
        "slug": "the-zuri-kumarakom-wedding",
        "name": "The Zuri Kumarakom Kerala Resort & Spa",
        "city": "Vembanad Lake, Kumarakom",
        "state": "Kerala",
        "tagline": "18-acre luxury lagoon resort on Vembanad Lake featuring private lagoon cottages, grand ballrooms, and serene sunset amphitheaters.",
        "capacity": "150 – 500 Guests",
        "rooms": "72 Lagoon Villas & Presidential Suites",
        "spaces": "Bhairavi Ballroom (300 pax), Lakeside Lawns (500 pax), Amphitheater (200 pax)",
        "pricing": "₹16,00,000 – ₹42,00,000 / day",
        "catering": "Kerala coastal delicacies, North Indian royal banquets, and live barbecue",
        "decor": "Earthy tropical elegance with bamboo, cane, and marigold canopies",
        "lead_time": "6 – 10 months",
        "hero_img": "images/12.jpg",
        "faqs": [
            ("Is The Zuri Kumarakom suitable for 200+ residential guests?", "Yes, its room inventory and adjoining boutique tie-ups accommodate full wedding residential blocks.")
        ]
    },

    # ----------------------------------------------------
    # 4. WESTERN GHATS & HILL ESTATES
    # ----------------------------------------------------
    {
        "slug": "taj-madikeri-resort-coorg-wedding",
        "name": "Taj Madikeri Resort & Spa Coorg",
        "city": "Madikeri, Coorg",
        "state": "Karnataka",
        "tagline": "Perched 4,000 feet above sea level amidst 180 acres of living rainforest, featuring panoramic amphitheaters and glass-walled grand ballrooms.",
        "capacity": "120 – 350 Guests",
        "rooms": "63 Luxury Rainforest Cottages & Luxury Pool Villas",
        "spaces": "Sohum Amphitheater (250 pax), Grand Ballroom (200 pax), Poolside Deck (150 pax)",
        "pricing": "₹22,00,000 – ₹55,00,000 / day",
        "catering": "Curated Kodava Pandi Curry, Akki Roti, authentic South Indian, and international gourmet banquets",
        "decor": "Rainforest foliage, wild eucalyptus, misty open-air floral mandaps, and wood crafted stages",
        "lead_time": "8 – 14 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("What makes Taj Madikeri unique for destination weddings?", "The 180-acre rainforest setting at 4,000 feet elevation provides crisp mountain weather, mist-covered morning pheras, and dramatic hill panoramas.")
        ]
    },
    {
        "slug": "the-tamara-coorg-wedding",
        "name": "The Tamara Coorg",
        "city": "Yevakapadi, Coorg",
        "state": "Karnataka",
        "tagline": "180-acre private luxury coffee, cardamom, and pepper plantation with luxury wooden cottages on stilts over babbling mountain streams.",
        "capacity": "80 – 200 Guests",
        "rooms": "56 Luxury Wooden Cottages & Suites",
        "spaces": "The Deck Lawn (180 pax), Plantation Amphitheater (150 pax)",
        "pricing": "₹18,00,000 – ₹40,00,000 / day buyout",
        "catering": "Estate-to-table organic Kodava and multi-cuisine cuisine",
        "decor": "Eco-luxury botanical styling, fairy light canopies, and rustic wood mandaps",
        "lead_time": "6 – 12 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("Is The Tamara Coorg ideal for intimate micro-weddings?", "Yes! It is widely recognized as one of India's most serene eco-luxury plantation resorts for 80–180 guest private buyouts.")
        ]
    },
    {
        "slug": "evolve-back-kabini-wedding",
        "name": "Evolve Back, Kuruba Safari Lodge, Kabini",
        "city": "Kabini, HD Kote",
        "state": "Karnataka",
        "tagline": "Tribal vernacular luxury on the banks of the Kabini River, with private pool huts and serene sunset riverfront celebration decks.",
        "capacity": "80 – 200 Guests",
        "rooms": "37 Luxury Huts, Pool Huts & Jacuzzi Villas",
        "spaces": "Riverfront Lawns (200 pax), Kuruba Courtyard (120 pax)",
        "pricing": "₹20,00,000 – ₹45,00,000 / day buyout",
        "catering": "Gourmet coastal and regional specialties, riverside live barbecues",
        "decor": "Natural timber, terracotta, wild foliage, and brass lanterns",
        "lead_time": "6 – 10 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("Can couples host a private riverside wedding at Evolve Back Kabini?", "Yes, the riverfront lawn provides sweeping views of the Kabini waters and wildlife reserve on the opposite bank.")
        ]
    },
    {
        "slug": "caravela-beach-resort-goa-wedding",
        "name": "Caravela Beach Resort Goa",
        "city": "Varca Beach, South Goa",
        "state": "Goa",
        "tagline": "24-acre tropical beachfront paradise on pristine Varca beach with sprawling landscaped gardens and 9-hole golf course.",
        "capacity": "150 – 600 Guests",
        "rooms": "198 Ocean-Facing Rooms & Beachfront Villas",
        "spaces": "Varca Beach Lawns (600 pax), Caravela Ballroom (300 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day",
        "catering": "Fresh coastal seafood, royal Indian feasts, and international banquets",
        "decor": "Tropical floral mandaps, fairy light canopies, and beach aisle runners",
        "lead_time": "6 – 10 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What makes Varca beach ideal for destination weddings?", "Varca beach is famous for its serene white sands, private coastline, and dramatic sunset backdrops.")
        ]
    },
    {
        "slug": "grand-hyatt-goa-wedding",
        "name": "Grand Hyatt Goa",
        "city": "Bambolim Bay, North Goa",
        "state": "Goa",
        "tagline": "28-acre 17th-century Indo-Portuguese palace on Bambolim Bay with Goa's largest indoor ballroom and seaside lawns.",
        "capacity": "250 – 1,200 Guests",
        "rooms": "313 Palatial Guest Rooms & Suites",
        "spaces": "Grand Ballroom (1,000 pax), Palace Lawns (1,200 pax), Bay View Courtyard (350 pax)",
        "pricing": "₹35,00,000 – ₹90,00,000 / day",
        "catering": "World-renowned Hyatt banqueting across Pan-Asian, Indian royal, and Middle Eastern counters",
        "decor": "Monumental royal stages, custom lighting rigs, and seaside mandap setups",
        "lead_time": "9 – 14 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("Can Grand Hyatt Goa host large 1,000+ guest weddings?", "Yes, it features the largest ballroom in Goa and expansive coastal lawns designed for grand scale celebrations.")
        ]
    },
    {
        "slug": "st-regis-goa-resort-wedding",
        "name": "The St. Regis Goa Resort",
        "city": "Mobor Beach, Cavelossim",
        "state": "Goa",
        "tagline": "49 acres of luxury between the Sal River and Mobor Beach, with signature St. Regis Butler service and private lagoon lawns.",
        "capacity": "150 – 600 Guests",
        "rooms": "206 Luxury Rooms, Suites & Presidential Pool Villas",
        "spaces": "Astor Ballroom (400 pax), Riverfront Lawns (600 pax), Mobor Beach Deck (250 pax)",
        "pricing": "₹35,00,000 – ₹85,00,000 / day",
        "catering": "Michelin-inspired dining and royal Indian banqueting",
        "decor": "High-end bespoke floral architecture and crystal chandeliers",
        "lead_time": "10 – 14 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What exclusive amenities does St. Regis Goa provide for weddings?", "Signature St. Regis Butler service, private lagoon lawns, and direct access to pristine Mobor Beach.")
        ]
    },
    {
        "slug": "jai-mahal-palace-jaipur-wedding",
        "name": "Jai Mahal Palace Jaipur",
        "city": "Jacob Road, Civil Lines, Jaipur",
        "state": "Rajasthan",
        "tagline": "18 acres of landscaped Mughal gardens dating back to 1745, offering authentic Indo-Saracenic royal palace luxury in central Jaipur.",
        "capacity": "200 – 1,000 Guests",
        "rooms": "100 Historic Palace Heritage Rooms & Suites",
        "spaces": "Palace Lawns (1,000 pax), Fountain Courtyard (400 pax), Durbar Hall (150 pax)",
        "pricing": "₹30,00,000 – ₹80,00,000 / day",
        "catering": "Taj royal Rajputana culinary feasts and multi-cuisine banquets",
        "decor": "Authentic Mughal garden styling, antique brass torchlights, and royal red carpet baaraats",
        "lead_time": "10 – 16 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Why is Jai Mahal Palace historic for weddings?", "Dating back to 1745, the property features authentic Mughal gardens and original Rajputana palace architecture.")
        ]
    },
    {
        "slug": "rambagh-palace-jaipur-wedding",
        "name": "Rambagh Palace Jaipur",
        "city": "Bhawani Singh Road, Jaipur",
        "state": "Rajasthan",
        "tagline": "The former residence of the Maharaja of Jaipur, widely recognized as one of the world's most luxurious heritage palace hotels.",
        "capacity": "150 – 600 Guests",
        "rooms": "78 Historic Palace Royal Suites",
        "spaces": "Mubarak Mahal (200 pax), Oriental Garden (600 pax), Sunken Lawn (350 pax)",
        "pricing": "₹60,00,000 – ₹1.8 Crores / day",
        "catering": "Suvarna Mahal royal palace silver service and bespoke culinary curation",
        "decor": "High royal heritage styling, antique silver chhatris, and hand-strung marigold canopies",
        "lead_time": "12 – 18 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Is Rambagh Palace suitable for ultra-luxury destination weddings?", "Yes, it is among the world's most prestigious royal palace properties, offering uncompromised Maharaja-style luxury.")
        ]
    },
    {
        "slug": "umaid-bhawan-palace-jodhpur-wedding",
        "name": "Umaid Bhawan Palace Jodhpur",
        "city": "Circuit House Rd, Jodhpur",
        "state": "Rajasthan",
        "tagline": "Perched on Chittar Hill, one of the world's largest private royal residences, featuring golden Art Deco-Rajput architecture.",
        "capacity": "200 – 600 Guests",
        "rooms": "70 Art Deco Royal Palace Suites",
        "spaces": "Baradari Lawns (600 pax), Marwar Hall (250 pax), Central Dome Pavilion (150 pax)",
        "pricing": "₹75,00,000 – ₹2.5 Crores / day",
        "catering": "Royal Marwar banqueting, gold-leaf plated dining, and international gourmet counters",
        "decor": "Opulent Art Deco royal florals, monumental crystal installations, and royal elephant baaraats",
        "lead_time": "12 – 24 months for prime dates",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What makes Umaid Bhawan Palace the pinnacle of royal weddings?", "Built between 1928 and 1943 from golden sandstone, it remains the principal residence of the Jodhpur royal family, offering unrivaled regal grandeur.")
        ]
    },
    {
        "slug": "the-westin-pushkar-wedding",
        "name": "The Westin Pushkar Resort & Spa",
        "city": "Pushkar, Ajmer",
        "state": "Rajasthan",
        "tagline": "Tranquil oasis surrounded by the picturesque Aravalli hills, featuring private plunge pool villas and expansive celebration lawns.",
        "capacity": "150 – 500 Guests",
        "rooms": "98 Private Pool Villas & Luxury Suites",
        "spaces": "Aravalli Lawns (500 pax), Grand Ballroom (250 pax), Poolside Courtyard (200 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day",
        "catering": "Royal Rajasthani, satvik pure vegetarian feasts, and global live counters",
        "decor": "Earthy desert elegance, terracotta accents, and fragrant marigold mandaps",
        "lead_time": "6 – 10 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Is The Westin Pushkar easily reachable from Jaipur?", "Yes, it is a smooth 2.5-hour highway drive from Jaipur International Airport (JAI).")
        ]
    },
    {
        "slug": "the-leela-kovalam-wedding",
        "name": "The Leela Kovalam, a Raviz Hotel",
        "city": "Kovalam Beach, Thiruvananthapuram",
        "state": "Kerala",
        "tagline": "Spectacular cliff-top luxury resort perched high above the Arabian Sea with private beach access and panoramic ocean sunset views.",
        "capacity": "150 – 500 Guests",
        "rooms": "188 Ocean-View Rooms & Cliff-Top Suites",
        "spaces": "Cliff Lawn (400 pax), Maya Grand Ballroom (300 pax), Private Beach Deck (200 pax)",
        "pricing": "₹22,00,000 – ₹55,00,000 / day",
        "catering": "Coastal seafood, traditional Kerala Sadhyas, and international banquet buffets",
        "decor": "Dramatic ocean cliff floral arches, candlelit pathways, and tropical palm canopies",
        "lead_time": "8 – 12 months",
        "hero_img": "images/12.jpg",
        "faqs": [
            ("How far is The Leela Kovalam from Trivandrum Airport?", "The resort is just 25 minutes from Trivandrum International Airport (TRV).")
        ]
    },
    {
        "slug": "the-serai-chikmagalur-wedding",
        "name": "The Serai Chikmagalur",
        "city": "Mugthihalli, Chikmagalur",
        "state": "Karnataka",
        "tagline": "Private plunge pool villas nestled inside a lush coffee plantation beneath Mullayanagiri peak.",
        "capacity": "100 – 300 Guests",
        "rooms": "29 Luxury Private Pool Villas & Estate Suites",
        "spaces": "Plantation Lawns (300 pax), Poolside Deck (150 pax)",
        "pricing": "₹15,00,000 – ₹35,00,000 / day buyout",
        "catering": "Authentic Malnad cuisine, fresh coffee baristas, and live grills",
        "decor": "Rustic wooden mandaps, wild ferns, eucalyptus, and warm fairy lights",
        "lead_time": "6 – 10 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("Can couples book the entire Serai Chikmagalur resort for a wedding?", "Yes, a full property buyout guarantees total privacy for 100–250 residential guests.")
        ]
    },
    {
        "slug": "evolve-back-hampi-wedding",
        "name": "Evolve Back, Kamalapura Palace, Hampi",
        "city": "Kamalapura, Hampi",
        "state": "Karnataka",
        "tagline": "Magnificent royal palace resort inspired by 14th-century Vijayanagara architecture, featuring stone arches, aqueducts, and private pool suites.",
        "capacity": "100 – 250 Guests",
        "rooms": "46 Palatial Suites (Jal Mahal & Nivasa)",
        "spaces": "Palace Courtyard (250 pax), Pushkarini Poolside (150 pax)",
        "pricing": "₹25,00,000 – ₹60,00,000 / day buyout",
        "catering": "Royal South Indian feasts, authentic Rayalaseema delicacies, and global dining",
        "decor": "Historic stone temple aesthetics, antique brass diyas, and temple marigold styling",
        "lead_time": "8 – 14 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What makes Evolve Back Hampi a unique wedding venue?", "Its authentic stone palace architecture transports guests directly into the golden era of the Vijayanagara empire.")
        ]
    },
    {
        "slug": "lalitha-mahal-palace-mysore-wedding",
        "name": "Lalitha Mahal Palace Hotel Mysore",
        "city": "Siddhartha Nagar, Mysore",
        "state": "Karnataka",
        "tagline": "Italianate royal palace built in 1921 by the Maharaja of Mysore, featuring magnificent white domes, grand banquet ballrooms, and manicured lawns.",
        "capacity": "200 – 800 Guests",
        "rooms": "54 Royal Heritage Palace Rooms & Suites",
        "spaces": "Main Palace Lawn (800 pax), Grand Ballroom (250 pax), Terrace (150 pax)",
        "pricing": "₹12,00,000 – ₹32,00,000 / day",
        "catering": "Royal Mysore royal cuisine, authentic South Indian plantain leaf spreads, and North Indian banquets",
        "decor": "Colonial white architecture accented with royal red carpets and authentic Mysore Mallige jasmine",
        "lead_time": "6 – 10 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("How accessible is Lalitha Mahal Palace from Bangalore?", "Via the new Bangalore-Mysore Expressway, travel time is approximately 90 minutes.")
        ]
    },
    {
        "slug": "radisson-blu-alibaug-wedding",
        "name": "Radisson Blu Resort & Spa Alibaug",
        "city": "Gondhalpada, Veshvi, Alibaug",
        "state": "Maharashtra",
        "tagline": "16-acre coastal luxury resort with tranquil lake waterways, open-air lawns, and close proximity to Mandwa Jetty.",
        "capacity": "150 – 500 Guests",
        "rooms": "156 Luxury Rooms, Suites & Villas",
        "spaces": "Grand Ballroom (350 pax), Lake Lawns (500 pax), Pool Deck (200 pax)",
        "pricing": "₹20,0,000 – ₹50,00,000 / day",
        "catering": "Coastal Konkani cuisine, royal Indian banquets, and continental live stations",
        "decor": "Tropical coastal elegance, fairy light canopies, and waterbody mandap setups",
        "lead_time": "6 – 10 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("How do Mumbai guests reach Radisson Blu Alibaug?", "A 20-minute speedboat ride from Gateway of India to Mandwa Jetty followed by a 15-minute transfer.")
        ]
    },
    {
        "slug": "della-resorts-lonavala-wedding",
        "name": "Della Resorts Lonavala",
        "city": "Kunegaon, Lonavala",
        "state": "Maharashtra",
        "tagline": "High-luxury adventure resort in the Sahyadri mountains with dramatic themed banquet ballrooms and luxury poolside courtyards.",
        "capacity": "150 – 600 Guests",
        "rooms": "250 Luxury Designer Rooms & Presidential Suites",
        "spaces": "Della Grand Ballroom (400 pax), Pool Amphitheater (600 pax), Valley Deck (200 pax)",
        "pricing": "₹25,00,000 – ₹65,00,000 / day",
        "catering": "Multi-cuisine gourmet dining, Parsi delicacies, and global live barbecue",
        "decor": "Contemporary high-glam lighting, LED concert trussing, and imported floral stages",
        "lead_time": "6 – 12 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("Why choose Della Resorts for a destination Sangeet and wedding?", "It offers high-capacity luxury rooms, 24/7 hospitality, and world-class concert audio-visual capabilities.")
        ]
    },
    {
        "slug": "the-taj-mahal-palace-mumbai-wedding",
        "name": "The Taj Mahal Palace Mumbai",
        "city": "Apollo Bunder, Colaba, South Mumbai",
        "state": "Maharashtra",
        "tagline": "India's most iconic historic flagship hotel overlooking the Gateway of India and the Arabian Sea, featuring legendary ballrooms.",
        "capacity": "150 – 650 Guests",
        "rooms": "285 Historic Palace & Tower Luxury Suites",
        "spaces": "The Ballroom (400 pax), Crystal Room (300 pax), Gateway View Terrace (150 pax)",
        "pricing": "₹45,00,000 – ₹1.2 Crores / day event hire",
        "catering": "Legendary Taj fine dining with silver service and bespoke menus curated by master chefs",
        "decor": "Flawless heritage palace styling with crystal chandeliers and royal floral art",
        "lead_time": "10 – 16 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What makes a wedding at The Taj Mahal Palace Mumbai iconic?", "Established in 1903, it is India's most prestigious hospitality landmark with direct views of the Gateway of India.")
        ]
    },
    {
        "slug": "jw-marriott-mussoorie-wedding",
        "name": "JW Marriott Mussoorie Walnut Grove Resort & Spa",
        "city": "Mussoorie, Uttarakhand",
        "state": "North",
        "tagline": "Perched in the Garhwal Himalayan foothills, featuring grand cedar tree lawns and panoramic mountain valley views.",
        "capacity": "150 – 450 Guests",
        "rooms": "115 Luxury Himalayan View Rooms & Suites",
        "spaces": "Grand Ballroom (300 pax), Walnut Grove Lawns (450 pax), Cedar Courtyard (200 pax)",
        "pricing": "₹35,00,000 – ₹90,00,000 / day",
        "catering": "Gourmet Garhwali specialties, North Indian royal feasts, and international banquets",
        "decor": "Rustic pinecone accents, Himalayan wild florals, and glass-canopy mandaps",
        "lead_time": "9 – 14 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What is the best season for a wedding at JW Marriott Mussoorie?", "April to June for pleasant summer mountain breezes, and October to November for crisp autumn foliage.")
        ]
    },
    {
        "slug": "taj-rishikesh-resort-wedding",
        "name": "Taj Rishikesh Resort & Spa",
        "city": "Singthali, Rishikesh",
        "state": "North",
        "tagline": "Tranquil sanctuary on the banks of the sacred Ganges, featuring private sand beach access and Himalayan terrace amphitheaters.",
        "capacity": "100 – 250 Guests",
        "rooms": "79 Luxury Hill-View Rooms & River Villas",
        "spaces": "Riverfront Beach Lawn (250 pax), Ganga Ballroom (150 pax), Sunset Terrace (120 pax)",
        "pricing": "₹28,00,000 – ₹70,00,000 / day buyout",
        "catering": "Satvik gourmet dining, organic regional delicacies, and international cuisine",
        "decor": "Sacred brass bells, marigold cascades, floating river diyas, and bamboo mandaps",
        "lead_time": "8 – 14 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Can a private Ganga Aarti be arranged for wedding ceremonies?", "Yes! Taj Rishikesh coordinates private riverside Ganga Aarti on its beach for unforgettable spiritual blessings.")
        ]
    },
    {
        "slug": "taj-corbett-resort-wedding",
        "name": "Taj Corbett Resort & Spa",
        "city": "Zero Garjia, Dhikuli, Jim Corbett",
        "state": "North",
        "tagline": "Sprawling Kosi riverfront property surrounded by dense Sal forests and the foothills of the Himalayas.",
        "capacity": "150 – 450 Guests",
        "rooms": "61 Luxury Cottages & Suites",
        "spaces": "Kosi Riverbank Lawns (450 pax), Jim's Grill Deck (200 pax), Ballroom (150 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day",
        "catering": "Kumaoni regional specialties, live jungle barbecue, and multi-cuisine spreads",
        "decor": "Rustic natural wood, wild forest greenery, lanterns, and open-air riverside mandaps",
        "lead_time": "6 – 10 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("How far is Taj Corbett Resort from Delhi NCR?", "It is approximately 4.5 hours by road or a direct luxury train to Ramnagar station.")
        ]
    },
    {
        "slug": "itc-grand-bharat-gurgaon-wedding",
        "name": "ITC Grand Bharat Gurgaon",
        "city": "Hasanpur, Tauru, Gurgaon",
        "state": "Delhi",
        "tagline": "300-acre palatial oasis modeled after ancient Indian dynasties with 27-hole Jack Nicklaus golf course and luxury pool pavilions.",
        "capacity": "200 – 800 Guests",
        "rooms": "104 Luxury Suites & 4 Presidential Villas",
        "spaces": "Aravalli Lawns (800 pax), Prithvi Ballroom (350 pax), Yamuna Courtyard (200 pax)",
        "pricing": "₹45,00,000 – ₹1.2 Crores / day",
        "catering": "ITC royal heritage dining (Bukhara, Dum Pukht) and global culinary stations",
        "decor": "Monumental royal architecture with stone-carved mandap structures and fireworks",
        "lead_time": "9 – 14 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Why is ITC Grand Bharat ideal for luxury residential weddings?", "It offers an all-suite retreat with total privacy just 60 minutes from New Delhi International Airport (DEL).")
        ]
    },
    {
        "slug": "taj-falaknuma-palace-hyderabad-wedding",
        "name": "Taj Falaknuma Palace Hyderabad",
        "city": "Engine Bowli, Falaknuma, Hyderabad",
        "state": "Telangana",
        "tagline": "The legendary 'Mirror of the Sky' palace of the Nizams perched 2,000 feet above Hyderabad with horse-drawn carriages and 101-seat dining tables.",
        "capacity": "150 – 500 Guests",
        "rooms": "60 Historic Palace Guest Rooms & Royal Presidential Suites",
        "spaces": "Main Palace Courtyard (500 pax), Rajasthani Gardens (300 pax), 101 Dining Hall (101 VIPs)",
        "pricing": "₹60,00,000 – ₹1.5 Crores / day event buyout",
        "catering": "Royal Nizami feasts, Hyderabadi Dum Biryani, and bespoke silver-plate service",
        "decor": "Historic royal palace preservation styling, floral cascades, and classical live sitar",
        "lead_time": "12 – 18 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("How do guests arrive at Taj Falaknuma Palace?", "Guests are welcomed with a royal horse-drawn carriage procession up the palace hill accompanied by rose petal showers."),
            ("Can non-residential guests attend weddings at Falaknuma Palace?", "Due to strict palace security and heritage preservation, intimate residential buyouts are highly recommended.")
        ]
    },
    {
        "slug": "itc-kohenur-hyderabad-wedding",
        "name": "ITC Kohenur Hyderabad",
        "city": "HITEC City, Madhapur, Hyderabad",
        "state": "Telangana",
        "tagline": "Ultra-luxury modern landmark overlooking Durgam Cheruvu lake, featuring dramatic pillarless ballrooms and avant-garde banquet architecture.",
        "capacity": "200 – 1000 Guests",
        "rooms": "271 Luxury Rooms, Suites & Serviced Residences",
        "spaces": "The Deccan State Ballroom (1000 pax), Sky Point Rooftop (200 pax), Pearl Lawns (400 pax)",
        "pricing": "₹30,00,000 – ₹75,00,000 / day",
        "catering": "Legendary ITC Dum Pukht Begum's, Yi Jing modern Chinese, and royal Deccani feasts",
        "decor": "Grand contemporary crystal styling, LED kinetic ceilings, and modern floral installations",
        "lead_time": "8 – 12 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What is the pillarless ballroom capacity at ITC Kohenur?", "The Deccan State Ballroom spans over 11,000 sq.ft and comfortably hosts up to 1,000 guests for grand Sangeet and reception nights.")
        ]
    },
    {
        "slug": "intercontinental-chennai-mahabalipuram-wedding",
        "name": "InterContinental Chennai Mahabalipuram Resort",
        "city": "East Coast Road (ECR), Mahabalipuram, Chennai",
        "state": "Tamil Nadu",
        "tagline": "Temple-inspired luxury sanctuary on the Coromandel Coast with sprawling beachfront lawns, central lotus ponds, and coastal sea breezes.",
        "capacity": "150 – 700 Guests",
        "rooms": "105 Luxury Rooms & Ocean Front Suites",
        "spaces": "Casuarina Beachfront Lawns (700 pax), Samudra Ballroom (350 pax), Lotus Courtyard (200 pax)",
        "pricing": "₹22,00,000 – ₹55,00,000 / day",
        "catering": "Coastal Tamil Chettinad feasts, fresh seafood live counters, and Pan-Asian banquets",
        "decor": "Coastal bohemian elegance, temple brass bells, and open-air beach mandaps",
        "lead_time": "8 – 12 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("Can beach mandaps be set up on the private beach at InterContinental Chennai?", "Yes, the property features a direct private beachfront lawn allowing serene sunset and sunrise ocean mandap ceremonies.")
        ]
    },
    {
        "slug": "taj-fishermans-cove-chennai-wedding",
        "name": "Taj Fisherman's Cove Resort & Spa Chennai",
        "city": "Covelong Beach, ECR, Chennai",
        "state": "Tamil Nadu",
        "tagline": "Built on the ramparts of an old Dutch Fort overlooking the Bay of Bengal, offering private beach cottages and oceanfront lawns.",
        "capacity": "150 – 800 Guests",
        "rooms": "150 Sea-Facing Cottages, Villas & Luxury Rooms",
        "spaces": "Bay View Lawns (800 pax), Casuarina Ballroom (300 pax), Beach Deck (250 pax)",
        "pricing": "₹25,00,000 – ₹60,00,000 / day",
        "catering": "Signature Taj coastal seafood, authentic South Indian wedding feasts, and global buffets",
        "decor": "Nautical coastal floral themes, fairy light canopies under coconut palms, and sunset stage designs",
        "lead_time": "9 – 14 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("Why choose Taj Fisherman's Cove for destination weddings in Tamil Nadu?", "It combines iconic Taj hospitality, historic Dutch fort architecture, and direct private beach access on Chennai's ECR.")
        ]
    },
    {
        "slug": "sheraton-grand-chennai-resort-wedding",
        "name": "Sheraton Grand Chennai Resort & Spa",
        "city": "Vadanemmeli, ECR, Chennai",
        "state": "Tamil Nadu",
        "tagline": "Contemporary beach paradise surrounded by turquoise waters and lush greenery with expansive beachfront banqueting lawns.",
        "capacity": "150 – 650 Guests",
        "rooms": "129 Sea View Rooms & Suites",
        "spaces": "Grand Ocean Lawn (650 pax), Coral Ballroom (350 pax), Pintail Deck (200 pax)",
        "pricing": "₹20,00,000 – ₹50,00,000 / day",
        "catering": "Multi-cuisine experiential banquets, live barbecue grills, and traditional vegetarian feasts",
        "decor": "Modern luxury pastel florals, drape styling, and beachfront boardwalk setups",
        "lead_time": "7 – 11 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("How far is Sheraton Grand Chennai from Chennai International Airport?", "It is approximately 45 minutes along the scenic East Coast Road (ECR).")
        ]
    },
    {
        "slug": "samode-palace-jaipur-wedding",
        "name": "Samode Palace Jaipur",
        "city": "Samode, Jaipur",
        "state": "Rajasthan",
        "tagline": "A 475-year-old royal marvel nestled in the Aravalli hills featuring world-renowned Sheesh Mahal mirror mosaics and rooftop infinity pools.",
        "capacity": "100 – 350 Guests",
        "rooms": "43 Grand Palace Suites & Royal Royal Suites",
        "spaces": "Main Palace Courtyard (350 pax), Sheesh Mahal (80 pax), Rooftop Pool Terrace (200 pax)",
        "pricing": "₹35,00,000 – ₹85,00,000 / day buyout",
        "catering": "Royal Rajputana gourmet feasts, live laal maas stations, and traditional Rajasthani banquets",
        "decor": "Heritage candlelit courtyards, marigold chandeliers, and hand-painted fresco backdrops",
        "lead_time": "10 – 16 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Is exclusive property buyout required for weddings at Samode Palace?", "Yes, Samode Palace is best booked as a total private royal buyout for exclusive 2-3 day wedding festivities.")
        ]
    },
    {
        "slug": "alila-fort-bishangarh-jaipur-wedding",
        "name": "Alila Fort Bishangarh",
        "city": "Manoharpur, Bishangarh, Jaipur",
        "state": "Rajasthan",
        "tagline": "A majestic 230-year-old warrior fortress perched atop a granite hill with 360-degree views of the Rajasthani countryside.",
        "capacity": "80 – 250 Guests",
        "rooms": "59 Fortress Heritage Suites",
        "spaces": "Aravalli Lawns (250 pax), Darbar Hall (150 pax), Dawat Terrace (100 pax)",
        "pricing": "₹40,00,000 – ₹95,00,000 / day buyout",
        "catering": "Artisanal open-fire cooking, royal Rajput culinary traditions, and wellness-focused menus",
        "decor": "Architectural stone lighting, minimalist organic florals, and fire torches",
        "lead_time": "9 – 15 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What style of weddings are suited to Alila Fort Bishangarh?", "Intimate, high-luxury experiential royal weddings with discerning architectural and gastronomic expectations.")
        ]
    },
    {
        "slug": "shiv-niwas-palace-udaipur-wedding",
        "name": "Shiv Niwas Palace (HRH Group) Udaipur",
        "city": "City Palace Complex, Udaipur",
        "state": "Rajasthan",
        "tagline": "Crescent-shaped royal palace inside Udaipur's historic City Palace complex overlooking Lake Pichola.",
        "capacity": "100 – 400 Guests",
        "rooms": "36 Unique Antique Heritage Suites",
        "spaces": "Zenana Mahal Courtyard (400 pax), Pool Deck (200 pax), Manek Chowk (600 pax)",
        "pricing": "₹35,00,000 – ₹90,00,000 / day",
        "catering": "HRH Royal Mewar hospitality and gourmet international dining",
        "decor": "Regal Mewari canopies, silver thrones, royal elephant welcomes, and fireworks across Lake Pichola",
        "lead_time": "10 – 16 months in advance",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Can couples host dinner at Zenana Mahal when booking Shiv Niwas?", "Yes, Zenana Mahal and Manek Chowk inside City Palace can be booked in coordination with Shiv Niwas accommodations.")
        ]
    },
    {
        "slug": "fateh-garh-udaipur-wedding",
        "name": "Fateh Garh Heritage Resort Udaipur",
        "city": "Sisarma, Udaipur",
        "state": "Rajasthan",
        "tagline": "Renaissance-style sustainable heritage palace perched on a hilltop overlooking Lake Pichola and the Sajjangarh Monsoon Palace.",
        "capacity": "150 – 450 Guests",
        "rooms": "56 Heritage Rooms & Suites",
        "spaces": "Dari Khana Terrace (400 pax), Poolside Amphitheater (250 pax), Courtyard (200 pax)",
        "pricing": "₹20,00,000 – ₹48,00,000 / day",
        "catering": "Authentic Mewari cuisine, Rajasthani royal platters, and continental dining",
        "decor": "Hilltop sunset lighting, vintage automobile entries, and traditional Rajasthani folk styling",
        "lead_time": "8 – 12 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Does Fateh Garh have vintage car collections for wedding entries?", "Yes, Fateh Garh has an on-site vintage car museum, and classic cars can be incorporated into the groom's Baraat.")
        ]
    },
    {
        "slug": "planet-hollywood-goa-wedding",
        "name": "Planet Hollywood Beach Resort Goa",
        "city": "Utorda Beach, South Goa",
        "state": "Goa",
        "tagline": "Contemporary oceanfront luxury resort on white sandy Utorda Beach with vibrant party vibes and grand lawn spaces.",
        "capacity": "150 – 750 Guests",
        "rooms": "115 Luxury Rooms, Suites & Tents",
        "spaces": "Grand Ballroom (350 pax), Utorda Beachfront Lawn (750 pax), Heart Shaped Pool Deck (300 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day",
        "catering": "Eclectic global dining, Goan beach barbecues, and expansive Indian wedding banquets",
        "decor": "High-glam Hollywood styling, beach bohemian setups, and illuminated pool walkways",
        "lead_time": "7 – 12 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("Is Planet Hollywood pet-friendly for couples wanting pets in their wedding party?", "Yes, Planet Hollywood Goa is one of the few luxury 5-star beachfront resorts with pet-friendly rooms and lawn policies.")
        ]
    },
    {
        "slug": "azaya-beach-resort-goa-wedding",
        "name": "Azaya Beach Resort Goa",
        "city": "Benaulim, South Goa",
        "state": "Goa",
        "tagline": "Maldivian-inspired barefoot luxury resort on Benaulim Beach featuring private plunge pool suites and open ocean lawns.",
        "capacity": "100 – 450 Guests",
        "rooms": "114 Design Rooms & Plunge Pool Suites",
        "spaces": "Ocean Lawns (450 pax), Cidade de Azaya Ballroom (250 pax), Library Lounge Deck (150 pax)",
        "pricing": "₹16,00,000 – ₹42,00,000 / day",
        "catering": "Coastal Goan delicacies, live wok stations, and contemporary international spreads",
        "decor": "Tropical pastel floristry, bamboo mandaps, and sunset fairy light canopies",
        "lead_time": "6 – 10 months",
        "hero_img": "images/10.jpg",
        "faqs": [
            ("What makes Azaya Beach Resort unique for intimate destination weddings?", "Its Maldivian architecture and private plunge pool rooms create an idyllic honeymoon-resort feel for close family celebrations.")
        ]
    },
    {
        "slug": "marari-beach-resort-kerala-wedding",
        "name": "Marari Beach Resort (CGH Earth) Kerala",
        "city": "Mararikulam, Alleppey, Kerala",
        "state": "Kerala",
        "tagline": "55-acre eco-luxury seaside retreat modeled after traditional fishermen villages with thatched cottages and organic spice gardens.",
        "capacity": "80 – 300 Guests",
        "rooms": "62 Heritage Thatched Cottages & Pool Villas",
        "spaces": "Beachfront Coconut Grove (300 pax), Lotus Lawns (200 pax), Garden Pavilion (120 pax)",
        "pricing": "₹18,00,000 – ₹45,00,000 / day buyout",
        "catering": "Traditional Kerala Sadhya served on banana leaves, coastal seafood grills, and organic farm-to-table cuisine",
        "decor": "Eco-friendly natural coconut palm weaving, brass vilakku oil lamps, and marigold garlands",
        "lead_time": "8 – 12 months",
        "hero_img": "images/12.jpg",
        "faqs": [
            ("Can Swariya coordinate zero-waste, eco-friendly weddings at Marari Beach Resort?", "Yes! Marari Beach is one of our flagship venues for eco-luxury sustainable weddings with zero single-use plastics and natural decor.")
        ]
    },
    {
        "slug": "brunton-boatyard-kochi-wedding",
        "name": "Brunton Boatyard (CGH Earth) Fort Kochi",
        "city": "Fort Kochi, Kochi, Kerala",
        "state": "Kerala",
        "tagline": "Historic Victorian and Dutch shipyard restored into a boutique waterfront hotel overlooking the Kochi harbor and Chinese fishing nets.",
        "capacity": "60 – 200 Guests",
        "rooms": "22 Sea-Facing Heritage Rooms & Suites",
        "spaces": "Harbour Pier Deck (200 pax), Central Courtyard (120 pax), History Ballroom (80 pax)",
        "pricing": "₹14,00,000 – ₹32,00,000 / day buyout",
        "catering": "Legendary Kochi colonial cuisine blending Portuguese, Dutch, Jewish, and Syrian Christian recipes",
        "decor": "Colonial antique brass, vintage wooden furniture, and harbor sunset backdrops",
        "lead_time": "6 – 10 months",
        "hero_img": "images/12.jpg",
        "faqs": [
            ("Can guests arrive by traditional Kerala backwater boat?", "Yes! Brunton Boatyard has its own private jetty where the bridal party and guests can arrive via decorated wooden boats.")
        ]
    },
    {
        "slug": "the-roseate-new-delhi-wedding",
        "name": "The Roseate New Delhi",
        "city": "NH8, Samalkha, New Delhi",
        "state": "Delhi",
        "tagline": "8 acres of tranquil water bodies and 650,000 architectural trees just 10 minutes from Delhi International Airport.",
        "capacity": "100 – 400 Guests",
        "rooms": "65 Architectural Water-Facing Rooms & Suites",
        "spaces": "Reflecting Water Courtyard (400 pax), The Ballroom (200 pax), Lakeside Lawns (300 pax)",
        "pricing": "₹30,00,000 – ₹70,00,000 / day buyout",
        "catering": "Artisanal modern Indian cuisine, European fine dining, and live confectionery stations",
        "decor": "Architectural water reflections, sculptural floral art, and minimalist modern luxury",
        "lead_time": "8 – 12 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("Why is The Roseate ideal for international fly-in destination weddings?", "Located right next to IGI Airport (DEL), international and Pan-India guests can land and reach the resort in under 10 minutes.")
        ]
    },
    {
        "slug": "taj-lands-end-mumbai-wedding",
        "name": "Taj Lands End Mumbai",
        "city": "Bandstand, Bandra West, Mumbai",
        "state": "Maharashtra",
        "tagline": "Ultra-luxury hotel overlooking the Bandra-Worli Sea Link and Arabian Sea with the historic Bandra Fort adjacent.",
        "capacity": "200 – 1200 Guests",
        "rooms": "493 Luxury Rooms & Sea-Facing Suites",
        "spaces": "Seaside Lawns (1200 pax), Ballroom (600 pax), Garden View Room (200 pax)",
        "pricing": "₹40,00,000 – ₹1.1 Crores / day",
        "catering": "Taj master chefs featuring Masala Bay, Ming Yang, and royal multi-cuisine banquet feasts",
        "decor": "Sea-facing modern luxury drapes, crystal chandeliers, and grand celebrity-scale staging",
        "lead_time": "9 – 14 months",
        "hero_img": "images/11.jpg",
        "faqs": [
            ("What is the largest lawn capacity at Taj Lands End?", "The Seaside Lawns can host up to 1,200 guests with open views of the Arabian Sea and Sea Link.")
        ]
    },
    {
        "slug": "ananda-in-the-himalayas-wedding",
        "name": "Ananda in the Himalayas",
        "city": "The Palace Estate, Narendra Nagar, Rishikesh",
        "state": "North",
        "tagline": "World-acclaimed wellness retreat in the Maharaja's Palace Estate overlooking the holy river Ganges and Himalayan mountains.",
        "capacity": "50 – 150 Guests",
        "rooms": "78 Palace Rooms, Suites & Himalayan Villas",
        "spaces": "Palace Courtyard (150 pax), Amphitheater (100 pax), Ridge Lawns (120 pax)",
        "pricing": "₹45,00,000 – ₹1.2 Crores / day buyout",
        "catering": "Gourmet Ayurvedic satvik menus, organic Himalayan dining, and international gourmet cuisine",
        "decor": "Sacred marigolds, brass bells, Himalayan cedar wood, and pure mountain elegance",
        "lead_time": "12 – 16 months",
        "hero_img": "images/15.jpg",
        "faqs": [
            ("What kind of wedding experience does Ananda in the Himalayas offer?", "A spiritual, ultra-exclusive wellness sanctuary wedding combining yoga, spa rejuvenation, and sacred Vedic ceremonies.")
        ]
    }
]

VENUE_TEMPLATE = """<!DOCTYPE html>
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
    <title>{name} Wedding Cost, Capacity & Planning Guide 2026 | Swariya Weddings</title>
    <meta name="description" content="{name} in {city}: Guest capacity ({capacity}), {rooms}, rental costs & decor rules. Plan your luxury celebration with 0% vendor markups.">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="https://swariyaweddings.com/venues/{slug}.html">

    <!-- Open Graph -->
    <meta property="og:title" content="{name} Wedding Guide | Swariya Weddings">
    <meta property="og:description" content="{tagline}">
    <meta property="og:url" content="https://swariyaweddings.com/venues/{slug}.html">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://swariyaweddings.com/{hero_img}">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../style.css?v=26">

    <!-- JSON-LD Schemas -->
    <script type="application/ld+json">
    {json_ld_schema}
    </script>

    <style>
        .venue-hero {{
            background: linear-gradient(180deg, rgba(10, 28, 24, 0.75) 0%, rgba(10, 28, 24, 0.9) 100%), url('../{hero_img}') center/cover no-repeat;
            color: #fff;
            padding: 110px 20px 70px;
            text-align: center;
        }}
        .venue-hero h1 {{
            font-size: clamp(2.2rem, 4.5vw, 3.2rem);
            color: #FAF6F0;
            margin-bottom: 12px;
            font-family: var(--font-heading);
        }}
        .venue-hero p.subtitle {{
            font-size: 1.1rem;
            max-width: 800px;
            margin: 0 auto 25px;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.6;
        }}
        .spec-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
            margin: 40px 0 60px;
        }}
        .spec-card {{
            background: #fff;
            border: 1px solid var(--border-gold);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        }}
        .spec-card h4 {{
            color: var(--primary);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }}
        .spec-card p {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--dark-luxury);
            margin: 0;
        }}
        .faq-card {{
            background: #fff;
            border: 1px solid var(--border-gold);
            border-radius: 10px;
            padding: 22px 26px;
            margin-bottom: 15px;
        }}
        .faq-card h3 {{
            font-size: 1.15rem;
            color: var(--dark-luxury);
            margin-bottom: 8px;
        }}
        .faq-card p {{
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
            <div class="logo"><a href="../index.html">SWARIYA</a></div>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="navLinks">&#9776;</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About us</a></li>
                <li><a href="../services.html">Our Services</a></li>
                <li><a href="../destination-wedding-planner-india.html">Destinations</a></li>
                <li><a href="../venues.html" class="active" style="color: var(--accent); font-weight: 500;">Our Venues</a></li>
                <li><a href="../client-portal.html">Wedding OS</a></li>
                <li><a href="../wedding-budget-calculator.html">Budget Tool</a></li>
                <li><a href="../wedding-brief-builder.html">Brief Builder</a></li>
                <li><a href="../reviews.html">Reviews</a></li>
                <li><a href="../contact.html" class="btn-contact">Contact us</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero -->
    <section class="venue-hero">
        <div class="container">
            <p class="section-label" style="color: var(--accent-light);">✦ CURATED LUXURY PROPERTY GUIDE • {city_upper}</p>
            <h1>{name}</h1>
            <p class="subtitle">{tagline}</p>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I'm%20interested%20in%20planning%20a%20wedding%20at%20{name_escaped}.%20Can%20we%20discuss%20date%20availability%20and%20costs?" class="btn-primary" style="background: linear-gradient(135deg, #D4AF37 0%, #AA820A 100%); color: #0A1C18; font-weight: 700; border: none; padding: 14px 28px; border-radius: 30px; text-decoration: none;" target="_blank" rel="noopener">Inquire on WhatsApp</a>
                <a href="../wedding-budget-calculator.html" style="background: transparent; border: 1.5px solid #fff; color: #fff; font-weight: 600; padding: 14px 26px; border-radius: 30px; text-decoration: none;">Calculate Budget</a>
            </div>
        </div>
    </section>

    <!-- Main Specs -->
    <main class="container" style="padding: 60px 0;">
        <h2 style="font-size: 1.8rem; color: var(--primary); text-align: center; margin-bottom: 10px;">Property Capacity & Specifications</h2>
        <p style="text-align: center; color: #666; max-width: 700px; margin: 0 auto;">Verified 2026 venue metrics and operational parameters for planning at {name}.</p>

        <div class="spec-grid">
            <div class="spec-card">
                <h4>👥 Guest Capacity</h4>
                <p>{capacity}</p>
            </div>
            <div class="spec-card">
                <h4>🛏️ On-Site Accommodation</h4>
                <p>{rooms}</p>
            </div>
            <div class="spec-card">
                <h4>🏰 Available Event Spaces</h4>
                <p style="font-size: 0.95rem; font-weight: 500;">{spaces}</p>
            </div>
            <div class="spec-card">
                <h4>💰 Estimated Investment</h4>
                <p>{pricing}</p>
            </div>
        </div>

        <!-- The Swariya Advantage -->
        <div style="background: linear-gradient(180deg, #FAF6F0 0%, #F5EDE0 100%); border-radius: 14px; padding: 35px; border: 1px solid var(--border-gold); margin: 50px 0;">
            <h3 style="color: var(--primary); font-size: 1.6rem; margin-bottom: 12px;">The Swariya Fiduciary Advantage at {name}</h3>
            <p style="color: #444; line-height: 1.7; font-size: 1.02rem;">
                Swariya Weddings manages your celebration at {name} with an unbending <strong>0% vendor markup guarantee</strong>. You contract and pay property tariffs, room blocks, catering, and sound setup directly with 100% transparent trade pricing while our in-house directors manage 3D spatial design, stage fabrication, and day-of Muhurtham run-sheets.
            </p>
        </div>

        <!-- FAQs -->
        <div style="margin-top: 50px;">
            <p class="section-label">✦ FREQUENTLY ASKED QUESTIONS</p>
            <h2 style="font-size: 1.8rem; color: var(--dark-luxury); margin-bottom: 25px;">Planning at {name}</h2>
            {faq_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="site-footer" style="margin-top: 80px;">
        <div class="container footer-content">
            <div class="footer-col">
                <a href="../index.html" class="footer-logo">Swariya <span>Weddings</span></a>
                <p>Pan-India Luxury & Destination Wedding Planners. Headquartered in Bengaluru with nationwide execution across Goa, Rajasthan, Kerala, Coorg & beyond. 150+ weddings planned with zero vendor markups.</p>
                <p style="margin-top: 10px; font-size: 0.85rem; color: #888;">📍 Atelier: HSR Layout, Bengaluru | 📞 +91 80505 73382</p>
            </div>
            <div class="footer-col">
                <h4>Venue Directory</h4>
                <ul>
                    <li><a href="../venues.html">All Wedding Venues</a></li>
                    <li><a href="../destination-wedding-planner-india.html">Destination Hubs</a></li>
                    <li><a href="../venue-finder.html">Venue Comparator Tool</a></li>
                    <li><a href="../bengaluru-wedding-cost-guide-2026.html">2026 Cost Benchmarks</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Planning Tools</h4>
                <ul>
                    <li><a href="../wedding-budget-calculator.html">Budget Calculator</a></li>
                    <li><a href="../wedding-brief-builder.html">Brief Builder</a></li>
                    <li><a href="../client-portal.html">Wedding OS</a></li>
                    <li><a href="../reviews.html">Verified Reviews</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Swariya Weddings. All Rights Reserved. • <a href="../sitemap.xml">Sitemap</a></p>
        </div>
    </footer>
    <script src="../nav.js"></script>
</body>
</html>
"""

def generate():
    os.makedirs("venues", exist_ok=True)
    print(f"Generating Phase 2: {len(DESTINATION_VENUES)} Dedicated Luxury Venue Guides...")
    generated_urls = []

    for v in DESTINATION_VENUES:
        slug = v["slug"]
        name = v["name"]
        city = v["city"]
        state = v["state"]
        tagline = v["tagline"]
        capacity = v["capacity"]
        rooms = v["rooms"]
        spaces = v["spaces"]
        pricing = v["pricing"]
        hero_img = v["hero_img"]
        city_upper = city.upper()
        name_escaped = name.replace(" ", "%20")

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
            <h3>{q}</h3>
            <p>{a}</p>
        </div>""" for q, a in v["faqs"]])

        json_ld_schema = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "EventVenue",
                    "@id": f"https://swariyaweddings.com/venues/{slug}.html#venue",
                    "name": f"{name} - Wedding Venue",
                    "description": tagline,
                    "url": f"https://swariyaweddings.com/venues/{slug}.html",
                    "address": {
                        "@type": "PostalAddress",
                        "addressLocality": city.split(",")[0].strip(),
                        "addressRegion": state,
                        "addressCountry": "IN"
                    },
                    "maximumAttendeeCapacity": capacity.split("–")[-1].replace("Guests", "").strip() if "–" in capacity else "500",
                    "priceRange": pricing
                },
                {
                    "@type": "FAQPage",
                    "@id": f"https://swariyaweddings.com/venues/{slug}.html#faq",
                    "mainEntity": faqs_schema
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"https://swariyaweddings.com/venues/{slug}.html#breadcrumb",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://swariyaweddings.com/"},
                        {"@type": "ListItem", "position": 2, "name": "Venues", "item": "https://swariyaweddings.com/venues.html"},
                        {"@type": "ListItem", "position": 3, "name": name, "item": f"https://swariyaweddings.com/venues/{slug}.html"}
                    ]
                }
            ]
        }, indent=2)

        rendered = VENUE_TEMPLATE.format(
            slug=slug,
            name=name,
            city=city,
            state=state,
            city_upper=city_upper,
            tagline=tagline,
            capacity=capacity,
            rooms=rooms,
            spaces=spaces,
            pricing=pricing,
            hero_img=hero_img,
            name_escaped=name_escaped,
            faq_html=faq_html,
            json_ld_schema=json_ld_schema
        )

        filepath = os.path.join("venues", f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(rendered)

        generated_urls.append(f"https://swariyaweddings.com/venues/{slug}.html")
        print(f"  -> Generated: {filepath}")

    # Update sitemap.xml
    print("\nUpdating sitemap.xml with new venue pages...")
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
    <priority>0.85</priority>
  </url>""")

    if new_entries:
        insert_point = "</urlset>"
        updated_sitemap = sitemap_content.replace(insert_point, "\n".join(new_entries) + "\n" + insert_point)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(updated_sitemap)
        print(f"Added {len(new_entries)} venue URLs to sitemap.xml")

    # Update llms.txt
    print("\nUpdating llms.txt...")
    with open("llms.txt", "r", encoding="utf-8") as f:
        llms_content = f.read()

    llms_entries = []
    for v in DESTINATION_VENUES:
        link_str = f"- [{v['name']}](https://swariyaweddings.com/venues/{v['slug']}.html): {v['capacity']} in {v['city']}. {v['tagline']}"
        if v['slug'] not in llms_content:
            llms_entries.append(link_str)

    if llms_entries:
        with open("llms.txt", "a", encoding="utf-8") as f:
            f.write("\n\n## Phase 2 Luxury Destination Venue Guides\n" + "\n".join(llms_entries) + "\n")
        print(f"Added {len(llms_entries)} venue entries to llms.txt")

    print(f"\n🎉 PHASE 2 COMPLETE! Successfully generated {len(DESTINATION_VENUES)} dedicated luxury venue guides.")

if __name__ == "__main__":
    generate()
