"""Industry pages, the industries hub, the Ask Loyalbase page and the festival guide.

Every claim here matches the product as shipped (Nov 2026): WooCommerce live, Shopify in early access,
POS not yet. Example answers use made-up names and numbers and say so on the page.
"""
from content import table, tpl, cta

PAGES = []

TAG = {
    "late": ("Late regular", "#FDF3E3", "#8A520E"),
    "occasion": ("Yearly occasion", "#E8F1FC", "#1F4F8F"),
    "first": ("First time buyer", "#E6F4ED", "#17704A"),
    "stopped": ("Stopped ordering", "#F7E8E8", "#8F2D2D"),
    "best": ("Best customer", "#FFF4D6", "#7A5A00"),
    "corp": ("Corporate buyer", "#EDEBFA", "#4A3A9A"),
    "unpaid": ("Unpaid checkout", "#F1EAFB", "#5B2D91"),
    "festival": ("Festival buyer", "#FCEBF3", "#8C2A5B"),
}


# ------------------------------------------------------------------ building blocks
def rhythm(dots, late=None, labels=(), caption="", aria="", mark="Late"):
    """An example customer's orders on a line. dots/late are percentages along the line."""
    d = "".join(f'<span class="sx-rh-dot" style="left: {x}%; animation-delay: {i * 90}ms"></span>' for i, x in enumerate(dots))
    lt = f'<span class="sx-rh-late" style="left: {late}%"><span>{mark}</span></span>' if late is not None else ""
    lb = "".join(f"<span>{t}</span>" for t in labels)
    return f'''<figure class="sx-rhythm">
<div class="sx-rh-track" role="img" aria-label="{aria}">{d}{lt}</div>
<div class="sx-rh-labels" aria-hidden="true">{lb}</div>
<figcaption>{caption}</figcaption>
</figure>'''


def lists(items):
    cards = ""
    for key, title, text in items:
        name, bg, fg = TAG[key]
        cards += f'<div class="sx-list"><span class="sx-tag" style="background: {bg}; color: {fg}">{name}</span><h3>{title}</h3><p>{text}</p></div>'
    return f'<div class="sx-lists">{cards}</div>'


def ask(question, answer, head=None, rows=None):
    tbl = ""
    if head and rows:
        th = "".join(f"<th scope=\"col\">{h}</th>" for h in head)
        tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
        tbl = f'<div class="sx-mini-wrap"><table class="sx-mini"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
    return f'''<div class="sx-ask">
<div class="sx-ask-q"><span class="sx-ask-icon" aria-hidden="true">?</span><p>{question}</p></div>
<div class="sx-ask-a"><p>{answer}</p>{tbl}</div>
<div class="sx-ask-foot">Example answer. Names and numbers are made up.</div>
</div>'''


def more_questions(qs):
    items = "".join(f"<li>{q}</li>" for q in qs)
    return f'<ul class="sx-asklist">{items}</ul><p class="sx-note">Change any underlined word to fit your shop. <a href="/ask-loyalbase/">See every question you can ask →</a></p>'


def dates(items, note=""):
    chips = "".join(f'<li><b>{n}</b><span>{w}</span></li>' for n, w in items)
    n = f'<p class="sx-note">{note}</p>' if note else ""
    return f'<ul class="sx-dates">{chips}</ul>{n}'


def u(s):
    return f"<u>{s}</u>"


def industry(slug, nav, title, desc, eyebrow, h1, stand, answer, body, faqs, related):
    PAGES.append(dict(path=f"/industries/{slug}/", section="industries", title=title, nav=nav, description=desc, eyebrow=eyebrow,
                      h1=h1, stand=stand, answer=answer, body=body, faqs=faqs, related=related, schema="article"))


COMMON_FAQ_PRIVACY = ("Does Loyalbase see my customers' names and phone numbers?",
                      "No. Names, phone numbers, emails and addresses stay on your store. Loyalbase holds order facts and scrambled codes it can't turn back into contact details. When you open a customer, your browser loads their name straight from your store.")

