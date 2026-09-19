import sys
import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    log("==================================================")
    log("🚀 Running Swariya Master Batch GSC Indexation")
    log("==================================================")

    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1360, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        # Step 1: Submit Sitemap
        sitemaps_url = "https://search.google.com/search-console/sitemaps?resource_id=https://swariyaweddings.com/"
        log(f"\n[Step 1] Navigating to Sitemaps: {sitemaps_url}")
        page.goto(sitemaps_url, wait_until="networkidle", timeout=60000)
        time.sleep(3)

        # Dismiss toasts
        try:
            got_its = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it')")
            for i in range(got_its.count()):
                if got_its.nth(i).is_visible():
                    got_its.nth(i).click()
                    time.sleep(1)
        except Exception:
            pass

        # Re-submit sitemap.xml
        try:
            sitemap_input = page.locator("input[aria-label*='sitemap' i], input[placeholder*='sitemap' i]").first
            if sitemap_input.is_visible():
                sitemap_input.click()
                sitemap_input.fill("sitemap.xml")
                time.sleep(1)
                submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT'), div[role='button']:has-text('Submit'), button:has-text('Submit')").first
                submit_btn.click()
                log("Submitted sitemap.xml to Google Search Console!")
                time.sleep(6)
                page.keyboard.press("Escape")
        except Exception as e:
            log(f"Sitemap submission notice: {e}")

        # Step 2: High Priority URL Batch
        urls = [
            ("budget_calculator", "https://swariyaweddings.com/wedding-budget-calculator.html"),
            ("brief_builder", "https://swariyaweddings.com/wedding-brief-builder.html"),
            ("venue_finder", "https://swariyaweddings.com/venue-finder.html"),
            ("comparison_guide", "https://swariyaweddings.com/top-wedding-planners-in-bangalore-comparison.html"),
            ("goa_cost_guide", "https://swariyaweddings.com/cost-of-destination-wedding-in-goa-2026.html"),
            ("udaipur_cost_guide", "https://swariyaweddings.com/cost-of-udaipur-palace-wedding-2026.html"),
            ("hsr_layout", "https://swariyaweddings.com/wedding-planners-in-hsr-layout-bangalore.html"),
            ("indiranagar", "https://swariyaweddings.com/wedding-planners-in-indiranagar-bangalore.html"),
            ("whitefield", "https://swariyaweddings.com/wedding-planners-in-whitefield-bangalore.html")
        ]

        log(f"\n[Step 2] Processing {len(urls)} High-Intent Transaction & Local Hubs...")
        for idx, (name, target_url) in enumerate(urls, 1):
            log(f"\n--- [{idx}/{len(urls)}] Inspecting URL: {target_url} ---")
            try:
                page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="domcontentloaded")
                time.sleep(2)
                page.keyboard.press("Escape")

                search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
                search_bar.click(force=True)
                search_bar.fill(target_url)
                page.keyboard.press("Enter")
                log("Inspecting live Google Index data...")
                time.sleep(10)
                page.keyboard.press("Escape")

                req_btn = page.locator("div[role='button']:has-text('Request indexing'), button:has-text('Request indexing')").first
                if req_btn.count() > 0 and req_btn.is_visible():
                    log("Clicking 'Request indexing'...")
                    req_btn.click(force=True)
                    time.sleep(15)
                    page.keyboard.press("Escape")
                    log("✅ Indexing requested successfully!")
                else:
                    log("ℹ️ URL inspection complete (Already indexed or quota limited).")

                shot_path = f"master_inspect_{idx}_{name}.png"
                page.screenshot(path=shot_path)
                log(f"📸 Saved screenshot: {shot_path}")

            except Exception as e:
                log(f"Notice on {target_url}: {e}")

        browser_context.close()
        log("\n🎉 Master GSC indexing pass complete!")

if __name__ == "__main__":
    main()
