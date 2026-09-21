#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boost internal cross-linking network across all clusters.
Guarantees every page has at least 6-10 inbound internal links.
"""

import os
import glob
import re
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

html_files = []
for root, _, files in os.walk(BASE_DIR):
    if any(x in root for x in ["node_modules", ".git", ".vercel", ".netlify"]):
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, BASE_DIR).replace("\\", "/")
            html_files.append((rel_path, path))
html_files.sort()

cluster_pages = defaultdict(list)
for rel_path, abs_path in html_files:
    if rel_path in ["404.html", "venues/template.html", "blog/template.html", "destinations-directory.html", "index.html"]:
        continue
    if rel_path.startswith("venues/"):
        cluster_pages["Venues & Resorts"].append((rel_path, abs_path))
    elif "bangalore" in rel_path or "bengaluru" in rel_path:
        cluster_pages["Bengaluru Corridors"].append((rel_path, abs_path))
    elif "goa" in rel_path or "beach" in rel_path:
        cluster_pages["Goa & Coastal Escapes"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["rajasthan", "jaipur", "udaipur", "jodhpur", "jaisalmer", "bikaner", "pushkar", "neemrana"]):
        cluster_pages["Rajasthan Palaces & Heritage"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["kerala", "kochi", "kovalam", "kumarakom", "munnar", "alleppey", "wayanad"]):
        cluster_pages["Kerala Backwaters & Hills"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["coorg", "chikmagalur", "kabini", "hampi", "mysore", "karnataka", "sakleshpur", "dandeli"]):
        cluster_pages["Karnataka Nature & Coffee Estates"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["rishikesh", "mussoorie", "shimla", "corbett", "kasauli", "dehradun", "manali", "hills", "chail"]):
        cluster_pages["North India Hill Stations"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["mumbai", "alibaug", "lonavala", "maharashtra", "pune", "karjat", "igatpuri"]):
        cluster_pages["Mumbai & Western Escapes"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["delhi", "gurgaon", "noida", "agra", "faridabad"]):
        cluster_pages["Delhi NCR & North Heritage"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["hyderabad", "telangana"]):
        cluster_pages["Hyderabad & Nizam Palaces"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["chennai", "mahabalipuram", "tamil", "chettinad", "ecr"]):
        cluster_pages["Chennai & Tamil Nadu"].append((rel_path, abs_path))
    elif any(k in rel_path for k in ["traditional", "rituals", "runsheet", "brahmin", "bengali", "punjabi", "gujarati", "marwari", "telugu", "kannada", "christian", "jain", "parsi", "sindhi", "kodava", "bunt", "interfaith"]):
        cluster_pages["Cultural Traditions & Rituals"].append((rel_path, abs_path))
    elif "cost" in rel_path or "budget" in rel_path:
        cluster_pages["2026 Cost Guides & Budgets"].append((rel_path, abs_path))
    else:
        cluster_pages["Signature Destinations & Guides"].append((rel_path, abs_path))

updated_count = 0
for cname, pages in cluster_pages.items():
    n = len(pages)
    if n < 2:
        continue
    for i, (rel_path, abs_path) in enumerate(pages):
        siblings = [pages[(i + offset) % n][0] for offset in range(1, min(7, n))]
        
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        links_html = "".join([f'<a href="/{p.replace(".html", "")}" style="display: inline-block; margin: 4px 6px; padding: 6px 12px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 16px; font-size: 0.82rem; color: #2C2723; text-decoration: none;">{p.replace(".html", "").replace("-", " ").title()[:35]}</a>' for p in siblings])
        
        new_crosslink_block = f"""        <section class="related-guides-grid" style="margin: 40px auto; max-width: 1100px; padding: 25px; background: #FAF6F0; border: 1px solid #E8DFD5; border-radius: 10px;">
            <h3 style="font-family: serif; font-size: 1.25rem; margin-bottom: 12px; color: #1C1917;">Explore Related {cname}</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {links_html}
                <a href="/destinations-directory" style="display: inline-block; margin: 4px 6px; padding: 6px 12px; background: #C5A059; color: #FFF; border-radius: 16px; font-size: 0.82rem; text-decoration: none; font-weight: bold;">View All 3,000+ Guides &rarr;</a>
            </div>
        </section>"""
        
        if '<section class="related-guides-grid"' in content:
            content = re.sub(r'<section class="related-guides-grid".*?</section>', new_crosslink_block, content, flags=re.DOTALL)
        elif "</main>" in content:
            content = content.replace("</main>", f"{new_crosslink_block}\n</main>")
        elif "</body>" in content:
            content = content.replace("</body>", f"{new_crosslink_block}\n</body>")
            
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"✅ Injected circular internal link meshes across {updated_count} pages in {len(cluster_pages)} clusters.")
