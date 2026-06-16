import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(2000)
        
        circle_tab = page.locator("a:has-text('वृत्त')").first
        await circle_tab.click()
        await page.wait_for_timeout(5000)
        
        content = await page.content()
        with open("forest_circles.html", "w", encoding="utf-8") as f:
            f.write(content)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
