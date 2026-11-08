#!/usr/bin/env python3
"""Extra Medium v12 — "Collage": B&W photography over flat color, animated.
Edit content here, run `python3 build.py`, commit the output."""
import pathlib, re
ROOT = pathlib.Path(__file__).parent

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'

ORG_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":["Organization","ProfessionalService"],"@id":"https://xmedium.co/#org",
"name":"Extra Medium","legalName":"Extra Medium LLC","url":"https://xmedium.co/",
"logo":"https://xmedium.co/assets/img/em-logo.png","email":"hello@xmedium.co",
"slogan":"We make businesses un-ignorable.",
"description":"Extra Medium is a founder-led marketing agency and fractional CMO practice based in Virginia Beach, Virginia — strategy, creative, growth and AI for clients from pre-launch startups to Fortune 100 brands — and the operator of Extra Medium Labs, which builds its own products including Magpie, the local creator marketing platform.",
"foundingLocation":"Virginia Beach, Virginia, US",
"address":{"@type":"PostalAddress","addressLocality":"Virginia Beach","addressRegion":"VA","addressCountry":"US"},
"geo":{"@type":"GeoCoordinates","latitude":36.852984,"longitude":-75.977418},
"areaServed":["Virginia Beach","Hampton Roads","Chicago","London","United States","United Kingdom"],
"founder":{"@id":"https://xmedium.co/#jeff"},
"sameAs":["https://www.linkedin.com/in/jeffrimmer"],
"makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":"Fractional CMO"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Growth Marketing"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Brand Strategy and Rebranding"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"AI Consulting and Automation"}},{"@type":"Offer","itemOffered":{"@type":"Service","name":"Product Launches and Go-To-Market"}}],
"knowsAbout":["Brand strategy","Rebranding","Growth marketing","Fractional CMO","Website design and development","Ecommerce and Shopify","Paid media","SEO and AI search optimization","AI consulting and automation","Go-to-market strategy","Product launches","Executive branding","Podcasts","Experiential marketing","Local creator marketing"]},
{"@type":"Person","@id":"https://xmedium.co/#jeff","name":"Jeff Rimmer","jobTitle":"Founder & Fractional CMO",
"worksFor":{"@id":"https://xmedium.co/#org"},"url":"https://xmedium.co/about/",
"description":"20+ years in marketing on every side of the table: digital strategy for media companies across four states, marketing leadership for large brands and Fortune 100 companies including influencer marketing at scale, and three startups founded.",
"sameAs":["https://www.linkedin.com/in/jeffrimmer"]},
{"@type":"WebSite","@id":"https://xmedium.co/#site","url":"https://xmedium.co/","name":"Extra Medium","publisher":{"@id":"https://xmedium.co/#org"},"inLanguage":"en-US"}
]}
</script>"""

def crumb_ld(items):
    lis = ",".join('{"@type":"ListItem","position":%d,"name":"%s","item":"https://xmedium.co%s"}' % (i + 1, n, u) for i, (n, u) in enumerate(items))
    return '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[' + lis + ']}</script>'

def head(title, desc, path, extra_ld=""):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Extra Medium LLC">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="https://xmedium.co{path}">
<meta name="geo.region" content="US-VA"><meta name="geo.placename" content="Virginia Beach">
<meta name="geo.position" content="36.852984;-75.977418"><meta name="ICBM" content="36.852984, -75.977418">
<meta property="og:type" content="website"><meta property="og:site_name" content="Extra Medium">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="https://xmedium.co{path}">
<meta property="og:image" content="https://xmedium.co/assets/img/og-collage.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://xmedium.co/assets/img/og-collage.jpg">
<meta name="theme-color" content="#f5f1ea">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/css/site.css?v=14">
{FONTS}
{ORG_LD}
{extra_ld}
</head><body>"""

def header(on=""):
    def cls(k): return ' class="on"' if on == k else ""
    return f"""<header class="site"><div class="wrap nav">
<a class="brand" href="/"><img src="/assets/img/em-logo.png" alt="Extra Medium logo"><span>extra medium<small>Studio &amp; Labs</small></span></a>
<nav class="main">
<a href="/work/"{cls('work')}>Work</a>
<a href="/services/"{cls('services')}>Studio</a>
<a href="/labs/"{cls('labs')}>Labs</a>
<a href="/about/"{cls('about')}>About</a>
<a href="/contact/" class="btn p small">Start a project</a>
</nav>
<button class="burger" aria-label="Open menu" aria-expanded="false">&#9776;</button>
</div></header>
<div class="menu" aria-hidden="true">
<button class="mclose" aria-label="Close menu">&#10005;</button>
<a class="mlink" style="transition-delay:.05s" href="/work/"><i>01</i>Work</a>
<a class="mlink" style="transition-delay:.12s" href="/services/"><i>02</i>Studio</a>
<a class="mlink" style="transition-delay:.19s" href="/labs/"><i>03</i>Labs</a>
<a class="mlink" style="transition-delay:.26s" href="/labs/magpie/"><i>04</i>Magpie</a>
<a class="mlink" style="transition-delay:.33s" href="/about/"><i>05</i>About</a>
<a class="mlink" style="transition-delay:.40s" href="/contact/"><i>06</i>Contact</a>
<div class="mfoot"><span>Virginia Beach <span class="vbclock">--:--</span> ET</span><a href="mailto:hello@xmedium.co">hello@xmedium.co</a><a href="https://www.linkedin.com/in/jeffrimmer">LinkedIn</a></div>
</div>"""

FOOTER = """<footer class="finale">
<div class="fin-cta-band"><div class="wrap">
<h2 class="rv">Start a <span class="it">conversation.</span></h2>
<p class="rv">A project, a bigger problem, or a marketing seat you need filled by someone senior. The first conversation is free and specific.</p>
<div class="cta-row rv"><a class="btn white" href="/contact/">Start a project</a><a class="btn ghost" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div>
<div class="fin-idea" id="ideaCap">
<div class="fin-idea-txt"><h3 class="fin-idea-h">The Extra Idea.</h3><p>One stolen-worthy business idea in your inbox, every week. Steal it, use it, watch it work.</p></div>
<form class="idea-form" name="extra-idea" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/?idea=1">
<p hidden><label>Don&rsquo;t fill this out: <input name="bot-field"></label></p>
<label class="idea-label" for="ideaEmail">Email for the weekly idea</label>
<div class="idea-row"><input id="ideaEmail" type="email" name="email" required placeholder="you@yourbusiness.com" autocomplete="email"><button class="btn ink" type="submit">Send me ideas</button></div>
<p class="idea-micro">One email a week. Unsubscribe anytime. No pitch decks, promise.</p>
</form>
</div>
</div></div>
<div class="fin-main"><div class="wrap">
<div class="fin-grid">
<div class="fin-brand"><a class="brand" href="/"><img src="/assets/img/em-logo.png" alt="Extra Medium logo"><span>extra medium<small>Studio &amp; Labs</small></span></a>
<p>A marketing agency and product lab. We build businesses people can&rsquo;t ignore &mdash; for clients, and for ourselves.</p></div>
<div><h4>Explore</h4><a href="/work/">Work</a><a href="/services/">Studio</a><a href="/labs/">Labs</a><a href="/about/">About</a><a href="/contact/">Contact</a></div>
<div><h4>Labs</h4><a href="/labs/magpie/">Magpie &mdash; flagship</a><a href="https://magpielocal.com">magpielocal.com</a><a href="/labs/">All ventures</a></div>
<div><h4>Connect</h4><a href="mailto:hello@xmedium.co">hello@xmedium.co</a><a href="https://www.linkedin.com/in/jeffrimmer">LinkedIn</a><a href="/contact/">Start a project</a></div>
</div>
<div class="fin-word" aria-hidden="true">extra medium.</div>
<div class="fin-base"><span>&copy; 2026 Extra Medium LLC &middot; Virginia Beach &middot; Chicago &middot; London</span><span class="fin-clock">Virginia Beach <span class="vbclock">--:--</span> ET</span><span>Magpie is a product of Extra Medium Labs.</span></div>
</div></div>
</footer>
<script src="/assets/js/site.js?v=14"></script></body></html>"""


