const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const prototypeDir = path.join(__dirname, 'prototype');
const imagesDir = path.join(__dirname, 'images');

(async () => {
    console.log('Launching browser...');
    const browser = await puppeteer.launch({
        headless: "new"
    });
    
    try {
        const files = fs.readdirSync(prototypeDir).filter(file => file.endsWith('.html'));
        
        console.log(`Found ${files.length} prototypes to capture.`);
        
        const page = await browser.newPage();
        await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 }); // Retina resolution
        
        for (const file of files) {
            const htmlPath = path.join(prototypeDir, file);
            const fileUri = `file:///${htmlPath.replace(/\\/g, '/')}`;
            const outPath = path.join(imagesDir, file.replace('.html', '.png'));
            
            console.log(`Capturing ${file}...`);
            await page.goto(fileUri, { waitUntil: 'networkidle0', timeout: 30000 });
            
            // Allow an extra second for web fonts to fully render
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            await page.screenshot({ path: outPath, fullPage: false });
            console.log(`Saved -> ${outPath}`);
        }
        
        console.log('Successfully captured all prototypes.');
        
    } catch (err) {
        console.error('Error during capture:', err);
    } finally {
        await browser.close();
    }
})();
