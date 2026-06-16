import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import io
import pandas as pd

async def main():
    async with async_playwright() as p_api:
        browser = await p_api.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating...")
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(3000)
        
        # Click Circles tab
        await page.locator("a:has-text('वृत्त')").first.evaluate("node => node.click()")
        await page.wait_for_timeout(5000)
        
        # Click expand Circles
        await page.locator("a:has(img[alt^='Expand '])").first.evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
        await page.wait_for_timeout(3000)
        
        # Click expand Samanya (General) - usually the first one
        await page.locator("a:has(img[alt^='Expand '])").nth(1).evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
        await page.wait_for_timeout(3000)
        
        # Now click a leaf node (e.g. Betul)
        await page.locator("a:has-text('बैतूल')").first.evaluate("node => node.click()")
        await page.wait_for_timeout(3000)
        
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all tables
        tables = soup.find_all('table')
        print(f"Found {len(tables)} tables")
        
        html_io = io.StringIO(str(soup))
        try:
            dfs = pd.read_html(html_io)
            for i, df in enumerate(dfs):
                print(f"\nTable {i} Columns:", df.columns.tolist())
                if len(df) > 0:
                    print("First row:", df.iloc[0].to_dict())
        except Exception as e:
            print("Error parsing tables:", e)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