import json as _json, os as _os
LAYERS = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "layers.json")))

def layers_fig(key, alt):
    m = LAYERS[key]
    parts = ['<figure class="frame bleed rv"><div class="layers" data-layers>']
    parts.append(f'<img class="lbg" src="/assets/img/{m["bg"]}" alt="" aria-hidden="true">')
    parts.append(f'<img class="lrest" src="/assets/img/{m["rest"]}" alt="" aria-hidden="true">')
    for i, pc in enumerate(m["pieces"]):
        a = alt if i == 0 else ""
        h = "" if i == 0 else ' aria-hidden="true"'
        parts.append(f'<img class="lp" src="/assets/img/{pc["file"]}" data-dx="{pc["dx"]}" data-dy="{pc["dy"]}" data-rot="{pc["rot"]}" alt="{a}"{h}>')
    parts.append("</div></figure>")
    return "".join(parts)

def page(title, desc, path, on, body, extra_ld=""):
    body = re.sub(r"\[\[layers:([a-z-]+)\|([^\]]*)\]\]", lambda m: layers_fig(m.group(1), m.group(2)), body)
    html = head(title, desc, path, extra_ld) + header(on) + body + FOOTER
    out = ROOT / (path.strip("/") + "/index.html" if path.strip("/") else "index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out)

CTA = """<section class="ctaband"><div class="wrap">
<p class="kick light rv">Let&rsquo;s talk</p><h2 class="rv">What are you trying to <span class="it">make happen?</span></h2>
<p class="rv">Don&rsquo;t know exactly what you need? Good. That&rsquo;s our job. Tell us where the business is headed and we&rsquo;ll tell you honestly whether we can help &mdash; and if we can&rsquo;t, who might.</p>
<div class="cta-row rv"><a class="btn white" href="/contact/">Start a conversation</a><a class="btn ghost" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div>
<p class="note rv" style="color:rgba(255,255,255,.85);margin-top:18px">Usually replies within one business day.</p></div></section>"""

MARQUEE = """<div class="marquee" aria-hidden="true"><div class="track"><span>Launch</span><i>&#10022;</i><span>Reinvent</span><i>&#10022;</i><span>Grow</span><i>&#10022;</i><span>Lead</span><i>&#10022;</i><span>Intelligence</span><i>&#10022;</i><span>Experiences</span><i>&#10022;</i><span>Launch</span><i>&#10022;</i><span>Reinvent</span><i>&#10022;</i><span>Grow</span><i>&#10022;</i><span>Lead</span><i>&#10022;</i><span>Intelligence</span><i>&#10022;</i><span>Experiences</span><i>&#10022;</i></div></div>"""

BADGE = """<svg class="badge-rot" viewBox="0 0 100 100" aria-hidden="true"><defs><path id="circ" d="M50,50 m-38,0 a38,38 0 1,1 76,0 a38,38 0 1,1 -76,0"/></defs><circle cx="50" cy="50" r="49" fill="#17130e"/><text fill="#f5f1ea" font-size="10.5" font-weight="700" letter-spacing="2.5"><textPath href="#circ">EXTRA MEDIUM &#8226; STUDIO &amp; LABS &#8226; </textPath></text><circle cx="50" cy="50" r="5" fill="#c2187a"/></svg>"""

# ============ HOMEPAGE ============
home = """
<section class="hero"><div class="wrap" style="position:relative">
<div class="dots"></div>
<p class="kick rv">A marketing agency &amp; product lab</p>
<h1 class="rv">We make businesses <span class="it">un&#8209;ignorable.</span></h1>
<p class="sub rv">Strategy, creative, growth and AI &mdash; plus <b>fractional CMO leadership</b> for companies that need a senior marketing brain without another executive seat. Senior-only. Founder-led.</p>
<div class="btns rv"><a class="btn p" href="/contact/">Start a project</a><a class="btn" href="/work/">See the work</a></div>
<div style="position:relative">
""" + BADGE + """
[[layers:collage-home|Black and white collage of a marble statue head merged with a bird, over a magenta field]]
</div>
<p class="def rv"><b>Extra Medium</b> is a founder-led marketing agency, fractional CMO practice and product lab in Virginia Beach, Virginia. We launch, reinvent and grow businesses &mdash; brand, creative, growth and technology under one roof &mdash; and through Extra Medium Labs we build and operate our own products, led by Magpie, the local creator marketing platform.</p>
<div class="facts rv"><span>20+ years, every side of the table</span><span>Virginia Beach &middot; Chicago &middot; London</span><span>Clients: startups to Fortune 100</span></div>
</div></section>
""" + MARQUEE + """
<section><div class="wrap">
<div class="sec-head rv"><h2>What we <span class="it">do</span></h2><span class="mono">The agency</span></div>
<div class="idxrow rv"><div class="num">01</div><div><div class="sq" style="background:var(--mag)"></div><h3>Launch</h3><p>Positioning, naming, brand identity, website and go-to-market for things that don&rsquo;t exist yet &mdash; shaped as one arc.</p></div><img class="thumb" src="/assets/img/img-launch.jpg" alt="A rocket launching at night over a beach crowd" loading="lazy"></div>
<div class="idxrow rv"><div class="num">02</div><div><div class="sq" style="background:var(--blue)"></div><h3>Reinvent</h3><p>Brand strategy, rebranding and website redesign that close the gap between what your business became and what the market still thinks it is.</p></div><img class="thumb" src="/assets/img/img-reinvent.jpg" alt="Hands reworking a plan across a laptop and an open notebook" loading="lazy"></div>
<div class="idxrow rv"><div class="num">03</div><div><div class="sq" style="background:var(--teal)"></div><h3>Grow</h3><p>Paid media, SEO &amp; AI search, ecommerce, lifecycle and creator channels &mdash; run as one system against revenue, with an owner.</p></div><img class="thumb" src="/assets/img/img-grow.jpg" alt="A strategy table from above — laptops, tablets and live numbers" loading="lazy"></div>
<div class="idxrow rv"><div class="num">04</div><div><div class="sq" style="background:var(--yel)"></div><h3>Lead <em>&mdash; fractional CMO</em></h3><p>Senior marketing leadership, embedded in your business, without another permanent executive seat.</p></div><img class="thumb" src="/assets/img/img-lead.jpg" alt="A founder, arms crossed, smiling at the camera" loading="lazy"></div>
<div class="idxrow rv"><div class="num">05</div><div><div class="sq" style="background:var(--mag)"></div><h3>Intelligence</h3><p>AI consulting, agents and automation wired into how the company actually operates &mdash; marketing, reporting, creative, workflow.</p></div><img class="thumb" src="/assets/img/img-intelligence.jpg" alt="A robotic hand reaching into a network of light" loading="lazy"></div>
<div class="idxrow rv"><div class="num">06</div><div><div class="sq" style="background:var(--blue)"></div><h3>Experiences</h3><p>Podcasts, events and experiential marketing &mdash; the things people are still talking about a year later.</p></div><img class="thumb" src="/assets/img/img-experiences.jpg" alt="A studio podcast microphone in dramatic light" loading="lazy"></div>
</div></section>
<section class="cmo"><div class="wrap">
[[layers:collage-cmo|Black and white collage of a vintage microphone and a hand tuning a retro television, over deep teal]]
<h2 class="rv">A CMO, <span class="it">fractionally.</span></h2>
<p class="rv">Most growing companies don&rsquo;t need another executive seat. They need a senior marketing brain in the room &mdash; owning the strategy, directing the team and the agencies, and answering for the number. That&rsquo;s the Lead practice, and it&rsquo;s led personally by our founder.</p>
<ul>
<li class="rv">Owns the marketing strategy end to end</li>
<li class="rv">Directs your team, freelancers and agencies</li>
<li class="rv">Reports at board level, in plain numbers</li>
</ul>
<div class="cta-row rv"><a class="btn white" href="/services/#lead">How fractional leadership works</a></div>
</div></section>
<section><div class="wrap">
<div class="sec-head rv"><h2>Selected <span class="it">work</span></h2><span class="mono">Proof</span></div>
<p class="lede rv" style="margin-bottom:8px">Some clients prefer not to be named, and fractional work belongs to the client &mdash; so stories are told without logos, with the details that matter. Ask us about any of it.</p>
<div class="work-row rv"><img src="/assets/img/img-grow.jpg" alt="A strategy table from above — laptops, tablets and live numbers" loading="lazy"><div><span class="tag">Growth system</span><h3>The consumer brand that needed a growth system, not more ads</h3><p>Growth became a system with an owner, not a pile of campaigns.</p></div></div>
<div class="work-row rv"><img src="/assets/img/img-reinvent.jpg" alt="Hands reworking a plan across a laptop and an open notebook" loading="lazy"><div><span class="tag">Reinvention</span><h3>The manufacturer that had to become one brand</h3><p>One brand, one digital foundation, international expansion supported.</p></div></div>
<div class="work-row rv"><img src="/assets/img/img-launch.jpg" alt="A rocket launching at night over a beach crowd" loading="lazy"><div><span class="tag">Our own launch</span><h3>The platform we launched ourselves</h3><p>Seed funding to 900,000 users. Magpie is us doing it again, in public.</p></div></div>
<div class="cta-row rv"><a class="btn" href="/work/">All the work &rarr;</a></div>
</div></section>
<section class="magsec"><div class="wrap">
[[layers:collage-labs|Black and white collage of a bird perched on a marble statue head beside a vintage camera, over electric blue]]
<img class="logo rv" src="/assets/img/magpie-logo.png" alt="Magpie">
<p class="lede rv">From Extra Medium Labs: local businesses comp or pay creators who actually live in their city to visit and post honestly &mdash; and every visit is tracked. 500 followers is enough when they&rsquo;re the right 500.</p>
<div class="trio rv"><img src="/assets/img/sample-portrait-sofia.jpg" alt="A Magpie creator" loading="lazy"><img src="/assets/img/sample-portrait-jordan.jpg" alt="A Magpie creator" loading="lazy"><img src="/assets/img/sample-portrait-priya.jpg" alt="A Magpie creator" loading="lazy"></div>
<div class="mstats rv"><div><b><span data-count="45">45</span></b><span>Founding markets</span></div><div><b><span data-count="13">13</span></b><span>Countries</span></div><div><b><span data-count="500">500</span></b><span>Followers is enough</span></div></div>
<div class="cta-row rv"><a class="btn white" href="/labs/magpie/">The Magpie story</a><a class="btn ghost" href="https://magpielocal.com">Visit magpielocal.com</a></div>
<p class="note rv" style="color:rgba(245,241,234,.65);margin-top:22px">Why lead with our own product? Because a studio that launches its own thing &mdash; brand, platform, pricing, go-to-market, operations &mdash; gives different advice than one that only sells launches. <a href="/labs/" style="color:#fff">More from Labs &rarr;</a></p>
</div></section>
<section><div class="wrap">
<div class="sec-head rv"><h2>The <span class="it">founder</span></h2><span class="mono">About</span></div>
<div class="jeff rv"><img src="/assets/img/jeff-rimmer.jpg" alt="Jeff Rimmer, founder of Extra Medium"><div><h3>Jeff Rimmer</h3><p class="role">Founder &amp; principal</p><p>I&rsquo;ve spent 2 decades in local media and startups, and most recently I&rsquo;ve been leading marketing for large brands and Fortune 100 companies, including influencer marketing at scale.</p></div></div>
<div class="cta-row rv"><a class="btn" href="/about/">The longer version &rarr;</a></div>
<div class="sec-head rv" style="margin-top:44px"><h2>Asked, <span class="it">answered.</span></h2><span class="mono">Straight answers</span></div>
<div class="faq">
<details class="rv"><summary>What does Extra Medium do?</summary><p>Extra Medium is a marketing agency and fractional CMO practice based in Virginia Beach, Virginia. We launch new businesses and products, reinvent brands that have outgrown their look, and run growth systems &mdash; paid media, search, creators and AI &mdash; measured against revenue, not vanity metrics.</p></details>
<details class="rv"><summary>What is a fractional CMO?</summary><p>A fractional CMO is a senior marketing executive who leads your marketing part-time &mdash; owning strategy, directing your team and agencies, and reporting results &mdash; without the cost of a permanent executive seat. Extra Medium&rsquo;s fractional CMO engagements are led personally by founder Jeff Rimmer.</p></details>
<details class="rv"><summary>What is Extra Medium Labs?</summary><p>Extra Medium Labs is where the studio builds and operates its own products instead of only advising clients. Its flagship is Magpie, a local creator marketing platform live in 45 founding markets across 13 countries, where local businesses comp or pay local creators to visit and post honestly, with every visit tracked.</p></details>
<details class="rv"><summary>Who does Extra Medium work with?</summary><p>Founder-led and high-growth companies, pre-launch startups, manufacturers, consumer brands and established enterprises up to Fortune 100 scale &mdash; across consumer products, ecommerce, healthcare, retail, media, music, hospitality, professional services and SaaS. The common thread is ambition, not industry.</p></details>
<details class="rv"><summary>How does an engagement start?</summary><p>With a conversation, not a proposal. Engagements take three shapes: fractional CMO leadership, a defined project such as a launch or rebrand, or ongoing growth work. If we are not the right fit, we say so &mdash; and usually know who is.</p></details>
</div>
</div></section>
"""

FAQ_HOME_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What does Extra Medium do?","acceptedAnswer":{"@type":"Answer","text":"Extra Medium is a marketing agency and fractional CMO practice based in Virginia Beach, Virginia. We launch new businesses and products, reinvent brands that have outgrown their look, and run growth systems — paid media, search, creators and AI — measured against revenue, not vanity metrics."}},
{"@type":"Question","name":"What is a fractional CMO?","acceptedAnswer":{"@type":"Answer","text":"A fractional CMO is a senior marketing executive who leads your marketing part-time — owning strategy, directing your team and agencies, and reporting results — without the cost of a permanent executive seat. Extra Medium's fractional CMO engagements are led personally by founder Jeff Rimmer."}},
{"@type":"Question","name":"What is Extra Medium Labs?","acceptedAnswer":{"@type":"Answer","text":"Extra Medium Labs is where the studio builds and operates its own products instead of only advising clients. Its flagship is Magpie, a local creator marketing platform live in 45 founding markets across 13 countries, where local businesses comp or pay local creators to visit and post honestly, with every visit tracked."}},
{"@type":"Question","name":"Who does Extra Medium work with?","acceptedAnswer":{"@type":"Answer","text":"Founder-led and high-growth companies, pre-launch startups, manufacturers, consumer brands and established enterprises up to Fortune 100 scale, across consumer products, ecommerce, healthcare, retail, media, music, hospitality, professional services and SaaS."}},
{"@type":"Question","name":"How does an engagement start?","acceptedAnswer":{"@type":"Answer","text":"With a conversation, not a proposal. Engagements take three shapes: fractional CMO leadership, a defined project such as a launch or rebrand, or ongoing growth work."}}]}
</script>"""

page("Extra Medium | Marketing Agency & Fractional CMO in Virginia Beach",
     "Extra Medium is a founder-led marketing agency and fractional CMO practice in Virginia Beach: strategy, creative, growth and AI for startups to Fortune 100 brands — plus Extra Medium Labs, home of Magpie.",
     "/", "home", home, FAQ_HOME_LD)
print("home done")

# ============ WORK ============
work = """
<section class="phero"><div class="wrap">
<p class="kick rv">Work</p>
<h1 class="rv">Done from <span class="it">both sides</span> of the table.</h1>
<p class="lede rv">Built brands from inside the building. Built companies from nothing. Sat across from agencies, founders and executive teams. We know what good advice looks like &mdash; and what survives Monday morning.</p>
[[layers:collage-work|Black and white collage of chess pieces, a pointing hand and a telescope, over a sunny yellow field]]
</div></section>
<section><div class="wrap">
<div class="receipt rv" aria-label="How we have worked">
<span class="stamp">Operator first, advisor second.</span>
<span class="stamp">Fortune 100 to pre-launch, same standard.</span>
<span class="stamp">Names on request. Receipts below.</span>
</div>
<div class="sec-head rv" style="margin-top:52px"><h2>Client <span class="it">stories</span></h2><span class="mono">The receipts</span></div>
<div class="story rv"><img src="/assets/img/img-grow.jpg" alt="A strategy table from above — laptops, tablets and live numbers" loading="lazy"><div><span class="tag">Growth</span><h3>The consumer brand that needed a growth system, not more ads</h3><p>A high-growth nutritional supplement brand had traction and a scattered set of channels. We took ownership of strategy end to end: investment across Google, Meta, affiliate, influencer, creator, UGC, Reddit and AI-driven channels; creator and affiliate programs built into real acquisition channels; AI across reporting, creative and workflow. <b>Growth became a system with an owner.</b></p></div></div>
<div class="story rv"><img src="/assets/img/img-reinvent.jpg" alt="Hands reworking a plan across a laptop and an open notebook" loading="lazy"><div><span class="tag">Reinvention</span><h3>The manufacturer that had to become one brand after an acquisition</h3><p>A global radiation protection manufacturer needed global marketing strategy across website, CRM, automation, ecommerce, SEO, paid media and product marketing, plus post-acquisition brand integration. We built the digital foundation, a physician-facing podcast, KOL and education programs, and supported product launches and international expansion.</p></div></div>
<div class="story rv"><img src="/assets/img/img-skyline.jpg" alt="A city skyline — the markets our clients play in" loading="lazy"><div><span class="tag">Scale</span><h3>The Fortune 500 retailer whose websites and apps had to work harder</h3><p>Leading planning, execution and optimization for the websites and apps of three retail banners &mdash; ecommerce, mobile, merchandising, loyalty and seasonal campaigns for millions of customers. <b>Improvements to average order value, engagement, mobile installs and SEO</b> from content strategy, technical optimization and continuous testing.</p></div></div>
<div class="story rv"><img src="/assets/img/img-experiences.jpg" alt="A studio podcast microphone in dramatic light" loading="lazy"><div><span class="tag">New revenue</span><h3>The music company whose next chapter was enterprise</h3><p>A subscription music-licensing business needed a new revenue model. We helped launch its enterprise licensing product, shaped go-to-market with product, engineering and sales leadership, and onboarded early enterprise adopters <b>including Microsoft and Baylor University</b>.</p></div></div>
<div class="story rv"><img src="/assets/img/img-launch.jpg" alt="A rocket launching at night over a beach crowd" loading="lazy"><div><span class="tag">Launch</span><h3>The platform we launched ourselves</h3><p>Before Extra Medium, our founder created a digital music platform from idea to launch &mdash; raised seed funding, built the team, onboarded artists and led the marketing that <b>grew it past 900,000 users</b>.</p></div></div>
<div class="story rv"><img src="/assets/img/img-team.jpg" alt="A team working around a table beneath a sticky-note board" loading="lazy"><div><span class="tag">Build</span><h3>The B2B division that needed to exist</h3><p>A contract manufacturer wanted to sell a new idea: helping major brands in hospitality, travel, food and beverage, fitness and retail create wellness products under their own names. We built the positioning and website for the division as <b>the invisible engine behind other brands</b>, with clear industry pages and a focused path to partnership.</p></div></div>
<div class="sec-head block rv" style="margin-top:52px"><p class="kick">The range</p><h2 style="margin-top:14px">From a napkin sketch to a <span class="it">Fortune 100 partner.</span></h2>
<p class="lede">Pre-launch startups. Founder-led growth brands. Makers and manufacturers. Fortune 500 retail. Industries: consumer products, ecommerce, healthcare and medical devices, retail, media and broadcast, music and entertainment, hospitality, professional services, technology and SaaS. The thread is ambition, not industry.</p></div>
</div></section>
""" + CTA

page("Work: From Startups to Fortune 100 | Extra Medium",
     "Extra Medium case stories: growth systems, brand reinvention, enterprise launches and our own products, from pre-launch startups to Fortune 100 partners.",
     "/work/", "work", work, crumb_ld([("Home", "/"), ("Work", "/work/")]))
print("work done")

# ============ SERVICES ============
services = """
<section class="phero"><div class="wrap">
<p class="kick rv">The studio</p>
<h1 class="rv">Whatever the medium. <span class="it">Make it matter.</span></h1>
<p class="lede rv">We do the right thing, in order. Strategy, creative, growth and technology, practiced together by one small senior team.</p>
[[layers:collage-cmo|Black and white collage of a vintage microphone and a hand tuning a retro television, over deep teal]]
</div></section>
<section><div class="wrap">
<div class="sec-head rv"><h2>Six <span class="it">chapters</span></h2><span class="mono">Services</span></div>
<div class="idxrow rv" id="launch"><div class="num">01</div><div><div class="sq" style="background:var(--mag)"></div><h3>Launch</h3><p>For things that don&rsquo;t exist yet, or haven&rsquo;t been introduced properly. Positioning, naming, brand identity, website, go-to-market and product launch &mdash; shaped as one arc, because launching something nobody has searched for yet is a different sport.</p></div><img class="thumb" src="/assets/img/img-launch.jpg" alt="A rocket launching at night over a beach crowd" loading="lazy"></div>
<div class="idxrow rv" id="reinvent"><div class="num">02</div><div><div class="sq" style="background:var(--blue)"></div><h3>Reinvent</h3><p>For businesses that moved faster than their brand. Brand strategy, rebranding, messaging and website redesign that close the gap between what the business became and what the market still thinks it is &mdash; without starting from zero.</p></div><img class="thumb" src="/assets/img/img-reinvent.jpg" alt="Hands reworking a plan across a laptop and an open notebook" loading="lazy"></div>
<div class="idxrow rv" id="grow"><div class="num">03</div><div><div class="sq" style="background:var(--teal)"></div><h3>Grow</h3><p>Growth marketing with an owner. Paid media, SEO and AI search, ecommerce and Shopify growth, lifecycle and creator channels &mdash; run as one system against revenue, not separate campaigns reporting vanity numbers.</p></div><img class="thumb" src="/assets/img/img-grow.jpg" alt="A strategy table from above — laptops, tablets and live numbers" loading="lazy"></div>
<div class="idxrow rv" id="lead"><div class="num">04</div><div><div class="sq" style="background:var(--yel)"></div><h3>Lead <em>&mdash; fractional CMO</em></h3><p>Fractional CMO leadership for businesses that need a senior marketing brain without another permanent executive seat. Plus executive and personal branding for the founders and physicians leading them.</p></div><img class="thumb" src="/assets/img/img-lead.jpg" alt="A founder, arms crossed, smiling at the camera" loading="lazy"></div>
<div class="idxrow rv" id="intelligence"><div class="num">05</div><div><div class="sq" style="background:var(--mag)"></div><h3>Intelligence</h3><p>AI consulting, AI agents and automation that connect how a company actually operates &mdash; not another unused tool. Applied AI across marketing, reporting, creative development and workflow, wired into the business instead of demoed at it.</p></div><img class="thumb" src="/assets/img/img-intelligence.jpg" alt="A robotic hand reaching into a network of light" loading="lazy"></div>
<div class="idxrow rv" id="experiences"><div class="num">06</div><div><div class="sq" style="background:var(--blue)"></div><h3>Experiences</h3><p>Podcasts, events and experiential marketing &mdash; the things people are still talking about a year later. Strategy and production for shows and moments that build a reputation, not just reach.</p></div><img class="thumb" src="/assets/img/img-experiences.jpg" alt="A studio podcast microphone in dramatic light" loading="lazy"></div>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">How engagements work</p><h2 style="margin-top:14px">No giant <span class="it">process.</span></h2>
<p class="lede">You tell us what&rsquo;s going on. We ask questions. We figure out whether we can actually help. If we can, we tell you what the right engagement looks like. If we can&rsquo;t, we tell you that too.</p></div>
<div class="grid3" style="margin-top:26px">
<div class="card rv"><span class="num">Shape 01</span><h3>Fractional leadership</h3><p>Senior marketing leadership, embedded, without adding a permanent executive seat. For founder-led and high-growth companies.</p></div>
<div class="card rv" style="transition-delay:.08s"><span class="num">Shape 02</span><h3>Project</h3><p>A defined problem, launch or build with a clear beginning and end &mdash; scoped after the first conversation, priced with a clear range.</p></div>
<div class="card rv" style="transition-delay:.16s"><span class="num">Shape 03</span><h3>Ongoing growth</h3><p>Continuous senior thinking and execution around growth, brand and performance. One owner, one system.</p></div>
</div>
<p class="note rv" style="margin-top:26px">Full capability list: brand strategy &middot; rebranding &middot; growth marketing &middot; fractional CMO &middot; website design &amp; development &middot; ecommerce &amp; Shopify &middot; paid media &middot; SEO &amp; AI search &middot; AI consulting, agents &amp; automation &middot; go-to-market &middot; product launches &middot; executive branding &middot; podcasts &middot; experiential.</p>
</div></section>
<section><div class="wrap">
<div class="sec-head rv"><h2>Before you <span class="it">ask.</span></h2><span class="mono">Studio questions</span></div>
<div class="faq">
<details class="rv"><summary>How much does it cost to work with Extra Medium?</summary><p>It depends on the shape. Fractional leadership is a monthly engagement, projects are scoped with a clear price range after the first conversation, and ongoing growth work is a monthly system with one owner. We do not publish a rate card because the honest price follows the actual problem &mdash; the first conversation is free and specific.</p></details>
<details class="rv"><summary>How fast can a launch or rebrand ship?</summary><p>Focused launches and rebrands typically run in weeks, not quarters, because one senior team owns strategy, creative and build together with no handoffs. Exact timing is set in the first conversation once the destination is clear.</p></details>
<details class="rv"><summary>Do you only work with Virginia Beach companies?</summary><p>No. Extra Medium is headquartered in Virginia Beach, Virginia, with presence in Chicago and London, and clients across the US and UK. Most engagements run remotely with in-person time when it matters.</p></details>
<details class="rv"><summary>What makes you different from a typical agency?</summary><p>Three things: every engagement is led personally by the founder; the team is senior-only with no account-manager telephone game; and the studio builds its own products in Extra Medium Labs &mdash; led by Magpie &mdash; so its advice is tested on its own money first.</p></details>
</div>
</div></section>
""" + CTA

SERVICES_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ItemList","name":"Extra Medium studio services","itemListElement":[
{"@type":"Service","position":1,"name":"Launch","provider":{"@id":"https://xmedium.co/#org"},"description":"Positioning, naming, brand identity, website and go-to-market for new businesses and products.","url":"https://xmedium.co/services/#launch"},
{"@type":"Service","position":2,"name":"Reinvent","provider":{"@id":"https://xmedium.co/#org"},"description":"Brand strategy, rebranding, messaging and website redesign for businesses that outgrew their brand.","url":"https://xmedium.co/services/#reinvent"},
{"@type":"Service","position":3,"name":"Grow","provider":{"@id":"https://xmedium.co/#org"},"description":"Growth marketing run as one system: paid media, SEO and AI search, ecommerce, lifecycle and creator channels.","url":"https://xmedium.co/services/#grow"},
{"@type":"Service","position":4,"name":"Lead — Fractional CMO","provider":{"@id":"https://xmedium.co/#org"},"description":"Fractional CMO leadership and executive branding for founder-led and high-growth companies.","url":"https://xmedium.co/services/#lead"},
{"@type":"Service","position":5,"name":"Intelligence — AI consulting","provider":{"@id":"https://xmedium.co/#org"},"description":"AI consulting, agents and automation wired into how a company actually operates.","url":"https://xmedium.co/services/#intelligence"},
{"@type":"Service","position":6,"name":"Experiences","provider":{"@id":"https://xmedium.co/#org"},"description":"Podcasts, events and experiential marketing that build reputation, not just reach.","url":"https://xmedium.co/services/#experiences"}]}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does it cost to work with Extra Medium?","acceptedAnswer":{"@type":"Answer","text":"It depends on the shape. Fractional leadership is a monthly engagement, projects are scoped with a clear price range after the first conversation, and ongoing growth work is a monthly system with one owner. We do not publish a rate card because the honest price follows the actual problem — the first conversation is free and specific."}},
{"@type":"Question","name":"How fast can a launch or rebrand ship?","acceptedAnswer":{"@type":"Answer","text":"Focused launches and rebrands typically run in weeks, not quarters, because one senior team owns strategy, creative and build together with no handoffs. Exact timing is set in the first conversation once the destination is clear."}},
{"@type":"Question","name":"Do you only work with Virginia Beach companies?","acceptedAnswer":{"@type":"Answer","text":"No. Extra Medium is headquartered in Virginia Beach, Virginia, with presence in Chicago and London, and clients across the US and UK. Most engagements run remotely with in-person time when it matters."}},
{"@type":"Question","name":"What makes you different from a typical agency?","acceptedAnswer":{"@type":"Answer","text":"Three things: every engagement is led personally by the founder; the team is senior-only with no account-manager telephone game; and the studio builds its own products in Extra Medium Labs — led by Magpie — so its advice is tested on its own money first."}}]}
</script>""" + crumb_ld([("Home", "/"), ("Studio", "/services/")])

