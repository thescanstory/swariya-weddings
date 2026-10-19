#!/usr/bin/env python3
"""
Swariya Weddings - Pan-India Destination Outreach & National Authority Dispatcher
Generates tailored outreach dossiers for:
1. National Royal Palaces (Rajasthan: Udaipur, Jaipur, Jodhpur, Jaisalmer)
2. National Beachfront & Clifftop Resorts (Goa)
3. National Backwater & Estate Retreats (Kerala & Karnataka)
4. National Travel, Luxury & Bridal Publications (Condé Nast Traveller, Vogue, YourStory)
5. Global NRI Wedding Portals (US, UK, UAE, Australia)
"""

import os
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

NATIONAL_PROSPECTS = [
    # RAJASTHAN ROYAL PALACES
    {
        "id": "NAT-01",
        "name": "Taj Lake Palace & Jagmandir Island",
        "city": "Udaipur, Rajasthan",
        "type": "Ultra-Luxury Royal Palace Hotel",
        "domain": "tajhotels.com",
        "est_dr": 78,
        "contact_target": "events.lakepalace@tajhotels.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-taj-lake-palace-udaipur-udaipur",
        "pitch_angle": "Empanelled Luxury Destination Planner & 3D Island Mandap Architecture"
    },
    {
        "id": "NAT-02",
        "name": "The Oberoi Udaivilas",
        "city": "Udaipur, Rajasthan",
        "type": "Premier Lake Palace Resort",
        "domain": "oberoihotels.com",
        "est_dr": 82,
        "contact_target": "weddings.udaivilas@oberoihotels.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-the-oberoi-udaivilas-udaipur",
        "pitch_angle": "Fiduciary Turnkey Buyout Specialist & NRI Concierge Link"
    },
    {
        "id": "NAT-03",
        "name": "Rambagh Palace Jaipur",
        "city": "Jaipur, Rajasthan",
        "type": "Historic Rajput Palace",
        "domain": "tajhotels.com",
        "est_dr": 78,
        "contact_target": "rambagh.jaipur@tajhotels.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-rambagh-palace-jaipur-jaipur",
        "pitch_angle": "Royal Heritage Production Partner & Direct Trade Vendor Empanelment"
    },
    {
        "id": "NAT-04",
        "name": "Fairmont Jaipur",
        "city": "Jaipur, Rajasthan",
        "type": "Mughal-Rajput Luxury Palace",
        "domain": "fairmont.com",
        "est_dr": 80,
        "contact_target": "jaipur@fairmont.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-fairmont-jaipur-jaipur",
        "pitch_angle": "Grand Baraat & 3D Mandap Spatial Design Showcase"
    },
    {
        "id": "NAT-05",
        "name": "Umaid Bhawan Palace Jodhpur",
        "city": "Jodhpur, Rajasthan",
        "type": "Art Deco Royal Residence",
        "domain": "tajhotels.com",
        "est_dr": 78,
        "contact_target": "umaidbhawan.jodhpur@tajhotels.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-umaid-bhawan-palace-jodhpur-jodhpur",
        "pitch_angle": "Grand Royal Multi-Day Production Coordination"
    },
    {
        "id": "NAT-06",
        "name": "Six Senses Fort Barwara",
        "city": "Sawai Madhopur, Rajasthan",
        "type": "14th Century Heritage Fort Sanctuary",
        "domain": "sixsenses.com",
        "est_dr": 76,
        "contact_target": "reservations-fortbarwara@sixsenses.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-six-senses-fort-barwara-ranthambore-sawai-madhopur",
        "pitch_angle": "Sustainable Luxury & Eco-Friendly Royal Wedding Feature"
    },
    {
        "id": "NAT-07",
        "name": "Suryagarh Jaisalmer",
        "city": "Jaisalmer, Rajasthan",
        "type": "Luxury Desert Fort Estate",
        "domain": "suryagarh.com",
        "est_dr": 58,
        "contact_target": "stay@suryagarh.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-suryagarh-jaisalmer-jaisalmer",
        "pitch_angle": "Thar Desert Sangeet & Sand Dunes Mandap Planning Link"
    },

    # GOA BEACHFRONT RESORTS
    {
        "id": "NAT-08",
        "name": "Alila Diwa Goa",
        "city": "Majorda, South Goa",
        "type": "Boutique Coastal Resort (Hyatt)",
        "domain": "hyatt.com",
        "est_dr": 88,
        "contact_target": "diwagoa@alilahotels.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-alila-diwa-goa-majorda",
        "pitch_angle": "Preferred Beachfront Destination Wedding Curator & Cost Guide Link"
    },
    {
        "id": "NAT-09",
        "name": "Grand Hyatt Goa",
        "city": "Bambolim Bay, Goa",
        "type": "17th Century Indo-Portuguese Palace",
        "domain": "hyatt.com",
        "est_dr": 88,
        "contact_target": "goa.grand@hyatt.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-grand-hyatt-goa-bambolim",
        "pitch_angle": "Waterfront Lawn Production & Mega Banquet Empanelment"
    },
    {
        "id": "NAT-10",
        "name": "The St. Regis Goa Resort",
        "city": "Cavelossim / Mobor, Goa",
        "type": "49-Acre River & Beach Luxury Resort",
        "domain": "marriott.com",
        "est_dr": 91,
        "contact_target": "stregis.goa@stregis.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-the-st-regis-goa-resort-mobor-cavelossim",
        "pitch_angle": "Ultra-Luxury Buyout Concierge & High-Net-Worth Client Matching"
    },
    {
        "id": "NAT-11",
        "name": "ITC Grand Goa Resort & Spa",
        "city": "Arossim Beach, South Goa",
        "type": "Village-Style Beach Resort",
        "domain": "itchotels.com",
        "est_dr": 76,
        "contact_target": "itcgrandgoa@itchotels.in",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-itc-grand-goa-resort-spa-arossim",
        "pitch_angle": "Direct Coastal Floral Architecture & In-House Production Empanelment"
    },
    {
        "id": "NAT-12",
        "name": "W Goa",
        "city": "Vagator Clifftop, North Goa",
        "type": "Bohemian Luxury Clifftop Resort",
        "domain": "marriott.com",
        "est_dr": 91,
        "contact_target": "w.goa@whotels.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-w-goa-vagator",
        "pitch_angle": "Boho Chic Sunset Sangeet & Modern Luxury Wedding Feature"
    },

    # KERALA & KARNATAKA DESTINATIONS
    {
        "id": "NAT-13",
        "name": "Kumarakom Lake Resort",
        "city": "Kumarakom, Kerala",
        "type": "Luxury Backwater Heritage Sanctuary",
        "domain": "kumarakomlakeresort.in",
        "est_dr": 59,
        "contact_target": "klr@kumarakomlakeresort.in",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-kumarakom-lake-resort-kumarakom",
        "pitch_angle": "Backwater Houseboat Logistics & Traditional Kerala Sadhya Wedding"
    },
    {
        "id": "NAT-14",
        "name": "Grand Hyatt Kochi Bolgatty",
        "city": "Bolgatty Island, Kochi, Kerala",
        "type": "Waterfront Marina & Convention Palace",
        "domain": "hyatt.com",
        "est_dr": 88,
        "contact_target": "kochi.grand@hyatt.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-grand-hyatt-kochi-bolgatty-bolgatty-island-kochi",
        "pitch_angle": "Island Marina Wedding Production & Helicopter Logistics"
    },
    {
        "id": "NAT-15",
        "name": "The Tamara Coorg",
        "city": "Kabbinakad, Coorg, Karnataka",
        "type": "Luxury Coffee Plantation & Rainforest Retreat",
        "domain": "thetamara.com",
        "est_dr": 49,
        "contact_target": "reservations@thetamara.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-destination-wedding-cost-at-the-tamara-coorg-coorg",
        "pitch_angle": "Intimate Plantation Buyouts & Kodava Traditional Runsheet Feature"
    },

    # NATIONAL MEDIA & TRAVEL PR
    {
        "id": "NAT-16",
        "name": "Condé Nast Traveller India",
        "city": "Mumbai / National",
        "type": "Luxury Travel & Destination Magazine",
        "domain": "cntraveller.in",
        "est_dr": 81,
        "contact_target": "editorial@cntraveller.in",
        "swariya_guide": "https://swariyaweddings.com/best-destination-wedding-places-in-india",
        "pitch_angle": "Op-Ed: The 2026 Economics of Indian Palace Buyouts vs Beach Retreats"
    },
    {
        "id": "NAT-17",
        "name": "Vogue India Weddings",
        "city": "Mumbai / National",
        "type": "Premier High-Fashion & Bridal Media",
        "domain": "vogue.in",
        "est_dr": 85,
        "contact_target": "weddings@vogue.in",
        "swariya_guide": "https://swariyaweddings.com/3-day-luxury-destination-wedding-master-guide",
        "pitch_angle": "Trend Report: How 3D CAD Walkthroughs are Transforming Luxury Mandap Design"
    },
    {
        "id": "NAT-18",
        "name": "YourStory Media",
        "city": "Bengaluru / National",
        "type": "Leading Business & Startup Platform",
        "domain": "yourstory.com",
        "est_dr": 84,
        "contact_target": "editorial@yourstory.com",
        "swariya_guide": "https://swariyaweddings.com/press",
        "pitch_angle": "Founder Story: Disrupting India's ₹5T Wedding Industry with a 0% Kickback Fiduciary Model"
    },
    {
        "id": "NAT-19",
        "name": "Maharani Weddings",
        "city": "Global (US & UK Diaspora)",
        "type": "Premier South Asian Destination Bridal Blog",
        "domain": "maharaniweddings.com",
        "est_dr": 68,
        "contact_target": "submissions@maharaniweddings.com",
        "swariya_guide": "https://swariyaweddings.com/3-day-runsheet-and-rituals-for-nri-luxury-destination-wedding",
        "pitch_angle": "Real Wedding Submission: Remote Destination Wedding in Udaipur with Zero Markup Billing"
    },
    {
        "id": "NAT-20",
        "name": "Brown Girl Magazine",
        "city": "Global (US/UK/Canada)",
        "type": "South Asian Diaspora Lifestyle & Bridal",
        "domain": "browngirlmagazine.com",
        "est_dr": 65,
        "contact_target": "editor@browngirlmagazine.com",
        "swariya_guide": "https://swariyaweddings.com/client-portal",
        "pitch_angle": "The Modern Diaspora Bride: How to Audit Wedding Invoices & Plan an India Wedding Seamlessly"
    }
]

