import os
import re
import json

ROOT = "/Users/mac/Documents/swariya-weddings-complete-project"
VENUES_DIR = os.path.join(ROOT, "venues")

# 1. Enhance venue pages with BreadcrumbList Schema
venue_files = [f for f in os.listdir(VENUES_DIR) if f.endswith(".html") and f != "template.html"]

for vfile in venue_files:
    vpath = os.path.join(VENUES_DIR, vfile)
    with open(vpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Get venue title / name
    title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
    title = title_match.group(1).split("|")[0].strip() if title_match else vfile.replace(".html", "").replace("-", " ").title()

    venue_url = f"https://swariyaweddings.com/venues/{vfile}"

    # Check if BreadcrumbList is in Schema
    if "BreadcrumbList" not in content:
        breadcrumb_schema = f"""
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://swariyaweddings.com/"
            }},
            {{
                "@type": "ListItem",
                "position": 2,
                "name": "Venues",
                "item": "https://swariyaweddings.com/venues.html"
            }},
            {{
                "@type": "ListItem",
                "position": 3,
                "name": "{title}",
                "item": "{venue_url}"
            }}
        ]
    }}
    </script>"""
        content = content.replace("</head>", f"{breadcrumb_schema}\n</head>")
        with open(vpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added BreadcrumbList to {vfile}")

# 2. Update sitemap.xml to include client-portal.html if missing
sitemap_path = os.path.join(ROOT, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

if "client-portal.html" not in sitemap_content:
    entry = """  <url>
    <loc>https://swariyaweddings.com/client-portal.html</loc>
    <lastmod>2026-09-13</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""
    sitemap_content = sitemap_content.replace("</urlset>", entry)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Added client-portal.html to sitemap.xml")

print("Enhancement complete!")
