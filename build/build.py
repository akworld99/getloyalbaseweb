#!/usr/bin/env python3
"""Builds getloyalbase.app: subpages, homepage SEO blocks, sitemap, robots, llms.txt, share images.

Run from the repo root:  python3 build/build.py   then   node build/prerender.js
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402
import industries as I  # noqa: E402

C.PAGES.extend(I.PAGES)

SITE = "https://getloyalbase.app"
GA = "G-32C4JZB9DC"
WA_NUMBER = "94770274519"
EMAIL = "akmal@digisavvyteam.com"
LINKEDIN = "https://www.linkedin.com/in/akmal-afzal24"

PAGES = C.PAGES
BY_PATH = {p["path"]: p for p in PAGES}

HOME_FAQS = [
    ("What is Loyalbase?", "A customer retention app for WooCommerce and Shopify stores. It reads your orders, tells you who to message on WhatsApp and why, and proves how much came back. It also shows what's selling, which dates to plan for, and whether your ads paid."),
    ("How much does Loyalbase cost?", "$50 a month, flat. The price doesn't rise as your orders grow, and early access is free while we set you up."),
    ("Do I need a points program?", "No. Nothing to design, no discounts to fund. If you have one, keep it. They work together."),
    ("How does it know a customer is late?", "It learns each customer's own rhythm. Someone who orders every three weeks is flagged after about six weeks without an order. Someone who orders twice a year isn't flagged for about nine months. Yearly occasions are spotted when the same person orders around the same date in different years."),
    ("Is customer data safe?", "Names, phones, emails and addresses never leave your store. Loyalbase holds order facts and scrambled IDs it can't reverse. Names load from your store to your screen, and every lookup is logged."),
    ("How do I know the messages worked?", "Every message is matched to paid orders within 60 days, counted once. And 1 in 10 people are held back and not messaged, so Results shows what your messages really added."),
    ("Does it work with my POS and branches?", "Not yet. It's on the roadmap, starting with a sales file per branch and then direct sync for cloud POS systems. Walk in customers join the same lists when the till records a phone number."),
    ("Which countries does it work in?", "Any country. Phone numbers are matched in full international form, and money shows in your own currency."),
    ("I use Klaviyo or a points app. Do I switch?", "No. Keep them. Loyalbase finds the people who need a personal nudge and shows what it was worth."),
    ("Can I ask Loyalbase questions about my store?", "Yes. Type a question in plain words, like \"who ordered before Eid last year but not since\", or pick one of over 40 ready-made questions. You get a sentence, a table or a list of customers from your own orders. The ready-made questions don't need AI, and any AI only ever sees totals."),
    ("Can it find customers who order every festival?", "Yes. Customers are grouped by the festivals they order for, year by year: Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali and Thai Pongal. Ask for anyone who ordered for a festival in two or more different years."),
    ("Does it spot business and corporate customers?", "Yes. Anyone who orders with a company name, or from a work email address, is marked as a business customer, and people from the same company are counted together. Personal addresses like Gmail don't count, and the email never leaves your store."),
]

HOME_DESC = "Get customers to order again, no loyalty program. Loyalbase finds who stopped buying, writes a WhatsApp message and shows what came back. From $50 a month."
HOME_TITLE = "Loyalbase: Customer Retention App for WooCommerce and Shopify"

ORG = {
    "@type": "Organization",
    "@id": f"{SITE}/#org",
    "name": "Loyalbase",
    "url": f"{SITE}/",
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo-light.png", "width": 1406, "height": 340},
    "description": "Customer retention app for WooCommerce and Shopify stores.",
    "parentOrganization": {"@type": "Organization", "name": "Digisavvy"},
    "founder": {"@type": "Person", "name": "Akmal Afzal", "sameAs": [LINKEDIN]},
    "foundingLocation": {"@type": "Place", "name": "Colombo, Sri Lanka"},
    "areaServed": "Worldwide",
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "telephone": "+94770274519", "email": EMAIL, "availableLanguage": ["English"]}],
}
WEBSITE = {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "Loyalbase", "publisher": {"@id": f"{SITE}/#org"}, "inLanguage": "en"}
SOFTWARE = {
    "@type": "SoftwareApplication",
    "@id": f"{SITE}/#software",
    "name": "Loyalbase",
    "url": f"{SITE}/",
    "applicationCategory": "BusinessApplication",
    "applicationSubCategory": "Customer retention",
    "operatingSystem": "Web; WordPress with WooCommerce",
    "description": "Loyalbase reads a store's orders, finds customers who stopped buying or are due to order, writes a WhatsApp message for each, and shows the sales that came back, measured against a held back group.",
    "image": f"{SITE}/assets/og.png",
    "offers": {
        "@type": "Offer",
        "price": "50",
        "priceCurrency": "USD",
        "url": f"{SITE}/#pricing",
        "availability": "https://schema.org/InStock",
        "priceSpecification": {"@type": "UnitPriceSpecification", "price": "50", "priceCurrency": "USD", "unitText": "MONTH"},
    },
    "featureList": [
        "Daily list of customers to bring back, with reasons",
        "Late regulars, yearly occasions, unpaid checkouts, first time buyers, stopped ordering, best customers, corporate buyers",
        "WhatsApp messages written for each customer",
        "Held back group to prove what messages added",
        "Sales by returning and new customers, best sellers, bought together",
        "Peak dates with last year's numbers",
        "Meta ads, Facebook and Instagram posts and Google Analytics next to real sales",
        "Ask Loyalbase: plain-word questions about customers, sales, products and ads, with over 40 ready-made questions that run without AI",
        "Customers grouped by the festivals they order for: Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali and Thai Pongal",
        "Business customers recognised from the company name or a work email address",
        "Customer names, phones, emails and addresses stay on the store",
    ],
    "publisher": {"@id": f"{SITE}/#org"},
}

NAV = [("/industries/", "Industries"), ("/ask-loyalbase/", "Ask"), ("/woocommerce-customer-retention/", "WooCommerce"), ("/guides/", "Guides"), ("/compare/", "Compare"), ("/#pricing", "Pricing")]

FOOTER_COLS = [
    ("Product", [("/#week", "How it works"), ("/#features", "Features"), ("/ask-loyalbase/", "Ask Loyalbase"), ("/#pricing", "Pricing"), ("/woocommerce-customer-retention/", "WooCommerce"), ("/shopify-customer-retention/", "Shopify")]),
    ("Industries", [("/industries/bakeries-and-cake-shops/", "Bakeries and cake shops"), ("/industries/gifts-flowers-and-hampers/", "Gifts, flowers and hampers"), ("/industries/online-grocery/", "Online grocery"), ("/industries/beauty-and-skincare/", "Beauty and skincare"), ("/industries/fashion-and-clothing/", "Fashion and clothing"), ("/industries/", "All industries")]),
    ("Guides", [("/guides/how-to-find-customers-who-stopped-buying/", "Find customers who stopped buying"), ("/whatsapp-messages-to-bring-back-customers/", "WhatsApp templates"), ("/guides/how-to-prove-your-messages-worked/", "Prove your messages worked"), ("/guides/festival-customers/", "Festival regulars"), ("/guides/loyalty-program-vs-win-back-messages/", "Loyalty program or win back"), ("/guides/", "All guides")]),
    ("Compare", [("/compare/smile-io-alternative-for-woocommerce/", "Smile.io alternative"), ("/compare/loyalbase-vs-klaviyo/", "Loyalbase vs Klaviyo"), ("/compare/", "All comparisons")]),
    ("Company", [("/about/", "About"), ("/#invest", "Investors"), ("/privacy/", "Privacy"), (f"https://wa.me/{WA_NUMBER}", "WhatsApp us"), (f"mailto:{EMAIL}", "Email us")]),
]

GA_SNIPPET = f'''<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA}');</script>'''

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap">'''

WA_ICON = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"></path></svg>'


def esc(s):
    return html.escape(s, quote=True)


def slug_of(path):
    s = path.strip("/").replace("/", "-")
    return s or "home"


def og_path(path):
    return f"/assets/og/{slug_of(path)}.png"


def banner():
    return f'''<div class="lf-banner"><div class="lf-wrap"><span><span class="lf-dot" aria-hidden="true"></span><b>We're raising our first round.</b> Early partners welcome.</span><a href="/#invest">Talk to the founders →</a></div></div>'''


def header(current=None):
    cur_attr = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur_attr if h == current else ""}>{t}</a>' for h, t in NAV)
    return f'''<header class="lf-head"><div class="lf-wrap">
<a class="lf-logo" href="/" aria-label="Loyalbase home"><img src="/assets/logo-light.svg" alt="Loyalbase" width="141" height="34"></a>
<nav class="lf-nav" aria-label="Main">{links}</nav>
<a class="lf-btn" href="/#early-access" data-cta>Get early access</a>
</div></header>'''


def footer():
    cols = ""
    for title, links in FOOTER_COLS:
        items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in links)
        cols += f'<div><h2>{title}</h2><ul>{items}</ul></div>'
    return f'''<footer class="lf-foot"><div class="lf-wrap">
<div class="lf-foot-top">
<div class="lf-foot-brand"><img src="/assets/logo-dark.svg" alt="Loyalbase" width="124" height="30" loading="lazy"><p>Customer retention for WooCommerce and Shopify stores. Find who stopped buying, message them on WhatsApp, see what came back.</p></div>
{cols}
</div>
<div class="lf-foot-bottom"><span>© 2026 Loyalbase. A Digisavvy product, Colombo, Sri Lanka.</span><span>getloyalbase.app</span></div>
</div></footer>'''


def wa_float():
    return f'''<a class="lf-wa" href="https://wa.me/{WA_NUMBER}?text=Hi%2C%20I%27d%20like%20early%20access%20to%20Loyalbase%20for%20my%20store" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp" data-wa>{WA_ICON}</a>'''


def faq_entity(faqs, page_url):
    return {
        "@type": "FAQPage",
        "@id": f"{page_url}#faq",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


def crumbs_for(p):
    trail = [("/", "Home")]
    if p["section"] == "guides" and p["path"] != "/guides/":
        trail.append(("/guides/", "Guides"))
    if p["section"] == "compare" and p["path"] != "/compare/":
        trail.append(("/compare/", "Compare"))
    if p["section"] == "industries" and p["path"] != "/industries/":
        trail.append(("/industries/", "Industries"))
    label = {"/guides/": "Guides", "/compare/": "Compare", "/industries/": "Industries"}.get(p["path"], p["nav"])
    trail.append((p["path"], label))
    return trail


def page_schema(p):
    url = SITE + p["path"]
    trail = crumbs_for(p)
    graph = [ORG, WEBSITE]
    bc = {"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + href} for i, (href, name) in enumerate(trail)]}
    common = {"@id": f"{url}#page", "url": url, "name": p["title"], "description": p["description"], "isPartOf": {"@id": f"{SITE}/#website"},
              "breadcrumb": {"@id": f"{url}#breadcrumb"}, "inLanguage": "en", "datePublished": C.UPDATED, "dateModified": C.UPDATED,
              "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + og_path(p["path"])}}
    kind = p["schema"]
    if kind == "article":
        graph.append({**common, "@type": "WebPage", "mainEntity": {"@id": f"{url}#article"}})
        graph.append({"@type": "Article", "@id": f"{url}#article", "headline": p["h1"][:110], "description": p["description"],
                      "image": SITE + og_path(p["path"]), "datePublished": C.UPDATED, "dateModified": C.UPDATED,
                      "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"}, "mainEntityOfPage": {"@id": f"{url}#page"},
                      "inLanguage": "en", "about": {"@id": f"{SITE}/#software"}})
    elif kind == "product":
        graph.append({**common, "@type": "WebPage", "about": {"@id": f"{SITE}/#software"}})
        graph.append(SOFTWARE)
    elif kind == "collection":
        graph.append({**common, "@type": "CollectionPage"})
    elif kind == "about":
        graph.append({**common, "@type": "AboutPage", "about": {"@id": f"{SITE}/#org"}})
    else:
        graph.append({**common, "@type": "WebPage"})
    graph.append(bc)
    if p.get("faqs"):
        graph.append(faq_entity(p["faqs"], url))
    return {"@context": "https://schema.org", "@graph": graph}


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def head(title, desc, path, og_img, schema, extra=""):
    url = SITE + path
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{GA_SNIPPET}
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{'website' if path == '/' else 'article'}">
<meta property="og:site_name" content="Loyalbase">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{og_img}">
<meta name="theme-color" content="#0F2A4A">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="alternate" type="text/plain" title="LLM summary" href="/llms.txt">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{extra}{jsonld(schema)}'''


PAGE_JS = '''<script>
(function(){
  function ev(n,p){if(window.gtag)gtag('event',n,p||{});}
  document.querySelectorAll('[data-copy]').forEach(function(b){
    b.addEventListener('click',function(){
      var t=b.closest('.sx-tpl').querySelector('.sx-bubble').innerText;
      var done=function(){var o=b.textContent;b.textContent='Copied';setTimeout(function(){b.textContent=o;},1600);};
      if(navigator.clipboard){navigator.clipboard.writeText(t).then(done,function(){});}
      ev('template_copy',{template:b.closest('.sx-tpl').querySelector('h3').textContent});
    });
  });
  document.querySelectorAll('[data-cta]').forEach(function(a){a.addEventListener('click',function(){ev('cta_click',{label:a.textContent.trim(),page:location.pathname});});});
  document.querySelectorAll('[data-wa]').forEach(function(a){a.addEventListener('click',function(){ev('whatsapp_chat_click',{page:location.pathname});});});
})();
</script>'''


def faq_html_sub(faqs):
    items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
    return f'<h2 id="faq">Questions</h2><div class="sx-faq">{items}</div>'


def related_html(paths):
    if not paths:
        return ""
    cards = ""
    for path in paths:
        r = BY_PATH[path]
        kind = {"guides": "Guide", "compare": "Compare", "product": "Product", "company": "Company", "industries": "Industry"}[r["section"]]
        if path == "/whatsapp-messages-to-bring-back-customers/":
            kind = "Templates"
        cards += f'<a class="sx-rel" href="{path}"><span>{kind}</span><b>{esc(r["h1"])}</b></a>'
    return f'<div class="sx-related"><h2>Keep reading</h2><div class="sx-related-grid">{cards}</div></div>'


def sources_html(srcs):
    if not srcs:
        return ""
    items = "".join(f'<li><a href="{u}" rel="noopener">{esc(t)}</a></li>' for t, u in srcs)
    return f'<div class="sx-sources"><h2>Sources</h2><ul>{items}</ul></div>'


def word_count(s):
    return len(re.sub(r"<[^>]+>", " ", s).split())


def render_page(p):
    trail = crumbs_for(p)
    crumbs = "".join(
        f'<li><a href="{h}">{esc(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(n)}</li>'
        for i, (h, n) in enumerate(trail))
    words = word_count(p["body"]) + word_count(p.get("answer") or "") + sum(word_count(q + a) for q, a in p.get("faqs", []))
    mins = max(2, round(words / 220))
    meta = f'<span>Updated {C.UPDATED_TEXT}</span><span>{mins} min read</span><span>By the Loyalbase team</span>' if p["schema"] == "article" else f"<span>Updated {C.UPDATED_TEXT}</span>"
    answer = f'<div class="sx-answer"><span class="sx-answer-label">Short answer</span><p>{p["answer"]}</p></div>' if p.get("answer") else ""
    faqs = faq_html_sub(p["faqs"]) if p.get("faqs") else ""
    current = p["path"] if any(h == p["path"] for h, _ in NAV) else ("/guides/" if p["section"] == "guides" else "/compare/" if p["section"] == "compare" else "/industries/" if p["section"] == "industries" else None)
    body_cls = "sx-body" if p["path"] not in ("/guides/", "/industries/") else "sx-body sx-wide"
    page = f'''<!doctype html>
<html lang="en">
<head>
{head(p["title"], p["description"], p["path"], og_path(p["path"]), page_schema(p))}
</head>
<body class="sx">
<a class="sx-skip" href="#main">Skip to content</a>
{banner()}
{header(current)}
<main id="main">
<div class="sx-hero"><div class="lf-wrap">
<nav class="sx-crumbs" aria-label="Breadcrumb"><ol>{crumbs}</ol></nav>
<div class="sx-eyebrow">{esc(p["eyebrow"])}</div>
<h1>{esc(p["h1"])}</h1>
<p class="sx-stand">{esc(p["stand"])}</p>
<div class="sx-meta">{meta}</div>
</div></div>
<div class="sx-main"><div class="lf-wrap"><article class="{body_cls}"{' style="max-width: none"' if p["path"] in ("/guides/", "/industries/") else ""}>
{answer}
{p["body"]}
{faqs}
{sources_html(p.get("sources"))}
{related_html(p.get("related"))}
</article></div></div>
</main>
{footer()}
{wa_float()}
{PAGE_JS}
</body>
</html>
'''
    out = os.path.join(ROOT, p["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    return out


# ------------------------------------------------------------------ homepage
def home_schema():
    url = SITE + "/"
    page = {"@type": "WebPage", "@id": f"{url}#page", "url": url, "name": HOME_TITLE, "description": HOME_DESC, "isPartOf": {"@id": f"{SITE}/#website"},
            "about": {"@id": f"{SITE}/#software"}, "inLanguage": "en", "dateModified": C.UPDATED,
            "primaryImageOfPage": {"@type": "ImageObject", "url": f"{SITE}/assets/og.png"}}
    return {"@context": "https://schema.org", "@graph": [ORG, WEBSITE, page, SOFTWARE, faq_entity(HOME_FAQS, url)]}


def home_seo_block():
    url = SITE + "/"
    return f'''<!--SEO-->
<title>{esc(HOME_TITLE)}</title>
<meta name="description" content="{esc(HOME_DESC)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Loyalbase">
<meta property="og:title" content="Loyalbase: get customers to order again. No loyalty program.">
<meta property="og:description" content="{esc(HOME_DESC)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Loyalbase: get customers to order again. No loyalty program.">
<meta name="twitter:description" content="{esc(HOME_DESC)}">
<meta name="twitter:image" content="{SITE}/assets/og.png">
<meta name="theme-color" content="#0F2A4A">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="alternate" type="text/plain" title="LLM summary" href="/llms.txt">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
{jsonld(home_schema())}
<!--/SEO-->'''


def home_faq_block():
    items = "".join(f'<details style="border-bottom: 1px solid #E3E8EE"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in HOME_FAQS)
    return f"<!--FAQ-->{items}<!--/FAQ-->"


def home_guides_block():
    cards = [
        ("/guides/how-to-find-customers-who-stopped-buying/", "Guide", "How to find customers who stopped buying"),
        ("/whatsapp-messages-to-bring-back-customers/", "Templates", "7 WhatsApp messages that bring customers back"),
        ("/guides/how-to-prove-your-messages-worked/", "Guide", "How to prove your messages worked"),
        ("/guides/loyalty-program-vs-win-back-messages/", "Guide", "Loyalty program or win back messages?"),
    ]
    html_cards = "".join(
        f'<a href="{h}" class="lb-card lb-screen" style="display: block; padding: 20px; text-decoration: none"><span class="lb-eyebrow" style="color: #2A78D6; font-size: 12px">{k}</span><span style="display: block; margin-top: 6px; font-size: 17px; font-weight: 600; line-height: 1.35; color: #0F2A4A">{t}</span></a>'
        for h, k, t in cards)
    return f'''<!--GUIDES--><section id="guides" class="lb-soft-bg" style="padding: clamp(48px, 6vw, 80px) 0">
<div class="lb-wrap">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 12px">
<div><div class="lb-eyebrow" style="color: #2A78D6">Free guides</div><h2 class="lb-h2">Guides for store owners</h2></div>
<a href="/guides/" style="font-weight: 600; color: #1F63B6; text-decoration: none">All guides →</a>
</div>
<div style="margin-top: 26px; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px">{html_cards}</div>
</div>
</section><!--/GUIDES-->'''


ASK_DEMOS = [
    {
        "q": "Customers who ordered before Eid ul-Fitr 2026 but haven't ordered since",
        "a": "96 customers ordered in the 3 weeks before Eid and haven't been back. They spent $8,450 then. 61 said yes to WhatsApp.",
        "head": ["Customer", "Eid order", "Orders ever"],
        "rows": [["Aisha N.", "$140", "4"], ["Omar K.", "$95", "1"], ["Fatima R.", "$210", "6"]],
        "chip": "Eid buyers who didn't come back",
    },
    {
        "q": "Which festivals do my customers order for?",
        "a": "Christmas is your biggest festival: 412 customers, 96 of them in two or more years. Avurudu is next with 288.",
        "head": ["Festival", "Customers", "2+ years"],
        "rows": [["Christmas", "412", "96"], ["Avurudu", "288", "61"], ["Eid ul-Fitr", "203", "47"]],
        "chip": "Which festivals?",
    },
    {
        "q": "What new customers buy first, and who comes back",
        "a": "The gentle cleanser brings the most second orders: 41% of people who started with it came back.",
        "head": ["First product", "New customers", "Came back"],
        "rows": [["Vitamin C serum", "212", "28%"], ["Gentle cleanser", "148", "41%"], ["SPF 50 sunscreen", "131", "33%"]],
        "chip": "What brings people back?",
    },
    {
        "q": "Business customers (company name or work email), sorted by spend",
        "a": "148 customers order for a company, from 64 companies. They spent $52,300 in the last 12 months.",
        "head": ["Customer", "Orders", "Spend"],
        "rows": [["Ravi M.", "14", "$6,840"], ["Lena M.", "9", "$4,210"], ["James T.", "6", "$3,960"]],
        "chip": "Business customers",
    },
]


def ask_table(d):
    th = "".join(f"<th scope=\"col\">{esc(h)}</th>" for h in d["head"])
    tr = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in d["rows"])
    return f"<p>{esc(d['a'])}</p><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


ASK_JS = """<script>
(function(){
  var D=__DATA__;
  var q=document.getElementById('lb-ask-q'),out=document.getElementById('lb-ask-out'),chips=[].slice.call(document.querySelectorAll('.lb-ask-chip'));
  if(!q||!out)return;
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cur=0,timer=null,auto=true,seen=false;
  function mark(i){chips.forEach(function(c,j){c.setAttribute('aria-pressed',j===i?'true':'false');});}
  function next(){if(auto&&!still){timer=setTimeout(function(){show((cur+1)%D.length);},5200);}}
  function show(i){
    clearTimeout(timer);cur=i;mark(i);
    if(still){q.textContent=D[i].q;out.innerHTML=D[i].h;return;}
    out.classList.add('lb-ask-hide');q.textContent='';
    var t=D[i].q,k=0;
    (function type(){
      if(k<=t.length){q.textContent=t.slice(0,k);k+=2;timer=setTimeout(type,28);}
      else{q.textContent=t;timer=setTimeout(function(){out.innerHTML=D[i].h;out.classList.remove('lb-ask-hide');next();},280);}
    })();
  }
  chips.forEach(function(c){c.addEventListener('click',function(){auto=false;show(+c.getAttribute('data-ask'));if(window.gtag)gtag('event','ask_demo_click',{question:c.textContent});});});
  if(!still&&'IntersectionObserver' in window){
    new IntersectionObserver(function(es,o){es.forEach(function(e){if(e.isIntersecting&&!seen){seen=true;o.disconnect();timer=setTimeout(function(){show(1);},3200);}});},{threshold:.4}).observe(out);
  }
})();
</script>"""


def home_ask_block():
    first = ASK_DEMOS[0]
    chips = "".join(
        f'<button type="button" class="lb-ask-chip" data-ask="{i}" aria-pressed="{"true" if i == 0 else "false"}">{esc(d["chip"])}</button>'
        for i, d in enumerate(ASK_DEMOS))
    data = json.dumps([{"q": d["q"], "h": ask_table(d)} for d in ASK_DEMOS], ensure_ascii=False).replace("</", "<\\/")
    return f'''<!--ASK--><section id="ask" class="lb-reveal" style="background: #FFFFFF; padding: clamp(56px, 7vw, 100px) 0">
<div class="lb-wrap lb-ask-grid">
<div class="lb-ask-copy">
<div class="lb-eyebrow" style="color: #2A78D6">New: Ask Loyalbase</div>
<h2 class="lb-h2">Ask your store anything. <span class="lb-soft">In plain words.</span></h2>
<p class="lb-lead">Type a question the way you'd say it. Get the answer, a table or a list of customers to message, straight from your own orders.</p>
<ul class="lb-ask-points">
<li>Over 40 ready-made questions about customers, sales, products and ads. No AI needed.</li>
<li>Change any underlined word: the festival, the product, the area, the dates.</li>
<li>Knows Eid, Avurudu, Vesak, Deepavali, Christmas and more, even when the dates move.</li>
<li>Customer details stay on your store. Any AI only sees totals.</li>
</ul>
<p style="margin: 24px 0 0"><a href="/ask-loyalbase/" style="color: #1F63B6; font-weight: 600; text-decoration: none">See every question you can ask →</a></p>
</div>
<div class="lb-ask-demo">
<div class="lb-card lb-ask-box">
<div class="lb-ask-bar"><span class="lb-ask-ico" aria-hidden="true">?</span><div class="lb-ask-text"><span><span id="lb-ask-q">{esc(first["q"])}</span><span class="lb-ask-caret" aria-hidden="true"></span></span></div></div>
<div class="lb-ask-out" id="lb-ask-out">{ask_table(first)}</div>
</div>
<div class="lb-ask-chips" role="group" aria-label="Example questions">{chips}</div>
<p class="lb-ask-note">Example answers. Names and numbers are made up.</p>
</div>
</div>
{ASK_JS.replace("__DATA__", data)}
</section><!--/ASK-->'''


def home_industries_block():
    cards = "".join(
        f'<a class="lb-ind" href="/industries/{slug}/"><b>{esc(name)}</b><span>{esc(text)}</span></a>'
        for slug, name, text in I.HUB_ITEMS)
    return f'''<!--INDUSTRIES--><section id="industries" class="lb-soft-bg" style="padding: clamp(48px, 6vw, 84px) 0">
<div class="lb-wrap">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 12px">
<div style="min-width: 0; flex: 1 1 520px"><div class="lb-eyebrow" style="color: #2A78D6">Industries</div><h2 class="lb-h2">Built for how your store sells</h2>
<p class="lb-lead">A bakery loses a birthday. A grocery store loses a weekly shop. Loyalbase learns each customer's own rhythm, so it fits both.</p></div>
<a href="/industries/" style="font-weight: 600; color: #1F63B6; text-decoration: none">All industries →</a>
</div>
<div class="lb-ind-grid">{cards}</div>
</div>
</section><!--/INDUSTRIES-->'''


def patch_home():
    path = os.path.join(ROOT, "index.html")
    h = open(path, encoding="utf-8").read()

    # one time: wrap existing head SEO tags in markers
    if "<!--SEO-->" not in h:
        start = h.index("<title>")
        end = h.index("</script>", h.index('application/ld+json')) + len("</script>")
        h = h[:start] + "<!--SEO--><!--/SEO-->" + h[end:]
        h = h.replace('<link rel="preconnect" href="https://fonts.googleapis.com">\n', '<link rel="preconnect" href="https://fonts.googleapis.com">\n', 1)
    h = re.sub(r"<!--SEO-->.*?<!--/SEO-->", lambda m: home_seo_block(), h, count=1, flags=re.S)

    # one time: hero template close tag fix
    h = h.replace('</template><div data-mount="hero" style="display: contents"></div></sc-if>', '</sc-if></template><div data-mount="hero" style="display: contents"></div>')

    # one time: mount markers for prerendered content
    for name in ("hero", "ticker", "week", "lists", "form"):
        h = h.replace(f'<div data-mount="{name}" style="display: contents"></div>', f'<div data-mount="{name}" style="display: contents"><!--pre:{name}--><!--/pre:{name}--></div>')

    # FAQ
    if "<!--FAQ-->" not in h:
        h = re.sub(r'(<div class="lb-faq" style="margin-top: 20px; border-top: 1px solid #E3E8EE">)\n?(.*?)(\n</div>\n</div>\n</section>)', lambda m: m.group(1) + "<!--FAQ--><!--/FAQ-->" + m.group(3), h, count=1, flags=re.S)
    h = re.sub(r"<!--FAQ-->.*?<!--/FAQ-->", lambda m: home_faq_block(), h, count=1, flags=re.S)

    # Guides strip after FAQ section
    if "<!--GUIDES-->" not in h:
        h = h.replace("\n<!-- INVEST -->", "\n<!--GUIDES--><!--/GUIDES-->\n\n<!-- INVEST -->", 1)
    h = re.sub(r"<!--GUIDES-->.*?<!--/GUIDES-->", lambda m: home_guides_block(), h, count=1, flags=re.S)

    # Ask demo + industries strip, between features and privacy
    if "<!--ASK-->" not in h:
        h = h.replace("<!-- PRIVACY (short) -->", "<!--ASK--><!--/ASK-->\n\n<!--INDUSTRIES--><!--/INDUSTRIES-->\n\n<!-- PRIVACY (short) -->", 1)
    h = re.sub(r"<!--ASK-->.*?<!--/ASK-->", lambda m: home_ask_block(), h, count=1, flags=re.S)
    h = re.sub(r"<!--INDUSTRIES-->.*?<!--/INDUSTRIES-->", lambda m: home_industries_block(), h, count=1, flags=re.S)

    # nav: Platform -> Industries, Features -> Ask
    h = h.replace('<a href="#platform" style="color: #16212F; text-decoration: none">Platform</a>', '<a href="/industries/" style="color: #16212F; text-decoration: none">Industries</a>', 1)
    h = h.replace('<a href="#features" style="color: #16212F; text-decoration: none">Features</a>', '<a href="#ask" style="color: #16212F; text-decoration: none">Ask</a>', 1)

    # Footer
    if "<!--FOOT-->" not in h:
        h = re.sub(r"<footer style=.*?</footer>", "<!--FOOT--><!--/FOOT-->", h, count=1, flags=re.S)
    h = re.sub(r"<!--FOOT-->.*?<!--/FOOT-->", lambda m: "<!--FOOT-->" + footer() + "<!--/FOOT-->", h, count=1, flags=re.S)

    # main landmark
    if '<main id="main">' not in h:
        h = h.replace("</header>\n", "</header>\n<main id=\"main\">\n", 1)
        h = re.sub(r'(\n<a href="https://wa\.me/94770274519\?text=Hi%2C%20I%27d%20like%20early)', "\n</main>\\1", h, count=1)

    # nav: add Guides link
    if 'href="/guides/" style="color: #16212F' not in h:
        h = h.replace('<a href="#pricing" style="color: #16212F; text-decoration: none">Pricing</a>',
                      '<a href="#pricing" style="color: #16212F; text-decoration: none">Pricing</a>\n<a href="/guides/" style="color: #16212F; text-decoration: none">Guides</a>', 1)

    # logos: absolute paths + dimensions (prevents layout shift)
    h = h.replace('<img src="assets/logo-light.png" alt="Loyalbase" height="34" style="height: 34px; width: auto; display: block">',
                  '<img src="/assets/logo-light.png" alt="Loyalbase" width="144" height="34" style="height: 34px; width: auto; display: block">')
    h = h.replace('<img src="assets/logo-light.png" alt="" aria-hidden="true" style="height: 22px; width: auto; display: block">',
                  '<img src="/assets/logo-light.png" alt="" aria-hidden="true" width="93" height="22" style="height: 22px; width: auto; display: block">')
    h = h.replace('<img src="assets/logo-dark.png" alt="Loyalbase" style="height: 32px; width: auto; display: block">',
                  '<img src="/assets/logo-dark.png" alt="Loyalbase" width="134" height="32" loading="lazy" style="height: 32px; width: auto; display: block">')

    # vector logos
    h = h.replace('<img src="/assets/logo-light.png" alt="Loyalbase" width="144" height="34"', '<img src="/assets/logo-light.svg" alt="Loyalbase" width="141" height="34"')
    h = h.replace('<img src="/assets/logo-light.png" alt="" aria-hidden="true" width="93" height="22"', '<img src="/assets/logo-light.svg" alt="" aria-hidden="true" width="91" height="22"')
    h = h.replace('<img src="/assets/logo-dark.png" alt="Loyalbase" width="134" height="32"', '<img src="/assets/logo-dark.svg" alt="Loyalbase" width="132" height="32"')
    h = h.replace('width="132" height="32" loading="lazy" style="height: 32px; width: auto; display: block">', 'width="132" height="32" loading="lazy" style="height: 32px; width: auto; display: block; align-self: flex-start">')

    # hero platform badges link to their pages
    h = h.replace('<span style="display: inline-flex; align-items: center; gap: 8px; padding: 7px 12px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, .18); background: rgba(255, 255, 255, .06); font-weight: 600; font-size: 14px">WooCommerce <span class="lb-pill" style="background: #17704A; color: #FFFFFF; font-size: 11px">Live</span></span>',
                  '<a href="/woocommerce-customer-retention/" style="display: inline-flex; align-items: center; gap: 8px; padding: 7px 12px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, .18); background: rgba(255, 255, 255, .06); font-weight: 600; font-size: 14px; color: #FFFFFF; text-decoration: none">WooCommerce <span class="lb-pill" style="background: #17704A; color: #FFFFFF; font-size: 11px">Live</span></a>')
    h = h.replace('<span style="display: inline-flex; align-items: center; gap: 8px; padding: 7px 12px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, .18); background: rgba(255, 255, 255, .06); font-weight: 600; font-size: 14px">Shopify <span class="lb-pill" style="background: #A86411; color: #FFFFFF; font-size: 11px">Early access</span></span>',
                  '<a href="/shopify-customer-retention/" style="display: inline-flex; align-items: center; gap: 8px; padding: 7px 12px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, .18); background: rgba(255, 255, 255, .06); font-weight: 600; font-size: 14px; color: #FFFFFF; text-decoration: none">Shopify <span class="lb-pill" style="background: #A86411; color: #FFFFFF; font-size: 11px">Early access</span></a>')

    # contextual internal links
    h = h.replace('Public pricing and help pages, checked October 2026. Loyalbase works alongside all of them.</p>',
                  'Public pricing and help pages, checked October 2026. Loyalbase works alongside all of them. <a href="/compare/" style="color: #1F63B6; font-weight: 600">See detailed comparisons →</a></p>')
    if 'href="/privacy/" style="color: #7FB2F0' not in h:
        h = h.replace('Names and numbers load straight from your store to your screen, and every lookup is logged.</p>',
                      'Names and numbers load straight from your store to your screen, and every lookup is logged. <a href="/privacy/" style="color: #7FB2F0; font-weight: 600">How it works →</a></p>', 1)
    if 'templates-link' not in h:
        i = h.index("<!-- FEATURES GRID -->")
        j = h.rfind("</section>", 0, i)
        k = h.rfind("</div>", 0, j)
        h = h[:k] + '<p id="templates-link" style="margin: 14px 0 0; font-size: 15px"><a href="/whatsapp-messages-to-bring-back-customers/" style="color: #7FB2F0; font-weight: 600">Get all seven messages as free templates →</a></p>\n' + h[k:]

    open(path, "w", encoding="utf-8").write(h)


# ------------------------------------------------------------------ text extraction for llms-full.txt
class TextOut(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip, self.row = [], 0, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "button", "svg") or "data-copy" in a:
            self.skip += 1
        elif tag == "h2":
            self.out.append("\n\n## ")
        elif tag == "h3":
            self.out.append("\n\n### ")
        elif tag in ("p", "div", "ul", "ol", "table"):
            self.out.append("\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.row.append("")
        elif tag == "br":
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "button", "svg"):
            self.skip = max(0, self.skip - 1)
        elif tag == "tr" and self.row is not None:
            self.out.append("\n| " + " | ".join(c.strip() for c in self.row) + " |")
            self.row = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.row is not None and self.row:
            self.row[-1] += data
        elif self.row is None:
            self.out.append(data)

    def text(self):
        t = "".join(self.out)
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
        return t.strip()


def to_text(fragment):
    p = TextOut()
    p.feed(fragment)
    return p.text()


def write_llms():
    groups = [
        ("Product", ["/woocommerce-customer-retention/", "/shopify-customer-retention/", "/ask-loyalbase/"]),
        ("Industries", ["/industries/"] + [p["path"] for p in I.PAGES if p["section"] == "industries" and p["path"] != "/industries/"]),
        ("Guides", ["/guides/how-to-find-customers-who-stopped-buying/", "/whatsapp-messages-to-bring-back-customers/", "/guides/festival-customers/", "/guides/how-to-prove-your-messages-worked/", "/guides/loyalty-program-vs-win-back-messages/"]),
        ("Compare", ["/compare/", "/compare/smile-io-alternative-for-woocommerce/", "/compare/loyalbase-vs-klaviyo/"]),
        ("Company", ["/about/", "/privacy/"]),
    ]
    facts = """Key facts:
