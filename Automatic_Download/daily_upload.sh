#!/bin/bash

# Go to your repo directory
cd /home/diego/Premier-Analysis || exit 1

# Add all changes
git add .

# Commit with today's date (only if there are changes)
git diff --cached --quiet || git commit -m "Auto update on $(date '+%Y-%m-%d')"

# Push to GitHub
git push origin main
