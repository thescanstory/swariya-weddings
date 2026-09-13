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

        urls = [
            ("reviews", "https://swariyaweddings.com/reviews.html"),
            ("ask", "https://swariyaweddings.com/ask.html"),
            ("kannada", "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html"),
            ("venue_tamarind", "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html")
        ]

        for name, u in urls:
            log(f"\n==========================================")
            log(f"Submitting Indexing for: {u}")
            page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="networkidle")
            time.sleep(2)
            
            # Dismiss any popup/overlay
            page.keyboard.press("Escape")

            # Fill search bar
            search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
            search_bar.click(force=True)
            search_bar.fill(u)
            page.keyboard.press("Enter")
            
            log("Waiting 14s for Google Index analysis...")
            time.sleep(14)
            page.keyboard.press("Escape")

            # Click Request Indexing
            btn = page.get_by_text("Request indexing", exact=False)
            if btn.count() > 0:
                log(f"Found 'Request indexing' ({btn.count()} matching elements). Clicking...")
                btn.first.click(force=True)
                log("Google is testing live URL and submitting quota request (waiting 22s)...")
                time.sleep(22)
                
                # Dismiss modal if any
                dismiss = page.get_by_text("Got it", exact=False)
                if dismiss.count() > 0:
                    dismiss.first.click(force=True)
                    log("Dismissed 'Indexing requested' modal.")
            else:
                log("Button not found or already indexed.")

            shot = f"submitted_inspect_{name}.png"
            page.screenshot(path=shot)
            log(f"📸 Saved screenshot: {shot}")

        log("🎉 All 4 remaining URLs submitted for indexing!")
        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    main()
