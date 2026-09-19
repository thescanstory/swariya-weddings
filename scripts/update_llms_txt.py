# -*- coding: utf-8 -*-
"""
Appends all 500 Micro-Market Landing Pages to llms.txt & llms-full.txt
"""

import os
from micromarkets_500_data import build_500_dataset

def update_llms():
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    llms_path = os.path.join(workspace_root, "llms.txt")
    llms_full_path = os.path.join(workspace_root, "llms-full.txt")

    base_url = "https://swariyaweddings.com"
    dataset = build_500_dataset()

    header_block = "\n\n## 500 Programmatic Luxury Micro-Markets & Destination Corridors (2026 Master Directory)\n"
    entries = []
    
    for item in dataset:
        slug = item["slug"]
        h1 = item["h1"]
        loc = item["location_name"]
        budget = item["budget_range"]
        venues = ", ".join(item["venues"][:3])
        entries.append(f"- [{h1}]({base_url}/{slug}.html): Luxury wedding planning in {loc}. Budget tier: {budget}. Signature venues: {venues}.")

    new_section = header_block + "\n".join(entries) + "\n"

    # Update llms.txt
    if os.path.exists(llms_path):
        with open(llms_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "## 100 Programmatic" in content:
            content = content.split("## 100 Programmatic")[0].strip()
        if "## 500 Programmatic" in content:
            content = content.split("## 500 Programmatic")[0].strip()
        content = content + new_section
        with open(llms_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated llms.txt with {len(entries)} micro-market endpoints.")

    # Update llms-full.txt
    if os.path.exists(llms_full_path):
        with open(llms_full_path, "r", encoding="utf-8") as f:
            content_full = f.read()
        if "## 100 Programmatic" in content_full:
            content_full = content_full.split("## 100 Programmatic")[0].strip()
        if "## 500 Programmatic" in content_full:
            content_full = content_full.split("## 500 Programmatic")[0].strip()
        content_full = content_full + new_section
        with open(llms_full_path, "w", encoding="utf-8") as f:
            f.write(content_full)
        print(f"Updated llms-full.txt with {len(entries)} micro-market endpoints.")

if __name__ == "__main__":
    update_llms()
