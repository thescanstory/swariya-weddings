import os
import json
import re

OUTPUT_DIR = "/Users/mac/Documents/swariya-weddings-complete-project"

# 1. Localities (50)
LOCALITIES = [
    ("HSR Layout", "hsr-layout", "South-East Bengaluru luxury tech hub & bespoke boutique enclave"),
    ("Indiranagar", "indiranagar", "100ft Road, Defence Colony & central contemporary wedding celebrations"),
    ("Koramangala", "koramangala", "Koramangala 3rd Block, 4th Block & 5th Block premium wedding setups"),
    ("Whitefield", "whitefield", "EPIP Zone, ITPL & prestige resort wedding venues"),
    ("Jayanagar", "jayanagar", "3rd Block, 4th Block traditional South Indian heritage weddings"),
    ("Sadashivanagar", "sadashivanagar", "Elite heritage corridor, luxury farmhouses & Palace Grounds proximity"),
    ("Malleshwaram", "malleshwaram", "Margosa Road, Sampige Road traditional Kannada rituals & heritage setups"),
    ("JP Nagar", "jp-nagar", "Phases 1 to 8, Mini Forest, luxury open lawn & banquet celebrations"),
    ("Electronic City", "electronic-city", "Phase 1 & Phase 2 modern IT corridor destination celebrations"),
    ("Hebbal", "hebbal", "Hebbal Lake, Bellary Road 5-star hotel & lakeview wedding enclaves"),
    ("Yelahanka", "yelahanka", "Old Town, New Town & resort belts along Doddaballapur Road"),
    ("Bellandur", "bellandur", "Outer Ring Road luxury convention centers & lakeside events"),
    ("Sarjapur Road", "sarjapur-road", "Carmelaram, Sompura gate open-air boutique lawn & villa weddings"),
    ("Marathahalli", "marathahalli", "ORR bridge corridor, central convention & banquet spaces"),
    ("Banashankari", "banashankari", "Stages 2, 3 & 6 traditional Brahmin, Gowda & Lingayat celebrations"),
    ("Basavanagudi", "basavanagudi", "Bull Temple Road heritage corridors, South Indian mandap styling"),
    ("Rajajinagar", "rajajinagar", "1st Block to 6th Block grand community wedding halls"),
    ("Frazer Town", "frazer-town", "Pulkeshi Nagar, Coles Park colonial church & banquet celebrations"),
    ("Benson Town", "benson-town", "Central Bengaluru vintage estates & bespoke intimate weddings"),
    ("Ulsoor", "ulsoor", "Ulsoor Lake, Kensington Road 5-star luxury lakefront weddings"),
    ("Richmond Town", "richmond-town", "Richmond Road, Langford Town elite heritage club weddings"),
    ("Lavelle Road", "lavelle-road", "UB City, Vittal Mallya Road ultra-luxury 5-star intimate affairs"),
    ("Cunningham Road", "cunningham-road", "High Ground, Ali Asker Road boutique corporate & elite weddings"),
    ("Vasanth Nagar", "vasanth-nagar", "Palace Road, Millers Road central 5-star ballroom celebrations"),
    ("Dollars Colony", "dollars-colony", "RMV 2nd Stage elite private villa & lawn celebrations"),
    ("RT Nagar", "rt-nagar", "Dinnur Main Road, Ganganagar central wedding venues"),
    ("Hennur", "hennur", "Hennur Bagalur Road, exotic open-air lawn & modern resort weddings"),
    ("Thanisandra", "thanisandra", "Manyata Tech Park corridor luxury hotel & lawn setups"),
    ("Sahakara Nagar", "sahakara-nagar", "North Bengaluru residential hub, premium hall celebrations"),
    ("Vidyaranyapura", "vidyaranyapura", "BEL Layout, green belt open lawn & traditional wedding setups"),
    ("Kanakapura Road", "kanakapura-road", "Art of Living corridor, expansive farmhouses & nature resort weddings"),
    ("Bannerghatta Road", "bannerghatta-road", "Jigani, Hulimavu luxury nature retreats & resort celebrations"),
    ("Mysore Road", "mysore-road", "Kengeri satellite corridor, mega convention grounds & royal setups"),
    ("Nagarbhavi", "nagarbhavi", "BDA Complex, outer ring road grand community wedding halls"),
    ("Vijayanagar", "vijayanagar", "RPC Layout, Club Road traditional grand celebrations"),
    ("Kalyan Nagar", "kalyan-nagar", "HRBR Layout, CMR Road contemporary boutique wedding events"),
    ("Kammanahalli", "kammanahalli", "Cosmopolitan North-East Bengaluru intimate & banquet weddings"),
    ("HRBR Layout", "hrbr-layout", "1st to 3rd Block serene residential wedding & reception setups"),
    ("Kasturi Nagar", "kasturi-nagar", "East Bengaluru connectivity corridor, modern banquet celebrations"),
    ("CV Raman Nagar", "cv-raman-nagar", "DRDO Township, BEML Layout boutique garden wedding events"),
    ("Mahadevapura", "mahadevapura", "Outer Ring Road IT hub contemporary wedding celebrations"),
    ("Kadugodi", "kadugodi", "Whitefield extension, expansive resort & farm venues"),
    ("Hoodi", "hoodi", "ITPL Main Road banquet & open-air lawn weddings"),
    ("Brookefield", "brookefield", "Kundalahalli, AECS Layout luxury boutique wedding setups"),
    ("AECS Layout", "aecs-layout", "Marathahalli-Brookefield junction banquet & lawn weddings"),
    ("Domlur", "domlur", "Embassy GolfLinks, Intermediate Ring Road 5-star ballroom weddings"),
    ("HAL", "hal", "Old Airport Road, heritage club & manicured lawn weddings"),
    ("MG Road", "mg-road", "Central Bengaluru iconic 5-star hotels & heritage banquet halls"),
    ("Residency Road", "residency-road", "Brigade Road junction, historic club & luxury celebrations"),
    ("Devanahalli", "devanahalli", "Airport luxury resort belt, mega destination & palace weddings")
]

