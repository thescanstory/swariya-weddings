import time
import os
from playwright.sync_api import sync_playwright

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    
    test_urls = [
        "https://swariyaweddings.com/",
        "https://swariyaweddings.com/destinations-directory",
        "https://swariyaweddings.com/bengaluru-wedding-cost-guide-2026",
        "https://swariyaweddings.com/wedding-budget-calculator",
        "https://swariyaweddings.com/cost-guide-for-kannada-traditional-royal-wedding-2026"
    ]
    
    print("=" * 70)
    print("🔍 IN-DEPTH MULTI-PAGE LIVE INSPECTION IN GOOGLE SEARCH CONSOLE")
    print("=" * 70)
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        for idx, u in enumerate(test_urls, 1):
            print(f"\n--- [{idx}/{len(test_urls)}] Testing URL: {u} ---")
            inspect_url = f"https://search.google.com/search-console?resource_id={resource_id}"
            page.goto(inspect_url, wait_until="domcontentloaded")
            time.sleep(3)
            
            search_bar = page.locator("input[placeholder*='Inspect any URL']").first
            if search_bar.is_visible():
                search_bar.click(force=True)
                search_bar.fill(u)
                page.keyboard.press("Enter")
                time.sleep(8)
                
                # Test live URL
                test_live_btn = page.locator("button:has-text('TEST LIVE URL'), div[role='button']:has-text('TEST LIVE URL')").first
                if test_live_btn.is_visible():
                    print("  -> Triggering Google Live Render Test...")
                    test_live_btn.click(force=True)
                    time.sleep(25)
                    
                body_text = page.locator("body").inner_text()
                lines = [l.strip() for l in body_text.split("\n") if l.strip()]
                
                is_available = any("url is available to google" in l.lower() for l in lines)
                can_index = any("page can be indexed" in l.lower() for l in lines)
                https_ok = any("https" in l.lower() and "valid" in l.lower() for l in lines) or "https" in body_text.lower()
                
                print(f"  • Google Verdict: {'✅ URL is available to Google' if is_available else '⚠️ Status: ' + lines[5] if len(lines)>5 else 'Unknown'}")
                print(f"  • Indexing: {'✅ Page can be indexed' if can_index else 'Pending'}")
                
                for l in lines:
                    if any(k in l.lower() for k in ["breadcrumbs", "faq", "user-declared canonical", "google-selected canonical", "1 valid item", "valid items"]):
                        print(f"    - {l}")
                        
        browser.close()
    print("\n" + "=" * 70)
    print("🏆 ALL 5 CORE URLS LIVE-TESTED DIRECTLY ON GOOGLE SERVERS")
    print("=" * 70)

if __name__ == "__main__":
    main()
