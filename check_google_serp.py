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

        queries = [
            ("Swariya Weddings", "google_swariya_brand.png"),
            ("Swariya Weddings Bangalore", "google_swariya_bangalore.png"),
            ("site:swariyaweddings.com", "google_swariya_site_index.png")
        ]

        results_report = []

        for q, screenshot_name in queries:
            print(f"Searching Google for: {q}")
            url = f"https://www.google.com/search?q={q.replace(' ', '+')}&hl=en"
            try:
                await page.goto(url, timeout=30000, wait_until="domcontentloaded")
                await asyncio.sleep(3)
                
                # Take screenshot
                screenshot_path = os.path.join(os.getcwd(), screenshot_name)
                await page.screenshot(path=screenshot_path, full_page=False)
                print(f"Saved screenshot: {screenshot_name}")

                # Extract organic titles and links
                results = await page.evaluate('''() => {
                    const items = [];
                    const searchResults = document.querySelectorAll('div.g, div[data-hveid]');
                    searchResults.forEach(el => {
                        const titleEl = el.querySelector('h3');
                        const linkEl = el.querySelector('a');
                        const snippetEl = el.querySelector('div[style*="-webkit-line-clamp"], div.VwiC3b');
                        if (titleEl && linkEl) {
                            items.push({
                                title: titleEl.innerText,
                                url: linkEl.href,
                                snippet: snippetEl ? snippetEl.innerText : ''
                            });
                        }
                    });
                    return items.slice(0, 8);
                }''')

                results_report.append({"query": q, "screenshot": screenshot_name, "results": results})
            except Exception as e:
                print(f"Error searching {q}: {e}")

        await browser.close()

        print("\n--- GOOGLE SEARCH LIVE REPORT ---")
        for rep in results_report:
            print(f"\nQUERY: {rep['query']}")
            for idx, r in enumerate(rep['results'], 1):
                print(f"{idx}. {r['title']} | {r['url']}")

if __name__ == "__main__":
    asyncio.run(main())