# 2. Venues (100)
VENUES = [
    ("The Tamarind Tree", "the-tamarind-tree", "Kanakapura Road", "Historic antique courtyards, cobblestone paths & pond pavilion"),
    ("Taj West End", "taj-west-end", "Race Course Road", "20-acre heritage botanical sanctuary, iconic tulip trees & Prince of Wales lawn"),
    ("The Leela Palace Bengaluru", "the-leela-palace", "Old Airport Road", "Vijayanagara royal architecture, grand ballrooms & cascading water fountains"),
    ("JW Marriott Prestige Golfshire", "jw-marriott-prestige-golfshire", "Nandi Hills", "275-acre golf resort, panoramic Nandi Hills backdrop & convention center"),
    ("ITC Gardenia", "itc-gardenia", "Residency Road", "Platinum LEED-certified luxury, Mysore Palace-inspired grand ballrooms"),
    ("ITC Windsor", "itc-windsor", "Sankey Road", "Regency-era British colonial architecture, glasshouse & manicured lawns"),
    ("Four Seasons Hotel Bengaluru", "four-seasons-hotel", "Embassy ONE, Bellary Road", "Grand Ballroom, private garden terrace & Michelin-grade culinary curation"),
    ("Shangri-La Bengaluru", "shangri-la-hotel", "Palace Road", "Panoramic city view ballrooms & luxury hospitality suites"),
    ("Conrad Bengaluru", "conrad-bengaluru", "Ulsoor Lake", "Lakeside infinity pool deck & 17-foot high ceiling Grand Ballroom"),
    ("Sheraton Grand Bangalore", "sheraton-grand-brigade-gateway", "Malleshwaram", "Brigade Gateway complex, skywalk access & versatile banquet halls"),
    ("The Ritz-Carlton Bangalore", "the-ritz-carlton", "Residency Road", "Jaali marble latticework, rooftop lantern terrace & Grand Ballroom"),
    ("TempleTree Leisure", "templetree-leisure", "Panathur, Outer Ring Road", "Eco-friendly Balinese architecture, thatched roofs & open lawns"),
    ("Miraya Greens", "miraya-greens", "Bannerghatta Road", "8-acre landscaped property, amphitheater & banquet halls"),
    ("The Groves", "the-groves", "Sarjapur Road", "Eucalyptus grove open-air sanctuary & rustic boho luxury setups"),
    ("Woodrose Club", "woodrose-club", "JP Nagar", "Award-winning landscaped greens, poolside lawn & amphitheater"),
    ("Royal Orchid Resort", "royal-orchid-resort", "Yelahanka", "8 acres of lush greens, convention pavilion & garden lawns"),
    ("Golden Palms Hotel & Spa", "golden-palams-resort", "Tumkur Road", "Moorish Mediterranean architecture & massive lagoon pool lawns"),
    ("Clarks Exotica Convention Resort", "clarks-exotica", "Devanahalli", "70-acre oasis, multi-tiered lawns & mega convention facilities"),
    ("Angsana Oasis Spa & Resort", "angsana-oasis-resort", "Doddaballapur Road", "Banyan tree amphitheater & holistic luxury resort lawns"),
    ("Goldfinch Retreat", "goldfinch-retreat", "Yelahanka", "Intimate poolside retreats & sprawling landscaped wedding grounds"),
    ("Jade 735", "jade-735", "Devanahalli", "Boutique private luxury party villa with pool, floating gazebo & chic cabanas"),
    ("Shibui", "shibui", "Nelamangala", "Japanese minimalist architectural estate, bamboo groves & tranquil water bodies"),
    ("Signature Club Resort", "signature-club-resort", "Brigade Orchards, Devanahalli", "Boutique villa lawns & heritage-inspired country club setups"),
    ("Gayatri Vihar", "gayatri-vihar-palace-grounds", "Palace Grounds", "Royal Rajasthani dome architecture, air-conditioned banquet & massive parking"),
    ("Kings Court", "kings-court-palace-grounds", "Palace Grounds", "Grand Roman imperial pillars, crystal chandeliers & 2,000+ capacity lawn"),
    ("Princess Shrine", "princess-shrine-palace-grounds", "Palace Grounds", "Majestic royal setup, air-conditioned hall & lush sprawling green lawns"),
    ("Sheesh Mahal", "sheesh-mahal-palace-grounds", "Palace Grounds", "Intricate mirror artwork, royal heritage ambiance & grand stage setups"),
    ("White Petals", "white-petals-palace-grounds", "Palace Grounds", "Contemporary glass facades, high ceilings & premier central exhibition/wedding hub"),
    ("Tripura Vasini", "tripura-vasini-palace-grounds", "Palace Grounds", "Massive open grounds capable of hosting 5,000+ royal banquet guests"),
    ("Gooty Vihar", "gooty-vihar-palace-grounds", "Palace Grounds", "Carved stone architecture, traditional mandap courtyards & dining pavilions"),
    ("Manpho Convention Centre", "manpho-convention-centre", "Manyata Tech Park Road", "Massive pillar-less convention halls & flexible multi-event complexes"),
    ("MLR Convention Centre JP Nagar", "mlr-convention-centre-jp-nagar", "JP Nagar 7th Phase", "State-of-the-art auditorium, dining hall & landscaped open courtyards"),
    ("MLR Convention Centre Whitefield", "mlr-convention-centre-whitefield", "Mahadevapura, Whitefield", "Award-winning acoustics, grand banquet floor & outdoor lawn"),
    ("Shankaraa Foundation", "shankaraa-foundation", "Kanakapura Road", "Cultural artistic sanctuary, stone amphitheater & heritage sculptures"),
    ("Radiant Resort", "radiant-resort", "Bannerghatta Road", "Forest-themed retreat, natural stone pathways & tranquil wedding lawns"),
    ("Guhantara Resort", "guhantara-resort", "Kanakapura Road", "India's first underground cave resort, rustic tribal decor & unique wedding spaces"),
    ("Windflower Prakruthi Resort", "windflower-prakruthi-resort", "Devanahalli", "7-acre lush green retreat, serene water bodies & open banquet lawns"),
    ("Eagleton Golf Resort", "eagleton-golf-resort", "Bidadi, Bangalore-Mysore Highway", "500-acre world-class golf course, multi-cuisine catering & grand ballrooms"),
    ("Palm Meadows Resort", "palm-meadows-resort", "Whitefield", "5-acre Victorian style luxury resort, palm-lined avenues & ballroom lawns"),
    ("Mango Mist Resort", "mango-mist-resort", "Bannerghatta Road", "Dense mango canopy gardens, rock waterfall backdrops & open-air sangeet setups"),
    ("The Oterra Hotel", "the-oterra-hotel", "Electronic City", "5-star luxury tech city ballroom, open infinity poolside & curated banqueting"),
    ("Hilton Bangalore Embassy GolfLinks", "hilton-embassy-golflinks", "Domlur", "Scenic golf course views, temperature-controlled poolside & grand ballroom"),
    ("Grand Mercure Bengaluru", "grand-mercure-koramangala", "Koramangala 3rd Block", "12th Main boutique central luxury, poolside courtyard & banquet facilities"),
    ("Courtyard by Marriott ORR", "courtyard-marriott-bellandur", "Outer Ring Road", "Contemporary IT corridor ballroom & bespoke culinary wedding services"),
    ("Aloft Bengaluru Cessna", "aloft-bengaluru-cessna", "Kadubeesanahalli", "Vibrant contemporary styling, splash pool deck & high-tech audio/visual ballrooms"),
    ("The Lalit Ashok Bangalore", "the-lalit-ashok", "Kumara Krupa High Grounds", "10-acre private gardens, poolside Kalinga hall & iconic central city address"),
    ("Taj Yeshwantpur", "taj-yeshwantpur", "Yeshwantpur", "Modern linear design, high-ceiling ballrooms & expansive wedding dining floor"),
    ("Vivanta Bengaluru Whitefield", "vivanta-whitefield", "ITPL, Whitefield", "Iconic futuristic architecture, open atrium lawns & ballroom banquets"),
    ("Vivanta Bengaluru Residency Road", "vivanta-residency-road", "Residency Road", "Central heritage luxury, private banquet hall & premier catering"),
    ("Moongate Events Venue", "moongate-events-venue", "International Airport Road", "10-acre private lakefront venue, amphitheater & glasshouse mandap pavilion"),
    ("The Conservatory", "the-conservatory-bangalore", "Kanakapura Road", "Glass greenhouse venue surrounded by tropical flora & bespoke dining courtyard"),
    ("Chancery Pavilion", "the-chancery-pavilion", "Residency Road", "Grand Sigma Ballroom, pool terrace & central Bangalore luxury wedding spaces"),
    ("Fortune Park JP Celestial", "fortune-park-jp-celestial", "Race Course Road", "Central luxury banquet halls & intimate rooftop cocktail venues"),
    ("Ramee Guestline Hotel", "ramee-guestline-hotel", "Attibele, Hosur Road", "5.5-acre landscaped resort, expansive open lawns & banquet facilities"),
    ("The Grand Magrath Hotel", "grand-magrath-hotel", "Magrath Road", "Central Bangalore classic ballrooms & curated South/North Indian banquets"),
    ("Radisson Blu Atria", "radisson-blu-atria", "Palace Road", "Sankey Tank corridor, contemporary ballrooms & high-end wedding dining"),
    ("St. Mark's Hotel", "st-marks-hotel", "St. Mark's Road", "Boutique luxury rooftop & intimate banquet spaces in the heart of CBD"),
    ("Hotel Royal Orchid Bangalore", "hotel-royal-orchid-old-airport", "Old Airport Road", "Adjoining KGA Golf Course, open rooftop & landscaped party lawns"),
    ("The Capitol Hotel", "the-capitol-hotel", "Raj Bhavan Road", "Central heritage vantage, Senator Ballroom & grand wedding feast arrangements"),
    ("Goldfinch Hotel Bangalore", "goldfinch-hotel-central", "Crescent Road", "High Grounds central banquet hall, silver leaf styling & specialty dining"),
    ("La Marvella", "la-marvella-hotel", "Jayanagar 2nd Block", "South Bangalore luxury boutique hotel, Aurum ballroom & vegetarian banquet excellence"),
    ("Citrine Hotel", "citrine-hotel", "Seshadripuram", "Central business banquet halls for intimate engagement & wedding ceremonies"),
    ("Pai Vista Convention Hall", "pai-vista-basavanagudi", "Basavanagudi", "Traditional South Indian wedding convention hall with dedicated dining floor"),
    ("Pai Resorts", "pai-resorts-yelahanka", "Yelahanka", "Quiet greenery, resort rooms for guest stay & open lawn wedding spaces"),
    ("Svenska Design Hotel", "svenska-design-hotel", "Electronic City", "Bespoke European design boutique hotel & intimate rooftop pool celebrations"),
    ("Keys Select Hotel Whitefield", "keys-select-whitefield", "ITPL Road", "Contemporary IT corridor banquet facilities for sangeet & intimate receptions"),
    ("Lemon Tree Premier Ulsoor", "lemon-tree-premier-ulsoor", "Ulsoor Lake", "Lakeside contemporary banquets & guest accommodations"),
    ("Attide Hotel", "attide-hotel", "Yelahanka, Bellary Road", "Airport expressway luxury banquet hall for pre-wedding & reception parties"),
    ("Evoma Hotel & Business Center", "evoma-hotel", "Old Madras Road, KR Puram", "Exotic Japanese garden, open lawn banquet & boutique stay"),
    ("Holiday Inn Bengaluru Racecourse", "holiday-inn-racecourse", "Race Course Road", "Direct Turf Club views, modern pillar-less ballroom & bespoke catering"),
    ("Holiday Inn Express Whitefield", "holiday-inn-express-whitefield", "ITPL Main Road", "Efficient guest room blocks & pre-wedding gathering halls"),
    ("Zone By The Park", "zone-by-the-park-infantry-road", "Infantry Road", "Modern chic vibrant decor & central Bangalore celebration suites"),
    ("Fairfield by Marriott Rajajinagar", "fairfield-marriott-rajajinagar", "Dr. Rajkumar Road", "Central West Bangalore luxury ballroom & Marriott culinary service"),
    ("Fairfield by Marriott Whitefield", "fairfield-marriott-whitefield", "Whitefield Main Road", "Modern banqueting floor for engagement, haldi & cocktail parties"),
    ("Courtyard by Marriott Hebbal", "courtyard-marriott-hebbal", "Nagavara, Hebbal", "Nagavara lake views, rooftop cocktail lounge & grand ballroom"),
    ("Four Points by Sheraton Whitefield", "four-points-sheraton-whitefield", "Whitefield", "Grand ballroom & dedicated open lawn for wedding pheras"),
    ("Mövenpick Hotel Bengaluru", "movenpick-hotel-hmt", "Gokula Extension, BEL Road", "Swiss hospitality, grand ballroom & pool deck sangeet celebrations"),
    ("Adarsh Palm Meadows Club", "adarsh-palm-meadows-club", "Ramagondanahalli, Whitefield", "Ultra-luxury gated community club, tranquil lakeside lawns & banquet hall"),
    ("Prestige Golfshire Club", "prestige-golfshire-club", "Nandi Hills Road", "Clubhouse terrace lawns overlooking 18-hole championship golf greens"),
    ("Country Club Devanahalli", "country-club-devanahalli", "Devanahalli", "Club lawns, poolside party deck & ample parking for grand gatherings"),
    ("Clarks Inn Airport Bangalore", "clarks-inn-airport-bangalore", "Devanahalli", "Convenient transit guest rooms & pre-wedding party hall"),
    ("The Paul Bangalore", "the-paul-bangalore", "Domlur", "Atrium courtyard, vintage Irish pub ambiance & luxury suite accommodations"),
    ("Sterlings MAC Hotel", "sterlings-mac-hotel", "Old Airport Road", "Indo-Asian architectural facade, grand ballroom & pure veg culinary setup"),
    ("Octave Hotel & Spa", "octave-hotel-sarjapur", "Sarjapur Road", "Contemporary banquet halls for sangeet, mehendi & intimate receptions"),
    ("Keys Hotel Hosur Road", "keys-hotel-hosur-road", "Singasandra", "South Bangalore connectivity, banquet halls & guest stay blocks"),
    ("Samskruthi Brindavan Convention", "samskruthi-brindavan", "JP Nagar 7th Phase", "Grand traditional South Indian wedding hall with massive dining hall"),
    ("Princess Green Palace Grounds", "princess-green-palace-grounds", "Palace Grounds Gate 9", "Sprawling grass lawns for open-air mandap setups & starry night receptions"),
    ("Nalapad Pavilion", "nalapad-pavilion-palace-grounds", "Palace Grounds", "High-capacity wedding hall with air conditioning & royal canopy decor"),
    ("Royal Palace Hall Palace Grounds", "royal-palace-hall-palace-grounds", "Palace Grounds Gate 6", "Classic palace ballroom structure with vast dining & stage setups"),
    ("Kalinga Hall at The Lalit Ashok", "kalinga-hall-lalit-ashok", "High Grounds", "One of Bengaluru's most iconic 5-star pillarless heritage ballrooms"),
    ("Grand Ball Room The Leela Palace", "grand-ball-room-leela-palace", "Old Airport Road", "Pure regal grandeur with gold leaf accents and hand-woven carpets"),
    ("Rasa Convention Centre", "rasa-convention-centre", "Kanakapura Road", "Architect-designed eco-heritage wedding hall with open central courtyards"),
    ("The Pergola", "the-pergola-rajankunte", "Rajanukunte, Doddaballapur Road", "Lush green tree-covered rustic lawn venue for aesthetic outdoor weddings"),
    ("Jayamahal Palace Hotel", "jayamahal-palace-hotel", "Jayamahal Road", "Historic 4-star palace hotel adjoining Palace Grounds with majestic gardens"),
    ("The Beginning", "the-beginning-sarjapur", "Sarjapur Road", "Curated open-air lawn venue with natural water body & minimalist pergolas"),
    ("Under The Mango Tree Venue", "under-the-mango-tree-bangalore", "Kanakapura Road", "Rustic organic farm wedding venue shaded by 50-year-old mango trees"),
    ("Vana Resort", "vana-resort-harohalli", "Kanakapura Road", "Ayurvedic sanctuary & eco-luxury resort lawns for wellness-oriented weddings"),
    ("Wildflower Hall Bangalore Venue", "wildflower-hall-bangalore", "Yelahanka Green Belt", "Bespoke floral wedding estate with manicured rose gardens & stone pavilions"),
    ("Samruddhi Convention Hall", "samruddhi-convention-hall", "Banashankari", "Modern multi-storey South Indian kalyana mantapa with high-speed elevators"),
    ("Shri Krishna Grand Convention", "shri-krishna-grand-convention", "Malleshwaram", "Heritage traditional Brahmin and vegetarian wedding destination hall")
]

