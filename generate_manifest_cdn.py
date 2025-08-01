#!/usr/bin/env python3
import json
from pathlib import Path

def humanize(s):
    return s.replace('-', ' ').title()

# Your jsDelivr spec
JSDELIVR_SPEC = "macbarton-eng/quilting-wizard-assets@main"
BASE = "images"

# Derive bases from local optimized_output to keep IDs in sync
local_thumb_dir = Path("optimized_output/thumbs/webp")
bases = {f.name[:-len("-thumb.webp")] for f in local_thumb_dir.glob("*-thumb.webp")}

threads = []
for base in sorted(bases):
    threads.append({
        "id": base,
        "name": humanize(base),
        "thumbnail_webp": f"https://cdn.jsdelivr.net/gh/{JSDELIVR_SPEC}/{BASE}/thumbs/webp/{base}-thumb.webp",
        "thumbnail_jpg": f"https://cdn.jsdelivr.net/gh/{JSDELIVR_SPEC}/{BASE}/thumbs/jpg/{base}-thumb.jpg",
        "full_webp": f"https://cdn.jsdelivr.net/gh/{JSDELIVR_SPEC}/{BASE}/full/webp/{base}.webp",
        "full_jpg": f"https://cdn.jsdelivr.net/gh/{JSDELIVR_SPEC}/{BASE}/full/jpg/{base}.jpg",
        "placeholder": None
    })

manifest = {"threads": threads, "pantographs": []}
with open("manifest_cdn.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Wrote manifest_cdn.json with {len(threads)} items.")
