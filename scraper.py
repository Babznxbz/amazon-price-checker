import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def scrape_price(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # ⛔ Not headless for debugging
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        page = await context.new_page()

        try:
            print("Navigating to URL...")
            await page.goto(url, timeout=60000)
            await page.wait_for_timeout(5000)  # give time for lazy loading

            # Use this more reliable CSS selector
            price_element = await page.query_selector(".a-price .a-offscreen")
            if price_element:
                price_text = await price_element.inner_text()
                cleaned = price_text.replace("₹", "").replace(",", "").strip()
                print(f"Found price: {cleaned}")
                await browser.close()
                return float(cleaned)

        except TimeoutError as te:
            print(f"Navigation timeout: {te}")
        except Exception as e:
            print(f"Scrape error: {e}")

        await browser.close()
        return None

def get_amazon_price(url):
    try:
        return asyncio.run(scrape_price(url))
    except Exception as e:
        print(f"get_amazon_price error: {e}")
        return None
