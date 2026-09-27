import asyncio
import os
import json
import time
import urllib.request
from playwright.async_api import async_playwright

USER_DATA_DIR = os.path.expanduser("~/.gsc_playwright_profile")
RESOURCE_ID = "https://swariyaweddings.com/"
LOG_FILE = "/Users/mac/Documents/swariya-weddings-complete-project/seo_health_status.json"

CORE_URLS = [
    "https://swariyaweddings.com/wedding-planners-in-bangalore.html",
    "https://swariyaweddings.com/top-wedding-planners-in-bangalore-comparison.html",
    "https://swariyaweddings.com/kannada-wedding-planner-bengaluru.html",
    "https://swariyaweddings.com/sitemap.html",
    "https://swariyaweddings.com/sitemap-bangalore-500.xml",
    "https://swariyaweddings.com/sitemap.xml"
]

QUERIES_TO_MONITOR = [
    "wedding planners in bangalore",
    "kannada wedding planner in bangalore",
    "top wedding planners in bangalore comparison",
    "site:swariyaweddings.com wedding planners in bangalore"
]

def check_http_health():
    results = {}
    for url in CORE_URLS:
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                results[url] = {"status_code": resp.getcode(), "ok": resp.getcode() == 200}
        except Exception as e:
            results[url] = {"status_code": 0, "ok": False, "error": str(e)}
    return results

async def monitor_gsc_and_serp():
    health_data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "http_health": check_http_health(),
        "sitemap_status": {},
        "indexing_metrics": {},
        "serp_rankings": {},
        "critical_alerts": []
    }

    # Check HTTP health issues
    for u, status in health_data["http_health"].items():
        if not status["ok"]:
            health_data["critical_alerts"].append(f"HTTP Alert: {u} returned {status.get('status_code')} / {status.get('error')}")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()

        try:
            # 1. Check GSC Sitemaps Status
            print("Checking GSC Sitemaps status...")
            await page.goto(f"https://search.google.com/search-console/sitemaps?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(5)
            await page.screenshot(path="monitor_gsc_sitemaps.png")

            content = await page.content()
            if "Couldn't fetch" in content:
                health_data["critical_alerts"].append("GSC Alert: One or more sitemaps show 'Couldn't fetch'")
            if "Success" in content:
                health_data["sitemap_status"]["general"] = "Success"

            # 2. Check GSC Indexing Pages Status
            print("Checking GSC Pages indexing tab...")
            await page.goto(f"https://search.google.com/search-console/index?resource_id={RESOURCE_ID}", wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(5)
            await page.screenshot(path="monitor_gsc_indexing.png")
            
            # 3. Check Live Google SERP for Core Queries
            for query in QUERIES_TO_MONITOR:
                print(f"Monitoring SERP for query: '{query}'...")
                search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&gl=in&hl=en"
                await page.goto(search_url, wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(3)
                
                links = await page.query_selector_all("a[href*='swariyaweddings.com']")
                found = len(links) > 0
                slug_query = query.replace(" ", "_").replace(":", "_")
                await page.screenshot(path=f"monitor_serp_{slug_query}.png")
                
                health_data["serp_rankings"][query] = {
                    "swariya_visible": found,
                    "matched_links_count": len(links)
                }

        except Exception as e:
            health_data["critical_alerts"].append(f"Automation execution error: {e}")
        finally:
            await context.close()

    # Write log
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(health_data, f, indent=4)
    print(f"Health monitoring check finished. Results saved to {LOG_FILE}")
    return health_data

if __name__ == "__main__":
    asyncio.run(monitor_gsc_and_serp())
