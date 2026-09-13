import os

# 1. VENUE FINDER TOOL (venue-finder.html)
venue_finder_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bengaluru Wedding Venue Finder & 3-Way Comparison Tool | Swariya Weddings</title>
    <meta name="description" content="Compare Bengaluru wedding venues side-by-side on guest capacity, room count, rental cost, catering rules and location with Swariya Weddings' interactive Venue Finder.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://swariyaweddings.com/venue-finder.html">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">

    <style>
        :root {
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
        }
        body { font-family: 'Plus Jakarta Sans', sans-serif; color: var(--text-main); background: var(--bg-light); line-height: 1.6; }
        h1, h2, h3 { font-family: 'Playfair Display', serif; color: var(--primary-dark); }
        .hero { padding: 130px 20px 50px; background: linear-gradient(135deg, #fdf0f4 0%, #fffbf2 100%); text-align: center; border-bottom: 1px solid #f0e2e7; }
        .hero h1 { font-size: 2.8rem; margin-bottom: 15px; }
        .hero p { font-size: 1.15rem; color: var(--text-muted); max-width: 800px; margin: 0 auto; }

        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        
        .tool-card { background: var(--white); border-radius: var(--border-radius); padding: 35px; box-shadow: var(--card-shadow); margin-top: 40px; border: 1px solid #f0eae5; }
        
        .selectors-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px; }
        @media (max-width: 850px) { .selectors-grid { grid-template-columns: 1fr; } }

        .selector-box { background: #fdfaf7; border: 2px solid #eedecf; border-radius: 8px; padding: 15px; }
        .selector-box label { display: block; font-weight: 700; color: var(--primary-dark); margin-bottom: 8px; }
        .selector-box select { width: 100%; padding: 12px; border-radius: 6px; border: 1px solid #ccc; font-size: 1rem; font-family: inherit; }

        .comparison-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .comparison-table th, .comparison-table td { padding: 16px; text-align: left; border: 1px solid #eedfdf; }
        .comparison-table th { background: var(--primary-light); color: var(--primary-dark); font-size: 1.05rem; }
        .comparison-table td { background: white; font-size: 0.95rem; }
        .comparison-table tr:hover td { background: #fffcf8; }
        .prop-col { font-weight: 700; color: #444; width: 22%; background: #faf4f0 !important; }

        .btn-wa-venue { display: inline-flex; align-items: center; gap: 8px; background: #25d366; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: 700; font-size: 0.9rem; }
    </style>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "Bengaluru Wedding Venue Finder & 3-Way Comparison Tool",
      "url": "https://swariyaweddings.com/venue-finder.html",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "All",
      "description": "Interactive tool to compare Bangalore wedding venues side-by-side on capacity, rooms, price, and catering rules."
    }
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
                <a href="venue-finder.html" class="nav-link active">Venue Finder</a>
                <a href="wedding-budget-calculator.html" class="nav-link">Calculator</a>
                <a href="wedding-brief-builder.html" class="nav-link">Brief Builder</a>
                <a href="contact.html" class="btn-primary">Book Consultation</a>
            </nav>
        </div>
    </header>

    <div class="hero">
        <div class="container">
            <h1>Bengaluru Wedding Venue Finder</h1>
            <p>Select any 3 venues across Bengaluru to compare guest capacities, room counts, rental rates, and catering policies side-by-side.</p>
        </div>
    </div>

    <main class="container">
        <div class="tool-card">
            <div class="selectors-grid">
                <div class="selector-box">
                    <label for="venue1">Select Venue #1</label>
                    <select id="venue1" onchange="renderComparison()">
                        <!-- Options injected by JS -->
                    </select>
                </div>
                <div class="selector-box">
                    <label for="venue2">Select Venue #2</label>
                    <select id="venue2" onchange="renderComparison()">
                        <!-- Options injected by JS -->
                    </select>
                </div>
                <div class="selector-box">
                    <label for="venue3">Select Venue #3</label>
                    <select id="venue3" onchange="renderComparison()">
                        <!-- Options injected by JS -->
                    </select>
                </div>
            </div>

            <div style="overflow-x: auto;">
                <table class="comparison-table" id="compTable">
                    <!-- Comparison rows injected by JS -->
                </table>
            </div>

            <div style="text-align: center; margin-top: 40px; padding: 25px; background: #fdf5f8; border-radius: 8px;">
                <h3 style="margin-bottom: 10px;">Need personalized venue inspections & consolidated quotes?</h3>
                <p style="color: #666; margin-bottom: 15px;">Swariya Weddings negotiates direct-to-venue pricing with zero hidden kickbacks.</p>
                <a href="https://wa.me/919606822204?text=Hi%20Swariya%20Weddings,%20I%20used%20your%20Venue%20Finder%20tool%20and%20would%20like%20to%20check%20availability%20for%20my%20dates." class="btn-wa-venue" target="_blank" rel="noopener">
                    💬 WhatsApp Swariya Venue Concierge
                </a>
            </div>
        </div>
    </main>

    <footer class="footer" style="background:#1a1a1a; color:#fff; padding:60px 0 30px; margin-top:80px;">
        <div class="container" style="text-align:center;">
            <p><strong>Swariya Weddings</strong> — Premier Wedding Planners in Bengaluru. 150+ Weddings | 500+ Happy Clients | 4.9/5 Rating.</p>
            <p style="font-size:0.9rem; color:#aaa;">© 2026 Swariya Weddings. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        const VENUES_DB = [
            { id: "tamarind", name: "The Tamarind Tree", location: "Kanakapura Rd", capacity: "150 – 1,000 Guests", rooms: "28 Heritage Villas", pricing: "₹4,50,000 – ₹9,00,000 / day", catering: "Outside catering allowed", style: "Heritage Rustic & Banyan Tree Lawns", link: "venues/the-tamarind-tree-bangalore.html" },
            { id: "leela", name: "The Leela Palace Bengaluru", location: "Old Airport Rd", capacity: "100 – 650 Guests", rooms: "357 5-Star Luxury Rooms", pricing: "₹4,000 – ₹7,500 / guest plate", catering: "In-house 5-Star Gourmet Banqueting", style: "Royal Vijayanagara Palace Ballroom", link: "venues/the-leela-palace-bengaluru.html" },
            { id: "taj_west_end", name: "Taj West End Bengaluru", location: "Race Course Rd", capacity: "150 – 800 Guests", rooms: "117 Heritage Luxury Rooms", pricing: "₹3,800 – ₹6,800 / guest plate", catering: "Taj In-House Luxury Banquets", style: "20-Acre Heritage Botanical Gardens", link: "venues/taj-west-end-bengaluru.html" },
            { id: "amita_rasa", name: "Amita Rasa", location: "Nandi Hills", capacity: "200 – 1,200 Guests", rooms: "22 Boutique Cottages", pricing: "₹3,75,000 – ₹7,50,000 / day", catering: "Outside catering permitted", style: "Open-Air Mountain Silhouette Amphitheater", link: "venues/amita-rasa-bangalore.html" },
            { id: "grape_garden", name: "The Grape Garden", location: "Kanakapura Rd", capacity: "100 – 500 Guests", rooms: "8 Rustic Cottages", pricing: "₹1,80,000 – ₹3,50,000 / day", catering: "Outside catering permitted", style: "Organic Vineyard & Countryside Farm", link: "venues/the-grape-garden-bangalore.html" },
            { id: "wiwaha", name: "Wiwaha Wedding Venue", location: "Yelahanka", capacity: "150 – 1,500 Guests", rooms: "32 Deluxe AC Rooms", pricing: "₹3,50,000 – ₹7,50,000 / day", catering: "Outside catering permitted", style: "Grand Modern AC Hall & Manicured Lawn", link: "venues/wiwaha-wedding-venue-bangalore.html" },
            { id: "gayatri_vihar", name: "Gayatri Vihar Palace Grounds", location: "Palace Grounds", capacity: "500 – 3,500 Guests", rooms: "6 VIP Green Suites", pricing: "₹6,00,000 – ₹15,00,000 / day", catering: "Outside royal catering permitted", style: "Iconic Royal Pillarless Grand Pavilion", link: "venues/gayatri-vihar-palace-grounds.html" },
            { id: "miraya_greens", name: "Miraya Greens", location: "Electronic City", capacity: "250 – 1,500 Guests", rooms: "24 Designer Suites", pricing: "₹4,00,000 – ₹8,00,000 / day", catering: "In-house & Outside catering", style: "Modern Glasshouse & Sprawling Lawn", link: "venues/miraya-greens-bangalore.html" },
            { id: "templetree", name: "TempleTree Leisure", location: "Bellandur / Sarjapur", capacity: "150 – 800 Guests", rooms: "12 Luxury Cottages", pricing: "₹3,00,000 – ₹6,00,000 / day", catering: "Outside catering permitted", style: "Balinese Thatched Pavilions & Courtyards", link: "venues/templetree-leisure-bangalore.html" },
            { id: "moongate", name: "The Moongate", location: "Airport Road", capacity: "300 – 2,000 Guests", rooms: "30 Boutique Villa Rooms", pricing: "₹5,00,000 – ₹12,00,000 / day", catering: "Outside catering permitted", style: "10-Acre Private Lakefront Amphitheater", link: "venues/moongate-bangalore.html" }
        ];

        function initSelectors() {
            const s1 = document.getElementById("venue1");
            const s2 = document.getElementById("venue2");
            const s3 = document.getElementById("venue3");

            VENUES_DB.forEach((v, idx) => {
                s1.add(new Option(v.name, v.id, idx === 0, idx === 0));
                s2.add(new Option(v.name, v.id, idx === 1, idx === 1));
                s3.add(new Option(v.name, v.id, idx === 5, idx === 5));
            });
            renderComparison();
        }

        function renderComparison() {
            const v1 = VENUES_DB.find(v => v.id === document.getElementById("venue1").value);
            const v2 = VENUES_DB.find(v => v.id === document.getElementById("venue2").value);
            const v3 = VENUES_DB.find(v => v.id === document.getElementById("venue3").value);

            const table = document.getElementById("compTable");
            table.innerHTML = `
                <thead>
                    <tr>
                        <th class="prop-col">Feature</th>
                        <th><strong>${v1.name}</strong></th>
                        <th><strong>${v2.name}</strong></th>
                        <th><strong>${v3.name}</strong></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="prop-col">Location</td>
                        <td>${v1.location}</td>
                        <td>${v2.location}</td>
                        <td>${v3.location}</td>
                    </tr>
                    <tr>
                        <td class="prop-col">Guest Capacity</td>
                        <td><strong>${v1.capacity}</strong></td>
                        <td><strong>${v2.capacity}</strong></td>
                        <td><strong>${v3.capacity}</strong></td>
                    </tr>
                    <tr>
                        <td class="prop-col">Rooms on Site</td>
                        <td>${v1.rooms}</td>
                        <td>${v2.rooms}</td>
                        <td>${v3.rooms}</td>
                    </tr>
                    <tr>
                        <td class="prop-col">Typical Pricing</td>
                        <td><span style="color:var(--primary); font-weight:700;">${v1.pricing}</span></td>
                        <td><span style="color:var(--primary); font-weight:700;">${v2.pricing}</span></td>
                        <td><span style="color:var(--primary); font-weight:700;">${v3.pricing}</span></td>
                    </tr>
                    <tr>
                        <td class="prop-col">Catering Policy</td>
                        <td>${v1.catering}</td>
                        <td>${v2.catering}</td>
                        <td>${v3.catering}</td>
                    </tr>
                    <tr>
                        <td class="prop-col">Aesthetic & Style</td>
                        <td>${v1.style}</td>
                        <td>${v2.style}</td>
                        <td>${v3.style}</td>
                    </tr>
                    <tr>
                        <td class="prop-col">Dedicated Guide</td>
                        <td><a href="${v1.link}" style="color:var(--primary); font-weight:600;">View Full Specs →</a></td>
                        <td><a href="${v2.link}" style="color:var(--primary); font-weight:600;">View Full Specs →</a></td>
                        <td><a href="${v3.link}" style="color:var(--primary); font-weight:600;">View Full Specs →</a></td>
                    </tr>
                </tbody>
            `;
        }

        window.onload = initSelectors;
    </script>
</body>
</html>
"""

# 2. WEDDING BUDGET CALCULATOR TOOL (wedding-budget-calculator.html)
calculator_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bengaluru Wedding Cost & Budget Calculator 2026 | Swariya Weddings</title>
    <meta name="description" content="Calculate your customized Bengaluru wedding budget in real-time. Estimate venue, catering, decor, photography and planning costs instantly with Swariya Weddings.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://swariyaweddings.com/wedding-budget-calculator.html">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">

    <style>
        :root {
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
        }
        body { font-family: 'Plus Jakarta Sans', sans-serif; color: var(--text-main); background: var(--bg-light); line-height: 1.6; }
        h1, h2, h3, h4 { font-family: 'Playfair Display', serif; color: var(--primary-dark); }
        .hero { padding: 130px 20px 50px; background: linear-gradient(135deg, #fdf0f4 0%, #fffbf2 100%); text-align: center; border-bottom: 1px solid #f0e2e7; }
        .hero h1 { font-size: 2.8rem; margin-bottom: 15px; }
        .hero p { font-size: 1.15rem; color: var(--text-muted); max-width: 800px; margin: 0 auto; }

        .container { max-width: 1140px; margin: 0 auto; padding: 0 20px; }
        
        .calc-grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; margin-top: 40px; }
        @media (max-width: 850px) { .calc-grid { grid-template-columns: 1fr; } }

        .calc-card { background: var(--white); border-radius: var(--border-radius); padding: 35px; box-shadow: var(--card-shadow); border: 1px solid #f0eae5; }
        .control-group { margin-bottom: 25px; }
        .control-group label { display: block; font-weight: 700; color: var(--text-main); margin-bottom: 10px; font-size: 1rem; }
        .range-slider { width: 100%; accent-color: var(--primary); height: 8px; border-radius: 4px; }
        .val-badge { display: inline-block; background: var(--primary-light); color: var(--primary); padding: 4px 12px; border-radius: 20px; font-weight: 700; font-size: 0.95rem; margin-left: 10px; }
        
        select.calc-select { width: 100%; padding: 12px; border-radius: 8px; border: 1px solid #d8ccc7; font-size: 1rem; font-family: inherit; background: white; }

        .results-card { background: linear-gradient(135deg, #2b111b 0%, #15080e 100%); color: white; border-radius: var(--border-radius); padding: 35px; box-shadow: var(--card-shadow); position: sticky; top: 100px; }
        .results-card h3 { color: white; margin-bottom: 5px; font-size: 1.8rem; }
        .est-total { font-size: 2.4rem; font-weight: 700; color: var(--accent); margin: 15px 0 25px; }
        
        .breakdown-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.1); font-size: 0.95rem; }
        .breakdown-row:last-child { border-bottom: none; }
        .breakdown-val { font-weight: 700; color: #fff; }

        .btn-wa-export { display: flex; align-items: center; justify-content: center; gap: 10px; background: #25d366; color: white; padding: 16px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 1.05rem; margin-top: 25px; transition: 0.2s; }
        .btn-wa-export:hover { background: #1eb956; }
    </style>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "Bengaluru Wedding Cost & Budget Calculator 2026",
      "url": "https://swariyaweddings.com/wedding-budget-calculator.html",
      "applicationCategory": "CalculatorApplication",
      "operatingSystem": "All",
      "description": "Interactive wedding budget estimation calculator for Bangalore weddings across venue, decor, catering and planning tiers."
    }
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
                <a href="venue-finder.html" class="nav-link">Venue Finder</a>
                <a href="wedding-budget-calculator.html" class="nav-link active">Calculator</a>
                <a href="wedding-brief-builder.html" class="nav-link">Brief Builder</a>
                <a href="contact.html" class="btn-primary">Book Consultation</a>
            </nav>
        </div>
    </header>

    <div class="hero">
        <div class="container">
            <h1>Bengaluru Wedding Budget Calculator 2026</h1>
            <p>Customize your guest count, celebration duration, venue tier, and decor style to get an instant, itemized Bengaluru wedding cost estimate.</p>
        </div>
    </div>

    <main class="container">
        <div class="calc-grid">
            <div class="calc-card">
                <h2>Configure Your Celebration</h2>

                <div class="control-group">
                    <label>Guest Count: <span id="guestBadge" class="val-badge">300 Guests</span></label>
                    <input type="range" id="guestInput" class="range-slider" min="50" max="1500" step="50" value="300" oninput="updateCalculator()">
                </div>

                <div class="control-group">
                    <label>Number of Celebration Days: <span id="daysBadge" class="val-badge">2 Days</span></label>
                    <input type="range" id="daysInput" class="range-slider" min="1" max="4" step="1" value="2" oninput="updateCalculator()">
                </div>

                <div class="control-group">
                    <label>Venue Style & Tier</label>
                    <select id="venueTier" class="calc-select" onchange="updateCalculator()">
                        <option value="heritage">Heritage Villa / Boutique Lawn (e.g. Tamarind Tree, Samavana)</option>
                        <option value="fivestar">5-Star Luxury Hotel (e.g. The Leela Palace, Taj West End)</option>
                        <option value="resort">Destination Resort (e.g. Area 83, Windflower Prakruthi)</option>
                        <option value="palace">Palace Grounds Grand Hall (e.g. Gayatri Vihar)</option>
                    </select>
                </div>

                <div class="control-group">
                    <label>Decor & Floral Production Tier</label>
                    <select id="decorTier" class="calc-select" onchange="updateCalculator()">
                        <option value="elegant">Elegant Traditional (Brass, Marigold, Temple Torans)</option>
                        <option value="premium">Premium Designer (Imported Florals, Custom Truss, Fairy Light Canopies)</option>
                        <option value="royal">Grand Royal & Thematic (Monumental Sets, 3D Pillars, Crystal Chandeliers)</option>
                    </select>
                </div>

                <div class="control-group">
                    <label>Catering & Food Style</label>
                    <select id="cateringTier" class="calc-select" onchange="updateCalculator()">
                        <option value="south_veg">Traditional South Indian Banana Leaf Oota (Pure Veg)</option>
                        <option value="multi_veg">Multi-Cuisine Pure Veg Feast (North, South, Live Chaat)</option>
                        <option value="multi_nv">Grand Multi-Cuisine Gourmet with Live Counters & Non-Veg</option>
                    </select>
                </div>
            </div>

            <div class="results-card">
                <h3>Estimated Investment</h3>
                <p style="opacity: 0.8; font-size: 0.9rem;">Bengaluru Market Benchmark (2026)</p>
                <div class="est-total" id="totalEstimate">₹38,50,000</div>

                <div style="margin-top: 20px;">
                    <div class="breakdown-row">
                        <span>Venue Rental / Room Blocks:</span>
                        <span class="breakdown-val" id="bVenue">₹10,00,000</span>
                    </div>
                    <div class="breakdown-row">
                        <span>Catering & Food Service:</span>
                        <span class="breakdown-val" id="bCatering">₹12,00,000</span>
                    </div>
                    <div class="breakdown-row">
                        <span>Decor, Mandap & Lighting:</span>
                        <span class="breakdown-val" id="bDecor">₹9,50,000</span>
                    </div>
                    <div class="breakdown-row">
                        <span>Photography & Cinematography:</span>
                        <span class="breakdown-val" id="bPhoto">₹4,00,000</span>
                    </div>
                    <div class="breakdown-row">
                        <span>Sound, DJ & Entertainment:</span>
                        <span class="breakdown-val" id="bMusic">₹1,50,000</span>
                    </div>
                    <div class="breakdown-row">
                        <span>Swariya Full-Service Planning:</span>
                        <span class="breakdown-val" id="bPlanning">₹1,50,000</span>
                    </div>
                </div>

                <a id="waExportBtn" href="#" class="btn-wa-export" target="_blank" rel="noopener">
                    💬 Export Estimate to WhatsApp
                </a>
            </div>
        </div>
    </main>

    <footer class="footer" style="background:#1a1a1a; color:#fff; padding:60px 0 30px; margin-top:80px;">
        <div class="container" style="text-align:center;">
            <p><strong>Swariya Weddings</strong> — Premier Wedding Planners in Bengaluru. 150+ Weddings | 500+ Happy Clients | 4.9/5 Rating.</p>
            <p style="font-size:0.9rem; color:#aaa;">© 2026 Swariya Weddings. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        function updateCalculator() {
            const guests = parseInt(document.getElementById("guestInput").value);
            const days = parseInt(document.getElementById("daysInput").value);
            const venueTier = document.getElementById("venueTier").value;
            const decorTier = document.getElementById("decorTier").value;
            const cateringTier = document.getElementById("cateringTier").value;

            document.getElementById("guestBadge").innerText = guests + " Guests";
            document.getElementById("daysBadge").innerText = days + (days === 1 ? " Day" : " Days");

            // Base calculations
            let venueBase = (venueTier === "heritage") ? 450000 : (venueTier === "fivestar" ? 650000 : (venueTier === "resort" ? 400000 : 800000));
            let venueCost = venueBase * days;

            let plateCost = (cateringTier === "south_veg") ? 900 : (cateringTier === "multi_veg" ? 1400 : 2000);
            let mealsCount = days * 2; // avg 2 major meals per day
            let cateringCost = guests * plateCost * mealsCount;

            let decorBase = (decorTier === "elegant") ? 400000 : (decorTier === "premium" ? 850000 : 1500000);
            let decorCost = decorBase * (1 + (days - 1) * 0.4);

            let photoCost = 250000 + (days - 1) * 120000;
            let musicCost = 100000 + (days - 1) * 50000;
            let planningCost = 150000 + (days - 1) * 50000;

            let total = venueCost + cateringCost + decorCost + photoCost + musicCost + planningCost;

            function formatINR(n) {
                return "₹" + Math.round(n).toLocaleString('en-IN');
            }

            document.getElementById("totalEstimate").innerText = formatINR(total);
            document.getElementById("bVenue").innerText = formatINR(venueCost);
            document.getElementById("bCatering").innerText = formatINR(cateringCost);
            document.getElementById("bDecor").innerText = formatINR(decorCost);
            document.getElementById("bPhoto").innerText = formatINR(photoCost);
            document.getElementById("bMusic").innerText = formatINR(musicCost);
            document.getElementById("bPlanning").innerText = formatINR(planningCost);

            const msg = `Hi Swariya Weddings, I used your Budget Calculator! Here is my estimate:\\n- Guests: ${guests}\\n- Days: ${days}\\n- Estimated Total: ${formatINR(total)}\\nCan we discuss date availability and itemized quotes?`;
            document.getElementById("waExportBtn").href = "https://wa.me/919606822204?text=" + encodeURIComponent(msg);
        }

        window.onload = updateCalculator;
    </script>
</body>
</html>
"""

# 3. WEDDING BRIEF & MOODBOARD BUILDER (wedding-brief-builder.html)
brief_builder_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Wedding Brief & Moodboard Builder | Swariya Weddings</title>
    <meta name="description" content="Build your custom wedding moodboard & brief in 3 minutes. Pick your aesthetic, functions, color palette and send it to Swariya Weddings for instant vision alignment.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://swariyaweddings.com/wedding-brief-builder.html">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">

    <style>
        :root {
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
        }
        body { font-family: 'Plus Jakarta Sans', sans-serif; color: var(--text-main); background: var(--bg-light); line-height: 1.6; }
        h1, h2, h3, h4 { font-family: 'Playfair Display', serif; color: var(--primary-dark); }
        .hero { padding: 130px 20px 50px; background: linear-gradient(135deg, #fdf0f4 0%, #fffbf2 100%); text-align: center; border-bottom: 1px solid #f0e2e7; }
        .hero h1 { font-size: 2.8rem; margin-bottom: 15px; }
        .hero p { font-size: 1.15rem; color: var(--text-muted); max-width: 800px; margin: 0 auto; }

        .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
        
        .step-card { background: var(--white); border-radius: var(--border-radius); padding: 35px; box-shadow: var(--card-shadow); margin-top: 30px; border: 1px solid #f0eae5; }
        .step-num { display: inline-block; background: var(--primary); color: white; width: 32px; height: 32px; text-align: center; line-height: 32px; border-radius: 50%; font-weight: 700; margin-right: 10px; }
        
        .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-top: 20px; }
        .opt-card { border: 2px solid #e8ded8; border-radius: 8px; padding: 18px; cursor: pointer; transition: 0.2s; background: #faf7f5; }
        .opt-card.selected { border-color: var(--primary); background: var(--primary-light); font-weight: 700; color: var(--primary-dark); }
        
        .color-dot { display: inline-block; width: 22px; height: 22px; border-radius: 50%; margin-right: 6px; vertical-align: middle; border: 1px solid rgba(0,0,0,0.1); }

        .brief-summary { background: linear-gradient(135deg, #2b111b 0%, #15080e 100%); color: white; border-radius: var(--border-radius); padding: 35px; margin-top: 40px; }
        .brief-summary h3 { color: white; font-size: 1.8rem; margin-bottom: 15px; }

        .btn-submit-brief { display: inline-flex; align-items: center; gap: 10px; background: #25d366; color: white; padding: 16px 30px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 1.1rem; margin-top: 20px; }
    </style>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "Interactive Wedding Brief & Moodboard Builder",
      "url": "https://swariyaweddings.com/wedding-brief-builder.html",
      "applicationCategory": "DesignApplication",
      "operatingSystem": "All",
      "description": "Customizable wedding moodboard and brief builder for Bangalore couples."
    }
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
                <a href="venue-finder.html" class="nav-link">Venue Finder</a>
                <a href="wedding-budget-calculator.html" class="nav-link">Calculator</a>
                <a href="wedding-brief-builder.html" class="nav-link active">Brief Builder</a>
                <a href="contact.html" class="btn-primary">Book Consultation</a>
            </nav>
        </div>
    </header>

    <div class="hero">
        <div class="container">
            <h1>Wedding Brief & Moodboard Builder</h1>
            <p>Select your aesthetic, ceremony lineup, and color story in 3 steps to generate an instant design brief for our creative team.</p>
        </div>
    </div>

    <main class="container">
        <!-- Step 1 -->
        <div class="step-card">
            <h2><span class="step-num">1</span> Choose Your Primary Design Aesthetic</h2>
            <div class="options-grid">
                <div class="opt-card selected" onclick="toggleSelect(this, 'theme')">🌺 Traditional Temple & Brass Floral</div>
                <div class="opt-card" onclick="toggleSelect(this, 'theme')">🌿 Rustic Garden & Banyan Tree Heritage</div>
                <div class="opt-card" onclick="toggleSelect(this, 'theme')">✨ Royal Palace & Golden Opulence</div>
                <div class="opt-card" onclick="toggleSelect(this, 'theme')">🌸 Modern Pastel & Bohemian Chic</div>
            </div>
        </div>

        <!-- Step 2 -->
        <div class="step-card">
            <h2><span class="step-num">2</span> Select Celebrations & Functions (Multi-Select)</h2>
            <div class="options-grid">
                <div class="opt-card selected" onclick="toggleMulti(this)">💛 Haldi / Pellikuthuru</div>
                <div class="opt-card selected" onclick="toggleMulti(this)">💚 Mehendi Ceremony</div>
                <div class="opt-card selected" onclick="toggleMulti(this)">🎉 High-Energy Sangeet</div>
                <div class="opt-card selected" onclick="toggleMulti(this)">🪔 Traditional Muhurtham</div>
                <div class="opt-card selected" onclick="toggleMulti(this)">🥂 Grand Evening Reception</div>
            </div>
        </div>

        <!-- Step 3 -->
        <div class="step-card">
            <h2><span class="step-num">3</span> Select Your Signature Color Palette</h2>
            <div class="options-grid">
                <div class="opt-card selected" onclick="toggleSelect(this, 'color')">
                    <span class="color-dot" style="background:#ffb703;"></span>
                    <span class="color-dot" style="background:#b7094c;"></span>
                    Marigold & Crimson Red
                </div>
                <div class="opt-card" onclick="toggleSelect(this, 'color')">
                    <span class="color-dot" style="background:#fceade;"></span>
                    <span class="color-dot" style="background:#255f45;"></span>
                    Blush Pink & Sage Green
                </div>
                <div class="opt-card" onclick="toggleSelect(this, 'color')">
                    <span class="color-dot" style="background:#ffffff;"></span>
                    <span class="color-dot" style="background:#d4af37;"></span>
                    Ivory & Royal Antique Gold
                </div>
                <div class="opt-card" onclick="toggleSelect(this, 'color')">
                    <span class="color-dot" style="background:#9d4edd;"></span>
                    <span class="color-dot" style="background:#ffd166;"></span>
                    Lavender & Sunlit Mustard
                </div>
            </div>
        </div>

        <!-- Summary & Submission -->
        <div class="brief-summary">
            <h3>Your Generated Wedding Brief</h3>
            <p id="briefText" style="font-size: 1.1rem; opacity: 0.95; line-height: 1.8;">Loading brief...</p>

            <a id="submitBriefBtn" href="#" class="btn-submit-brief" target="_blank" rel="noopener">
                💬 Submit Brief to Swariya Design Studio via WhatsApp
            </a>
        </div>
    </main>

    <footer class="footer" style="background:#1a1a1a; color:#fff; padding:60px 0 30px; margin-top:80px;">
        <div class="container" style="text-align:center;">
            <p><strong>Swariya Weddings</strong> — Premier Wedding Planners in Bengaluru. 150+ Weddings | 500+ Happy Clients | 4.9/5 Rating.</p>
            <p style="font-size:0.9rem; color:#aaa;">© 2026 Swariya Weddings. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        function toggleSelect(el, group) {
            const parent = el.parentElement;
            parent.querySelectorAll(".opt-card").forEach(c => c.classList.remove("selected"));
            el.classList.add("selected");
            updateBrief();
        }

        function toggleMulti(el) {
            el.classList.toggle("selected");
            updateBrief();
        }

        function updateBrief() {
            const themeEl = document.querySelector(".options-grid .selected");
            const theme = themeEl ? themeEl.innerText.trim() : "Custom Theme";

            const funcs = [];
            document.querySelectorAll(".step-card:nth-child(2) .selected").forEach(el => funcs.push(el.innerText.trim()));

            const colorEl = document.querySelectorAll(".step-card:nth-child(3) .selected")[0];
            const color = colorEl ? colorEl.innerText.trim() : "Custom Palette";

            const summary = `<strong>Primary Aesthetic:</strong> ${theme}<br><strong>Celebration Lineup:</strong> ${funcs.join(", ")}<br><strong>Color Story:</strong> ${color}`;
            document.getElementById("briefText").innerHTML = summary;

            const waMsg = `Hi Swariya Weddings, I designed my Wedding Brief on your site:\\n- Theme: ${theme}\\n- Functions: ${funcs.join(", ")}\\n- Color Palette: ${color}\\nCan we discuss customized decor sketches and timelines?`;
            document.getElementById("submitBriefBtn").href = "https://wa.me/919606822204?text=" + encodeURIComponent(waMsg);
        }

        window.onload = updateBrief;
    </script>
</body>
</html>
"""

with open("venue-finder.html", "w", encoding="utf-8") as f:
    f.write(venue_finder_html)
print("Created: venue-finder.html")

with open("wedding-budget-calculator.html", "w", encoding="utf-8") as f:
    f.write(calculator_html)
print("Created: wedding-budget-calculator.html")

with open("wedding-brief-builder.html", "w", encoding="utf-8") as f:
    f.write(brief_builder_html)
print("Created: wedding-brief-builder.html")
