import asyncio
import os
import json
from playwright.async_api import async_playwright

async def main():
    queries = [
        "site:swariyaweddings.com",
        "Swariya Weddings",
        "Swariya Weddings Bangalore",
        "top luxury wedding planners in bangalore comparison",
        "kannada wedding planner bengaluru",
        "3 day destination wedding cost at the tamarind tree bangalore"
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1360, "height": 900},
            locale="en-IN"
        )
        page = await context.new_page()

        report = {}

        for q in queries:
            print(f"Testing Google SERP for: '{q}'...", flush=True)
            encoded_q = q.replace(" ", "+").replace(":", "%3A")
            url = f"https://www.google.com/search?q={encoded_q}&hl=en&gl=in"
            
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=25000)
                await asyncio.sleep(2)
                
                # Check for swariyaweddings.com in top 30 organic results
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
                total_indexed = len(data) if "site:" in q else None
                
                report[q] = {
                    "total_organic_found": len(data),
                    "swariya_hits": swariya_matches,
                    "top_3": data[:3]
                }
                
                safe_name = q.replace(":", "_").replace(" ", "_").lower()[:30]
                await page.screenshot(path=f"serp_{safe_name}.png", full_page=False)
                
            except Exception as e:
                report[q] = {"error": str(e)}

        await browser.close()

        print("\n==================================================", flush=True)
        print("📊 LIVE GOOGLE SERP RANKING AUDIT RESULTS", flush=True)
        print("==================================================", flush=True)
        for query, info in report.items():
            print(f"\n🔍 Query: '{query}'")
            if "error" in info:
                print(f"   ❌ Error: {info['error']}")
                continue
            if info['swariya_hits']:
                for hit in info['swariya_hits']:
                    print(f"   ✅ FOUND Swariya at Rank #{hit['rank']}: {hit['title']}")
                    print(f"      URL: {hit['url']}")
            else:
                print(f"   ⚠️ Swariya not in top {info['total_organic_found']} organic results.")
                print(f"   Current Top 1: {info['top_3'][0]['title'] if info['top_3'] else 'N/A'}")

        with open("serp_audit_summary.json", "w") as f:
            json.dump(report, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
