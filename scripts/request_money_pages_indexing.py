import time
import os
import sys
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def close_overlays(page):
    try:
        page.keyboard.press("Escape")
        page.evaluate("""() => {
            document.querySelectorAll('#google-feedback, iframe, .pTyUxe').forEach(e => e.remove());
        }""")
    except Exception:
        pass

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    
    # Priority money pages with low KD and highest conversion value
    target_urls = [
        "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html",
        "https://swariyaweddings.com/3-day-destination-wedding-cost-at-the-tamarind-tree-bangalore.html",
        "https://swariyaweddings.com/3-day-destination-wedding-cost-at-gayatri-vihar-palace-grounds-bangalore.html",
        "https://swariyaweddings.com/3-day-runsheet-and-rituals-for-grand-telugu-royal-wedding.html",
        "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026.html",
        "https://swariyaweddings.com/wedding-brief-builder.html"
    ]
    
    log(f"Launching Playwright to inspect & request indexation for {len(target_urls)} high-intent URLs...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        for idx, u in enumerate(target_urls, 1):
            log(f"\n[{idx}/{len(target_urls)}] Inspecting URL: {u}")
            gsc_home = f"https://search.google.com/search-console?resource_id={resource_id}"
            page.goto(gsc_home, wait_until="networkidle")
            time.sleep(2)
            close_overlays(page)

            search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
            if not search_bar.is_visible():
                log("Search bar not found directly, clicking inspect icon...")
                page.keyboard.press("/")
                time.sleep(1)
                search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
            
            search_bar.click(force=True)
            search_bar.fill(u)
            time.sleep(0.5)
            page.keyboard.press("Enter")
            log("Waiting 12s for inspection results...")
            time.sleep(12)
            close_overlays(page)

            # Check status
            page_text = page.locator("body").inner_text()
            if "URL is on Google" in page_text:
                log("-> Status: Already on Google / Indexed.")
            else:
                log("-> Status: Not yet on Google or crawling queue.")

            # Look for Request Indexing button
            req_btn = page.locator("text='REQUEST INDEXING', div[role='button']:has-text('REQUEST INDEXING'), span:has-text('REQUEST INDEXING')").first
            if req_btn.is_visible():
                log("-> Clicking 'REQUEST INDEXING'...")
                req_btn.click(force=True)
                log("Waiting 20s for live URL test...")
                time.sleep(20)
                close_overlays(page)

                ok_btn = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it'), button:has-text('GOT IT')")
                if ok_btn.count() > 0 and ok_btn.first.is_visible():
                    ok_btn.first.click(force=True)
                    log("-> Indexing request submitted successfully!")
                else:
                    log("-> Confirmation button not detected or already closed.")
            else:
                log("-> 'REQUEST INDEXING' button not currently active (quota or already submitted).")
            
            time.sleep(3)

        log("\nPriority URL inspection routine completed.")

if __name__ == "__main__":
    main()
