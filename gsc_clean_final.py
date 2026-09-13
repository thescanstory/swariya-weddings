import sys
import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def close_all_drawers(page):
    try:
        page.keyboard.press("Escape")
        time.sleep(0.5)
        page.evaluate("""() => {
            document.querySelectorAll('#google-feedback, iframe[src*="feedback"], div[aria-label*="feedback" i]').forEach(e => e.remove());
        }""")
    except Exception:
        pass

def main():
    log("==================================================")
    log("✨ Final Clean GSC Execution & Verification")
    log("==================================================")

    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        # Step 1: Submit Sitemap
        sitemaps_url = "https://search.google.com/search-console/sitemaps?resource_id=https://swariyaweddings.com/"
        log(f"\n[1/2] Submitting sitemap.xml...")
        page.goto(sitemaps_url, wait_until="networkidle", timeout=60000)
        time.sleep(2)
        close_all_drawers(page)

        try:
            sitemap_inp = page.locator("input[placeholder*='Enter sitemap URL'], input[aria-label*='Enter sitemap URL']").first
            sitemap_inp.click(force=True)
            sitemap_inp.fill("sitemap.xml")
            time.sleep(1)

            submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT')").first
            submit_btn.click(force=True)
            log("✅ Clicked SUBMIT! Waiting 6s...")
            time.sleep(6)
            close_all_drawers(page)
            
            # Dismiss 'Sitemap submitted' dialog if visible
            dialog_got_it = page.locator("div[role='dialog'] button:has-text('Got it'), div[role='dialog'] div[role='button']:has-text('Got it')")
            if dialog_got_it.count() > 0 and dialog_got_it.first.is_visible():
                dialog_got_it.first.click(force=True)

            time.sleep(2)
            page.screenshot(path="clean_sitemap_submitted.png")
            log("📸 Saved: clean_sitemap_submitted.png")
        except Exception as e:
            log(f"Sitemap error: {e}")

        # Step 2: URL Inspection & Indexing
        urls = [
            "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026.html",
            "https://swariyaweddings.com/reviews.html",
            "https://swariyaweddings.com/ask.html",
            "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
            "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html"
        ]

        log(f"\n[2/2] Requesting Indexing for {len(urls)} URLs...")
        for idx, u in enumerate(urls, 1):
            log(f"\n--- [{idx}/{len(urls)}] Inspecting URL: {u} ---")
            try:
                close_all_drawers(page)
                search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
                search_bar.click(force=True)
                search_bar.fill(u)
                time.sleep(0.5)
                page.keyboard.press("Enter")
                log("Waiting for Google Index lookup (12s)...")
                time.sleep(12)
                close_all_drawers(page)

                # Look for Request indexing button
                req_btn = page.locator("div[role='button']:has-text('Request indexing'), button:has-text('Request indexing'), div[role='button']:has-text('REQUEST INDEXING')")
                if req_btn.count() > 0 and req_btn.first.is_visible():
                    log("Found Request indexing button! Submitting live test request...")
                    req_btn.first.click(force=True)
                    log("Testing live URL (waiting 20s)...")
                    time.sleep(20)

                    # Click 'Got it' on the 'Indexing requested' confirmation modal
                    modal_ok = page.locator("div[role='dialog'] button:has-text('Got it'), div[role='dialog'] div[role='button']:has-text('Got it')")
                    if modal_ok.count() > 0 and modal_ok.first.is_visible():
                        modal_ok.first.click(force=True)
                        log(f"✅ Indexing confirmed & dialog dismissed for {u}")
                    else:
                        log(f"✅ Indexing requested for {u}")
                else:
                    log(f"ℹ️ URL status retrieved / already queued for {u}")

                time.sleep(1)
                close_all_drawers(page)
                shot = f"clean_inspect_{idx}.png"
                page.screenshot(path=shot)
                log(f"📸 Saved: {shot}")
            except Exception as e:
                log(f"Inspect error on {u}: {e}")

        log("\n🎉 Clean automation complete!")
        time.sleep(2)
        browser_context.close()

if __name__ == "__main__":
    main()
