#!/usr/bin/env python3
import zipfile
import os
import requests
import time

zip_path = "/tmp/swariya_deploy.zip"
exclude_dirs = {".git", ".gemini", "node_modules", ".agents", "scratch", ".system_generated", ".netlify"}
exclude_extensions = {".py", ".pyc", ".log", ".tmp"}

print("Creating deploy zip package...")
file_count = 0
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in exclude_extensions and not f.startswith("sw"):
                continue
            if f.endswith(".zip") or f.endswith(".tar.gz") or f == ".DS_Store":
                continue
            file_path = os.path.join(root, f)
            arcname = os.path.relpath(file_path, ".")
            zf.write(file_path, arcname)
            file_count += 1

size_mb = os.path.getsize(zip_path) / (1024 * 1024)
print(f"Zipped {file_count} files. Package size: {size_mb:.2f} MB")

headers = {
    "Authorization": "Bearer nfc_kFuBZiwk81rMVD11zFUMQhjRmEnyNKXBd3c4",
    "Content-Type": "application/zip"
}
url = "https://api.netlify.com/api/v1/sites/35d10d9d-bf93-4e21-b826-93b6e1d1526c/deploys"

print("Uploading deploy archive directly to Netlify Production...")
with open(zip_path, "rb") as f:
    resp = requests.post(url, headers=headers, data=f, timeout=180)

print(f"HTTP Status: {resp.status_code}")
if resp.status_code in (200, 201):
    data = resp.json()
    deploy_id = data.get("id")
    state = data.get("state")
    ssl_url = data.get("deploy_ssl_url")
    print(f"✅ Production Deploy Success!")
    print(f"Deploy ID: {deploy_id}")
    print(f"State: {state}")
    print(f"Deploy URL: {ssl_url}")
else:
    print(f"❌ Deploy Failed. Response:")
    print(resp.text)