# 3. Cultural & Community Weddings (80)
COMMUNITIES = [
    ("Kannada Brahmin Madhwa", "kannada-brahmin-madhwa", "Traditional Madhwa rituals: Nandi, Kashi Yatra, Vara Pooja, Kanyadaana, Dhareyeroyuvudu & Sapthapadi"),
    ("Kannada Brahmin Smartha", "kannada-brahmin-smartha", "Vedic chanting, Havans, Okhli games & strict Madi pure vegetarian catering"),
    ("Kannada Vokkaliga Gowda", "kannada-vokkaliga-gowda", "Grand Gowda rituals: Chappara Pooja, Bale Shastra, Kashi Yatra & grand Non-Veg/Veg feast"),
    ("Kannada Lingayat Veerashaiva", "kannada-lingayat-veerashaiva", "Ishtalinga Pooja, Vibhuti Dharana, Mangalashtaka & pure sattvic feast"),
    ("Kannada Reddy", "kannada-reddy", "Grand Reddy wedding rituals: Pradhanam, Kanyadaanam, Talambralu & royal floral mandap"),
    ("Mangalorean Bunt (Buntara Vivaha)", "mangalorean-bunt", "Groom arrival with traditional Korambu, Dhare Havani, Kanya Daana & coastal feast"),
    ("Mangalorean Catholic", "mangalorean-catholic", "Roce ceremony, Church nuptials, Latin hymns, Bridal March & Grand Reception Waltz"),
    ("Coorg Kodava Traditional", "coorg-kodava", "Baalopaat, Ganga Pooja, Kakkada, Kupya Chele attire & traditional Kodava Pork/Pandi curation"),
    ("Telugu Arya Vysya", "telugu-arya-vysya", "Pellikuthuru, Snathakam, Jeelakarra Bellam, Madhuparkam & authentic Telugu vegetarian feast"),
    ("Telugu Kamma Naidu", "telugu-kamma-naidu", "Grand Pelli, Kashi Yatra, Mangalasutram, Talambralu & grand royal orchestra"),
    ("Telugu Reddy Royal", "telugu-reddy-royal", "Royal palace decor, traditional Sannai Melam, Talambralu showers & 7-course feast"),
    ("Tamil Brahmin Iyer", "tamil-brahmin-iyer", "Vratham, Janavasam in vintage car, Oonjal swing ritual, Kanyadaanam & Saptapadi"),
    ("Tamil Brahmin Iyengar", "tamil-brahmin-iyengar", "Nadaswaram maestro live, Sambandhi Virundhu, Oonjal & traditional silk Madisar tying"),
    ("Tamil Chettiar (Nagarathar)", "tamil-chettiar-nagarathar", "Chettinad antique brass vilakku, Mahruthali, Pattumani & 16-dish Chettinad feast"),
    ("Kerala Nair", "kerala-nair", "Dakshina, Pudavamuri, Thalikettu in front of Nilavilakku & traditional Sadya on plantain leaf"),
    ("Kerala Christian (Syrian / Catholic)", "kerala-christian-syrian", "Manthrakodi presentation, Minnu tying, Chantham Charthu & grand reception choir"),
    ("Gujarati Jain Shwetambar", "gujarati-jain-shwetambar", "Mameru, Grand Garba Night, Hasta Melap, Jain chauvihar strictly before sunset"),
    ("Gujarati Jain Digambar", "gujarati-jain-digambar", "Vedic Jinendra Pooja, Mangal Pheras & pure jain root-free culinary banquet"),
    ("Marwari Maheshwari", "marwari-maheshwari", "Mudda Teeka, Sangeet & Dhol beats, Royal Baraat on elephant/vintage car, Pheras & Bidaai"),
    ("Marwari Agarwal", "marwari-agarwal", "Chunri ceremony, grand Bollywood sangeet production, Toran tying & midnight royal pheras"),
    ("Marwari Oswal", "marwari-oswal", "Traditional Jain Marwari customs, grand silver cutlery dining & bespoke floral decor"),
    ("Punjabi Sikh (Anand Karaj)", "punjabi-sikh-anand-karaj", "Gurdwara Anand Karaj with 4 Laavaan, Jaggo night, Dholis & grand Tandoori reception"),
    ("Punjabi Hindu", "punjabi-hindu", "Roka, Chunni, Chooda & Kaleerein ceremony, lively Sangeet & open-bar cocktail party"),
    ("Bengali Traditional", "bengali-traditional", "Subho Drishti, Saat Paake Ghomar, Mala Badal, Sindoor Daan & Kolkata style grand feast"),
    ("Sindhi Traditional", "sindhi-traditional", "Santh, Ghari Pooja, Navgraha Pooja, Jaimala & traditional Sindhi curry banquet"),
    ("Odia Royal Temple", "odia-royal-temple", "Nirbandha, Jayee Anukolo, Baad Dharan, Kanya Daan & authentic Chhena Poda sweets"),
    ("Assamese Biya", "assamese-biya", "Juran ceremony, Tel Diya, Pani Tula, traditional Mekhela Chador styling & feast"),
    ("Bihari Traditional Shadi", "bihari-traditional-shadi", "Tilak, Mandachhad, Kanya Daan, Kohbar painting setup & authentic Bihari feast"),
    ("Kashmiri Pandit", "kashmiri-pandit", "Livun, Wanvun folk songs, Devgon, Lagan & traditional 7-course vegetarian Wazwan"),
    ("Parsi Navjote & Lagan", "parsi-lagan", "Achu Michu ritual, Varadh-Patra, White Parsi Gara sari styling & traditional Patra Ni Machhi"),
    ("Interfaith Hindu-Christian Fusion", "interfaith-hindu-christian-fusion", "Dual ceremony: Morning Church Nuptials & Evening Vedic Mandap with seamless transitions"),
    ("Interfaith North-South Indian Fusion", "interfaith-north-south-fusion", "Combining lively Punjabi Dhol Sangeet with serene South Indian Temple Vedic Pheras"),
    ("Arya Samaj Vedic", "arya-samaj-vedic", "Simple noble Vedic Hawan, Gayatri Mantra chanting, 0% pomp, focused pure holy rituals"),
    ("Eco-Friendly Zero Waste", "eco-friendly-zero-waste", "Seed paper invites, upcycled brass decor, composting all food waste & solar lighting"),
    ("Intimate 50-Guest Luxury Micro-Wedding", "intimate-50-guest-micro-wedding", "Ultra-curated private villa buyout, personalized 5-course chef table & acoustic live trio"),
    ("100-Guest Boutique Garden Wedding", "100-guest-boutique-garden", "Bespoke glasshouse styling, fairy light canopy & farm-to-table culinary curation"),
    ("500-Guest Royal Grand Wedding", "500-guest-royal-grand", "Full turnkey production: 360-degree LED staging, celebrity artists & mega dining halls"),
    ("1000-Guest Mega Palace Grounds Wedding", "1000-guest-mega-palace-grounds", "Palace Grounds mega pavilion, 20-acre parking management & multi-regional buffet setups"),
    ("Kannada Devanga Traditional", "kannada-devanga", "Chowki Pooja, Godhuli Lagna wedding pheras & traditional silk saree draping"),
    ("Kannada Billava Traditional", "kannada-billava", "Coastal Karnataka rituals, Tulunadu deity blessings & authentic coastal delicacies"),
    ("Kannada Kuruba Traditional", "kannada-kuruba", "Vedic canopy setup, traditional haldi bath rituals & authentic regional feast"),
    ("Kannada Korama Traditional", "kannada-korama", "Sacred grove decor, ancestral blessings & vibrant community celebrations"),
    ("Kannada Vishwakarma Traditional", "kannada-vishwakarma", "Sacred fire altar, silver/gold bridal crowns & ancient Vedic rituals"),
    ("Kannada Ganiga Traditional", "kannada-ganiga", "Traditional lamp lighting, turmeric paste application & temple rituals"),
    ("Kannada Tigala Traditional", "kannada-tigala", "Draupadi Karaga tradition inspired grand floral artwork & vibrant processions"),
    ("Kannada Namadhari Naika", "kannada-namadhari-naika", "North Canara coastal rituals, betel leaf exchange & traditional village feast"),
    ("Kannada Bhavasar Kshatriya", "kannada-bhavasar-kshatriya", "Royal Kshatriya insignia, Haldi Chandan ceremony & traditional festive feast"),
    ("Telugu Balija Naidu", "telugu-balija-naidu", "Royal Gajalu bangle ceremony, Pradhanam & grand floral stage mandap"),
    ("Telugu Velama Royal", "telugu-velama-royal", "Aristocratic heritage setup, traditional shehnai & elaborate multi-dish banquet"),
    ("Telugu Kapu Grand", "telugu-kapu-grand", "Pellikoduku ceremony, grand reception entrance & authentic coastal Andhra dishes"),
    ("Telugu Brahmin Niyogi", "telugu-brahmin-niyogi", "Rig Vedic rituals, Upanyasam, Kashi Yatra & pristine sattvic catering"),
    ("Telugu Brahmin Vaidiki", "telugu-brahmin-vaidiki", "Yajur Vedic chanting, sacred Homam fire & grand traditional sweet spreads"),
    ("Tamil Mudaliar", "tamil-mudaliar", "Mappillai Azhaippu, Thali Dharanam & traditional banana leaf feast"),
    ("Tamil Pillai", "tamil-pillai", "Traditional temple bells, Jasmine floral chandeliers & grand classical Carnatic concert"),
    ("Tamil Gounder (Kongu Vellalar)", "tamil-gounder-kongu", "Porutham, Mangala Vazhthu singing by Arumaikaarar & traditional Kongu feast"),
    ("Tamil Nadar", "tamil-nadar", "Kalyana Malai exchange, Thali tying with gold coin & grand modern reception"),
    ("Tamil Vanniyar", "tamil-vanniyar", "Agni Kula Kshatriya traditions, sacred fire pradakshina & royal floral canopy"),
    ("Tamil Naicker", "tamil-naicker", "Royal Nayak dynasty inspired decor, flower shower talambralu & grand dinner"),
    ("Tamil Saurashtra Traditional", "tamil-saurashtra", "Silk weaver bridal patterns, Gujarati-Tamil cultural blend & feast"),
    ("Kerala Ezhava Traditional", "kerala-ezhava", "Guru Pooja, Garland exchange, Pudava Kodukkal & traditional Kerala feast"),
    ("Kerala Brahmin (Namboothiri)", "kerala-brahmin-namboothiri", "Veli ceremony, Kudiveppu, pure Vedic fire & authentic Palada Pradhaman"),
    ("Kerala Thiyya Traditional", "kerala-thiyya", "North Malabar coastal rituals, traditional silk mundu & coastal fish/veg banquet"),
    ("Kerala Knanaya Catholic", "kerala-knanaya-catholic", "Othukalyanam, Mylanchi Ideel, Baratham singing & Purathanam waltz"),
    ("Kerala Latin Catholic", "kerala-latin-catholic", "Traditional white gown cathedral nuptials, brass band & seaside reception"),
    ("Goan Hindu Saraswat", "goan-hindu-saraswat", "Simant Pooja, Kaan Pili, Oti Bharap & traditional Goan Saraswat feast"),
    ("Goan Catholic Heritage", "goan-catholic-heritage", "Portuguese villa courtyard setup, vintage car drive, violinists & multi-tier cake cutting"),
    ("Maharashtrian Brahmin Konkanastha", "maharashtrian-brahmin-konkanastha", "Sakharpuda, Kelvan, Mundavalya tying, Kanyadaan & authentic Ukdiche Modak"),
    ("Maharashtrian Brahmin Deshastha", "maharashtrian-brahmin-deshastha", "Vedic Lagna Vidhi, Sunmukh, Saptapadi & traditional Puran Poli feast"),
    ("Maharashtrian Maratha 96 Kuli", "maharashtrian-maratha-royal", "Peshwai pagdi, Tutari trumpets, grand royal sword entry & lavish feast"),
    ("Rajasthani Rajput Royal Sword", "rajasthani-rajput-royal", "Royal horse/elephant baraat, Aarti with royal thali, Pheras & Rajputana sword guard"),
    ("Rajasthani Jain Shwetambar", "rajasthani-jain-shwetambar", "Grand Sangeet night, Toran bandhan & strictly pure vegetarian Jain menu"),
    ("Gujarati Patel (Leva / Kadva)", "gujarati-patel", "Grand Dandiya Raas, Jaan arrival, Pokhwanu & 24-item Gujarati thali"),
    ("UP Brahmin Traditional", "up-brahmin-traditional", "Tilak, Dwar Pooja, Kanyadaan, Kohbar & Banarasi Paan counters"),
    ("UP Rajput Traditional", "up-rajput-traditional", "Royal elephant entry, Jai Mala stage fireworks & traditional Awadhi delicacies"),
    ("Haryanvi Traditional", "haryanvi-traditional", "Bhaat ceremony, grand Dhol Tasha baraat & authentic Haryanvi hospitality"),
    ("Himachali Pahadi Traditional", "himachali-pahadi-traditional", "Traditional Dhaam feast cooked by Botis, Pahadi topi groom styling & folk music"),
    ("Uttarakhandi Kumaoni / Garhwali", "uttarakhandi-pahadi", "Pichora dupatta bridal styling, Ganesh Pooja & authentic Garhwali sweet banquet"),
    ("Buddhism Inspired Zen", "buddhism-inspired-zen", "Chanting of Triple Gem, water blessing ceremony, minimalist lotus decor & tea station"),
    ("Sufi & Qawwali Sangeet Special", "sufi-qawwali-sangeet-special", "Live Nizami Brothers / Qawwal troupe, velvet lounge seating & royal Mughal lamps"),
    ("Retro Bollywood Themed Sangeet", "retro-bollywood-sangeet", "Filmfare-style red carpet, customized choreography & LED wall dance performances")
]

