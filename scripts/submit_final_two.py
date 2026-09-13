import time
import os
from playwright.sync_api import sync_playwright

def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=False,
            viewport={"width": 1440, "height": 900}
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        urls = [
            ("gayatri_vihar", "https://swariyaweddings.com/venues/gayatri-vihar-palace-grounds.html"),
            ("marwari", "https://swariyaweddings.com/marwari-wedding-planner-bengaluru.html")
        ]

        for name, u in urls:
            print(f"Inspecting: {u}")
            page.goto("https://search.google.com/search-console?resource_id=https://swariyaweddings.com/", wait_until="domcontentloaded")
            time.sleep(2)
            page.keyboard.press("Escape")

            search_bar = page.locator("input[placeholder*='Inspect any URL'], input[aria-label*='Inspect any URL']").first
            search_bar.click(force=True)
            search_bar.fill(u)
            page.keyboard.press("Enter")
            time.sleep(12)
            page.keyboard.press("Escape")

            btn = page.get_by_text("Request indexing", exact=False)
            if btn.count() > 0:
                btn.first.click(force=True)
                time.sleep(20)
                page.keyboard.press("Escape")

            shot = f"gsc_expansion_{name}.png"
            page.screenshot(path=shot)
            print(f"Saved: {shot}")

        browser.close()

if __name__ == "__main__":
    main()
