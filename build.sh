#!/bin/bash

echo ">> Installing Python packages"
pip install -r requirements.txt

echo ">> Installing Chromium for Playwright"
playwright install chromium

echo ">> Build complete"
