import asyncio
import json
import os
import time
from datetime import datetime
from playwright.async_api import async_playwright

KEYWORD_TARGETS = [
    "Swariya Weddings",
    "Swariya Weddings Bangalore",
    "Luxury Wedding Planners in Bangalore",
    "Destination Wedding Planner in Bangalore",
    "Wedding Planners in Sadashivanagar Bangalore",
    "Wedding Planners in Palace Grounds Bangalore",
    "Wedding Planners in Lavelle Road Bangalore",
    "Wedding Planners in Indiranagar Bangalore",
    "Wedding Planners in Whitefield Bangalore",
    "Wedding Planners in HSR Layout",
    "Wedding Planners in Koramangala Bangalore",
    "Destination Wedding Planner in Udaipur",
    "Destination Wedding Planner in Goa",
    "Destination Wedding Planner in Kerala",
    "Destination Wedding Planner in Coorg",
    "NRI Destination Wedding Planner India",
    "Marwari Wedding Planner Bangalore",
    "Telugu Wedding Planner Bangalore",
    "Tamil Brahmin Wedding Planner Bangalore",
    "Cost of Destination Wedding in Goa 2026",
    "Palace Grounds Wedding Planners Bangalore",
    "The Tamarind Tree Wedding Cost"
]

async def run_rank_audit():
    print("=" * 70)
    print("📊 SWARIYA WEDDINGS — AUTOMATED SEARCH ENGINE RANK TRACKER")
    print(f"🕒 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    rankings = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900}
        )
        page = await context.new_page()

        for kw in KEYWORD_TARGETS:
            print(f"\n🔍 Tracking Keyword: \"{kw}\"...")
            url = f"https://www.google.com/search?q={kw.replace(' ', '+')}&hl=en&num=20"
            try:
                await page.goto(url, timeout=30000, wait_until="domcontentloaded")
                await asyncio.sleep(2)

                results = await page.evaluate('''() => {
                    const items = [];
                    const searchResults = document.querySelectorAll('div.g, div[data-hveid]');
                    searchResults.forEach(el => {
                        const titleEl = el.querySelector('h3');
                        const linkEl = el.querySelector('a');
                        if (titleEl && linkEl && linkEl.href && !linkEl.href.includes('google.com/search')) {
                            items.push({
                                title: titleEl.innerText,
                                url: linkEl.href
                            });
                        }
                    });
                    return items;
                }''')

                swariya_pos = None
                swariya_url = None
                top_competitors = []

                for idx, r in enumerate(results, 1):
                    if "swariyaweddings.com" in r["url"] or "swariya" in r["title"].lower():
                        if swariya_pos is None:
                            swariya_pos = idx
                            swariya_url = r["url"]
                    if idx <= 5:
                        top_competitors.append(f"#{idx} {r['title'][:45]} ({r['url'][:40]}...)")

                status_str = f"🏆 Rank #{swariya_pos}" if swariya_pos else "⏳ In Crawl Queue (Beyond Page 2)"
                print(f"   Result: {status_str}")

                rankings.append({
                    "keyword": kw,
                    "rank": swariya_pos if swariya_pos else ">20",
                    "url_ranking": swariya_url if swariya_url else "N/A",
                    "top_results": top_competitors[:3]
                })

            except Exception as e:
                print(f"   Error fetching {kw}: {e}")
                rankings.append({"keyword": kw, "rank": "Error", "error": str(e)})

        await browser.close()

    # Save to JSON
    report_data = {
        "audit_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_keywords_tracked": len(KEYWORD_TARGETS),
        "rankings": rankings
    }

    with open("rankings_report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    print("\n" + "=" * 70)
    print("📈 RANK TRACKING BASELINE GENERATED -> rankings_report.json")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(run_audit := run_rank_audit())
