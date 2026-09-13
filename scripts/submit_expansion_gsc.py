import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        # Step 1: Submit updated sitemap
        log("\n[1/2] Submitting updated sitemap.xml on Google Search Console...")
        page.goto("https://search.google.com/search-console/sitemaps?resource_id=https://swariyaweddings.com/", wait_until="networkidle")
        time.sleep(3)
        page.keyboard.press("Escape")

        inp = page.locator("input[placeholder*='Enter sitemap URL'], input[aria-label*='Enter sitemap URL']").first
        inp.click(force=True)
        inp.fill("sitemap.xml")
        time.sleep(1)

        submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT')").first
        submit_btn.click(force=True)
        log("Clicked SUBMIT for sitemap.xml! Waiting 8s...")
        time.sleep(8)
        page.keyboard.press("Escape")

        # Step 2: Inspect top new pages
        new_targets = [
            ("venue_finder", "https://swariyaweddings.com/venue-finder.html"),
            ("calculator", "https://swariyaweddings.com/wedding-budget-calculator.html"),
            ("telugu", "https://swariyaweddings.com/telugu-wedding-planner-bengaluru.html"),
            ("tamil", "https://swariyaweddings.com/tamil-wedding-planner-bengaluru.html"),
            ("comparison", "https://swariyaweddings.com/top-wedding-planners-in-bangalore-comparison.html"),
            ("gayatri_vihar", "https://swariyaweddings.com/venues/gayatri-vihar-palace-grounds.html")
        ]

        log(f"\n[2/2] Requesting Indexing for {len(new_targets)} flagship new URLs...")
        for name, u in new_targets:
            log(f"\n--- Submitting Indexing: {u} ---")
            page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="networkidle")
            time.sleep(2)
            page.keyboard.press("Escape")

            search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
            search_bar.click(force=True)
            search_bar.fill(u)
            page.keyboard.press("Enter")
            log("Waiting 14s for Google Index analysis...")
            time.sleep(14)
            page.keyboard.press("Escape")

            btn = page.get_by_text("Request indexing", exact=False)
            if btn.count() > 0:
                log("Clicking Request indexing...")
                btn.first.click(force=True)
                log("Google is running live URL test (waiting 22s)...")
                time.sleep(22)
                page.keyboard.press("Escape")
            else:
                log("Button not found or already indexed.")

            shot = f"gsc_expansion_{name}.png"
            page.screenshot(path=shot)
            log(f"📸 Saved: {shot}")

        log("🎉 All new expansion pages submitted to Google Search Console!")
        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    main()