page("Studio: Launch, Reinvent, Grow, Lead | Extra Medium",
     "Extra Medium studio services: launch, reinvention, growth marketing, fractional CMO leadership, AI and experiences — one senior team, three engagement shapes.",
     "/services/", "services", services, SERVICES_LD)
print("services done")

# ============ LABS ============
labs = """
<section class="phero"><div class="wrap">
<p class="kick rv">Extra Medium Labs</p>
<h1 class="rv">Things we build when <span class="it">nobody hired us to.</span></h1>
<p class="lede rv">Labs is where the studio puts its own money where its advice is. One flagship product, live and operating. A small number of ventures behind it. Nothing else &mdash; a flagship only means something if most things aren&rsquo;t one.</p>
[[layers:collage-labs|Black and white collage of a bird perched on a marble statue head beside a vintage camera, over electric blue]]
</div></section>
<section><div class="wrap">
<div class="receipt rv" aria-label="Why Labs exists">
<span class="stamp">Advice is cheap.</span>
<span class="stamp">So we built the thing.</span>
<span class="stamp">Now we run it.</span>
</div>
<div class="flagship rv"><div class="flagship-grid">
<div class="flagship-copy"><span class="badge">Flagship &middot; Live</span>
<img class="logo" src="/assets/img/magpie-logo.png" alt="Magpie">
<h3 style="font-size:1.8rem;line-height:1.08">Local creator marketing, city by city.</h3>
<p>Influencer marketing skipped local. The creators who move a neighborhood business live there &mdash; and 500 local followers beat 500,000 strangers. A business makes an offer, a creator visits, posts honestly within 48 hours, and every visit is tracked down to register spend.</p>
<div class="stats"><div><b><span data-count="45">45</span></b><span>Founding markets</span></div><div><b><span data-count="13">13</span></b><span>Countries</span></div><div><b><span data-count="500">500</span></b><span>Followers is enough</span></div></div>
<div class="cta-row"><a class="btn p" href="/labs/magpie/">The full case study</a><a class="btn" href="https://magpielocal.com">magpielocal.com</a></div></div>
<div class="flagship-media"><img src="/assets/img/table-phone-photo.jpg" alt="A creator photographing a dish at a local restaurant table"></div>
</div></div>
<p class="note rv" style="margin-top:22px">Status, honestly: live platform, founding rosters forming market by market, home market Virginia Beach activating first. Operated by Extra Medium LLC. Pricing, standards and the Visit Guarantee are published on the product site &mdash; because that&rsquo;s how products should behave.</p>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">In development</p><h2 style="margin-top:14px">The next <span class="it">bench.</span></h2>
<p class="lede">Three ventures in active development. Everything else we&rsquo;ve explored has been archived off this page &mdash; focus is a feature.</p></div>
<div class="grid3" style="margin-top:26px">
<div class="card rv"><span class="num">01 &middot; Prototype &middot; Waitlist open</span><h3>Roon</h3><p>The days you&rsquo;d give anything to have back. A memory-keeping app that turns the photos, videos and voice notes a family already has into stories you can step back into &mdash; because storage isn&rsquo;t the problem. Meaning is.</p><span class="arrow"><a href="https://roonapp.co" style="text-decoration:none;color:inherit">roonapp.co &rarr;</a></span></div>
<div class="card rv" style="transition-delay:.08s"><span class="num">02 &middot; In development</span><h3>JAWNRA</h3><p>The world&rsquo;s music, in motion. A global music discovery and chart platform that measures momentum instead of popularity &mdash; the chart that tells you what&rsquo;s about to win, not what already did.</p><span class="arrow"><a href="https://jawnra.com" style="text-decoration:none;color:inherit">jawnra.com &rarr;</a></span></div>
<div class="card rv" style="transition-delay:.16s"><span class="num">03 &middot; In development</span><h3>hapsta</h3><p>Make something happen. An AI engine for spontaneous real life: tell it what you&rsquo;re looking for and get a Happening &mdash; people, place, activity, time. Software that gets you off the phone and into a room.</p><span class="arrow"><a href="https://hapsta.co" style="text-decoration:none;color:inherit">hapsta.co &rarr;</a></span></div>
</div>
</div></section>
<div class="band-media"><img class="bandimg" data-plx="0.1" src="/assets/img/img-tokyo.jpg" alt="A neon city street at night, alive with signs">
<div class="cap"><div class="wrap"><p class="kick light">Why a studio builds its own things</p><h2 style="max-width:22ch;margin-top:10px">Because it keeps us <span class="it">honest.</span></h2></div></div></div>
<section><div class="wrap"><div class="split">
<div class="prose rv"><h2>Our money first. <span class="it">Then yours.</span></h2>
<p>Labs is where we test our own thinking about launching something nobody has searched for yet and growing a product from zero. Every lesson &mdash; pricing in public, standards as marketing, distribution built into the product &mdash; <b>flows straight back into client work</b>.</p>
<p>It also changes the conversation. We&rsquo;re not theorizing about your launch with your money. We&rsquo;ve made the same decisions with ours.</p>
<div class="cta-row"><a class="btn p" href="/contact/">Talk to Labs</a><a class="btn" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div></div>
<div class="rv"><img class="ph" src="/assets/img/street-night.jpg" alt="A city street at night"></div>
</div></div></section>
"""

