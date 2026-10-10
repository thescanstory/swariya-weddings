import asyncio
import os
import json
import urllib.parse
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"

QUERIES = [
    "swariya weddings",
    "swariya weddings bangalore",
    "kannada wedding planner in bangalore",
    "wedding planners in bangalore",
    "site:swariyaweddings.com"
]

async def check_serp_and_gsc():
    results = {
        "serp_results": {},
        "gsc_data": {}
    }

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()

        # 1. SERP Search
        for q in QUERIES:
            print(f"\nSearching Google for: '{q}'...")
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(q)}&gl=in&hl=en"
            await page.goto(search_url, wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(4)

            slug = q.replace(" ", "_").replace(":", "_")
            screenshot_path = f"live_rank_{slug}.png"
            await page.screenshot(path=screenshot_path)
            print(f"Saved screenshot: {screenshot_path}")

            # Analyze visible links and snippets
            links = await page.query_selector_all("a")
            swariya_links = []
            organic_position = None
            pos_counter = 0

            # Find search results container
            search_results = await page.query_selector_all("div#rso > div, div.g")
            for idx, res in enumerate(search_results):
                text = await res.inner_text()
                link_el = await res.query_selector("a[href*='swariyaweddings.com']")
                if link_el:
                    href = await link_el.get_attribute("href")
                    swariya_links.append(href)
                    if organic_position is None:
                        organic_position = idx + 1

            all_swariya = await page.query_selector_all("a[href*='swariyaweddings.com']")
            swariya_all_hrefs = [await a.get_attribute("href") for a in all_swariya]

            results["serp_results"][q] = {
                "visible": len(swariya_all_hrefs) > 0,
                "organic_rank": organic_position if organic_position else ("Found in page elements" if len(swariya_all_hrefs) > 0 else "Not in top 10"),
                "matched_urls": list(set(swariya_all_hrefs))[:5]
            }
            print(f"Result for '{q}': Rank={results['serp_results'][q]['organic_rank']}, Matched URLs={len(swariya_all_hrefs)}")

        # 2. Check GSC Performance
        try:
            print("\nNavigating to GSC Performance overview...")
            await page.goto(f"https://search.google.com/search-console/performance/search-analytics?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(5)
            await page.screenshot(path="live_gsc_performance_now.png", full_page=True)
            print("Saved GSC Performance screenshot: live_gsc_performance_now.png")
        except Exception as e:
            print(f"GSC Error: {e}")

        # 3. Check GSC Indexing Pages
        try:
            print("\nNavigating to GSC Indexing Pages...")
            await page.goto(f"https://search.google.com/search-console/index?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(5)
            await page.screenshot(path="live_gsc_indexing_now.png", full_page=True)
            print("Saved GSC Indexing screenshot: live_gsc_indexing_now.png")
        except Exception as e:
            print(f"GSC Indexing Error: {e}")

        await context.close()

    with open("live_ranking_report_now.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print("\nLive ranking audit complete!")

if __name__ == "__main__":
    asyncio.run(check_serp_and_gsc())
