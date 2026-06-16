import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p_api:
        browser = await p_api.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating to MP Forest Directory...")
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(3000)
        
        print("Clicking Circles tab...")
        await page.locator("a:has-text('वृत्त')").first.evaluate("node => node.click()")
        await page.wait_for_timeout(5000)
        
        print("Expanding Circles Root...")
        expand_links = await page.locator("a:has(img[alt^='Expand '])").element_handles()
        if expand_links:
            await expand_links[0].evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
            await page.wait_for_timeout(3000)
        
        # Expand general node
        expand_links = await page.locator("a:has(img[alt^='Expand '])").element_handles()
        if len(expand_links) > 1:
            await expand_links[1].evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
            await page.wait_for_timeout(3000)
            
        print("Clicking specific leaf node...")
        # Now click a real leaf node (e.g. Betul)
        leaf_nodes = await page.locator("a[id*='t'][href*='__doPostBack']:has-text('बैतूल')").element_handles()
        if leaf_nodes:
            print("Found Betul node!")
            await leaf_nodes[0].evaluate("node => node.click()")
            await page.wait_for_timeout(4000)
            
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            tables = soup.find_all('table')
            for i, t in enumerate(tables):
                headers = [th.text.strip() for th in t.find_all('th')]
                if headers:
                    print(f"Table {i} Headers: {headers}")
                else:
                    first_row = t.find('tr')
                    if first_row:
                        tds = [td.text.strip() for td in first_row.find_all('td')]
                        print(f"Table {i} First Row: {tds}")
        else:
            print("Could not find Betul node.")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