# 4. Budget & Guest Tiers (70)
BUDGETS = [
    ("Budget Under 5 Lakhs", "budget-under-5-lakhs", "Affordable intimate wedding packages with smart decor, photography & sound for 50-100 guests"),
    ("Budget 5 to 10 Lakhs", "budget-5-to-10-lakhs", "Mid-tier turnkey planning covering hall decor, priest, bridal makeup, photo/video & DJ setup"),
    ("Budget 10 to 15 Lakhs", "budget-10-to-15-lakhs", "Comprehensive 2-day wedding package with designer mandap, sound & light, drone coverage & coordination"),
    ("Budget 15 to 25 Lakhs", "budget-15-to-25-lakhs", "Premium celebrations with customized 3D decor concepts, live artist entertainment & full logistics"),
    ("Budget 25 to 50 Lakhs", "budget-25-to-50-lakhs", "Luxury multi-event wedding management with exotic florals, guest hospitality desk & celebrity anchors"),
    ("Budget 50 Lakhs to 1 Crore", "budget-50-lakhs-to-1-crore", "High-end luxury wedding production with imported florals, curated theme sets & 5-star venue management"),
    ("Ultra Luxury Above 1 Crore", "ultra-luxury-above-1-crore", "Royal bespoke celebrations with full venue buyouts, international artists, designer pavilions & custom staging"),
    ("Intimate 50 Guests Package", "intimate-50-guests-package", "Curated boutique private villa setup, bespoke table scaping, acoustic music & personalized favors"),
    ("Intimate 100 Guests Package", "intimate-100-guests-package", "Open lawn ceremony with fairy lighting, specialized live counters & complete decor"),
    ("Grand 200 Guests Package", "grand-200-guests-package", "Turnkey 2-day celebrations covering Mehendi, Sangeet, Muhurtham & Grand Reception"),
    ("Grand 300 Guests Package", "grand-300-guests-package", "Full banquet management, multiple catering live stations, photo booths & guest transfers"),
    ("Grand 500 Guests Package", "grand-500-guests-package", "Sprawling convention center coordination, 20+ member on-ground team & multi-camera livestream"),
    ("Mega 1000 Guests Package", "mega-1000-guests-package", "Palace Grounds mega production, multi-tiered food courts, VIP lounge & traffic management"),
    ("Mega 2000 Guests Royal Package", "mega-2000-guests-royal-package", "Massive logistical execution, multiple dining pavilions, grand royal entry & celebrity performers")
]

