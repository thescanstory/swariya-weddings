#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instant IndexNow Automation Script for Swariya Weddings.
Generates an IndexNow verification key, deploys it to the root,
and broadcasts all 3,291 URLs across the 16 sitemaps to IndexNow search engine endpoints for immediate crawling.
"""

import os
import json
import urllib.request
import xml.etree.ElementTree as ET
import time
import ssl

HOST = "swariyaweddings.com"
KEY = "swariya7b3d9f1a8e2c45b89a0c12e3f4a6b8d0"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

def setup_key_file():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    key_file_path = os.path.join(root_dir, f"{KEY}.txt")
    with open(key_file_path, "w", encoding="utf-8") as f:
        f.write(KEY + "\n")
    print(f"✅ Generated IndexNow Key file: {key_file_path}")
    return key_file_path

def collect_all_urls():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    urls = [
        f"https://{HOST}/",
        f"https://{HOST}/wedding-budget-calculator",
        f"https://{HOST}/wedding-brief-builder",
        f"https://{HOST}/venue-finder",
        f"https://{HOST}/client-portal",
        f"https://{HOST}/reviews"
    ]
    
    # Read all sitemap-*.xml files
    sitemap_files = [f for f in os.listdir(root_dir) if f.startswith("sitemap-") and f.endswith(".xml")]
    
    for sm in sitemap_files:
        path = os.path.join(root_dir, sm)
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            for child in root:
                loc = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                if loc is not None and loc.text:
                    urls.append(loc.text.strip())
        except Exception as e:
            print(f"Error parsing {sm}: {e}")
            
    # Deduplicate while preserving order
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
            
    print(f"✅ Collected {len(deduped)} Unique URLs for Instant Indexing Submission")
    return deduped

def submit_to_indexnow(url_list):
    endpoints = [
        ("api.indexnow.org", "https://api.indexnow.org/indexnow"),
        ("Bing IndexNow", "https://www.bing.com/indexnow"),
        ("Yandex IndexNow", "https://yandex.com/indexnow")
    ]
    
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": url_list
    }
    
    json_data = json.dumps(payload).encode("utf-8")
    ctx = ssl.create_default_context()
    
    print("\n" + "="*60)
    print("🚀 BROADCASTING INSTANT INDEXING REQUESTS TO GLOBAL SEARCH ENGINES")
    print("="*60)
    
    for name, endpoint in endpoints:
        try:
            req = urllib.request.Request(
                endpoint,
                data=json_data,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                    "User-Agent": "SwariyaWeddings-IndexNow/1.0"
                }
            )
            t0 = time.time()
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                elapsed = (time.time() - t0) * 1000
                status = resp.status
                print(f"✅ [{name}] HTTP {status} OK ({elapsed:4.0f}ms) — {len(url_list)} URLs accepted for instant crawl!")
        except urllib.error.HTTPError as e:
            print(f"⚠️ [{name}] Response code {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"❌ [{name}] Error: {e}")
            
    print("="*60)

if __name__ == "__main__":
    setup_key_file()
    urls = collect_all_urls()
    print(f"Ready to broadcast {len(urls)} URLs.")
    submit_to_indexnow(urls)