# ------------------------------------------------------------------ 1. Bakeries
industry(
    "bakeries-and-cake-shops", "Bakeries and cake shops",
    "Customer Retention for Bakeries and Cake Shops | Loyalbase",
    "Bring cake customers back for every birthday, anniversary and festival. Loyalbase finds who is due, writes the WhatsApp message and shows what came back.",
    "For bakeries and cake shops",
    "Get cake customers back for every birthday, not just one",
    "Most cake customers order for a reason: a birthday, an anniversary, Eid, Christmas. Loyalbase remembers the date for you and tells you who to message, two weeks before.",
    "Loyalbase is a customer retention app for bakeries and cake shops that sell on WooCommerce (Shopify is in early access). It reads your orders, spots customers who order around the same date every year, regulars who have gone quiet and festival buyers who didn't come back, and gives you a WhatsApp message for each. Cake wording is turned into a label like \"birthday\" on your own website, so the message itself never leaves your store.",
    f'''
<h2>How cake customers come back</h2>
<p>A bakery has two kinds of regulars. The first orders every week or two: office treats, bread, a Friday dessert. The second orders once or twice a year, always for the same reason, and is just as valuable. If you don't remind them, they order from whoever shows up first on Instagram that week.</p>
<p>Your WooCommerce orders already know who these people are. The cake message says "Happy 30th Anna" on 14 March. The same customer ordered on 12 March last year. That's a birthday you can plan for.</p>
{rhythm([8, 41, 74], 97, ("Mar 2024", "Mar 2025", "Mar 2026", "Now"), "Example: a customer who orders a birthday cake every March. Loyalbase puts her on the occasions list two weeks before the date.", "One order each March for three years, and a reminder two weeks before the next one", "Due")}

<h2>The lists that matter most for a bakery</h2>
{lists([
    ("occasion", "Birthdays and anniversaries coming up", "Customers who ordered around the same date in different years, due in the next two weeks. Each shows what they ordered last time and what it was worth."),
    ("late", "Weekly regulars who went quiet", "Someone who ordered every two weeks and hasn't in six. Loyalbase judges each person against their own rhythm, so twice-a-year customers aren't flagged by mistake."),
    ("first", "First birthday cake, no second order", "Bought once, 45 to 150 days ago. A short note before their next celebration is the easiest second order you'll get."),
    ("corp", "Offices that order for staff birthdays", "Customers who order with a company name or a work email. People from the same company are counted together, so you know how many offices you really sell to."),
])}

<h2>Questions bakery owners ask Loyalbase</h2>
<p>Open Ask, type a question the way you'd say it, or pick one from the list. Answers come straight from your own orders.</p>
{ask(f"Customers with a {u('birthday')} in the next {u('2 weeks')}",
     "12 customers have a birthday order due in the next 14 days. Last year they spent $1,140 between them.",
     ["Customer", "Due", "Last order"], [["Anna P.", "18 Mar", "$95"], ["Kasun D.", "21 Mar", "$120"], ["Sofia L.", "24 Mar", "$78"]])}
{ask(f"Customers who order for {u('Christmas')} in at least {u('2 different years')}",
     "41 customers ordered in the Christmas window in at least 2 of the last 3 years. They spent $5,860 last December. 9 haven't ordered at all this year.",
     ["Customer", "Christmas years", "Last December"], [["James T.", "3", "$240"], ["Priya S.", "2", "$180"], ["Omar K.", "2", "$150"]])}
{more_questions([
    f"What's bought together with {u('chocolate fudge cake')} {u('in the last 12 months')}",
    f"Delivery vs pickup {u('this month')}",
    f"Gift orders vs other orders {u('in the last 12 months')}",
    f"Sales by occasion {u('this year')}",
])}

<h2>Dates to plan for</h2>
{dates([("Valentine's Day", "Ads live 3 weeks before"), ("Mother's Day", "Pre-orders fill up fast"), ("Avurudu", "Sweets and gift boxes"), ("Eid ul-Fitr", "Cakes and dessert boxes"), ("Children's Day", "Cupcakes and party boxes"), ("Deepavali", "Sweets for family visits"), ("Christmas", "Your biggest month for many"), ("New Year's Eve", "Party orders")],
       "Loyalbase shows each date with last year's orders and the day your ads should go live.")}

<h2>A message that works for a bakery</h2>
{tpl(*TAG["occasion"], "The birthday cake, a year later",
     "about two weeks before the date they ordered for last year, so there's still time to pre-order.",
     "Hi [Name]! Last year you ordered a cake from us for a birthday on [date]. It's coming up again. Would you like us to make something this year? Order by [cut-off date] and we'll have it ready.\n[Shop name]",
     "It helps them remember a date before they start searching. The cut-off date gives a reason to answer now, without a discount.")}
<p>All seven bring-back messages are free on our <a href="/whatsapp-messages-to-bring-back-customers/">WhatsApp templates page</a>.</p>
{cta("See your bakery's birthdays and festival regulars")}
''',
    [
        ("Does Loyalbase read the message written on the cake?", "Only on your own website. The plugin turns the wording into a label such as birthday, anniversary, wedding or new baby, and only the label is sent. The wording itself never leaves your store."),
        ("We have walk-in customers at our branches. Are they included?", "Not yet. Loyalbase reads online orders from WooCommerce today. Branch and POS sales are on the roadmap. Online orders picked up at a branch are included, and show the branch as the area."),
        ("Can I see which branch people pick up from?", "Yes. When the shipping method says pickup or takeaway with a branch name, Loyalbase shows it as Pickup and the branch name, so you can ask for sales or customers by branch."),
        ("Many of our orders are gifts. Who gets the reminder?", "The person who placed the order. Loyalbase marks an order as a gift when it has a gift tick, a card message, or a different name or address for delivery, and the reminder goes to the buyer."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/guides/festival-customers/", "/industries/gifts-flowers-and-hampers/", "/whatsapp-messages-to-bring-back-customers/"],
)

# ------------------------------------------------------------------ 2. Gifts, flowers, hampers
industry(
    "gifts-flowers-and-hampers", "Gifts, flowers and hampers",
    "Customer Retention for Gift, Flower and Hamper Shops | Loyalbase",
    "Gift buyers order for other people, on dates they forget. Loyalbase remembers the dates, finds last Valentine's buyers and writes the message.",
    "For gift, flower and hamper shops",
    "Remind gift buyers before the date, not after",
    "Gift buyers order for someone else, on a date that comes round every year. Loyalbase spots the date, the gift and the buyer, and tells you who to remind first.",
    "Loyalbase is a customer retention app for gift, flower and hamper shops on WooCommerce (Shopify in early access). It recognises gift orders, learns the dates each customer buys for, groups company buyers together, and lists who to remind before Valentine's Day, Mother's Day, birthdays and hamper season, with a WhatsApp message for each. It also shows which of last year's peak-day buyers never came back.",
    f'''
<h2>Why gift customers drift away</h2>
<p>A gift shop's best customer might order four times a year: a partner's birthday, an anniversary, Mother's Day and Valentine's Day. Each order is an emergency. If you're the first shop they think of, you get it. If not, it goes to whoever has the fastest delivery that day.</p>
<p>Peak days make this worse. Valentine's Day can bring hundreds of first-time buyers, and most never order again. That's not because they didn't like you. Nobody asked them back.</p>
{rhythm([6, 18, 48, 56, 82, 94], None, ("Feb", "May", "Aug", "Feb", "May"), "Example: one buyer, four reasons a year. Valentine's Day, Mother's Day, a birthday in August and an anniversary.", "Orders clustered around the same four dates each year")}

<h2>The lists that matter most for a gift shop</h2>
{lists([
    ("occasion", "Dates they bought for last year", "Birthdays, anniversaries and other dates the same customer ordered around in different years, due in the next two weeks."),
    ("stopped", "Last Valentine's buyers who never returned", "Ask for customers who ordered before Valentine's Day last year but not since. Your warmest audience for this year's pre-orders."),
    ("corp", "Hamper buyers at companies", "Customers ordering with a company name or work email, sorted by spend. Call them before year-end, Eid, Avurudu or Deepavali."),
    ("best", "People who mostly send gifts", "Customers whose orders are mostly gifts. A thank you and first pick of the new range keeps them yours."),
])}

<h2>Questions gift shop owners ask Loyalbase</h2>
{ask(f"Customers who ordered {u('before Valentine’s Day 2026')} but haven't ordered since",
     "184 customers ordered in the 3 weeks before Valentine's Day 2026 and haven't ordered again. 151 of them ordered for the first time that week.",
     ["Customer", "Valentine's order", "Orders ever"], [["Daniel R.", "$85", "1"], ["Aisha N.", "$120", "1"], ["Ravi M.", "$64", "2"]])}
{ask(f"Sales by occasion {u('in the last 12 months')}",
     "Birthdays brought the most money: $18,400 from 312 orders. Anniversaries had the biggest orders, $96 on average.",
     ["Occasion", "Orders", "Sales"], [["Birthday", "312", "$18,400"], ["Anniversary", "121", "$11,620"], ["Festive", "208", "$14,980"], ["Thank you", "64", "$3,140"]])}
{more_questions([
    "Customers who mostly order gifts",
    f"Customers who ordered {u('before Mother’s Day 2026')} but not {u('before Mother’s Day 2025')}",
    "Business customers (company name or work email), sorted by spend",
    f"Gift orders vs other orders {u('this year')}",
])}

<h2>Dates to plan for</h2>
{dates([("Valentine's Day", "Ads live 3 weeks before"), ("Women's Day", "Flowers for teams"), ("Mother's Day", "Second biggest for many"), ("Father's Day", "Hampers and gift boxes"), ("Eid ul-Fitr", "Family hampers"), ("Deepavali", "Sweets and gift boxes"), ("Christmas", "Corporate hamper season"), ("New Year's Eve", "Last-minute gifts")],
       "Each date comes with last year's numbers, so you know how much stock to plan for.")}

<h2>A message that works for gift buyers</h2>
{tpl(*TAG["stopped"], "Last Valentine's Day, one year on",
     "three weeks before Valentine's Day, to people who ordered before it last year and haven't been back.",
     "Hi [Name], last Valentine's you sent flowers through us. Valentine's Day is on [date] this year. Shall we save you a delivery slot? Slots usually fill up a week before.\n[Shop name]",
     "A reminder of what they did last year, with a real reason to book early. It doesn't mention who the flowers were for, which keeps it polite if things have changed.")}
{cta("Find last year's peak-day buyers in your shop")}
''',
    [
        ("How does Loyalbase know an order was a gift?", "An order counts as a gift when it has a gift tick or card message, or when the delivery name or address is different from the buyer's. That check runs on your website."),
        ("Does the person who received the gift get a message?", "No. Loyalbase only works with your customer, the person who paid. Recipients' details aren't used."),
        ("Can it tell which occasion each order was for?", "Yes, when your checkout has a card or gift message. The plugin turns the wording into a label such as birthday, anniversary, get well or thank you, and only the label is sent."),
        ("We sell hampers to companies. Can I see those customers separately?", "Yes. Customers who order with a company name, or from a work email address, are marked as business customers, and people from the same company are counted together. Personal addresses like Gmail, Yahoo or Outlook aren't counted, and the email and domain never leave your store."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/corporate-gifting-and-b2b/", "/industries/bakeries-and-cake-shops/", "/guides/festival-customers/"],
)

# ------------------------------------------------------------------ 3. Grocery
industry(
    "online-grocery", "Online grocery",
    "Customer Retention for Online Grocery Stores | Loyalbase",
    "Weekly shoppers rarely say goodbye, they just stop. Loyalbase spots the missed weekly shop early, shows who is due and which areas are slipping.",
    "For online grocery and supermarkets",
    "Notice the missed weekly shop before it becomes a lost customer",
    "Grocery customers don't cancel. They miss one week, then two, then they're shopping somewhere else. Loyalbase shows you who missed their usual shop while it's still easy to win them back.",
    "Loyalbase is a customer retention app for online grocery stores and supermarkets on WooCommerce (Shopify in early access). It learns how often each customer shops, lists who is due and who has gone quiet, shows sales by delivery area, day and time, and gives you a WhatsApp message for each person. For weekly shoppers, Ask can find anyone with a month since their last order.",
    f'''
<h2>How grocery customers slip away</h2>
<p>Your best grocery customers shop every week or two. The basket is big and the margin is thin, so each lost regular costs you real money every month. They rarely complain. A late delivery, one missing item, a cheaper app, and they quietly move on.</p>
<p>The earlier you notice, the cheaper it is to win them back. A message in week three feels like service. A message in month three feels like spam.</p>
{rhythm([4, 13, 22, 31, 40, 49, 58, 67], 90, ("8 weeks ago", "4 weeks ago", "Now"), "Example: a customer who ordered every week, then stopped. Ask finds weekly shoppers like this a month after their last order.", "Weekly orders that stop, with a gap at the end")}

<h2>The lists that matter most for a grocery store</h2>
{lists([
    ("late", "Regulars who missed their usual shop", "Customers with two or more orders who have gone clearly longer than their own gap. For weekly shoppers, ask for anyone with 4+ orders and nothing in a month."),
    ("first", "First order, no second", "The second order is where grocery habits start. Bought once, 45 to 150 days ago, and not back."),
    ("unpaid", "Baskets that stopped at payment", "Full baskets that didn't get paid in the last two weeks. Often a card problem, easy to fix with a quick message."),
    ("best", "Big-basket households", "Customers whose usual order is well above average. Worth a personal thank you and a priority delivery slot."),
])}

<h2>Questions grocery owners ask Loyalbase</h2>
{ask(f"Customers who ordered {u('4')}+ times but haven't ordered in {u('a month')}",
     "63 customers who used to order regularly haven't ordered in a month. Their usual orders add up to $4,410 a week.",
     ["Customer", "Orders", "Last order", "Usual order"], [["Fatima R.", "22", "34 days ago", "$92"], ["Nuwan D.", "15", "31 days ago", "$71"], ["Lena M.", "9", "39 days ago", "$64"]])}
{ask(f"Sales by delivery area {u('last month')}",
     "Colombo 05 brought the most sales last month: $12,300 from 214 orders. Dehiwala fell 18% compared with the month before.",
     ["Area", "Orders", "Sales"], [["Colombo 05", "214", "$12,300"], ["Nugegoda", "176", "$9,850"], ["Dehiwala", "121", "$6,940"]])}
{more_questions([
    f"Customers usually due to order again in the next {u('3 days')}",
    f"Which day of the week sells most {u('in the last 90 days')}",
    f"What time of day people order {u('in the last 90 days')}",
    f"Customers whose usual order is over {u('$80')}",
])}
<p class="sx-note">Area names come from your own delivery settings, so they'll match the areas you already use.</p>

<h2>Dates to plan for</h2>
{dates([("Avurudu", "Bulk staples and sweets"), ("Ramadan", "Iftar orders every evening"), ("Eid ul-Fitr", "Big family baskets"), ("Deepavali", "Sweets and oil"), ("Christmas", "Baking and party orders"), ("Black Friday", "Stock-up deals")],
       "Ramadan works as a date range in Ask, so you can compare this year's Ramadan sales with last year's.")}

<h2>A message that works for grocery</h2>
{tpl(*TAG["late"], "The missed weekly shop",
     "when a weekly shopper has gone about a month without ordering.",
     "Hi [Name], we haven't seen your weekly order in a while. Is everything OK with your deliveries? If something went wrong, tell us and we'll fix it. Want us to set up your usual basket for [day]?\n[Shop name]",
     "It asks about the service first. Grocery customers often leave over one bad delivery, and an apology plus their usual basket wins many of them back.")}
{cta("See which regulars missed their shop this week")}
''',
    [
        ("Our customers shop weekly. Will the late list flag them in time?", "The late list waits at least 45 days, so it never nags. For weekly shoppers, use Ask: Customers who ordered 4+ times but haven't ordered in a month. Change the numbers to suit your store."),
        ("Can it show which delivery areas are slipping?", "Yes. Sales by delivery area shows orders and sales for each area, and you can compare any two periods. Customers in an area can be listed and sorted by spend."),
        ("Does it work with my delivery slots plugin?", "Loyalbase reads your orders after they're placed and doesn't change checkout, so it works alongside slot and delivery plugins."),
        ("Can I send one message to everyone on a list?", "You can download any list as a WhatsApp campaign file for Meta's Messaging campaigns, a spreadsheet, or send it to your Sendy email list. Only people who said yes to messages are included."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/guides/how-to-find-customers-who-stopped-buying/", "/industries/pet-food-and-supplies/", "/ask-loyalbase/"],
)

# ------------------------------------------------------------------ 4. Beauty
industry(
    "beauty-and-skincare", "Beauty and skincare",
    "Customer Retention for Beauty and Skincare Brands | Loyalbase",
    "Know when a customer's serum is running low, which first product turns buyers into regulars, and whether discounts bring them back.",
    "For beauty and skincare brands",
    "Reach beauty customers when the bottle runs out",
    "Skincare customers come back when they run out, if they remember you. Loyalbase learns each customer's refill rhythm and shows which first products turn into regulars.",
    "Loyalbase is a customer retention app for beauty and skincare brands on WooCommerce (Shopify in early access). It learns how often each customer reorders, lists who is overdue, shows which first product leads to a second order, what's bought together and whether discount codes bring people back, with a WhatsApp message ready for each customer.",
    f'''
<h2>How beauty customers come back</h2>
<p>A cleanser lasts about as long as it lasts. When it runs out, your customer either reorders from you, picks something up at the pharmacy, or tries the brand an influencer posted that morning. The order goes to whoever is in front of them at the right moment.</p>
<p>Two things decide most of it: reaching people near their refill date, and knowing which first product makes someone stay. Loyalbase answers both from your own orders.</p>
{rhythm([5, 25, 46, 66], 92, ("Jan", "Mar", "May", "Jul", "Now"), "Example: a customer who reorders roughly every 9 weeks. When the gap stretches well past that, she's on the late list.", "Orders about every nine weeks, then a long gap")}

<h2>The lists that matter most for a beauty brand</h2>
{lists([
    ("late", "Overdue for a refill", "Customers who reorder on a rhythm and have gone clearly past it. Each shows what they usually buy."),
    ("first", "Tried one product, never came back", "First order 45 to 150 days ago. Pair the message with the product that most often leads to a second order."),
    ("best", "Your loyal regulars", "Top spenders. Give them first look at launches before they're on Instagram."),
    ("stopped", "Lapsed regulars", "Two or more orders, nothing in over a year. Small list, worth a personal note."),
])}

<h2>Questions beauty owners ask Loyalbase</h2>
{ask(f"What new customers buy first {u('in the last 12 months')}, and who comes back",
     "The Vitamin C serum is the most common first buy, but people who start with the gentle cleanser come back most often: 41% placed a second order.",
     ["First product", "New customers", "Came back"], [["Vitamin C serum", "212", "28%"], ["Gentle cleanser", "148", "41%"], ["SPF 50 sunscreen", "131", "33%"]])}
{ask(f"Customers who bought {u('Vitamin C serum')} but haven't ordered in {u('2 months')}",
     "57 customers bought the Vitamin C serum and haven't ordered in 2 months. 38 of them said yes to WhatsApp messages.",
     ["Customer", "Orders", "Last order"], [["Priya S.", "3", "71 days ago"], ["Emma W.", "2", "64 days ago"], ["Hana K.", "4", "88 days ago"]])}
{more_questions([
    f"What's bought together with {u('gentle cleanser')} {u('in the last 12 months')}",
    f"Orders with and without a discount code {u('in the last 6 months')}",
    f"Customers who first came from {u('Instagram')} {u('in the last 6 months')}",
    f"Best posts by {u('likes')} {u('in the last 90 days')}",
])}

<h2>Dates to plan for</h2>
{dates([("Valentine's Day", "Gift sets"), ("Women's Day", "Self-care bundles"), ("Mother's Day", "Gift sets and minis"), ("Eid ul-Fitr", "Festive glow"), ("11.11 sale", "Big online sale day"), ("Black Friday", "Stock-up and bundles"), ("Christmas", "Gift sets")])}

<h2>A message that works for skincare</h2>
{tpl(*TAG["late"], "The refill reminder",
     "when a customer who reorders on a rhythm has gone clearly past their usual gap.",
     "Hi [Name], it's been about [weeks] weeks since your last [product]. If you're running low, we can send a fresh one out [day]. Want me to set it up?\n[Shop name]",
     "It names the product and the timing, so it reads like help, not an ad. No discount needed when the timing is right.")}
{cta("See which first products turn into regulars")}
''',
    [
        ("Can it tell me which product brings customers back?", "Yes. Ask \"What new customers buy first, and who comes back\" to see each first product with how many of those customers ordered again."),
        ("Should I offer a discount to bring people back?", "Check first. Ask for orders with and without a discount code, or customers who used a code. Loyalbase shows which codes bring people back for a second order and which only bring one-off buyers."),
        ("Does it connect to my Instagram and Facebook?", "Yes. Connect Facebook to see Meta ad results and your Facebook and Instagram posts next to the sales that really came in. Ask can rank your posts by reach, likes or comments."),
        ("Can I send launch news to my best customers only?", "Yes. Ask for your top customers by spend, then download the list as a WhatsApp campaign file or send it to Sendy. Only people who said yes are included."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/fashion-and-clothing/", "/whatsapp-messages-to-bring-back-customers/", "/ask-loyalbase/"],
)

# ------------------------------------------------------------------ 5. Fashion
industry(
    "fashion-and-clothing", "Fashion and clothing",
    "Customer Retention for Fashion and Clothing Stores | Loyalbase",
    "Find last Eid's buyers before this Eid, see who only buys on discount, and bring back last season's shoppers. For WooCommerce fashion stores.",
    "For fashion and clothing stores",
    "Bring last season's shoppers back for the next one",
    "Fashion customers buy in seasons: Eid, Avurudu, Deepavali, Christmas, a big sale day. Loyalbase shows who bought last season and hasn't come back, so your launch goes to people who already like you.",
    "Loyalbase is a customer retention app for fashion and clothing stores on WooCommerce (Shopify in early access). It groups customers by the festivals they shop for, finds last season's buyers who haven't returned, shows who only buys with a discount code, and compares this season with last year's, with a WhatsApp message ready for each customer.",
    f'''
<h2>How fashion customers buy</h2>
<p>Clothing doesn't run out like coffee. People come back when there's a reason: a festival, a wedding, a new collection, a sale. Miss the reason and they buy their festival outfit somewhere else.</p>
<p>The good news is the reasons repeat. A customer who bought before Eid two years running is very likely to buy before this Eid. You just need to reach her before she starts browsing.</p>
{rhythm([14, 47, 80], 96, ("Eid 2024", "Eid 2025", "Eid 2026", "Now"), "Example: a customer who shops in the weeks before Eid every year. Loyalbase counts her as an Eid customer for three years running.", "One order before Eid each year for three years", "Due")}

<h2>The lists that matter most for a fashion store</h2>
{lists([
    ("festival", "Festival regulars", "Customers who ordered in the festival window in at least two different years. Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali and Thai Pongal."),
    ("stopped", "Last season, not this one", "Ask for customers who ordered before last Eid (or Christmas, or Black Friday) but haven't ordered since."),
    ("best", "Full-price regulars", "Top spenders who rarely use codes. Show them the collection first, without the discount."),
    ("first", "One-time sale shoppers", "First order 45 to 150 days ago. Worth a note when the new collection lands."),
])}

<h2>Questions fashion owners ask Loyalbase</h2>
{ask("Which festivals do my customers order for?",
     "Eid ul-Fitr is your biggest festival: 486 customers ordered for it, 132 of them in at least two years. Avurudu is second with 301.",
     ["Festival", "Customers", "2+ years"], [["Eid ul-Fitr", "486", "132"], ["Avurudu", "301", "74"], ["Christmas", "244", "51"], ["Deepavali", "118", "29"]])}
{ask(f"Customers who {u('never used')} a discount code {u('in the last 12 months')}",
     "212 customers bought at full price in the last 12 months. They spent $38,900, which is 46% of your sales.",
     ["Customer", "Orders", "Spend"], [["Aisha N.", "6", "$640"], ["Sofia L.", "4", "$510"], ["Zara H.", "5", "$470"]])}
{more_questions([
    f"Customers who order for {u('Eid ul-Fitr')} in at least {u('2 different years')}",
    f"Compare {u('November 2026')} with {u('the same dates a year before')}",
    f"Slowest-selling products {u('in the last 90 days')}",
    f"Best-selling products {u('this month')}, by {u('sales')}",
])}

<h2>Dates to plan for</h2>
{dates([("Avurudu", "New clothes tradition"), ("Eid ul-Fitr", "Biggest for modest fashion"), ("Eid ul-Adha", "Second Eid wave"), ("Vesak", "White wear"), ("Deepavali", "Sarees and festive wear"), ("11.11 sale", "Online sale day"), ("Black Friday", "Sale season starts"), ("Christmas", "Party and gift wear")],
       "Loyalbase shows when your ads should go live for each date, based on how early your customers started ordering last year.")}

<h2>A message that works for fashion</h2>
{tpl(*TAG["festival"], "Last Eid's shopper, before this Eid",
     "three weeks before Eid, to customers who ordered before Eid last year.",
     "Hi [Name]! Thank you for shopping with us for Eid last year. The new Eid collection is in, and I wanted you to see it before we post it: [link]. Orders before [date] arrive in time for Eid.\n[Shop name]",
     "First look feels like a favour, not an ad. The delivery deadline gives a reason to order early.")}
{cta("See which festivals your customers shop for")}
''',
    [
        ("How does Loyalbase decide someone is an Eid customer?", "Each festival has a short ordering window, for example the 10 days before Eid ul-Fitr. Orders in that window count for that festival, year by year. Days that fall in two festivals' windows count for neither, so an order is never put down to the wrong one."),
        ("Which festivals does it know?", "Customers are grouped by Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali and Thai Pongal. Peak dates also cover Valentine's Day, Mother's Day, 11.11, Black Friday, New Year's Eve and more, and you can pick your own dates in Ask."),
        ("Can I see if my sale only attracted discount hunters?", "Yes. Ask for customers who used a discount code in a period, and look at how many of them came back for a second order."),
        ("Does it handle sizes and variants?", "Loyalbase works with product names as they appear on the order. Best sellers, slow sellers and bought together use those names."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/guides/festival-customers/", "/industries/beauty-and-skincare/", "/guides/loyalty-program-vs-win-back-messages/"],
)

# ------------------------------------------------------------------ 6. Pet
industry(
    "pet-food-and-supplies", "Pet food and supplies",
    "Customer Retention for Pet Food and Pet Supply Stores | Loyalbase",
    "Pet food runs out on a schedule. Loyalbase learns each customer's timing, lists who is due this week and who switched away, and writes the reminder.",
    "For pet food and supply stores",
    "Remind pet owners before the food bag runs out",
    "Pet food is the most predictable reorder in ecommerce. The same food, the same bag size, every few weeks. Loyalbase learns each customer's timing and shows who is due before they run out.",
    "Loyalbase is a customer retention app for pet food and pet supply stores on WooCommerce (Shopify in early access). It learns how often each customer reorders, lists who is due in the next few days and who has gone past their usual gap, and shows which products are bought together, with a WhatsApp reminder ready for each customer.",
    f'''
<h2>How pet owners reorder</h2>
<p>A dog doesn't skip dinner. When the bag runs low, the owner buys more, from you or from the supermarket on the way home. Once they switch, they rarely switch back, because pets get used to a food and owners stop shopping around.</p>
<p>That makes timing everything. A reminder two days before the bag runs out wins the order. A reminder two weeks after means they already bought it elsewhere.</p>
{rhythm([5, 20, 35, 50, 65, 80], 97, ("5 months ago", "3 months ago", "Now"), "Example: a customer who buys a 10 kg bag every 4 to 5 weeks. Loyalbase shows when she's due, before she runs out.", "Orders every four to five weeks, next one due", "Due")}

<h2>The lists that matter most for a pet store</h2>
{lists([
    ("late", "Past their usual reorder", "Regulars who have gone clearly past their own gap. Most have run out and bought elsewhere this time. Win back the next bag."),
    ("first", "First bag, no second", "First order 45 to 150 days ago. Ask how the pet is getting on with the food."),
    ("best", "Multi-pet households", "Top spenders with big usual orders. A delivery slot that suits them keeps them for years."),
    ("stopped", "Switched away", "Two or more orders, nothing in over a year. Sometimes the pet passed away, so keep the message gentle."),
])}

<h2>Questions pet store owners ask Loyalbase</h2>
{ask(f"Customers usually due to order again in the next {u('7 days')}",
     "46 customers are due to reorder in the next 7 days, based on their own past gaps. Their usual orders add up to $3,150.",
     ["Customer", "Usually orders every", "Due"], [["Omar K.", "32 days", "in 2 days"], ["Lena M.", "28 days", "in 4 days"], ["Kasun P.", "35 days", "in 6 days"]])}
{ask(f"What's bought together with {u('Adult dry food 10kg')} {u('in the last 12 months')}",
     "Dental chews are bought with the 10 kg bag in 22% of orders. Customers who add them come back more often.",
     ["Bought with it", "Orders together", "Share"], [["Dental chews", "118", "22%"], ["Wet food pouches 12-pack", "96", "18%"], ["Flea and tick drops", "41", "8%"]])}
{more_questions([
    f"Customers who bought {u('Adult dry food 10kg')} but haven't ordered in {u('6 weeks')}",
    "Regulars who are late for their usual next order",
    f"Top {u('20')} customers by {u('spend')} {u('this year')}",
    f"How {u('Kitten food 2kg')} sold, month by month, {u('in the last 12 months')}",
])}

<h2>Dates to plan for</h2>
{dates([("Black Friday", "Stock-up bags"), ("11.11 sale", "Online sale day"), ("Christmas", "Toys and treats"), ("New Year's Eve", "Calming products before fireworks")],
       "Pet stores sell steadily all year, so the reorder lists matter more than any single date.")}

<h2>A message that works for pet food</h2>
{tpl(*TAG["late"], "The bag is about to run out",
     "a few days before a regular is due, or as soon as they go past their usual gap.",
     "Hi [Name], it's about time for [pet's food] again. Want us to send the usual [bag size] on [day]? Reply YES and we'll sort it.\n[Shop name]",
     "One word to reply, and the decision is already made for them. Reminders that save a trip work better than discounts.")}
{cta("See which pet owners are due this week")}
''',
    [
        ("Can Loyalbase send reminders automatically?", "Not yet. Today it lists who is due and writes the message, and you send it with a tap on WhatsApp. Automatic reminders that you approve first are next on our roadmap."),
        ("How does it know when a customer is due?", "It looks at the gaps between each customer's own past orders. Someone who orders every 30 days is due around day 30. Ask can list everyone due in the next few days."),
        ("Can I see customers by the product they buy?", "Yes. Ask for customers who bought a product in any period, or who bought it but haven't ordered since a set number of days."),
        ("We also sell in a physical shop. Are those sales included?", "Not yet. Online orders from WooCommerce are included today. POS and branch sales are on the roadmap."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/online-grocery/", "/industries/coffee-tea-and-specialty-food/", "/guides/how-to-find-customers-who-stopped-buying/"],
)

# ------------------------------------------------------------------ 7. Restaurants
industry(
    "restaurants-and-cloud-kitchens", "Restaurants and cloud kitchens",
    "Customer Retention for Restaurants and Cloud Kitchens | Loyalbase",
    "For restaurants taking orders on their own website. See your regulars, when they order, which areas and branches sell, and bring back customers who went quiet.",
    "For restaurants and cloud kitchens",
    "Keep your regulars ordering direct, not through the delivery apps",
    "Every order on your own website saves you the delivery app's cut. Loyalbase shows who your direct regulars are, when they usually order, and who has gone quiet, so you can keep them.",
    "Loyalbase is a customer retention app for restaurants and cloud kitchens that take orders on their own WooCommerce website. It lists regulars who have gone quiet and first-time customers who didn't come back, shows the busiest days and hours, delivery against pickup and sales by area or branch, and writes a WhatsApp message for each customer. Orders placed through delivery apps aren't included.",
    f'''
<h2>Why direct regulars matter</h2>
<p>Delivery apps bring new customers, then take a slice of every order those customers place. When the same person orders from your own website, you keep the margin and you know who they are.</p>
<p>Direct regulars are worth protecting. They usually order on the same days, at the same times, for the same dishes. When one goes quiet, you should hear about it in weeks, not months.</p>
{rhythm([3, 11, 19, 27, 36, 44, 52, 60], 92, ("2 months ago", "1 month ago", "Now"), "Example: a Friday-night regular who ordered almost every week, then stopped.", "Weekly orders that stopped about a month ago")}

<h2>The lists that matter most for a restaurant</h2>
{lists([
    ("late", "Regulars who went quiet", "Customers who used to order often and haven't lately. For weekly regulars, ask for anyone with 5+ orders and nothing in a month."),
    ("first", "Tried you once", "First order 45 to 150 days ago. Many found you on a busy night and forgot your name."),
    ("best", "Your house favourites", "Top customers by orders. A thank-you dessert in the next order costs little and keeps them loyal."),
    ("corp", "Office lunch orders", "Customers ordering with a company name or a work email. Worth a call before month-end team lunches."),
])}

<h2>Questions restaurant owners ask Loyalbase</h2>
{ask(f"What time of day people order {u('in the last 90 days')}",
     "8 pm is your busiest hour, then 7 pm. Lunch brings fewer orders, but they're bigger.",
     ["Hour", "Orders", "Average order"], [["8 pm", "890", "$32"], ["7 pm", "820", "$30"], ["1 pm", "640", "$35"]])}
{ask(f"Delivery vs pickup {u('this month')}",
     "62% of this month's orders were delivered. Pickup grew 14% compared with the same days last month.",
     ["Type", "Orders", "Sales"], [["Delivery", "812", "$25,600"], ["Pickup", "497", "$14,100"]])}
{more_questions([
    f"Customers who ordered {u('5')}+ times but haven't ordered in {u('a month')}",
    f"Which day of the week sells most {u('in the last 90 days')}",
    f"Sales from new vs returning customers {u('this month')}",
    f"Sales by delivery area {u('last month')}",
])}

<h2>Dates to plan for</h2>
{dates([("Valentine's Day", "Dinner for two"), ("Ramadan", "Iftar every evening"), ("Eid ul-Fitr", "Family feasts"), ("Mother's Day", "Family lunch"), ("Christmas", "Party platters"), ("New Year's Eve", "Party orders")])}

<h2>A message that works for restaurants</h2>
{tpl(*TAG["late"], "The regular you haven't heard from",
     "when a weekly regular has gone about a month without ordering.",
     "Hi [Name], we've missed your [day] orders! Your usual [dish] is waiting. Order direct this week at [link] and dessert is on us.\n[Shop name]",
     "It shows you noticed, mentions their favourite, and gives a small reason to order direct rather than through an app.")}
{cta("See your direct regulars and when they order")}
''',
    [
        ("Does Loyalbase include orders from delivery apps?", "No. It reads orders placed on your own WooCommerce website. Orders placed through delivery apps stay in those apps."),
        ("We take dine-in and walk-in orders on a POS. Are those included?", "Not yet. Branch and POS sales are on our roadmap. Online orders for pickup at a branch are included and show the branch name."),
        ("Can I see busy times by day and hour?", "Yes. Ask which day of the week sells most, or what time of day people order, for any period."),
        ("How do I message a regular?", "Tap the customer and WhatsApp opens with the message written. You can change every word before it goes. Lists can also be downloaded as a WhatsApp campaign file, with only people who said yes."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/online-grocery/", "/industries/bakeries-and-cake-shops/", "/ask-loyalbase/"],
)

# ------------------------------------------------------------------ 8. Coffee, tea, specialty food
industry(
    "coffee-tea-and-specialty-food", "Coffee, tea and specialty food",
    "Customer Retention for Coffee, Tea and Specialty Food | Loyalbase",
    "Turn tasting-set buyers into monthly regulars, remind people before the bag runs out, and find your gift and office customers.",
    "For coffee, tea and specialty food brands",
    "Turn one bag of coffee into a monthly habit",
    "Coffee, tea and pantry customers reorder when they run out, and gift your products at festivals. Loyalbase shows who is due, which first product makes them stay, and who buys for gifts.",
    "Loyalbase is a customer retention app for coffee, tea and specialty food brands on WooCommerce (Shopify in early access). It learns each customer's reorder rhythm, shows which first product leads to a second order, separates gift orders from everyday ones, groups office buyers by company, and gives you a WhatsApp message for each customer.",
    f'''
<h2>How coffee and tea customers come back</h2>
<p>Your customers buy for two reasons. They drink it every day and reorder when the bag runs low. And they give it as a gift, to family at festivals or to clients at year-end. The everyday buyer is your steady income. The gift buyer brings you new everyday buyers.</p>
<p>Most brands treat them the same. Loyalbase splits them, so the reorder reminder goes to the daily drinker and the hamper reminder goes to the gifter.</p>
{rhythm([6, 24, 41, 59, 76], 96, ("6 months ago", "3 months ago", "Now"), "Example: a customer who buys a 500 g bag about every 5 weeks. The gap is stretching, so she's due a reminder.", "Orders about every five weeks, the last gap longer", "Due")}

<h2>The lists that matter most for coffee and tea</h2>
{lists([
    ("late", "Running low", "Regulars who have gone clearly past their own reorder gap. Each shows the product they usually buy."),
    ("first", "Sample pack, no full bag", "First order 45 to 150 days ago. The moment to suggest the full-size version of what they tried."),
    ("occasion", "Gift buyers before festivals", "Customers whose orders are mostly gifts, and those who bought before last Christmas or Avurudu."),
    ("corp", "Office and client buyers", "Customers ordering with a company name or work email. Office coffee and client gifts are often your biggest orders."),
])}

<h2>Questions coffee and tea owners ask Loyalbase</h2>
{ask(f"What new customers buy first {u('in the last 12 months')}, and who comes back",
     "The tasting set is the most popular first buy, and 44% of those customers came back. Only 19% of people who started with a single 250 g bag ordered again.",
     ["First product", "New customers", "Came back"], [["Tasting set", "184", "44%"], ["House blend 250 g", "236", "19%"], ["Ceylon black tea 500 g", "121", "37%"]])}
{ask(f"Gift orders vs other orders {u('in the last 12 months')}",
     "Gift orders were 27% of orders but 38% of sales, mostly in December and before Avurudu.",
     ["Type", "Orders", "Sales", "Average order"], [["Gift", "412", "$21,300", "$52"], ["Not a gift", "1,108", "$34,700", "$31"]])}
{more_questions([
    f"How {u('House blend 250 g')} sold, month by month, {u('in the last 12 months')}",
    "Customers who mostly order gifts",
    f"Customers who bought {u('Tasting set')} but haven't ordered in {u('2 months')}",
    "Business customers (company name or work email), sorted by spend",
])}

<h2>Dates to plan for</h2>
{dates([("Avurudu", "Tea gift boxes"), ("Mother's Day", "Gift sets"), ("Father's Day", "Coffee gifts"), ("Eid ul-Fitr", "Hampers for visits"), ("Deepavali", "Gift boxes"), ("Christmas", "Client and family gifts")])}

<h2>A message that works for coffee and tea</h2>
{tpl(*TAG["first"], "From tasting set to full bag",
     "about four weeks after a first order of a sample or tasting set.",
     "Hi [Name], how did you find the tasting set? Most people end up with a favourite. Tell me which one and I'll send a full bag, roasted this week.\n[Shop name]",
     "It asks for their opinion first, and turns the answer into an easy order. \"Roasted this week\" gives a reason to buy direct.")}
{cta("See which first buys turn into regulars")}
''',
    [
        ("We sell subscriptions. Is Loyalbase still useful?", "Yes. It shows customers who buy regularly without a subscription, and those whose orders stopped. Those are the people most likely to sign up, or to need a nudge."),
        ("Can I find customers who buy for gifts?", "Yes. Orders with a gift tick, card message or a different delivery name or address count as gifts. Ask for customers who mostly order gifts, or compare gift and other orders."),
        ("Can I see how one product is doing over time?", "Yes. Ask how any product sold, month by month, and which products are rising or falling."),
        ("Does it work outside Sri Lanka?", "Yes. Loyalbase works in any country and currency, and phone numbers are matched in full international form."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/gifts-flowers-and-hampers/", "/industries/pet-food-and-supplies/", "/ask-loyalbase/"],
)

# ------------------------------------------------------------------ 9. Baby and kids
industry(
    "baby-and-kids", "Baby and kids",
    "Customer Retention for Baby and Kids Stores | Loyalbase",
    "Nappies run out, children grow, birthdays come round. Loyalbase shows which parents are due, what they buy next, and who orders for birthdays.",
    "For baby and kids stores",
    "Grow with your customers' children",
    "Parents reorder nappies and wipes on a rhythm, then move to the next size, the next toy and the next birthday. Loyalbase shows who is due, and what parents usually buy next.",
    "Loyalbase is a customer retention app for baby and kids stores on WooCommerce (Shopify in early access). It learns each parent's reorder rhythm, lists who is due or has gone quiet, shows what new customers buy first and who comes back, spots gift orders like new baby gifts, and writes a WhatsApp message for each customer.",
    f'''
<h2>How parents buy</h2>
<p>A baby store has a customer for a few years, and the needs change every few months. Newborn nappies become size 3. Bottles become cups. Then it's birthdays, school bags and Children's Day.</p>
<p>That means "stopped ordering" doesn't always mean lost. Sometimes the child simply grew out of what you sell them. The fix is to show them the next stage at the right time, before they find it somewhere else.</p>
{rhythm([5, 17, 29, 41, 53, 65], 92, ("6 months ago", "3 months ago", "Now"), "Example: a parent who bought nappies and wipes every 3 to 4 weeks, then stopped. Time to ask about the next size.", "Orders every three to four weeks, then a gap")}

<h2>The lists that matter most for a baby store</h2>
{lists([
    ("late", "Due for nappies and wipes", "Parents who reorder on a rhythm and have gone past it. Each shows what they usually buy."),
    ("first", "Baby shower gift, no second order", "First order 45 to 150 days ago, often a gift. Many buyers are about to need baby things themselves, or know someone who will."),
    ("occasion", "Birthdays coming up", "Customers who ordered around the same date in different years. Often a child's birthday."),
    ("best", "Your most loyal parents", "Top spenders. First look at the next-stage range keeps them with you as the child grows."),
])}

<h2>Questions baby store owners ask Loyalbase</h2>
{ask(f"Customers who bought {u('Newborn nappies 84-pack')} but haven't ordered in {u('6 weeks')}",
     "73 customers bought newborn nappies and haven't ordered in 6 weeks. Most of their babies will be in the next size by now.",
     ["Customer", "Orders", "Last order"], [["Sofia L.", "5", "52 days ago"], ["Hana K.", "3", "61 days ago"], ["Nuwan D.", "4", "47 days ago"]])}
{ask(f"Sales by occasion {u('in the last 12 months')}",
     "New baby gifts brought $9,800 from 214 orders, and birthdays $14,200. Most new baby gift buyers ordered only once.",
     ["Occasion", "Orders", "Sales"], [["Birthday", "286", "$14,200"], ["New baby", "214", "$9,800"], ["Festive", "151", "$6,900"]])}
{more_questions([
    f"What's bought together with {u('baby wipes 12-pack')} {u('in the last 12 months')}",
    f"What new customers buy first {u('in the last 12 months')}, and who comes back",
    f"Customers who ordered {u('before Children’s Day 2025')} but haven't ordered since",
    f"Customers with a {u('birthday')} in the next {u('30 days')}",
])}

<h2>Dates to plan for</h2>
{dates([("Avurudu", "New clothes and toys"), ("Mother's Day", "Gifts for new mums"), ("Children's Day", "Toys and treats"), ("Eid ul-Fitr", "Festive outfits"), ("11.11 sale", "Stock-up day"), ("Christmas", "Toys")])}

<h2>A message that works for baby stores</h2>
{tpl(*TAG["late"], "The next size up",
     "when a parent who bought nappies regularly has gone past their usual gap.",
     "Hi [Name]! It's been a while since your last nappy order. [Baby's name] is probably ready for the next size by now. Want me to send size [x] with your usual wipes?\n[Shop name]",
     "It assumes the reason they stopped is a happy one, and makes the next stage the easy choice.")}
{cta("See which parents are due this week")}
''',
    [
        ("A customer stopped buying nappies. Have we lost them?", "Not always. Often the child moved to a new size or stage. Loyalbase shows what they used to buy, so your message can offer the next stage instead of the same product."),
        ("Can it spot new baby gifts?", "Yes, when the order has a gift tick, a card message or a different delivery address. The plugin turns card wording into a label such as new baby or birthday, and the wording never leaves your store."),
        ("Do you store information about children?", "No. Loyalbase works with orders and the occasion label only. Customer names, phones, emails, addresses and card wording stay on your store."),
        ("Can I message only parents who said yes?", "Yes. Bulk downloads and email sends only include customers who said yes to messages. Tapping to WhatsApp one person is your call."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/gifts-flowers-and-hampers/", "/industries/online-grocery/", "/whatsapp-messages-to-bring-back-customers/"],
)

# ------------------------------------------------------------------ 10. Corporate / B2B
industry(
    "corporate-gifting-and-b2b", "Corporate gifting and B2B",
    "Find and Keep Corporate and B2B Customers in WooCommerce | Loyalbase",
    "Loyalbase spots business customers from the company name or a work email, counts each company once and shows who ordered last festive season but not this one.",
    "For corporate gifting and B2B orders",
    "See your company customers as companies, not strangers",
    "Five people from one company order from you, each with their own email. WooCommerce sees five strangers. Loyalbase sees five buyers from one company, what they spend and when they order.",
    "Loyalbase finds business customers in your WooCommerce orders from the company name at checkout, or from a work email address when the company field is empty. Personal addresses like Gmail, Yahoo and Outlook are left out, and the email and domain never leave your store. People from the same company are counted together, and you get a list of every business customer sorted by spend, who ordered last festive season but not this one, and who to call before year-end.",
    f'''
<h2>Why company customers get missed</h2>
<p>Corporate orders are often a store's biggest: year-end hampers, staff birthday cakes, client gifts, office supplies. But they arrive looking like ordinary orders, placed by different people from the same office, often without a company name.</p>
<p>So the account is invisible. Nobody notices when the company that ordered 40 hampers last December hasn't called this year, until December is over.</p>

<h2>How Loyalbase spots a company</h2>
<ol class="sx-steps">
<li><b>Company name at checkout.</b> If the customer typed one, that's the company.</li>
<li><b>Work email address.</b> If the company field is empty, an email at a company's own domain counts. People at the same company are counted as one company.</li>
<li><b>Personal and shop addresses left out.</b> Gmail, Yahoo, Hotmail, Outlook, iCloud and similar, plus local internet providers and your own shop's domain, never count as a company.</li>
<li><b>Nothing readable leaves your store.</b> The plugin sends only a scrambled code for the company. Loyalbase can tell two people share a company, but can't turn the code back into the email or domain.</li>
</ol>

<h2>The lists that matter most for B2B</h2>
{lists([
    ("corp", "Business customers by spend", "Everyone who orders with a company name or work email, with spend and last order, and how many companies they come from. Your key accounts, without a CRM."),
    ("stopped", "Last festive season, not this one", "Companies that ordered before last Christmas, Eid or Avurudu and haven't ordered since. Call them first."),
    ("occasion", "Yearly company events", "Companies that order around the same date every year: an anniversary, an annual day, staff awards."),
    ("best", "Big-order buyers", "Customers whose usual order is well above average. Often the person in charge of office gifting."),
])}

<h2>Questions B2B sellers ask Loyalbase</h2>
{ask("Business customers (company name or work email), sorted by spend",
     "148 customers order with a company name or a work email, from 64 companies. Together they spent $52,300 in the last 12 months.",
     ["Customer", "Orders", "Spend"], [["Ravi M.", "14", "$6,840"], ["Lena M.", "9", "$4,210"], ["James T.", "6", "$3,960"]])}
{ask(f"Customers who ordered {u('before Christmas 2025')} but haven't ordered since",
     "38 customers ordered in the four weeks before Christmas 2025 and haven't ordered since. 17 of them order for a company.",
     ["Customer", "Christmas order", "Company"], [["James T.", "$1,240", "Yes"], ["Priya S.", "$860", "Yes"], ["Omar K.", "$140", "No"]])}
{more_questions([
    f"Customers whose usual order is over {u('$300')}",
    f"Customers who have spent more than {u('$2,000')} in total",
    f"Compare {u('December 2025')} with {u('the same dates a year before')}",
    f"Customers who order for {u('Christmas')} in at least {u('2 different years')}",
])}

<h2>Dates to plan for</h2>
{dates([("Avurudu", "Staff and client gifts"), ("Eid ul-Fitr", "Hampers"), ("Deepavali", "Sweet boxes"), ("Christmas", "Year-end gifting"), ("New Year's Eve", "Office parties"), ("Women's Day", "Team gifts")],
       "Corporate buyers plan earlier than shoppers. Call 6 weeks before, not 2.")}

<h2>A message that works for company buyers</h2>
{tpl(*TAG["corp"], "Planning year-end gifts?",
     "about six weeks before the season the company ordered for last year.",
     "Hi [Name], last year we made [number] hampers for [Company] for Christmas. Are you planning gifts again this year? I can send this year's range and hold your delivery date now.\n[Shop name]",
     "It shows you remember the account, and holding a delivery date is a practical reason to decide early.")}
{cta("See every business customer in your store")}
''',
    [
        ("How does Loyalbase know a customer is a business?", "From the company name at checkout, or from a work email address when that's empty. Personal providers like Gmail, Yahoo, Hotmail, Outlook and iCloud don't count, and nor does your own shop's domain."),
        ("Does my customers' email domain leave my store?", "No. The plugin sends a scrambled code made with a key that stays on your website. Loyalbase can tell when two customers share a company, but can't read the email or domain."),
        ("Do I need to update the plugin?", "Yes, to group by work email you need plugin version 0.5.0 or newer. Settings in Loyalbase has a download for the latest version once your store is connected."),
        ("Is this a CRM?", "No. Loyalbase shows who your company customers are, what they're worth and who to call, from your orders. If you use a CRM, keep it."),
        COMMON_FAQ_PRIVACY,
    ],
    ["/industries/gifts-flowers-and-hampers/", "/guides/festival-customers/", "/ask-loyalbase/"],
)


# ------------------------------------------------------------------ Industries hub
HUB_ITEMS = [
    ("bakeries-and-cake-shops", "Bakeries and cake shops", "Birthdays, anniversaries and festival orders, remembered for you."),
    ("gifts-flowers-and-hampers", "Gifts, flowers and hampers", "Remind gift buyers before the date, and win back last Valentine's buyers."),
    ("online-grocery", "Online grocery", "Notice the missed weekly shop while it's still easy to fix."),
    ("beauty-and-skincare", "Beauty and skincare", "Reach customers when the bottle runs out, and learn which first product makes them stay."),
    ("fashion-and-clothing", "Fashion and clothing", "Bring last season's festival shoppers back for the next one."),
    ("pet-food-and-supplies", "Pet food and supplies", "Remind pet owners before the food bag runs out."),
    ("restaurants-and-cloud-kitchens", "Restaurants and cloud kitchens", "Keep regulars ordering direct, and see when they order."),
    ("coffee-tea-and-specialty-food", "Coffee, tea and specialty food", "Turn a tasting set into a monthly habit."),
    ("baby-and-kids", "Baby and kids", "Grow with your customers' children, from nappies to birthdays."),
    ("corporate-gifting-and-b2b", "Corporate gifting and B2B", "Find every business customer, and call them before the season."),
]

hub_cards = "".join(f'<a href="/industries/{s}/"><span>Industry</span><b>{n}</b><p>{t}</p></a>' for s, n, t in HUB_ITEMS)
PAGES.append(dict(
    path="/industries/",
    section="industries",
    title="Customer Retention by Industry | Loyalbase",
    nav="Industries",
    description="How Loyalbase brings customers back for bakeries, gift shops, grocery, beauty, fashion, pet, restaurants, coffee, baby stores and B2B sellers on WooCommerce.",
    eyebrow="Industries",
    h1="Built for how your store sells",
    stand="Every kind of store loses customers in its own way. A bakery loses a birthday, a grocery store loses a weekly shop. Pick yours to see the lists, questions and messages that matter most.",
    answer="Loyalbase works for any WooCommerce store whose customers buy more than once (Shopify is in early access). It learns each customer's own rhythm, so the same app spots a missed weekly grocery shop, a skincare refill that's overdue and a birthday cake due once a year.",
    body=f'''
<div class="sx-hub">{hub_cards}</div>
<h2>Don't see your industry?</h2>
<p>If your customers buy more than once, Loyalbase will find the ones drifting away. It doesn't need to know your industry, because it judges each customer against their own past orders. A customer who buys every three weeks is late after about six. One who buys twice a year isn't late for about nine months.</p>
<p>Some features shine for certain stores. Occasions come from gift card and cake wording. Festival groups suit stores with seasonal peaks. Company accounts suit anyone who sells to offices. Ask works for everyone.</p>
{cta("Not sure it fits? Ask us on WhatsApp", "Tell us what you sell and we'll show you what Loyalbase would find in a store like yours. From $50 a month, free while we set you up.")}
''',
    faqs=[
        ("Which stores is Loyalbase best for?", "Stores where customers buy more than once: food, gifts, beauty, fashion, pet, coffee, baby and kids, and anyone selling to offices. One-off purchases like furniture get less from it."),
        ("Does it work outside Sri Lanka?", "Yes. Loyalbase works in any country and currency. Phone numbers are matched in full international form."),
        ("Which platforms does it work with?", "WooCommerce today. The Shopify app is in early access. POS and branch sales are on the roadmap."),
    ],
    related=[],
    schema="collection",
))


# ------------------------------------------------------------------ Ask Loyalbase page
def qline(s):
    return f"<li>{s}</li>"


ASK_GROUPS = [
    ("Customers", [
        f"Top {u('20')} customers by {u('spend')} {u('this year')}",
        f"Customers who ordered {u('3')}+ times but haven't ordered in {u('2 months')}",
        "Regulars who are late for their usual next order",
        f"Customers usually due to order again in the next {u('7 days')}",
        f"New customers who first ordered {u('this month')}",
        f"Customers who first ordered {u('in the last 6 months')} and never ordered again",
        f"Customers who bought {u('a product')} {u('in the last 12 months')}",
        f"Customers who bought {u('a product')} but haven't ordered in {u('2 months')}",
        f"Customers who ordered {u('before Christmas 2025')}",
        f"Customers who ordered {u('before Eid ul-Fitr 2026')} but haven't ordered since",
        f"Customers who order for {u('Avurudu')} in at least {u('2 different years')}",
        "Which festivals do my customers order for?",
        f"Customers who ordered {u('last year')} but not {u('this year')}",
        f"Customers in {u('an area')}, sorted by {u('spend')}",
        f"Customers who first came from {u('Instagram')} {u('this year')}",
        f"Customers with a {u('birthday')} in the next {u('2 weeks')}",
        f"Customers who have spent more than {u('$500')} in total",
        f"Customers whose usual order is over {u('$100')}",
        f"Customers who {u('used')} a discount code {u('in the last 12 months')}",
        "Business customers (company name or work email), sorted by spend",
        "Customers who said yes to WhatsApp messages",
        "Customers who mostly order gifts",
        "Customers not seen in over a year",
        "How many customers do I have, and in which groups?",
        "How many new customers come back for a second order?",
        f"Where did new customers come from {u('this year')}, and did they order again?",
    ]),
    ("Sales", [
        f"Total sales {u('last month')}",
        f"Sales by {u('month')} {u('in the last 12 months')}",
        f"Compare {u('this month')} with {u('the same days last month')}",
        f"My best {u('10')} days {u('this year')}",
        f"Which day of the week sells most {u('in the last 90 days')}",
        f"What time of day people order {u('in the last 90 days')}",
        f"Sales by delivery area {u('last month')}",
        f"Sales by where orders came from {u('this year')}",
        f"Sales from new vs returning customers {u('this year')}",
        f"Sales by occasion {u('in the last 12 months')}",
        f"Delivery vs pickup {u('this month')}",
        f"Orders with and without a discount code {u('in the last 6 months')}",
        f"Gift orders vs other orders {u('in the last 12 months')}",
    ]),
    ("Products", [
        f"Best-selling products {u('this month')}, by {u('sales')}",
        f"Slowest-selling products {u('in the last 90 days')}",
        f"How {u('a product')} sold, month by month, {u('in the last 12 months')}",
        f"What new customers buy first {u('in the last 12 months')}, and who comes back",
        f"What's bought together with {u('a product')} {u('in the last 12 months')}",
    ]),
    ("Marketing", [
        f"Meta ad results by {u('week')} {u('in the last 90 days')}",
        f"Meta ads next to my sales, month by month, {u('this year')}",
        f"Best posts by {u('reach')} {u('in the last 90 days')}",
    ]),
]
ask_lists = "".join(f'<h3>{g} ({len(qs)})</h3><ul class="sx-asklist">{"".join(qline(q) for q in qs)}</ul>' for g, qs in ASK_GROUPS)
ASK_COUNT = sum(len(qs) for _, qs in ASK_GROUPS)

PAGES.append(dict(
    path="/ask-loyalbase/",
    section="product",
    title="Ask Loyalbase: Questions About Your Store in Plain Words",
    nav="Ask Loyalbase",
    description=f"Ask about your customers, sales, products or ads in plain words and get an answer, a table or a customer list. {ASK_COUNT} ready-made questions, no AI needed.",
    eyebrow="New in Loyalbase",
    h1="Ask your store questions in plain words",
    stand="Who ordered before Eid last year but not since? Which day sells most? What do new customers buy first? Type it the way you'd say it, and get the answer from your own orders.",
    answer=f"Ask Loyalbase lets a store owner type a question in plain words, or pick one of {ASK_COUNT} ready-made questions, and get an answer from the store's own orders: a sentence, a table, or a list of customers ready to message. Every underlined word can be changed: dates, festivals, products, areas, amounts. The ready-made questions run without AI. Where AI answers are switched on, the AI only sees totals and product names, never customer names, phone numbers or emails.",
    body=f'''
<h2>How it works</h2>
<ol class="sx-steps">
<li><b>Type a question, or pick one.</b> "who bought before christmas but didn't come back" works. So does "best days last month".</li>
<li><b>Check the underlined words.</b> Loyalbase fills in the dates, festivals, products, areas and amounts it heard. Tap any of them to change it. Blanks start filled with your own top product, area and channel.</li>
<li><b>Get the answer.</b> A plain sentence first, then a table or a list of customers.</li>
<li><b>Act on it.</b> Customer lists open like any other list: tap to WhatsApp one person, or download the list as a WhatsApp campaign file or a spreadsheet. Only people who said yes are included in downloads.</li>
</ol>

{ask(f"Customers who ordered {u('before Eid ul-Fitr 2026')} but haven't ordered since",
     "96 customers ordered in the 3 weeks before Eid ul-Fitr 2026 and haven't ordered since. They spent $8,450 then. 61 said yes to WhatsApp messages.",
     ["Customer", "Eid order", "Orders ever"], [["Aisha N.", "$140", "4"], ["Omar K.", "$95", "1"], ["Fatima R.", "$210", "6"]])}

<h2>Every question you can ask</h2>
<p>{ASK_COUNT} ready-made questions across customers, sales, products and marketing. The underlined words are examples. Change them to anything that fits your shop.</p>
{ask_lists}

<h2>Festivals understood</h2>
<p>Type a festival and Ask knows its dates, including moon-calendar festivals that move every year: Valentine's Day, Women's Day, Avurudu, Mother's Day, Father's Day, Children's Day, Ramadan, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali, Thai Pongal, 11.11, Black Friday, Christmas and New Year's Eve. "Before Christmas" means the weeks when people order for it, not just the day itself. You can also pick your own dates.</p>
<p>Customers are also grouped by the festivals they order for, year by year, so you can find people who order for Eid or Christmas every year. <a href="/guides/festival-customers/">How festival groups work →</a></p>

<h2>What stays private</h2>
<div class="sx-cols">
<div class="sx-card sx-card-good"><h3>What answers use</h3><ul><li>Order totals, counts and dates</li><li>Your product names</li><li>Delivery areas and where orders came from</li><li>Your own post captions, for marketing questions</li></ul></div>
<div class="sx-card sx-card-bad"><h3>What the AI never sees</h3><ul><li>Customer names</li><li>Phone numbers and emails</li><li>Addresses</li><li>Order numbers</li></ul></div>
</div>
<p>When a question finds customers, the list goes straight to your screen, and names load from your store in your browser, the same as everywhere else in Loyalbase. Where AI answers are switched on, the AI is told only how many customers matched and their totals.</p>
{cta("Ask your own store a question")}
''',
    faqs=[
        ("Do I need AI to use Ask?", f"No. The {ASK_COUNT} ready-made questions run straight on your numbers without AI. You type or pick a question, and Loyalbase matches it and fills in the details from your words."),
        ("What if my question isn't on the list?", "Pick the closest one and change the underlined words. Where AI answers are switched on, you can also ask anything else in your own words."),
        ("Can I send a message to the customers in an answer?", "Yes. A customer answer is a normal Loyalbase list. Tap to WhatsApp one person, or download it as a WhatsApp campaign file or spreadsheet with only people who said yes."),
        ("Does Ask work with my Meta ads and posts?", "Yes, once Facebook is connected. Ask for Meta ad results by week or month, ads next to your sales, or your best posts by reach, likes or comments."),
        ("Is it in other languages?", "Questions are in English today. Festival names like Avurudu, Eid, Vesak and Deepavali are understood, including common spellings."),
    ],
    related=["/guides/festival-customers/", "/industries/", "/woocommerce-customer-retention/"],
    schema="product",
))


# ------------------------------------------------------------------ Festival guide
FEST_ROWS = [
    ["Christmas", "15 days before, up to the day", "4 weeks before"],
    ["Avurudu", "13 days before to 1 day after", "3 weeks before"],
    ["Eid ul-Fitr", "10 days before to 1 day after", "3 weeks before"],
    ["Eid ul-Adha (Hajj)", "7 days before to 1 day after", "2 weeks before"],
    ["Vesak", "7 days before to 1 day after", "2 weeks before"],
    ["Deepavali", "10 days before, up to the day", "3 weeks before"],
    ["Thai Pongal", "6 days before to 1 day after", "10 days before"],
]
PAGES.append(dict(
    path="/guides/festival-customers/",
    section="guides",
    title="Find Customers Who Order Every Eid, Avurudu or Christmas | Loyalbase",
    nav="Festival customers",
    description="A simple way to find customers who order for the same festival every year, when to message them, and what to say. With a spreadsheet method and ready messages.",
    eyebrow="Guide",
    h1="How to find customers who order for the same festival every year",
    stand="Your Eid regulars, Christmas regulars and Avurudu regulars are already in your order history. Here's how to find them, and when to reach them.",
    answer="Pick a short ordering window for each festival, for example the 10 days before Eid ul-Fitr. Tag every order that falls in that window, year by year, and leave out days that fall in two festivals' windows. Customers with orders in the window in two or more different years are your festival regulars. Message them about three weeks before the festival, before they start shopping around. Loyalbase does this automatically for Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali and Thai Pongal.",
    body=f'''
<h2>Why festival regulars are worth finding</h2>
<p>A festival buyer isn't a random shopper. Someone who bought from you before Eid two years running has a habit, and a reason that comes back every year. They're the easiest people to sell to next Eid, if you reach them before they start browsing.</p>
<p>The trouble is that festival orders hide inside normal sales. A customer who orders twice a year looks quiet most of the time. Unless you look by festival, you won't see the pattern.</p>

<h2>Step 1: choose a window for each festival</h2>
<p>People don't order on the day itself. They order in the days before. A window that's too wide catches ordinary orders. One that's too narrow misses early planners. These are the windows Loyalbase uses:</p>
{table(["Festival", "Orders that count", "When to message"], FEST_ROWS)}
<p class="sx-note">Eid, Vesak and Deepavali follow moon calendars and move every year, sometimes by a day either way. Use the dates announced for your country.</p>

<h2>Step 2: tag each order, year by year</h2>
<p>For each year, mark every order inside a festival's window with that festival. Some years, two festivals sit close together. Avurudu and Eid ul-Fitr can land in the same weeks. When a day falls inside two windows, don't count it for either. That way an order is never put down to the wrong festival.</p>

<h2>Step 3: find people with two or more years</h2>
<p>Count, for each customer and festival, how many different years they ordered in that window. One year might be a coincidence. Two or more is a habit. That's your list.</p>

<h3>Doing it in a spreadsheet</h3>
<ol class="sx-steps">
<li>Export your orders with the order date and the customer's phone or email.</li>
<li>Add a column for each festival. Mark it with the year when the order date is inside that year's window.</li>
<li>Clear the mark when the date is inside two festivals' windows.</li>
<li>Make a pivot table: customers down the side, festivals across the top, count of different years in the cells.</li>
<li>Filter for 2 or more.</li>
</ol>
<p class="sx-note">It works, but plan an afternoon, and redo it before every festival.</p>

<h3>Doing it in Loyalbase</h3>
<p>Open Ask and pick <b>Which festivals do my customers order for?</b> for the overview, or <b>Customers who order for <u>Eid ul-Fitr</u> in at least <u>2 years</u></b> for the list. Change the festival or the number of years with a tap. <a href="/ask-loyalbase/">See every question you can ask</a>.</p>
{ask("Which festivals do my customers order for?",
     "Christmas is your biggest festival: 412 customers ordered for it, 96 of them in at least two years. Avurudu is second with 288.",
     ["Festival", "Customers", "2+ years", "Last year's sales"], [["Christmas", "412", "96", "$21,400"], ["Avurudu", "288", "61", "$12,900"], ["Eid ul-Fitr", "203", "47", "$10,300"], ["Deepavali", "96", "18", "$4,100"]])}

<h2>What to send, and when</h2>
<p>Message festival regulars before the window opens, so you're the first shop they think of. About three weeks before is right for most festivals, four for Christmas, and longer for companies ordering gifts.</p>
{tpl("Festival regular", "#FCEBF3", "#8C2A5B", "The customer who orders every festival",
     "about three weeks before the festival, to customers who ordered for it in at least two years.",
     "Hi [Name]! You've ordered from us for [festival] the last two years, thank you. [Festival] is on [date] this year. Want us to get your order ready early? Orders before [cut-off] are guaranteed in time.\n[Shop name]",
     "It thanks them for a habit they may not have noticed, and gives a practical reason to order now.")}
{tpl("Lapsed festival buyer", "#F7E8E8", "#8F2D2D", "Last year's festival buyer who never came back",
     "three weeks before the festival, to people who ordered before it last year and haven't ordered since.",
     "Hi [Name], last [festival] you ordered from us. It's coming up again on [date]. Shall we help this year too? Here's what's new: [link]\n[Shop name]",
     "A light reminder of what they did last year, with something new to look at.")}
{cta("See your festival regulars in Loyalbase")}
''',
    faqs=[
        ("Which festivals does Loyalbase group customers by?", "Christmas, Avurudu, Eid ul-Fitr, Eid ul-Adha, Vesak, Deepavali and Thai Pongal. Ask also understands Valentine's Day, Women's Day, Mother's Day, Father's Day, Children's Day, Ramadan, 11.11, Black Friday and New Year's Eve as date ranges."),
        ("What if a customer orders in two festivals that overlap?", "Days that fall inside two festivals' windows in the same year count for neither, so an order is never counted for the wrong festival."),
        ("Is Ramadan a festival group?", "Ramadan is understood as a date range in Ask, so you can see who ordered during Ramadan or compare Ramadan sales year on year. The festival groups use Eid ul-Fitr."),
        ("How many years of orders do I need?", "Two festivals' worth to find regulars, one to find last year's buyers. Loyalbase reads your full order history when you connect, so most stores have several years on day one."),
    ],
    related=["/industries/fashion-and-clothing/", "/industries/bakeries-and-cake-shops/", "/whatsapp-messages-to-bring-back-customers/"],
    schema="article",
))
