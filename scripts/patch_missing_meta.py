import os
import re

fixes = [
    {
        "file": "privacy-policy.html",
        "insert_before": "</head>",
        "content": """    <meta property="og:title" content="Privacy Policy & Terms | Swariya Weddings">
    <meta property="og:description" content="Swariya Weddings privacy policy, data protection, financial transparency guarantee, and client confidentiality terms.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://swariyaweddings.com/privacy-policy.html">
    <meta property="og:image" content="https://swariyaweddings.com/images/16.jpg">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Privacy Policy & Terms | Swariya Weddings",
      "url": "https://swariyaweddings.com/privacy-policy.html",
      "description": "Privacy policy, client confidentiality terms, and financial transparency guarantee for Swariya Weddings."
    }
    </script>
"""
    },
    {
        "file": "wedding-budget-calculator.html",
        "insert_before": "</head>",
        "content": """    <meta property="og:title" content="Pan-India Wedding Budget Calculator 2026 | Swariya Weddings">
    <meta property="og:description" content="Calculate and customize wedding costs across Bengaluru, Goa, Rajasthan, Kerala, and Pan-India with 0% vendor markup transparency.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://swariyaweddings.com/wedding-budget-calculator.html">
    <meta property="og:image" content="https://swariyaweddings.com/images/15.jpg">
"""
    },
    {
        "file": "venue-finder.html",
        "insert_before": "</head>",
        "content": """    <meta property="og:title" content="Bangalore Wedding Venue Finder & 3-Way Comparator | Swariya Weddings">
    <meta property="og:description" content="Compare Bengaluru wedding venues side-by-side on capacity, room counts, catering rules, and 2026 pricing.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://swariyaweddings.com/venue-finder.html">
    <meta property="og:image" content="https://swariyaweddings.com/images/13.jpg">
"""
    }
]

venue_files = [
    "venues/the-grape-garden-bangalore.html",
    "venues/the-leela-palace-bengaluru.html",
    "venues/amita-rasa-bangalore.html",
    "venues/the-tamarind-tree-bangalore.html",
    "venues/taj-west-end-bengaluru.html"
]

for item in fixes:
    fpath = item["file"]
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if "</head>" in c:
            c = c.replace("</head>", item["content"] + "</head>")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Patched {fpath}")

for vpath in venue_files:
    if os.path.exists(vpath):
        with open(vpath, "r", encoding="utf-8") as f:
            c = f.read()
        if "og:image" not in c and "</head>" in c:
            tag = '\n    <meta property="og:image" content="https://swariyaweddings.com/images/16.jpg">\n'
            c = c.replace("</head>", tag + "</head>")
            with open(vpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Patched {vpath}")
