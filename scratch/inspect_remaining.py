import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

URLS = [
    "https://swariyaweddings.com/top-wedding-planners-in-bangalore-comparison.html",
    "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html"
]

async def inspect(url):
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        try:
            print(f"Opening GSC for {url}...")
            await page.goto(f"https://search.google.com/search-console?resource_id={RESOURCE_ID}", timeout=45000)
            await asyncio.sleep(5)
            search_bar = page.locator('input[placeholder*="Inspect any URL"], input[aria-label*="Inspect any URL"]').first
            if await search_bar.is_visible():
                await search_bar.click(force=True)
                await search_bar.fill(url)
                await page.keyboard.press("Enter")
                print("Waiting 12s for inspection result...")
                await asyncio.sleep(12)
                
                req_btn = page.locator('div[role="button"]:has-text("REQUEST INDEXING"), button:has-text("Request Indexing"), div[role="button"]:has-text("Request indexing")')
                if await req_btn.count() > 0 and await req_btn.first.is_visible():
                    print(f"Submitting indexing request for {url}...")
                    await req_btn.first.click()
                    await asyncio.sleep(12)
                    print(f"Indexing request submitted for {url}")
                else:
                    print(f"Request button not active or already in queue for {url}")
        finally:
            await context.close()

async def main():
    for u in URLS:
        try:
            await inspect(u)
            await asyncio.sleep(3)
        except Exception as e:
            print(f"Error on {u}: {e}")

if __name__ == "__main__":
    asyncio.run(main())
