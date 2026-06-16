import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p_api:
        browser = await p_api.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating...")
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
        
        print("Finding a leaf node...")
        links = await page.eval_on_selector_all(
            "a[id*='t'][href*='__doPostBack']",
            "elements => elements.filter(e => e.href.includes(\"'s\")).map(e => ({id: e.id, text: e.innerText.trim(), href: e.href}))"
        )
        
        if links:
            # Pick a leaf node other than 'वृत्त'
            target = None
            for link in links:
                if link['text'] != 'वृत्त':
                    target = link
                    break
            
            if target:
                print(f"Clicking leaf node: {target['text']}")
                await page.locator(f"#{target['id']}").first.evaluate("node => node.click()")
                await page.wait_for_timeout(4000)
                
                with open("leaf.html", "w", encoding="utf-8") as f:
                    f.write(await page.content())
                print("Saved leaf.html")
            else:
                print("No suitable leaf node found")
        else:
            print("No links found")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
