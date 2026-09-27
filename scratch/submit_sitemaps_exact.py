import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

async def submit_exact_sitemap(sitemap_name):
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        try:
            print(f"Opening GSC Sitemaps for {sitemap_name}...")
            await page.goto(f"https://search.google.com/search-console/sitemaps?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(4)
            
            # Press escape to close any feedback dialogs if open
            await page.keyboard.press("Escape")
            await asyncio.sleep(1)
            
            # Input field inside "Add a new sitemap" form
            input_box = page.locator('input[aria-label*="Add a new sitemap"], input[aria-label*="Enter sitemap URL"], input[name="sitemap_url"]').first
            if not await input_box.is_visible():
                input_box = page.locator('input[type="text"]').first
                
            if await input_box.is_visible():
                await input_box.click(force=True)
                await input_box.fill(sitemap_name)
                print(f"Filled: {sitemap_name}")
                await asyncio.sleep(1)
                
                # Submit button next to input
                submit_btn = page.locator('form button, div[data-action-id="sitemaps-submit-button"], button:has-text("Submit")').first
                if await submit_btn.is_visible():
                    await submit_btn.click()
                    print(f"Submitted {sitemap_name}! Waiting 8s for confirmation...")
                    await asyncio.sleep(8)
                    await page.screenshot(path=f"gsc_submitted_{sitemap_name}.png", full_page=True)
                    print(f"Saved screenshot: gsc_submitted_{sitemap_name}.png")
        finally:
            await context.close()

async def main():
    await submit_exact_sitemap("sitemap-bangalore-500.xml")
    await submit_exact_sitemap("sitemap.xml")

if __name__ == "__main__":
    asyncio.run(main())
