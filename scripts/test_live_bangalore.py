import time
import os
from playwright.sync_api import sync_playwright

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    target_url = "https://swariyaweddings.com/wedding-planners-in-bangalore"
    
    print("=" * 65)
    print(f"🔍 TESTING LIVE GOOGLEBOT RENDER FOR: {target_url}")
    print("=" * 65)
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        inspect_url = f"https://search.google.com/search-console?resource_id={resource_id}"
        page.goto(inspect_url, wait_until="domcontentloaded")
        time.sleep(3)
        page.keyboard.press("Escape")
        
        search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
        search_bar.click(force=True)
        search_bar.fill(target_url)
        page.keyboard.press("Enter")
        time.sleep(10)
        page.keyboard.press("Escape")
        
        # Click "TEST LIVE URL"
        test_live_btn = page.locator("div[role='button']:has-text('TEST LIVE URL'), button:has-text('TEST LIVE URL')").first
        if test_live_btn.is_visible():
            print("Found TEST LIVE URL button! Clicking...")
            test_live_btn.click(force=True)
            print("Google is performing real-time live test (waiting 30s)...")
            time.sleep(30)
            page.keyboard.press("Escape")
            
        page.screenshot(path="gsc_live_test_bangalore_result.png", full_page=False)
        print("📸 Captured gsc_live_test_bangalore_result.png")
        
        # Now click REQUEST INDEXING
        req_btn = page.get_by_text("REQUEST INDEXING", exact=False).first
        if req_btn.is_visible():
            print("Found REQUEST INDEXING! Clicking...")
            req_btn.click(force=True)
            print("Waiting for Google index submission popup (20s)...")
            time.sleep(20)
            page.keyboard.press("Escape")
            
            got_it = page.locator("button:has-text('GOT IT'), div[role='button']:has-text('GOT IT')").first
            if got_it.is_visible():
                got_it.click(force=True)
                print("Dismissed confirmation popup.")
                
        page.screenshot(path="gsc_indexing_requested_confirmation.png", full_page=False)
        print("📸 Captured gsc_indexing_requested_confirmation.png")
        
        browser.close()
        print("✅ Live test & indexing request complete!")

if __name__ == "__main__":
    main()