def generate_dossier():
    output_file = os.path.join(REPORTS_DIR, "pan_india_destination_dossier.html")
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Swariya Weddings — Pan-India Destination Authority Dossier</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #FAF6F0; color: #1C1917; margin: 0; padding: 30px; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: #FFF; padding: 35px; border-radius: 12px; box-shadow: 0 4px 25px rgba(0,0,0,0.06); }}
        h1 {{ font-family: Georgia, serif; color: #8B1A1A; margin-top: 0; font-size: 2rem; }}
        p.subtitle {{ color: #57534E; font-size: 1.05rem; margin-top: -8px; margin-bottom: 25px; }}
        .summary-cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 30px; }}
        .card {{ background: #FAF6F0; border-left: 4px solid #C5A059; padding: 16px; border-radius: 6px; }}
        .card strong {{ display: block; font-size: 1.4rem; color: #8B1A1A; }}
        .card span {{ font-size: 0.85rem; color: #57534E; text-transform: uppercase; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        th, td {{ padding: 12px 14px; text-align: left; border-bottom: 1px solid #E8DFD5; font-size: 0.9rem; }}
        th {{ background: #8B1A1A; color: #FFF; font-weight: 600; }}
        tr:hover {{ background: #FCF9F6; }}
        .dr-pill {{ background: #FFF3CD; color: #856404; font-weight: 700; padding: 3px 8px; border-radius: 10px; font-size: 0.8rem; }}
        .btn {{ display: inline-block; padding: 6px 12px; background: #8B1A1A; color: #FFF; border-radius: 4px; text-decoration: none; font-size: 0.8rem; }}
        .btn:hover {{ background: #C5A059; color: #1C1917; }}
    </style>
</head>
<body>
<div class="container">
    <h1>Swariya Weddings — Pan-India Destination Authority Dossier</h1>
    <p class="subtitle">Priority National Palace, Beach Resort & Luxury Media Target Pipeline (Rajasthan, Goa, Kerala, NRI)</p>

    <div class="summary-cards">
        <div class="card">
            <strong>Pan-India</strong>
            <span>Operational Scale</span>
        </div>
        <div class="card">
            <strong>DR 49 – 91</strong>
            <span>Target Authority Range</span>
        </div>
        <div class="card">
            <strong>20 Flagship Targets</strong>
            <span>Phase 1 National Batch</span>
        </div>
        <div class="card">
            <strong>0% Markup Fiduciary</strong>
            <span>Unique National Pitch Hook</span>
        </div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Code</th>
                <th>Target Property / Publication</th>
                <th>Location / Belt</th>
                <th>Est. DR</th>
                <th>Target Swariya Guide</th>
                <th>National Outreach Hook</th>
            </tr>
        </thead>
        <tbody>
    """

    for item in NATIONAL_PROSPECTS:
        html += f"""
            <tr>
                <td><strong>{item['id']}</strong></td>
                <td><strong>{item['name']}</strong><br><small style="color:#666;">{item['domain']} | {item['type']}</small></td>
                <td>{item['city']}</td>
                <td><span class="dr-pill">DR {item['est_dr']}</span></td>
                <td><a href="{item['swariya_guide']}" target="_blank" style="color:#8B1A1A;font-weight:500;">{item['swariya_guide'].split('/')[-1]}</a></td>
                <td><span style="font-size:0.85rem;color:#444;">{item['pitch_angle']}</span></td>
            </tr>
        """

    html += """
        </tbody>
    </table>
</div>
</body>
</html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generated Pan-India Destination Dossier: {output_file}")

if __name__ == "__main__":
    generate_dossier()