page("Extra Medium Labs | Magpie, Our Flagship Product",
     "Extra Medium Labs builds the studio's own products. Flagship: Magpie, the live local creator marketing platform. Plus ventures in development: Roon, JAWNRA and hapsta.",
     "/labs/", "labs", labs, crumb_ld([("Home", "/"), ("Labs", "/labs/")]))
print("labs done")

# ============ Magpie CASE STUDY ============
signl = """
<section class="phero"><div class="wrap">
<p class="kick rv">Extra Medium Labs &middot; Flagship &middot; Case study</p>
<img class="rv" src="/assets/img/magpie-logo.png" alt="Magpie" style="height:58px;width:auto;margin:24px 0 6px">
<h1 class="rv" style="max-width:20ch">Get talked about by the people your city <span class="it">actually follows.</span></h1>
<p class="lede rv">Magpie is the local creator marketing platform built, branded and operated by Extra Medium. Local businesses comp or pay creators who live in their city to visit and post honestly &mdash; and every visit is tracked.</p>
<div class="cta-row rv"><a class="btn p" href="https://magpielocal.com">Visit magpielocal.com</a><a class="btn" href="https://app.magpielocal.com">Open the app</a></div>
<p class="note rv" style="margin-top:20px">Case study by Jeff Rimmer, Founder &middot; Extra Medium Labs &middot; October 2026</p>
<div class="hero-meta rv">
<div><b>Live</b><span>Platform &amp; founding markets</span></div>
<div><b><span data-count="45">45</span></b><span>Founding markets, 13 countries</span></div>
<div><b><span data-count="500">500</span></b><span>Followers is enough</span></div>
<div><b>97%</b><span>Creators keep of paid bookings</span></div>
</div>
<figure class="frame bleed rv" style="margin-top:30px"><img data-plx="0.06" src="/assets/img/dining-room-busy.jpg" alt="A packed local dining room at night — the kind of business Magpie sends its creators to" style="filter:grayscale(1) contrast(1.03)"></figure>
</div></section>
<section><div class="wrap"><div class="split">
<div class="prose rv"><p class="kick">The problem</p><h2>Influencer marketing <span class="it">skipped local.</span></h2>
<p>A neighborhood restaurant doesn&rsquo;t need a creator with two million followers in another state. It needs the 2,000 people within walking distance who decide where Friday night happens &mdash; and those people follow <b>neighbors, not influencers</b>.</p>
<p>Meanwhile local creators with small, fiercely local audiences had no front door: brands couldn&rsquo;t find them, couldn&rsquo;t book them properly, and couldn&rsquo;t tell what a visit brought in.</p>
<p><b>So we built the front door</b> &mdash; a two-sided platform where the standards are the marketing: published pricing, a two-business-day decision on every application, tracked visits, and a Visit Guarantee.</p></div>
<div class="rv"><img class="round" src="/assets/img/sample-portrait-sofia.jpg" alt="A Magpie creator — the neighbor a local business is really booking"></div>
</div></div></section>
<div class="band-media"><img class="bandimg" data-plx="0.1" src="/assets/img/concert-poster.jpg" alt="A festival crowd under stage lights">
<div class="cap"><div class="wrap"><p class="kick light">Built by the studio</p><h2 style="max-width:24ch;margin-top:10px">Brand. Product. Platform. Pricing. <span class="it">Go-to-market. Ops.</span></h2></div></div></div>
<section><div class="wrap"><div class="split" style="align-items:start">
<div class="prose rv"><p class="kick">What we built</p><h2>Everything a launch takes. <span class="it">Ours.</span></h2>
<p><b>Brand &amp; naming</b> &mdash; Magpie, a one-word name with its gradient identity system, designed here.</p>
<p><b>Product &amp; platform</b> &mdash; creator applications with automatic tiering (Neighbors 500&ndash;2k, Locals 2k&ndash;15k, Headliners 15k+, stacked across platforms), business onboarding, and the offer &rarr; visit &rarr; post &rarr; tracked-outcome lifecycle.</p></div>
<div class="prose rv"><p><b>Business model</b> &mdash; two lanes: comped visits, and paid bookings where creators keep 97%. Plans and pricing are published on the product site &mdash; in the open, like everything else.</p>
<p><b>Go-to-market</b> &mdash; city-by-city founding rosters, hand-picked market by market, home market Virginia Beach first. <b>Operations</b> &mdash; run daily by this studio, under Extra Medium LLC.</p>
<div class="cta-row"><a class="btn p" href="/contact/">Want this for your product? &rarr;</a></div></div>
</div></div></section>
<section><div class="wrap">
<div class="sec-head rv"><h2>Four steps, <span class="it">no theater.</span></h2><span class="mono">How a visit works</span></div>
<div class="steps" style="margin-top:26px">
<div class="step rv"><b>01 &middot; The offer</b><h3>A business makes an offer</h3><p>A comped dinner, a service, an experience &mdash; or a paid booking at the creator&rsquo;s own rate.</p></div>
<div class="step rv" style="transition-delay:.07s"><b>02 &middot; The visit</b><h3>A local creator shows up</h3><p>Someone from the neighborhood. Their followers are your neighbors too.</p></div>
<div class="step rv" style="transition-delay:.14s"><b>03 &middot; The post</b><h3>They post it honestly</h3><p>One post or reel plus two stories within 48 hours. Disclosed, in their own voice, never a script.</p></div>
<div class="step rv" style="transition-delay:.21s"><b>04 &middot; The proof</b><h3>The business sees what it brought in</h3><p>Every visit tracked. Register spend counted at the till; media value modeled and labeled as modeled.</p></div>
</div>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">Why it&rsquo;s the flagship</p><h2 style="margin-top:14px">Magpie is the studio&rsquo;s <span class="it">proof of work.</span></h2>
<p class="lede">Every discipline we sell is inside this product, exercised on our own budget. When a client asks whether we can launch their thing, Magpie is the answer we can point at.</p></div>
<div class="grid3" style="margin-top:26px">
<a class="card rv" href="https://magpielocal.com/businesses.html"><span class="num">For businesses</span><h3>Put a visit in front of local creators</h3><p>Founding businesses join the list now and activate when their market opens.</p><span class="arrow">magpielocal.com &rarr;</span></a>
<a class="card rv" style="transition-delay:.08s" href="https://magpielocal.com/creators.html"><span class="num">For creators</span><h3>500 followers is enough</h3><p>Free for creators, always. Get comped or paid by the businesses near you.</p><span class="arrow">magpielocal.com &rarr;</span></a>
<a class="card rv" style="transition-delay:.16s" href="/contact/"><span class="num">For your launch</span><h3>Want this done for your product?</h3><p>That&rsquo;s the studio side. Same team, same standards, your budget this time.</p><span class="arrow">Start a conversation &rarr;</span></a>
</div>
<p class="note rv" style="margin-top:26px">Magpie is a product of Extra Medium Labs, operated by Extra Medium LLC. Status: live, in founding-market formation; full platform terms apply at market launch.</p>
</div></section>
"""

