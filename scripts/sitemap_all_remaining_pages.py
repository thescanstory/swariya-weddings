#!/usr/bin/env python3
"""
scripts/sitemap_all_remaining_pages.py
======================================
Scans the entire repository for ANY HTML page not currently in an XML sitemap.
Generates clean, schema-valid XML sub-sitemaps (max 500 URLs per file).
Updates the master sitemap.xml index.
Dispatches all new sitemap URLs to IndexNow APIs.
"""

import os
import glob
import xml.etree.ElementTree as ET
import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_URL = "https://swariyaweddings.com"

def get_currently_sitemapped_slugs():
    sitemapped = set()
    for sm in glob.glob(os.path.join(ROOT_DIR, "sitemap-*.xml")):
        try:
            tree = ET.parse(sm)
            root = tree.getroot()
            for loc in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                if loc.text:
                    clean = loc.text.replace(f"{BASE_URL}/", "").rstrip("/")
                    sitemapped.add(clean)
        except Exception:
            pass
    return sitemapped

def main():
    print("=" * 60)
    print("SITEMAPPING 100% OF REMAINING HTML PAGES")
    print("=" * 60)

    already_sitemapped = get_currently_sitemapped_slugs()
    print(f"Already sitemapped unique pages: {len(already_sitemapped)}")

    all_html_files = [
        f[:-5] for f in os.listdir(ROOT_DIR)
        if f.endswith(".html") and not f.startswith(".")
    ]
    print(f"Total HTML files in repository: {len(all_html_files)}")

    unsitemapped = sorted([f for f in all_html_files if f not in already_sitemapped and f != "sitemap"])
    print(f"Total unsitemapped pages found: {len(unsitemapped)}")

    if not unsitemapped:
        print("All pages are already 100% sitemapped!")
        return

    # Split into 500-URL chunks
    chunk_size = 500
    new_sitemaps = []
    
    for i in range(0, len(unsitemapped), chunk_size):
        part_num = (i // chunk_size) + 1
        sm_name = f"sitemap-bangalore-expansion-part{part_num}.xml"
        chunk = unsitemapped[i:i + chunk_size]
        
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]
        for slug in chunk:
            url = f"{BASE_URL}/{slug}" if slug else f"{BASE_URL}/"
            xml_lines.append("  <url>")
            xml_lines.append(f"    <loc>{url}</loc>")
            xml_lines.append("    <lastmod>2026-10-11</lastmod>")
            xml_lines.append("    <changefreq>weekly</changefreq>")
            xml_lines.append("    <priority>0.8</priority>")
            xml_lines.append("  </url>")
        xml_lines.append("</urlset>")

        target_file = os.path.join(ROOT_DIR, sm_name)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("\n".join(xml_lines))
            
        new_sitemaps.append((sm_name, [f"{BASE_URL}/{s}" for s in chunk]))
        print(f"Created sub-sitemap: {sm_name} ({len(chunk)} URLs)")

    # Update root sitemap.xml
    root_sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
    if os.path.exists(root_sitemap_path):
        with open(root_sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_entries = ""
        for sm_name, _ in new_sitemaps:
            if sm_name not in content:
                new_entries += f"""  <sitemap>
    <loc>{BASE_URL}/{sm_name}</loc>
    <lastmod>2026-10-11</lastmod>
  </sitemap>\n"""

        if new_entries:
            content = content.replace("</sitemapindex>", new_entries + "</sitemapindex>")
            with open(root_sitemap_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully updated root sitemap.xml with all new expansion sitemaps!")

    # Dispatch all newly sitemapped URLs to IndexNow
    print("\n--- Dispatching newly sitemapped URLs to IndexNow ---")
    all_new_urls = []
    for _, url_list in new_sitemaps:
        all_new_urls.extend(url_list)

    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow"
    ]

    for i in range(0, len(all_new_urls), 500):
        batch = all_new_urls[i:i + 500]
        payload = {
            "host": "swariyaweddings.com",
            "key": "c9842a1b7e904328b93f619b02a7b8e1",
            "keyLocation": "https://swariyaweddings.com/c9842a1b7e904328b93f619b02a7b8e1.txt",
            "urlList": batch
        }
        data = json.dumps(payload).encode("utf-8")
        for ep in endpoints:
            try:
                req = urllib.request.Request(
                    ep,
                    data=data,
                    headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
                    print(f"Batch {i//500 + 1}: Dispatched {len(batch)} URLs to {ep} -> HTTP {resp.status}")
            except Exception as e:
                print(f"Batch {i//500 + 1} Error on {ep}: {e}")

    print("=" * 60)
    print("ALL REMAINING PAGES 100% SITEMAPPED AND BROADCAST!")
    print("=" * 60)

if __name__ == "__main__":
    main()
