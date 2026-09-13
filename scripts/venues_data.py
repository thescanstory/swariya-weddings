import os
import json

VENUES_DATA = [
    {
        "slug": "wiwaha-wedding-venue-bangalore",
        "name": "Wiwaha Wedding Venue",
        "location": "Yelahanka, North Bengaluru",
        "tagline": "A premier modern-traditional wedding destination blending manicured open lawns with an expansive climate-controlled banquet hall in North Bengaluru.",
        "capacity": "150 – 1,500 Guests",
        "rooms": "32 Deluxe Guest Rooms",
        "spaces": "Main Lawn (1,200 capacity), Grand AC Hall (800 capacity), Dining Mandap (450 seated)",
        "pricing": "₹3,50,000 – ₹7,50,000 / day rental",
        "catering": "Flexible outside catering allowed with state-of-the-art live kitchen infrastructure",
        "decor": "Open decor policy with pre-approved fabrication guidelines",
        "lead_time": "8 – 14 months for prime Muhurtham dates",
        "faqs": [
            ("What is the guest capacity at Wiwaha Wedding Venue?", "Wiwaha comfortably accommodates celebrations from 150 guests for intimate pre-wedding functions up to 1,500 guests for grand wedding receptions across its combined lawns and air-conditioned hall."),
            ("How many rooms are available for bridal parties and guests?", "Wiwaha features 32 fully air-conditioned deluxe guest rooms and 2 dedicated luxury bridal dressing suites on-site."),
            ("What is Swariya Weddings' role at Wiwaha?", "Swariya Weddings provides end-to-end wedding planning at Wiwaha, including customized floral mandap design, stage production, sound/lighting, guest transport from Kempegowda Airport, and complete ritual timeline management.")
        ]
    },
    {
        "slug": "samavana-wedding-venue-bangalore",
        "name": "Samavana",
        "location": "Hesaraghatta, Bengaluru",
        "tagline": "An organic, heritage-infused sanctuary nestled among lush green groves for sustainable, earthy, and culturally rooted celebrations.",
        "capacity": "200 – 1,000 Guests",
        "rooms": "18 Eco-Luxury Cottages",
        "spaces": "Sacred Grove Lawn, Central Courtyard, Banyan Tree Amphitheater",
        "pricing": "₹2,75,000 – ₹5,50,000 / day rental",
        "catering": "Specializes in traditional South Indian banana leaf Oota and bespoke artisanal catering",
        "decor": "Eco-friendly, brass, terracotta, and botanical floral installations encouraged",
        "lead_time": "6 – 12 months in advance",
        "faqs": [
            ("What makes Samavana unique for Bangalore weddings?", "Samavana offers an untouched natural setting with ancient trees, rustic stone pathways, and open-air courtyards, ideal for serene daytime muhurthams and sunset receptions."),
            ("Is outside catering permitted at Samavana?", "Yes, Samavana permits curated outside catering teams and provides dedicated preparation and dining zones suitable for traditional satvik and multi-course feasts."),
            ("How does Swariya Weddings plan ceremonies at Samavana?", "Swariya designs bespoke natural floral setups, brass lamp illumination, sound engineering for outdoor acoustic clarity, and seamless shuttle transport from the city center.")
        ]
    },
    {
        "slug": "tharavadu-mane-bangalore",
        "name": "Tharavadu Mane",
        "location": "Kanakapura Road, Bengaluru",
        "tagline": "Authentic Kerala-style sloping tile architecture, wooden pillars, and intimate courtyards for soulfully traditional weddings.",
        "capacity": "100 – 600 Guests",
        "rooms": "14 Heritage Rooms & Suites",
        "spaces": "Nadumuttam Central Courtyard, Coconut Grove Lawn, Traditional Oottupura Dining Hall",
        "pricing": "₹2,00,000 – ₹4,50,000 / day rental",
        "catering": "Outside catering permitted; perfect for Sadya, Chettinad, and traditional South Indian spreads",
        "decor": "Brass urulis, marigold canopies, temple-inspired mandaps, and deepam lighting",
        "lead_time": "6 – 10 months",
        "faqs": [
            ("What wedding styles suit Tharavadu Mane best?", "Tharavadu Mane is ideal for intimate South Indian, Kerala Nair/Christian, and traditional Kannada weddings seeking authentic heritage aesthetics."),
            ("Can music and live instruments be played outdoors?", "Yes, traditional Chenda Melam, Nadaswaram, and acoustic classical ensembles are welcome in the courtyard and grove areas."),
            ("Why hire Swariya Weddings for Tharavadu Mane?", "Swariya coordinates authentic temple floral styling, heritage lighting, priest coordination, and guest hospitality to elevate the venue's antique charm.")
        ]
    },
    {
        "slug": "miraya-greens-bangalore",
        "name": "Miraya Greens",
        "location": "Electronic City / Sakalavara, Bengaluru",
        "tagline": "A sprawling contemporary oasis combining high-ceiling glass ballrooms with pristine manicured lawns for modern luxury weddings.",
        "capacity": "250 – 1,500 Guests",
        "rooms": "24 Designer Suites",
        "spaces": "The Glass House, Magnolia Lawn, Palm Courtyard, Poolside Deck",
        "pricing": "₹4,00,000 – ₹8,00,000 / day rental",
        "catering": "In-house & outside catering options available with multi-cuisine banqueting",
        "decor": "Contemporary floral installations, fairy light canopies, and architectural lighting",
        "lead_time": "9 – 15 months",
        "faqs": [
            ("What are the primary event areas at Miraya Greens?", "Miraya Greens features 'The Glass House' banquet hall for climate-controlled celebrations, alongside the grand 'Magnolia Lawn' and tropical poolside for Sangeet and cocktail parties."),
            ("How many guests can stay on-site?", "The property includes 24 premium boutique suites capable of housing 60–80 close family members and bridal entourage."),
            ("How does Swariya Weddings manage weddings at Miraya Greens?", "Swariya handles full-scale lighting and trussing inside The Glass House, luxury mandap styling on the lawn, sound curation, and multi-day hospitality.")
        ]
    },
    {
        "slug": "templetree-leisure-bangalore",
        "name": "TempleTree Leisure",
        "location": "Bellandur / Sarjapur Road, Bengaluru",
        "tagline": "An eco-luxe urban sanctuary featuring open-to-sky thatched pavilions, natural stone water bodies, and Balinese tranquility.",
        "capacity": "150 – 800 Guests",
        "rooms": "12 Luxury Cottages",
        "spaces": "Open-Air Thatched Pavilion, Central Lawn, Frangipani Water Courtyard",
        "pricing": "₹3,00,000 – ₹6,00,000 / day rental",
        "catering": "Outside catering allowed; dedicated commercial kitchen area",
        "decor": "Boho-chic, Balinese tropical, and traditional South Indian floral fusion",
        "lead_time": "8 – 12 months",
        "faqs": [
            ("Where is TempleTree Leisure located?", "TempleTree Leisure is centrally positioned near Bellandur and Outer Ring Road, making it highly accessible for Bangalore tech-corridor guests."),
            ("Is alcohol allowed for Sangeet or Cocktail functions?", "Yes, alcohol can be served with appropriate temporary event licensing, which Swariya Weddings arranges."),
            ("What planning services does Swariya provide at TempleTree Leisure?", "Swariya transforms the organic pavilions with bespoke illumination, hanging floral chandeliers, sound balance, and full day-of ceremony management.")
        ]
    },
    {
        "slug": "royalton-leisure-bangalore",
        "name": "Royalton Leisure",
        "location": "Bannerghatta Road, Bengaluru",
        "tagline": "A picturesque landscape of natural granite rock formations, lush cascading lawns, and majestic poolside celebration spaces.",
        "capacity": "200 – 1,200 Guests",
        "rooms": "20 AC Rooms & Cottages",
        "spaces": "Rock Amphitheater, The Grand Poolside Lawn, AC Banquet Pavilion",
        "pricing": "₹2,50,000 – ₹5,50,000 / day rental",
        "catering": "Open outside catering policy with extensive buffet preparation areas",
        "decor": "Dramatic rock-uplighting, mandap water-reflections, and floral pathways",
        "lead_time": "6 – 12 months",
        "faqs": [
            ("What is the highlight of Royalton Leisure?", "The natural granite rock formations provide a breathtaking, majestic backdrop for evening pheras, cocktail receptions, and pre-wedding shoots."),
            ("Are fireworks and special effects permitted?", "Cold pyros, dry ice fog, and controlled low-smoke effects are permitted with prior clearance managed by Swariya Weddings."),
            ("What is Swariya Weddings' coordination package for Royalton Leisure?", "Swariya provides full spatial design, lighting across the granite formations, power backup management, catering oversight, and guest flow coordination.")
        ]
    },
    {
        "slug": "gayatri-vihar-palace-grounds",
        "name": "Gayatri Vihar (Palace Grounds)",
        "location": "Palace Grounds, Jayamahal, Bengaluru",
        "tagline": "The royal benchmark for grand-scale luxury celebrations with pillarless banquet architecture in Bengaluru's most iconic royal corridor.",
        "capacity": "500 – 3,500 Guests",
        "rooms": "6 VIP Green Rooms & Bridal Suites",
        "spaces": "Pillarless Main Royal Hall, Sprawling Outer Exhibition Lawn, Dining Enclosure",
        "pricing": "₹6,00,000 – ₹15,00,000 / day rental",
        "catering": "Outside royal catering permitted with industrial-scale banquet kitchens",
        "decor": "Monumental royal stages, thematic palace facades, crystal chandeliers",
        "lead_time": "9 – 18 months for peak wedding dates",
        "faqs": [
            ("What size weddings is Gayatri Vihar designed for?", "Gayatri Vihar is engineered for mid-to-grand scale celebrations, easily hosting 500 to 3,500+ attendees with extensive valet parking for 1,000+ vehicles."),
            ("How does Swariya Weddings manage large-scale logistics at Palace Grounds?", "Swariya deploys a dedicated 25+ member production crew for crowd flow, security, VVIP protocol, multi-buffet catering logistics, and sound zoning."),
            ("Can heavy thematic sets and trusses be erected?", "Yes, the pillarless high-ceiling structure is fully capable of heavy trussing, LED walls, and intricate palace mandap set builds.")
        ]
    },
    {
        "slug": "itc-gardenia-bengaluru",
        "name": "ITC Gardenia",
        "location": "Residency Road, Central Bengaluru",
        "tagline": "Five-star LEED Platinum luxury hotel featuring the majestic Mysuru Hall and manicured rooftop terraces in the heart of the city.",
        "capacity": "100 – 500 Guests",
        "rooms": "292 Luxury Rooms & Presidential Suites",
        "spaces": "Mysuru Hall Ballroom, Plumeria Lawn, Botania Rooftop Garden",
        "pricing": "₹3,500 – ₹6,500 + taxes per guest package",
        "catering": "Exclusive gourmet banquet masterclasses by ITC’s award-winning culinary team",
        "decor": "Understated 5-star elegance, customized imported florals, and crystal accents",
        "lead_time": "6 – 12 months",
        "faqs": [
            ("What is the culinary standard at ITC Gardenia?", "ITC Gardenia is globally celebrated for its culinary expertise, offering customized North Indian, traditional South Indian, Pan-Asian, and European banquet spreads."),
            ("Can pre-wedding ceremonies take place on the outdoor terrace?", "Yes, the Botania and Plumeria terrace gardens are ideal for chic Mehendi, Cocktail, and intimate Phera ceremonies under the stars."),
            ("How does Swariya Weddings collaborate with ITC Gardenia?", "Swariya handles 5-star vendor clearance, ballroom acoustic transformation, bridal suite coordination, and guest concierge services.")
        ]
    },
    {
        "slug": "jw-marriott-bengaluru",
        "name": "JW Marriott Hotel Bengaluru",
        "location": "Vittal Mallya Road, Bengaluru",
        "tagline": "Ultra-luxury hospitality overlooking Cubbon Park with soaring ballrooms, poolside cabanas, and opulent urban sophistication.",
        "capacity": "150 – 600 Guests",
        "rooms": "281 Luxury Rooms & Suites",
        "spaces": "Grand Ballroom (5,000 sq ft), Outdoor Poolside Deck, JW Lawns",
        "pricing": "₹3,800 – ₹7,000 + taxes per guest package",
        "catering": "Signature JW banquet menus, live interactive stations, and bespoke confectionery",
        "decor": "Modern luxury design, ceiling floral canopies, immersive LED lighting",
        "lead_time": "8 – 14 months",
        "faqs": [
            ("Why choose JW Marriott for a luxury Bangalore wedding?", "JW Marriott provides premier central city prestige, proximity to UB City, world-class guest accommodation, and a pillarless ballroom with direct street access."),
            ("Are outdoor cocktail parties possible?", "Yes, the poolside deck with private cabanas and overlooking greenery offers an exquisite setting for high-energy Sangeet or Welcome parties."),
            ("What value does Swariya Weddings add at JW Marriott?", "Swariya orchestrates precision decor fabrication adhering strictly to hotel standards, celebrity artist coordination, and frictionless room-block management.")
        ]
    },
    {
        "slug": "shankaraa-foundation-bangalore",
        "name": "Shankaraa Foundation",
        "location": "Kanakapura Road, Bengaluru",
        "tagline": "An artistic and cultural sanctuary featuring clay amphitheaters, handcrafted stone sculptures, and terracotta courtyards.",
        "capacity": "100 – 500 Guests",
        "rooms": "10 Eco-Dressing Suites & Guest Cottages",
        "spaces": "Open-Air Amphitheater, Mandap Courtyard, Artisan Grove",
        "pricing": "₹2,00,000 – ₹4,00,000 / day rental",
        "catering": "Outside catering welcome; perfect for satvik, traditional Karnataka and South Indian feasts",
        "decor": "Terracotta lamps, raw silk drapes, marigold torans, and temple bells",
        "lead_time": "5 – 10 months",
        "faqs": [
            ("What type of weddings are celebrated at Shankaraa Foundation?", "Couples looking for soulful, culturally rich, artisanal, and heritage-inspired weddings with zero commercial feel love Shankaraa."),
            ("Is classical music and cultural performance allowed?", "Yes, the acoustically designed amphitheater is built specifically for classical Indian music, Nadaswaram, and dance performances."),
            ("How does Swariya Weddings design at Shankaraa Foundation?", "Swariya blends minimal natural aesthetics with heritage brass props, clay deepams, and authentic ritual management to honor the venue's spiritual vibe.")
        ]
    },
    {
        "slug": "jade-735-bangalore",
        "name": "Jade 735",
        "location": "Near International Airport, Devanahalli",
        "tagline": "A boutique private pool retreat designed for ultra-stylish intimate weddings, pool parties, and bespoke luxury gatherings.",
        "capacity": "50 – 250 Guests",
        "rooms": "Chalet Suites & Gazebo Bedrooms (up to 30 staying guests)",
        "spaces": "Floating Pool Pavilion, Bamboo Grove Deck, Lower Lounge Lawn",
        "pricing": "₹3,00,000 – ₹6,00,000 / buyout per day",
        "catering": "Curated artisanal catering & private chef experiences permitted",
        "decor": "Fairy light canopies, floating pool mandap, boho chic lounge decor",
        "lead_time": "4 – 8 months",
        "faqs": [
            ("What makes Jade 735 ideal for destination weddings in Bangalore?", "Jade 735 offers complete private property buyouts just 15 minutes from Kempegowda Airport, ideal for intimate 2-day destination weddings."),
            ("Can we host a pool party Sangeet at Jade 735?", "Yes, the illuminated floating pavilion over the private pool is one of Bangalore's most sought-after party backdrops."),
            ("How does Swariya Weddings style weddings at Jade 735?", "Swariya creates chic, intimate micro-wedding setups with ambient bistro lighting, live acoustic musicians, mixologist bars, and personalized guest gifts.")
        ]
    },
    {
        "slug": "gitanjali-wedding-venue-bangalore",
        "name": "Gitanjali Farm",
        "location": "Hennur / Bagalur Road, Bengaluru",
        "tagline": "A serene 5-acre rustic farm surrounded by mango trees, blooming bougainvillea, and open skies for romantic outdoor nuptials.",
        "capacity": "150 – 800 Guests",
        "rooms": "12 Rustic Air-Conditioned Rooms",
        "spaces": "Mango Orchard Lawn, Rustic Covered Pavilion, Poolside Lawn",
        "pricing": "₹2,50,000 – ₹5,00,000 / day rental",
        "catering": "Open outside catering policy with spacious preparation yards",
        "decor": "Farmhouse rustic, macrame accents, sunflower & marigold styling",
        "lead_time": "6 – 12 months",
        "faqs": [
            ("What is the ambiance at Gitanjali Farm?", "Gitanjali Farm offers a relaxed, nature-centric countryside atmosphere with vast open green lawns and flowering trees."),
            ("Is there parking space available for large guest counts?", "Yes, Gitanjali provides on-site secured parking for over 200 cars with valet management arranged by Swariya Weddings."),
            ("Why choose Swariya Weddings for Gitanjali Farm?", "Swariya manages complete lawn illumination, weather-contingency covered structures, sound balancing, and high-standard catering coordination.")
        ]
    },
    {
        "slug": "white-mist-bangalore",
        "name": "White Mist by Happy Retreats",
        "location": "Foot of Nandi Hills, Bengaluru",
        "tagline": "A picturesque mountain-view getaway venue offering tranquil valley breezes, modern villas, and breathtaking sunset ceremonies.",
        "capacity": "100 – 500 Guests",
        "rooms": "16 Luxury Cottages & Villa Suites",
        "spaces": "Valley View Lawn, Central Pool Amphitheater, Glass Banquet Deck",
        "pricing": "₹3,50,000 – ₹7,00,000 / buyout per day",
        "catering": "Flexible in-house and curated partner catering options",
        "decor": "Pastel florals, pampas grass installations, mountain-silhouette mandaps",
        "lead_time": "6 – 12 months",
        "faqs": [
            ("What is the biggest highlight of White Mist?", "The sweeping views of the Nandi Hills range provide an iconic natural backdrop for daytime muhurthams and sunset pheras."),
            ("Can guests stay on the property?", "Yes, up to 50–60 close family and friends can be comfortably accommodated in the on-site luxury cottages."),
            ("How does Swariya Weddings plan destination weddings at White Mist?", "Swariya arranges end-to-end airport transfers, scenic floral mandaps, evening DJ/Sangeet setups, and mountain-side dining experiences.")
        ]
    },
    {
        "slug": "area-83-bangalore",
        "name": "Area 83",
        "location": "Bannerghatta, Bengaluru",
        "tagline": "An expansive luxury adventure resort surrounded by private lakes, wooden chalets, and sprawling emerald lawns.",
        "capacity": "150 – 1,000 Guests",
        "rooms": "22 Luxury Chalets & Lakeside Suites",
        "spaces": "The Lakefront Lawn, Grand Covered Pavilion, Island Mandap Deck",
        "pricing": "₹3,50,000 – ₹7,50,000 / day rental",
        "catering": "In-house culinary packages and approved outside catering",
        "decor": "Lakeside lighting, floating lanterns, floral arches, and bohemian lounges",
        "lead_time": "7 – 12 months",
        "faqs": [
            ("What wedding experiences are popular at Area 83?", "Area 83 is renowned for experiential weddings featuring lakeside mandaps, boat entries for couples, and fun pre-wedding adventure activities for guests."),
            ("How are weather contingencies handled at Area 83?", "Area 83 has expansive weatherproof covered pavilions alongside its open lawns, ensuring rainproof celebrations year-round."),
            ("What role does Swariya Weddings play at Area 83?", "Swariya orchestrates unique bridal boat entries, customized lakefront lighting, guest activity itineraries, and multi-cuisine banqueting.")
        ]
    },
    {
        "slug": "royal-palms-bangalore",
        "name": "Royal Palms",
        "location": "Electronic City, Bengaluru",
        "tagline": "Vibrant palm-fringed lawns and spacious covered dining areas offering high-capacity elegance in South Bengaluru.",
        "capacity": "200 – 1,200 Guests",
        "rooms": "15 Air-Conditioned Rooms",
        "spaces": "Palm Grove Lawn, Royal Covered Hall, Dining Hall",
        "pricing": "₹2,50,000 – ₹5,00,000 / day rental",
        "catering": "Outside catering permitted; well-equipped kitchen spaces",
        "decor": "Grand floral stages, traditional temple mandap, and modern LED arches",
        "lead_time": "6 – 12 months",
        "faqs": [
            ("Where is Royal Palms located?", "Royal Palms is conveniently situated in Electronic City, making it easily accessible for families across South Bengaluru and Hosur corridor."),
            ("What are the catering options at Royal Palms?", "Royal Palms allows families to bring their preferred caterers, with separate dedicated cooking areas for pure vegetarian kitchens."),
            ("How does Swariya Weddings coordinate at Royal Palms?", "Swariya provides complete venue decor styling, electrical and lighting infrastructure, stage production, and guest ushering.")
        ]
    },
    {
        "slug": "moongate-bangalore",
        "name": "The Moongate",
        "location": "International Airport Road, Bengaluru",
        "tagline": "A majestic 10-acre private lakefront venue featuring water amphitheaters, lush lawns, and state-of-the-art event architecture.",
        "capacity": "300 – 2,000 Guests",
        "rooms": "30 Boutique Guest Rooms & Villa Suites",
        "spaces": "Waterfront Amphitheater, Grand Central Lawn, Climate-Controlled Banquet Hall",
        "pricing": "₹5,00,000 – ₹12,00,000 / day rental",
        "catering": "Approved premium outside caterers allowed with commercial staging kitchens",
        "decor": "Illuminated water pathways, mega floating mandaps, grand fairy light canopies",
        "lead_time": "9 – 16 months for peak season",
        "faqs": [
            ("What makes The Moongate a top luxury venue in Bangalore?", "The Moongate features a stunning private lake with an integrated stepped amphitheater, creating an unmatched stage for grand Indian weddings."),
            ("How close is The Moongate to Bangalore Airport?", "It is situated right on the International Airport Road, just 20 minutes from Kempegowda International Airport."),
            ("Why choose Swariya Weddings for The Moongate?", "Swariya specializes in large-scale floral architecture, lakefront sound mapping, high-tech stage production, and luxury NRI guest hospitality at Moongate.")
        ]
    },
    {
        "slug": "windflower-prakruthi-bangalore",
        "name": "The Windflower Prakruthi Resort",
        "location": "Devanahalli, Bengaluru",
        "tagline": "A 7-acre luxury garden resort blending lush tropical greenery with full-service destination wedding hospitality.",
        "capacity": "200 – 1,000 Guests",
        "rooms": "49 Luxury Rooms, Cottages & Villas",
        "spaces": "Prakruthi Lawn, Poolside Amphitheater, Banquet Hall",
        "pricing": "₹3,50,000 – ₹8,00,000 / day buyout packages",
        "catering": "In-house gourmet multi-cuisine banqueting & custom menus",
        "decor": "Eco-chic floral decor, pastel drapery, and romantic tree lighting",
        "lead_time": "8 – 14 months",
        "faqs": [
            ("How many residential wedding guests can Windflower Prakruthi host?", "With 49 rooms and private villas, the resort comfortably accommodates 120–150 residential wedding guests on a private buyout basis."),
            ("Can multiple ceremonies take place across different lawns?", "Yes, you can host Haldi by the pool, Mehendi on the garden lawns, Muhurtham in the central grove, and Reception at the main hall."),
            ("How does Swariya Weddings manage events at Windflower Prakruthi?", "Swariya handles multi-day ceremony scheduling, room hampers, customized theme decor across 4 distinct zones, and seamless vendor coordination.")
        ]
    },
    {
        "slug": "goldfinch-retreat-bangalore",
        "name": "Goldfinch Retreat",
        "location": "New Airport Road, Tarabanahalli, Bengaluru",
        "tagline": "A serene 4-star resort retreat featuring manicured event lawns, sparkling pools, and effortless proximity to the airport.",
        "capacity": "150 – 800 Guests",
        "rooms": "36 Elegant Deluxe Rooms & Suites",
        "spaces": "The Retreat Lawn, Poolside Deck, Silver Banquet Hall",
        "pricing": "₹2,50,000 – ₹6,00,000 / day rental & package",
        "catering": "Exquisite in-house catering with customizable vegetarian & non-vegetarian menus",
        "decor": "Modern elegant floral backdrops, LED trusses, and pathway illumination",
        "lead_time": "6 – 12 months",
        "faqs": [
            ("Is Goldfinch Retreat suitable for out-of-town wedding guests?", "Yes, its proximity to Bangalore Airport (15 mins) makes it a preferred hub for destination weddings with traveling relatives."),
            ("What is the capacity of the Silver Banquet Hall?", "The indoor hall accommodates up to 250 guests in theater style and connects directly to the open lawns for buffet dining."),
            ("What does Swariya Weddings provide at Goldfinch Retreat?", "Swariya provides complete theme execution, sound & DJ management, photography team coordination, and dedicated bridal assistants.")
        ]
    },
    {
        "slug": "signature-club-resort-bangalore",
        "name": "Signature Club Resort",
        "location": "Brigade Orchards, Devanahalli, Bengaluru",
        "tagline": "An elite country club resort within a 130-acre smart township offering neoclassical architecture and refined hospitality.",
        "capacity": "100 – 600 Guests",
        "rooms": "45 Boutique Rooms & Luxury 4-BHK Villas",
        "spaces": "The Grand Ballroom, Signature Lawn, Jasmine Courtyard, Terrace Lounge",
        "pricing": "₹3,50,000 – ₹7,50,000 / day package",
        "catering": "Signature culinary catering by Brigade Hospitality with custom menus",
        "decor": "Neoclassical floral pillars, crystal light canopies, modern luxury mandaps",
        "lead_time": "7 – 14 months",
        "faqs": [
            ("What sets Signature Club Resort apart?", "The tranquil, gated 130-acre township setting with neoclassical architecture, green avenues, and premium villa stays provides unmatched privacy."),
            ("Can separate villas be booked for groom and bride families?", "Yes, the luxury 4-BHK on-site villas provide dedicated private homes for both families with private lawns."),
            ("How does Swariya Weddings plan weddings at Signature Club Resort?", "Swariya oversees bespoke mandap design, villa hospitality, golf-cart guest shuttles, and luxury lighting across the grounds.")
        ]
    },
    {
        "slug": "shilhaandara-resort-ramnagara",
        "name": "Shilhaandara Resort",
        "location": "Ramanagara (Bangalore-Mysore Highway)",
        "tagline": "An extraordinary monolithic rock resort offering dramatic cave architecture, heritage tranquility, and unforgettable destination weddings.",
        "capacity": "150 – 800 Guests",
        "rooms": "30 Rock Suites, Cottages & Tents",
        "spaces": "The Rock Amphitheater, Soumya Lawn, Cave Banquet Hall",
        "pricing": "₹2,50,000 – ₹6,00,000 / day rental & buyout",
        "catering": "Traditional Karnataka & South Indian banquet spreads + North Indian buffets",
        "decor": "Rustic granite illumination, brass deepam setups, marigold draping",
        "lead_time": "5 – 10 months",
        "faqs": [
            ("How far is Shilhaandara from Bangalore?", "Shilhaandara is located in Ramanagara, approximately 45–55 minutes via the Bangalore-Mysore Expressway."),
            ("Is Shilhaandara good for weekend destination weddings?", "Yes! Guests enjoy ziplining, swimming, and nature walks between traditional wedding ceremonies for a memorable mini-holiday."),
            ("How does Swariya Weddings manage destination logistics at Shilhaandara?", "Swariya coordinates luxury AC coach travel from Bengaluru, ambient rock lighting, sound amplification, and full priest/ritual management.")
        ]
    }
]

print(f"Loaded {len(VENUES_DATA)} new venues.")
