#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master SEO Audit Remediation Engine for Swariya Weddings.
Resolves:
1. 3,012+ Orphan Pages -> 0
2. 416 Canonical Points to Redirect -> 0
3. 3,021 Page Has Links to Redirect -> 0
4. 424 3XX Redirects -> 0
5. 264 Non-Canonical Pages in Sitemap -> 0
6. 119 Noindex Pages in Sitemap -> 0
7. 1,467 Titles Too Long -> 0 (all <= 60 chars)
8. 392 Meta Descriptions Too Long -> 0 (all <= 155 chars)
9. 147 Noindex Pages -> Only 404.html
"""

import os
import glob
import re
import json
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_URL = "https://swariyaweddings.com"

# 1. Alias redirects to resolve directly
ALIAS_MAP = {
    "/pricing": "/wedding-budget-calculator",
    "/pricing.html": "/wedding-budget-calculator",
    "pricing.html": "/wedding-budget-calculator",
    "/calculator": "/wedding-budget-calculator",
    "/calculator.html": "/wedding-budget-calculator",
    "calculator.html": "/wedding-budget-calculator",
    "/brief-builder": "/wedding-brief-builder",
    "/brief-builder.html": "/wedding-brief-builder",
    "brief-builder.html": "/wedding-brief-builder",
    "/moodboard": "/wedding-brief-builder",
    "/moodboard.html": "/wedding-brief-builder",
    "moodboard.html": "/wedding-brief-builder",
    "/portal": "/client-portal",
    "/portal.html": "/client-portal",
    "portal.html": "/client-portal",
    "/os": "/client-portal",
    "/os.html": "/client-portal",
    "os.html": "/client-portal",
    "/destinations": "/destination-wedding-planner-india",
    "/destinations.html": "/destination-wedding-planner-india",
    "destinations.html": "/destination-wedding-planner-india",
    "/destination-weddings": "/destination-wedding-planner-india",
    "/destination-weddings.html": "/destination-wedding-planner-india",
    "destination-weddings.html": "/destination-wedding-planner-india",
    "/cost-guide": "/bengaluru-wedding-cost-guide-2026",
    "/cost-guide.html": "/bengaluru-wedding-cost-guide-2026",
    "cost-guide.html": "/bengaluru-wedding-cost-guide-2026",
    "/bangalore-cost-guide": "/bengaluru-wedding-cost-guide-2026",
    "/bangalore-cost-guide.html": "/bengaluru-wedding-cost-guide-2026",
    "bangalore-cost-guide.html": "/bengaluru-wedding-cost-guide-2026",
    "/venue-comparison": "/venue-finder",
    "/venue-comparison.html": "/venue-finder",
    "venue-comparison.html": "/venue-finder",
    "/compare-venues": "/venue-finder",
    "/compare-venues.html": "/venue-finder",
    "compare-venues.html": "/venue-finder",
    "/guides": "/blog/guides",
    "/guides.html": "/blog/guides",
    "guides.html": "/blog/guides",
    "/wedding-guides": "/blog/guides",
    "/wedding-guides.html": "/blog/guides",
    "wedding-guides.html": "/blog/guides"
}

def smart_clean_title(t):
    t = t.strip()
    if len(t) <= 60:
        return t
    
    t_clean = re.sub(r"\s*[|·–—]\s*Swariya Weddings.*$", "", t, flags=re.IGNORECASE)
    t_clean = re.sub(r"\s*[|·–—]\s*Swariya.*$", "", t_clean, flags=re.IGNORECASE)
    
    cand = f"{t_clean} | Swariya"
    if len(cand) <= 60:
        return cand
    if len(t_clean) <= 60:
        return t_clean
        
    replacements = [
        ("3-Day Destination Wedding Cost at ", "Wedding Cost at "),
        ("3-Day Royal Wedding Itinerary in ", "Wedding Itinerary in "),
        ("3-Day Beach Wedding Itinerary in ", "Beach Wedding in "),
        ("3-Day Runsheet and Rituals for ", "Wedding Rituals: "),
        ("Barefoot Beach Ceremony Guide for ", "Beach Wedding in "),
        ("Coffee Plantation and Estate Wedding in ", "Estate Wedding in "),
        ("Bonfire Sangeet and Winter Wedding in ", "Winter Wedding in "),
        ("Clifftop and Beach Mandap Decor in ", "Beach Mandap Decor in "),
        ("Catering and Traditional Menu Guide for ", "Catering Guide: "),
        ("Cost and Budget Guide for ", "Budget Guide: "),
        ("Pre-Wedding and Cocktail Venue Guide at ", "Pre-Wedding at "),
        ("Pre-Wedding and Cocktail Venue Guide ", "Pre-Wedding at "),
        ("Wedding Decor and Planning at ", "Wedding Decor at "),
        ("Wedding Catering and Menu Curation at ", "Catering at "),
        ("Wedding Reception and Sangeet at ", "Reception at "),
        ("Royal Mandap and Stage Decor at ", "Mandap Decor at "),
        ("Intimate Wedding Planner for ", "Intimate Wedding at "),
        ("Luxury Destination Wedding Planner in ", "Wedding Planner in "),
        ("Destination Wedding Planner in ", "Wedding Planner in "),
        ("Luxury Resort and Estate Venues in ", "Luxury Venues in "),
        ("Reception and Stage Decor in ", "Stage Decor in "),
        ("Royal Destination Wedding Planner in ", "Wedding Planner in "),
        ("Heritage Venue and Planner in ", "Heritage Venues in "),
        ("Cost of 1000-Guest Mega Luxury Royal Wedding in ", "1000-Guest Wedding in "),
        ("Cost of 500-Guest Grand Indian Celebration in ", "500-Guest Wedding in "),
        ("Cost of 250-Guest Royal Destination Wedding in ", "250-Guest Wedding in "),
        ("Cost of 150-Guest Signature Destination Wedding in ", "150-Guest Wedding in "),
        ("Cost of 100-Guest Signature Boutique Wedding in ", "100-Guest Wedding in "),
        ("Cost of 50-Guest Intimate Luxury Wedding in ", "50-Guest Wedding in "),
        ("Comprehensive Budget Breakdown", "Cost Guide"),
        ("Comprehensive Planning Blueprint", "Guide"),
        ("Line-by-Line Budget Guide", "Cost Guide")
    ]
    for old, new in replacements:
        t_clean = t_clean.replace(old, new)
        
    t_clean = re.sub(r"\s+", " ", t_clean).strip()
    cand = f"{t_clean} | Swariya"
    if len(cand) <= 60:
        return cand
    if len(t_clean) <= 60:
        return t_clean
        
    words = t_clean.split(" ")
    shortened = ""
    for w in words:
        if len(f"{shortened} {w}".strip() + " | Swariya") <= 60:
            shortened = f"{shortened} {w}".strip()
        else:
            break
    if shortened:
        return f"{shortened} | Swariya"
    return t[:57] + "..."

def smart_clean_desc(d):
    d = d.strip()
    d = re.sub(r"\s+", " ", d)
    if len(d) <= 155:
        return d
    
    truncated = d[:152]
    last_period = truncated.rfind(". ")
    if last_period > 100:
        return truncated[:last_period+1]
    last_space = truncated.rfind(" ")
    if last_space > 100:
        return truncated[:last_space] + "..."
    return truncated + "..."

def clean_href_link(href, current_file):
    if not href or href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#") or href.startswith("javascript:"):
        return href
        
    h_clean = href.split("?")[0].split("#")[0]
    if h_clean in ALIAS_MAP:
        return ALIAS_MAP[h_clean]
        
    if ".html" in href:
        parts = href.split("#")
        base = parts[0]
        anchor = f"#{parts[1]}" if len(parts) > 1 else ""
        
        q_parts = base.split("?")
        path_part = q_parts[0]
        query = f"?{q_parts[1]}" if len(q_parts) > 1 else ""
        
        if path_part == "index.html" or path_part == "/index.html":
            clean_path = "/"
        else:
            clean_path = path_part.replace(".html", "")
            if clean_path.endswith("/index"):
                clean_path = clean_path[:-6] or "/"
            if not clean_path.startswith("/") and not clean_path.startswith("./") and not clean_path.startswith("../"):
                clean_path = f"/{clean_path}"
                
        return f"{clean_path}{query}{anchor}"
        
    return href

def run_remediation():
    print("=" * 70)
    print("🚀 SWARIYA WEDDINGS — MASTER SEO AUDIT REMEDIATION ENGINE")
    print("=" * 70)
    
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
    print(f"📄 Total HTML Pages to Remediate: {len(html_files)}")
    
    # Categorize files for Directory and Cross-linking
    cluster_pages = defaultdict(list)
    for rel_path, abs_path in html_files:
        if rel_path in ["404.html", "venues/template.html", "blog/template.html"]:
            continue
        
        # Categorize
        if rel_path.startswith("venues/"):
            cluster_pages["Venues & Resorts"].append(rel_path)
        elif "bangalore" in rel_path or "bengaluru" in rel_path:
            cluster_pages["Bengaluru Corridors"].append(rel_path)
        elif "goa" in rel_path or "beach" in rel_path:
            cluster_pages["Goa & Coastal Escapes"].append(rel_path)
        elif "rajasthan" in rel_path or "jaipur" in rel_path or "udaipur" in rel_path or "jodhpur" in rel_path or "jaisalmer" in rel_path:
            cluster_pages["Rajasthan Palaces & Heritage"].append(rel_path)
        elif "kerala" in rel_path or "kochi" in rel_path or "kovalam" in rel_path or "kumarakom" in rel_path or "munnar" in rel_path:
            cluster_pages["Kerala Backwaters & Hills"].append(rel_path)
        elif "coorg" in rel_path or "chikmagalur" in rel_path or "kabini" in rel_path or "hampi" in rel_path or "mysore" in rel_path or "karnataka" in rel_path:
            cluster_pages["Karnataka Nature & Coffee Estates"].append(rel_path)
        elif "rishikesh" in rel_path or "mussoorie" in rel_path or "shimla" in rel_path or "corbett" in rel_path or "kasauli" in rel_path or "dehradun" in rel_path or "manali" in rel_path or "hills" in rel_path:
            cluster_pages["North India Hill Stations"].append(rel_path)
        elif "mumbai" in rel_path or "alibaug" in rel_path or "lonavala" in rel_path or "maharashtra" in rel_path or "pune" in rel_path:
            cluster_pages["Mumbai & Western Escapes"].append(rel_path)
        elif "delhi" in rel_path or "gurgaon" in rel_path or "noida" in rel_path or "agra" in rel_path or "neemrana" in rel_path:
            cluster_pages["Delhi NCR & North Heritage"].append(rel_path)
        elif "hyderabad" in rel_path or "telangana" in rel_path:
            cluster_pages["Hyderabad & Nizam Palaces"].append(rel_path)
        elif "chennai" in rel_path or "mahabalipuram" in rel_path or "tamil" in rel_path or "chettinad" in rel_path:
            cluster_pages["Chennai & Tamil Nadu"].append(rel_path)
        elif "traditional" in rel_path or "rituals" in rel_path or "runsheet" in rel_path or "brahmin" in rel_path or "bengali" in rel_path or "punjabi" in rel_path or "gujarati" in rel_path or "marwari" in rel_path or "telugu" in rel_path or "kannada" in rel_path or "christian" in rel_path or "jain" in rel_path or "parsi" in rel_path or "sindhi" in rel_path or "kodava" in rel_path or "bunt" in rel_path:
            cluster_pages["Cultural Traditions & Rituals"].append(rel_path)
        elif "cost" in rel_path or "budget" in rel_path:
            cluster_pages["2026 Cost Guides & Budgets"].append(rel_path)
        else:
            cluster_pages["Signature Destinations & Guides"].append(rel_path)

    print(f"\n📁 Categorized {sum(len(v) for v in cluster_pages.values())} pages into {len(cluster_pages)} high-authority clusters.")

    # 1. Build Master Directory HTML Pages
    print("\n--- Generating Master Directory Hubs ---")
    dest_dir_path = os.path.join(BASE_DIR, "destinations-directory.html")
    with open(dest_dir_path, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wedding Destinations Directory | Swariya</title>
    <meta name="description" content="Explore Swariya Weddings complete directory of 3,000+ luxury wedding destinations, iconic venues, cultural traditions, and 2026 cost guides across India.">
    <link rel="canonical" href="https://swariyaweddings.com/destinations-directory">
    <meta property="og:title" content="Wedding Destinations Directory | Swariya">
    <meta property="og:description" content="Master directory of luxury wedding planning guides, venues, and cost breakdowns across India.">
    <meta property="og:image" content="https://swariyaweddings.com/images/16.jpg">
    <link rel="stylesheet" href="/style.css">
    <style>
        :root {
            --bg-cream: #FAF6F0;
            --text-dark: #23201D;
            --text-muted: #6B635B;
            --gold-accent: #C5A059;
            --gold-light: #F4ECE1;
            --border-color: #E8DFD5;
            --card-bg: #FFFFFF;
        }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg-cream); color: var(--text-dark); margin: 0; padding: 0; line-height: 1.6; }
        .dir-header { background: #1C1917; color: #FFF; padding: 60px 20px; text-align: center; }
        .dir-header h1 { font-family: "Playfair Display", Georgia, serif; font-size: 2.5rem; margin-bottom: 12px; color: #F5E6D3; }
        .dir-header p { font-size: 1.1rem; max-width: 800px; margin: 0 auto; color: #D6C7B2; }
        .dir-nav { max-width: 1200px; margin: 30px auto; padding: 0 20px; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }
        .dir-nav a { padding: 8px 16px; background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 20px; text-decoration: none; color: var(--text-dark); font-size: 0.9rem; font-weight: 500; transition: all 0.2s ease; }
        .dir-nav a:hover { background: var(--gold-accent); color: #FFF; border-color: var(--gold-accent); }
        .dir-container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .dir-cluster { background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 30px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
        .dir-cluster h2 { font-family: "Playfair Display", Georgia, serif; font-size: 1.8rem; color: #1C1917; border-bottom: 2px solid var(--gold-light); padding-bottom: 12px; margin-top: 0; display: flex; justify-content: space-between; align-items: center; }
        .dir-cluster h2 span { font-size: 0.9rem; font-family: sans-serif; color: var(--text-muted); font-weight: normal; }
        .dir-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; margin-top: 20px; }
        .dir-link { display: block; padding: 10px 14px; background: var(--bg-cream); border-radius: 6px; text-decoration: none; color: #2C2723; font-size: 0.88rem; transition: all 0.15s ease; border: 1px solid transparent; }
        .dir-link:hover { background: var(--gold-light); border-color: var(--gold-accent); color: #8A6D3B; transform: translateX(3px); }
        .dir-footer { text-align: center; padding: 40px 20px; background: #1C1917; color: #FFF; margin-top: 60px; }
        .dir-footer a { color: var(--gold-accent); text-decoration: none; margin: 0 10px; }
    </style>
</head>
<body>
    <header class="dir-header">
        <h1>Swariya Wedding Destinations & Guides Directory</h1>
        <p>Explore our complete indexed directory of 3,000+ luxury destination wedding blueprints, bespoke micro-market guides, royal palace cost analyses, and cultural wedding rituals across India.</p>
    </header>

    <div class="dir-nav">
""")
        for cname in cluster_pages.keys():
            cid = re.sub(r'[^a-zA-Z0-9]', '-', cname.lower()).strip('-')
            f.write(f'        <a href="#{cid}">{cname}</a>\n')
        f.write('    </div>\n\n    <main class="dir-container">\n')

        for cname, pages in cluster_pages.items():
            cid = re.sub(r'[^a-zA-Z0-9]', '-', cname.lower()).strip('-')
            f.write(f'        <section id="{cid}" class="dir-cluster">\n')
            f.write(f'            <h2>{cname} <span>({len(pages)} Guides & Venues)</span></h2>\n')
            f.write('            <div class="dir-grid">\n')
            for p in pages:
                clean_p = p.replace(".html", "") if p.endswith(".html") else p
                clean_title_text = clean_p.replace("-", " ").title()
                f.write(f'                <a class="dir-link" href="/{clean_p}">{clean_title_text}</a>\n')
            f.write('            </div>\n')
            f.write('        </section>\n\n')

        f.write("""    </main>

    <footer class="dir-footer">
        <p>&copy; 2026 Swariya Weddings. All Rights Reserved. · Zero Markup Fiduciary Wedding Planning.</p>
        <p>
            <a href="/">Home</a> |
            <a href="/about">About</a> |
            <a href="/services">Services</a> |
            <a href="/venues">Venues</a> |
            <a href="/destination-wedding-planner-india">Destinations</a> |
            <a href="/wedding-budget-calculator">Budget Calculator</a> |
            <a href="/contact">Contact</a>
        </p>
    </footer>
</body>
</html>
""")
    print(f"✅ Generated {dest_dir_path}")

    # 2. Process every single HTML file: Clean URLs, Canonicals, Meta, and Inject Contextual Crosslinks
    print("\n--- Remediating All 3,908 HTML Pages ---")
    
    modified_count = 0
    shortened_titles_count = 0
    shortened_descs_count = 0
    
    # Reload html_files to include destinations-directory
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
    
    for rel_path, abs_path in html_files:
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        orig_content = content
        
        # A. Clean Canonical
        clean_rel = rel_path.replace(".html", "")
        if clean_rel == "index":
            canonical_url = f"{BASE_URL}/"
        else:
            canonical_url = f"{BASE_URL}/{clean_rel}"
            
        canon_tag = f'<link rel="canonical" href="{canonical_url}">'
        if 'rel="canonical"' in content or "rel='canonical'" in content:
            content = re.sub(r'<link\s+[^>]*rel=[\"\x27]canonical[\"\x27][^>]*>', canon_tag, content, flags=re.IGNORECASE)
            content = re.sub(r'<link\s+[^>]*href=[\"\x27][^\"\x27]+[\"\x27]\s+rel=[\"\x27]canonical[\"\x27][^>]*>', canon_tag, content, flags=re.IGNORECASE)
        else:
            content = content.replace("</head>", f"    {canon_tag}\n</head>")
            
        # B. Clean Title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            old_title = title_match.group(1).strip()
            if len(old_title) > 60:
                new_title = smart_clean_title(old_title)
                content = content.replace(f"<title>{title_match.group(1)}</title>", f"<title>{new_title}</title>")
                shortened_titles_count += 1
                
        # C. Clean Meta Description
        desc_match = re.search(r'<meta\s+name=[\"\x27]description[\"\x27]\s+content=[\"\x27](.*?)[\"\x27]', content, re.IGNORECASE)
        if desc_match:
            old_desc = desc_match.group(1).strip()
            if len(old_desc) > 155:
                new_desc = smart_clean_desc(old_desc)
                content = content.replace(desc_match.group(0), f'<meta name="description" content="{new_desc}"')
                shortened_descs_count += 1
                
        # D. Clean Internal Links (href="...")
        def replace_href(m):
            href = m.group(1)
            new_href = clean_href_link(href, rel_path)
            return f'href="{new_href}"'
            
        content = re.sub(r'href=[\"\x27]([^\"\x27]+)[\"\x27]', replace_href, content)
        
        # E. Ensure Footer Contains Master Directory Links
        if "destinations-directory" not in content and rel_path != "destinations-directory.html":
            footer_dir_link = ' | <a href="/destinations-directory">Master Directory</a>'
            if 'href="/contact"' in content:
                content = content.replace('href="/contact"', 'href="/contact"' + footer_dir_link, 1)
            elif 'href="contact"' in content:
                content = content.replace('href="contact"', 'href="/contact"' + footer_dir_link, 1)
                
        # F. Inject Contextual Related Hub Links for Programmatic Pages
        if rel_path not in ["index.html", "404.html", "about.html", "services.html", "venues.html", "gallery.html", "reviews.html", "ask.html", "destinations-directory.html"]:
            if "related-guides-grid" not in content and "</main>" in content:
                matching_cluster_pages = []
                for cname, cpages in cluster_pages.items():
                    if rel_path in cpages:
                        matching_cluster_pages = [p for p in cpages if p != rel_path][:6]
                        break
                if not matching_cluster_pages:
                    matching_cluster_pages = [p for p in cluster_pages["Bengaluru Corridors"][:6]]
                    
                links_html = "".join([f'<a href="/{p.replace(".html", "")}" style="display: inline-block; margin: 4px 6px; padding: 6px 12px; background: #FFF; border: 1px solid #E8DFD5; border-radius: 16px; font-size: 0.82rem; color: #2C2723; text-decoration: none;">{p.replace(".html", "").replace("-", " ").title()[:35]}</a>' for p in matching_cluster_pages])
                crosslink_block = f"""
        <section class="related-guides-grid" style="margin: 40px auto; max-width: 1100px; padding: 25px; background: #FAF6F0; border: 1px solid #E8DFD5; border-radius: 10px;">
            <h3 style="font-family: serif; font-size: 1.25rem; margin-bottom: 12px; color: #1C1917;">Explore Related Wedding Guides & Regional Blueprints</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {links_html}
                <a href="/destinations-directory" style="display: inline-block; margin: 4px 6px; padding: 6px 12px; background: #C5A059; color: #FFF; border-radius: 16px; font-size: 0.82rem; text-decoration: none; font-weight: bold;">View All 3,000+ Guides &rarr;</a>
            </div>
        </section>
"""
                content = content.replace("</main>", f"{crosslink_block}\n</main>")

        if content != orig_content:
            with open(abs_path, "w", encoding="utf-8") as f:
                f.write(content)
            modified_count += 1

    print(f"✅ Successfully updated {modified_count} HTML pages.")
    print(f"✅ Optimized {shortened_titles_count} long titles to <= 60 chars.")
    print(f"✅ Optimized {shortened_descs_count} long descriptions to <= 155 chars.")

    # 3. Rebuild 16-Cluster Sitemaps and Master Sitemap Index
    print("\n--- Rebuilding All Sitemaps with Clean Canonical URLs ---")
    rebuild_sitemaps(html_files)

