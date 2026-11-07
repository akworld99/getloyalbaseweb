# Content for getloyalbase.app subpages. Plain English, no em dashes or hyphens in visible copy.
# Every fact here comes from the Loyalbase repo or a cited public source.

UPDATED = "2026-11-07"
UPDATED_TEXT = "7 November 2026"

SRC_SMILE_PLATFORMS = ("Smile.io help centre: supported ecommerce platforms", "https://help.smile.io/en/articles/4036185-supported-ecommerce-platforms")
SRC_SMILE_PRICE = ("Rivo: Smile.io pricing breakdown, April 2026 (a competing vendor)", "https://www.rivo.io/blog/smile-io-pricing")
SRC_LL_PRICE = ("Rivo: LoyaltyLion pricing breakdown, April 2026 (a competing vendor)", "https://www.rivo.io/blog/loyaltylion-pricing")
SRC_YOTPO = ("Yotpo Loyalty and Referrals pricing", "https://www.yotpo.com/v2/wp-content/uploads/2026/08/loyalty-pricing-1.md")
SRC_KLAVIYO_PRICE = ("Omnisend: Klaviyo pricing, May 2026 (a competing vendor)", "https://www.omnisend.com/blog/klaviyo-pricing/")
SRC_KLAVIYO_WA = ("Klaviyo: WhatsApp product launch, September 2025", "https://www.klaviyo.com/blog/klaviyo-whatsapp-product-launch")
SRC_KLAVIYO_ADDON = ("Klaviyo help centre: Marketing Analytics", "https://help.klaviyo.com/hc/en-us/articles/33789259613595-Getting-started-with-Marketing-Analytics")
SRC_LL_WOO = ("WPLoyalty: LoyaltyLion alternatives (a competing vendor)", "https://wployalty.net/best-loyaltylion-alternatives/")
SRC_META_OPTIN = ("Meta for Developers: Get opt in for WhatsApp", "https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in")


def table(head, rows, us_col=None):
    h = "<div class=\"sx-tablewrap\"><table class=\"sx-table\"><thead><tr>"
    for i, c in enumerate(head):
        cls = ' class="sx-us"' if us_col is not None and i == us_col else ""
        h += f'<th scope="col"{cls}>{c}</th>'
    h += "</tr></thead><tbody>"
    for r in rows:
        h += "<tr>"
        for i, c in enumerate(r):
            if i == 0:
                h += f'<th scope="row">{c}</th>'
            else:
                cls = ' class="sx-us"' if us_col is not None and i == us_col else ""
                h += f"<td{cls}>{c}</td>"
        h += "</tr>"
    return h + "</tbody></table></div>"


def tpl(tag, tag_bg, tag_fg, title, when, message, why):
    return f'''<div class="sx-tpl">
<div class="sx-tpl-head"><span class="sx-tag" style="background: {tag_bg}; color: {tag_fg}">{tag}</span><h3>{title}</h3></div>
<p class="sx-tpl-when"><b>When to send:</b> {when}</p>
<div class="sx-bubblewrap"><div class="sx-bubble">{message}</div></div>
<div class="sx-tpl-foot"><p><b>Why it works:</b> {why}</p><button type="button" class="sx-copy" data-copy>Copy message</button></div>
</div>'''


def cta(title="See this for your own store", text="Connect your store and get your first list in about ten minutes. From $50 a month, free while we set you up."):
    return f'''<div class="sx-cta"><h2>{title}</h2><p>{text}</p>
<div class="sx-cta-row"><a class="lf-btn lf-btn-lg lf-btn-light" href="/#early-access" data-cta>Get early access</a>
<a class="lf-btn lf-btn-lg lf-btn-wa" href="https://wa.me/94770274519?text=Hi%2C%20I%27d%20like%20to%20see%20Loyalbase%20for%20my%20store" data-cta>Ask on WhatsApp</a></div></div>'''


LISTS_ROWS = [
    ["Late regulars", "Customers with two or more orders who have gone quiet for longer than their usual gap."],
    ["Yearly occasions", "Customers who order around the same date every year, due in the next two weeks."],
    ["Unpaid checkouts", "People who picked what they wanted in the last two weeks and didn't finish paying."],
    ["First time buyers", "Bought once, 45 to 150 days ago. The window when a second order is most likely."],
    ["Stopped ordering", "Two or more orders in the past, nothing in over a year."],
    ["Best customers", "Your top buyers. Worth a thank you before any offer."],
    ["Corporate buyers", "People ordering for a company. Worth a call before office events and festive seasons."],
]

PAGES = []

