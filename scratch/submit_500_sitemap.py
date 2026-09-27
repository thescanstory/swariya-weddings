import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

async def submit_sitemap():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        try:
            print("Navigating to GSC Sitemaps page...")
            await page.goto(f"https://search.google.com/search-console/sitemaps?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(5)
            
            # Look for sitemap input field
            input_box = page.locator('input[aria-label*="Enter sitemap URL"], input[placeholder*="Enter sitemap URL"]').first
            if await input_box.is_visible():
                print("Entering sitemap-bangalore-500.xml...")
                await input_box.fill("sitemap-bangalore-500.xml")
                submit_btn = page.locator('button:has-text("Submit"), div[role="button"]:has-text("Submit"), div[role="button"]:has-text("SUBMIT")').first
                if await submit_btn.is_visible():
                    await submit_btn.click()
                    print("Clicked submit for sitemap-bangalore-500.xml. Waiting 8s...")
                    await asyncio.sleep(8)
                    await page.screenshot(path="gsc_sitemap_bangalore_500_submitted.png", full_page=True)
                    print("Saved confirmation screenshot!")
            else:
                print("Sitemap input field not visible.")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(submit_sitemap())
