import os
import re
import json

def fix_everything():
    print("=== SWARIYA PRODUCTION AUDIT FIXER ===")
    
    # 1. Fix blog/case-studies/index.html
    cs_index_path = "blog/case-studies/index.html"
    if os.path.exists(cs_index_path):
        with open(cs_index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        schema_to_add = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Real Wedding Case Studies & Production Breakdowns",
  "url": "https://swariyaweddings.com/blog/case-studies/",
  "description": "Detailed production breakdowns of real weddings planned by Swariya across Bengaluru, Goa, and Udaipur.",
  "publisher": {
    "@type": "Organization",
    "name": "Swariya Weddings",
    "url": "https://swariyaweddings.com/"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://swariyaweddings.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Journal",
        "item": "https://swariyaweddings.com/blog.html"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Case Studies",
        "item": "https://swariyaweddings.com/blog/case-studies/"
      }
    ]
  }
}
</script>
"""
        if "application/ld+json" not in content:
            content = content.replace("</head>", f"{schema_to_add}\n</head>")
            with open(cs_index_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Added structured schema to {cs_index_path}")

    # 2. Fix venues/index.html relative links and asset paths
    venues_index_path = "venues/index.html"
    if os.path.exists(venues_index_path):
        with open(venues_index_path, "r", encoding="utf-8") as f:
            v_content = f.read()
        
        # Replace relative href="venues/...html" with href="/venues/...html" or direct filename
        v_content = v_content.replace('href="venues/', 'href="/venues/')
        v_content = v_content.replace('href="style.css', 'href="/style.css')
        v_content = v_content.replace('href="index.html"', 'href="/index.html"')
        v_content = v_content.replace('href="about.html"', 'href="/about.html"')
        v_content = v_content.replace('href="services.html"', 'href="/services.html"')
        v_content = v_content.replace('href="venues.html"', 'href="/venues.html"')
        v_content = v_content.replace('href="gallery.html"', 'href="/gallery.html"')
        v_content = v_content.replace('href="reviews.html"', 'href="/reviews.html"')
        v_content = v_content.replace('href="ask.html"', 'href="/ask.html"')
        v_content = v_content.replace('href="blog.html"', 'href="/blog.html"')
        v_content = v_content.replace('href="contact.html"', 'href="/contact.html"')
        v_content = v_content.replace('href="bengaluru-wedding-cost-guide-2026.html"', 'href="/bengaluru-wedding-cost-guide-2026.html"')
        v_content = v_content.replace('href="kannada-wedding-planner-bengaluru.html"', 'href="/kannada-wedding-planner-bengaluru.html"')
        
        with open(venues_index_path, "w", encoding="utf-8") as f:
            f.write(v_content)
        print(f"✅ Fixed asset & internal link paths in {venues_index_path}")

    # 3. Fix gmb_audit_report_swariya.html metadata
    gmb_report_path = "gmb_audit_report_swariya.html"
    if os.path.exists(gmb_report_path):
        with open(gmb_report_path, "r", encoding="utf-8") as f:
            g_content = f.read()
            
        if '<meta name="description"' not in g_content:
            meta_block = """    <meta name="description" content="Google My Business (GMB) and Local SEO Audit Report for Swariya Weddings Bangalore. Component breakdown, review velocity, NAP consistency, and local pack ranking analysis.">
    <link rel="canonical" href="https://swariyaweddings.com/gmb_audit_report_swariya.html">
    <meta property="og:title" content="GMB Audit Report · Swariya Weddings · Bangalore">
    <meta property="og:description" content="Official Google My Business & Local SEO Audit for Swariya Weddings Bangalore.">
    <meta property="og:image" content="https://swariyaweddings.com/images/16.jpg">
    <meta property="og:type" content="article">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Report",
      "name": "Google My Business Audit Report - Swariya Weddings",
      "about": {
        "@type": "LocalBusiness",
        "name": "Swariya Weddings",
        "telephone": "+91-8050573382",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "#343, 9th Main, 22nd Cross Rd, HSR Layout",
          "addressLocality": "Bengaluru",
          "postalCode": "560102",
          "addressCountry": "IN"
        }
      }
    }
    </script>"""
            g_content = g_content.replace("<head>", f"<head>\n{meta_block}")
            with open(gmb_report_path, "w", encoding="utf-8") as f:
                f.write(g_content)
            print(f"✅ Added SEO meta and Schema to {gmb_report_path}")

    # 4. Check all HTML pages for missing meta descriptions, canonicals, OG images
    html_files = []
    for root, _, files in os.walk("."):
        if any(x in root for x in ["node_modules", ".git", ".vercel", ".netlify"]):
            continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file).replace("./", "").replace("\\", "/")
                html_files.append(path)
                
    for path in html_files:
        if path in ["venues/template.html", "404.html"]:
            continue
            
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            
        modified = False
        
        # Check canonical
        if "canonical" not in c:
            clean_name = path if path != "index.html" else ""
            canon_tag = f'<link rel="canonical" href="https://swariyaweddings.com/{clean_name}">'
            c = c.replace("</head>", f"    {canon_tag}\n</head>")
            modified = True
            
        # Check meta description
        if 'name="description"' not in c and "name='description'" not in c:
            title_m = re.search(r'<title>(.*?)</title>', c, re.IGNORECASE)
            title_text = title_m.group(1).strip() if title_m else "Swariya Weddings"
            desc_tag = f'<meta name="description" content="{title_text} - Bespoke luxury and destination wedding planning across India by Swariya Weddings.">'
            c = c.replace("</head>", f"    {desc_tag}\n</head>")
            modified = True
            
        # Check OG image
        if 'property="og:image"' not in c and "property='og:image'" not in c:
            og_tag = '<meta property="og:image" content="https://swariyaweddings.com/images/16.jpg">'
            c = c.replace("</head>", f"    {og_tag}\n</head>")
            modified = True
            
        if modified:
            with open(path, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"✅ Patched meta tags in {path}")

    # 5. Rebuild sitemap.xml to be 100% complete
    print("\n--- Rebuilding sitemap.xml ---")
    import scripts.update_sitemap as sm
    sm.build_sitemap()

if __name__ == "__main__":
    fix_everything()
