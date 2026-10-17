#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject contextual high-authority banner into Bangalore venue guides
funneling PageRank and search traffic directly into /wedding-planners-in-bangalore.
"""

import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BANGALORE_VENUES = [
    "venues/the-tamarind-tree-bangalore.html",
    "venues/taj-west-end-bengaluru.html",
    "venues/the-leela-palace-bengaluru.html",
    "venues/amita-rasa-bangalore.html",
    "venues/gayatri-vihar-palace-grounds.html",
    "venues/itc-gardenia-bengaluru.html",
    "venues/jw-marriott-bengaluru.html",
    "venues/templetree-leisure-bangalore.html",
    "venues/the-grape-garden-bangalore.html",
    "venues/clarks-exotica-resort-bangalore-wedding.html",
    "venues/angsana-oasis-resort-bangalore-wedding.html",
    "venues/signature-club-resort-bangalore.html",
    "venues/miraya-greens-bangalore.html",
    "venues/moongate-bangalore.html",
    "venues/jade-735-bangalore.html",
    "venues/royal-palms-bangalore.html",
    "venues/royalton-leisure-bangalore.html",
    "venues/samavana-wedding-venue-bangalore.html",
    "venues/shankaraa-foundation-bangalore.html",
    "venues/white-mist-bangalore.html",
    "venues/windflower-prakruthi-bangalore.html",
    "venues/wiwaha-wedding-venue-bangalore.html",
    "venues/tharavadu-mane-bangalore.html",
    "venues/gitanjali-wedding-venue-bangalore.html",
    "venues/goldfinch-retreat-bangalore.html",
    "venues/area-83-bangalore.html"
]

BADGE_HTML = """
        <!-- Featured Bangalore Wedding Planner Authority Callout -->
        <div style="background: #FDFBF7; border: 1.5px solid #D9B872; border-left: 5px solid #8B1A1A; border-radius: 8px; padding: 16px 22px; margin: 25px 0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; box-shadow: 0 4px 15px rgba(217, 184, 114, 0.12);">
            <div>
                <div style="font-weight: 700; color: #8B1A1A; font-size: 1rem; margin-bottom: 2px;">✦ Swariya Weddings — Premier Luxury Wedding Planners in Bangalore</div>
                <div style="font-size: 0.9rem; color: #555;">Planning your celebration at this venue? We provide 0% vendor markups, 3D CAD mandap renders & turnkey coordination.</div>
            </div>
            <a href="/wedding-planners-in-bangalore" style="background: #8B1A1A; color: #FFF; padding: 10px 18px; border-radius: 6px; font-size: 0.88rem; font-weight: 700; text-decoration: none; display: inline-block; white-space: nowrap;">Best Wedding Planners in Bangalore &rarr;</a>
        </div>
"""

def inject():
    count = 0
    for v in BANGALORE_VENUES:
        fpath = os.path.join(BASE_DIR, v)
        if not os.path.exists(fpath):
            continue
            
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fh:
            c = fh.read()
            
        if "Featured Bangalore Wedding Planner Authority Callout" in c:
            continue
            
        # Target injection point: after <h1> or after the venue subtitle paragraph
        if "</h1>" in c:
            # Insert after the first </p> that follows <h1>
            h1_idx = c.find("</h1>")
            p_end_idx = c.find("</p>", h1_idx)
            if p_end_idx != -1:
                insert_pos = p_end_idx + 4
                c = c[:insert_pos] + BADGE_HTML + c[insert_pos:]
                with open(fpath, "w", encoding="utf-8") as fh:
                    fh.write(c)
                count += 1
                print(f"✓ Injected authority banner in {v}")
                
    print(f"Successfully injected banner in {count} Bangalore venue guides.")

if __name__ == "__main__":
    inject()