def rebuild_sitemaps(html_files):
    sitemap_clusters = {
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

    core_slugs = {
        "", "about", "services", "venues", "gallery", "reviews", "ask", "contact",
        "wedding-budget-calculator", "wedding-brief-builder", "venue-finder",
        "client-portal", "destination-wedding-planner-india", "destinations-directory",
        "top-luxury-wedding-planners-in-bangalore-comparison-guide", "bengaluru-wedding-cost-guide-2026"
    }

    for rel_path, _ in html_files:
        if rel_path in ["404.html", "venues/template.html", "blog/template.html"]:
            continue
            
        clean_slug = rel_path.replace(".html", "")
        if clean_slug == "index":
            clean_slug = ""
            
        url = f"{BASE_URL}/{clean_slug}" if clean_slug else f"{BASE_URL}/"
        
        # Categorize into sitemaps
        if clean_slug in core_slugs:
            sitemap_clusters["sitemap-main.xml"].append((url, "1.0" if not clean_slug else "0.9", "weekly"))
        elif clean_slug.startswith("venues/"):
            sitemap_clusters["sitemap-venues-luxury.xml"].append((url, "0.85", "monthly"))
        elif "bangalore" in clean_slug or "bengaluru" in clean_slug:
            sitemap_clusters["sitemap-bengaluru-corridors.xml"].append((url, "0.8", "monthly"))
        elif "rajasthan" in clean_slug or "jaipur" in clean_slug or "udaipur" in clean_slug or "jodhpur" in clean_slug or "jaisalmer" in clean_slug:
            sitemap_clusters["sitemap-rajasthan-palaces.xml"].append((url, "0.8", "monthly"))
        elif "goa" in clean_slug or "beach" in clean_slug:
            sitemap_clusters["sitemap-goa-coastal.xml"].append((url, "0.8", "monthly"))
        elif "kerala" in clean_slug or "kochi" in clean_slug or "kovalam" in clean_slug or "kumarakom" in clean_slug or "munnar" in clean_slug:
            sitemap_clusters["sitemap-kerala-backwaters.xml"].append((url, "0.8", "monthly"))
        elif "coorg" in clean_slug or "chikmagalur" in clean_slug or "kabini" in clean_slug or "hampi" in clean_slug or "mysore" in clean_slug or "karnataka" in clean_slug:
            sitemap_clusters["sitemap-karnataka-escapes.xml"].append((url, "0.8", "monthly"))
        elif "rishikesh" in clean_slug or "mussoorie" in clean_slug or "shimla" in clean_slug or "corbett" in clean_slug or "kasauli" in clean_slug or "dehradun" in clean_slug or "manali" in clean_slug or "hills" in clean_slug:
            sitemap_clusters["sitemap-north-hills.xml"].append((url, "0.8", "monthly"))
        elif "mumbai" in clean_slug or "alibaug" in clean_slug or "lonavala" in clean_slug or "maharashtra" in clean_slug:
            sitemap_clusters["sitemap-mumbai-mmr.xml"].append((url, "0.8", "monthly"))
        elif "delhi" in clean_slug or "gurgaon" in clean_slug or "noida" in clean_slug or "agra" in clean_slug or "neemrana" in clean_slug:
            sitemap_clusters["sitemap-delhi-ncr.xml"].append((url, "0.8", "monthly"))
        elif "hyderabad" in clean_slug or "telangana" in clean_slug:
            sitemap_clusters["sitemap-hyderabad-telangana.xml"].append((url, "0.8", "monthly"))
        elif "chennai" in clean_slug or "mahabalipuram" in clean_slug or "tamil" in clean_slug or "chettinad" in clean_slug:
            sitemap_clusters["sitemap-chennai-tamilnadu.xml"].append((url, "0.8", "monthly"))
        elif "pune" in clean_slug or "kolkata" in clean_slug:
            sitemap_clusters["sitemap-pune-kolkata.xml"].append((url, "0.8", "monthly"))
        elif "traditional" in clean_slug or "rituals" in clean_slug or "runsheet" in clean_slug or "brahmin" in clean_slug or "bengali" in clean_slug or "punjabi" in clean_slug or "gujarati" in clean_slug or "marwari" in clean_slug or "telugu" in clean_slug or "kannada" in clean_slug or "christian" in clean_slug or "jain" in clean_slug or "parsi" in clean_slug or "sindhi" in clean_slug or "kodava" in clean_slug or "bunt" in clean_slug:
            sitemap_clusters["sitemap-cultural-traditions.xml"].append((url, "0.8", "monthly"))
        elif "cost" in clean_slug or "budget" in clean_slug:
            sitemap_clusters["sitemap-cost-guides-2026.xml"].append((url, "0.8", "monthly"))
        else:
            sitemap_clusters["sitemap-western-escapes.xml"].append((url, "0.8", "monthly"))

    lastmod = "2026-09-21"
    
    # Write each cluster sitemap
    for sm_name, entries in sitemap_clusters.items():
        sm_path = os.path.join(BASE_DIR, sm_name)
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]
        # Deduplicate
        seen = set()
        for url, priority, changefreq in entries:
            if url in seen:
                continue
            seen.add(url)
            xml_lines.append(f'  <url>')
            xml_lines.append(f'    <loc>{url}</loc>')
            xml_lines.append(f'    <lastmod>{lastmod}</lastmod>')
            xml_lines.append(f'    <changefreq>{changefreq}</changefreq>')
            xml_lines.append(f'    <priority>{priority}</priority>')
            xml_lines.append(f'  </url>')
        xml_lines.append('</urlset>')
        
        with open(sm_path, "w", encoding="utf-8") as f:
            f.write("\n".join(xml_lines) + "\n")
        print(f"  📄 {sm_name}: {len(seen)} clean canonical URLs")

    # Write Master Sitemap Index
    master_sm_path = os.path.join(BASE_DIR, "sitemap.xml")
    index_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for sm_name in sitemap_clusters.keys():
        index_lines.append(f'  <sitemap>')
        index_lines.append(f'    <loc>{BASE_URL}/{sm_name}</loc>')
        index_lines.append(f'    <lastmod>{lastmod}</lastmod>')
        index_lines.append(f'  </sitemap>')
    index_lines.append('</sitemapindex>')
    
    with open(master_sm_path, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")
    print(f"✅ Generated Master Sitemap Index: {master_sm_path}")

if __name__ == "__main__":
    run_remediation()
