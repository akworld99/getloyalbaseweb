# getloyalbase.app

Marketing site for Loyalbase, served by GitHub Pages.

## Editing
- Subpage copy lives in `build/content.py`. Homepage FAQ, SEO tags and footer live in `build/build.py`.
- After any change, run from this folder:

```
python3 build/build.py      # pages, homepage SEO blocks, sitemap, robots, llms.txt, share images
node build/prerender.js     # writes the homepage's interactive sections into the HTML for crawlers
```

Copy rules: plain English, no em dashes or hyphens in visible text.
