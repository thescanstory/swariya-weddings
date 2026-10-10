import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

async def submit_pan_india_sitemap():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        try:
            print("Opening GSC Sitemaps...")
            await page.goto(f"https://search.google.com/search-console/sitemaps?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(4)
            await page.keyboard.press("Escape")
            await asyncio.sleep(1)
            
            input_box = page.locator('input[aria-label*="Add a new sitemap"], input[aria-label*="Enter sitemap URL"], input[name="sitemap_url"]').first
            if not await input_box.is_visible():
                input_box = page.locator('input[type="text"]').first
                
            if await input_box.is_visible():
                await input_box.click(force=True)
                await input_box.fill("sitemap-pan-india-national.xml")
                print("Filled sitemap-pan-india-national.xml")
                await asyncio.sleep(1)
                
                submit_btn = page.locator('form button, div[data-action-id="sitemaps-submit-button"], button:has-text("Submit")').first
                if await submit_btn.is_visible():
                    await submit_btn.click()
                    print("Submitted sitemap-pan-india-national.xml! Waiting 8s...")
                    await asyncio.sleep(8)
                    await page.screenshot(path="gsc_submitted_pan_india_national.png", full_page=True)
                    print("Saved confirmation screenshot!")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(submit_pan_india_sitemap())
