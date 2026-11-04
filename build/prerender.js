// Writes the first render of the homepage's interactive sections into index.html,
// so crawlers that don't run JavaScript (most AI answer engines) still see the content.
// Run from the repo root after build.py:  node build/prerender.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const file = path.resolve(__dirname, '..', 'index.html');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.route('**/*', (r) => (r.request().url().startsWith('file:') ? r.continue() : r.abort()));
  await page.goto('file://' + file);
  await page.waitForTimeout(400);
  const mounts = await page.evaluate(() => {
    const out = {};
    document.querySelectorAll('[data-mount]').forEach((m) => { out[m.dataset.mount] = m.innerHTML; });
    return out;
  });
  await browser.close();
  let html = fs.readFileSync(file, 'utf8');
  for (const [name, inner] of Object.entries(mounts)) {
    const re = new RegExp(`<!--pre:${name}-->[\\s\\S]*?<!--/pre:${name}-->`);
    if (!re.test(html)) { console.error('missing marker', name); process.exit(1); }
    html = html.replace(re, () => `<!--pre:${name}-->${inner}<!--/pre:${name}-->`);
  }
  fs.writeFileSync(file, html);
  console.log('prerendered', Object.keys(mounts).map((k) => `${k}:${mounts[k].length}`).join(' '));
})();