# ---------------------------------------------------------------- WooCommerce
PAGES.append(dict(
    path="/woocommerce-customer-retention/",
    section="product",
    title="WooCommerce Customer Retention Plugin | Loyalbase",
    nav="WooCommerce",
    description="Find WooCommerce customers who stopped buying, send each a ready written WhatsApp message, and see the sales that came back. 10 minute setup, $50 a month.",
    eyebrow="For WooCommerce stores",
    h1="Get more repeat customers from your WooCommerce store",
    stand="WooCommerce keeps every order you've ever had. Loyalbase turns them into a short list each morning: who to message, why, and what it's worth.",
    answer="Loyalbase is a customer retention plugin and app for WooCommerce. Install the plugin, press Connect, and your order history comes in. Every morning you see which customers are late for their next order, have a yearly occasion coming up, stopped at payment, or bought once and never came back, each with a WhatsApp message ready to send. Results shows which messages brought sales back.",
    body=f'''
<h2>Why WooCommerce stores lose repeat customers</h2>
<p>WooCommerce is good at taking orders. It isn't built to tell you who stopped ordering. Its reports show totals: sales this month, top products, average order value. They don't tell you that a customer who used to buy every three weeks hasn't ordered in two months.</p>
<p>Customers rarely cancel. They drift to a competitor, a marketplace or the supermarket, and most owners only notice when the sales line goes flat. By then a friendly message is much less likely to work.</p>

<h2>What Loyalbase finds in your WooCommerce orders</h2>
<p>Seven lists, refreshed every day. Each person comes with the reason they're on the list and what one more order from them is worth.</p>
{table(["List", "Who is on it"], LISTS_ROWS)}
<p>You also get a WhatsApp message written for each list. You can change every word before it goes. See all seven in our <a href="/whatsapp-messages-to-bring-back-customers/">WhatsApp message templates</a>.</p>

<h2>How it works</h2>
<ol class="sx-steps">
<li><b>Install the Loyalbase plugin.</b> In WordPress, go to Plugins, then Add New, then Upload Plugin. The download already knows your account.</li>
<li><b>Press Connect to Loyalbase.</b> Approve once. Your store creates its own secret key, which never leaves your website.</li>
<li><b>Your order history comes in.</b> It sends in the background with a live count while the Loyalbase page is open. Big stores take minutes, not hours.</li>
<li><b>Open Today.</b> Up to three jobs a morning, on your phone or laptop. Tap a customer and WhatsApp opens with the message written.</li>
</ol>
<p>After that, Loyalbase updates after new orders and again every night.</p>

<h2>What the plugin sends, and what it never sends</h2>
<div class="sx-cols">
<div class="sx-card sx-card-good"><h3>Sent to Loyalbase</h3><ul><li>Order dates and amounts</li><li>Products bought</li><li>Delivery area</li><li>An occasion label such as "birthday", worked out on your site</li><li>Scrambled versions of the phone and email, so repeat customers can be recognised</li></ul></div>
<div class="sx-card sx-card-bad"><h3>Never sent</h3><ul><li>Names</li><li>Phone numbers</li><li>Email addresses</li><li>Street addresses</li><li>Cake or card wording</li></ul></div>
</div>
<p>The key used to scramble phone numbers and emails is created on your website and never sent, so Loyalbase can't turn them back into contact details. When you open a customer, your browser fetches their name straight from your store using a pass that expires in five minutes, and every lookup is logged in WordPress. Read more on our <a href="/privacy/">privacy page</a>.</p>

<h2>More than a list</h2>
<ul>
<li><b>Sales:</b> returning and new customers by month, best sellers, products rising and falling, what's bought together, and which discount codes bring people back.</li>
<li><b>Dates to plan for:</b> big sale and gifting dates with last year's numbers and the date your ads should go live.</li>
<li><b>Marketing:</b> connect Facebook and Google Analytics to see ad spend, posts and website visits next to the sales that really came in.</li>
<li><b>Bulk sends:</b> download any list as a WhatsApp campaign file or a spreadsheet, or send it to your Sendy email list. Only people who said yes are included.</li>
<li><b>WhatsApp tick box at checkout:</b> an optional box that lets customers say yes to WhatsApp messages. The answer is saved on the order as their consent record.</li>
<li><b>Proof:</b> 1 in 10 people on the bring back lists are held back, so Results shows what your messages really added. <a href="/guides/how-to-prove-your-messages-worked/">How that works</a>.</li>
</ul>

<h2>Requirements</h2>
<ul>
<li>WordPress 6.2 or newer (tested up to 6.8)</li>
<li>PHP 7.4 or newer</li>
<li>WooCommerce</li>
<li>Any country and currency. Phone numbers are matched in full international form.</li>
</ul>
{cta()}
''',
    faqs=[
        ("Do I need a developer to set it up?", "No. If you can install a WordPress plugin, you can set up Loyalbase. Upload the plugin, activate it, and press Connect to Loyalbase."),
        ("Will it slow down my store?", "The plugin sends order facts in the background in small batches. The only thing it adds to your checkout is the optional WhatsApp tick box, and you can leave that switched off."),
        ("What happens if I uninstall the plugin?", "Uninstalling removes Loyalbase's settings and keys from your site. Customers' WhatsApp consent stays saved on their orders, because it's their record. To remove your store's data from Loyalbase as well, use Delete this shop in Loyalbase settings."),
        ("Does it work with my email or loyalty plugin?", "Yes. Loyalbase doesn't change your checkout, prices or emails, so it runs alongside points plugins and email tools."),
        ("How much does it cost?", "$50 a month, flat, whatever your order volume. Early access is free while we set you up."),
    ],
    related=["/whatsapp-messages-to-bring-back-customers/", "/guides/how-to-find-customers-who-stopped-buying/", "/compare/smile-io-alternative-for-woocommerce/"],
    schema="product",
))

# ---------------------------------------------------------------- Shopify
PAGES.append(dict(
    path="/shopify-customer-retention/",
    section="product",
    title="Shopify Customer Retention App (Early Access) | Loyalbase",
    nav="Shopify",
    description="Loyalbase finds Shopify customers who stopped buying and gives you a WhatsApp message for each, with proof of what came back. Now in early access.",
    eyebrow="For Shopify stores",
    h1="Bring back Shopify customers without running a points program",
    stand="The Loyalbase Shopify app is in early access. Same lists, same proof and same privacy rules as our WooCommerce version, inside your Shopify admin.",
    answer="Loyalbase for Shopify is in early access. It reads your Shopify orders, finds customers who are late for their next order, have a yearly occasion coming up or bought once and never came back, and gives you a WhatsApp message for each. Join early access and we'll set your store up as soon as it can connect.",
    body=f'''
<h2>What Shopify stores get</h2>
{table(["List", "Who is on it"], LISTS_ROWS[:5])}
<p>Plus the rest of Loyalbase: sales by returning and new customers, dates to plan for with last year's numbers, Meta ads and posts next to real sales, and Results with a held back group so you know what your messages added.</p>

<h2>How it's different from a Shopify loyalty app</h2>
<p>Points apps such as Smile.io, LoyaltyLion and Yotpo reward customers who keep coming back. That's useful, but a customer who has stopped buying doesn't visit your store, so they never see their points.</p>
<p>Loyalbase goes after the ones who stopped. There's no widget to install, no rewards to design and no discounts to fund. You get a short list each morning and a message to send. Many stores run both. Read <a href="/guides/loyalty-program-vs-win-back-messages/">loyalty program or win back messages</a> for the full comparison.</p>

<h2>Privacy on Shopify</h2>
<p>Loyalbase works from order facts and scrambled IDs, not contact details. On Shopify, customer names load inside your Shopify admin, and are never stored by Loyalbase.</p>

<h2>What you can do today</h2>
<ol class="sx-steps">
<li><b>Export your orders</b> from Shopify admin as a CSV file.</li>
<li><b>Find the customers who stopped buying</b> with the spreadsheet method in our <a href="/guides/how-to-find-customers-who-stopped-buying/">step by step guide</a>.</li>
<li><b>Message them</b> using our <a href="/whatsapp-messages-to-bring-back-customers/">seven free WhatsApp templates</a>.</li>
</ol>
{cta(title="Get the Shopify app first", text="Early access stores connect first. Tell us your store and we'll message you on WhatsApp when it's ready.")}
''',
    faqs=[
        ("When will the Shopify app be ready?", "Early access stores get it first. Join the list and we'll message you on WhatsApp when your store can connect."),
        ("Will it work with my Shopify loyalty or email app?", "Yes. Loyalbase doesn't change your theme, checkout or emails, so it runs alongside Smile.io, LoyaltyLion, Yotpo or Klaviyo."),
        ("How much will it cost?", "The same flat price as WooCommerce, from $50 a month. The price doesn't rise as your orders grow."),
    ],
    related=["/guides/how-to-find-customers-who-stopped-buying/", "/whatsapp-messages-to-bring-back-customers/", "/compare/"],
    schema="product",
))

