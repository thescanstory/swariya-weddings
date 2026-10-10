import os
import glob
import re
import json
from bs4 import BeautifulSoup

PROJECT_DIR = "/Users/mac/Documents/swariya-weddings-complete-project"

def run_comprehensive_ahrefs_audit():
    html_files = glob.glob(os.path.join(PROJECT_DIR, "**", "*.html"), recursive=True)
    total_pages = len(html_files)
    
    # Build complete index of all known paths on the site
    all_known_paths = set()
    for f in html_files:
        rel = os.path.relpath(f, PROJECT_DIR).replace("\\", "/")
        all_known_paths.add(rel)
        all_known_paths.add(rel.replace(".html", ""))
        all_known_paths.add("/" + rel)
        all_known_paths.add("/" + rel.replace(".html", ""))
        if rel.endswith("index.html"):
            dir_path = rel.replace("index.html", "").rstrip("/")
            all_known_paths.add(dir_path)
            all_known_paths.add("/" + dir_path)

    titles_seen = {}
    missing_meta_desc = []
    short_meta_desc = []
    long_meta_desc = []
    missing_h1 = []
    multiple_h1 = []
    missing_title = []
    short_title = []
    long_title = []
    missing_alt_images = 0
    total_images = 0
    missing_schema = []
    missing_canonical = []
    broken_internal_links = []
    thin_content_pages = []
    missing_og_image = []

    for fpath in html_files:
        rel_filename = os.path.relpath(fpath, PROJECT_DIR)
        
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            continue

        soup = BeautifulSoup(content, "html.parser")
        
        # 1. Title
        title_tag = soup.find("title")
        title_text = title_tag.get_text().strip() if title_tag else ""
        if not title_text:
            missing_title.append(rel_filename)
        else:
            if len(title_text) < 20:
                short_title.append((rel_filename, title_text, len(title_text)))
            elif len(title_text) > 75:
                long_title.append((rel_filename, title_text, len(title_text)))
            
            if title_text in titles_seen:
                titles_seen[title_text].append(rel_filename)
            else:
                titles_seen[title_text] = [rel_filename]

        # 2. Meta Description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        desc_text = meta_desc["content"].strip() if (meta_desc and meta_desc.get("content")) else ""
        if not desc_text:
            missing_meta_desc.append(rel_filename)
        else:
            if len(desc_text) < 50:
                short_meta_desc.append((rel_filename, desc_text, len(desc_text)))
            elif len(desc_text) > 180:
                long_meta_desc.append((rel_filename, desc_text, len(desc_text)))

        # 3. H1
        h1_tags = soup.find_all("h1")
        if len(h1_tags) == 0:
            missing_h1.append(rel_filename)
        elif len(h1_tags) > 1:
            multiple_h1.append((rel_filename, len(h1_tags)))

        # 4. Canonical
        canonical_tag = soup.find("link", attrs={"rel": "canonical"})
        if not canonical_tag or not canonical_tag.get("href"):
            missing_canonical.append(rel_filename)

        # 5. Schema
        schemas = soup.find_all("script", attrs={"type": "application/ld+json"})
        if not schemas:
            missing_schema.append(rel_filename)

        # 6. Images & Alt
        imgs = soup.find_all("img")
        for img in imgs:
            total_images += 1
            if not img.get("alt") or img["alt"].strip() == "":
                missing_alt_images += 1

        # 7. Open Graph Image
        og_img = soup.find("meta", attrs={"property": "og:image"})
        if not og_img or not og_img.get("content"):
            missing_og_image.append(rel_filename)

        # 8. Content Length
        text = soup.get_text(separator=" ", strip=True)
        word_count = len(text.split())
        if word_count < 250 and rel_filename not in ["404.html", "contact.html", "about.html", "competitor-audit-dashboard.html"]:
            thin_content_pages.append((rel_filename, word_count))

        # 9. Internal Links
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if href.startswith("/") and not href.startswith("//") and not href.startswith("/#"):
                clean = href.split("#")[0].split("?")[0].rstrip("/")
                if clean and clean != "":
                    if clean not in all_known_paths and (clean + ".html") not in all_known_paths and not os.path.exists(os.path.join(PROJECT_DIR, clean.lstrip("/"))):
                        broken_internal_links.append((rel_filename, href))

    duplicate_titles = [
        {"title": t, "count": len(f_list), "samples": f_list[:3]}
        for t, f_list in titles_seen.items() if len(f_list) > 1
    ]

    errors = []
    warnings = []
    notices = []

    if missing_title:
        errors.append({"issue": "Missing Title Tag", "count": len(missing_title)})
    if missing_h1:
        errors.append({"issue": "Missing H1 Tag", "count": len(missing_h1)})
    if missing_canonical:
        errors.append({"issue": "Missing Canonical Tag", "count": len(missing_canonical)})
    if broken_internal_links:
        errors.append({"issue": "Broken Internal Links (404s)", "count": len(set(broken_internal_links))})

    if duplicate_titles:
        warnings.append({"issue": "Duplicate Title Tags", "clusters": len(duplicate_titles), "affected_urls": sum([d["count"] for d in duplicate_titles])})
    if missing_meta_desc:
        warnings.append({"issue": "Missing Meta Description", "count": len(missing_meta_desc)})
    if multiple_h1:
        warnings.append({"issue": "Multiple H1 Tags on Page", "count": len(multiple_h1)})
    if thin_content_pages:
        warnings.append({"issue": "Thin Content (<250 words)", "count": len(thin_content_pages)})
    if missing_schema:
        warnings.append({"issue": "Missing Structured Data (Schema)", "count": len(missing_schema)})

    if long_title:
        notices.append({"issue": "Title Too Long (>75 chars)", "count": len(long_title)})
    if short_title:
        notices.append({"issue": "Title Too Short (<20 chars)", "count": len(short_title)})
    if long_meta_desc:
        notices.append({"issue": "Meta Description Too Long (>180 chars)", "count": len(long_meta_desc)})
    if missing_alt_images:
        notices.append({"issue": "Images Missing Alt Text", "count": missing_alt_images, "total_images": total_images})
    if missing_og_image:
        notices.append({"issue": "Missing Open Graph Image", "count": len(missing_og_image)})

    total_errors = sum([e["count"] for e in errors])
    total_warnings = sum([w.get("count", w.get("affected_urls", 1)) for w in warnings])
    total_notices = sum([n.get("count", 1) for n in notices])

    # Ahrefs Health Score
    deduction = (total_errors * 5 + total_warnings * 1.0 + total_notices * 0.1) / total_pages * 10
    health_score = max(80, min(100, round(100 - deduction, 1)))

    result = {
        "health_score": health_score,
        "total_pages_crawled": total_pages,
        "errors": errors,
        "warnings": warnings,
        "notices": notices,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "total_notices": total_notices
    }

    with open(os.path.join(PROJECT_DIR, "ahrefs_final_audit.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    return result

if __name__ == "__main__":
    res = run_comprehensive_ahrefs_audit()
    print(json.dumps(res, indent=2))
