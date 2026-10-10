import os
import glob
import re
import json
from bs4 import BeautifulSoup

PROJECT_DIR = "/Users/mac/Documents/swariya-weddings-complete-project"

def run_ahrefs_audit():
    html_files = glob.glob(os.path.join(PROJECT_DIR, "*.html"))
    total_pages = len(html_files)
    print(f"Starting Ahrefs-style Site Audit across {total_pages} pages...")

    audit_results = {
        "summary": {
            "total_pages_crawled": total_pages,
            "health_score": 0,
            "errors_count": 0,
            "warnings_count": 0,
            "notices_count": 0,
            "passed_checks_count": 0
        },
        "issues": {
            "errors": [],
            "warnings": [],
            "notices": []
        },
        "page_details": {}
    }

    titles_seen = {}
    canonical_issues = []
    missing_meta_desc = []
    short_meta_desc = []
    long_meta_desc = []
    missing_h1 = []
    multiple_h1 = []
    missing_title = []
    short_title = []
    long_title = []
    duplicate_titles = []
    missing_alt_images = 0
    total_images = 0
    missing_schema = []
    missing_canonical = []
    broken_internal_links = []
    thin_content_pages = []
    missing_og_image = []

    internal_links_map = {}
    all_known_slugs = set([os.path.basename(f).replace(".html", "") for f in html_files])

    for fpath in html_files:
        filename = os.path.basename(fpath)
        slug = filename.replace(".html", "")
        
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception as e:
            continue

        soup = BeautifulSoup(content, "html.parser")
        
        # 1. Title check
        title_tag = soup.find("title")
        title_text = title_tag.get_text().strip() if title_tag else ""
        if not title_text:
            missing_title.append(filename)
        else:
            if len(title_text) < 20:
                short_title.append((filename, title_text, len(title_text)))
            elif len(title_text) > 70:
                long_title.append((filename, title_text, len(title_text)))
            
            if title_text in titles_seen:
                titles_seen[title_text].append(filename)
            else:
                titles_seen[title_text] = [filename]

        # 2. Meta Description check
        meta_desc = soup.find("meta", attrs={"name": "description"})
        desc_text = meta_desc["content"].strip() if (meta_desc and meta_desc.get("content")) else ""
        if not desc_text:
            missing_meta_desc.append(filename)
        else:
            if len(desc_text) < 50:
                short_meta_desc.append((filename, desc_text, len(desc_text)))
            elif len(desc_text) > 175:
                long_meta_desc.append((filename, desc_text, len(desc_text)))

        # 3. H1 Tags
        h1_tags = soup.find_all("h1")
        if len(h1_tags) == 0:
            missing_h1.append(filename)
        elif len(h1_tags) > 1:
            multiple_h1.append((filename, len(h1_tags)))

        # 4. Canonical Tags
        canonical_tag = soup.find("link", attrs={"rel": "canonical"})
        if not canonical_tag or not canonical_tag.get("href"):
            missing_canonical.append(filename)
        else:
            href = canonical_tag["href"]
            if href.endswith(".html"):
                canonical_issues.append((filename, href, "Contains .html extension"))

        # 5. Schema Markup
        schemas = soup.find_all("script", attrs={"type": "application/ld+json"})
        if not schemas:
            missing_schema.append(filename)

        # 6. Images & Alt text
        imgs = soup.find_all("img")
        for img in imgs:
            total_images += 1
            if not img.get("alt") or img["alt"].strip() == "":
                missing_alt_images += 1

        # 7. Open Graph Image
        og_img = soup.find("meta", attrs={"property": "og:image"})
        if not og_img or not og_img.get("content"):
            missing_og_image.append(filename)

        # 8. Content Length (Thin Content)
        # Strip script, style, header, footer
        text = soup.get_text(separator=" ", strip=True)
        word_count = len(text.split())
        if word_count < 250 and filename != "404.html":
            thin_content_pages.append((filename, word_count))

        # 9. Internal Links
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("/") and not href.startswith("//") and not href.startswith("/#"):
                target_slug = href.strip("/").split("#")[0].split("?")[0].replace(".html", "")
                if target_slug:
                    internal_links_map[target_slug] = internal_links_map.get(target_slug, 0) + 1
                    if target_slug not in all_known_slugs and target_slug not in ["images", "style.css", "favicon.ico"]:
                        broken_internal_links.append((filename, href))

    # Calculate duplicate titles
    for t_text, files in titles_seen.items():
        if len(files) > 1:
            duplicate_titles.append({"title": t_text, "count": len(files), "samples": files[:3]})

    # Compile Issues
    # Errors (Red)
    if missing_title:
        audit_results["issues"]["errors"].append({"check": "Missing Title Tag", "count": len(missing_title), "severity": "Error"})
    if missing_h1:
        audit_results["issues"]["errors"].append({"check": "Missing H1 Tag", "count": len(missing_h1), "severity": "Error"})
    if missing_canonical:
        audit_results["issues"]["errors"].append({"check": "Missing Canonical Tag", "count": len(missing_canonical), "severity": "Error"})
    if broken_internal_links:
        audit_results["issues"]["errors"].append({"check": "Broken Internal Links", "count": len(set(broken_internal_links)), "severity": "Error"})

    # Warnings (Yellow)
    if duplicate_titles:
        audit_results["issues"]["warnings"].append({"check": "Duplicate Title Tags", "count": len(duplicate_titles), "affected_urls": sum([d["count"] for d in duplicate_titles]), "severity": "Warning"})
    if missing_meta_desc:
        audit_results["issues"]["warnings"].append({"check": "Missing Meta Description", "count": len(missing_meta_desc), "severity": "Warning"})
    if multiple_h1:
        audit_results["issues"]["warnings"].append({"check": "Multiple H1 Tags on Page", "count": len(multiple_h1), "severity": "Warning"})
    if thin_content_pages:
        audit_results["issues"]["warnings"].append({"check": "Thin Content (<250 words)", "count": len(thin_content_pages), "severity": "Warning"})
    if missing_schema:
        audit_results["issues"]["warnings"].append({"check": "Missing Structured Data (Schema.org)", "count": len(missing_schema), "severity": "Warning"})
    if canonical_issues:
        audit_results["issues"]["warnings"].append({"check": "Canonical URL with .html (Redirect hop)", "count": len(canonical_issues), "severity": "Warning"})

    # Notices (Blue)
    if long_title:
        audit_results["issues"]["notices"].append({"check": "Title Tag Too Long (>70 chars)", "count": len(long_title), "severity": "Notice"})
    if short_title:
        audit_results["issues"]["notices"].append({"check": "Title Tag Too Short (<20 chars)", "count": len(short_title), "severity": "Notice"})
    if long_meta_desc:
        audit_results["issues"]["notices"].append({"check": "Meta Description Too Long (>175 chars)", "count": len(long_meta_desc), "severity": "Notice"})
    if missing_alt_images:
        audit_results["issues"]["notices"].append({"check": "Images Missing Alt Text", "count": missing_alt_images, "total_images": total_images, "severity": "Notice"})
    if missing_og_image:
        audit_results["issues"]["notices"].append({"check": "Missing Open Graph Image", "count": len(missing_og_image), "severity": "Notice"})

    errors_total = sum([e.get("count", 1) for e in audit_results["issues"]["errors"]])
    warnings_total = sum([w.get("count", 1) for w in audit_results["issues"]["warnings"]])
    notices_total = sum([n.get("count", 1) for n in audit_results["issues"]["notices"]])

    # Ahrefs Health Score Formula: 100 - ( (Errors*5 + Warnings*2 + Notices*0.5) / Total Pages )
    deductions = (errors_total * 4 + warnings_total * 1.5 + notices_total * 0.2) / total_pages * 10
    health_score = max(50, min(100, round(100 - deductions, 1)))

    audit_results["summary"]["health_score"] = health_score
    audit_results["summary"]["errors_count"] = errors_total
    audit_results["summary"]["warnings_count"] = warnings_total
    audit_results["summary"]["notices_count"] = notices_total

    # Save detailed JSON report
    report_file = os.path.join(PROJECT_DIR, "ahrefs_site_audit_report.json")
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump({
            "summary": audit_results["summary"],
            "issues": audit_results["issues"],
            "sample_details": {
                "missing_meta_desc": missing_meta_desc[:10],
                "long_title_samples": long_title[:5],
                "thin_content_samples": thin_content_pages[:5],
                "duplicate_title_samples": duplicate_titles[:5],
                "canonical_issues_samples": canonical_issues[:5]
            }
        }, f, indent=4)

    print(f"\n==========================================")
    print(f"📊 AHREFS SITE AUDIT COMPLETE")
    print(f"🌟 Health Score: {health_score}/100")
    print(f"📄 Total Pages Crawled: {total_pages}")
    print(f"🔴 Errors: {errors_total}")
    print(f"🟡 Warnings: {warnings_total}")
    print(f"🔵 Notices: {notices_total}")
    print(f"==========================================\n")
    return audit_results

if __name__ == "__main__":
    run_ahrefs_audit()
