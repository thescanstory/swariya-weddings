#!/usr/bin/env python3
"""
Swariya Weddings - 500 Referring Domains Live Execution Sprint
1. Updates Sitemaps with new authority hubs (/partners, /press).
2. Generates the Batch 1 Interactive Outreach Dossier for the first 125 High-DR targets.
3. Broadcasts IndexNow instant indexing requests.
4. Triggers Netlify live production deployment.
"""

import os
import json
import subprocess
import time
import urllib.request
import ssl
import xml.etree.ElementTree as ET

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(ROOT_DIR, "data", "500_referring_domains_database.json")

def step1_update_sitemap():
    print("\n[+] Step 1: Adding /partners and /press to sitemap-main.xml...")
    sitemap_main = os.path.join(ROOT_DIR, "sitemap-main.xml")
    if os.path.exists(sitemap_main):
        with open(sitemap_main, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_entries = ""
        if "https://swariyaweddings.com/partners" not in content:
            new_entries += """  <url>
    <loc>https://swariyaweddings.com/partners</loc>
    <lastmod>2026-10-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
"""
        if "https://swariyaweddings.com/press" not in content:
            new_entries += """  <url>
    <loc>https://swariyaweddings.com/press</loc>
    <lastmod>2026-10-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
        if new_entries:
            content = content.replace("</urlset>", new_entries + "</urlset>")
            with open(sitemap_main, "w", encoding="utf-8") as f:
                f.write(content)
            print("  -> Updated sitemap-main.xml with /partners and /press")
        else:
            print("  -> /partners and /press already present in sitemap-main.xml")
    else:
        print("  -> sitemap-main.xml not found, skipping update.")

def step2_generate_batch1_dossier():
    print("\n[+] Step 2: Generating Batch 1 Interactive Outreach Dossier (First 125 Targets)...")
    with open(DB_PATH, "r", encoding="utf-8") as f:
        domains = json.load(f)
    
    batch1 = domains[:125]
    os.makedirs(os.path.join(ROOT_DIR, "reports"), exist_ok=True)
    dossier_path = os.path.join(ROOT_DIR, "reports", "batch_1_outreach_dossier.html")

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Swariya Weddings - Batch 1 High-DR Outreach Dossier (125 Targets)</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #FAF6F0; color: #1C1917; margin: 0; padding: 30px; }
        .container { max-width: 1200px; margin: 0 auto; background: #FFF; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); }
        h1 { color: #8B1A1A; margin-top: 0; }
        .meta { display: flex; gap: 20px; background: #F5EFEB; padding: 15px; border-radius: 8px; margin-bottom: 25px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #E8DFD5; font-size: 0.9rem; }
        th { background: #8B1A1A; color: #FFF; }
        tr:hover { background: #FCF9F6; }
        .dr-badge { display: inline-block; padding: 3px 8px; border-radius: 12px; font-weight: bold; font-size: 0.8rem; background: #E7F5E8; color: #1E7E34; }
        .dr-ultra { background: #FFF3CD; color: #856404; }
        .action-btn { display: inline-block; padding: 6px 12px; background: #8B1A1A; color: #FFF; border-radius: 4px; text-decoration: none; font-size: 0.8rem; font-weight: 500; }
        .action-btn:hover { background: #C5A059; color: #1C1917; }
    </style>
</head>
<body>
<div class="container">
    <h1>Swariya Weddings — Batch 1 Priority Backlink Dossier</h1>
    <div class="meta">
        <div><strong>Total Targets:</strong> 125 Domains</div>
        <div><strong>Category:</strong> National Portals (50) + Local Citations (75)</div>
        <div><strong>Expected DR Impact:</strong> DR 2 &rarr; DR 24+</div>
        <div><strong>Status:</strong> Ready for Live Submission</div>
    </div>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Platform / Domain</th>
                <th>Category</th>
                <th>Est. DR</th>
                <th>Target Landing Page</th>
                <th>Action Hook</th>
            </tr>
        </thead>
        <tbody>
"""
    for item in batch1:
        dr_cls = "dr-ultra" if item["est_dr"] >= 75 else "dr-badge"
        html += f"""            <tr>
                <td>#{item["id"]}</td>
                <td><strong>{item["name"]}</strong><br><small style="color:#666;">{item["domain"]}</small></td>
                <td>{item["category"]}</td>
                <td><span class="{dr_cls}">DR {item["est_dr"]}</span></td>
                <td><a href="{item["landing_page_target"]}" target="_blank" style="color:#8B1A1A;font-size:0.8rem;">{item["landing_page_target"].split('/')[-1] or 'Homepage'}</a></td>
                <td><span style="font-size:0.85rem;color:#444;">{item["outreach_angle"]}</span></td>
            </tr>\n"""

    html += """        </tbody>
    </table>
</div>
</body>
</html>"""

    with open(dossier_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  -> Generated {dossier_path}")

def step3_broadcast_indexnow():
    print("\n[+] Step 3: Broadcasting Instant IndexNow Pings for /partners & /press...")
    setup_script = os.path.join(ROOT_DIR, "scripts", "setup_indexnow.py")
    if os.path.exists(setup_script):
        try:
            res = subprocess.run(["python3", setup_script], capture_output=True, text=True, timeout=30)
            print("  -> IndexNow output:")
            for line in res.stdout.strip().split("\n")[-6:]:
                print("     " + line)
        except Exception as e:
            print(f"  -> IndexNow broadcast error: {e}")
    else:
        print("  -> setup_indexnow.py not found.")

def step4_deploy_production():
    print("\n[+] Step 4: Deploying Live to Netlify Production...")
    deploy_script = os.path.join(ROOT_DIR, "scripts", "deploy_netlify.py")
    if os.path.exists(deploy_script):
        try:
            res = subprocess.run(["python3", deploy_script], capture_output=True, text=True, timeout=120)
            print("  -> Netlify Deploy Output:")
            for line in res.stdout.strip().split("\n")[-7:]:
                print("     " + line)
        except Exception as e:
            print(f"  -> Deploy script error: {e}")
    else:
        print("  -> deploy_netlify.py not found.")

if __name__ == "__main__":
    print("================================================================================")
    print("        SWARIYA WEDDINGS — EXECUTING 500 REFERRING DOMAINS SPRINT               ")
    print("================================================================================")
    step1_update_sitemap()
    step2_generate_batch1_dossier()
    step3_broadcast_indexnow()
    step4_deploy_production()
    print("\n[SUCCESS] SPRINT EXECUTION COMPLETE!")
    print("================================================================================")
