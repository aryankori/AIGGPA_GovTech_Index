import asyncio
from playwright.async_api import async_playwright
import csv

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating to MP Forest Directory...")
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(2000)
        
        # The tree view has links like javascript:__doPostBack(...)
        # Let's find the 'वित्त/बजट' link to click
        print("Finding link for 'वित्त/बजट' (Finance/Budget)...")
        finance_link = page.locator("a:has-text('वित्त/बजट')").first
        if await finance_link.count() > 0:
            print("Clicking Finance/Budget...")
            await finance_link.click()
            await page.wait_for_timeout(3000)
            
            # Now let's dump the HTML
            content = await page.content()
            with open("forest_finance.html", "w", encoding="utf-8") as f:
                f.write(content)
            print("Dumped finance table HTML.")
        else:
            print("Link not found!")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
