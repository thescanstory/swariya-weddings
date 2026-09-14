import os
import re

url_fixes = {
    'href="destination-wedding-goa.html"': 'href="/destination-wedding-planner-in-goa.html"',
    'href="destination-wedding-udaipur.html"': 'href="/destination-wedding-planner-in-udaipur-rajasthan.html"',
    'href="destination-wedding-jaipur.html"': 'href="/destination-wedding-planner-in-jaipur-rajasthan.html"',
    'href="destination-wedding-kerala.html"': 'href="/destination-wedding-planner-in-kerala.html"',
    'href="destination-wedding-coorg.html"': 'href="/destination-wedding-planner-in-coorg.html"',
    "href='destination-wedding-goa.html'": "href='/destination-wedding-planner-in-goa.html'",
    "href='destination-wedding-udaipur.html'": "href='/destination-wedding-planner-in-udaipur-rajasthan.html'",
    "href='destination-wedding-jaipur.html'": "href='/destination-wedding-planner-in-jaipur-rajasthan.html'",
    "href='destination-wedding-kerala.html'": "href='/destination-wedding-planner-in-kerala.html'",
    "href='destination-wedding-coorg.html'": "href='/destination-wedding-planner-in-coorg.html'",
    'href="/destination-wedding-goa.html"': 'href="/destination-wedding-planner-in-goa.html"',
    'href="/destination-wedding-udaipur.html"': 'href="/destination-wedding-planner-in-udaipur-rajasthan.html"',
    'href="/destination-wedding-jaipur.html"': 'href="/destination-wedding-planner-in-jaipur-rajasthan.html"',
    'href="/destination-wedding-kerala.html"': 'href="/destination-wedding-planner-in-kerala.html"',
    'href="/destination-wedding-coorg.html"': 'href="/destination-wedding-planner-in-coorg.html"',
}

def fix_all_links():
    modified_count = 0
    for root, _, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                new_content = content
                for old_link, new_link in url_fixes.items():
                    if old_link in new_content:
                        new_content = new_content.replace(old_link, new_link)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    modified_count += 1
                    
    print(f"Fixed internal links across {modified_count} HTML files.")

if __name__ == "__main__":
    fix_all_links()