# ---------------------------------------------------------------- WhatsApp templates
TPLS = [
    ("Late regular", "#FDF3E3", "#8A520E", "The customer who has gone quiet",
     "a customer with two or more orders has gone clearly longer than their usual gap. For example, someone who orders every three weeks and hasn't ordered in six.",
     "Hi [Name], it's been a little while! We'd love to have you back. Anything we can get ready for you this week?\n[Shop name]",
     "No discount and no guilt. It reminds them you exist and gives them an easy yes."),
    ("Yearly occasion", "#E8F1FC", "#1F4F8F", "The birthday or anniversary they order for every year",
     "about two weeks before the date they ordered for last year.",
     "Hi [Name]! Your yearly [birthday] order is coming up on [date]. Shall we get something ready for you?\n[Shop name]",
     "You solve a problem before they remember they have it. It works best for flowers, cakes and gifts. If you know who the order is for, try: \"[Recipient]'s birthday is coming up on [date]. Would you like us to get something ready again this year?\""),
    ("Unpaid checkout", "#F1EAFB", "#5B2D91", "The checkout that stopped at payment",
     "within a day or two of a checkout that didn't get paid.",
     "Hi [Name], we noticed your order didn't go through. Can we help you finish it, or would you like to pay another way?\n[Shop name]",
     "Many unpaid checkouts are failed cards or payment worries, not lost interest. Offering another way to pay, like bank transfer or cash on delivery, removes the blocker."),
    ("First time buyer", "#E6F4ED", "#17704A", "The customer who bought once",
     "45 to 150 days after their first order, if they haven't ordered again.",
     "Hi [Name], thank you again for your first order with [Shop name]! We hope you loved it. Anything we can get for you next?",
     "The second order is where a buyer becomes a customer. A thank you with an open question feels like service, not marketing."),
    ("Stopped ordering", "#FBEAEA", "#9E2A2A", "The past regular you haven't seen in a year",
     "when someone with two or more past orders hasn't bought in over a year.",
     "Hi [Name], we've missed you at [Shop name]! A lot has changed since your last order. Can we tempt you this week?",
     "It's honest about the gap, and \"a lot has changed\" gives them a reason to look. If you have a new product, name it."),
    ("Best customer", "#E3E8EE", "#0F2A4A", "Your favourite customers",
     "any time, and especially before a busy season.",
     "Hi [Name], thank you for being one of our favourite customers. It means a lot to us.\n[Shop name]",
     "There's no ask. Your best customers are the ones most likely to recommend you, and a thank you keeps them close."),
    ("Corporate buyer", "#E3F3F4", "#0E5E66", "The person who orders for their office",
     "a few weeks before office events, year end and festive seasons.",
     "Hi [Name], thank you for the orders for your team! Planning anything for the office soon? We can put together a box for any size.\n[Shop name]",
     "One office order can be worth many personal ones. A reminder before the season puts you first in line."),
]
PAGES.append(dict(
    path="/whatsapp-messages-to-bring-back-customers/",
    section="guides",
    title="7 WhatsApp Messages to Bring Back Customers (Free Templates)",
    nav="WhatsApp templates",
    description="Copy 7 WhatsApp templates to win back customers: late regulars, first time buyers, unpaid checkouts, yearly occasions and more, with when to send each.",
    eyebrow="Free templates",
    h1="7 WhatsApp messages that bring customers back",
    stand="Short, personal and sent at the right moment. Copy them, change the words to sound like you, and send from your shop's own WhatsApp.",
    answer="The best WhatsApp message to bring a customer back is short, personal and sent at the right moment: when a regular is later than usual, two weeks before a yearly occasion, 45 to 150 days after a first order, or a day or two after an unpaid checkout. Use their first name, sign with your shop's name, ask one easy question, and leave discounts for later.",
    body="\n".join(tpl(*t) for t in TPLS) + f'''
<h2>Seven rules for win back messages that don't annoy people</h2>
<ol>
<li><b>Only message people who said yes.</b> Meta requires businesses to get permission before messaging people on WhatsApp, and the permission has to name your business. A tick box at checkout is the simplest way to get it.</li>
<li><b>Space them out.</b> One message per person every two weeks at most is a good rule.</li>
<li><b>Send in the day.</b> Never late at night or early in the morning.</li>
<li><b>Use their name and your shop's name.</b> A message that could have come from anyone gets ignored.</li>
<li><b>Ask one easy question.</b> "Anything we can get ready for you this week?" is easier to answer than a link to your catalogue.</li>
<li><b>Lead without a discount.</b> Save offers for people who don't reply, so you don't teach customers to wait for a code.</li>
<li><b>Always honour stop.</b> If someone asks you to stop, stop, and note it so nobody on your team messages them again.</li>
</ol>

<h2>Send one by one, or in bulk?</h2>
<p>For a handful of people a day, send from the WhatsApp Business app on your phone. It's personal and free.</p>
<p>For bigger lists, use Meta's WhatsApp Business Platform. Marketing messages there use templates that Meta approves first, and they're charged per message.</p>
<p>Loyalbase does both. Tap a customer and WhatsApp opens with the message written, or download a whole list as a campaign file for Meta's messaging campaigns. Only people who said yes are included.</p>

<h2>How to tell if it worked</h2>
<p>Write down who you messaged and when, then check who ordered in the next 60 days. Better still, keep a few people aside and don't message them, then compare. Our guide on <a href="/guides/how-to-prove-your-messages-worked/">proving your messages worked</a> shows how. Loyalbase does it for you automatically.</p>
{cta(title="Know exactly who to send these to", text="Loyalbase picks the right people each morning, fills in their name and occasion, and tracks what came back.")}
''',
    faqs=[
        ("Is it OK to message customers on WhatsApp?", "Yes, if they gave you their number and agreed to hear from your business. Meta requires this permission for business messages, and data protection laws in many countries apply too. If someone asks you to stop, stop."),
        ("What's the best time to send?", "Send during daytime hours when your customers would normally shop, and never late at night. Try two different times for a few weeks and keep the one that gets more replies."),
        ("Should I offer a discount to bring customers back?", "Not in the first message. A personal check in works for many customers on its own. Keep a small offer for people who don't reply, so discounts don't become the reason anyone orders."),
        ("How many customers should I message a day?", "Only as many as you can reply to properly. A fast, friendly reply is part of what brings them back."),
    ],
    related=["/guides/how-to-find-customers-who-stopped-buying/", "/guides/how-to-prove-your-messages-worked/", "/woocommerce-customer-retention/"],
    sources=[SRC_META_OPTIN],
    schema="article",
    has_copy=True,
))