page("Magpie — Flagship Product of Extra Medium Labs",
     "Magpie is the live local creator marketing platform built and operated by Extra Medium Labs: local businesses comp or pay local creators to visit and post honestly, every visit tracked.",
     "/labs/magpie/", "labs", signl, """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Article","headline":"Magpie — Flagship Product of Extra Medium Labs",
"description":"Magpie is the live local creator marketing platform built and operated by Extra Medium Labs: local businesses comp or pay local creators to visit and post honestly, every visit tracked.",
"author":{"@id":"https://xmedium.co/#jeff"},"publisher":{"@id":"https://xmedium.co/#org"},
"datePublished":"2026-10-23","dateModified":"2026-11-07","mainEntityOfPage":"https://xmedium.co/labs/magpie/",
"image":"https://xmedium.co/assets/img/og-collage.jpg",
"about":{"@type":"SoftwareApplication","name":"Magpie","applicationCategory":"BusinessApplication","url":"https://magpielocal.com","creator":{"@id":"https://xmedium.co/#org"}}}
</script>""" + crumb_ld([("Home", "/"), ("Labs", "/labs/"), ("Magpie", "/labs/magpie/")]))
print("case study done")

# ============ ABOUT ============
about = """
<section class="phero"><div class="wrap">
<p class="kick rv">About Extra Medium</p>
<h1 class="rv" style="max-width:18ch">A studio for businesses becoming <span class="it">who they were meant to be.</span></h1>
<p class="lede rv">Most agencies will tell you what they do. We&rsquo;d rather talk about where you&rsquo;re going. But since you asked &mdash; here is who we are, and why it works.</p>
[[layers:collage-about|Black and white collage of a typewriter, a rotary telephone and a marble statue head, over magenta]]
</div></section>
<section><div class="wrap"><div class="split">
<div class="rv"><img class="round" src="/assets/img/jeff-rimmer.jpg" alt="Jeff Rimmer, founder and principal of Extra Medium"></div>
<div class="prose rv"><p class="kick">Founder &amp; Principal</p><h2>Jeff <span class="it">Rimmer</span></h2>
<p><b>More than twenty years in marketing, on every side of the table.</b> Inside startups and inside Fortune 100 companies. Founder of several businesses of his own &mdash; including a music platform taken from a blank page to hundreds of thousands of users, and now Magpie, built in our own Labs. And the outside partner to clients across that same range, from a founder with a napkin sketch to enterprise teams serving millions.</p>
<p>That mix is the point. Jeff can write the positioning, direct the creative, build the growth engine and wire the intelligence underneath it &mdash; and has done each of those jobs for real, with his own budget on the line. Deepest experience: music and entertainment, retail and ecommerce, healthcare and wellness &mdash; three industries where attention is expensive and trust is everything.</p>
<p>He founded Extra Medium to give ambitious businesses one senior partner who thinks like an owner, builds like a studio and measures like an operator. He leads every engagement personally, works from Virginia Beach, and travels regularly to Chicago and the UK.</p>
<div class="cta-row"><a class="btn p" href="https://www.linkedin.com/in/jeffrimmer">LinkedIn</a><a class="btn" href="/work/">See the work</a></div></div>
</div></div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">A word about the name</p><h2 style="margin-top:14px">Medium is a compliment <span class="it">nobody wants.</span></h2>
<p class="lede">We believe boring is a choice, and we don&rsquo;t make it. We believe extra isn&rsquo;t too much &mdash; it&rsquo;s the whole point. And great businesses are built when someone connects every medium together: brand and growth, story and intelligence, leadership and experience. The medium changes. The idea doesn&rsquo;t.</p></div>
<div class="sec-head rv" style="margin-top:44px"><h2>Principles, <span class="it">not process decks.</span></h2><span class="mono">How we work</span></div>
<div class="prin">
<div class="rv"><b>01</b><h3>Where you are going, not what you need built</h3><p>Every engagement starts with the destination. The deliverable is decided after we understand the ambition, never before.</p></div>
<div class="rv"><b>02</b><h3>Creative on the surface, structured underneath</h3><p>Memorable work that is also disciplined: clear positioning, clean architecture, honest measurement.</p></div>
<div class="rv"><b>03</b><h3>Operators, not vendors</h3><p>We have owned budgets, teams and P&amp;Ls. We make recommendations we would make with our own money &mdash; and say the uncomfortable thing when it needs saying.</p></div>
<div class="rv"><b>04</b><h3>Connect the dots</h3><p>Brand, growth, technology and experiences are one system. We work across them because that is where the leverage is.</p></div>
<div class="rv"><b>05</b><h3>Real experience only</h3><p>What we publish and advise comes from work we have actually done. No borrowed case studies, no invented results. Magpie is the standing proof.</p></div>
<div class="rv"><b>06</b><h3>A conversation, not a proposal</h3><p>Engagements begin with a real conversation. If we are not the right fit, we will tell you who might be.</p></div>
</div>
<p class="note rv" style="margin-top:30px">Headquartered in Virginia Beach, Virginia, with presence in Chicago and London. Clients across the US and UK.</p>
</div></section>
""" + CTA

