import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

PAN_INDIA_URLS = [
    "https://swariyaweddings.com/destination-wedding-planner-in-india",
    "https://swariyaweddings.com/wedding-planners-in-goa",
    "https://swariyaweddings.com/wedding-planners-in-udaipur",
    "https://swariyaweddings.com/wedding-planners-in-jaipur",
    "https://swariyaweddings.com/wedding-planners-in-mumbai",
    "https://swariyaweddings.com/wedding-planners-in-delhi",
    "https://swariyaweddings.com/wedding-planners-in-hyderabad",
    "https://swariyaweddings.com/wedding-planners-in-chennai",
    "https://swariyaweddings.com/wedding-planners-in-kerala"
]

async def inspect_url(page, url):
    print(f"Opening GSC for {url}...")
    await page.goto(f"https://search.google.com/search-console?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=45000)
    await asyncio.sleep(4)
    search_bar = page.locator('input[placeholder*="Inspect any URL"], input[aria-label*="Inspect any URL"]').first
    if await search_bar.is_visible():
        await search_bar.click(force=True)
        await search_bar.fill(url)
        await page.keyboard.press("Enter")
        print(f"Requested inspect for {url}, waiting 10s...")
        await asyncio.sleep(10)
        req_btn = page.locator('div[role="button"]:has-text("REQUEST INDEXING"), button:has-text("Request Indexing"), div[role="button"]:has-text("Request indexing")')
        if await req_btn.count() > 0 and await req_btn.first.is_visible():
            await req_btn.first.click()
            print(f"Clicked Request Indexing for {url}!")
            await asyncio.sleep(10)

async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        for u in PAN_INDIA_URLS:
            try:
                await inspect_url(page, u)
            except Exception as e:
                print(f"Error on {u}: {e}")
        await context.close()
        print("Pan-India GSC inspection dispatch complete!")

if __name__ == "__main__":
    asyncio.run(main())