# ---------------------------------------------------------------- Guide: find customers who stopped buying
PAGES.append(dict(
    path="/guides/how-to-find-customers-who-stopped-buying/",
    section="guides",
    title="How to Find Customers Who Stopped Buying From Your Store",
    nav="Find customers who stopped buying",
    description="A simple method to spot customers who stopped buying, using each person's own buying rhythm. Includes a spreadsheet version you can do today.",
    eyebrow="Guide",
    h1="How to find customers who stopped buying from your store",
    stand="One fixed rule like \"no order in 90 days\" gets it wrong for most customers. Here's the method that works, by hand or automatically.",
    answer="Work out each customer's usual time between orders, then flag anyone who has gone clearly longer than that. Someone who orders every three weeks and hasn't ordered in six is slipping. Someone who orders twice a year isn't. Also check first time buyers 45 to 150 days after their first order, and anyone who orders around the same date every year.",
    body=f'''
<h2>Why one cut off date doesn't work</h2>
<p>A coffee customer who orders every three weeks is long gone after 90 days. A customer who buys a gift twice a year is perfectly normal at 90 days. One number for everyone flags the wrong people and misses the right ones.</p>
<p>The fix is to judge each customer against their own rhythm.</p>

<h2>The four groups worth checking every week</h2>
{table(["Group", "Who", "Why it matters"], [
    ["Late regulars", "Two or more orders, now clearly past their usual gap", "Still warm, and the easiest to win back"],
    ["First time buyers", "One order, placed 45 to 150 days ago", "The second order is where loyalty starts"],
    ["Yearly occasions", "Ordered around the same date in two or more different years", "You can remind them before they shop elsewhere"],
    ["Past regulars", "Two or more orders, nothing in over a year", "Worth one honest message"],
])}

<h2>How Loyalbase decides someone is late</h2>
<p>For each customer with at least two orders, Loyalbase takes the median gap between their orders. That's the middle value, so one odd gap doesn't skew it. A customer counts as late when the days since their last order are more than the largest of these three numbers:</p>
<ul>
<li>one and a half times their usual gap</li>
<li>their usual gap plus 21 days</li>
<li>45 days</li>
</ul>
{table(["Usual gap between orders", "Flagged as late after"], [
    ["3 weeks (21 days)", "45 days, about 6 weeks"],
    ["1 month (30 days)", "51 days"],
    ["2 months (60 days)", "90 days"],
    ["6 months (182 days)", "273 days, about 9 months"],
])}
<p>Yearly occasions are found when the same person orders within ten days of the same date in different years. Big public gifting dates such as Valentine's Day, Mother's Day and Christmas are left out, so everyone who orders for Christmas isn't treated as having a personal occasion.</p>
<p>Loyalbase also matches the same person across orders by phone or email, and ignores numbers shared by four or more different customers, like an office line.</p>

<h2>Do it yourself in a spreadsheet</h2>
<ol class="sx-steps">
<li><b>Export your orders.</b> In WooCommerce, go to Analytics, then Orders, then Download. In Shopify admin, export orders as a CSV file. Keep the customer email or phone, the order date and the order total.</li>
<li><b>Sort by customer, then by date.</b></li>
<li><b>For each customer, count their orders</b> and note their last order date.</li>
<li><b>Work out their usual gap.</b> For customers with two or more orders, find the days between each pair of orders and take the middle value.</li>
<li><b>Work out days since their last order:</b> today minus the last order date.</li>
<li><b>Flag them as late</b> if days since their last order is more than all three: 1.5 times their usual gap, their usual gap plus 21, and 45.</li>
<li><b>Filter first time buyers</b> separately: one order, placed 45 to 150 days ago.</li>
</ol>
<p class="sx-note">Expect this to take an hour or two the first time, and to be out of date a week later.</p>

<h2>Or let Loyalbase do it every morning</h2>
<p>Loyalbase runs this for every customer each night, adds yearly occasions, unpaid checkouts and best customers, and gives you a WhatsApp message for each person. Then it tracks who came back.</p>
{cta()}
''',
    faqs=[
        ("How long before a customer counts as lost?", "In Loyalbase, a customer with no order in more than 12 months counts as not seen in a year. Those with two or more past orders also go on the stopped ordering list, because they're worth one honest message."),
        ("What is a good repeat purchase rate?", "It depends heavily on what you sell. Stores selling things people run out of, like coffee, pet food or skincare, see far more repeat orders than stores selling furniture. Compare yourself with your own numbers from last year rather than a general benchmark."),
        ("What should I send to customers who stopped buying?", "A short, personal message with their first name and your shop's name, and one easy question. Our seven free WhatsApp templates cover each group."),
    ],
    related=["/whatsapp-messages-to-bring-back-customers/", "/guides/how-to-prove-your-messages-worked/", "/guides/loyalty-program-vs-win-back-messages/"],
    schema="article",
))

