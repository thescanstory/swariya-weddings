import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    
    log("Launching Playwright with persistent GSC profile...")
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        # Step 1: Submit clean 100-page sitemap.xml
        log("\n--- Submitting clean 100-page sitemap.xml on Google Search Console ---")
        page.goto(f"https://search.google.com/search-console/sitemaps?resource_id={resource_id}", wait_until="networkidle")
        time.sleep(4)
        page.keyboard.press("Escape")

        inp = page.locator("input[placeholder*='Enter sitemap URL'], input[aria-label*='Enter sitemap URL']").first
        if inp.is_visible():
            inp.click(force=True)
            inp.fill("sitemap.xml")
            time.sleep(1)

            submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT')").first
            submit_btn.click(force=True)
            log("Clicked SUBMIT for sitemap.xml! Waiting 10s for Google confirmation...")
            time.sleep(10)
            page.keyboard.press("Escape")
        else:
            log("Sitemap input not found on page.")

        # Capture sitemaps state screenshot
        shot = "gsc_100_sitemap_submitted.png"
        page.screenshot(path=shot, full_page=True)
        log(f"📸 Saved: {shot}")

        # Extract rows from table
        try:
            rows = page.locator("table, [role='table'], [role='row']").all_inner_texts()
            log("Recent Sitemaps in GSC:")
            for r in rows[:6]:
                log(f"  • {r.strip()}")
        except Exception as e:
            log(f"Error reading sitemap table: {e}")

        # Step 2: Inspect flagship Bangalore hub
        log("\n--- Checking Flagship Hub URL Inspection ---")
        test_url = "https://swariyaweddings.com/wedding-planners-in-bangalore"
        page.goto(f"https://search.google.com/search-console?resource_id={resource_id}", wait_until="networkidle")
        time.sleep(3)
        search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
        if search_bar.is_visible():
            search_bar.click(force=True)
            search_bar.fill(test_url)
            page.keyboard.press("Enter")
            log("Waiting 12s for inspection...")
            time.sleep(12)
            page.screenshot(path="gsc_100_bangalore_hub_inspect.png", full_page=True)
            log("📸 Saved: gsc_100_bangalore_hub_inspect.png")

        browser.close()
        log("\n🎉 Google Search Console Sitemap Submission & Hub Inspection Complete!")

if __name__ == "__main__":
    main()