page("About Extra Medium | Studio Founded by Jeff Rimmer",
     "Extra Medium is a founder-led strategy, creative, growth and technology studio founded by Jeff Rimmer — 20+ years on every side of the marketing table, now building Magpie in its own Labs.",
     "/about/", "about", about, crumb_ld([("Home", "/"), ("About", "/about/")]))
print("about done")

# ============ CONTACT ============
contact = """
<section class="phero"><div class="wrap">
<p class="kick rv">Contact</p>
<h1 class="rv">What are you trying to <span class="it">make happen?</span></h1>
<p class="lede rv">Just start the conversation. A project, a bigger problem, a product of your own you want built the way we built Magpie &mdash; or Labs business. All reasonable ways to start.</p>
[[layers:collage-contact|Black and white collage of a bird carrying an envelope, a mailbox and a megaphone, over deep teal]]
</div></section>
<section><div class="wrap"><div class="split" style="align-items:start">
<div class="rv">
<form class="lead" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/contact/?sent=1">
<input type="hidden" name="form-name" value="contact"><p hidden><label>Don&rsquo;t fill this out: <input name="bot-field"></label></p>
<div><label for="name">Your name</label><input id="name" name="name" required autocomplete="name"></div>
<div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
<div><label for="kind">What is this about?</label><select id="kind" name="kind">
<option>A project for the studio</option><option>A bigger problem / not sure yet</option>
<option>Fractional CMO</option><option>Labs &mdash; Magpie</option><option>Labs &mdash; partnership or another venture</option><option>Something else</option></select></div>
<div><label for="msg">Tell us what&rsquo;s going on</label><textarea id="msg" name="message" required></textarea></div>
<button class="btn p" type="submit">Send it</button>
<p class="note">Usually replies within one business day. If it&rsquo;s urgent, email <a href="mailto:hello@xmedium.co">hello@xmedium.co</a>.</p>
</form></div>
<div class="prose rv">
<img class="nogray" src="/assets/img/em-logo.png" alt="Extra Medium logo" style="width:96px;height:96px;border-radius:22px;margin-bottom:24px">
<p class="kick">Prefer email?</p><h2>hello@xmedium.co</h2>
<p><b>Studio</b> &mdash; launches, reinventions, growth systems, fractional leadership.</p>
<p><b>Labs</b> &mdash; Magpie partnerships, founding markets, venture collaborations.</p>
<p>Virginia Beach (HQ) &middot; Chicago &middot; London. Most engagements run remotely, with in-person time when it matters.</p>
<p class="note">Extra Medium LLC, Virginia Beach, Virginia.</p>
</div>
</div></div></section>
"""

page("Contact | Extra Medium",
     "Start a conversation with Extra Medium — studio projects, fractional CMO, or Labs and Magpie partnerships. Replies usually within one business day.",
     "/contact/", "contact", contact, crumb_ld([("Home", "/"), ("Contact", "/contact/")]))
print("contact done")

# 404 in the new system
pathlib.Path(ROOT / "404.html").write_text("""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Not found | Extra Medium</title><link rel="icon" href="/favicon.ico" sizes="any"><link rel="stylesheet" href="/assets/css/site.css?v=14">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"></head>
<body><section class="phero"><div class="wrap"><p class="kick">404</p><h1>This page is a Small. <span class="it">We don&rsquo;t stock those.</span></h1>
<p class="lede">It doesn&rsquo;t exist anymore &mdash; the site was rebuilt around the work and our flagship product. Try one of these:</p>
<div class="cta-row" style="margin-top:28px"><a class="btn p" href="/">Home</a><a class="btn" href="/labs/magpie/">Magpie, our flagship</a><a class="btn" href="/work/">Work</a></div>
</div></section></body></html>""")
print("404 done")
