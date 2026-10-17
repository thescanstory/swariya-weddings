#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enforce Index/Noindex Directives to Focus Google Crawl Budget.
- Selected 100 Quality Pages: index, follow, max-image-preview:large
- All other pages: noindex, follow
"""

import os
import re
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from build_100_quality_sitemap import SELECTED_100
SELECTED_SET = set(os.path.normpath(f[0]) for f in SELECTED_100)

ROBOTS_INDEX = '<meta name="robots" content="index, follow, max-image-preview:large">'
ROBOTS_NOINDEX = '<meta name="robots" content="noindex, follow">'

def run():
    modified_noindex = 0
    verified_index = 0
    skipped = 0

    for root, dirs, files in os.walk(BASE_DIR):
        # Skip node_modules, git, reports, etc.
        if any(skip in root for skip in [".git", "node_modules", ".vercel", ".netlify"]):
            continue
            
        for f in files:
            if not f.endswith(".html"):
                continue
                
            rel_path = os.path.normpath(os.path.relpath(os.path.join(root, f), BASE_DIR))
            
            # Don't touch reports or 404
            if rel_path.startswith("reports") or f == "404.html":
                continue
                
            full_path = os.path.join(BASE_DIR, rel_path)
            
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
            except Exception:
                continue

            is_quality_100 = rel_path in SELECTED_SET
            target_meta = ROBOTS_INDEX if is_quality_100 else ROBOTS_NOINDEX
            
            # Check if meta robots exists
            if re.search(r'<meta\s+name=["\x27]robots["\x27][^>]*>', content, re.IGNORECASE):
                # Replace existing meta robots tag
                new_content = re.sub(
                    r'<meta\s+name=["\x27]robots["\x27][^>]*>',
                    target_meta,
                    content,
                    flags=re.IGNORECASE
                )
            else:
                # Insert inside <head>
                new_content = re.sub(
                    r'(<head[^>]*>)',
                    r'\1\n    ' + target_meta,
                    content,
                    flags=re.IGNORECASE
                )

            if new_content != content:
                with open(full_path, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                if is_quality_100:
                    verified_index += 1
                else:
                    modified_noindex += 1
            else:
                if is_quality_100:
                    verified_index += 1
                else:
                    skipped += 1

    print(f"Done! Verified 100 Quality Pages: {verified_index}")
    print(f"Set noindex on {modified_noindex} programmatic pages (unchanged/already noindexed: {skipped}).")

if __name__ == "__main__":
    run()
