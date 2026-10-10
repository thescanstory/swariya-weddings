#!/usr/bin/env python3
"""
scripts/unify_entity_schemas.py

Unifies all Schema.org structured data across all HTML pages on swariyaweddings.com:
1. Normalizes reviewCount to '50' (matching Google Knowledge Graph and Google Maps live profile).
2. Connects all LocalBusiness / Service providers to Google Knowledge Graph entity (/g/11x03vrzsw)
   and Google Maps share link (https://share.google/BbGtUofhfLQtxvCIp) via hasMap and sameAs.
3. Validates that all modified JSON-LD scripts parse cleanly as valid JSON before writing to disk.
"""

import os
import glob
import re
import json

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    # 1. Normalize reviewCount across all aggregateRatings
    new_content = re.sub(r"\"reviewCount\":\s*\"(150|500)\"", "\"reviewCount\": \"50\"", new_content)
    new_content = re.sub(r"\"reviewCount\":\s*(150|500)", "\"reviewCount\": \"50\"", new_content)

    # 2. Inject hasMap and sameAs into provider / LocalBusiness schemas if missing
    if "hasMap" not in new_content:
        map_block = (
            "\"hasMap\": \"https://share.google/BbGtUofhfLQtxvCIp\",\n"
            "        \"sameAs\": [\n"
            "            \"https://www.google.com/search?kgmid=/g/11x03vrzsw&q=Swariya+Weddings\",\n"
            "            \"https://share.google/BbGtUofhfLQtxvCIp\",\n"
            "            \"https://www.instagram.com/swariya_weddings/\"\n"
            "        ],"
        )
        if "\"telephone\": \"+91-8050573382\"," in new_content:
            new_content = new_content.replace(
                "\"telephone\": \"+91-8050573382\",",
                "\"telephone\": \"+91-8050573382\",\n        " + map_block,
                1
            )

    if new_content == content:
        return False, "No change"

    # 3. Validate JSON-LD
    scripts = re.findall(r"<script type=\"application/ld\+json\">(.*?)</script>", new_content, re.DOTALL)
    for i, s in enumerate(scripts):
        try:
            json.loads(s)
        except Exception as e:
            # If invalid JSON, abort modifying this file
            return False, f"JSON Error in script {i}: {e}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, "Updated successfully"

def main():
    html_files = sorted(glob.glob("*.html"))
    print(f"Total HTML files to process: {len(html_files)}")
    
    updated_count = 0
    errors = 0
    
    for idx, filepath in enumerate(html_files):
        success, msg = process_file(filepath)
        if success:
            updated_count += 1
        elif "JSON Error" in msg:
            errors += 1
            print(f"Error in {filepath}: {msg}")
            
        if (idx + 1) % 500 == 0:
            print(f"Processed {idx + 1}/{len(html_files)} files... ({updated_count} updated)")

    print("=" * 60)
    print(f"Finished processing {len(html_files)} files.")
    print(f"Total files updated: {updated_count}")
    print(f"Total errors: {errors}")
    print("=" * 60)

if __name__ == "__main__":
    main()
