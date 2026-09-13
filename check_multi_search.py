import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900}
        )
        page = await context.new_page()

        # Check Bing
        print("Searching Bing for: Swariya Weddings")
        await page.goto("https://www.bing.com/search?q=Swariya+Weddings+Bangalore", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        await page.screenshot(path="bing_swariya_bangalore.png")

        # Check DuckDuckGo
        print("Searching DuckDuckGo for: site:swariyaweddings.com")
        await page.goto("https://html.duckduckgo.com/html/?q=site%3Aswariyaweddings.com", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        await page.screenshot(path="ddg_swariya_site.png")

        # Check DuckDuckGo for brand
        print("Searching DuckDuckGo for: Swariya Weddings Bangalore")
        await page.goto("https://html.duckduckgo.com/html/?q=Swariya+Weddings+Bangalore", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        await page.screenshot(path="ddg_swariya_brand.png")

        # Extract DDG results
        ddg_results = await page.evaluate('''() => {
            const items = [];
            document.querySelectorAll('.result__title a').forEach(el => {
                items.push({ title: el.innerText, url: el.href });
            });
            return items;
        }''')

        print("\n--- DUCKDUCKGO LIVE RESULTS ---")
        for idx, r in enumerate(ddg_results, 1):
            print(f"{idx}. {r['title']} | {r['url']}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
