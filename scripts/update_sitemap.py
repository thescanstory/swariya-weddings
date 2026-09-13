import os
import glob

def build_sitemap():
    base_url = "https://swariyaweddings.com"
    html_files = []
    
    for root, _, files in os.walk("."):
        if "node_modules" in root or ".git" in root or "temp" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f).replace("./", "")
                if path == "venues/template.html":
                    continue
                html_files.append(path)

    html_files.sort()
    
    today = "2026-09-13"
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for page in html_files:
        if page == "index.html":
            loc = f"{base_url}/"
            priority = "1.0"
            changefreq = "weekly"
        elif page in ["bengaluru-wedding-cost-guide-2026.html", "reviews.html", "ask.html", "venue-finder.html", "wedding-budget-calculator.html", "wedding-brief-builder.html"]:
            loc = f"{base_url}/{page}"
            priority = "0.95"
            changefreq = "weekly"
        elif "kannada" in page or "telugu" in page or "tamil" in page or "marwari" in page or "nri" in page or "top-wedding" in page:
            loc = f"{base_url}/{page}"
            priority = "0.9"
            changefreq = "weekly"
        elif page.startswith("venues/"):
            loc = f"{base_url}/{page}"
            priority = "0.85"
            changefreq = "weekly"
        elif page in ["about.html", "services.html", "venues.html", "gallery.html", "contact.html"]:
            loc = f"{base_url}/{page}"
            priority = "0.8"
            changefreq = "monthly"
        else:
            loc = f"{base_url}/{page}"
            priority = "0.7"
            changefreq = "monthly"
            
        xml_lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

    xml_lines.append('</urlset>')
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")
    print(f"Generated sitemap.xml with {len(html_files)} URLs!")

build_sitemap()
