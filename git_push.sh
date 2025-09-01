#!/bin/bash
# Path to your bot repo
cd ~/mybot || exit

# Commit message
MSG=${1:-"Update bot code"}

# Pull remote changes first (rebase)
git pull --rebase origin main

# Add all changes
git add .

# Commit with provided message
git commit -m "$MSG"

# Push changes
git push origin main
