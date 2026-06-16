import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import io
import os

async def main():
    async with async_playwright() as p_api:
        browser = await p_api.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating...")
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(3000)
        
        await page.locator("a:has-text('वृत्त')").first.evaluate("node => node.click()")
        await page.wait_for_timeout(5000)
        
        # Expand general node
        expand_links = await page.locator("a:has(img[alt^='Expand '])").element_handles()
        if expand_links:
            await expand_links[0].evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
            await page.wait_for_timeout(4000)
            
        expand_links = await page.locator("a:has(img[alt^='Expand '])").element_handles()
        if len(expand_links) > 1:
            await expand_links[1].evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
            await page.wait_for_timeout(4000)
            
        print("Finding Betul...")
        links = await page.eval_on_selector_all(
            "a[id*='t'][href*='__doPostBack']",
            "elements => elements.filter(e => e.href.includes(\"'s\")).map(e => ({id: e.id, text: e.innerText.trim(), href: e.href}))"
        )
        
        for link in links:
            if 'बैतूल' in link['text']:
                print("Clicking Betul...")
                await page.locator(f"#{link['id']}").first.evaluate("node => node.click()")
                await page.wait_for_timeout(4000)
                
                content = await page.content()
                soup = BeautifulSoup(content, 'html.parser')
                html_io = io.StringIO(str(soup))
                try:
                    dfs = pd.read_html(html_io)
                    for i, df in enumerate(dfs):
                        if df.shape[1] > 3 and len(df) > 1:
                            print(f"--- Table {i} ---")
                            print("Columns:", df.columns.tolist())
                            print(df.head(2))
                except Exception as e:
                    print("Parse error:", e)
                break
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
