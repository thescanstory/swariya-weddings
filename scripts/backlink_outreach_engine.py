#!/usr/bin/env python3
"""
Swariya Weddings - 500 Referring Domains Outreach & Verification Engine
Tracks, formats outreach pitches, and verifies active backlinks.
"""

import json
import os
import sys
import urllib.request
import re

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "500_referring_domains_database.json")

def load_db():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        sys.exit(1)
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def show_summary():
    data = load_db()
    total = len(data)
    by_category = {}
    by_status = {}
    dr_dist = {"DR 70-99 (Tier 1 Ultra)": 0, "DR 50-69 (High Authority)": 0, "DR 30-49 (Mid-Market)": 0, "DR <30 (Niche)": 0}

    for item in data:
        cat = item["category"]
        st = item["status"]
        dr = item["est_dr"]
        
        by_category[cat] = by_category.get(cat, 0) + 1
        by_status[st] = by_status.get(st, 0) + 1
        
        if dr >= 70:
            dr_dist["DR 70-99 (Tier 1 Ultra)"] += 1
        elif dr >= 50:
            dr_dist["DR 50-69 (High Authority)"] += 1
        elif dr >= 30:
            dr_dist["DR 30-49 (Mid-Market)"] += 1
        else:
            dr_dist["DR <30 (Niche)"] += 1

    print("================================================================================")
    print("        SWARIYA WEDDINGS — 500 REFERRING DOMAINS ENGINE DASHBOARD              ")
    print("================================================================================")
    print(f"Total Prospect Domains: {total}")
    print("\n[+] Breakdown by Category:")
    for c, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"    - {c:<40}: {count} domains")
    
    print("\n[+] Authority Profile (Estimated DR Distribution):")
    for d, count in dr_dist.items():
        print(f"    - {d:<35}: {count} domains")

    print("\n[+] Pipeline Status:")
    for s, count in by_status.items():
        print(f"    - {s:<25}: {count}")
    print("================================================================================")

def get_outreach_pitch(domain_id):
    data = load_db()
    target = next((item for item in data if item["id"] == domain_id), None)
    if not target:
        print(f"Domain ID {domain_id} not found.")
        return

    cat = target["category"]
    name = target["name"]
    domain = target["domain"]
    target_page = target["landing_page_target"]

    print("\n" + "="*80)
    print(f"OUTREACH KIT FOR #{domain_id}: {name} ({domain})")
    print(f"Category: {cat} | Target Link: {target_page}")
    print("="*80)

    if "Venue" in cat:
        print("""
Subject: Swariya Weddings x {name} — 2026 Wedding Cost Guide & Empanelment Feature

Dear {name} Events Team,

We have recently published our comprehensive 2026 Bangalore & Karnataka Luxury Wedding Planning Guide, featuring {name} prominently to prospective luxury couples:
URL: {target_page}

Our guide highlights your estate/ballroom dimensions, guest hospitality capacities, and recommended production setups for multi-day celebrations.

As a luxury planning atelier specializing in bespoke celebrations across Bangalore, we would love to be listed on your official recommended planners/empanelled vendor directory, or share a reciprocal link to assist couples planning their weddings at your property.

Could you please connect us with your venue partnership/marketing coordinator?

Warm regards,
Swariya Weddings Concierge Team
https://swariyaweddings.com | contact@swariyaweddings.com
""".format(name=name, target_page=target_page))

    elif "Wedding Portal" in cat or "Citation" in cat:
        print("""
ACTION: DIRECT SUBMISSION / VERIFIED PROFILE CREATION
Platform: {name}
Listing Name: Swariya Weddings - Luxury Wedding Planners Bangalore
Target Page to Link: {target_page}
NAP Details:
  - Address: HSR Layout & Indiranagar, Bengaluru, Karnataka 560102
  - Phone: +91 80505 73382
  - Email: contact@swariyaweddings.com
  - Core Differentiators: 0% Vendor Markups (Fiduciary Model), 3D Spatial CAD Mandap Previews, 150+ Celebrations Planned.
""".format(name=name, target_page=target_page))

    elif "Media" in cat or "PR" in cat:
        print("""
Subject: Story Pitch: The Bangalore Startup Replacing Wedding Commissions with 3D CAD & 0% Markup

Dear Editorial Team at {name},

While the Indian wedding industry is notorious for opaque 15%–30% vendor kickbacks and marked-up invoices, Bengaluru-based Swariya Weddings is pioneering a transparent, fiduciary planning model.

Clients review direct, itemized vendor contracts at trade cost, accompanied by photorealistic 3D architectural CAD previews of every mandap and ballroom setup before a single flower is cut.

We have compiled comprehensive data on modern South Indian wedding budgets and shifting millennial luxury preferences in our 2026 Bengaluru Wedding Cost Report:
{target_page}

We would be delighted to share founder insights, data charts, or a guest feature on the economics of transparent luxury celebrations in Bangalore.

Best regards,
Editorial Desk | Swariya Weddings
https://swariyaweddings.com
""".format(name=name, target_page=target_page))

    else:
        print("""
Subject: Collaboration & Vendor Credit Feature with Swariya Weddings

Hi {name} Team,

We love your work across Bangalore's luxury wedding circuit. At Swariya Weddings, we are continuously curating high-trust creative partners across our upcoming 2026 wedding calendar (including landmark celebrations at The Tamarind Tree and Palace Grounds).

We regularly feature collaborative partners, photographers, and artisans on our Bangalore planning hubs:
{target_page}

We'd love to explore cross-featuring our brands, exchanging portfolio backlinks, and coordinating on upcoming client briefs. Let's connect!

Warm regards,
Swariya Weddings Partner Team
https://swariyaweddings.com
""".format(name=name, target_page=target_page))

def check_live_link(url_to_check):
    print(f"Checking {url_to_check} for links to swariyaweddings.com...")
    try:
        req = urllib.request.Request(
            url_to_check,
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            matches = re.findall(r'href=[\'"]([^\'"]*swariyaweddings\.com[^\'"]*)[\'"]', content, re.I)
            if matches:
                print(f"[SUCCESS] Found {len(matches)} live backlink(s):")
                for m in set(matches):
                    print(f"   -> {m}")
                return True
            else:
                print("[INFO] Page fetched successfully, but no active swariyaweddings.com link detected.")
                return False
    except Exception as e:
        print(f"[ERROR] Could not check URL: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_summary()
        print("\nCommands:")
        print("  python3 backlink_outreach_engine.py summary")
        print("  python3 backlink_outreach_engine.py pitch <DOMAIN_ID>")
        print("  python3 backlink_outreach_engine.py check <URL>")
    else:
        cmd = sys.argv[1].lower()
        if cmd == "summary":
            show_summary()
        elif cmd == "pitch" and len(sys.argv) > 2:
            get_outreach_pitch(int(sys.argv[2]))
        elif cmd == "check" and len(sys.argv) > 2:
            check_live_link(sys.argv[2])
        else:
            show_summary()