# 5. Services & Specialties (100)
SERVICES = [
    ("Turnkey Wedding Planning", "turnkey-wedding-planning", "End-to-end wedding execution from vendor contract negotiations to day-of timeline coordination"),
    ("3D Mandap & Decor Design", "3d-mandap-and-decor-design", "Photorealistic 3D renders before build, in-house fabrication & zero third-party decor markups"),
    ("Wedding Venue Selection & Booking", "wedding-venue-selection-and-booking", "Exclusive negotiated rates across 100+ Bangalore 5-star hotels, luxury resorts & heritage grounds"),
    ("Catering Curation & Menu Tasting", "catering-curation-and-menu-tasting", "Connecting with premier authentic regional caterers for South Indian, North Indian, Jain & Global cuisines"),
    ("Wedding Photography & Cinematic Film", "wedding-photography-and-cinematic-film", "Top candid wedding photographers, traditional videography, drone cinematography & same-day edits"),
    ("Bridal Makeup & Styling Coordination", "bridal-makeup-and-styling-coordination", "Top celebrity makeup artists, saree draping experts, mehendi artists & grooming packages"),
    ("Sangeet Choreography & Show Production", "sangeet-choreography-and-show-production", "Professional dance choreographers, interactive LED stages, intelligent lighting & pyrotechnics"),
    ("Guest Hospitality & Room Logistics", "guest-hospitality-and-room-logistics", "Airport pickup fleet, hotel check-in concierge desk, welcome hampers & 24/7 guest helpline"),
    ("Live Music, DJ & Celebrity Artists", "live-music-dj-and-celebrity-artists", "Renowned wedding DJs, Sufi singers, Carnatic fusion bands, Shehnai & Nadaswaram maestros"),
    ("Custom Wedding Invites & E-Invites", "custom-wedding-invites-and-e-invites", "Bespoke boxed physical invitations, WhatsApp video invitations & personalized wedding websites"),
    ("Vintage Car & Royal Baraat Entry", "vintage-car-and-royal-baraat-entry", "Vintage convertible cars, decorated elephants, royal horses, mobile DJ trucks & Dhol Tasha troupes"),
    ("Floral Jewelry & Varmala Styling", "floral-jewelry-and-varmala-styling", "Fresh exotic rose/orchid/lotus varmalas, traditional South Indian jada billalu & floral dupattas"),
    ("Priest & Vedic Pundit Coordination", "priest-and-vedic-pundit-coordination", "Experienced regional priests fluent in Kannada, Telugu, Tamil, Marathi, Hindi & Sanskrit Vedic mantras"),
    ("Cocktail Party & Bar Management", "cocktail-party-and-bar-management", "Licensed bartenders, flair mixology counters, custom bride & groom cocktails & glassware rental"),
    ("Haldi & Phoolon Ki Holi Setup", "haldi-and-phoolon-ki-holi-setup", "Marigold backdrop setups, brass urlis for couple seating, flower petal showers & dhol beats"),
    ("Mehendi Lounge & Bohemian Decor", "mehendi-lounge-and-bohemian-decor", "Teepee tents, colorful floor cushions, dreamcatchers, live bangle stalls & customized mehendi favors"),
    ("Wedding Favors & Return Gifts", "wedding-favors-and-return-gifts", "Curated artisanal sweets, eco-friendly potted plants, silver coins & personalized gift boxes"),
    ("Live Streaming & Virtual Guest Lounge", "live-streaming-and-virtual-guest-lounge", "Multi-camera 4K YouTube/Zoom live streams for NRI relatives and guests worldwide"),
    ("On-Day Master Checklist & Coordination", "on-day-master-checklist-and-coordination", "Shadow managers for bride, groom & parents to ensure 100% zero stress and timely ritual execution"),
    ("Post-Wedding Reception Planning", "post-wedding-reception-planning", "Glitz & glamour stage backdrops, cake cutting setups, formal dinner seating & guest photo ops")
]

