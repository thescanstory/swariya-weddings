import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
URL_TO_INSPECT = "https://swariyaweddings.com/wedding-planners-in-bangalore.html"

async def main():
    async with async_playwright() as p:
        print("Launching browser with user data dir...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        
        # Navigate to GSC URL inspection directly
        gsc_url = f"https://search.google.com/search-console/inspect?resource_id=sc-domain%3Aswariyaweddings.com&id={URL_TO_INSPECT}"
        print(f"Navigating to: {gsc_url}")
        await page.goto(gsc_url, wait_until="domcontentloaded", timeout=60000)
        
        # Wait for inspection data or request indexing button
        print("Waiting for page inspection UI to settle...")
        await asyncio.sleep(10)
        await page.screenshot(path="gsc_inspect_bangalore_page.png")
        print("Screenshot saved: gsc_inspect_bangalore_page.png")
        
        # Look for "Request Indexing" button
        req_buttons = await page.query_selector_all("text='Request Indexing'")
        if not req_buttons:
            req_buttons = await page.query_selector_all("text='REQUEST INDEXING'")
            
        if req_buttons:
            print(f"Found {len(req_buttons)} request indexing button(s). Clicking...")
            await req_buttons[0].click()
            print("Clicked Request Indexing. Waiting 15s for dialog...")
            await asyncio.sleep(15)
            await page.screenshot(path="gsc_inspect_bangalore_after_req.png")
            print("Screenshot saved: gsc_inspect_bangalore_after_req.png")
        else:
            print("Request indexing button not immediately found. Checking text content...")
            content = await page.content()
            if "URL is on Google" in content:
                print("URL is already indexed or on Google!")
            elif "URL is not on Google" in content:
                print("URL is not on Google yet. Crawl queue requested.")
                
        await context.close()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