- What it is: a customer retention app for WooCommerce stores (live) and Shopify stores (early access). Not a points or loyalty program.
- What it does: reads a store's orders and, every morning, lists customers to bring back with the reason and the value of one more order: late regulars, yearly occasions, unpaid checkouts, first time buyers (45 to 150 days after a first order), customers who stopped ordering, best customers and corporate buyers. Each comes with a WhatsApp message ready to send.
- How "late" is decided: for customers with two or more orders, late means the days since their last order exceed the largest of 1.5 times their median gap, their median gap plus 21 days, and 45 days.
- Proof: every message is matched to the first paid order within 60 days, each order counted once. 1 in 10 people on the bring back lists are held back at random so Results shows how many orders the messages added.
- Ask Loyalbase: owners type a question in plain words or pick one of over 40 ready-made questions (customers, sales, products, Meta ads and posts). Answers are a sentence, a table or a customer list. Every date, festival, product, area and amount can be changed. Ready-made questions run without AI; where AI is switched on it only receives totals, product names, areas and order sources, never customer names, phones, emails or order numbers.
- Festival groups: customers are tagged by the festivals they order for, year by year, using a short ordering window for each (Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali, Thai Pongal). Days shared by two festivals count for neither.
- Business customers: recognised from the company name at checkout, or a work email domain when that's empty (personal providers and the shop's own domain excluded). Only a keyed hash of the domain leaves the store (plugin 0.5.0+).
- Industries it suits: bakeries and cake shops, gifts, flowers and hampers, online grocery, beauty and skincare, fashion and clothing, pet food and supplies, restaurants and cloud kitchens (own website orders), coffee, tea and specialty food, baby and kids, corporate gifting and B2B.
- Also includes: sales by returning and new customers, best sellers, products rising and falling, bought together, discount code performance, peak dates with last year's numbers, Meta ads and Facebook and Instagram posts and Google Analytics next to the store's real sales, a Monday brief, a monthly report, team logins, list downloads and Sendy email sends.
- Privacy: customer names, phone numbers, emails and addresses never leave the store. Loyalbase stores order facts and keyed hashes. Names load from the store to the owner's browser using a 5 minute signed pass, and each lookup is logged on the store.
- Setup: install the WordPress plugin (WordPress 6.2 or newer, PHP 7.4 or newer, WooCommerce), press Connect, approve. About 10 minutes.
- Price: $50 a month, flat; does not rise with order volume. Early access is free while the store is set up.
- Not yet: POS and branch sales, orders placed through delivery apps. Coming next: Shopify app, automatic WhatsApp reminders the owner approves, POS and branch sales, reorder links, referrals and review asks.
- Company: built by Digisavvy in Colombo, Sri Lanka; founded by Akmal Afzal. Contact: WhatsApp +94 77 027 4519, akmal@digisavvyteam.com."""
    lines = ["# Loyalbase", "", "> Loyalbase is a customer retention app for WooCommerce and Shopify stores. It finds customers who stopped buying or are due to order, writes a WhatsApp message for each, and shows the sales that came back, measured against a held back group. From $50 a month, flat.", "", facts, ""]
    lines.append("## Main page")
    lines.append(f"- [Loyalbase home]({SITE}/): what it does, a week with Loyalbase, features, comparison, pricing, FAQ")
    lines.append("")
    for title, paths in groups:
        lines.append(f"## {title}")
        for p in paths:
            pg = BY_PATH[p]
            lines.append(f"- [{pg['h1']}]({SITE}{p}): {pg['description']}")
        lines.append("")
    lines.append("## Optional")
    lines.append(f"- [Full text of every page]({SITE}/llms-full.txt)")
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

    full = ["# Loyalbase: full site text", "", facts, "", "# Home: frequently asked questions", ""]
    for q, a in HOME_FAQS:
        full += [f"## {q}", a, ""]
    for p in PAGES:
        full += ["", "---", "", f"# {p['h1']}", f"URL: {SITE}{p['path']}", ""]
        if p.get("answer"):
            full += ["Short answer: " + p["answer"], ""]
        full.append(to_text(p["body"]))
        if p.get("faqs"):
            full.append("\n## Questions")
            for q, a in p["faqs"]:
                full += [f"\n### {q}", a]
        if p.get("sources"):
            full.append("\nSources: " + "; ".join(f"{t} ({u})" for t, u in p["sources"]))
    open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full) + "\n")


def write_sitemap_robots():
    urls = ["/"] + [p["path"] for p in PAGES]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml.append(f"  <url><loc>{SITE}{u}</loc><lastmod>{C.UPDATED}</lastmod></url>")
    xml.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(xml) + "\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User",
            "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "DuckDuckBot", "CCBot", "meta-externalagent"]
    robots = ["# getloyalbase.app: search engines and AI assistants are welcome.", "User-agent: *", "Allow: /", "Disallow: /build/", ""]
    for b in bots:
        robots += [f"User-agent: {b}", "Allow: /", "Disallow: /build/", ""]
    robots.append(f"Sitemap: {SITE}/sitemap.xml")
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(robots) + "\n")


def write_404():
    page = f'''<!doctype html>
<html lang="en">
<head>
{head("Page not found | Loyalbase", "This page doesn't exist. Find guides and templates for bringing customers back.", "/404.html", "/assets/og.png", {"@context": "https://schema.org", "@graph": [ORG, WEBSITE]})}
<meta name="robots" content="noindex">
</head>
<body class="sx">
{header()}
<main id="main"><div class="sx-hero"><div class="lf-wrap">
<div class="sx-eyebrow">404</div><h1>This page went quiet</h1>
<p class="sx-stand">It doesn't exist, or it moved. Here's where most people are heading.</p>
</div></div>
<div class="sx-main"><div class="lf-wrap"><div class="sx-hub">
<a href="/"><span>Home</span><b>Loyalbase</b><p>Get customers to order again. No loyalty program.</p></a>
<a href="/guides/"><span>Guides</span><b>Guides for store owners</b><p>Find customers who stopped buying, and bring them back.</p></a>
<a href="/whatsapp-messages-to-bring-back-customers/"><span>Templates</span><b>7 WhatsApp messages</b><p>Copy and send.</p></a>
</div></div></div></main>
{footer()}
</body>
</html>
'''
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(page)


# ------------------------------------------------------------------ share images
def make_og_images():
    from PIL import Image, ImageDraw, ImageFont
    fdir = "/usr/share/fonts/opentype/inter/"
    def font(name, size):
        try:
            return ImageFont.truetype(fdir + name, size)
        except OSError:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    logo = Image.open(os.path.join(ROOT, "assets", "logo-dark.png")).convert("RGBA")
    logo.thumbnail((310, 75))
    os.makedirs(os.path.join(ROOT, "assets", "og"), exist_ok=True)

    def card(title, kicker, out):
        W, H = 1200, 630
        img = Image.new("RGB", (W, H), (8, 26, 48))
        px = img.load()
        for y in range(H):
            for x in range(0, W, 2):
                t = (x / W) * 0.6 + (y / H) * 0.4
                r, g, b = int(8 + (21 - 8) * t), int(26 + (60 - 26) * t), int(48 + (110 - 48) * t)
                px[x, y] = (r, g, b)
                if x + 1 < W:
                    px[x + 1, y] = (r, g, b)
        d = ImageDraw.Draw(img)
        img.paste(logo, (80, 70), logo)
        fk = font("Inter-SemiBold.otf", 28)
        d.text((82, 196), kicker.upper(), font=fk, fill=(127, 178, 240))
        size = 68
        while True:
            ft = font("InterDisplay-Bold.otf", size)
            words, lines, cur = title.split(), [], ""
            for w in words:
                trial = (cur + " " + w).strip()
                if d.textlength(trial, font=ft) <= 1040:
                    cur = trial
                else:
                    lines.append(cur)
                    cur = w
            lines.append(cur)
            if len(lines) <= 3 or size <= 46:
                break
            size -= 4
        y = 248
        for ln in lines[:4]:
            d.text((80, y), ln, font=ft, fill=(255, 255, 255))
            y += int(size * 1.15)
        d.text((82, 548), "getloyalbase.app", font=font("Inter-Medium.otf", 26), fill=(200, 212, 227))
        img.save(out, optimize=True)

    card("Get customers to order again. No loyalty program.", "Customer retention for WooCommerce and Shopify", os.path.join(ROOT, "assets", "og.png"))
    for p in PAGES:
        card(p["h1"], p["eyebrow"], os.path.join(ROOT, "assets", "og", slug_of(p["path"]) + ".png"))


if __name__ == "__main__":
    for p in PAGES:
        render_page(p)
    patch_home()
    write_llms()
    write_sitemap_robots()
    write_404()
    if "--no-images" not in sys.argv:
        make_og_images()
    print(f"built {len(PAGES)} pages + home, sitemap, robots, llms.txt, 404")
