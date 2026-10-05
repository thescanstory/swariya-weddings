#!/usr/bin/env python3
"""
IndexNow Bulk Fast-Track Submitter
Submits all key URLs directly to the IndexNow protocol (Bing, Yahoo, DuckDuckGo, AI Search engines).
"""

import urllib.request
import json
import ssl
import glob
import xml.etree.ElementTree as ET

INDEXNOW_KEY = "c9842a1b7e904328b93f619b02a7b8e1"
HOST = "swariyaweddings.com"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_all_sitemap_urls():
    all_urls = []
    for sm in glob.glob("sitemap-*.xml"):
        try:
            tree = ET.parse(sm)
            root = tree.getroot()
            for loc in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                if loc.text:
                    all_urls.append(loc.text)
        except Exception as e:
            print(f"Error reading {sm}: {e}")
    return list(set(all_urls))

def submit_indexnow(urls):
    print(f"\nSubmitting {len(urls)} URLs to IndexNow Protocol (Bing / Yandex / DuckDuckGo / ChatGPT Search)...")
    
    # IndexNow accepts batches of up to 10,000 URLs
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls[:1000]  # First priority batch of 1,000
    }
    
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow"
    ]
    
    for ep in endpoints:
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                ep,
                data=data,
                headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
                print(f"  ✅ [SUCCESS {resp.status}] Dispatched to {ep}")
        except urllib.error.HTTPError as e:
            print(f"  ℹ️ [{ep}] Response: {e.code} ({e.read().decode('utf-8', errors='ignore')[:100]})")
        except Exception as e:
            print(f"  ❌ [{ep}] Error: {e}")

if __name__ == "__main__":
    urls = get_all_sitemap_urls()
    print(f"Total Unique URLs loaded from Sitemaps: {len(urls)}")
    submit_indexnow(urls)