# ---------------------------------------------------------------- Guide: loyalty program vs win back
PAGES.append(dict(
    path="/guides/loyalty-program-vs-win-back-messages/",
    section="guides",
    title="Loyalty Program vs Win Back Messages: What Small Stores Need",
    nav="Loyalty program or win back messages",
    description="Points programs reward customers who already come back. Win back messages reach the ones who stopped. Costs, pros and cons, and when to use each.",
    eyebrow="Guide",
    h1="Do you need a loyalty program, or win back messages?",
    stand="Both aim for repeat customers. They reach different people, cost different amounts, and are measured differently.",
    answer="A points program rewards customers who already come back. Win back messages reach the ones who stopped. For most small stores, win back messages are the better first step: they cost a message instead of a discount, they work on the customers you're actually losing, and you can see which ones brought sales back. Add a points program later if your regulars want rewards.",
    body=f'''
<h2>What a points program does well</h2>
<ul>
<li>Gives regulars a reason to keep choosing you over a competitor.</li>
<li>Tiers make your best customers feel recognised.</li>
<li>Gives new visitors a reason to create an account.</li>
</ul>

<h2>What a points program costs</h2>
<p>Three costs, not one: the app fee, the rewards you fund, and the time to set it up and keep it running. Most loyalty apps also charge more as your order volume grows.</p>
{table(["App", "Free plan", "Paid plans from"], [
    ["Smile.io", "Up to 200 orders a month", "$79 a month for 1,000 orders"],
    ["LoyaltyLion", "About 400 orders a month", "$199 a month"],
    ["Yotpo Loyalty", "Basic points and referrals", "$199 a month for the first 500 orders"],
])}
<p class="sx-note">Public pricing, checked October 2026. Sources at the bottom of this page.</p>

<h2>What a points program misses</h2>
<p>A customer who has stopped buying doesn't visit your store, so they never see their points balance. Points are a reason to come back for people who are already coming back.</p>

<h2>What win back messages do</h2>
<ul>
<li>Go straight to the person, on WhatsApp, from your shop.</li>
<li>Arrive when it matters: when that customer is later than their usual rhythm, or before their yearly occasion.</li>
<li>Need no discount to work for many customers.</li>
<li>Can be measured: who ordered after a message, compared with people who weren't messaged.</li>
</ul>

<h2>Side by side</h2>
{table(["", "Points program", "Win back messages"], [
    ["Who it reaches", "Customers who visit your store", "Customers who stopped visiting"],
    ["What it costs", "App fee plus the rewards you give", "A message"],
    ["Setup", "Rules, rewards, a widget, emails", "A list and a phone"],
    ["How you measure it", "Points earned and redeemed", "Orders after a message, against a held back group"],
    ["Best for", "Stores with many frequent buyers", "Stores losing customers after the first or second order"],
])}

<h2>Which should you start with?</h2>
<h3>Start with win back messages if</h3>
<ul><li>most of your customers buy once or twice</li><li>you sell things people reorder</li><li>you don't want to fund ongoing discounts</li></ul>
<h3>Add a points program if</h3>
<ul><li>you have many frequent buyers who ask for rewards</li><li>your margins can carry ongoing discounts</li></ul>
<h3>Use both if</h3>
<ul><li>you want to reward your regulars and win back the ones drifting away. They don't conflict.</li></ul>
{cta()}
''',
    faqs=[
        ("Can I use a loyalty program and Loyalbase together?", "Yes. Loyalbase doesn't add a widget or change your checkout, so it runs alongside any points app."),
        ("Are loyalty programs worth it for small stores?", "They can be, if you have enough frequent buyers to make points feel valuable and the margin to fund rewards. If most customers buy once or twice, start by bringing those customers back."),
        ("Do win back messages need a discount?", "Not usually in the first message. A personal check in at the right moment works for many customers. Keep an offer for people who don't reply."),
    ],
    related=["/compare/", "/whatsapp-messages-to-bring-back-customers/", "/guides/how-to-find-customers-who-stopped-buying/"],
    sources=[SRC_SMILE_PRICE, SRC_LL_PRICE, SRC_YOTPO],
    schema="article",
))

# ---------------------------------------------------------------- Guide: prove it worked
PAGES.append(dict(
    path="/guides/how-to-prove-your-messages-worked/",
    section="guides",
    title="How to Prove Your Win Back Messages Worked (Held Back Groups)",
    nav="Prove your messages worked",
    description="Some customers would have ordered anyway. A held back group shows how many extra orders your messages really added. Simple explanation with a worked example.",
    eyebrow="Guide",
    h1="How to tell if your messages really brought customers back",
    stand="\"She ordered after my message\" isn't proof. Some customers would have ordered anyway. Here's the simple way to know the difference.",
    answer="Keep a random 1 in 10 of the people you planned to message aside, and don't message them. After 60 days, compare how many in each group ordered. The gap between the two groups is what your messages added. The rest would have ordered anyway.",
    body=f'''
<h2>Why "they ordered after my message" isn't proof</h2>
<p>If you message 90 customers and 26 order, it's tempting to credit the message with 26 orders. But some of them were going to order that week anyway. Without a comparison, you can't tell how many.</p>

<h2>What a held back group is</h2>
<p>Before you send, set aside a random few people from the same list and don't message them. Same type of customer, same timing, one difference: no message. Whatever they do is what would have happened anyway.</p>

<h2>A worked example</h2>
<p>100 customers are on your late regulars list. You message 90 and hold back 10. After 60 days:</p>
{table(["", "Messaged", "Held back"], [
    ["People", "90", "10"],
    ["Ordered within 60 days", "26", "1"],
    ["Came back rate", "29%", "10%"],
])}
<p>Without a message, about 10% would have ordered anyway. That's about 9 of the 90 you messaged. So your messages added about <b>17 extra orders</b> (26 minus 9). If your average order is $60, that's about $1,020 in sales you wouldn't have had.</p>

<h2>How Loyalbase counts a customer who came back</h2>
<ul>
<li>A message counts when the customer pays for an order within 60 days of it.</li>
<li>Each order is credited once, to the earliest message before it, so messaging someone three times never counts as three wins.</li>
<li>Messages less than 14 days old are left out of the came back rate, because those customers haven't had time to order yet.</li>
<li>1 in 10 people on the yearly occasion, late regular, first time buyer and stopped ordering lists are held back at random. You can switch this off in settings.</li>
</ul>

<h2>Rules for a fair test</h2>
<ol>
<li><b>Choose who to hold back at random.</b> Not your favourite customers, not the hardest cases.</li>
<li><b>Hold back from the same list.</b> Compare late regulars with late regulars.</li>
<li><b>Don't contact the held back group another way.</b> A promo email to them spoils the comparison.</li>
<li><b>Read results over months, not days.</b> Small groups swing a lot.</li>
</ol>
{cta(title="Get this calculated for you", text="Loyalbase holds people back, matches every message to paid orders, and tells you in plain words how many extra orders your messages added.")}
''',
    faqs=[
        ("Don't I lose sales by holding people back?", "Possibly a few orders from 1 in 10 people. In exchange, you learn which messages are worth sending. In Loyalbase you can switch it off at any time."),
        ("How many customers do I need for this to work?", "Small lists swing a lot. With 10 people held back, one order moves their rate by 10 points. Read the results over two or three months."),
        ("Is this the same as an A/B test?", "It's close. An A/B test compares two versions of a message. A held back group compares sending a message with sending nothing."),
    ],
    related=["/whatsapp-messages-to-bring-back-customers/", "/guides/how-to-find-customers-who-stopped-buying/", "/woocommerce-customer-retention/"],
    schema="article",
))

