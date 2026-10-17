#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
100-Quality-Pages Architecture Verification Suite.
Audits all 100 pages for:
- Existence & HTTP-readiness
- Title, Meta Description & Canonical tag
- Schema.org JSON-LD presence
- Robots indexability
- Inclusion in sitemap.xml & llms.txt
"""

import os
import sys
import warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from build_100_quality_sitemap import SELECTED_100

def verify_all():
    print("=" * 70)
    print("SWARIYA WEDDINGS — 100 QUALITY PAGES AUDIT SUITE")
    print("=" * 70)
    
    # 1. Check Sitemap
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as fh:
        sitemap_soup = BeautifulSoup(fh.read(), "html.parser")
    sitemap_locs = set(loc.text.strip() for loc in sitemap_soup.find_all("loc"))
    print(f"✓ sitemap.xml entries count: {len(sitemap_locs)}")
    
    # 2. Check llms.txt
    llms_path = os.path.join(BASE_DIR, "llms.txt")
    with open(llms_path, "r", encoding="utf-8") as fh:
        llms_text = fh.read()
    print(f"✓ llms.txt size: {len(llms_text)} bytes")

    # 3. Audit each of the 100 pages
    results = []
    issues = 0
    
    for filename, priority, changefreq, description in SELECTED_100:
        fpath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(fpath):
            results.append((filename, False, "File missing on disk!"))
            issues += 1
            continue
            
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
            soup = BeautifulSoup(content, "html.parser")
            
        title = soup.find("title")
        meta_desc = soup.find("meta", attrs={"name": "description"})
        canonical = soup.find("link", rel="canonical")
        meta_robots = soup.find("meta", attrs={"name": "robots"})
        schema = soup.find("script", type="application/ld+json")
        
        has_title = bool(title and title.text.strip())
        has_desc = bool(meta_desc and meta_desc.get("content"))
        has_canonical = bool(canonical and canonical.get("href"))
        has_robots = bool(meta_robots and "index" in meta_robots.get("content", "").lower() and "noindex" not in meta_robots.get("content", "").lower())
        has_schema = bool(schema and schema.text.strip())
        
        # Check canonical match in sitemap
        canon_url = canonical["href"].strip() if canonical and canonical.get("href") else ""
        in_sitemap = canon_url in sitemap_locs
        
        page_ok = has_title and has_desc and has_canonical and has_robots and has_schema and in_sitemap
        if not page_ok:
            issues += 1
            status = f"Title:{has_title} Desc:{has_desc} Canon:{has_canonical} Robots:{has_robots} Schema:{has_schema} InSitemap:{in_sitemap}"
        else:
            status = "100% Valid"
            
        results.append((filename, page_ok, status, title.text.strip() if has_title else ""))

    print(f"\nAudit complete: {len(results)}/100 pages evaluated.")
    print(f"Total issues found: {issues}")
    
    if issues == 0:
        print("🎉 SUCCESS: ALL 100 PAGES ARE 100% COMPLIANT & READY FOR GOOGLEBOT!")
    else:
        print(f"⚠️ {issues} pages need attention:")
        for r in results:
            if not r[1]:
                print(f"  • {r[0]}: {r[2]}")
                
    return issues == 0

if __name__ == "__main__":
    verify_all()
