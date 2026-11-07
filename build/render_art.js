// Renders the industry SVG illustrations to PNG (2x) for the share images.
// Run from the repo root before build.py:  node build/render_art.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const src = path.resolve(__dirname, '..', 'assets', 'ind');
  const out = path.resolve(__dirname, '.art');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 400, height: 240 }, deviceScaleFactor: 2, reducedMotion: 'reduce' });
  for (const f of fs.readdirSync(src).filter((f) => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(path.join(src, f), 'utf8').replace('@media (prefers-reduced-motion:reduce){*{animation:none!important}}', '*{animation:none!important}');
    await p.setContent(`<body style="margin:0">${svg}</body>`);
    await p.screenshot({ path: path.join(out, f.replace('.svg', '.png')), clip: { x: 0, y: 0, width: 400, height: 240 } });
  }
  await b.close();
  console.log('rendered art to', out);
})();