# ---------------------------------------------------------------- Compare hub
COMPARE_ROWS = [
    ["Built for", "Bringing customers back", "Points and rewards", "Points and tiers", "Points and referrals", "Email and SMS"],
    ["WooCommerce", "Yes", "No", "Through a separate connector", "Yes", "Yes"],
    ["Shopify", "Early access", "Yes", "Yes", "Yes", "Yes"],
    ["Tells you who to message today", "Every morning, with reasons", "No", "No", "Segments on Premium", "You build the flows"],
    ["WhatsApp", "One tap, message written", "Through other apps", "Through other apps", "Through other apps", "Built in since 2025"],
    ["Proves what messages added", "Held back group", "No", "No", "No", "A/B tests"],
    ["Ads and posts next to real sales", "Meta and Google Analytics", "No", "No", "No", "Mainly its own channels"],
    ["No discounts to fund", "Yes", "No", "No", "No", "Yes"],
    ["Customer contact details", "Stay on your store", "Stored on their platform", "Stored on their platform", "Stored on their platform", "Stored on their platform"],
    ["Paid plans from", "$50 a month, flat", "$79 a month, rises with orders", "$199 a month, rises with orders", "$199 a month, rises with orders", "$20 a month, rises with contacts"],
]
PAGES.append(dict(
    path="/compare/",
    section="compare",
    title="Loyalbase vs Smile.io, LoyaltyLion, Yotpo and Klaviyo",
    nav="All comparisons",
    description="How Loyalbase compares with loyalty apps and email tools for WooCommerce and Shopify stores: what each is for, platforms, WhatsApp, proof and pricing.",
    eyebrow="Compare",
    h1="How Loyalbase compares",
    stand="Points apps reward people who keep showing up. Email tools send what you build. Loyalbase finds the customers who stopped, and proves what came back.",
    answer="Smile.io, LoyaltyLion and Yotpo are points and rewards programs. Klaviyo is an email and SMS platform. Loyalbase is different: it tells you which customers to bring back each day, gives you a WhatsApp message for each, and proves what came back with a held back group. It works alongside all of them.",
    body=table(["", "Loyalbase", "Smile.io", "LoyaltyLion", "Yotpo Loyalty", "Klaviyo"], COMPARE_ROWS, us_col=1) + '''
<p class="sx-note">Competitor details from their public pricing and help pages and independent reviews, checked October 2026. Plans change often, so check before you decide.</p>
<h2>Detailed comparisons</h2>
<div class="sx-hub">
<a href="/compare/smile-io-alternative-for-woocommerce/"><span>Compare</span><b>Smile.io alternative for WooCommerce</b><p>Smile.io doesn't support WooCommerce. Your options, and how Loyalbase differs.</p></a>
<a href="/compare/loyalbase-vs-klaviyo/"><span>Compare</span><b>Loyalbase vs Klaviyo</b><p>An email platform you build in, or a daily list of who to bring back. Or both.</p></a>
<a href="/guides/loyalty-program-vs-win-back-messages/"><span>Guide</span><b>Loyalty program or win back messages?</b><p>What each costs, who each reaches, and which to start with.</p></a>
</div>
''' + cta(),
    faqs=[
        ("Is Loyalbase a loyalty program?", "No. There are no points, tiers or rewards. Loyalbase tells you which customers to bring back and why, writes the message, and proves what came back."),
        ("Can I use Loyalbase with Smile.io or Klaviyo?", "Yes. Loyalbase doesn't change your store's checkout, theme or emails, so it runs alongside loyalty and email tools."),
    ],
    related=["/compare/smile-io-alternative-for-woocommerce/", "/compare/loyalbase-vs-klaviyo/", "/guides/loyalty-program-vs-win-back-messages/"],
    sources=[SRC_SMILE_PLATFORMS, SRC_SMILE_PRICE, SRC_LL_PRICE, SRC_LL_WOO, SRC_YOTPO, SRC_KLAVIYO_PRICE, SRC_KLAVIYO_WA],
    schema="collection",
))

# ---------------------------------------------------------------- Smile alternative
PAGES.append(dict(
    path="/compare/smile-io-alternative-for-woocommerce/",
    section="compare",
    title="Smile.io Alternative for WooCommerce Stores | Loyalbase",
    nav="Smile.io alternative",
    description="Smile.io doesn't support WooCommerce. Here are the options for WooCommerce stores that want repeat customers, and how Loyalbase compares.",
    eyebrow="Compare",
    h1="Smile.io doesn't work with WooCommerce. Here are your options.",
    stand="If you run a WooCommerce store and wanted Smile.io, you'll need something else. Which option fits depends on what you're really after: points, or customers ordering again.",
    answer="Smile.io supports Shopify, Shopify Plus, Shopify POS and BigCommerce, and its help centre says it doesn't integrate with WordPress, so WooCommerce stores can't use it. If you want points, use a WooCommerce loyalty plugin or a platform such as Yotpo that supports WooCommerce. If what you want is customers ordering again, Loyalbase finds the ones who stopped and gives you a WhatsApp message for each.",
    body=f'''
<h2>Your options on WooCommerce</h2>
{table(["Option", "What it is", "Good for"], [
    ["A WooCommerce points plugin, such as WooCommerce Points and Rewards or WPLoyalty", "Points and rewards inside your store", "A classic points program on a small budget"],
    ["Yotpo Loyalty", "A loyalty and referrals platform that supports WooCommerce", "Bigger stores, with paid plans from $199 a month"],
    ["Loyalbase", "Finds customers who stopped buying, writes a WhatsApp message for each, and proves what came back", "Getting customers to order again without funding rewards"],
])}

<h2>Smile.io vs Loyalbase</h2>
{table(["", "Smile.io", "Loyalbase"], [
    ["What it is", "Points and rewards program", "Tells you who to bring back, and how"],
    ["Platforms", "Shopify, Shopify Plus, Shopify POS, BigCommerce", "WooCommerce now, Shopify in early access"],
    ["Who it reaches", "Customers who visit your store", "Customers who stopped visiting"],
    ["What you fund", "The rewards customers redeem", "Nothing beyond the subscription"],
    ["WhatsApp", "Through other apps", "One tap, message written"],
    ["Proof", "Program reports", "Held back group shows what messages added"],
    ["Price", "Free up to 200 orders a month, then $79 a month for 1,000 orders, $199 for 2,500", "$50 a month, flat"],
], us_col=2)}

<h2>When Smile.io is the better choice</h2>
<p>If you're on Shopify or BigCommerce and want a polished points and referral program, Smile.io is a well known option. Many stores run a points program and Loyalbase side by side: points for regulars, messages for the customers drifting away.</p>
{cta()}
''',
    faqs=[
        ("Does Smile.io work with WordPress or WooCommerce?", "No. Smile.io's help centre lists Shopify, Shopify Plus, Shopify POS and BigCommerce as supported platforms and says it doesn't integrate with WordPress."),
        ("Can I use a points plugin and Loyalbase together?", "Yes. Loyalbase doesn't change your checkout or add a widget, so it runs alongside any WooCommerce points plugin."),
        ("Is Loyalbase a loyalty program?", "No. There are no points or rewards. It finds customers who stopped buying, gives you a message for each, and shows the sales that came back."),
    ],
    related=["/woocommerce-customer-retention/", "/guides/loyalty-program-vs-win-back-messages/", "/compare/"],
    sources=[SRC_SMILE_PLATFORMS, SRC_SMILE_PRICE, SRC_YOTPO],
    schema="article",
))

