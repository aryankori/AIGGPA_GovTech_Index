import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import io
import os
import sys

def p(*args):
    print(*args, flush=True)

async def parse_table(page):
    try:
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        html_io = io.StringIO(str(soup))
        try:
            dfs = pd.read_html(html_io)
            for df in dfs:
                if 'अधिकारी का नाम' in df.columns or 'क्र.' in df.columns or 'फ़ोन कार्यालय' in df.columns:
                    if len(df.columns) > 3:
                        return df
        except ValueError:
            pass
    except Exception as e:
        print(f"Error parsing table: {e}")
    return None

async def expand_all_nodes(page):
    visited_expands = set()
    while True:
        # Get element handles instead of just hrefs to avoid CSS escaping issues
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
            break # No more unvisited expand links!
            
        try:
            name = unvisited_href.split(',')[-1].replace(')', '').replace("'", "")
            p(f"  Expanding: {name}")
            # Evaluate click on the DOM element handle directly
            await unvisited_link.evaluate("node => { let code = node.getAttribute('href'); if(code && code.startsWith('javascript:')) eval(code.replace('javascript:', '')); else node.click(); }")
            visited_expands.add(unvisited_href)
            await page.wait_for_timeout(3000)
        except Exception as e:
            p(f"Expand Error: {e}")
            visited_expands.add(unvisited_href) # Mark visited even on error to avoid infinite loop

async def main():
    csv_file = "mp_forest_directory.csv"
    
    rename_map = {
        'क्र.': 'S.No (क्र.)',
        'अधिकारी का नाम': 'Name (नाम)',
        'नाम': 'Name (नाम)',
        'पद': 'Designation (पद)',
        'फ़ोन कार्यालय': 'Office Phone (कार्यालय फोन)',
        'मोबाइल': 'Mobile (मोबाइल)',
        'ईमेल': 'Email (ईमेल)',
        'सेक्शन': 'Section (अनुभाग)',
        'अतिरिक्त प्रभार': 'Additional Charge (अतिरिक्त प्रभार)',
        'फैक्स': 'Fax (फैक्स)'
    }
    
    first_write = not os.path.exists(csv_file)
    
    async with async_playwright() as p_api:
        browser = await p_api.chromium.launch(headless=True)
        page = await browser.new_page()
        p("Navigating to MP Forest Directory...")
        await page.goto("https://mpforest.gov.in/publicdomain/Edirectory/Home.aspx")
        await page.wait_for_timeout(3000)
        
        # Only process Circles and Divisions to resume
        tabs = [
            ("Headquarters", "a:has-text('मुख्यालय')"),
            ("Circles", "a:has-text('वृत्त')"),
            ("Divisions", "a:has-text('वनमंडल')")
        ]
        
        for category_name, tab_selector in tabs:
            p(f"--- Processing Tab: {category_name} ---")
            tab_link = page.locator(tab_selector).first
            if await tab_link.count() > 0:
                await tab_link.evaluate("node => node.click()")
                await page.wait_for_timeout(5000)
                
                p(f"Expanding all nodes for {category_name}...")
                await expand_all_nodes(page)
                
                p(f"Collecting leaf nodes...")
                # Filter for links that select nodes (href has 's')
                links = await page.eval_on_selector_all(
                    "a[id*='t'][href*='__doPostBack']",
                    "elements => elements.filter(e => e.href.includes(\"'s\")).map(e => ({id: e.id, text: e.innerText.trim(), href: e.href}))"
                )
                
                p(f"Found {len(links)} nodes in {category_name}.")
                
                for link_info in links:
                    node_id = link_info['id']
                    node_text = link_info['text']
                    
                    if not node_id:
                        continue
                        
                    p(f"  Scraping node: {node_text}")
                    try:
                        # Find the node link by ID and click via evaluate to bypass special chars
                        node_locator = page.locator(f"#{node_id}").first
                        if await node_locator.count() > 0:
                            await node_locator.evaluate("node => node.click()")
                            await page.wait_for_timeout(3000)
                            
                            df = await parse_table(page)
                            if df is not None and not df.empty:
                                df = df.dropna(how='all')
                                if not df.empty:
                                    df['Category (श्रेणी)'] = category_name
                                    df['Node (नोड)'] = node_text
                                    df = df.rename(columns=rename_map)
                                    
                                    # Select only the columns we want in the final output
                                    columns_to_keep = ['Category (श्रेणी)', 'Node (नोड)', 'S.No (क्र.)', 'Name (नाम)', 'Designation (पद)', 'Office Phone (कार्यालय फोन)', 'Mobile (मोबाइल)', 'Email (ईमेल)', 'Section (अनुभाग)', 'Additional Charge (अतिरिक्त प्रभार)', 'Fax (फैक्स)']
                                    for col in columns_to_keep:
                                        if col not in df.columns:
                                            df[col] = ''
                                    df = df[columns_to_keep]
                                    
                                    df.to_csv(csv_file, mode='a', header=first_write, index=False, encoding='utf-8-sig')
                                    first_write = False
                                    p(f"    -> Extracted {len(df)} rows.")
                            else:
                                p("    -> No data table found.")
                        else:
                            p(f"    -> Error: Node #{node_id} not found.")
                    except Exception as e:
                        p(f"    -> Error: {e}")
            else:
                p(f"Tab {category_name} not found!")
                
        await browser.close()
        p("Finished scraping!")

if __name__ == "__main__":
    asyncio.run(main())
