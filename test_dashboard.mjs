import { chromium } from 'playwright';

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();

    page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));

    await page.goto('http://localhost:5173/dashboard.html');

    await page.waitForTimeout(2000); // let FB initialize

    console.log("Clicking new session btn via ID...");
    await page.click('#new-session-btn');

    await page.waitForTimeout(2000);

    const url = page.url();
    console.log("Current URL after click:", url);

    const isModalVisible = await page.isVisible('#session-modal');
    console.log("Is Session Modal Visible?", isModalVisible);

    await browser.close();
})();
