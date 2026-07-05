#!/bin/bash
# Prompt Skills Scraper - Run Script
# Collects high-quality prompt skills from real, verified GitHub repositories
# All content is ACTUALLY scraped - no fabrication

set -e

cd "$(dirname "$0")"

echo "📦 Installing dependencies..."
pip install -q requests beautifulsoup4 lxml rich aiohttp

echo ""
echo "🚀 Starting Prompt Skills Scraper..."
echo ""

python -m scraper.main "$@"
