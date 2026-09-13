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
    
    urls = [
        "https://swariyaweddings.com/destination-wedding-planner-india.html",
        "https://swariyaweddings.com/wedding-brief-builder.html"
    ]

    log(f"Submitting final 2 URLs to GSC...")

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        for idx, u in enumerate(urls, 1):
            log(f"\n--- [{idx}/{len(urls)}] Inspecting URL: {u} ---")
            try:
                page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="domcontentloaded", timeout=60000)
                time.sleep(3)
                close_overlays(page)

                search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
                search_bar.click(force=True)
                search_bar.fill(u)
                time.sleep(0.5)
                page.keyboard.press("Enter")
                log("Waiting for Google Search Console inspection results...")
                time.sleep(12)
                close_overlays(page)

                req_btn = page.locator("text='REQUEST INDEXING', div[role='button']:has-text('REQUEST INDEXING'), span:has-text('REQUEST INDEXING')").first
                if req_btn.is_visible():
                    log("Clicking REQUEST INDEXING...")
                    req_btn.click(force=True)
                    log("Waiting 20s for Google live test...")
                    time.sleep(20)
                    close_overlays(page)

                    ok_btn = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it'), button:has-text('GOT IT')")
                    if ok_btn.count() > 0 and ok_btn.first.is_visible():
                        ok_btn.first.click(force=True)
                    log(f"✅ Successfully requested indexing for: {u}")
                else:
                    log(f"ℹ️ Request indexing button status recorded for: {u}")

                screenshot_name = f"gsc_retry_{idx}.png"
                page.screenshot(path=screenshot_name)
                log(f"Screenshot saved to {screenshot_name}")

            except Exception as e:
                log(f"⚠️ Error during GSC inspection for {u}: {e}")

        browser.close()
        log("\n🎉 GSC Retry process completed.")

if __name__ == "__main__":
    main()
