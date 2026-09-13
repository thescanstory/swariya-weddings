import time
import os
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
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        urls = [
            "https://swariyaweddings.com/reviews.html",
            "https://swariyaweddings.com/ask.html",
            "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
            "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html"
        ]

        for idx, u in enumerate(urls, 2):
            log(f"\n--- Requesting Indexing for URL #{idx}: {u} ---")
            page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="networkidle")
            time.sleep(2)
            close_overlays(page)

            search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
            search_bar.click(force=True)
            search_bar.fill(u)
            time.sleep(0.5)
            page.keyboard.press("Enter")
            log("Waiting 12s for inspection results...")
            time.sleep(12)
            close_overlays(page)

            req_btn = page.locator("text='REQUEST INDEXING', div[role='button']:has-text('REQUEST INDEXING'), span:has-text('REQUEST INDEXING')").first
            if req_btn.is_visible():
                log("Clicking REQUEST INDEXING...")
                req_btn.click(force=True)
                log("Waiting 20s for Google live test...")
                time.sleep(20)
                close_overlays(page)

                # Dismiss confirmation
                ok_btn = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it'), button:has-text('GOT IT')")
                if ok_btn.count() > 0 and ok_btn.first.is_visible():
                    ok_btn.first.click(force=True)
                    log("Dismissed confirmation modal.")
            else:
                log("Already requested or button not visible.")

            shot = f"clean_inspect_{idx}.png"
            page.screenshot(path=shot)
            log(f"📸 Saved: {shot}")

        log("Completed requesting indexing for all pages!")
        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    main()
