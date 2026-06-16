import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def expand_all_nodes(page):
    visited_expands = set()
    while True:
        expand_links = await page.locator("a:has(img[alt^='Expand '])").element_handles()
        unvisited_link = None
        unvisited_href = None
        for link in expand_links:
            href = await link.get_attribute("href")
            if href and href not in visited_expands:
                unvisited_link = link
                unvisited_href = href
                break
                
        if not unvisited_link:
            break
            
        try:
            await unvisited_link.evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
            visited_expands.add(unvisited_href)
            await page.wait_for_timeout(3000)
        except:
            visited_expands.add(unvisited_href)

async def main():
    async with async_playwright() as p_api:
        browser = await p_api.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating...")
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(3000)
        
        await page.locator("a:has-text('वृत्त')").first.evaluate("node => node.click()")
        await page.wait_for_timeout(5000)
        
        print("Expanding all nodes...")
        await expand_all_nodes(page)
        
        print("Finding Betul...")
        links = await page.eval_on_selector_all(
            "a[id*='t'][href*='__doPostBack']",
            "elements => elements.filter(e => e.href.includes(\"'s\")).map(e => ({id: e.id, text: e.innerText.trim(), href: e.href}))"
        )
        
        for link in links:
            if link['text'] == 'बैतूल':
                print("Clicking Betul...")
                await page.locator(f"#{link['id']}").first.evaluate("node => node.click()")
                await page.wait_for_timeout(5000)
                
                with open("betul_full.html", "w", encoding="utf-8") as f:
                    f.write(await page.content())
                print("Saved betul_full.html")
                break
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
