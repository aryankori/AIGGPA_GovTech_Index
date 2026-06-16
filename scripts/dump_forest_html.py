import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        # Wait a bit for the page to render
        await page.wait_for_timeout(3000)
        content = await page.content()
        with open("forest_home.html", "w", encoding="utf-8") as f:
            f.write(content)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
