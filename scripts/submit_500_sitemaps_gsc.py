# -*- coding: utf-8 -*-
"""
Google Search Console Automation for Swariya Weddings
Submits the Master Sitemap Index and all 8 Thematic Child Sitemaps
"""

import os
import sys
import time
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    log("==================================================")
    log("🚀 Submitting Swariya 500-Page Sitemaps to GSC")
    log("==================================================")

    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    sitemaps_to_submit = [
        "sitemap.xml",
        "sitemap-main.xml",
        "sitemap-bengaluru.xml",
        "sitemap-rajasthan.xml",
        "sitemap-goa-kerala.xml",
        "sitemap-karnataka-destinations.xml",
        "sitemap-north-hills.xml",
        "sitemap-metros.xml",
        "sitemap-cultural.xml"
    ]

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1360, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        sitemaps_url = "https://search.google.com/search-console/sitemaps?resource_id=https://swariyaweddings.com/"
        log(f"\n[Step 1] Navigating to GSC Sitemaps: {sitemaps_url}")
        page.goto(sitemaps_url, wait_until="domcontentloaded", timeout=45000)
        time.sleep(5)

        # Dismiss banners
        try:
            got_its = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it')")
            for i in range(got_its.count()):
                if got_its.nth(i).is_visible():
                    got_its.nth(i).click()
                    time.sleep(1)
        except Exception:
            pass

        for sm in sitemaps_to_submit:
            log(f"\nSubmitting: {sm}...")
            try:
                sitemap_input = page.locator("input[aria-label*='sitemap' i], input[placeholder*='sitemap' i]").first
                if sitemap_input.is_visible():
                    sitemap_input.click()
                    sitemap_input.fill(sm)
                    time.sleep(1)
                    submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT'), div[role='button']:has-text('Submit'), button:has-text('Submit')").first
                    submit_btn.click()
                    log(f"✅ Submitted {sm} successfully!")
                    time.sleep(5)
                    page.keyboard.press("Escape")
                    time.sleep(1)
            except Exception as e:
                log(f"Notice submitting {sm}: {e}")

        # Capture final screenshot
        page.screenshot(path="final_500_sitemaps_submitted.png")
        log("\nCaptured screenshot: final_500_sitemaps_submitted.png")
        time.sleep(3)
        browser_context.close()
        log("GSC Sitemaps Submission Pipeline Finished!")

if __name__ == "__main__":
    main()
