import os
import re
import json

def validate_all_schemas():
    total_files = 0
    total_schemas = 0
    errors = 0
    
    for root, _, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                total_files += 1
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                # Find all <script type="application/ld+json">
                matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
                for block in matches:
                    total_schemas += 1
                    try:
                        json.loads(block.strip())
                    except Exception as e:
                        print(f"❌ Error parsing JSON-LD in {filepath}: {e}")
                        errors += 1
                        
    print(f"✅ Schema Validation Complete: {total_schemas} JSON-LD schemas validated across {total_files} HTML files with {errors} errors.")
    return errors == 0

if __name__ == "__main__":
    validate_all_schemas()