# 6. Destination Getaways from Bangalore (100)
DESTINATIONS = [
    ("Coorg (Kodagu)", "coorg-kodagu", "Lush coffee plantation luxury resorts, misty mountain backdrops & Kodava cultural touch"),
    ("Chikmagalur", "chikmagalur", "Mullayanagiri hill retreats, sprawling tea/coffee estates & intimate luxury villas"),
    ("Kabini & Nagarhole", "kabini-nagarhole", "Lakeside safari lodges, riverfront mandap setups & tranquil nature serenity"),
    ("Sakleshpur", "sakleshpur", "Rolling green Western Ghats valleys, private waterfalls & eco-luxury resorts"),
    ("Mysore (Mysuru)", "mysore-palace-city", "Lalitha Mahal Palace, heritage royal courtyards & authentic Mysore silk heritage"),
    ("Hampi & Kamalapura", "hampi-heritage", "Vijayanagara royal palace ruins, stone temple heritage & ultra-luxe boutique stays"),
    ("Gokarna & Om Beach", "gokarna-coastal", "Secluded cliff-top mandaps, tranquil Arabian Sea sunsets & boho-chic beach weddings"),
    ("Bekal & North Kerala Coast", "bekal-kerala-coast", "Historic Bekal Fort, sprawling luxury beachfront resorts & backwater serenity"),
    ("Wayanad Rainforest", "wayanad-rainforest", "Lush valley mist, bamboo grove retreats & treehouse intimate pre-wedding getaways"),
    ("Ooty & Nilgiris", "ooty-nilgiris-hills", "Colonial heritage tea estate bungalows, botanical gardens & cool mountain air"),
    ("Goa Beachfront", "goa-beachfront", "Direct 1-hour flight from BLR: pristine South Goa white sand beaches & luxury 5-star resorts"),
    ("Mahabalipuram Coastal", "mahabalipuram-coastal", "Historic shore temple backdrop, 5-star Bay of Bengal beachfront lawns"),
    ("Pondicherry (Puducherry)", "pondicherry-french-quarter", "French colonial heritage villas, promenade beachfront & bohemian chic setups"),
    ("Bandipur National Park", "bandipur-safari-lodges", "Wilderness luxury resorts, open canopy starlit sangeets & rustic forest charm"),
    ("Dandeli Riverfront", "dandeli-kali-river", "Kali riverfront eco-resorts, adventure sangeets & lush jungle wedding backdrops")
]

print("Starting generation of 500 hyper-targeted Bangalore SEO landing pages...")

