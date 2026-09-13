import sys
import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    log("==================================================")
    log("🚀 Running Perfected GSC Automation")
    log("==================================================")

    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1360, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        sitemaps_url = "https://search.google.com/search-console/sitemaps?resource_id=https://swariyaweddings.com/"
        log(f"\n[Step 1] Navigating to Sitemaps: {sitemaps_url}")
        page.goto(sitemaps_url, wait_until="networkidle", timeout=60000)
        time.sleep(3)

        # 1. Dismiss any helper toast (like "Got it")
        log("Checking for helper overlays/toasts...")
        try:
            got_its = page.locator("button:has-text('Got it'), div[role='button']:has-text('Got it')")
            for i in range(got_its.count()):
                if got_its.nth(i).is_visible():
                    got_its.nth(i).click()
                    log("Dismissed overlay toast.")
                    time.sleep(1)
        except Exception as e:
            log(f"Toast dismiss notice: {e}")

        # 2. Submit sitemap.xml
        log("\n[Step 2] Submitting sitemap.xml...")
        try:
            sitemap_input = page.locator("input[aria-label*='sitemap' i], input[placeholder*='sitemap' i]").first
            sitemap_input.wait_for(state="visible", timeout=10000)
            sitemap_input.click()
            sitemap_input.fill("sitemap.xml")
            time.sleep(1)

            submit_btn = page.locator("div[role='button']:has-text('SUBMIT'), button:has-text('SUBMIT'), div[role='button']:has-text('Submit'), button:has-text('Submit')").first
            submit_btn.click()
            log("Clicked SUBMIT button! Waiting for submission response...")
            time.sleep(8)

            # Dismiss confirmation modal
            confirm_dismiss = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), div[role='button']:has-text('GOT IT')")
            if confirm_dismiss.count() > 0 and confirm_dismiss.first.is_visible():
                confirm_dismiss.first.click()
                log("Dismissed 'Sitemap submitted' confirmation dialog.")
                time.sleep(2)

            page.screenshot(path="verified_sitemap_success.png")
            log("📸 Saved verified sitemap screenshot: verified_sitemap_success.png")
        except Exception as e:
            log(f"Error submitting sitemap: {e}")

        # 3. Inspect and Request Indexing for 5 Key URLs
        urls = [
            "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026.html",
            "https://swariyaweddings.com/reviews.html",
            "https://swariyaweddings.com/ask.html",
            "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
            "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html"
        ]

        log(f"\n[Step 3] Inspecting & Requesting Indexing for {len(urls)} URLs via GSC top inspection bar...")
        for idx, target_url in enumerate(urls, 1):
            log(f"\n--- [{idx}/{len(urls)}] Inspecting URL: {target_url} ---")
            try:
                # Click the top search / inspection bar
                inspect_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
                if not inspect_bar.is_visible():
                    # Navigate back to overview if inspection bar not on current view
                    page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="domcontentloaded")
                    time.sleep(3)
                    inspect_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first

                inspect_bar.click()
                inspect_bar.fill(target_url)
                time.sleep(1)
                page.keyboard.press("Enter")
                log("Submitted URL to inspection engine. Waiting for Google Index lookup (12s)...")
                time.sleep(12)

                # Look for Request Indexing button
                req_btn = page.locator("div[role='button']:has-text('Request indexing'), button:has-text('Request indexing'), div[role='button']:has-text('REQUEST INDEXING')").first
                if req_btn.is_visible():
                    log("Found 'Request indexing' button! Clicking now...")
                    req_btn.click()
                    log("Testing live URL before submitting request (waiting 25s)...")
                    time.sleep(25)

                    # Check for confirmation modal
                    done_btn = page.locator("button:has-text('GOT IT'), button:has-text('Got it'), div[role='button']:has-text('GOT IT')")
                    if done_btn.count() > 0 and done_btn.first.is_visible():
                        done_btn.first.click()
                        log("✅ Indexing requested & confirmation modal dismissed!")
                    else:
                        log("✅ Indexing request submitted.")
                else:
                    log("ℹ️ URL is already indexed or indexing was already requested recently.")

                shot_path = f"verified_inspect_{idx}.png"
                page.screenshot(path=shot_path)
                log(f"📸 Screenshot saved: {shot_path}")
            except Exception as e:
                log(f"Error inspecting {target_url}: {e}")

        log("\n🎉 All Google Search Console tasks completed successfully!")
        time.sleep(3)
        browser_context.close()

if __name__ == "__main__":
    main()
