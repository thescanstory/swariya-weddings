import os
import re

def audit_links():
    html_files = set()
    for root, _, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.normpath(os.path.join(root, file)).replace("\\", "/")
                if rel_path.startswith("./"):
                    rel_path = rel_path[2:]
                html_files.add(rel_path)
                
    print(f"Total internal HTML files registered: {len(html_files)}")
    
    broken_links = 0
    total_checked = 0
    
    for page in html_files:
        with open(page, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        # extract href links
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        page_dir = os.path.dirname(page)
        
        for href in hrefs:
            if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#") or href.startswith("javascript:"):
                continue
            
            # strip anchors and query params
            clean_href = href.split("#")[0].split("?")[0]
            if not clean_href:
                continue
                
            if clean_href.startswith("/"):
                target = clean_href.lstrip("/")
            else:
                target = os.path.normpath(os.path.join(page_dir, clean_href)).replace("\\", "/")
                
            total_checked += 1
            if target not in html_files and not os.path.exists(target):
                print(f"⚠️ Potential broken link in {page}: {href} -> {target}")
                broken_links += 1
                
    print(f"✅ Link Audit Complete: {total_checked} links checked. Broken links: {broken_links}.")
    return broken_links == 0

if __name__ == "__main__":
    audit_links()
