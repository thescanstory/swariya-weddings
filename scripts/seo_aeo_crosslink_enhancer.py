import os
import re

ROOT = "/Users/mac/Documents/swariya-weddings-complete-project"
GUIDES_DIR = os.path.join(ROOT, "blog", "guides")

# 1. Enhance Pillar Pages with SpeakableSpecification
pillar_files = [
    "index.html",
    "bengaluru-wedding-cost-guide-2026.html",
    "ask.html",
    "client-portal.html",
    "venue-finder.html",
    "wedding-budget-calculator.html",
    "kannada-wedding-planner-bengaluru.html",
    "telugu-wedding-planner-bengaluru.html",
    "tamil-wedding-planner-bengaluru.html",
    "marwari-wedding-planner-bengaluru.html",
    "nri-destination-wedding-planner-bangalore.html"
]

speakable_schema_template = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", ".section-label", ".hero p", "main p", ".methodology-text"]
      }
    }
    </script>"""

for pf in pillar_files:
    p_path = os.path.join(ROOT, pf)
    if os.path.exists(p_path):
        with open(p_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "SpeakableSpecification" not in content:
            content = content.replace("</head>", f"{speakable_schema_template}\n</head>")
            with open(p_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added Speakable schema to {pf}")

# 2. Add Contextual Resource Box to Blog Guides if not present
crosslink_box = """
        <div class="guide-crosslink-box" style="margin: 40px 0; background: #FFF8F0; border-left: 4px solid #D4AF37; padding: 22px 26px; border-radius: 0 8px 8px 0; font-family: 'Poppins', sans-serif;">
            <h4 style="color: #8B1A1A; margin-bottom: 8px; font-family: 'Playfair Display', serif; font-size: 1.2rem;">Planning a Wedding in Bengaluru? Explore Swariya's Tools</h4>
            <p style="font-size: 0.9rem; color: #555; line-height: 1.6; margin-bottom: 14px;">Estimate your costs with 100% financial transparency and zero vendor markups:</p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                <a href="/wedding-budget-calculator.html" style="background: #8B1A1A; color: #fff; padding: 6px 14px; border-radius: 4px; font-size: 0.82rem; text-decoration: none; font-weight: 600;">📊 Budget Calculator</a>
                <a href="/venues.html" style="background: #8B1A1A; color: #fff; padding: 6px 14px; border-radius: 4px; font-size: 0.82rem; text-decoration: none; font-weight: 600;">🏰 25+ Bangalore Venues</a>
                <a href="/client-portal.html" style="background: #8B1A1A; color: #fff; padding: 6px 14px; border-radius: 4px; font-size: 0.82rem; text-decoration: none; font-weight: 600;">💻 Wedding OS Workspace</a>
                <a href="/bengaluru-wedding-cost-guide-2026.html" style="background: #8B1A1A; color: #fff; padding: 6px 14px; border-radius: 4px; font-size: 0.82rem; text-decoration: none; font-weight: 600;">📖 2026 Cost Report</a>
            </div>
        </div>
"""

guide_files = [f for f in os.listdir(GUIDES_DIR) if f.endswith(".html") and f != "index.html"]
modified_guides = 0

for gfile in guide_files:
    gpath = os.path.join(GUIDES_DIR, gfile)
    with open(gpath, "r", encoding="utf-8") as f:
        gcontent = f.read()

    if "guide-crosslink-box" not in gcontent and "</article>" in gcontent:
        gcontent = gcontent.replace("</article>", f"{crosslink_box}\n</article>")
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gcontent)
        modified_guides += 1
    elif "guide-crosslink-box" not in gcontent and "</main>" in gcontent:
        gcontent = gcontent.replace("</main>", f"{crosslink_box}\n</main>")
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gcontent)
        modified_guides += 1

print(f"Cross-linked {modified_guides} blog guides to venue and interactive tool hubs!")