# ---------------------------------------------------------------- Klaviyo
PAGES.append(dict(
    path="/compare/loyalbase-vs-klaviyo/",
    section="compare",
    title="Loyalbase vs Klaviyo: Which Does a Small Store Need?",
    nav="Loyalbase vs Klaviyo",
    description="Klaviyo is an email and SMS platform you build flows in. Loyalbase tells you who to bring back each day and proves what came back. How they differ.",
    eyebrow="Compare",
    h1="Loyalbase vs Klaviyo",
    stand="They overlap less than you'd think. One is a full email platform. The other is a daily list of who to bring back, and proof of what came back.",
    answer="Klaviyo is a full email and SMS marketing platform: you build lists, flows and campaigns yourself, and the price rises with your contacts. Loyalbase is narrower: each morning it tells you which customers to bring back and why, gives you a WhatsApp message for each, and proves what came back against a held back group. Many stores use Klaviyo for newsletters and Loyalbase for personal win backs.",
    body=f'''
<h2>Side by side</h2>
{table(["", "Klaviyo", "Loyalbase"], [
    ["Built for", "Email and SMS marketing at any scale", "Getting customers to order again"],
    ["Main channel", "Email and SMS, with WhatsApp since 2025", "WhatsApp, with lists you can send to email"],
    ["Who decides who to contact", "You build segments and flows", "Loyalbase picks people each morning, with reasons"],
    ["Setup", "Flows, templates, segments", "Install a plugin, open Today"],
    ["Proof", "Revenue reports and A/B tests", "Held back group shows what messages added"],
    ["Ads next to real sales", "Not its focus", "Meta ads and Google Analytics beside your store's sales"],
    ["Customer contact details", "Stored on Klaviyo", "Stay on your store"],
    ["Price", "Free up to 250 profiles, $20 a month for 500 contacts, $60 for 2,500, $150 for 10,000", "$50 a month, flat"],
], us_col=2)}

<h2>Choose Klaviyo if</h2>
<ul><li>email is your main channel and your list is large</li><li>you want newsletters and automated abandoned cart emails</li><li>you have someone with time to build and maintain flows</li></ul>
<h2>Choose Loyalbase if</h2>
<ul><li>your customers answer WhatsApp faster than email</li><li>you don't have time to build segments and flows</li><li>you want a short list each day and proof of what it brought back</li></ul>
<h2>Using both</h2>
<p>Keep Klaviyo for newsletters and store emails. Use Loyalbase to find the people worth a personal message. You can download any Loyalbase list as a spreadsheet and import it into your email tool, or send it straight to Sendy.</p>
{cta()}
''',
    faqs=[
        ("Does Loyalbase send emails?", "Not by itself. You can send any list to your own Sendy email list, or download it as a spreadsheet for your email tool."),
        ("Is Loyalbase cheaper than Klaviyo?", "It depends on your list size. Klaviyo is free for very small lists and its price rises with your contacts. Loyalbase is $50 a month, flat, however many customers you have."),
        ("Does Klaviyo support WhatsApp?", "Yes. Klaviyo announced WhatsApp in September 2025. You still build the flows and decide who to message yourself."),
    ],
    related=["/compare/", "/whatsapp-messages-to-bring-back-customers/", "/guides/how-to-prove-your-messages-worked/"],
    sources=[SRC_KLAVIYO_PRICE, SRC_KLAVIYO_WA, SRC_KLAVIYO_ADDON],
    schema="article",
))

# ---------------------------------------------------------------- Guides hub
PAGES.append(dict(
    path="/guides/",
    section="guides",
    title="Guides for Store Owners: Repeat Customers and Win Backs | Loyalbase",
    nav="All guides",
    description="Plain English guides for WooCommerce and Shopify store owners: find customers who stopped buying, WhatsApp templates, loyalty programs and proving what worked.",
    eyebrow="Guides",
    h1="Guides for store owners",
    stand="Plain English, no jargon. How to find the customers you're losing, what to send them, and how to know it worked.",
    answer=None,
    body='''
<div class="sx-hub">
<a href="/guides/how-to-find-customers-who-stopped-buying/"><span>Guide</span><b>How to find customers who stopped buying</b><p>The method that judges each customer against their own rhythm, plus a spreadsheet version.</p></a>
<a href="/whatsapp-messages-to-bring-back-customers/"><span>Templates</span><b>7 WhatsApp messages that bring customers back</b><p>Copy and send. When to send each one, and why it works.</p></a>
<a href="/guides/how-to-prove-your-messages-worked/"><span>Guide</span><b>How to prove your messages worked</b><p>Held back groups explained, with a worked example.</p></a>
<a href="/guides/loyalty-program-vs-win-back-messages/"><span>Guide</span><b>Loyalty program or win back messages?</b><p>What each costs, who each reaches, and which to start with.</p></a>
<a href="/guides/festival-customers/"><span>Guide</span><b>How to find customers who order for the same festival every year</b><p>Eid, Avurudu, Christmas and Deepavali regulars, and when to message them.</p></a>
<a href="/ask-loyalbase/"><span>Product</span><b>Ask your store questions in plain words</b><p>Every ready-made question, and what stays private.</p></a>
<a href="/industries/"><span>Industries</span><b>Built for how your store sells</b><p>Bakeries, gifts, grocery, beauty, fashion, pet, restaurants and more.</p></a>
<a href="/woocommerce-customer-retention/"><span>WooCommerce</span><b>Customer retention for WooCommerce</b><p>What Loyalbase finds in your WooCommerce orders, and how to set it up.</p></a>
<a href="/compare/"><span>Compare</span><b>Loyalbase vs loyalty and email apps</b><p>Smile.io, LoyaltyLion, Yotpo and Klaviyo, side by side.</p></a>
</div>
''',
    faqs=[],
    related=[],
    schema="collection",
))