def generate_page(title, h1, meta_desc, slug, category, context_text, pricing_tier, faq_items, related_links):
    canonical_url = f"https://swariyaweddings.com/{slug}"
    
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
            } for item in faq_items
        ]
    }
    
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
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "12.9121",
            "longitude": "77.6446"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "500"
        }
    }

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
    <title>{title} | Swariya 4.9★</title>
    
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
        .service-hero {{ background: linear-gradient(135deg, #FAF7F2 0%, #F5EFEB 100%); padding: 60px 0 40px; border-bottom: 1px solid #EBE4D8; }}
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
        .related-tags {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }}
        .related-tags a {{ background: #FAF7F2; border: 1px solid #EBE4D8; color: #8B1A1A; padding: 6px 14px; border-radius: 20px; font-size: 13px; text-decoration: none; transition: 0.2s; }}
        .related-tags a:hover {{ background: #8B1A1A; color: #fff; }}
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
                <li><a href="/wedding-planners-in-bangalore">Bangalore Guide</a></li>
                <li><a href="/top-wedding-planners-in-bangalore-comparison">Compare Planners</a></li>
                <li><a href="/reviews">Reviews</a></li>
                <li><a href="/contact" class="btn-contact">Get Free Quote</a></li>
            </ul>
        </div>
    </nav>

    <header class="service-hero">
        <div class="container">
            <p class="section-label" style="color: #8B1A1A; font-weight: 600;">✦ {category.upper()} SPECIALISTS IN BENGALURU</p>
            <h1 style="font-family: 'Playfair Display', serif; font-size: 38px; color: #2C2C2C; margin: 12px 0 16px; line-height: 1.2;">{h1}</h1>
            <p style="font-size: 16px; color: #555; max-width: 800px; line-height: 1.7;">{context_text}</p>
            <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 24px;">
                <a href="#quote" class="btn-primary">Book Consultation Call</a>
                <a href="https://wa.me/918050573382?text=Hi%20Swariya%20Weddings,%20I%20am%20looking%20for%20{title.replace(' ', '%20')}" class="btn-primary" style="background: #25D366; border-color: #25D366;">WhatsApp Expert 💬</a>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Trust & Highlights Section -->
        <section class="content-box">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; text-align: center;">
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">0%</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Vendor Kickbacks or Hidden Markups</p>
                </div>
                <div>
                    <h3 style="font-size: 28px; color: #8B1A1A; margin-bottom: 4px;">4.9 ★</h3>
                    <p style="font-size: 13px; color: #666; font-weight: 500;">Rated by 500+ Couples in Bangalore</p>
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

        <!-- Pricing Breakdown -->
        <section style="margin: 40px 0;">
            <div style="text-align: center; margin-bottom: 30px;">
                <p class="section-label">✦ TRANSPARENT 2026 ESTIMATES</p>
                <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #2C2C2C;">Turnkey Planning & Decor Fee Tiers</h2>
                <p style="color: #666; max-width: 650px; margin: 8px auto 0;">All packages feature direct vendor billing, in-house decor production, and dedicated on-ground shadow managers.</p>
            </div>

            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>Day-Of Coordination</h3>
                    <div class="price">₹1.5 Lakhs <span style="font-size: 14px; font-weight: 400; color: #777;">/ 1-2 Days</span></div>
                    <ul>
                        <li>Full vendor timeline alignment</li>
                        <li>Shadow coordinators for Bride & Groom</li>
                        <li>Guest welcoming & seating management</li>
                        <li>Pooja samagri & priest coordination</li>
                        <li>Audio/Visual cues & DJ sync</li>
                    </ul>
                    <a href="#quote" class="btn-primary" style="display: block; text-align: center; font-size: 14px;">Select Plan</a>
                </div>

                <div class="pricing-card featured">
                    <h3>Complete Turnkey Management</h3>
                    <div class="price">₹3.5 - ₹6 Lakhs <span style="font-size: 14px; font-weight: 400; color: #777;">/ Multi-Day</span></div>
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
                {"".join([f'''<div class="faq-item">
                    <h4>{item["q"]} <span>+</span></h4>
                    <div class="faq-ans">{item["a"]}</div>
                </div>''' for item in faq_items])}
            </div>
        </section>

        <!-- Related Guides / Tags -->
        <section style="margin: 40px 0 60px;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 22px; color: #2C2C2C; margin-bottom: 12px;">Explore Related Bangalore Wedding Resources</h3>
            <div class="related-tags">
                {"".join([f'<a href="{link["url"]}">{link["title"]}</a>' for link in related_links])}
            </div>
        </section>

        <!-- Contact CTA -->
        <section id="quote" class="content-box" style="background: linear-gradient(135deg, #8B1A1A 0%, #5E0E0E 100%); color: #fff; text-align: center; padding: 45px 20px;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #D9B872; margin-bottom: 12px;">Plan Your Perfect Celebration with Swariya Weddings</h2>
            <p style="max-width: 600px; margin: 0 auto 24px; color: #F5EFEB; font-size: 15px;">Talk to our senior Bengaluru wedding directors today for a custom moodboard, 3D decor layout, and honest itemized cost breakdown.</p>
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
                <p>Premier luxury wedding planners in Bangalore. Registered office: HSR Layout Sector 2, Bengaluru, Karnataka 560102.</p>
                <p>Phone: +91 80505 73382 | Email: hello@swariyaweddings.com</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="/wedding-planners-in-bangalore">Bangalore Main Hub</a></li>
                    <li><a href="/top-wedding-planners-in-bangalore-comparison">Top 10 Planners Comparison</a></li>
                    <li><a href="/kannada-wedding-planner-bengaluru">Kannada Wedding Traditions</a></li>
                    <li><a href="/sitemap.html">Complete 500+ Directory</a></li>
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

# Track all created pages for sitemap
ALL_PAGES = []

# Generate 50 Localities
for name, slug, desc in LOCALITIES:
    page_slug = f"wedding-planners-in-{slug}-bangalore"
    title = f"Wedding Planners in {name} Bangalore"
    h1 = f"Luxury Wedding Planners in {name}, Bangalore"
    meta_desc = f"Looking for top wedding planners in {name} Bangalore? Swariya Weddings offers bespoke decor, 3D renders & 0% markup across {name} banquet halls."
    faqs = [
        {"q": f"What is the average cost of hiring a wedding planner in {name} Bangalore?", "a": f"Wedding planning fees in {name} typically range from ₹1.5L for day-of coordination to ₹3.5L–₹6L for full turnkey management with 0% vendor markups."},
        {"q": f"How early should we book our wedding venue and planner in {name}?", "a": f"Due to high demand during peak Muhurtham dates in Bengaluru, we recommend confirming your {name} planner and venue 6 to 9 months in advance."},
        {"q": f"Do you handle complete decor production in-house for {name} weddings?", "a": f"Yes! Swariya Weddings operates its own in-house fabrication and floral workshops, eliminating third-party rental markups for {name} couples."}
    ]
    related = [
        {"title": "Bangalore Master Planning Guide", "url": "/wedding-planners-in-bangalore.html"},
        {"title": "Compare Bangalore Planners", "url": "/top-wedding-planners-in-bangalore-comparison.html"},
        {"title": "HSR Layout Planners", "url": "/wedding-planners-in-hsr-layout-bangalore.html"},
        {"title": "Indiranagar Planners", "url": "/wedding-planners-in-indiranagar-bangalore.html"}
    ]
    html_content = generate_page(title, h1, meta_desc, page_slug, f"{name} Locality", desc, "₹3.5L - ₹6L", faqs, related)
    filepath = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    ALL_PAGES.append({"title": title, "slug": page_slug, "category": "Bangalore Localities"})

# Generate 100 Venues
for name, slug, locality, desc in VENUES:
    page_slug = f"wedding-planner-for-{slug}-bangalore"
    title = f"Wedding Planner for {name} Bangalore"
    h1 = f"Bespoke Wedding Planning & Decor at {name}, Bangalore"
    meta_desc = f"Planning your wedding at {name} ({locality})? Swariya Weddings delivers custom 3D decor, stage fabrication, sound logistics & 0% markups."
    faqs = [
        {"q": f"What are the venue rental and decor guidelines for {name}?", "a": f"{name} in {locality} requires specific structural load clearances and acoustic timings. Swariya Weddings manages all permissions and vendor logistics directly."},
        {"q": f"How much does turnkey decor cost for a wedding at {name}?", "a": f"Turnkey production at {name} generally ranges from ₹4L to ₹18L depending on guest count, floral densities, and custom mandap structures."},
        {"q": f"Can we bring our own catering and specialized chefs to {name}?", "a": f"We coordinate with {name}'s banquet management regarding kitchen access, live counter setups, and dietary compliance (pure veg, Jain, or global fusion)."}
    ]
    related = [
        {"title": f"Wedding Planners in {locality}", "url": "/wedding-planners-in-bangalore.html"},
        {"title": "Bangalore Venue Cost Guide 2026", "url": "/bengaluru-wedding-cost-guide-2026.html"},
        {"title": "Top Bangalore Planners Comparison", "url": "/top-wedding-planners-in-bangalore-comparison.html"},
        {"title": "Palace Grounds Weddings", "url": "/wedding-planner-for-gayatri-vihar-palace-grounds-bangalore.html"}
    ]
    html_content = generate_page(title, h1, meta_desc, page_slug, f"{name} Venue", desc, "₹4L - ₹10L", faqs, related)
    filepath = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    ALL_PAGES.append({"title": title, "slug": page_slug, "category": "Bangalore Venues"})

# Generate 80 Cultural & Community Traditions
for name, slug, desc in COMMUNITIES:
    page_slug = f"{slug}-wedding-planner-in-bangalore"
    title = f"{name} Wedding Planner in Bangalore"
    h1 = f"{name} Wedding Planning & Traditional Rituals in Bangalore"
    meta_desc = f"Expert {name} wedding planners in Bangalore. Complete ritual coordination, authentic priests, traditional mandap decor & 0% vendor markups."
    faqs = [
        {"q": f"How do you ensure authentic traditional customs for {name} weddings?", "a": f"We collaborate with revered community scholars, priests, and ritual coordinators who ensure every Vedic shloka, muhurtham timing, and ceremonial detail is observed flawlessly."},
        {"q": f"Do you arrange authentic regional catering for {name} celebrations?", "a": f"Yes, we connect couples with master traditional Maharajs and caterers specializing in authentic recipes, banana leaf dining, and satvik preparation."},
        {"q": f"Can you blend modern luxury decor with traditional {name} mandap aesthetics?", "a": f"Absolutely. We specialize in contemporary heritage designs using temple brass bells, traditional marigold/tuberoses, and subtle warm lighting."}
    ]
    related = [
        {"title": "Kannada Wedding Traditions", "url": "/kannada-wedding-planner-bengaluru.html"},
        {"title": "Tamil Brahmin Weddings", "url": "/brahmin-traditional-wedding-planner-bengaluru.html"},
        {"title": "Bangalore Planners Guide", "url": "/wedding-planners-in-bangalore.html"},
        {"title": "Compare Top Planners", "url": "/top-wedding-planners-in-bangalore-comparison.html"}
    ]
    html_content = generate_page(title, h1, meta_desc, page_slug, f"{name} Rituals", desc, "₹3L - ₹8L", faqs, related)
    filepath = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    ALL_PAGES.append({"title": title, "slug": page_slug, "category": "Cultural & Community Weddings"})

# Generate 70 Budget & Format Combinations
for b_name, b_slug, b_desc in BUDGETS:
    for loc_name, loc_slug, _ in LOCALITIES[:5]: # Top 5 localities x 14 budget tiers = 70
        page_slug = f"wedding-planner-bangalore-{b_slug}-{loc_slug}"
        title = f"{b_name} in {loc_name} Bangalore"
        h1 = f"{b_name} - Wedding Planning in {loc_name}, Bangalore"
        meta_desc = f"Planning a {b_name.lower()} in {loc_name} Bangalore? Get itemized transparent cost estimates, curated venues & 0% vendor markups with Swariya."
        faqs = [
            {"q": f"What is included in the {b_name.lower()} in {loc_name}?", "a": f"Our {b_name.lower()} covers venue management, customized decor styling, photography coordination, sound/DJ setups, and on-ground execution."},
            {"q": f"Are there any hidden charges or commission markups?", "a": f"Zero. Swariya operates on a transparent fiduciary model with direct-to-vendor billing and 0% markups."}
        ]
        related = [
            {"title": "Bangalore Wedding Budget Calculator", "url": "/wedding-budget-calculator.html"},
            {"title": "Bangalore Cost Guide 2026", "url": "/bengaluru-wedding-cost-guide-2026.html"},
            {"title": f"Wedding Planners in {loc_name}", "url": f"/wedding-planners-in-{loc_slug}-bangalore.html"}
        ]
        html_content = generate_page(title, h1, meta_desc, page_slug, f"Budget & Tiers ({loc_name})", b_desc, b_name, faqs, related)
        filepath = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        ALL_PAGES.append({"title": title, "slug": page_slug, "category": "Budget & Scale Guides"})

# Generate 100 Services x Locality Combinations
for s_name, s_slug, s_desc in SERVICES:
    for loc_name, loc_slug, _ in LOCALITIES[:5]: # 20 services x 5 top localities = 100
        page_slug = f"{s_slug}-in-{loc_slug}-bangalore"
        title = f"{s_name} in {loc_name} Bangalore"
        h1 = f"Luxury {s_name} in {loc_name}, Bangalore"
        meta_desc = f"Looking for professional {s_name.lower()} in {loc_name} Bangalore? Swariya Weddings delivers bespoke excellence with 0% vendor markups."
        faqs = [
            {"q": f"How does Swariya manage {s_name.lower()} in {loc_name}?", "a": f"We provide dedicated specialists and on-site directors ensuring meticulous execution, quality checks, and timely delivery."},
            {"q": f"Can we customize our requirements for {s_name.lower()}?", "a": f"Yes, every single element is customized to your personal aesthetic, wedding theme, and budget specifications."}
        ]
        related = [
            {"title": "Our Core Services", "url": "/services.html"},
            {"title": "Bangalore Main Guide", "url": "/wedding-planners-in-bangalore.html"},
            {"title": f"Planners in {loc_name}", "url": f"/wedding-planners-in-{loc_slug}-bangalore.html"}
        ]
        html_content = generate_page(title, h1, meta_desc, page_slug, f"Wedding Services ({loc_name})", s_desc, "Customized", faqs, related)
        filepath = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        ALL_PAGES.append({"title": title, "slug": page_slug, "category": "Specialized Services"})

# Generate 100 Destination Getaways from Bangalore
DEST_THEMES = [
    ("3-Day Luxury Package", "3-day-luxury-package", "Full 3-day weekend destination wedding with Welcome Dinner, Sangeet & Muhurtham"),
    ("Intimate Villa Buyout", "intimate-villa-buyout", "Exclusive private estate buyout for 50-100 close guests with personal chefs"),
    ("Heritage Royal Celebration", "heritage-royal-celebration", "Palace architecture, royal regal welcome & traditional cultural banquet"),
    ("Nature & Plantation Wedding", "nature-plantation-wedding", "Eco-chic coffee estate or forest lawn ceremony with acoustic starlit nights"),
    ("Beachfront Coastal Wedding", "beachfront-coastal-wedding", "Sunset beach mandap, barefoot cocktail party & seafood barbecue banquets"),
    ("Monsoon & Mountain Retreat", "monsoon-mountain-retreat", "Misty valley views, indoor glasshouse mandap & cozy bonfire sangeet"),
    ("Budget Destination Package", "budget-destination-package", "Smart luxury 100-guest destination package under ₹25 Lakhs from Bangalore")
]

for d_name, d_slug, d_desc in DESTINATIONS:
    for t_name, t_slug, t_desc in DEST_THEMES[:7]: # 15 destinations x 7 themes = 105 pages
        if len(ALL_PAGES) >= 505:
            break
        page_slug = f"destination-wedding-in-{d_slug}-{t_slug}-from-bangalore"
        title = f"{t_name} in {d_name} from Bangalore"
        h1 = f"{t_name} in {d_name} for Bangalore Couples"
        meta_desc = f"Planning a destination wedding in {d_name} from Bangalore? Swariya Weddings manages resort buyouts, travel logistics & 0% markups."
        faqs = [
            {"q": f"How do Bangalore guests travel to {d_name}?", "a": f"We coordinate complete fleet transfers, Volvo luxury coaches, or flight/train reception desks from Bengaluru directly to the resort."},
            {"q": f"How much does a destination wedding in {d_name} cost from Bangalore?", "a": f"A 2-to-3 day destination wedding in {d_name} typically ranges from ₹20L to ₹60L for 100-150 guests including stay, meals, and complete decor."},
            {"q": f"Do you send your Bangalore decor production team to {d_name}?", "a": f"Yes, Swariya dispatches our senior Bangalore design and technical crew to oversee 100% flawless setup and on-time execution."}
        ]
        related = [
            {"title": "Pan-India Destination Planners", "url": "/destination-wedding-planner-india.html"},
            {"title": "Bangalore Master Guide", "url": "/wedding-planners-in-bangalore.html"},
            {"title": "Coorg Wedding Guide", "url": "/coorg-destination-wedding-cost-guide-2026.html"},
            {"title": "Goa Destination Guide", "url": "/cost-of-destination-wedding-in-goa-2026.html"}
        ]
        html_content = generate_page(title, h1, meta_desc, page_slug, f"Destination from Bangalore ({d_name})", f"{d_desc} - {t_desc}", "₹20L - ₹50L", faqs, related)
        filepath = os.path.join(OUTPUT_DIR, f"{page_slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        ALL_PAGES.append({"title": title, "slug": page_slug, "category": "Destination Getaways from BLR"})

print(f"Successfully generated {len(ALL_PAGES)} targeted Bangalore landing pages!")

# 7. Create Dedicated XML Sub-Sitemap for the 500 Pages
sitemap_xml_path = os.path.join(OUTPUT_DIR, "sitemap-bangalore-500.xml")
sitemap_xml_content = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in ALL_PAGES:
    sitemap_xml_content.append(f'''  <url>
    <loc>https://swariyaweddings.com/{p["slug"]}</loc>
    <lastmod>2026-09-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>''')
sitemap_xml_content.append('</urlset>')


with open(sitemap_xml_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml_content))
print(f"Created XML Sub-Sitemap at {sitemap_xml_path} with {len(ALL_PAGES)} URLs.")

# 8. Update main sitemap.xml index
main_sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
with open(main_sitemap_path, "r", encoding="utf-8") as f:
    main_sitemap_content = f.read()

if "sitemap-bangalore-500.xml" not in main_sitemap_content:
    entry = """  <sitemap>
    <loc>https://swariyaweddings.com/sitemap-bangalore-500.xml</loc>
    <lastmod>2026-09-28</lastmod>
  </sitemap>
</sitemapindex>"""
    main_sitemap_content = main_sitemap_content.replace("</sitemapindex>", entry)
    with open(main_sitemap_path, "w", encoding="utf-8") as f:
        f.write(main_sitemap_content)
    print("Updated root sitemap.xml with sitemap-bangalore-500.xml index reference.")

# 9. Update sitemap.html with categorized links to prevent orphan status
sitemap_html_path = os.path.join(OUTPUT_DIR, "sitemap.html")
with open(sitemap_html_path, "r", encoding="utf-8") as f:
    sitemap_html = f.read()

# Group pages by category
categories = {}
for p in ALL_PAGES:
    cat = p["category"]
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(p)

category_cards = []
for cat_name, items in categories.items():
    list_items = "".join([f'<li><a href="/{item["slug"]}.html">{item["title"]}</a></li>\n' for item in items])
    card_html = f"""
            <div class="directory-card">
                <h2>{cat_name} (500 Cluster)</h2>
                <ul>
                    {list_items}
                </ul>
            </div>"""
    category_cards.append(card_html)

injected_cards = "\n".join(category_cards)
if '<div class="directory-grid">' in sitemap_html:
    sitemap_html = sitemap_html.replace('<div class="directory-grid">', f'<div class="directory-grid">\n{injected_cards}')
    with open(sitemap_html_path, "w", encoding="utf-8") as f:
        f.write(sitemap_html)
    print("Injected all 500+ URLs into sitemap.html master directory.")
