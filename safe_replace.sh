#!/bin/bash
find . -type f ! -path "./.git/*" | while read -r file; do
  if file -I "$file" | grep -q 'charset=utf-8'; then
    sed -i '' 's/wellness_hub/wellness_hub/g' "$file"
  fi
done
