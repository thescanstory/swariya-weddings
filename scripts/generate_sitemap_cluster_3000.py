#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
16-Cluster Master XML Sitemap Generator for Swariya Weddings (3,000+ Page Architecture).
Creates clean, categorized sitemaps and a Master Sitemap Index for Google Search Console.
"""

import os
import glob
from micromarkets_3000_data import get_3000_micromarkets

BASE_URL = "https://swariyaweddings.com"
LASTMOD = "2026-09-19"

def generate_sitemaps():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    markets = get_3000_micromarkets()
    
    # 1. Main Core Pages
    core_pages = [
        "",
        "about.html",
        "services.html",
        "venues.html",
        "gallery.html",
        "reviews.html",
        "ask.html",
        "wedding-budget-calculator.html",
        "wedding-brief-builder.html",
        "venue-finder.html",
        "client-portal.html",
        "destination-wedding-planner-india.html",
        "top-luxury-wedding-planners-in-bangalore-comparison-guide.html",
        "bengaluru-wedding-cost-guide-2026.html"
    ]

    # Additional editorial / venue pages if they exist
    existing_venues = [
        os.path.relpath(p, root_dir) for p in glob.glob(os.path.join(root_dir, "venues", "*.html"))
        if not p.endswith("template.html") and not p.endswith("index.html")
    ]
    existing_blogs = [
        os.path.relpath(p, root_dir) for p in glob.glob(os.path.join(root_dir, "blog", "**", "*.html"), recursive=True)
        if not p.endswith("template.html") and not p.endswith("index.html")
    ]

    clusters = {
        "sitemap-main.xml": [],
        "sitemap-venues-luxury.xml": [],
        "sitemap-bengaluru-corridors.xml": [],
        "sitemap-rajasthan-palaces.xml": [],
        "sitemap-goa-coastal.xml": [],
        "sitemap-kerala-backwaters.xml": [],
        "sitemap-karnataka-escapes.xml": [],
        "sitemap-north-hills.xml": [],
        "sitemap-western-escapes.xml": [],
        "sitemap-mumbai-mmr.xml": [],
        "sitemap-delhi-ncr.xml": [],
        "sitemap-hyderabad-telangana.xml": [],
        "sitemap-chennai-tamilnadu.xml": [],
        "sitemap-pune-kolkata.xml": [],
        "sitemap-cultural-traditions.xml": [],
        "sitemap-cost-guides-2026.xml": []
    }

    # Populate main sitemap
    for cp in core_pages:
        clean_cp = cp.replace(".html", "") if cp.endswith(".html") else cp
        url = f"{BASE_URL}/{clean_cp}" if clean_cp else f"{BASE_URL}/"
        clusters["sitemap-main.xml"].append((url, "1.0" if not clean_cp else "0.9", "weekly"))

    for vp in existing_venues:
        clean_vp = vp.replace(".html", "") if vp.endswith(".html") else vp
        clusters["sitemap-venues-luxury.xml"].append((f"{BASE_URL}/{clean_vp}", "0.85", "monthly"))

    for bp in existing_blogs:
        clean_bp = bp.replace(".html", "") if bp.endswith(".html") else bp
        clusters["sitemap-cost-guides-2026.xml"].append((f"{BASE_URL}/{clean_bp}", "0.8", "monthly"))

    # Map category to sitemap file
    cat_mapping = {
        "venues-luxury": "sitemap-venues-luxury.xml",
        "bengaluru-corridors": "sitemap-bengaluru-corridors.xml",
        "rajasthan-palaces": "sitemap-rajasthan-palaces.xml",
        "goa-coastal": "sitemap-goa-coastal.xml",
        "kerala-backwaters": "sitemap-kerala-backwaters.xml",
        "karnataka-escapes": "sitemap-karnataka-escapes.xml",
        "north-hills": "sitemap-north-hills.xml",
        "western-escapes": "sitemap-western-escapes.xml",
        "mumbai-mmr": "sitemap-mumbai-mmr.xml",
        "delhi-ncr": "sitemap-delhi-ncr.xml",
        "hyderabad-telangana": "sitemap-hyderabad-telangana.xml",
        "chennai-tamilnadu": "sitemap-chennai-tamilnadu.xml",
        "pune-kolkata": "sitemap-pune-kolkata.xml",
        "cultural-traditions": "sitemap-cultural-traditions.xml",
        "cost-guides-2026": "sitemap-cost-guides-2026.xml"
    }

    for m in markets:
        cat = m.get("category", "bengaluru-corridors")
        target_sitemap = cat_mapping.get(cat, "sitemap-bengaluru-corridors.xml")
        page_url = f"{BASE_URL}/{m['slug']}"
        clusters[target_sitemap].append((page_url, "0.85", "monthly"))

    # Write each child sitemap
    total_urls = 0
    child_sitemap_names = []
    for sitemap_name, urls in clusters.items():
        if not urls:
            continue
        child_sitemap_names.append(sitemap_name)
        total_urls += len(urls)
        xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        for loc, prio, freq in urls:
            xml_content.append('  <url>')
            xml_content.append(f'    <loc>{loc}</loc>')
            xml_content.append(f'    <lastmod>{LASTMOD}</lastmod>')
            xml_content.append(f'    <changefreq>{freq}</changefreq>')
            xml_content.append(f'    <priority>{prio}</priority>')
            xml_content.append('  </url>')
        xml_content.append('</urlset>')
        
        file_path = os.path.join(root_dir, sitemap_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(xml_content))
        print(f"Created {sitemap_name}: {len(urls)} URLs")

    # Generate Master Sitemap Index
    index_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    index_xml.append('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for s_name in child_sitemap_names:
        index_xml.append('  <sitemap>')
        index_xml.append(f'    <loc>{BASE_URL}/{s_name}</loc>')
        index_xml.append(f'    <lastmod>{LASTMOD}</lastmod>')
        index_xml.append('  </sitemap>')
    index_xml.append('</sitemapindex>')

    master_path = os.path.join(root_dir, "sitemap.xml")
    with open(master_path, "w", encoding="utf-8") as f:
        f.write("\n".join(index_xml))

    print(f"\n✅ Master sitemap.xml created with {len(child_sitemap_names)} child sitemaps and {total_urls} total indexed URLs!")

if __name__ == "__main__":
    generate_sitemaps()
