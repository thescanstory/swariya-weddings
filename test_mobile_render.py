import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Emulate iPhone 14 / mobile viewport
        context = await browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
        )
        page = await context.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        await page.goto(file_path, wait_until="networkidle")
        await asyncio.sleep(1)

        # 1. Capture Mobile Hero
        await page.screenshot(path="mobile_hero_test.png", full_page=False)

        # 2. Scroll to and capture Quick Inquiry Section
        quick_inquiry = page.locator("#services")
        await quick_inquiry.scroll_into_view_if_needed()
        await asyncio.sleep(1)
        await page.screenshot(path="mobile_quick_inquiry_test.png", full_page=False)

        # 3. Test Mobile Nav toggle
        nav_toggle = page.locator(".nav-toggle")
        if await nav_toggle.is_visible():
            await nav_toggle.click()
            await asyncio.sleep(0.5)
            await page.screenshot(path="mobile_nav_open_test.png", full_page=False)

        await browser.close()
        print("Mobile render screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(main())
