import os
import re

def fix_css_paths():
    for root, _, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                is_sub = "venues/" in filepath or "blog/" in filepath or "ask/" in filepath
                correct_css = "../style.css" if is_sub else "style.css"
                
                content_new = re.sub(r'href=["\'](\.\./)?css/style\.css["\']', f'href="{correct_css}"', content)
                
                if content_new != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content_new)
                    print(f"Fixed stylesheet path in: {filepath}")

fix_css_paths()
