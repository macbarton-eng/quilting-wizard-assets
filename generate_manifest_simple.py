#!/usr/bin/env python3
import os, base64, json
from pathlib import Path

def humanize(s):
    return s.replace('-', ' ').title()

input_dir = Path("optimized_output")
thumbs_webp = input_dir / "thumbs" / "webp"
thumbs_jpg = input_dir / "thumbs" / "jpg"
full_webp = input_dir / "full" / "webp"
full_jpg = input_dir / "full" / "jpg"
placeholders = input_dir / "placeholders"

threads = []
bases = {f.name[:-len("-thumb.webp")] for f in thumbs_webp.glob("*-thumb.webp")}

for base in sorted(bases):
    placeholder_path = placeholders / f"{base}-placeholder.jpg"
    placeholder_data = None
    if placeholder_path.exists():
        with open(placeholder_path, "rb") as f:
            placeholder_data = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

    threads.append({
        "id": base,
        "name": humanize(base),
        "thumbnail_webp": str(thumbs_webp / f"{base}-thumb.webp"),
        "thumbnail_jpg": str(thumbs_jpg / f"{base}-thumb.jpg"),
        "full_webp": str(full_webp / f"{base}.webp"),
        "full_jpg": str(full_jpg / f"{base}.jpg"),
        "placeholder": placeholder_data
    })

manifest = {
    "threads": threads,
    "pantographs": []
}

with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Wrote manifest.json with {len(threads)} thread items.")
