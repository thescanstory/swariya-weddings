import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    
    log("=" * 65)
    log("🚀 GSC CORE SITEMAP SUBMISSION & VERIFICATION")
    log("=" * 65)

    sitemaps_to_submit = [
        "sitemap-main.xml",
        "sitemap-bengaluru.xml",
        "sitemap-cost-guides-2026.xml"
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        # 1. Navigate to Sitemaps tab
        sitemaps_url = f"https://search.google.com/search-console/sitemaps?resource_id={resource_id}"
        log(f"Navigating to {sitemaps_url}...")
        page.goto(sitemaps_url, wait_until="domcontentloaded")
        time.sleep(4)
        page.keyboard.press("Escape")
        
        for sm in sitemaps_to_submit:
            log(f"\nSubmitting: {sm} ...")
            try:
                inp = page.locator("input[placeholder*='Enter sitemap URL'], input[aria-label*='Enter sitemap URL']").first
                if inp.is_visible():
                    inp.click(force=True)
                    inp.fill(sm)
                    time.sleep(1)
                    
                    submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT')").first
                    if submit_btn.is_visible():
                        submit_btn.click(force=True)
                        log(f"Clicked SUBMIT for {sm}. Waiting for confirmation...")
                        time.sleep(7)
                        page.keyboard.press("Escape")
                        
                        # Dismiss any dialog/snackbar
                        got_it_btn = page.locator("div[role='button']:has-text('GOT IT'), button:has-text('GOT IT')").first
                        if got_it_btn.is_visible():
                            got_it_btn.click(force=True)
                            time.sleep(1)
            except Exception as e:
                log(f"Error submitting {sm}: {e}")

        # Capture final sitemaps overview
        time.sleep(3)
        page.screenshot(path="gsc_sitemaps_updated.png", full_page=False)
        log("📸 Captured gsc_sitemaps_updated.png")
        
        # Extract rows from sitemap table
        try:
            table_text = page.locator("table, [role='table']").all_inner_texts()
            log("\n--- Current Sitemaps Status in GSC ---")
            for t in table_text[:5]:
                log(t.strip())
        except Exception as e:
            log(f"Could not read table: {e}")

        # 2. Inspect & Request Indexing for Flagship Bangalore URL
        target_url = "https://swariyaweddings.com/wedding-planners-in-bangalore"
        log(f"\n--- Requesting Live Crawl & Indexing for: {target_url} ---")
        inspect_url = f"https://search.google.com/search-console?resource_id={resource_id}"
        page.goto(inspect_url, wait_until="domcontentloaded")
        time.sleep(3)
        page.keyboard.press("Escape")

        search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
        if search_bar.is_visible():
            search_bar.click(force=True)
            search_bar.fill(target_url)
            page.keyboard.press("Enter")
            log("Waiting 10s for Google inspection result...")
            time.sleep(10)
            page.keyboard.press("Escape")

            # Click Request Indexing if present
            btn = page.locator("button:has-text('Request indexing'), div[role='button']:has-text('Request indexing')").first
            if btn.is_visible():
                log("Clicking 'Request indexing'...")
                btn.click(force=True)
                log("Google is running live URL testing (waiting 20s)...")
                time.sleep(20)
                page.keyboard.press("Escape")
                
                got_it = page.locator("button:has-text('GOT IT'), div[role='button']:has-text('GOT IT')").first
                if got_it.is_visible():
                    got_it.click(force=True)

            page.screenshot(path="gsc_inspect_bangalore_live.png", full_page=False)
            log("📸 Captured gsc_inspect_bangalore_live.png")

        browser.close()
        log("\n✅ Done!")

if __name__ == "__main__":
    main()
