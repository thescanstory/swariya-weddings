# -*- coding: utf-8 -*-
"""
Swariya Weddings - Segmented 8-Cluster XML Sitemap & Master Index Generator (500 Targets)
"""

import os
from datetime import datetime
from micromarkets_500_data import build_500_dataset

def generate_sitemaps():
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    base_url = "https://swariyaweddings.com"
    today = datetime.now().strftime("%Y-%m-%d")
    dataset = build_500_dataset()

    # 1. Main Core Pages
    main_pages = [
        {"loc": f"{base_url}/", "priority": "1.0", "changefreq": "daily"},
        {"loc": f"{base_url}/about.html", "priority": "0.85", "changefreq": "monthly"},
        {"loc": f"{base_url}/services.html", "priority": "0.90", "changefreq": "weekly"},
        {"loc": f"{base_url}/venues.html", "priority": "0.90", "changefreq": "weekly"},
        {"loc": f"{base_url}/gallery.html", "priority": "0.85", "changefreq": "weekly"},
        {"loc": f"{base_url}/reviews.html", "priority": "0.95", "changefreq": "weekly"},
        {"loc": f"{base_url}/contact.html", "priority": "0.85", "changefreq": "monthly"},
        {"loc": f"{base_url}/wedding-budget-calculator.html", "priority": "0.95", "changefreq": "weekly"},
        {"loc": f"{base_url}/wedding-brief-builder.html", "priority": "0.95", "changefreq": "weekly"},
        {"loc": f"{base_url}/venue-finder.html", "priority": "0.95", "changefreq": "weekly"},
        {"loc": f"{base_url}/client-portal.html", "priority": "0.90", "changefreq": "weekly"},
        {"loc": f"{base_url}/ask.html", "priority": "0.85", "changefreq": "weekly"},
        {"loc": f"{base_url}/destination-wedding-planner-india.html", "priority": "0.95", "changefreq": "weekly"},
        {"loc": f"{base_url}/bengaluru-wedding-cost-guide-2026.html", "priority": "0.90", "changefreq": "weekly"},
    ]

    # Write sitemap-main.xml
    main_xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in main_pages:
        main_xml_lines.append(f"""  <url>
    <loc>{p['loc']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{p['changefreq']}</changefreq>
    <priority>{p['priority']}</priority>
  </url>""")
    main_xml_lines.append('</urlset>')
    
    with open(os.path.join(workspace_root, "sitemap-main.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(main_xml_lines))
    print(f"Generated sitemap-main.xml ({len(main_pages)} URLs)")

    # 2. Segmented Thematic Sub-Sitemaps
    sub_sitemaps_map = {
        "bengaluru": ("sitemap-bengaluru.xml", "0.90"),
        "rajasthan": ("sitemap-rajasthan.xml", "0.90"),
        "goa-kerala": ("sitemap-goa-kerala.xml", "0.90"),
        "karnataka-destinations": ("sitemap-karnataka-destinations.xml", "0.85"),
        "north-hills": ("sitemap-north-hills.xml", "0.85"),
        "metros": ("sitemap-metros.xml", "0.85"),
        "cultural": ("sitemap-cultural.xml", "0.85"),
    }

    sub_sitemaps_created = ["sitemap-main.xml"]

    for cat_key, (filename, prio) in sub_sitemaps_map.items():
        cat_items = [m for m in dataset if m.get("category") == cat_key]
        xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        
        for item in cat_items:
            loc = f"{base_url}/{item['slug']}.html"
            xml_lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{prio}</priority>
  </url>""")
        
        xml_lines.append('</urlset>')
        
        with open(os.path.join(workspace_root, filename), "w", encoding="utf-8") as f:
            f.write("\n".join(xml_lines))
        
        sub_sitemaps_created.append(filename)
        print(f"Generated {filename} ({len(cat_items)} URLs)")

    # 3. Master Sitemap Index (sitemap.xml)
    index_xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for sub in sub_sitemaps_created:
        index_xml_lines.append(f"""  <sitemap>
    <loc>{base_url}/{sub}</loc>
    <lastmod>{today}</lastmod>
  </sitemap>""")
    index_xml_lines.append('</sitemapindex>')

    with open(os.path.join(workspace_root, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_xml_lines))
    print(f"\nGenerated Master sitemap.xml (Sitemap Index containing {len(sub_sitemaps_created)} child sitemaps with 500 total URLs!)")

if __name__ == "__main__":
    generate_sitemaps()
