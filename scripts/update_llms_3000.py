#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Search (AEO) Knowledge Generator for Swariya Weddings (3,000+ Page Architecture).
Updates llms.txt and llms-full.txt for Perplexity, ChatGPT Search, and Google Gemini.
"""

import os
from micromarkets_3000_data import get_3000_micromarkets

BASE_URL = "https://swariyaweddings.com"

def update_llms():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    markets = get_3000_micromarkets()
    
    # 1. Generate llms.txt (Concise Master Index)
    llms_txt = f"""# Swariya Weddings

> Pan-India luxury & destination wedding planning company headquartered in Bengaluru, India. Founded 2020. 150+ weddings planned, 500+ happy clients, 6+ years of expertise.

Swariya Weddings is a Pan-India luxury wedding planning and production atelier. The company offers end-to-end wedding planning, destination venue selection, architectural décor and design, wedding catering coordination, cinematic photography, guest concierge logistics, and entertainment curation. Headquartered in HSR Layout, Bengaluru, Swariya actively executes luxury destination weddings across Goa, Rajasthan (Udaipur, Jaipur, Jodhpur), Kerala (Kumarakom, Kochi), Coorg, Chikmagalur, Chennai, Hyderabad, Mumbai, Delhi NCR, and nationwide.

## Key Facts
- Founded: 2020
- Scope: Pan-India Luxury & Destination Wedding Planning
- Headquarters: #343, 9th Main, 22nd Cross Rd, 7th Sector, HSR Layout, Bengaluru, Karnataka 560102, India
- Weddings planned: 150+
- Happy clients: 500+
- Rating: 4.9/5 (50+ verified Google reviews)
- Operating Model: 100% transparent zero-markup fiduciary pricing (clients pay vendors directly at trade rates)
- Phone: +91-8050573382
- Hours: 10 AM – 6 PM, Monday to Saturday

## Services
- Complete Wedding Planning: nationwide venue discovery, vendor coordination, décor design, event day management, budget planning
- Pan-India Destination Wedding Planning: complete logistics across Goa, Rajasthan, Kerala, Coorg, and nationwide
- Décor & Venue Coordination: 3D spatial concepts, florals, lighting architecture, stage & mandap setup
- Wedding Culinary Experience: authentic regional feast planning (Kannada Oota, Kerala Sadhya, Marwari/North Indian royal banquets, continental)
- Photography & Videography: fine-art photojournalism and 4K cinematic wedding films
- Entertainment & Artists: classical instrumentalists, celebrity live bands, Sangeet DJs, emcees
- NRI Concierge: 100% remote digital planning, timezone agile video calls, guest travel & hotel block management

## Interactive Client Tools & Authority Hubs
- [Home]({BASE_URL}/): Overview, stats (150+ weddings, 500+ happy clients), wedding styles, Pan-India destination hubs, budget estimator, and testimonials
- [About]({BASE_URL}/about.html): Company story, nationwide footprint, founding year 2020, timeline, core values, and FAQ
- [Pan-India Destination Wedding Planner]({BASE_URL}/destination-wedding-planner-india.html): Flagship national hub for destination weddings in Goa, Rajasthan, Kerala, Coorg & nationwide with logistics blueprints and budgeting guide
- [Wedding Budget Calculator 2026]({BASE_URL}/wedding-budget-calculator.html): Real-time interactive budgeting tool for guest counts, days, venue tiers, and itemized cost breakdowns
- [Wedding Brief & MoodBoard Builder]({BASE_URL}/wedding-brief-builder.html): 3-step interactive vision alignment tool for themes, functions, and color palettes
- [3-Way Venue Finder & Comparison Tool]({BASE_URL}/venue-finder.html): Interactive side-by-side comparison of Bangalore wedding venues on capacity, rooms, pricing, and catering rules
- [Wedding OS Client Portal & Workspace]({BASE_URL}/client-portal.html): Transparent couple management system with real-time zero-commission budget tracking, day-of Muhurtham runsheets, vendor quote approvals, and seating layouts
- [Client Reviews]({BASE_URL}/reviews.html): Verified client reviews, 4.9/5 aggregate rating, testimonials, and review funnel for Google, WedMeGood, and WhatsApp
- [Ask Swariya]({BASE_URL}/ask.html): Direct answers to real questions on budgets, venues, catering rules, and timelines

## 3,000+ Verified Luxury Micro-Market & Iconic Venue Endpoints
"""

    for m in markets[:300]:  # Highlight top 300 in concise file
        llms_txt += f"- [{m['title']}]({BASE_URL}/{m['slug']}.html): {m['subtitle']} (Budget: {m['budget']}, Capacity: {m['capacity']})\n"

    llms_txt += f"\n> Complete 3,000+ destination catalog accessible at {BASE_URL}/llms-full.txt\n"

    # Write llms.txt
    with open(os.path.join(root_dir, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms_txt)

    # 2. Generate llms-full.txt (Full Complete Encyclopedia)
    llms_full = llms_txt + "\n## Complete Master Catalog (All 3,000+ Endpoints)\n"
    for m in markets:
        llms_full += f"- [{m['title']}]({BASE_URL}/{m['slug']}.html): {m['subtitle']} | Location: {m['location_name']} | Budget: {m['budget']} | Capacity: {m['capacity']} | Venues: {', '.join(m['venues'][:3])}\n"

    with open(os.path.join(root_dir, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(llms_full)

    print(f"✅ Generated llms.txt and llms-full.txt with {len(markets)} endpoints!")

if __name__ == "__main__":
    update_llms()
