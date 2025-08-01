#!/bin/bash
shopt -s nocaseglob

mkdir -p optimized_output/thumbs/jpg optimized_output/thumbs/webp optimized_output/full/jpg optimized_output/full/webp optimized_output/placeholders

for src in originals/*.{jpg,jpeg,png,tiff}; do
  [ -f "$src" ] || continue
  base=$(basename "$src")
  base="${base%.*}"
  safe_base=$(echo "$base" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
  echo "Processing $base"

  magick "$src" -auto-orient -resize 400x -strip -interlace Plane -quality 75 "optimized_output/thumbs/jpg/${safe_base}-thumb.jpg"
  cwebp -q 75 "optimized_output/thumbs/jpg/${safe_base}-thumb.jpg" -o "optimized_output/thumbs/webp/${safe_base}-thumb.webp"

  magick "$src" -auto-orient -resize 1600x -strip -interlace Plane -quality 75 "optimized_output/full/jpg/${safe_base}.jpg"
  cwebp -q 75 "optimized_output/full/jpg/${safe_base}.jpg" -o "optimized_output/full/webp/${safe_base}.webp"

  magick "$src" -auto-orient -resize 20x -strip -blur 0x8 -quality 30 "optimized_output/placeholders/${safe_base}-placeholder.jpg"
done

echo "✅ All done."
