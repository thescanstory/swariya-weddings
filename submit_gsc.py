import sys
import time
import os
import urllib.parse
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    log("==================================================")
    log("🚀 Antigravity Playwright GSC Automation")
    log("==================================================")

    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    os.makedirs(profile_dir, exist_ok=True)

    with sync_playwright() as p:
        log(f"Launching persistent Chromium browser at: {profile_dir}")
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1280, "height": 850},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        target_resource = "https://swariyaweddings.com/"
        sitemaps_url = f"https://search.google.com/search-console/sitemaps?resource_id={urllib.parse.quote(target_resource, safe='')}"
        
        log(f"\n[Step 1] Navigating to Sitemaps: {sitemaps_url}")
        page.goto(sitemaps_url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(5)

        # Log current page state
        log(f"Current URL: {page.url}")
        page.screenshot(path="current_page_state.png")

        # Step 2: Submit Sitemap
        log("\n[Step 2] Processing Sitemap Submission...")
        try:
            # Look for sitemap input field
            inputs = page.locator("input[type='text'], input[aria-label*='sitemap' i], input[placeholder*='sitemap' i]")
            log(f"Found {inputs.count()} potential input elements.")
            
            submitted = False
            for i in range(inputs.count()):
                inp = inputs.nth(i)
                if inp.is_visible():
                    log(f"Entering 'sitemap.xml' in input #{i}...")
                    inp.click()
                    inp.fill("sitemap.xml")
                    time.sleep(1)
                    
                    # Look for nearby submit button
                    submit_btn = page.locator("button:has-text('Submit'), div[role='button']:has-text('Submit'), button[type='submit']")
                    if submit_btn.count() > 0 and submit_btn.first.is_visible():
                        log("Clicking Submit button...")
                        submit_btn.first.click()
                        time.sleep(6)
                        submitted = True
                        log("✅ Sitemap submitted successfully!")
                        break

            # Handle Got it modal
            got_it = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), button:has-text('OK'), div[role='button']:has-text('Got it')")
            if got_it.count() > 0 and got_it.first.is_visible():
                got_it.first.click()
                log("Dismissed 'Got it' dialog.")
                time.sleep(2)

            page.screenshot(path="gsc_sitemap_result.png")
            log("📸 Saved sitemap screenshot to gsc_sitemap_result.png")
        except Exception as e:
            log(f"Sitemap step notice: {e}")

        # Step 3: Inspect & Request Indexing
        urls_to_inspect = [
            "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026.html",
            "https://swariyaweddings.com/reviews.html",
            "https://swariyaweddings.com/ask.html",
            "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
            "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html"
        ]

        log(f"\n[Step 3] Inspecting & Requesting Indexing for {len(urls_to_inspect)} priority URLs...")
        for idx, u in enumerate(urls_to_inspect, 1):
            log(f"\n--- ({idx}/{len(urls_to_inspect)}) Inspecting: {u} ---")
            encoded_id = urllib.parse.quote(u, safe='')
            encoded_res = urllib.parse.quote(target_resource, safe='')
            inspect_url = f"https://search.google.com/search-console/inspect?resource_id={encoded_res}&id={encoded_id}"
            
            try:
                page.goto(inspect_url, wait_until="domcontentloaded", timeout=60000)
                log("Waiting for Google Index data retrieval (10s)...")
                time.sleep(10)
                
                # Look for Request Indexing button
                req_btn = page.locator("button:has-text('Request indexing'), div[role='button']:has-text('Request indexing'), button:has-text('REQUEST INDEXING'), div[role='button']:has-text('REQUEST INDEXING')")
                
                if req_btn.count() > 0 and req_btn.first.is_visible():
                    log("Found 'Request Indexing' button! Clicking now...")
                    req_btn.first.click()
                    log("Testing live URL / submitting indexing request (waiting 20s)...")
                    time.sleep(20)
                    
                    # Dismiss confirmation popup if any
                    dismiss_btn = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), button:has-text('Dismiss'), div[role='button']:has-text('Got it')")
                    if dismiss_btn.count() > 0 and dismiss_btn.first.is_visible():
                        dismiss_btn.first.click()
                        log(f"✅ Indexing request confirmed for {u}")
                    else:
                        log(f"✅ Indexing requested for {u}")
                else:
                    log(f"ℹ️ Request Indexing button not active or already requested recently for {u}")

                shot_name = f"gsc_inspect_{idx}.png"
                page.screenshot(path=shot_name)
                log(f"📸 Screenshot saved: {shot_name}")
            except Exception as ex:
                log(f"Inspection error on {u}: {ex}")

        log("\n🎉 All GSC tasks completed!")
        time.sleep(3)
        browser_context.close()

if __name__ == "__main__":
    main()
