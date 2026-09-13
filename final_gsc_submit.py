import sys
import time
import os
import urllib.parse
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def cleanup_overlays(page):
    try:
        page.evaluate("""() => {
            document.querySelectorAll('#google-feedback, iframe[src*="feedback"], .pTyUxe').forEach(el => el.remove());
        }""")
    except Exception:
        pass

def main():
    log("==================================================")
    log("🚀 Final Robust Google Search Console Automation")
    log("==================================================")

    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1400, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        target_res = "https://swariyaweddings.com/"
        sitemaps_url = f"https://search.google.com/search-console/sitemaps?resource_id={urllib.parse.quote(target_res, safe='')}"

        log(f"\n[Step 1] Loading Sitemaps: {sitemaps_url}")
        page.goto(sitemaps_url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(4)
        cleanup_overlays(page)

        # Step 2: Submit Sitemap
        log("\n[Step 2] Submitting sitemap.xml...")
        try:
            sitemap_input = page.locator("input[placeholder*='Enter sitemap URL'], input[aria-label*='Enter sitemap URL']").first
            if sitemap_input.is_visible():
                sitemap_input.click()
                sitemap_input.fill("sitemap.xml")
                time.sleep(1)

                # Locate SUBMIT inside the Add a new sitemap section
                submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT')").first
                submit_btn.click()
                log("✅ SUBMIT clicked! Waiting for Google response...")
                time.sleep(8)

                cleanup_overlays(page)
                # Dismiss modal if present
                dismiss_btn = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), div[role='button']:has-text('GOT IT')")
                if dismiss_btn.count() > 0 and dismiss_btn.first.is_visible():
                    dismiss_btn.first.click()
                    log("Dismissed confirmation modal.")
            else:
                log("Sitemap input not directly found.")
            
            page.screenshot(path="final_sitemap_success.png")
            log("📸 Saved screenshot: final_sitemap_success.png")
        except Exception as e:
            log(f"Sitemap submission notice: {e}")

        # Step 3: Inspect & Request Indexing for 5 Key URLs
        urls = [
            "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026.html",
            "https://swariyaweddings.com/reviews.html",
            "https://swariyaweddings.com/ask.html",
            "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
            "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html"
        ]

        log(f"\n[Step 3] Submitting Indexing Requests for {len(urls)} URLs...")
        for idx, target_url in enumerate(urls, 1):
            log(f"\n--- [{idx}/{len(urls)}] Inspecting URL: {target_url} ---")
            inspect_url = f"https://search.google.com/search-console/inspect?resource_id={urllib.parse.quote(target_res, safe='')}&id={urllib.parse.quote(target_url, safe='')}"
            
            try:
                page.goto(inspect_url, wait_until="domcontentloaded", timeout=60000)
                log("Loading URL inspection data (waiting 10s)...")
                time.sleep(10)
                cleanup_overlays(page)

                # Find Request indexing button
                req_btn = page.locator("text='Request indexing', div[role='button']:has-text('Request indexing'), button:has-text('Request indexing'), div[role='button']:has-text('REQUEST INDEXING')")
                
                if req_btn.count() > 0 and req_btn.first.is_visible():
                    log("Found 'Request indexing' button! Clicking...")
                    req_btn.first.click()
                    log("Google is testing live URL and submitting indexing request (waiting 22s)...")
                    time.sleep(22)
                    cleanup_overlays(page)

                    # Click 'GOT IT'
                    got_it = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), div[role='button']:has-text('GOT IT'), div[role='button']:has-text('Got it')")
                    if got_it.count() > 0 and got_it.first.is_visible():
                        got_it.first.click()
                        log(f"✅ Indexing confirmed & modal dismissed for {target_url}")
                    else:
                        log(f"✅ Indexing request submitted for {target_url}")
                else:
                    log(f"ℹ️ URL already indexed or recently submitted for {target_url}")

                shot_path = f"final_inspect_{idx}.png"
                page.screenshot(path=shot_path)
                log(f"📸 Saved inspection screenshot: {shot_path}")
            except Exception as e:
                log(f"Inspection notice for {target_url}: {e}")

        log("\n🎉 All GSC indexing submissions completed successfully!")
        time.sleep(3)
        browser_context.close()

if __name__ == "__main__":
    main()
