import asyncio
import os
import json
from playwright.async_api import async_playwright

async def main():
    profile_dir = os.path.expanduser("~/.gsc_playwright_profile")
    queries = [
        "site:swariyaweddings.com",
        "Swariya Weddings",
        "Swariya Weddings Bangalore",
        "top luxury wedding planners in bangalore comparison swariya",
        "kannada wedding planner bengaluru swariya"
    ]

    async with async_playwright() as p:
        browser_context = await p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            viewport={"width": 1360, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser_context.pages[0] if browser_context.pages else await browser_context.new_page()

        report = {}

        for q in queries:
            print(f"Testing Google SERP for: '{q}'...", flush=True)
            encoded_q = q.replace(" ", "+").replace(":", "%3A")
            url = f"https://www.google.com/search?q={encoded_q}&hl=en&gl=in"
            
            try:
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(3)
                
                # Check for swariyaweddings.com in organic results
                data = await page.evaluate('''() => {
                    const results = [];
                    const headings = document.querySelectorAll('h3');
                    let rank = 1;
                    headings.forEach(h => {
                        const a = h.closest('a');
                        if (a && a.href && !a.href.includes('google.com')) {
                            const isSwariya = a.href.includes('swariyaweddings.com');
                            results.push({
                                rank: rank++,
                                title: h.innerText,
                                url: a.href,
                                isSwariya: isSwariya
                            });
                        }
                    });
                    return results;
                }''')
                
                swariya_matches = [r for r in data if r['isSwariya']]
                
                report[q] = {
                    "total_results": len(data),
                    "swariya_hits": swariya_matches,
                    "top_results": data[:5]
                }
                
                safe_name = q.replace(":", "_").replace(" ", "_").lower()[:30]
                await page.screenshot(path=f"real_serp_{safe_name}.png", full_page=False)
                
            except Exception as e:
                report[q] = {"error": str(e)}

        await browser_context.close()

        print("\n==================================================", flush=True)
        print("📊 REAL GOOGLE SERP RANKING AUDIT", flush=True)
        print("==================================================", flush=True)
        for query, info in report.items():
            print(f"\n🔍 Query: '{query}'")
            if "error" in info:
                print(f"   ❌ Error: {info['error']}")
                continue
            if info['swariya_hits']:
                for hit in info['swariya_hits']:
                    print(f"   ✅ [Rank #{hit['rank']}] {hit['title']}")
                    print(f"      🔗 {hit['url']}")
            else:
                print(f"   ⚠️ Swariya not in top {info['total_results']} results.")
                for idx, tr in enumerate(info['top_results'][:2], 1):
                    print(f"      #{idx}: {tr['title']} ({tr['url'][:50]}...)")

        with open("real_serp_summary.json", "w") as f:
            json.dump(report, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
