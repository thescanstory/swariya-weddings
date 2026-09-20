import sys
import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    log("==================================================")
    log("👑 Swariya Weddings - Google Search Console Master Automation")
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

        # Step 1: Submit Sitemap
        sitemaps_url = "https://search.google.com/search-console/sitemaps?resource_id=https://swariyaweddings.com/"
        log(f"\n[1/2] Submitting sitemap.xml on {sitemaps_url}...")
        page.goto(sitemaps_url, wait_until="networkidle", timeout=60000)
        time.sleep(3)

        try:
            # Dismiss toast if any
            toasts = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it')")
            if toasts.count() > 0:
                toasts.first.click(force=True)
                time.sleep(1)

            # Fill sitemap input
            sitemap_inp = page.locator("input[placeholder*='Enter sitemap URL'], input[aria-label*='Enter sitemap URL']").first
            sitemap_inp.click(force=True)
            sitemap_inp.fill("sitemap.xml")
            time.sleep(1)

            # Click SUBMIT button
            submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT')").first
            submit_btn.click(force=True)
            log("✅ Clicked SUBMIT for sitemap.xml! Waiting 8s for confirmation...")
            time.sleep(8)

            # Dismiss modal
            confirm_modals = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), div[role='button']:has-text('GOT IT')")
            if confirm_modals.count() > 0 and confirm_modals.first.is_visible():
                confirm_modals.first.click(force=True)
                log("Dismissed sitemap confirmation dialog.")
                time.sleep(2)

            page.screenshot(path="master_sitemap_submitted.png")
            log("📸 Saved sitemap screenshot: master_sitemap_submitted.png")
        except Exception as e:
            log(f"Sitemap error: {e}")

        # Step 2: URL Inspection & Indexing
        urls_to_index = [
            "https://swariyaweddings.com/",
            "https://swariyaweddings.com/wedding-budget-calculator",
            "https://swariyaweddings.com/wedding-planner-in-sadashivanagar-bangalore",
            "https://swariyaweddings.com/royal-destination-wedding-planner-in-udaipur-lake-pichola-rajasthan",
            "https://swariyaweddings.com/destination-wedding-planner-in-candolim-beachfront-goa",
            "https://swariyaweddings.com/specialist-planner-for-nri-luxury-destination-wedding",
            "https://swariyaweddings.com/wedding-cost-at-taj-lake-palace-udaipur-udaipur"
        ]

        log(f"\n[2/2] Inspecting & Requesting Indexing for {len(urls_to_index)} priority pages...")
        for idx, target_url in enumerate(urls_to_index, 1):
            log(f"\n--- [{idx}/{len(urls_to_index)}] Inspecting: {target_url} ---")
            try:
                # Click the top search / inspection bar
                search_input = page.locator("input[aria-label*='Inspect any URL'], input[placeholder*='Inspect any URL']").first
                search_input.click(force=True)
                search_input.fill(target_url)
                time.sleep(1)
                page.keyboard.press("Enter")
                log("Submitted to Google Inspection engine. Waiting for index retrieval (15s)...")
                time.sleep(15)

                # Look for 'Request indexing'
                req_btn = page.locator("div[role='button']:has-text('Request indexing'), button:has-text('Request indexing'), div[role='button']:has-text('REQUEST INDEXING')")
                if req_btn.count() > 0 and req_btn.first.is_visible():
                    log("Found 'Request indexing' button! Submitting live test request...")
                    req_btn.first.click(force=True)
                    log("Testing live URL with Googlebot (waiting 25s)...")
                    time.sleep(25)

                    # Handle 'GOT IT' modal
                    got_it = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), div[role='button']:has-text('GOT IT')")
                    if got_it.count() > 0 and got_it.first.is_visible():
                        got_it.first.click(force=True)
                        log(f"✅ Indexing confirmed & dialog closed for {target_url}")
                    else:
                        log(f"✅ Indexing requested for {target_url}")
                else:
                    log(f"ℹ️ URL is already inspected / indexed or queued.")

                shot_path = f"master_inspect_{idx}.png"
                page.screenshot(path=shot_path)
                log(f"📸 Saved screenshot: {shot_path}")
            except Exception as ex:
                log(f"Inspection error on {target_url}: {ex}")

        log("\n🎉 ALL GOOGLE SEARCH CONSOLE TASKS COMPLETED!")
        time.sleep(3)
        browser_context.close()

if __name__ == "__main__":
    main()
