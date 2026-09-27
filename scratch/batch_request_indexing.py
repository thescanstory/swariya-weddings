import asyncio
import os
import time
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

URLS_TO_INSPECT = [
    "https://swariyaweddings.com/wedding-planners-in-bangalore.html",
    "https://swariyaweddings.com/top-wedding-planners-in-bangalore-comparison.html",
    "https://swariyaweddings.com/sitemap.html",
    "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html"
]

async def inspect_url(page, url):
    print(f"\n--- Inspecting {url} ---")
    await page.goto(f"https://search.google.com/search-console?resource_id={RESOURCE_ID}", wait_until="domcontentloaded")
    await asyncio.sleep(4)
    
    # Locate search bar
    search_bar = page.locator('input[placeholder*="Inspect any URL"], input[aria-label*="Inspect any URL"]').first
    if await search_bar.is_visible():
        await search_bar.click(force=True)
        await search_bar.fill(url)
        await page.keyboard.press("Enter")
        print("Submitted URL in search bar, waiting 10s for Google retrieval...")
        await asyncio.sleep(10)
        
        slug = url.split("/")[-1].replace(".html", "")
        await page.screenshot(path=f"gsc_inspect_{slug}.png", full_page=True)
        print(f"Saved inspection screenshot: gsc_inspect_{slug}.png")
        
        # Check for REQUEST INDEXING button
        req_btn = page.locator('div[role="button"]:has-text("REQUEST INDEXING"), button:has-text("Request Indexing"), div[role="button"]:has-text("Request indexing")')
        if await req_btn.count() > 0 and await req_btn.first.is_visible():
            print("Found REQUEST INDEXING button. Submitting live indexing request...")
            await req_btn.first.click()
            await asyncio.sleep(12)
            await page.screenshot(path=f"gsc_req_done_{slug}.png", full_page=True)
            print(f"Indexing request submitted for {url}!")
        else:
            print("Request indexing button not visible or already queued.")
    else:
        print("Search bar not found on GSC dashboard.")

async def main():
    async with async_playwright() as p:
        print("Starting persistent context...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        
        for url in URLS_TO_INSPECT:
            try:
                await inspect_url(page, url)
            except Exception as e:
                print(f"Error inspecting {url}: {e}")
                
        await context.close()
        print("\nAll URL inspections complete!")

if __name__ == "__main__":
    asyncio.run(main())
