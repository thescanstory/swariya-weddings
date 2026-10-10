import glob
import os

OUTPUT_DIR = "/Users/mac/Documents/swariya-weddings-complete-project"
sub_sitemaps = sorted([os.path.basename(f) for f in glob.glob(os.path.join(OUTPUT_DIR, "sitemap-*.xml"))])

root_sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")

sitemap_index_content = ['<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for s in sub_sitemaps:
    sitemap_index_content.append(f'''  <sitemap>
    <loc>https://swariyaweddings.com/{s}</loc>
    <lastmod>2026-09-28</lastmod>
  </sitemap>''')

sitemap_index_content.append('</sitemapindex>')

with open(root_sitemap_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_index_content))

print(f"Updated root sitemap.xml with all {len(sub_sitemaps)} sub-sitemaps!")
