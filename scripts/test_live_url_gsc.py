import time
import os
from playwright.sync_api import sync_playwright

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    test_url = "https://swariyaweddings.com/cost-guide-for-kannada-traditional-royal-wedding-2026"
    
    print(f"Testing live URL in Google Search Console: {test_url}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        # Go to inspect URL
        inspect_url = f"https://search.google.com/search-console?resource_id={resource_id}"
        page.goto(inspect_url, wait_until="domcontentloaded")
        time.sleep(4)
        
        # Search for the URL
        search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
        if search_bar.is_visible():
            search_bar.click(force=True)
            search_bar.fill(test_url)
            page.keyboard.press("Enter")
            print("Submitted URL for inspection. Waiting for GSC results...")
            time.sleep(10)
            
            # Click TEST LIVE URL
            test_live_btn = page.locator("button:has-text('TEST LIVE URL'), div[role='button']:has-text('TEST LIVE URL'), span:has-text('TEST LIVE URL')").first
            if test_live_btn.is_visible():
                print("Clicking 'TEST LIVE URL' in Google Search Console...")
                test_live_btn.click(force=True)
                print("Google is performing live fetch and rendering test (takes ~25-35s)...")
                time.sleep(30)
                
            page.screenshot(path="gsc_test_live_url_result.png", full_page=True)
            print("Saved screenshot: gsc_test_live_url_result.png")
            
            # Extract live test verdict
            body_text = page.locator("body").inner_text()
            lines = [l.strip() for l in body_text.split("\n") if l.strip()]
            print("\n=== GOOGLE SEARCH CONSOLE LIVE VERDICT ===")
            for l in lines:
                if any(k in l.lower() for k in ["url is available", "url is not available", "page can be indexed", "crawled successfully", "user-declared canonical", "google-selected canonical", "breadcrumbs", "faq", "https", "valid"]):
                    print("  •", l)
                    
        browser.close()

if __name__ == "__main__":
    main()
