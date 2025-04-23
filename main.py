from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    print("✅ Chromium er installeret og kører!")
    browser.close()