# ---------------------------------------------------------------- About
PAGES.append(dict(
    path="/about/",
    section="company",
    title="About Loyalbase",
    nav="About",
    description="Loyalbase is a customer retention app for WooCommerce and Shopify stores, built in Colombo by Digisavvy. Who we are and what we believe.",
    eyebrow="About",
    h1="About Loyalbase",
    stand="We help store owners get customers to order again, without a loyalty program, and prove what came back.",
    answer="Loyalbase is a customer retention app for WooCommerce and Shopify stores, built in Colombo, Sri Lanka, by Digisavvy, a performance marketing team. It reads a store's orders, tells the owner who to message each day and why, and shows the sales that came back.",
    body='''
<h2>How it started</h2>
<p>Loyalbase began as a customer dashboard we built for a cake and gifting store in Sri Lanka. The owner wanted to know which regulars had gone quiet and who to remind before birthdays and anniversaries. We turned it into a product any WooCommerce or Shopify store can use.</p>

<h2>What we believe</h2>
<ul>
<li><b>Customer data belongs to the store.</b> Names, phone numbers, emails and addresses stay on your website. Loyalbase works from order facts and scrambled IDs.</li>
<li><b>Plain words beat dashboards.</b> "Late for their next order" instead of "at risk segment". One clear thing to do on every screen.</li>
<li><b>Proof beats vanity numbers.</b> We count the orders your messages added, against a held back group, not messages sent or opened.</li>
<li><b>WhatsApp first.</b> In many markets, customers answer WhatsApp long before they open an email.</li>
</ul>

<h2>Who we are</h2>
<p>Loyalbase is built by <b>Digisavvy</b>, a performance marketing team in Colombo, and founded by <a href="https://www.linkedin.com/in/akmal-afzal24" rel="noopener">Akmal Afzal</a>.</p>

<h2>Where we're going</h2>
<p>Next up: the Shopify app, automatic WhatsApp reminders you approve before they send, and walk in sales from POS systems at your outlets. Our first markets are Sri Lanka, India, Pakistan, Bangladesh, the UAE and the Gulf, and stores anywhere can join.</p>
<p>We're raising our first round. If you know ecommerce in South Asia or the Gulf, <a href="/#invest">talk to us</a>.</p>

<h2>Contact</h2>
<ul>
<li>WhatsApp: <a href="https://wa.me/94770274519">+94 77 027 4519</a></li>
<li>Email: <a href="mailto:akmal@digisavvyteam.com">akmal@digisavvyteam.com</a></li>
</ul>
''' + cta(),
    faqs=[],
    related=["/woocommerce-customer-retention/", "/guides/", "/privacy/"],
    schema="about",
))

# ---------------------------------------------------------------- Privacy
PAGES.append(dict(
    path="/privacy/",
    section="company",
    title="Privacy | Loyalbase",
    nav="Privacy",
    description="How the Loyalbase website and app handle personal data. Customer names, phone numbers, emails and addresses stay on your store.",
    eyebrow="Privacy",
    h1="Privacy",
    stand="Two parts: what this website collects about you, and how the Loyalbase app handles your customers' data.",
    answer="This website uses Google Analytics to count visits and Formspree to receive the early access form. We don't sell personal data. The Loyalbase app never stores your customers' names, phone numbers, emails or addresses: those stay on your store, and Loyalbase works from order facts and scrambled IDs.",
    body='''
<h2 id="website">This website</h2>
<h3>Analytics</h3>
<p>We use Google Analytics to understand which pages are useful. It uses cookies and records things like pages viewed, device type and approximate location. You can block it with your browser settings or the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Google Analytics opt out add on</a>.</p>
<h3>Early access form</h3>
<p>When you fill in the early access form, we receive your email, store website and WhatsApp number through Formspree, which delivers it to our inbox. We use it only to contact you about Loyalbase.</p>
<h3>WhatsApp links</h3>
<p>Tapping a WhatsApp button opens WhatsApp, which is run by Meta. If you message us, we see your number and messages like any WhatsApp chat.</p>
<h3>Hosting and fonts</h3>
<p>This site is hosted on GitHub Pages and loads fonts from Google Fonts. Like any web host, they may receive your IP address when you visit.</p>
<h3>How long we keep it, and your choices</h3>
<p>We keep early access details for as long as we're in touch about Loyalbase, and delete them when you ask. You can ask to see, correct or delete anything we hold about you by emailing <a href="mailto:akmal@digisavvyteam.com">akmal@digisavvyteam.com</a>. We don't sell personal data.</p>

<h2 id="app">The Loyalbase app and your store's data</h2>
<ul>
<li><b>What Loyalbase stores:</b> order facts such as dates, totals, products and delivery area, an occasion label such as "birthday", consent flags, and scrambled versions of phone numbers and emails.</li>
<li><b>What it never stores:</b> customer names, phone numbers, emails, street addresses, or cake and card wording.</li>
<li><b>Scrambled IDs can't be reversed.</b> The key used to scramble them is created on your website and never sent to Loyalbase.</li>
<li><b>Names stay on your store.</b> When you open a customer, your browser fetches the name straight from your store using a pass that expires in five minutes. Names are never sent to Loyalbase or saved in your browser.</li>
<li><b>Every lookup is logged</b> on your own store, so you can see each time a name was shown.</li>
<li><b>Anything that looks like contact details is refused.</b> The Loyalbase servers reject data containing fields they don't expect.</li>
<li><b>You can delete your store</b> from Loyalbase at any time with Delete this shop in settings.</li>
</ul>

<h2>Who we are</h2>
<p>Loyalbase is a product of Digisavvy, Colombo, Sri Lanka. Questions about privacy: <a href="mailto:akmal@digisavvyteam.com">akmal@digisavvyteam.com</a>.</p>
''',
    faqs=[],
    related=[],
    schema="webpage",
))
