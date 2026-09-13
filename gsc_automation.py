import sys
import time
import os
from playwright.sync_api import sync_playwright

def main():
    print("==================================================")
    print("🚀 Google Search Console Automation with Playwright")
    print("==================================================")
    
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    os.makedirs(profile_dir, exist_ok=True)
    
    with sync_playwright() as p:
        print(f"Launching Chromium with persistent context at: {profile_dir}")
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1280, "height": 850},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()

        target_resource = "https://swariyaweddings.com/"
        sitemaps_url = f"https://search.google.com/search-console/sitemaps?resource_id={target_resource}"
        
        print(f"\n[1/3] Navigating to Sitemaps: {sitemaps_url}")
        page.goto(sitemaps_url, wait_until="domcontentloaded", timeout=60000)

        # Handle Google Account Authentication
        print("Checking authentication status...")
        time.sleep(3)
        
        # Keep waiting while on accounts.google.com or login page
        while "accounts.google.com" in page.url or "signin" in page.url:
            print("🔑 Awaiting Google sign-in in the Chromium window... (Checking every 3s)")
            time.sleep(3)
            if "search.google.com/search-console" in page.url and "accounts.google.com" not in page.url:
                print("✅ Logged in successfully!")
                break

        print("Logged in to Google Search Console. Ensuring we are on Sitemaps page...")
        if "sitemaps" not in page.url:
            page.goto(sitemaps_url, wait_until="networkidle", timeout=60000)
            time.sleep(3)

        # Step 2: Submit Sitemap
        print("\n[2/3] Submitting Sitemap (sitemap.xml)...")
        try:
            # Wait for sitemap input or table
            page.wait_for_timeout(3000)
            # Find input box for sitemap URL
            input_box = page.locator("input[name='sitemapPath'], input[aria-label*='sitemap' i], input[type='text']").first
            if input_box.is_visible():
                print("Found sitemap input box. Entering 'sitemap.xml'...")
                input_box.click()
                input_box.fill("sitemap.xml")
                time.sleep(1)
                
                submit_btn = page.locator("button:has-text('Submit'), div[role='button']:has-text('Submit')").first
                if submit_btn.is_visible():
                    submit_btn.click()
                    print("✅ Clicked Submit button for sitemap.xml!")
                    time.sleep(6)
                    # Dismiss modal if present
                    modal_dismiss = page.locator("button:has-text('Got it'), button:has-text('OK'), div[role='button']:has-text('Got it')")
                    if modal_dismiss.count() > 0 and modal_dismiss.first.is_visible():
                        modal_dismiss.first.click()
                        print("Dismissed submission confirmation dialog.")
            else:
                print("Sitemap input not directly visible; check screenshot.")
            
            page.screenshot(path="sitemap_status.png")
            print("📸 Saved sitemap status screenshot to sitemap_status.png")
        except Exception as e:
            print(f"Error submitting sitemap: {e}")

        # Step 3: Inspect & Request Indexing
        urls_to_inspect = [
            "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026.html",
            "https://swariyaweddings.com/reviews.html",
            "https://swariyaweddings.com/ask.html",
            "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
            "https://swariyaweddings.com/venues/the-tamarind-tree-bangalore.html"
        ]

        print(f"\n[3/3] Inspecting and Requesting Indexing for {len(urls_to_inspect)} priority pages...")
        for idx, u in enumerate(urls_to_inspect, 1):
            print(f"\n--- [{idx}/{len(urls_to_inspect)}] Inspecting: {u} ---")
            inspect_url = f"https://search.google.com/search-console/inspect?resource_id={target_resource}&id={u}"
            try:
                page.goto(inspect_url, wait_until="domcontentloaded", timeout=60000)
                print("Retrieving data from Google index (waiting 8s)...")
                time.sleep(8)
                
                # Check for "Request Indexing"
                req_btn = page.locator("text='Request Indexing', div[role='button']:has-text('Request Indexing'), button:has-text('Request Indexing')")
                if req_btn.count() > 0 and req_btn.first.is_visible():
                    print("Found 'Request Indexing' button. Clicking...")
                    req_btn.first.click()
                    print("Waiting for live test and quota response (15s)...")
                    time.sleep(15)
                    # Dismiss confirmation
                    dismiss_btn = page.locator("button:has-text('Got it'), button:has-text('Dismiss'), div[role='button']:has-text('Got it')")
                    if dismiss_btn.count() > 0 and dismiss_btn.first.is_visible():
                        dismiss_btn.first.click()
                        print("✅ Indexing request confirmed.")
                    else:
                        print("✅ Indexing requested.")
                else:
                    print("Request Indexing button not clickable or already submitted.")
                
                shot_path = f"inspect_url_{idx}.png"
                page.screenshot(path=shot_path)
                print(f"📸 Screenshot saved: {shot_path}")
            except Exception as ex:
                print(f"Error inspecting {u}: {ex}")

        print("\n🎉 Google Search Console automation completed successfully!")
        time.sleep(4)
        browser_context.close()

if __name__ == "__main__":
    main()


