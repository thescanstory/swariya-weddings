import time
import os
from playwright.sync_api import sync_playwright

def log(msg):
    print(msg, flush=True)

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    resource_id = "https://swariyaweddings.com/"
    
    log(f"Launching Playwright to check Google Search Console for {resource_id}...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        # 1. Check Sitemaps Page
        log("\n--- Checking Sitemaps in Google Search Console ---")
        sitemaps_url = f"https://search.google.com/search-console/sitemaps?resource_id={resource_id}"
        page.goto(sitemaps_url, wait_until="networkidle")
        time.sleep(5)
        page.screenshot(path="gsc_sitemaps_status.png", full_page=True)
        log("Captured gsc_sitemaps_status.png")
        
        # Extract text from sitemaps table
        try:
            sitemap_rows = page.locator("table, [role='table'], [role='row']").all_inner_texts()
            log("Sitemaps Content:")
            for r in sitemap_rows[:10]:
                log(r.strip())
        except Exception as e:
            log(f"Error reading sitemaps table: {e}")
            
        # 2. Check Performance / Search Analytics
        log("\n--- Checking Performance Overview in Google Search Console ---")
        perf_url = f"https://search.google.com/search-console/performance/search-analytics?resource_id={resource_id}"
        page.goto(perf_url, wait_until="networkidle")
        time.sleep(5)
        page.screenshot(path="gsc_performance_status.png", full_page=True)
        log("Captured gsc_performance_status.png")
        
        try:
            body_text = page.locator("body").inner_text()
            lines = [l.strip() for l in body_text.split("\n") if l.strip()]
            for l in lines[:30]:
                if any(k in l.lower() for k in ["clicks", "impressions", "ctr", "position", "queries", "pages"]):
                    log(f"  • {l}")
        except Exception as e:
            log(f"Error reading performance: {e}")

        # 3. Check Index Coverage / Pages
        log("\n--- Checking Pages Indexing in Google Search Console ---")
        pages_url = f"https://search.google.com/search-console/index?resource_id={resource_id}"
        page.goto(pages_url, wait_until="networkidle")
        time.sleep(5)
        page.screenshot(path="gsc_pages_status.png", full_page=True)
        log("Captured gsc_pages_status.png")
        
        try:
            body_text = page.locator("body").inner_text()
            lines = [l.strip() for l in body_text.split("\n") if l.strip()]
            for l in lines[:30]:
                if any(k in l.lower() for k in ["indexed", "not indexed", "page indexing", "reasons"]):
                    log(f"  • {l}")
        except Exception as e:
            log(f"Error reading pages: {e}")

        # 4. URL Inspection for Clean Homepage & Category
        test_url = "https://swariyaweddings.com/"
        log(f"\n--- URL Inspection for {test_url} ---")
        inspect_url = f"https://search.google.com/search-console?resource_id={resource_id}"
        page.goto(inspect_url, wait_until="networkidle")
        time.sleep(3)
        search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
        if search_bar.is_visible():
            search_bar.click(force=True)
            search_bar.fill(test_url)
            page.keyboard.press("Enter")
            time.sleep(8)
            page.screenshot(path="gsc_inspect_homepage.png", full_page=True)
            log("Captured gsc_inspect_homepage.png")
            try:
                status_text = page.locator("body").inner_text()
                for l in [x.strip() for x in status_text.split("\n") if x.strip()][:25]:
                    if any(k in l.lower() for k in ["url is on google", "url is not on google", "crawled", "indexing", "sitemap", "referring page"]):
                        log(f"  • {l}")
            except Exception as e:
                log(f"Error reading inspect status: {e}")

        browser.close()
        log("\n✅ Completed Google Search Console Live Check!")

if __name__ == "__main__":
    main()
