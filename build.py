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
"logo":"https://xmedium.co/assets/img/em-icon-shout.png","email":"hello@xmedium.co",
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
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/img/em-icon-shout.png">
<link rel="stylesheet" href="/assets/css/site.css?v=21">
{FONTS}
{ORG_LD}
{extra_ld}
</head><body>"""

def header(on=""):
    def cls(k): return ' class="on"' if on == k else ""
    return f"""<header class="site"><div class="wrap nav">
<a class="brand" href="/"><img src="/assets/img/em-icon-shout.png" alt="Extra Medium logo"><span class="wm">extra medium.</span></a>
<nav class="main">
<a href="/work/"{cls('work')}>Work</a>
<a href="/services/"{cls('services')}>Studio</a>
<a href="/labs/"{cls('labs')}>Labs</a>
<a href="/about/"{cls('about')}>About</a>
<a href="/magazine/"{cls('magazine')}>Extra Extra</a>
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
<a class="mlink" style="transition-delay:.47s" href="/magazine/"><i>07</i>Extra Extra</a>
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
<div class="fin-brand"><a class="brand" href="/"><img src="/assets/img/em-icon-shout.png" alt="Extra Medium logo"><span class="wm">extra medium.</span></a>
<p>A marketing agency and product lab. We build businesses people can&rsquo;t ignore &mdash; for clients, and for ourselves.</p></div>
<div><h4>Explore</h4><a href="/work/">Work</a><a href="/services/">Studio</a><a href="/labs/">Labs</a><a href="/about/">About</a><a href="/magazine/">Extra Extra</a><a href="/contact/">Contact</a></div>
<div><h4>Labs</h4><a href="/labs/magpie/">Magpie &mdash; flagship</a><a href="https://magpielocal.com">magpielocal.com</a><a href="/labs/">All ventures</a></div>
<div><h4>Connect</h4><a href="mailto:hello@xmedium.co">hello@xmedium.co</a><a href="https://www.linkedin.com/in/jeffrimmer">LinkedIn</a><a href="/contact/">Start a project</a></div>
</div>
<div class="fin-word" aria-hidden="true">extra medium.</div>
<div class="fin-base"><span>&copy; 2026 Extra Medium LLC &middot; Virginia Beach &middot; Chicago &middot; London</span><span class="fin-clock">Virginia Beach <span class="vbclock">--:--</span> ET</span><span>Magpie is a product of Extra Medium Labs.</span></div>
</div></div>
</footer>
<script src="/assets/js/site.js?v=14"></script></body></html>"""

# Pages that already end with their own CTA band use this footer (band headline
# removed, Extra Idea form kept) so the CTA never doubles up.
FOOTER_PLAIN = FOOTER.replace("""<h2 class="rv">Start a <span class="it">conversation.</span></h2>
<p class="rv">A project, a bigger problem, or a marketing seat you need filled by someone senior. The first conversation is free and specific.</p>
<div class="cta-row rv"><a class="btn white" href="/contact/">Start a project</a><a class="btn ghost" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div>
""", "").replace('<footer class="finale">', '<footer class="finale plain">').replace('<div class="fin-cta-band">', '<div class="fin-cta-band plain">')


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
    footer = FOOTER_PLAIN if ('class="ctaband"' in body or 'name="contact"' in body) else FOOTER
    html = head(title, desc, path, extra_ld) + header(on) + body + footer
    out = ROOT / (path.strip("/") + "/index.html" if path.strip("/") else "index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out)

CTA = """<section class="ctaband"><div class="wrap">
<p class="kick light rv">Let&rsquo;s talk</p><h2 class="rv">What are you trying to <span class="it">make happen?</span></h2>
<p class="rv">Don&rsquo;t know exactly what you need? Good. That&rsquo;s our job. Tell us where the business is headed and we&rsquo;ll tell you honestly whether we can help &mdash; and if we can&rsquo;t, who might.</p>
<div class="cta-row rv"><a class="btn white" href="/contact/">Start a conversation</a><a class="btn ghost" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div>
<p class="note rv" style="color:rgba(255,255,255,.85);margin-top:18px">Usually replies within one business day.</p></div></section>"""

DIVIDER = """<div class="divider" aria-hidden="true"><span class="dshape d-disc"></span><span class="dshape d-bar"></span><span class="dshape d-spark"></span><span class="dshape d-tri"></span><span class="dshape d-ring"></span></div>"""

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
""" + DIVIDER + """
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
<details class="rv"><summary>What is Extra Medium Labs?</summary><p>Extra Medium Labs is where the studio builds and operates its own products instead of only advising clients. Its flagship is Magpie, a local creator marketing platform live in 45 founding markets across 13 countries, where local businesses comp or pay local creators to visit and post honestly, with every visit tracked. Its second live product is Hapsta (hapsta.co), small capped live video rooms where fans hang out or play games with famous people.</p></details>
<details class="rv"><summary>Who does Extra Medium work with?</summary><p>Founder-led and high-growth companies, pre-launch startups, manufacturers, consumer brands and established enterprises up to Fortune 100 scale &mdash; across consumer products, ecommerce, healthcare, retail, media, music, hospitality, professional services and SaaS. The common thread is ambition, not industry.</p></details>
<details class="rv"><summary>How does an engagement start?</summary><p>With a conversation, not a proposal. Engagements take three shapes: fractional CMO leadership, a defined project such as a launch or rebrand, or ongoing growth work. If we are not the right fit, we say so &mdash; and usually know who is.</p></details>
</div>
</div></section>
"""

FAQ_HOME_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What does Extra Medium do?","acceptedAnswer":{"@type":"Answer","text":"Extra Medium is a marketing agency and fractional CMO practice based in Virginia Beach, Virginia. We launch new businesses and products, reinvent brands that have outgrown their look, and run growth systems — paid media, search, creators and AI — measured against revenue, not vanity metrics."}},
{"@type":"Question","name":"What is a fractional CMO?","acceptedAnswer":{"@type":"Answer","text":"A fractional CMO is a senior marketing executive who leads your marketing part-time — owning strategy, directing your team and agencies, and reporting results — without the cost of a permanent executive seat. Extra Medium's fractional CMO engagements are led personally by founder Jeff Rimmer."}},
{"@type":"Question","name":"What is Extra Medium Labs?","acceptedAnswer":{"@type":"Answer","text":"Extra Medium Labs is where the studio builds and operates its own products instead of only advising clients. Its flagship is Magpie, a local creator marketing platform live in 45 founding markets across 13 countries, where local businesses comp or pay local creators to visit and post honestly, with every visit tracked. Its second live product is Hapsta (hapsta.co), small capped live video rooms where fans hang out or play games with famous people."}},
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
<p class="lede rv">Labs is where the studio puts its own money where its advice is. Two live products of our own &mdash; one flagship, one core project &mdash; and a small bench behind them. Nothing else. Focus is a feature.</p>
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
<div class="flagship rv"><div class="flagship-grid">
<div class="flagship-copy"><span class="badge">Core project &middot; Live</span>
<h3 style="font-size:2.4rem;line-height:1.02;margin:10px 0 4px">Hapsta</h3>
<h3 style="font-size:1.8rem;line-height:1.08">Hang out with your fave. <span class="it">Live, in the room.</span></h3>
<p>A livestream is a broadcast: thousands watch, the celebrity talks at a crowd. Hapsta is the opposite &mdash; a small, capped, live video room where fans are <b>in it</b> with the celebrity: seen, heard, and called on by name. Some sessions hang out. Some play the celebrity&rsquo;s game, with fans seated in the party. The celebrity sets the price, the length and the room size, and keeps 80%. Our production board runs the talk line, the clock and the recording, so the celebrity just hosts.</p>
<div class="stats"><div><b><span data-count="80">80</span>%</b><span>Kept by the celebrity</span></div><div><b><span data-count="12">12</span></b><span>Max on camera</span></div><div><b><span data-count="1">1</span></b><span>Link to host</span></div></div>
<div class="cta-row"><a class="btn p" href="https://hapsta.co">hapsta.co</a><a class="btn" href="/magazine/the-room-got-small/">The story in Extra Extra</a></div></div>
<div class="flagship-media"><img src="/assets/img/hapsta-gamer.jpg" alt="A fan playing in a game session, seen over the shoulder"></div>
</div></div>
<p class="note rv" style="margin-top:22px">Status, honestly: live at hapsta.co, waitlist open, first sessions forming. Fans request the celebrities they want, and those requests decide who gets approached first. No payments are live yet &mdash; the waitlist hears first.</p>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">In development</p><h2 style="margin-top:14px">The next <span class="it">bench.</span></h2>
<p class="lede">Two ventures in active development. Everything else we&rsquo;ve explored has been archived off this page &mdash; focus is a feature.</p></div>
<div class="grid2" style="margin-top:26px">
<div class="card rv"><span class="num">01 &middot; Prototype &middot; Waitlist open</span><h3>Roon</h3><p>The days you&rsquo;d give anything to have back. A memory-keeping app that turns the photos, videos and voice notes a family already has into stories you can step back into &mdash; because storage isn&rsquo;t the problem. Meaning is.</p><span class="arrow"><a href="https://roonapp.co" style="text-decoration:none;color:inherit">roonapp.co &rarr;</a></span></div>
<div class="card rv" style="transition-delay:.08s"><span class="num">02 &middot; In development</span><h3>JAWNRA</h3><p>The world&rsquo;s music, in motion. A global music discovery and chart platform that measures momentum instead of popularity &mdash; the chart that tells you what&rsquo;s about to win, not what already did.</p><span class="arrow"><a href="https://jawnra.com" style="text-decoration:none;color:inherit">jawnra.com &rarr;</a></span></div>
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
     "Extra Medium Labs builds the studio's own products. Flagship: Magpie, the live local creator marketing platform. Core project: Hapsta, live rooms where fans hang out with famous people. In development: Roon and JAWNRA.",
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
<img class="nogray" src="/assets/img/em-icon-shout.png" alt="Extra Medium logo" style="height:96px;width:auto;margin-bottom:24px">
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


# ============ THE EXTRA — MAGAZINE ============
def _plain(t):
    return (t.replace("&rsquo;", "\u2019").replace("&ldquo;", "\u201c").replace("&rdquo;", "\u201d")
             .replace("&mdash;", "\u2014").replace("&middot;", "\u00b7").replace("&amp;", "&").replace("&hellip;", "\u2026"))

def faq_ld(qas):
    import json as _j
    items = ",".join(_j.dumps({"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}}) for q, a in qas)
    return '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + items + "]}</script>"

def article_ld(a):
    import json as _j
    d = {"@context": "https://schema.org", "@type": "Article",
         "headline": _plain(a["title"]), "description": _plain(a["dek"]),
         "datePublished": a["iso"], "dateModified": a["iso"],
         "author": {"@type": "Person", "name": "Jeff Rimmer", "jobTitle": "Co-Founder & CEO, Extra Medium"},
         "publisher": {"@type": "Organization", "name": "Extra Medium", "url": "https://xmedium.co/"},
         "mainEntityOfPage": "https://xmedium.co/magazine/" + a["slug"] + "/",
         "articleSection": a["cat"]}
    return '<script type="application/ld+json">' + _j.dumps(d) + "</script>"

ARTICLES = [
dict(slug="the-room-got-small", cat="Music & Media", cover=True,
     title="The Room Got Small: What Happens to Celebrity Access When Fans Stop Watching and Start Showing Up",
     dek="Hapsta is not another livestream. It is a ticket into a small live room where the celebrity talks with fans instead of at them, and it changes what a famous person is actually selling.",
     date="November 14, 2026", iso="2026-11-14", mins=4,
     hero=("img", "/assets/img/hapsta-studio.jpg", "A musician playing acoustic guitar in a recording studio"),
     pull="Watching is free everywhere now, and it feels like it. Being in the room is the part that got rare.",
     body="""
<p>The livestream solved distribution and broke the encounter. A celebrity can reach a million people at once now, and every one of those people knows the celebrity cannot see them. Chat scrolls too fast to read. The comments are a crowd, not a conversation. Fans got infinite access to watch and almost no access to be in it.</p>
<p>Hapsta, a product from Extra Medium Labs and live now at hapsta.co, starts from the other end. A Hapsta session is a ticket to one live session with a famous person, online, on your phone. The room is capped on purpose. Most sessions are hangouts: a small live video room where the celebrity talks with the people in it. Fans can be seen, heard, and called on by name. It is built to feel less like a broadcast and more like being somewhere.</p>
<h2>Small is the product</h2>
<p>The tiers describe how present you are. Room gets you in, watching and talking in the room. Mic puts you in the talk line, able to speak when you are called on. Video puts your camera in the room, capped at 12 people, the closest thing to sitting across from someone. Nobody in the room is anonymous crowd. The cap is not a limitation the product apologizes for. The cap is the product.</p>
<p>Some sessions are game sessions instead of hangouts. The format is the same ticket, pointed at a different room: fans get a seat in the celebrity&rsquo;s game party and play alongside them, while everyone else watches and talks from the room. The common thread is not the activity. It is the size. A capped room is a place a celebrity can actually host, and a place a fan can actually be noticed.</p>
[[pull]]
<h2>The celebrity sets the terms</h2>
<p>Hapsta does not set prices, because the value of an hour varies too much from one name to the next. The celebrity sets the price, the length, and the room size, and keeps 80% of ticket revenue. One celebrity can run a small room at a high price. Another can run a bigger room cheap. Both are rational, and both are the celebrity&rsquo;s call.</p>
<p>The work around the session is handled by an AI-assisted production board. It runs the talk line, the clock, the recording, and moderation prompts, so the person hosting does not need to produce their own show while starring in it. There is no streaming setup to buy and no gaming skill required. Talent applies to host; most have 20,000 or more followers somewhere, on any platform. What they bring is the audience and themselves. The platform brings the room and the machinery.</p>
<h2>Access is being repriced</h2>
<p>No payments are live on Hapsta yet. Fans join a waitlist and request the celebrities they want, and those requests decide who gets approached first. That order matters. Instead of booking whoever will say yes and hoping an audience follows, the platform can walk to a celebrity with a room already asking for them. The demand is documented before the pitch is made.</p>
<p>That is the shift worth watching. For a decade, celebrity access online has been sold by reach: how many people can this post hit. A capped room sells the opposite. It sells scarcity that is real, because a room with 12 cameras in it cannot be scaled without becoming the thing it replaced. The celebrity is not selling impressions. The celebrity is selling an hour of being known by name, and there is a hard limit on how much of that exists.</p>
<p>Whether fans keep paying for that is an open question, and the waitlist is how Hapsta finds out. But the direction is hard to argue with. Watching is free everywhere now, and it feels like it. Being in the room is the part that got rare.</p>
"""),
dict(slug="magpie-announcement", cat="News · Press release", cover=False,
     title="Extra Medium Labs Launches Magpie, a Local Creator Marketing Platform That Ranks Creators by Local Reach",
     dek="Magpie is live at magpielocal.com, with founding markets forming now and Hampton Roads first.",
     date="November 14, 2026", iso="2026-11-14", mins=3,
     hero=("layers", "collage-labs"),
     pull="Magpie counts the followers who live near the business. That is a smaller number, and it is the honest one.",
     body="""
<p><b>FOR IMMEDIATE RELEASE</b></p>
<p><b>VIRGINIA BEACH, Va., November 14, 2026</b> &mdash; Extra Medium Labs today announced Magpie, a local creator marketing platform that lets local businesses book local creators for comped experiences or paid posts, and shows each creator&rsquo;s local reach before anyone books. Magpie is live at magpielocal.com, with founding markets forming now and Hampton Roads first.</p>
<p>Most influencer marketing runs on one number: total followers. Magpie runs on a different one. Every creator profile shows how much of that creator&rsquo;s audience is actually local, and search ranks creators by that local reach ahead of raw follower count. A creator with 800 mostly local followers can outrank an account ten times its size, because for a restaurant, a gym, or a shop, the followers who can walk in are the ones that matter.</p>
<p>Paid bookings work on the creator&rsquo;s terms. Creators list their own rate, and they keep 97% of every paid booking. The remaining 3% covers payment transaction fees, which is what makes payment immediate instead of net-30. Businesses that prefer to comp can offer an experience instead: a meal, a service, a visit. Either way, the terms are visible before anyone commits.</p>
<p>More than 100 founding creators joined during the founding period, and signups and interest now span 45 markets in 13 countries. Founding markets are forming in sequence, starting with Hampton Roads, Virginia, where Extra Medium is based.</p>
<p>The platform includes Maggie, an AI assistant built into every account. Maggie works only from the signed-in user&rsquo;s own account data. She does not pull from other accounts, and she does not surface platform-wide numbers to individual users.</p>
<p>&ldquo;Local businesses have been priced out of creator marketing and local creators have been overlooked by it, and both problems come from the same place: the industry only counts total followers,&rdquo; said Jeff Rimmer, Co-Founder &amp; CEO of Extra Medium. &ldquo;Magpie counts the followers who live near the business. That is a smaller number, and it is the honest one.&rdquo;</p>
[[pull]]
<h2>About Magpie</h2>
<p>Magpie is a local creator marketing platform built and operated by Extra Medium Labs. Local businesses book local creators for comped experiences or paid posts at the creator&rsquo;s own listed rate, with each creator&rsquo;s local reach shown before booking and ranked above raw follower count. Creators keep 97% of paid bookings. Magpie is live at magpielocal.com.</p>
<h2>About Extra Medium</h2>
<p>Extra Medium is a founder-led marketing agency and fractional CMO practice in Virginia Beach, Virginia. Through Extra Medium Labs, the company also builds and operates its own products, including Magpie. The studio works with clients from startups to Fortune 100 companies.</p>
<p><b>Media contact:</b> hello@xmedium.co</p>
"""),
dict(slug="what-a-fractional-cmo-does", cat="Marketing", cover=False,
     title="What a Fractional CMO Actually Does All Week",
     dek="It is not a part-time version of a marketing job. It is the whole job, pointed at fewer things, on the days that matter.",
     date="November 14, 2026", iso="2026-11-14", mins=5,
     hero=("layers", "collage-cmo"),
     pull="A strategy that cannot say no is a list.",
     body="""
<p>Most founders meet the fractional CMO idea at the same moment: marketing has become too important to improvise and too expensive to staff at the top. A full-time chief marketing officer is a serious executive seat, with a serious salary attached. Hiring a junior marketer and hoping they grow into the strategy is the other option, and it usually ends with a busy calendar and no direction. The fractional model sits between those two. A senior marketing executive embeds in your company part-time, owns the strategy, and runs the function as if the seat were theirs. Because it is, for the hours they are there.</p>
<h2>Diagnosis before decoration</h2>
<p>The first weeks are not campaigns. They are an audit. Where does revenue actually come from? Which channels produce customers and which produce reports? Where does money leak: the offer nobody understands, the landing page that loses people, the ad spend pointed at an audience that was never going to buy? A fractional CMO spends real time in the numbers before touching anything creative, because most marketing problems are not creativity problems. They are clarity problems wearing a creative costume. Until the diagnosis is done, every new idea is a guess, and guesses are the most expensive line item a growing company has.</p>
<h2>One strategy everyone argues from</h2>
<p>After diagnosis comes the document most companies do not have: a single strategy, written plainly, that every marketing decision gets tested against. Who we serve. What we say. What we will not do this year. This is the unglamorous core of the job, and it is the part that changes everything downstream. Once the strategy exists, the weekly work becomes enforcement. The founder stops re-deciding the direction every Monday. The team stops building three versions of everything. Good ideas that do not fit get killed, and killing them is not a failure of imagination. It is the job. A strategy that cannot say no is a list.</p>
[[pull]]
<h2>Running the calendar, managing the people</h2>
<p>The middle of the week is operational. Launches and campaigns get planned on one calendar instead of five threads. Agencies, freelancers, and vendors get briefed properly, managed tightly, and held to outcomes instead of deliverables, so the founder does not have to do it between everything else. The fractional CMO sits in leadership meetings and translates: here is what marketing can do this quarter, here is what it cannot, here is what the numbers say we should stop funding. That translation, between the boardroom version of growth and the working version, is where a lot of companies quietly lose years. Someone senior has to stand in the middle of it.</p>
<h2>How this differs from the alternatives</h2>
<p>A consultant gives advice and leaves. The advice can be excellent, and then it sits in a document while the company goes back to improvising. An agency executes a brief. If the brief is wrong, the agency will execute the wrong thing beautifully, because execution is what you bought. A junior hire works hard and learns on your budget, but they need the strategy set for them, which means the founder becomes the CMO by default, at midnight, without the experience. The fractional CMO is the option that owns the outcome: embedded enough to be accountable, senior enough to set the strategy, and structured so the company pays for leadership hours instead of a full-time executive seat.</p>
<p>At Extra Medium, the practice is senior-only and founder-led, built on 20+ years across startups to Fortune 100 companies. It also sits inside an agency that builds, so the strategy and the execution live under one roof. The person who writes the plan is in the room when the plan meets reality, and the plan changes accordingly. That is the whole model: fewer hours than a full-time seat, none of them junior.</p>
"""),
dict(slug="the-local-advertiser", cat="Media", cover=False,
     title="The Local Advertiser Didn&rsquo;t Leave. The Audience Did.",
     dek="For decades a local business bought the paper, the radio station, and the TV spot because that was where the town was paying attention. The town is still paying attention. It is just looking at people now.",
     date="November 14, 2026", iso="2026-11-14", mins=5,
     hero=("layers", "collage-work"),
     pull="The trust that used to attach to the station now attaches to the person.",
     body="""
<h2>Where local attention used to live</h2>
<p>There was a time when buying local media was a simple decision, because there were only a few shelves to buy from. The morning paper landed on every porch that mattered. The radio station played in every truck and kitchen. The evening news was a shared appointment. A restaurant, a car dealer, a furniture store: they bought those outlets not out of loyalty but out of arithmetic. That was where local attention lived, and attention is what advertising has always actually purchased.</p>
<p>That arithmetic held for decades, and then the audience moved. Not away from the town, and not away from local life. Away from the outlets. Attention went to the phone, and on the phone it did not settle on institutions. It settled on people.</p>
<h2>The most trusted channel in town is a person</h2>
<p>Ask a local business owner where their customers hear about things now and the answer is rarely a media brand. It is a person. The neighbor who posts where she eats. The dad who reviews every taco truck in the county. The creator with 3,000 followers, most of them within twenty miles, who actually shows up at the restaurant, eats the food, and posts about it to people who trust her because she is one of them.</p>
<p>That is not a lesser form of media. In practical terms it is a stronger one. The old local outlets delivered reach and a borrowed credibility. A local creator delivers both in a smaller, denser package: a defined local audience and a voice that audience chose to follow. The trust that used to attach to the station now attaches to the person, and it attaches more firmly, because the relationship feels like what it is: one person talking to people who know her.</p>
[[pull]]
<h2>A big market with no shelf</h2>
<p>The scale of the shift is not in dispute. The creator economy is estimated at $250 billion, growing toward $480 billion by 2027. US creator ad spend is estimated at around $37 billion in 2025, growing roughly 26 percent a year. National brands have built whole departments around buying this attention.</p>
<p>Local businesses, by and large, have been locked out of it. Not because the value is unclear to them &mdash; they can see exactly who their customers listen to. They have been locked out because there was no shelf to buy it from. No standard way to find the local creators in their market, no way to see how much of a creator&rsquo;s audience is actually local, no clean way to book, brief, and pay them. A national brand buys through platforms and agencies. A restaurant owner was left to slide into someone&rsquo;s messages and hope. So the money mostly stayed in the old channels even as the audience drained out of them, or it went to boosted posts aimed at everyone and no one.</p>
<h2>What we built about it</h2>
<p>That gap is a building problem, so we built. Magpie is the platform our lab made for it: a place where a business can see a local creator&rsquo;s actual local reach before booking them, not a follower count with a guess behind it, and then comp an experience or pay the creator&rsquo;s listed rate, in the open, on standard terms.</p>
<p>The local advertiser never stopped wanting what they always wanted: the attention of the people nearby, delivered by a voice those people trust. For fifty years that voice belonged to an outlet. Now it belongs to a person. The businesses that figure that out first are not chasing a trend. They are just buying media where the town actually is.</p>
"""),
dict(slug="your-logo-is-not-your-brand", cat="Advertising", cover=False,
     title="Your Logo Is Not Your Brand",
     dek="A logo is the label on the jar. Your brand is everything inside it, and everything about how the jar gets handed over.",
     date="November 14, 2026", iso="2026-11-14", mins=5,
     hero=("layers", "collage-about"),
     pull="Nobody ever left because of a typeface. They left because the second experience didn&rsquo;t match the first promise.",
     body="""
<p>Ask a founder what their brand is and most will point at the logo. Sometimes they&rsquo;ll point at the color palette, or the typeface, or the mood board from the last redesign. All of those things are real, and all of them matter. But none of them is the brand.</p>
<p>Your brand is the set of expectations a customer carries into every interaction with you, and whether those expectations survive the interaction. It&rsquo;s the work itself. It&rsquo;s how fast you reply to an email, and whether the reply sounds like a person. It&rsquo;s the invoice, clear or confusing. It&rsquo;s the hold music, the packaging tape, the way a problem gets handled when something goes wrong at 4 p.m. on a Friday. The logo is just the label on the jar. It tells people which jar to reach for. It says nothing about what&rsquo;s inside.</p>
<h2>Why redesigns fail</h2>
<p>This is why so many rebrands disappoint. A company changes the label and leaves the jar exactly as it was. The operations stay the same, the offer stays the same, the follow-through stays the same, and six months later someone is asking why the new identity didn&rsquo;t move anything.</p>
<p>It couldn&rsquo;t have. Customers don&rsquo;t experience your identity system. They experience your behavior, in sequence, over time. If the old brand felt unreliable, that feeling wasn&rsquo;t produced by the old typeface. It was produced by missed deadlines, inconsistent quality, and promises the business couldn&rsquo;t keep at volume. A redesign that doesn&rsquo;t touch any of that is a costume change. The market notices for about a week, then goes back to believing its own experience.</p>
<p>There&rsquo;s a harder version of this problem, too. A sharper logo on an unchanged operation can actually make things worse, because it raises the expectation the operation then fails to meet. The gap between what you look like and what you act like is where trust goes to die.</p>
[[pull]]
<h2>What actually compounds</h2>
<p>The brands that hold up over years are rarely the most designed ones. They&rsquo;re the most consistent ones. A few things do the compounding:</p>
<p><b>Consistency.</b> The same standard, kept in the tenth interaction as in the first. This sounds simple and is the hardest thing on this list, because consistency is an operations problem, not a design problem.</p>
<p><b>A point of view.</b> A brand should stand for a specific way of seeing its category, stated plainly enough that a customer could repeat it. If your positioning can&rsquo;t survive being paraphrased by a stranger, it isn&rsquo;t finished.</p>
<p><b>Promises kept at scale.</b> Every business keeps its promises when it&rsquo;s small and the founder touches everything. The brand is what happens when the founder doesn&rsquo;t. Systems, hiring, and standards are brand work, even though nobody puts them in the brand book.</p>
<p>None of this makes design unimportant. Design is how the point of view becomes visible, and visible matters. It just comes second in the order of operations, not first.</p>
<h2>Fix this before anyone opens a design tool</h2>
<p>When we run a launch or a rebrand, three things get settled before identity work starts, because identity built on unsettled ground has to be rebuilt later.</p>
<p>First, the offer. What exactly is being sold, to whom, and why is it the right choice for that person? If the team can&rsquo;t answer in two sentences, the logo brief will quietly try to answer it instead, and logos are bad at that job.</p>
<p>Second, the story. Not a tagline, the actual account of why this business exists and what it changes for the customer. The story is what the identity has to carry. Decide the load before you design the vehicle.</p>
<p>Third, the proof. What can you point to? Work done, customers served, results you can state without decoration. A launch with proof can afford quiet design. A launch without it tends to ask design to shout, and shouting reads as doubt.</p>
<p>This is the order we build in on our Launch work: positioning, naming, identity, and go-to-market treated as one arc, not four separate purchases. And it&rsquo;s the discipline behind our Reinvent work, too. A rebrand is a chance to fix the jar and the label in the right order. Most companies only fix the label because it&rsquo;s the part you can see in a presentation. The jar is the part your customers can see.</p>
"""),
dict(slug="inside-the-lab", cat="The Lab", cover=False,
     title="Inside the Lab: Why a Marketing Agency Builds Its Own Products",
     dek="Extra Medium Labs is where we spend our own money on our own advice, and client work is better for it.",
     date="November 14, 2026", iso="2026-11-14", mins=5,
     hero=("layers", "collage-contact"),
     pull="It&rsquo;s easy to be brave with somebody else&rsquo;s budget.",
     body="""
<p>Most agencies sell advice they never have to live on. The campaign ends, the report gets presented, and whether the thinking actually worked becomes somebody else&rsquo;s problem. We wanted a different arrangement, so we built one. Extra Medium Labs is the product arm of this studio, the part of the business where we build and run our own products, with our own budget, on our own deadlines.</p>
<p>Four products are in the lab right now. Magpie, our flagship, is a live platform for local creator marketing: it connects local businesses with creators in their own market, ranked by how local their audience actually is. Hapsta, live at hapsta.co, runs small, capped live video rooms where fans hang out or play games with famous people; the celebrity sets the price and keeps 80 percent, and it&rsquo;s currently in its waitlist stage. Roon turns the photos, videos, and voice notes a family already has into stories; it&rsquo;s in prototype, with a waitlist open. JAWNRA, a global music discovery and chart platform that measures momentum instead of popularity, is in development.</p>
<p>Here&rsquo;s what running them does to the client work.</p>
<h2>It keeps the advice honest</h2>
<p>When you market your own product, there is no client to blame and no scope to hide behind. The positioning either works in the market or it doesn&rsquo;t, and the invoice for finding out arrives either way. That changes how you give advice. Recommendations get shorter and more specific, because you know exactly which ones you&rsquo;d fund yourself and which ones sound good in a deck.</p>
<p>Every agency has opinions about what a launch needs. A lab turns those opinions into a track record you can inspect. When we tell a client their offer needs work before their identity does, that&rsquo;s not a philosophy. It&rsquo;s a conclusion we paid to reach.</p>
[[pull]]
<h2>Every lesson gets paid for twice</h2>
<p>Client work teaches you things once, in someone else&rsquo;s context. Your own products teach you the same lesson again, in yours, with your money. Pricing, onboarding, the gap between what users say and what they do, the features that demo well and die quietly: you learn these differently when the P&amp;L has your name on it.</p>
<p>The transfer runs in both directions. A pattern we prove on a client engagement gets tested against our own products, where the feedback is fast and unfiltered. A mistake we make in the lab becomes a warning we can give a client with a straight face and a specific story attached. Paid for twice, used many times.</p>
<h2>It&rsquo;s a standing prototype shop</h2>
<p>A working lab is also infrastructure. We have live products with real signups, real payment flows, real support questions, and real analytics, which means new ideas don&rsquo;t have to be argued in the abstract. A landing page structure, an onboarding sequence, a pricing presentation: we can build it, put it in front of actual users on our own properties, and see what happens before a client spends anything on it.</p>
<p>That speed matters most at the start of an engagement, when the questions are biggest and the evidence is thinnest. Instead of bringing a client our best guess, we can often bring them something we&rsquo;ve already watched succeed or fail at small scale, and the conversation starts from evidence instead of taste.</p>
<h2>The same work, for your product</h2>
<p>None of this makes the lab a side project. It&rsquo;s the reason the studio side works the way it does. The Launch, Reinvent, and Grow engagements we run for clients use the same process we use on Magpie, Hapsta, Roon, and JAWNRA, because it&rsquo;s the only process we have: settle the offer, tell the story plainly, prove it in the market, then make it look like what it is.</p>
<p>If you&rsquo;re building something and want a team that has to follow its own advice to stay in business, that&rsquo;s the arrangement we&rsquo;re offering. The lab door is the same door as the studio door. Start a conversation and we&rsquo;ll show you both sides of it.</p>
"""),
]

def hero_html(a):
    kind = a["hero"][0]
    if kind == "layers":
        return "[[layers:" + a["hero"][1] + "|Magazine story artwork]]"
    return ('<figure class="frame bleed rv"><img data-plx="0.06" src="' + a["hero"][1] + '" alt="' + a["hero"][2] + '"></figure>')

def art_cards(items):
    out = []
    for a in items:
        out.append('<a class="card rv art-card" href="/magazine/' + a["slug"] + '/"><span class="num">' + a["cat"] + ' &middot; ' + a["date"] + '</span><h3>' + a["title"] + '</h3><p>' + a["dek"] + '</p><span class="arrow">Read &rarr;</span></a>')
    return "".join(out)

_cover = [a for a in ARTICLES if a.get("cover")][0]
_rest = [a for a in ARTICLES if not a.get("cover")]

mag_index = """
<section class="phero mag-mast"><div class="wrap">
<p class="kick rv">Extra! Extra! Read all about it</p>
<h1 class="mag-title rv">Extra <span class="it">Extra.</span></h1>
<p class="lede rv">Notes on marketing, advertising, music and media &mdash; and dispatches from our own lab. Written by the people doing the work, published when there&rsquo;s something worth saying.</p>
<p class="art-meta rv">Vol. 01 &middot; November 2026 &middot; Virginia Beach</p>
</div></section>
""" + DIVIDER + """
[[layers:collage-extra|Black and white collage of a marble statue wearing a 1920s newsboy cap, mouth open yelling the news, with flying newspaper pages and a megaphone, over a yellow field]]
<section><div class="wrap">
<p class="kick rv">Cover story &middot; """ + _cover["cat"] + """</p>
<div class="mag-cover rv">
""" + hero_html(_cover) + """
<div class="mag-cover-copy"><h2><a href="/magazine/""" + _cover["slug"] + """/">""" + _cover["title"] + """</a></h2>
<p class="lede">""" + _cover["dek"] + """</p>
<p class="art-meta">By Jeff Rimmer &middot; """ + _cover["date"] + """ &middot; """ + str(_cover["mins"]) + """ min read</p>
<a class="btn p" href="/magazine/""" + _cover["slug"] + """/">Read the cover story</a></div>
</div>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">The latest</p><h2 style="margin-top:14px">This <span class="it">issue.</span></h2></div>
<div class="grid3" style="margin-top:26px">""" + art_cards(_rest) + """</div>
</div></section>
<section><div class="wrap"><div class="split">
<div class="prose rv"><h2>Why a magazine?</h2>
<p>Because the answers clients pay for shouldn&rsquo;t live only in decks. Extra Extra is where Extra Medium publishes its thinking in the open: how marketing actually works, what we&rsquo;re learning from building our own products, and the occasional official announcement when the lab ships something.</p>
<p>New pieces land here first, then travel to LinkedIn and Instagram. One new article a day, most days.</p></div>
<div class="prose rv"><h2>Start with the work</h2>
<p>The magazine is the thinking. The studio is the doing: launches, reinventions, growth systems and fractional CMO leadership for companies from startups to Fortune 100 &mdash; plus a lab that builds its own products, so the advice is always tested at home first.</p>
<div class="cta-row"><a class="btn p" href="/services/">What the studio does</a><a class="btn" href="/labs/">Inside Labs</a></div></div>
</div></div></section>
""" + CTA

import json as _json
_mag_items = ",".join(_json.dumps({"@type": "ListItem", "position": i + 1, "url": "https://xmedium.co/magazine/" + a["slug"] + "/"}) for i, a in enumerate(ARTICLES))
_mag_ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Extra Extra — the Extra Medium magazine",'
           '"url":"https://xmedium.co/magazine/","mainEntity":{"@type":"ItemList","itemListElement":[' + _mag_items + "]}}</script>")

page("Extra Extra — Magazine | Extra Medium",
     "Extra Extra is Extra Medium's magazine: marketing, advertising, music, media, and dispatches from the lab that built Magpie and Hapsta.",
     "/magazine/", "magazine", mag_index, _mag_ld + crumb_ld([("Home", "/"), ("Magazine", "/magazine/")]))
print("magazine index done")

for _a in ARTICLES:
    _others = [x for x in ARTICLES if x["slug"] != _a["slug"]][:3]
    _body = """
<section class="phero art-head"><div class="wrap">
<p class="kick rv">""" + _a["cat"] + """ &middot; Extra Extra</p>
<h1 class="rv art-title">""" + _a["title"] + """</h1>
<p class="lede rv art-dek">""" + _a["dek"] + """</p>
<p class="art-meta rv">By Jeff Rimmer &middot; """ + _a["date"] + """ &middot; """ + str(_a["mins"]) + """ min read</p>
""" + hero_html(_a) + """
</div></section>
<section><div class="wrap"><div class="article-body rv">
""" + _a["body"].replace("[[pull]]", '<blockquote class="pull">' + _a["pull"] + "</blockquote>") + """
</div></div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">Keep reading</p><h2 style="margin-top:14px">More from <span class="it">Extra Extra.</span></h2></div>
<div class="grid3" style="margin-top:26px">""" + art_cards(_others) + """</div>
</div></section>
""" + CTA
    page(_a["title"] + " | Extra Extra",
         _a["dek"],
         "/magazine/" + _a["slug"] + "/", "magazine", _body,
         article_ld(_a) + crumb_ld([("Home", "/"), ("Magazine", "/magazine/"), (_a["cat"], "/magazine/" + _a["slug"] + "/")]))
    print("article done:", _a["slug"])

# ============ STRAIGHT ANSWERS (search landing pages, not in the menu) ============
ANSWERS = [
dict(slug="fractional-cmo", title="What Is a Fractional CMO? | Extra Medium",
     hero="collage-cmo",
     q="What is a fractional CMO, and what does one actually do?",
     desc="A fractional CMO is a senior marketing executive embedded part-time. What the job covers, who it fits, and how Extra Medium runs the practice.",
     answer="A fractional CMO is a senior marketing executive who works inside your company part-time &mdash; typically a set number of days a week &mdash; and owns your marketing strategy and function the way a full-time CMO would, without the full-time executive seat. At Extra Medium the practice is senior-only and founder-led: diagnosis first, one strategy everyone argues from, then running the calendar, the team and the vendors against it.",
     sections=[
       ("The job, in one week", "<p>Monday starts with the numbers: where revenue came from, what each channel produced, what gets stopped. The middle of the week is the calendar &mdash; launches, campaigns, the agencies and freelancers briefed and held to outcomes. Leadership meetings get a translator: what marketing can do this quarter, what it can&rsquo;t, and what the evidence says to fund. Underneath all of it is one written strategy that every decision gets tested against, including the decision to kill good ideas that don&rsquo;t fit.</p>"),
       ("Who it fits", "<p>Companies whose marketing has outgrown improvisation but not the budget for a full-time executive: founders still acting as their own CMO at midnight, teams of juniors with no one setting direction, and businesses spending real money on agencies with nobody senior on their side of the table. It also fits companies between CMOs, where the seat can&rsquo;t sit empty for two quarters.</p>"),
       ("How it works at Extra Medium", "<p>The Lead practice at Extra Medium pairs the fractional seat with the studio underneath it, so strategy and execution live under one roof: the person who writes the plan is in the room when the plan meets reality. Engagements are shaped as fractional leadership &mdash; a set cadence, a named senior, and the studio&rsquo;s Launch, Reinvent and Grow teams available behind it.</p>"),
     ],
     faqs=[
       ("What is the difference between a fractional CMO and a consultant?", "A consultant advises and leaves; the advice then has to survive contact with your calendar without them. A fractional CMO is embedded and accountable: they own the strategy, run the function on their days, and answer for outcomes in the leadership meeting."),
       ("How many days a week is a fractional CMO?", "It depends on the size of the function being run. Most engagements are one to three days a week equivalent, weighted toward launches and planning cycles. The shape is set in the first conversation, against what actually needs leading."),
       ("Do you need an agency as well as a fractional CMO?", "Not necessarily. An agency executes a brief; a fractional CMO writes the brief and judges the work. At Extra Medium the two sit in one company, which removes the hand-off where most strategy gets lost."),
     ]),
dict(slug="fractional-cmo-cost", title="How Much Does a Fractional CMO Cost? | Extra Medium",
     hero="collage-work",
     q="How much does a fractional CMO cost?",
     desc="Fractional CMO pricing, honestly: what drives it, how engagements are usually structured, and what to compare it against.",
     answer="A fractional CMO is priced as a monthly engagement, set by how many days a week the seat is filled and how much function there is to run. The honest comparison is not the day rate &mdash; it is the cost of the alternatives: a full-time CMO&rsquo;s salary and equity, a year of agency spend aimed by nobody senior, or another year of the founder doing the job at midnight. Fractional leadership exists because it is a fraction of the first and prevents the other two.",
     sections=[
       ("What drives the price", "<p>Three things: cadence (how many days a week, and whether launches spike it), scope (strategy only, or strategy plus managing your agencies, freelancers and internal team), and seniority. A genuine CMO-level operator with 20+ years across startups and Fortune 100 companies costs more per day than a mid-level marketer with a new title &mdash; and the difference is the entire point of the model. You are buying judgment that has already made the expensive mistakes somewhere else.</p>"),
       ("How engagements are usually structured", "<p>Most fractional arrangements run as a monthly retainer with a defined cadence, reviewed quarterly against outcomes. Project-shaped starts are common: a diagnosis and strategy phase first, priced on its own, so both sides can see the size of the job before committing to a cadence. Extra Medium shapes every engagement in the first conversation and puts the number in writing before any work begins. No pricing games, no discovery-call maze.</p>"),
       ("What to ask before you sign anyone", "<p>Ask who exactly sits in the seat (named person, not a bench), what they will stop you doing in the first month, how they report against revenue rather than activity, and what happens to the strategy when they are not in the room. The answers separate an operator from a deck.</p>"),
     ],
     faqs=[
       ("Is a fractional CMO cheaper than hiring a CMO?", "Yes, in total cost: you pay for leadership days instead of a full-time executive package. The right comparison also counts what a senior seat prevents &mdash; misdirected agency spend, launches without strategy, and junior hires learning on your budget."),
       ("Do fractional CMOs work on retainer or by the hour?", "Almost always a monthly retainer tied to a cadence. Hourly billing works against the model: you want the CMO thinking about your business between sessions, not watching a clock inside them."),
       ("How long do companies keep a fractional CMO?", "Long enough to set the strategy, build the calendar and team rhythm, and either hand over to a full-time hire or settle into a steady cadence. Some engagements run a quarter; many run for years at a lighter rhythm."),
     ]),
dict(slug="marketing-agency-virginia-beach", title="Marketing Agency in Virginia Beach | Extra Medium",
     hero="collage-home",
     q="A marketing agency in Virginia Beach that works like an owner, not a vendor?",
     desc="Extra Medium is a founder-led marketing agency in Virginia Beach: launches, reinventions, growth systems and fractional CMO leadership, for startups to Fortune 100.",
     answer="Extra Medium is a founder-led marketing agency headquartered in Virginia Beach, Virginia. It launches, reinvents and grows businesses &mdash; brand, creative, growth and technology under one roof &mdash; and it also builds its own products in Extra Medium Labs, led by Magpie. The practice is senior-only: the person you meet is the person who does the work, and clients range from pre-launch startups to Fortune 100 companies across the US and UK.",
     sections=[
       ("What the studio does", "<p>Six practices, one team. <b>Launch</b>: positioning, naming, identity and go-to-market as one arc. <b>Reinvent</b>: rebrands that fix the offer and story before the label. <b>Grow</b>: ongoing growth systems &mdash; content, campaigns, conversion. <b>Lead</b>: fractional CMO leadership, senior-only. <b>Intelligence</b>: AI consulting, agents and automation that survive contact with real workflows. <b>Experiences</b>: events and moments people actually remember.</p>"),
       ("Why Hampton Roads companies work with us", "<p>Local matters for some things: knowing the market, being in the room, understanding how business actually moves in Hampton Roads. For everything else, the work travels &mdash; most engagements run remotely with in-person time when it matters, and the client list runs from Virginia Beach to Chicago to London. What doesn&rsquo;t change by geography is the standard: senior people, plain talk, and advice we test on our own products first.</p>"),
       ("How an engagement starts", "<p>One conversation. Bring the project, the bigger problem, or the marketing seat you need filled. The first conversation is free and specific &mdash; you will leave knowing whether we can help, what we&rsquo;d do first, and what it would cost. If we&rsquo;re not the right fit, we&rsquo;ll say who might be.</p>"),
     ],
     faqs=[
       ("Is Extra Medium only for Virginia Beach clients?", "No. Virginia Beach is home and the first market for our own products, but studio clients are across the US and UK. Local knowledge is an advantage we bring to Hampton Roads work, not a boundary on the practice."),
       ("What size companies does Extra Medium work with?", "From pre-launch startups to Fortune 100 companies. The common thread is not size; it is a founder or leadership team that wants senior marketing thinking without building a full department first."),
       ("Does Extra Medium take project work or only retainers?", "Both. Engagements come in three shapes: fractional leadership, defined projects, and ongoing growth. The shape follows the problem, not the other way around."),
     ]),
dict(slug="fractional-cmo-vs-agency", title="Fractional CMO vs. Marketing Agency | Extra Medium",
     hero="collage-about",
     q="Fractional CMO or marketing agency: which does your company need?",
     desc="The honest difference between a fractional CMO and a marketing agency, when you need one, the other, or both, and why Extra Medium is built as both.",
     answer="An agency executes: give it a brief and it produces campaigns, creative and media. A fractional CMO leads: they own the strategy, write the brief, manage whoever executes, and answer for the outcome. If your problem is that work isn&rsquo;t getting made, you need an agency. If your problem is that nobody senior can say what work should be made, or why, you need the CMO seat filled first &mdash; otherwise the agency will execute the wrong thing beautifully.",
     sections=[
       ("The difference, plainly", "<p>Agencies are production capacity plus channel expertise, hired by the project or the month. They are excellent at making things and are structurally rewarded for making more things. A fractional CMO is leadership capacity: diagnosis, strategy, prioritization, vendor management and accountability in the leadership meeting. They are rewarded for outcomes, including the outcome of doing less, better.</p>"),
       ("When each one is the right buy", "<p>Buy the agency when the strategy is settled and the constraint is hands: a launch date, a content engine, a media plan that needs running. Buy the fractional CMO when the strategy is the constraint: spend spread across channels nobody can connect to revenue, agencies unmanaged, a founder making every marketing decision by default. Buy both, in sequence, when you need the strategy set and then executed without a hand-off &mdash; which is most growing companies, most of the time.</p>"),
       ("Why Extra Medium is both", "<p>The studio was built so the two never sit in different companies arguing over whose fault the quarter was. The Lead practice sets the strategy; the Launch, Reinvent and Grow practices execute it; and Labs keeps both honest by spending the studio&rsquo;s own money on the same advice. One roof, one accountable team.</p>"),
     ],
     faqs=[
       ("Can a fractional CMO manage our existing agency?", "Yes &mdash; that is one of the highest-value uses of the seat. A senior operator on your side of the table briefs the agency properly, judges the work against strategy, and stops spend that can&rsquo;t defend itself."),
       ("We already have a marketing manager. Do we still need a fractional CMO?", "Often, yes, and it&rsquo;s the combination that works best: the manager runs the week, the fractional CMO sets the direction, develops the manager, and carries the senior conversations. It&rsquo;s how many companies grow into a full-time seat."),
       ("What if we choose wrong?", "Start with diagnosis. A short strategy phase shows whether your constraint is direction or production before you commit to either shape. That is how Extra Medium starts most engagements."),
     ]),
dict(slug="ai-marketing-consulting", title="AI Marketing Consulting That Ships | Extra Medium",
     hero="collage-labs",
     q="How can AI actually help a marketing team, beyond the demos?",
     desc="Extra Medium's Intelligence practice: AI audits, agents and automation for marketing teams, built by a studio that runs its own AI products in production.",
     answer="AI helps a marketing team when it is pointed at a specific job with a measurable outcome: research that took a day taking an hour, first drafts that start from your own data instead of a blank page, agents that handle the repetitive middle of a workflow while people keep the judgment calls. Extra Medium&rsquo;s Intelligence practice audits where AI actually pays inside your marketing operation, then builds the agents and automations &mdash; the same discipline we use on our own products, where an AI assistant works from each user&rsquo;s own account data and nothing else.",
     sections=[
       ("Where AI pays first", "<p>The wins are boring and compounding: turning customer language into briefs, keeping content calendars fed with researched first drafts, summarizing campaign performance into decisions, qualifying and routing inquiries, and keeping a knowledge base the whole team can actually query. The pattern is the same everywhere &mdash; a clear job, a defined data boundary, a human approving anything that leaves the building.</p>"),
       ("What we build", "<p>Three shapes of work. <b>AI audits</b>: a map of your marketing workflows with the automation candidates ranked by payoff and risk. <b>Agents</b>: purpose-built assistants on your own data &mdash; like Maggie, the assistant inside Magpie, who answers only from the signed-in user&rsquo;s account data, never from anyone else&rsquo;s. <b>Automation</b>: the connective work between tools you already have, so the system runs while the team does the thinking.</p>"),
       ("What we don&rsquo;t do", "<p>We don&rsquo;t sell AI as a personality transplant for your brand, and we don&rsquo;t ship anything that publishes, sends or spends without a human in the loop where it matters. AI that can&rsquo;t show its work doesn&rsquo;t go near a client&rsquo;s customers. The standard is the one we run at home: useful, bounded, and honest about what it is.</p>"),
     ],
     faqs=[
       ("Do we need our data cleaned up before starting with AI?", "Some order helps, but a full data project is not a prerequisite. The audit starts from the workflows as they are and identifies the smallest data fixes that unlock the first wins."),
       ("Will AI replace our marketing team?", "It replaces tasks, not judgment. Teams that adopt it well end up doing more of the work only people can do: strategy, taste, relationships, and the final call."),
       ("How is this different from buying an AI tool subscription?", "Tools are generic; the value is in the fit to your workflows, your data boundaries and your approval rules. We build that fit, train the team on it, and leave the system documented and owned by you."),
     ]),
dict(slug="what-does-a-fractional-cmo-do", title="What Does a Fractional CMO Do? | Extra Medium",
     q="What does a fractional CMO actually do all week?",
     desc="What a fractional CMO actually does each week: strategy, priorities, budget, team leadership, and reporting against revenue.",
     hero="collage-cmo",
     answer="A fractional CMO owns your marketing the way a full-time CMO would, for a set share of the week. They set the strategy and positioning, decide the priorities and the budget, lead whoever is doing the work, and answer for the results. The difference from a full-time hire is the calendar, not the seniority: same seat, fewer days. Most engagements run one to three days a week, inside your leadership meetings and your numbers.",
     sections=[
       ("Strategy and positioning first", "<p>The week starts with decisions, not tasks. A fractional CMO settles who the customer is, what the company promises them, and which few channels deserve the budget. Everything else gets cut or parked. That work turns into a written plan with 90-day priorities, so the team is executing against something instead of improvising. Positioning, pricing input, and the message the whole company uses all sit in this seat. If your company is still deciding whether it needs this at all, the signs are laid out in <a href=\"/when-to-hire-a-fractional-cmo/\">when to hire a fractional CMO</a>.</p>"),
       ("Leading the people doing the work", "<p>Most growing companies already have hands: a junior marketer or two, an agency, a few freelancers. What they do not have is anyone senior telling those hands what matters. The fractional CMO briefs the agency, reviews the work before it ships, kills the projects that do not serve the plan, and coaches the internal team. Hiring sits here too: writing the marketing job descriptions, interviewing, and deciding who to bring in next. The seat also manages vendors and budgets, so spend stops drifting across tools and retainers nobody is watching.</p>"),
       ("Reporting against revenue, and building what stays", "<p>The seat sits in your leadership meetings and reports the way an executive does: pipeline, revenue, cost per customer, and what changes next because of them. Not impressions, not activity. A good fractional CMO also builds the systems that outlast the engagement: the dashboard, the planning rhythm, the brief templates, the scorecard the team keeps using. When the engagement ends, the function keeps running. What this cadence costs is covered in <a href=\"/fractional-cmo-cost/\">what a fractional CMO costs</a>; at Extra Medium the seat comes with the studio underneath it, so the strategy and the execution live in one company.</p>"),
     ],
     faqs=[
       ("How many hours a week does a fractional CMO work?", "Published guides put most engagements at one to three days a week, roughly 8 to 24 hours. The right cadence depends on team size and how much is moving: a launch quarter needs more than a steady-state quarter. The cadence is agreed up front and can flex as the work does."),
       ("Does a fractional CMO do the work themselves or direct it?", "Both, in different proportions. The seat directs: strategy, priorities, briefs, reviews, and the numbers. Hands-on execution (design, copy, media buying, development) usually sits with your team, your agencies, or, at Extra Medium, the studio under the same roof. Expect the CMO to write the plan and the brief, not the social posts."),
       ("How fast should we see results?", "Published guides put time to value at roughly 30 to 45 days: the audit, the plan, and the first corrections land in the first month or two. Revenue movement takes longer and depends on your sales cycle. Anyone promising a specific return in a specific week is guessing, and you should price that guess accordingly."),
     ]),

dict(slug="fractional-cmo-vs-full-time-cmo", title="Fractional CMO vs. Full-Time CMO | Extra Medium",
     q="Fractional CMO or full-time CMO: which is right for your company?",
     desc="The honest cost and risk comparison between a fractional CMO and a full-time CMO, and the company stages where each one wins.",
     hero="collage-work",
     answer="It comes down to workload and risk. A full-time CMO in the US commonly costs $300,000 to $570,000 a year all-in, and the hire takes months to make and a year to unwind if it is wrong. A fractional CMO gives you the same seniority for one to three days a week, at a published market range of $3,000 to $20,000 a month. If marketing genuinely needs an executive forty hours a week, hire full-time. Most companies under that load do not.",
     sections=[
       ("The cost math, honestly", "<p>Published 2026 guides put a full-time CMO&rsquo;s total cost in the US at $300,000 to $570,000 a year once salary, bonus, benefits, and equity are counted, before recruiting fees. Fractional retainers in the same guides typically run $3,000 to $20,000 a month depending on cadence and scope, with most small and mid-sized companies landing between $3,000 and $8,000. That is not a rounding difference; it is a different budget category. The full breakdown lives in <a href=\"/fractional-cmo-cost/\">what a fractional CMO costs</a>. Neither option is cheap. The question is which one matches the actual workload.</p>"),
       ("The risk is asymmetric", "<p>A full-time executive search takes months. Ramp-up takes more months. If the hire is wrong, you lose the better part of a year, plus severance, plus the team&rsquo;s momentum, and then you start the search again. Companies also tend to hire the full-time CMO before they can describe the job, which is how the hire goes wrong. A fractional engagement is a contract: a 3 to 6 month initial term is typical, the cadence can be adjusted, and if the fit is wrong it ends without an org chart to rebuild. You can also use the fractional seat to define the full-time job before you hire it.</p>"),
       ("When each one wins", "<p>Hire full-time when the load is real: a marketing team large enough to need a daily executive, revenue past roughly $25M, a board and investor cadence that consumes the seat, and decisions that cannot wait two days. Hire fractional when the leadership gap is real but the load is part-time: strategy is missing, agencies are unled, the founder is the default marketer, and the budget cannot carry a $300,000-plus package without starving the work itself. Many companies run fractional for a year or two, then hire full-time once the function is built and the job is obvious.</p>"),
     ],
     faqs=[
       ("Can a fractional CMO become our full-time CMO later?", "Sometimes, and it is a clean way to hire: you have watched the person work for months before either side commits. It is not the default, though. Many fractional CMOs run a portfolio practice by choice. Treat the conversion as a possible outcome to discuss openly, not an assumption to build the engagement on."),
       ("How long do fractional engagements usually last?", "Published guides describe a 3 to 6 month initial term as typical, with many engagements extending well past a year once the rhythm is working. Time to value is usually 30 to 45 days. If a provider asks for a long lock-in before any work has shipped, that is worth a hard question."),
       ("What if we already have a marketing manager?", "That is the normal setup, not an obstacle. A fractional CMO gives your manager the senior direction, priorities, and cover they cannot give themselves, and usually makes them more effective rather than redundant. The arrangement to avoid is two people both claiming the strategy seat. One person owns the plan; everyone else owns pieces of it."),
     ]),

dict(slug="fractional-cmo-vs-consultant", title="Fractional CMO vs. Marketing Consultant | Extra Medium",
     q="Fractional CMO or marketing consultant: what's the real difference?",
     desc="The real difference between a fractional CMO and a marketing consultant is ownership: advice that leaves versus leadership that stays.",
     hero="collage-about",
     answer="Ownership. A consultant answers a defined question and hands the answer back: an audit, a plan, a recommendation. Then they leave, and your team decides what to do with it. A fractional CMO makes the decision, leads the people doing the work, and is still there next quarter when a call turns out wrong. If you have one well-formed question, hire a consultant. If the gap is ongoing leadership, that is the fractional seat.",
     sections=[
       ("Advice versus accountability", "<p>A consulting engagement is scoped as a deliverable. You buy an answer: a market study, a pricing review, a channel audit. The work ends when the document lands, and whether anything changes is your problem. A fractional CMO is scoped as a retainer because the work is a function, not a document. They set the strategy, then stay to run it: leading the team, managing the budget, adjusting when the numbers move. The expertise can be identical. The difference is who is accountable the morning after the recommendation. That is also why consultants are priced per project and fractional CMOs per month.</p>"),
       ("Where the interim CMO and the advisor fit", "<p>Two neighboring arrangements get mixed into this decision. An interim CMO is full-time but temporary: they fill a CMO-shaped hole that already exists, usually because a permanent leader left or is being recruited, and the function cannot pause. A fractional engagement usually starts earlier, when the company is not yet sure the seat should exist at all. An advisor is lighter still: a few hours a month of access to experience, sometimes for equity, with no operational responsibility. Advisors are useful. They are not leadership, and they should not be priced or judged as if they were.</p>"),
       ("How to choose, in one pass", "<p>Ask what happens after the answer. If the honest answer is &ldquo;we will know what to do and we have the people to do it,&rdquo; a consultant is the cheaper, correct buy. If the answer is &ldquo;we will still need someone senior deciding, week after week,&rdquo; you are describing the fractional seat. And if the strategy is settled but the work itself is not getting done, neither is the fix; that gap belongs to an agency, which is a different comparison: <a href=\"/fractional-cmo-vs-agency/\">fractional CMO vs. agency</a>. Buy the shape of help that matches the shape of the gap.</p>"),
     ],
     faqs=[
       ("Can a consultant become our fractional CMO?", "It happens, usually after a strategy project lands well and both sides see the ongoing gap. Watch the incentives when it does: the person who sold the diagnosis should not be the only voice deciding the prescription is a retainer. Ask what they would do in the first 90 days and judge that, not the deck."),
       ("Is a fractional CMO more expensive than a consultant?", "Per month, usually yes; per outcome, not necessarily. A consultant&rsquo;s project fee looks smaller until the recommendations sit unimplemented and get re-bought next year. A fractional retainer costs more because it includes the implementation leadership. Compare total cost over twelve months, including the work that did or did not get done, not the first invoice."),
       ("How do we know if our problem is advice-shaped or leadership-shaped?", "Look at your last three marketing initiatives. If they failed for lack of a good plan, the problem is advice-shaped. If reasonable plans kept dying in execution, drift, or indecision, the problem is leadership-shaped. Most companies that call us have already bought the plan once. They are missing the person who makes it happen."),
     ]),

dict(slug="when-to-hire-a-fractional-cmo", title="When to Hire a Fractional CMO | Extra Medium",
     q="When should you hire a fractional CMO?",
     desc="The signs a company needs a fractional CMO, the signs it does not, and what a first conversation should cover.",
     hero="collage-home",
     answer="When marketing has become a leadership gap rather than a labor gap. The pattern looks like this: the founder is still the default marketing decision-maker, real money is going out the door with nobody able to say what it returned, and agencies or a small team are executing without anyone senior on your side setting direction. You do not need more hands. You need the seat filled, at a fraction of the week and the cost.",
     sections=[
       ("The signs, in plain terms", "<p><b>The founder is the marketing department.</b> Every decision waits on the person with the least time to make it. <b>Spend nobody can account for.</b> Money goes to ads, tools, and retainers, and nobody can connect it to revenue. <b>Agencies without a senior counterpart.</b> Work gets executed, but nobody on your side decides whether it is the right work. <b>Growth has stalled or turned unpredictable.</b> Referrals carried you here; they will not carry the next stage. <b>Something big is coming.</b> A launch, a raise, a rebrand, a new market: moments that punish improvised marketing. Two or three of these together is the signal.</p>"),
       ("When not to hire one", "<p>Three situations argue against it. <b>There is nobody to lead.</b> If there is no team, no agency, and no budget to execute, a strategist is an executive watching an empty channel; buy execution first. <b>The problem is one bounded thing.</b> A website, a logo, a single campaign: hire for that, at a project price. <b>The product itself is still unsettled.</b> If you do not yet know what you are selling or to whom, marketing strategy is premature, because it would lock in answers that are about to change. A good fractional CMO will tell you this in the first conversation rather than sell you the seat.</p>"),
       ("What happens next, if the signs fit", "<p>The next step is a conversation, not a commitment. At Extra Medium the first conversation is free and specific: we look at your current marketing, name the gap as we see it, and say plainly whether the fractional seat is the right fix or whether something cheaper is. If it is the right fix, the engagement shape and the price go in writing before any work begins. The mechanics of vetting and hiring, including the questions worth asking any provider, are in <a href=\"/how-to-hire-a-fractional-cmo/\">how to hire a fractional CMO</a>. Bring last quarter&rsquo;s numbers if you have them.</p>"),
     ],
     faqs=[
       ("What revenue size fits a fractional CMO?", "There is no universal threshold, but published guides cluster around companies from roughly $1M to $25M in revenue: large enough to have real marketing spend and execution capacity, not yet large enough to need the seat forty hours a week. Below that range the fee can crowd out the work; above it, full-time usually wins."),
       ("Can a fractional CMO bridge us to a full-time hire?", "Yes, and it is one of the better uses of the model. The fractional seat runs the function now, defines what the full-time job actually is, and can help interview and onboard the permanent hire. Companies that hire the executive first often discover the job they described is not the job they needed."),
       ("How quickly can an engagement start?", "Faster than any executive hire: there is no search, no notice period, and no relocation. Published guides put time to value at 30 to 45 days once started, most of it the audit and the first plan. At Extra Medium, the first conversation is free, and the engagement shape and price are in writing before work begins."),
     ]),
dict(slug="fractional-cmo-for-startups", title="Fractional CMO for Startups | Extra Medium",
     q="Should a startup hire a fractional CMO?",
     desc="When a startup actually needs a fractional CMO, what the seat does, and when it is too early.",
     hero="collage-labs",
     answer="A startup should hire a fractional CMO after it has a product customers already want, and not before. Past product-market fit, the problem stops being discovery and becomes direction: positioning, a go-to-market plan, the first marketing hires, and a story investors can repeat. A fractional CMO owns those calls a few days a week. Published guides put typical retainers at $3,000 to $20,000 a month, against $300,000 to $570,000 a year loaded for a full-time CMO. Before that fit exists, spend the money on customers, not leadership.",
     sections=[
       ("The moment it makes sense", "<p>The signals are consistent. Revenue is coming in, but from scattered efforts nobody planned. The founder is still the marketing department, and marketing is the job that gets done last, after product, hiring, and fundraising. Channels get tried one at a time with no system connecting them, and every agency or freelancer gets briefed by someone who is guessing. That is a leadership gap, not a labor gap. More hands will not fix it, because nobody senior is deciding what the hands should do, in what order, and what to stop doing.</p>"),
       ("What the seat does at a startup", "<p>Four things, mostly. <b>Positioning</b>: who the product is for and why it wins, said in words a buyer repeats. <b>Go-to-market</b>: which channels get tested first, with what budget, and what result kills or scales each one. <b>First hires</b>: the order matters &mdash; the wrong first marketing hire is an expensive year. And the <b>investor narrative</b>: the growth story in the deck has to match the numbers in the room. At Extra Medium the Lead practice pairs the seat with the studio underneath it, so the same company can also name, brand, and launch the business through our Launch practice when that is what the stage calls for.</p>"),
       ("The honest warning, and the junior-hire trap", "<p>Before product-market fit, do not hire one. A fractional CMO builds a system: positioning, channels, measurement. Built around the wrong customer, that system just gets you to the wrong answer faster and with more confidence. Early on you need discovery, not direction. The other common mistake is hiring a junior marketer full-time instead. A junior hire can run tasks. They cannot set strategy, judge channels, or tell a founder no &mdash; and they will learn marketing by spending your budget. A senior operator a few days a week costs less and decides better. Smaller companies face a version of the same choice, covered in <a href=\"/fractional-cmo-for-small-business/\">fractional CMO for small business</a>, and the timing signals are laid out in <a href=\"/when-to-hire-a-fractional-cmo/\">when to hire a fractional CMO</a>.</p>"),
     ],
     faqs=[
       ("How early is too early to hire a fractional CMO?", "If you are still figuring out who the customer is and whether they will pay, it is too early. That stage needs customer discovery and cheap experiments, not a marketing system. Once a defined customer is buying and the problem is reaching more of them in an organized way, the seat starts paying for itself."),
       ("How many days a week does a startup need?", "Most engagements run one to three days a week. A startup setting positioning and a first go-to-market plan usually needs one to two. More days make sense when there is a team to lead, agencies to manage, or a launch in motion. The cadence should follow the workload, not a package."),
       ("Can a fractional CMO help with fundraising?", "Yes, in a specific way. Investors test whether the growth story and the numbers agree. A fractional CMO sharpens the narrative, builds the marketing metrics behind it, and closes the obvious gaps in the go-to-market plan before you are in the room. They cannot fix a story the numbers contradict."),
     ]),

dict(slug="fractional-cmo-for-small-business", title="Fractional CMO for Small Business | Extra Medium",
     q="Does a small business need a fractional CMO?",
     desc="For owners running marketing themselves: what a fractional CMO changes, and the fee test to run first.",
     hero="collage-home",
     answer="A small business needs a fractional CMO when marketing has outgrown the owner&rsquo;s spare time but not the budget for a full-time executive &mdash; for most companies, somewhere in the $1 million to $10 million revenue range. What you are buying is ownership: one plan, one person managing the vendors, and spend that gets accounted for. Published guides put typical retainers at $3,000 to $8,000 a month for companies this size. Run the fee test first: if the fee would eat most of your marketing budget, buy execution instead.",
     sections=[
       ("The ceiling on owner-led marketing", "<p>Owner-led marketing works until it doesn&rsquo;t. The owner knows the customers and the offer better than anyone, so early marketing is good. Then the business grows, marketing becomes five jobs &mdash; the website, the ads, the social accounts, the agency, the occasional campaign &mdash; and every one of them gets the owner&rsquo;s leftover attention. Decisions pile up. Vendors get briefed in fragments. Nobody can say what last quarter&rsquo;s spend produced. The ceiling is not effort or talent. It is that marketing has become a leadership job and it is being done in the margins of a different job.</p>"),
       ("What changes when the seat is filled", "<p>Three things, and they are unglamorous. <b>One plan</b>: every channel and vendor works from the same priorities, set against revenue, not activity. <b>Managed vendors</b>: the agencies and freelancers you already pay get a senior person briefing them, reviewing the work, and cutting what is not performing &mdash; most small businesses get more from the vendors they have before they need new ones. <b>Accounted spend</b>: a monthly read on what went out, what came back, and what changes next. That includes local businesses. A regional firm, a multi-location service company, or a retailer lives on local demand, and local demand is exactly where uncoordinated spend leaks worst.</p>"),
       ("The sanity rule on fees", "<p>Be suspicious of any leadership hire, including us, until this math works. If your total marketing budget is $2,000 a month, spending most of it on strategy leaves nothing to execute with. That is backwards. Buy execution first &mdash; a good freelancer, a focused agency, one channel done properly &mdash; and add leadership when the spend is large enough that wasting it costs more than the fee. For most businesses that point arrives somewhere around $1 million in revenue. Below the leadership threshold, the honest answer is often a smaller engagement or none. The full cost picture, including what a full-time CMO runs, is in <a href=\"/fractional-cmo-cost/\">what a fractional CMO costs</a>.</p>"),
     ],
     faqs=[
       ("What size business is the right fit for a fractional CMO?", "Published guides put the typical band at roughly $1 million to $25 million in revenue. Small businesses usually land between $1 million and $10 million: large enough that marketing spend is real money, small enough that a full-time CMO at $300,000 or more a year loaded makes no sense. Revenue is a guide, not a gate &mdash; the real test is whether a leadership gap exists."),
       ("Does a fractional CMO work for a local business?", "Yes. Local businesses often run more marketing pieces than they realize &mdash; search, reviews, social, a website, maybe an agency &mdash; with nobody coordinating them. A fractional CMO sets the plan around how local customers actually choose, manages the vendors, and cuts the spend that is not producing calls, bookings, or sales."),
       ("We already have an agency. Would a fractional CMO replace it?", "Usually not. Most engagements start by getting more out of the vendors already in place. The fractional CMO sits on your side of the table: setting the strategy the agency executes against, judging the work, and deciding what continues. If an agency is the wrong fit, you will hear that too, with the reasoning in plain terms."),
     ]),

dict(slug="how-to-hire-a-fractional-cmo", title="How to Hire a Fractional CMO | Extra Medium",
     q="How do you hire a fractional CMO and choose the right one?",
     desc="The questions that separate operators from decks, the red flags, and how a good engagement starts.",
     hero="collage-contact",
     answer="Hire a named person, not a firm&rsquo;s bench, and interview for operating history, not vocabulary. Ask who exactly will sit in the seat, what they would stop you doing in the first month, how they report against revenue, and what happens to the strategy when they are not in the room. A real operator answers all four concretely. A good engagement then starts with a short diagnosis phase before any retainer &mdash; the plan should be built on your numbers, not a template. Everything else is negotiation.",
     sections=[
       ("The questions that separate operators from decks", "<p>Ask these, and weigh the answers literally. <b>Who exactly sits in the seat?</b> A named person with a history you can check &mdash; if the answer is a rotating bench, you are buying an agency with a new label. <b>What will you stop us doing in month one?</b> Operators cut things. Someone who only adds has never owned a budget. <b>How do you report?</b> The answer should end at revenue: pipeline, sales, cost per customer &mdash; not impressions and engagement. <b>What happens when you are not in the room?</b> The strategy has to survive their absence, in writing, with the team able to run it.</p>"),
       ("Red flags", "<p>Three show up again and again. <b>Decks without operating history</b>: polished frameworks from someone who has never been accountable for a number. Ask what they ran, at what size, and what it returned &mdash; then check. <b>Activity reporting</b>: monthly reports full of posts shipped, campaigns launched, and traffic charts, with no line connecting any of it to revenue. That is a vendor protecting a retainer. <b>Nothing is ever killed</b>: channels only get added, budgets only grow, and every quarter is a building quarter. A CMO who will not cut a channel is not managing your money; they are spending it politely.</p>"),
       ("How a good engagement starts", "<p>Diagnosis first, retainer second. A serious fractional CMO will want a few weeks inside the business before proposing the plan: the numbers, the customers, the current spend, the team, the vendors. What comes back should be specific &mdash; what is working, what is leaking, what happens in the first 90 days, and what it costs. That is how we work at Extra Medium. The first conversation is free and specific, and the engagement shape and price are put in writing before any work begins. If a provider wants a long contract signed before they have looked at your business, keep looking. For grounding on the role itself, see <a href=\"/what-does-a-fractional-cmo-do/\">what a fractional CMO does</a>.</p>"),
     ],
     faqs=[
       ("Should a fractional CMO be one named person or a team?", "One named person in the seat. Teams are fine underneath &mdash; strategists need execution support, and our own model pairs the seat with a studio &mdash; but accountability has to have a name on it. If the person in your leadership meeting changes month to month, nobody owns the outcome, and outcomes are the entire point of the hire."),
       ("How long is a typical fractional CMO commitment?", "Most engagements run one to three days a week on a monthly retainer, often with an initial term of a few months so both sides can judge fit. Be wary of long lock-ins demanded up front. The honest structure is a short diagnosis, a defined first phase, and a retainer that continues because it is working, not because the contract says so."),
       ("What should reporting from a fractional CMO look like?", "One page, monthly, tied to money: spend by channel, what it produced in pipeline or revenue, cost per customer, and what changes next month and why. Supporting detail can sit behind it, but if the first page is activity &mdash; posts, campaigns, traffic &mdash; instead of results, you are being managed, not led."),
     ]),

dict(slug="marketing-agency-vs-in-house", title="Marketing Agency vs. In-House Team | Extra Medium",
     q="Should you hire a marketing agency or build an in-house team?",
     desc="An honest comparison of agency, in-house, and the hybrid most growing companies actually land on.",
     hero="collage-work",
     answer="For most growing companies, neither one alone. An agency buys production capacity and channel expertise, and is rewarded for output. An in-house team buys control and context, but no single hire covers strategy, creative, media, and technology &mdash; and a senior team costs more than most owners expect. The structure that usually wins is a hybrid: a lean in-house core, an agency for production, and fractional leadership over both. Which piece you need first depends on whether your gap is hands, skills, or direction.",
     sections=[
       ("What an agency is actually for", "<p>An agency is rented capacity: designers, writers, media buyers, and developers you could never justify as full-time seats, available in the mix you need this quarter. Good agencies bring pattern recognition from dozens of businesses like yours. The limits are structural. An agency is rewarded for output &mdash; deliverables shipped, campaigns live &mdash; not for your revenue, and it will rarely tell you to spend less. It also works from a brief. If nobody senior on your side is setting strategy and judging the work, you get competent execution of an unexamined plan, which is the most expensive kind of marketing there is.</p>"),
       ("What in-house gives you, and what it costs", "<p>In-house buys context no vendor can match: your team knows the customers, hears the sales calls, and feels the product change. Control is real, and for content and customer knowledge it compounds. The problem is coverage and cost. Marketing is now at least four professions &mdash; strategy, creative, media, and technology &mdash; and one hire, however good, is one of them. Owners routinely hire a single marketer and expect all four. A genuinely senior in-house team, even a small one, quickly runs past the loaded cost of a full-time CMO, commonly $300,000 to $570,000 a year for that seat alone. Most growing companies buy the team before they can feed it.</p>"),
       ("The hybrid most growing companies land on", "<p>The working structure is three layers. <b>A lean in-house core</b>: one or two people who own the customer knowledge, the content, and the day-to-day. <b>An agency or freelancers for production</b>: the specialist output the core cannot cover, scoped tightly. <b>Fractional leadership over both</b>: a fractional CMO setting the plan, briefing the agency, developing the in-house team, and answering for the number &mdash; typically $3,000 to $20,000 a month against a full-time executive package. That is the model Extra Medium is built on: the Lead practice pairs the fractional seat with the studio, so leadership and production sit in one company. The leadership-versus-agency distinction is drawn in detail at <a href=\"/fractional-cmo-vs-agency/\">fractional CMO vs. agency</a>.</p>"),
     ],
     faqs=[
       ("Which is cheaper, an agency or an in-house team?", "An agency, at the start, almost always. You rent exactly the hours and skills you need with no salary, benefits, or recruiting. In-house gets competitive only when your demand for a skill is constant and heavy enough to fill a seat &mdash; and by then the comparison should include management time and the cost of the skills that seat does not have."),
       ("Can one senior marketing hire replace an agency?", "Rarely. A senior hire brings strategy and judgment, but one person cannot also be the designer, the media buyer, the writer, and the developer at a professional level. What usually happens is the senior hire spends their time doing junior production badly, or managing freelancers with no system. Senior leadership plus rented production beats either one pretending to be both."),
       ("When does building in-house win outright?", "When marketing is a core, daily, proprietary function of the business &mdash; high-volume content engines, performance media at serious scale, or a product where marketing data is a competitive asset. At that point the volume justifies the seats and the context is worth more than the flexibility. Most companies get there later than they think, and the hybrid carries them until they do."),
     ]),
dict(slug="fractional-cmo-hampton-roads", title="Fractional CMO in Hampton Roads | Extra Medium",
     q="Fractional CMO in Hampton Roads: senior marketing leadership, based here.",
     desc="Fractional CMO leadership in Hampton Roads from Extra Medium, the Virginia Beach studio led by founder Jeff Rimmer.",
     hero="collage-cmo",
     answer="A fractional CMO in Hampton Roads gives a company senior marketing leadership for one to three days a week, without a full-time executive hire. Extra Medium is based in Virginia Beach, so this is home turf: the same studio that launches and grows brands nationally sits in your leadership meetings, sets the plan, and answers for the results. You get a named senior operator, a studio behind the seat, and the shape and price in writing before work begins.",
     sections=[
       ("Marketing in a relationship town, until it stops working", "<p>Hampton Roads runs on relationships. Defense and military-adjacent contractors, port and logistics firms, healthcare systems, hospitality groups, and thousands of owner-led businesses have grown for years on referrals, reputation, and who knows whom across the seven cities. That works, until a competitor gets serious about search, a contract gets competed, or the next generation of buyers never hears your name. Then the gap shows: no one senior owns the plan, the website says less than the sales team does, and marketing is a pile of vendor invoices. A fractional CMO closes that gap by setting direction, joining up the pieces, and making the spend answer to revenue.</p>"),
       ("What working with us looks like here", "<p>Because the studio is here, the cadence is simple. Your fractional CMO is in the room for leadership meetings, planning days, and the moments that need a senior marketer present, not on a screen. Between those days the work runs remotely: strategy, briefs, vendor direction, and reporting. Behind the seat sits the full Extra Medium studio, covering the six practices, Launch, Reinvent, Grow, Lead, Intelligence, and Experiences, so the plan does not wait on hiring. If you are comparing local firms as well, our <a href='/marketing-agency-virginia-beach/'>marketing agency in Virginia Beach</a> page sets out the studio side.</p>"),
       ("Who it fits in Hampton Roads", "<p>It fits companies that have outgrown founder-led or relationship-led marketing but are not ready for a full-time CMO: a contractor chasing larger awards, a healthcare or hospitality group with locations across the metro, a professional firm whose referrals are thinning, or an owner-led business spending real money with no one senior owning the result. It starts with a first conversation, free and specific, about your market and your numbers. If the seat is the right answer, you get the engagement shape and price in writing before any work begins. If it is not, we say so.</p>"),
     ],
     faqs=[
       ("Are you based in Hampton Roads?", "Yes. Extra Medium is headquartered in Virginia Beach, and Hampton Roads is our home market. Your fractional CMO works from here, in your offices across the seven cities when it matters and remotely day to day. You are not buying a national firm that flies someone in. You are hiring the senior studio down the road, led by founder Jeff Rimmer."),
       ("How much does a fractional CMO cost in Hampton Roads?", "It is priced as a monthly engagement, not a salary, and it runs a fraction of a full-time CMO package. The exact shape depends on days per week, scope, and how much studio support sits behind the seat. We never quote a number before understanding the work. You get the engagement shape and price in writing before work begins, with no surprises later."),
       ("How is this different from hiring a local marketing agency?", "An agency executes channels. A fractional CMO owns the plan those channels serve. Extra Medium does both under one roof: the Lead practice puts a senior operator in your leadership seat, and the studio executes the work the plan calls for. That means one accountable conversation about strategy, spend, and results, instead of a vendor reporting on its own activity."),
     ]),

dict(slug="fractional-cmo-richmond", title="Fractional CMO in Richmond, VA | Extra Medium",
     q="Fractional CMO in Richmond: what does the seat do for a Richmond company?",
     desc="Fractional CMO leadership for Richmond, Virginia companies from Extra Medium, two hours away in Virginia Beach and in the room when it matters.",
     hero="collage-work",
     answer="A fractional CMO gives a Richmond company senior marketing leadership for one to three days a week, on a monthly cadence, without a full-time executive hire. Extra Medium is headquartered in Virginia Beach, about two hours away: close enough for regular in-person days, senior enough to run the function remotely between them. You get a named operator in your leadership meetings, a studio behind the seat, and the engagement shape and price in writing first.",
     sections=[
       ("A capital city with a serious middle layer", "<p>Richmond is the state capital, and it shows in the company mix: finance, insurance, and legal firms with long histories, state-adjacent organizations, and a strong layer of mid-sized companies that sell regionally and nationally from a Richmond base. VCU adds energy, talent, and a steady stream of younger companies. Marketing here usually stalls quietly. The firm is respected, the relationships are old, and the website and story have not kept up with what the company has become. Referrals carry the pipeline until they do not, and nobody senior owns the fix.</p>"),
       ("What working with Extra Medium looks like from Richmond", "<p>We work with Richmond companies the way the seat actually runs: leadership meetings, planning, and reporting on a weekly rhythm, mostly remote, with regular in-person days in Richmond when the work needs a room. Two hours is an easy drive, and we make it. Behind the fractional CMO sits the full studio, so strategy, brand, web, content, and AI work move without you hiring or managing a bench of vendors. One senior conversation owns the plan, the spend, and the results, and you always know who that conversation is with.</p>"),
       ("Who it fits in Richmond, and how it starts", "<p>It fits the established firm whose marketing has not kept pace with its reputation, the mid-sized company selling beyond Virginia for the first time, and the growing business where the founder or managing partner is still the default marketing department. It starts with a first conversation, free and specific, about where growth is supposed to come from and what is blocking it. If a fractional CMO is the right answer, the shape and price arrive in writing before work begins. Founder Jeff Rimmer leads the seat himself, with 20+ years across media, startups, and Fortune 100 work.</p>"),
     ],
     faqs=[
       ("Are you based in Richmond?", "No, and we will not pretend otherwise. Extra Medium is headquartered in Virginia Beach, about two hours from Richmond. We work with Richmond companies remotely day to day and in the room for leadership days, planning sessions, and launches. What you get is a senior operator who knows Virginia business, not a local office sign."),
       ("How often would you be in Richmond in person?", "On the rhythm the work needs. Leadership and planning days are scheduled in person, and launches or major decisions usually get a room, not a video call. Day to day, the seat runs remotely with the same weekly cadence, reporting, and access you would expect from someone on your own team."),
       ("What does the engagement cost?", "It is a monthly engagement, priced well below a full-time CMO package, and shaped by days per week and scope. We do not quote a number before we understand the company and the work. The first conversation is free, and you receive the engagement shape and price in writing before anything begins."),
     ]),

dict(slug="fractional-cmo-charlottesville", title="Fractional CMO in Charlottesville, VA | Extra Medium",
     q="Fractional CMO in Charlottesville: senior marketing leadership for a small, serious market.",
     desc="Fractional CMO leadership for Charlottesville, Virginia companies from Extra Medium, senior marketing direction for a small, high-trust market.",
     hero="collage-about",
     answer="A fractional CMO gives a Charlottesville company senior marketing leadership for one to three days a week, without a full-time executive hire. Extra Medium is headquartered in Virginia Beach and works with Charlottesville companies remotely day to day, in the room when it matters. In a market this small and reputation-driven, the value is judgment: a senior operator who sets the plan carefully, protects the name you have built, and answers for results.",
     sections=[
       ("A small market with a long memory", "<p>Charlottesville punches above its size. The University of Virginia anchors the economy and spins out research, health, and technology companies. Around it sit biotech and health firms, wine and hospitality businesses that sell an experience as much as a product, and professional firms built on trust. It is a high-trust, relationship-first culture, and reputation travels fast in both directions. Sloppy marketing is remembered here. So is quiet competence. Most local companies do not need louder marketing. They need a senior person making sure the story, the spend, and the experience line up.</p>"),
       ("What working with us looks like from Charlottesville", "<p>The seat runs on a monthly cadence, one to three days a week. Day to day we work remotely: strategy, planning, vendor and team direction, and reporting your leadership can actually use. When the work calls for a room, a launch, a planning day, a hard conversation, we are in Charlottesville for it. Behind the fractional CMO is the full Extra Medium studio across Launch, Reinvent, Grow, Intelligence, and Experiences, so a UVA spinout or a hospitality group gets senior leadership and execution without building a marketing department first.</p>"),
       ("Who it fits here", "<p>It fits the spinout that has outgrown founder-led marketing, the health or biotech firm selling to buyers far beyond Albemarle County, and the established local business whose next customers will find it online before they hear about it at dinner. It also fits companies that need discretion: senior judgment, no noise. It starts with a first conversation, free and specific. If the seat fits, you get the engagement shape and price in writing before work begins. If your real need is smaller, we will tell you that instead.</p>"),
     ],
     faqs=[
       ("Are you based in Charlottesville?", "No. Extra Medium is headquartered in Virginia Beach. We work with Charlottesville companies remotely day to day and travel in for the days that need a room. We will not claim a local office we do not have. What we offer is senior leadership that understands how a small, high-trust market actually works."),
       ("Can a fractional CMO work for a company our size?", "Usually, yes, and size is the point. Charlottesville companies often need CMO-level judgment long before they can justify a full-time CMO. One to three days a week of senior leadership, with a studio behind it, matches the scale of the market. If your need is really a pair of hands, we will say so honestly."),
       ("How does it start?", "With a first conversation, free and specific, about your market, your reputation, and where growth should come from next. From there you get a written engagement shape and price before any work begins. No retainer pitch, no pressure. In a town where people talk, we would rather earn the referral than win the argument."),
     ]),

dict(slug="fractional-cmo-raleigh", title="Fractional CMO in Raleigh & the Triangle | Extra Medium",
     q="Fractional CMO in Raleigh: marketing leadership for Triangle companies.",
     desc="Fractional CMO leadership for Raleigh and Triangle companies from Extra Medium, senior marketing direction for teams outgrowing founder-led marketing.",
     hero="collage-labs",
     answer="A fractional CMO gives a Raleigh company senior marketing leadership for one to three days a week, without a full-time executive hire. By Raleigh we mean the whole Triangle, Raleigh, Durham, and Chapel Hill, one market. Extra Medium is headquartered in Virginia Beach and works with Triangle companies remotely day to day, in the room when it matters. You get a senior operator who owns the plan, and a studio behind the seat.",
     sections=[
       ("Growth is not the problem. Focus is.", "<p>The Triangle is one of the fastest-growing business regions in the country. Research Triangle Park anchors tech and life sciences, Durham and Chapel Hill add research, health, and university spinouts, and transplant talent keeps raising the bar. Companies here rarely lack opportunity. They lack senior marketing focus. The founder still runs marketing between everything else, agencies execute in pieces, and the story changes depending on who wrote the page. A fractional CMO gives a scaling company one accountable owner for positioning, plan, and pipeline before it hires a full executive team.</p>"),
       ("What working with us looks like from the Triangle", "<p>The seat runs one to three days a week on a monthly cadence. Strategy, planning, team and vendor direction, and reporting run remotely, built into your leadership rhythm. We are in the Triangle in person for planning days, launches, and the decisions that need a room. Behind the fractional CMO sits the Extra Medium studio, covering brand, web, content, and AI, so a company scaling past founder-led marketing gets leadership and execution together, without pausing growth to recruit a department. One plan, one owner, one conversation about results.</p>"),
       ("Who it fits in Raleigh, Durham, and Chapel Hill", "<p>It fits the tech or life sciences company between funding rounds that needs a real go-to-market plan, the services firm hiring its first marketers and needing someone senior to lead them, and the established Triangle business whose growth has outpaced its brand. It starts with a first conversation, free and specific, about your stage and your numbers. If the seat is right, the engagement shape and price come in writing before work begins. Jeff Rimmer, our founder, brings 20+ years across media, three startups, and Fortune 100 clients.</p>"),
     ],
     faqs=[
       ("Are you based in Raleigh?", "No. Extra Medium is headquartered in Virginia Beach, Virginia. We work with Raleigh and Triangle companies remotely day to day and in person for planning days, launches, and leadership sessions. We know the Triangle as one market, Raleigh, Durham, and Chapel Hill together, and we will never confuse it with Charlotte."),
       ("Do you work with early-stage Triangle startups?", "Yes, when the company has something real to sell and marketing leadership is the gap. Pre-launch and early growth companies often need positioning and a go-to-market plan more than a full-time CMO. If you are too early for the seat to pay off, we will tell you what to do first instead."),
       ("What does a fractional CMO cost in Raleigh?", "It is a monthly engagement at a fraction of a full-time CMO package, shaped by days per week and scope. Triangle rates for senior leadership are competitive with any major metro, which is exactly why the fractional shape helps. You get the shape and price in writing before work begins."),
     ]),
dict(slug="fractional-cmo-washington-dc", title="Fractional CMO in Washington, DC | Extra Medium",
     q="Fractional CMO in Washington, DC: who does it fit in this market?",
     desc="Fractional CMO leadership for Washington, DC associations, nonprofits, contractors and professional services firms, from Extra Medium.",
     hero="collage-contact",
     answer="A fractional CMO is a senior marketing leader who works with your organization part-time, usually one to three days a week, and owns the marketing plan the way a full-time CMO would. Extra Medium brings that leadership to Washington organizations whose marketing is about membership, events, policy audiences and credibility as much as pipeline: associations, nonprofits, government contractors and professional services firms. The work is founder-led, run day to day remotely and in the room for board meetings, launches and decisions that need a person present.",
     sections=[
       ("What marketing leadership means in Washington", "<p>In DC, marketing rarely answers to a sales quota alone. Associations answer to members and renewal rates; nonprofits to donors, boards and mission; contractors to credibility with agencies and partners; advocacy groups to policy audiences who read carefully. Buying cycles are long, committees are everywhere, and every claim gets checked. That changes the job: positioning has to survive a board packet, events carry real weight, and the plan has to connect membership, attendance and influence, not just leads. A fractional CMO sets that plan, directs the staff and vendors executing it, and reports to leadership in the language boards actually use.</p>"),
       ("Working with Extra Medium from Washington", "<p>Extra Medium is founder-led and senior-only, which matters in Washington, where the person in the room is the product. Day to day, your fractional CMO works set days each week inside your leadership rhythm: staff meetings, vendor and agency direction, budget decisions and the monthly report your board will actually read. That runs remotely from our Virginia Beach headquarters. Board presentations, planning sessions, launches and sensitive meetings happen in person, in the room. You are never handed to a junior team after the first call. The first conversation is free and specific, and the engagement shape and price are in writing before any work begins.</p>"),
       ("Who it fits, and how it starts", "<p>It fits an association with a capable marketing team and nobody senior setting its direction. It fits a nonprofit between marketing directors, a contractor whose credibility with agencies and partners has outgrown a coordinator, or a professional services firm where the partners are still the marketing department by default. It does not fit if what you need is hands alone, someone to post and place ads, or a leader in the building five days a week. It starts with a free conversation about your specific situation. If there is a fit, you get the engagement shape and the price in writing, and you decide with the full picture in front of you.</p>"),
     ],
     faqs=[
       ("Are you based in Washington, DC?", "No. Extra Medium is headquartered in Virginia Beach, Virginia, and Washington is one of the markets we work in. Day to day, your fractional CMO works remotely on set days each week. Board meetings, planning sessions, launches and the conversations that need a person in the room happen in person. You get a senior leader without a DC salary, office or headcount attached."),
       ("What does a fractional CMO engagement cost?", "Fractional engagements are priced as a monthly engagement, based on how many days a week you need and what the role has to own. There is no rate card and no hourly meter. After a first conversation about your situation, you get the shape and the exact price in writing before any work begins, so the decision is made on a real number, not a range."),
       ("How does the work run day to day?", "On an agreed rhythm, usually one to three days a week. Your fractional CMO sits in your leadership meetings, sets the plan and priorities, directs your staff, agencies and freelancers, owns the marketing budget, and reports results to you and your board monthly. It is the accountability of a chief marketing officer, bought by the fraction instead of the full-time hire."),
     ]),

dict(slug="fractional-cmo-chicago", title="Fractional CMO in Chicago | Extra Medium",
     q="Fractional CMO in Chicago: what does it cost, and who does it fit?",
     desc="Fractional CMO leadership for Chicago companies: published cost ranges, who it fits, and how Extra Medium works with Chicago teams.",
     hero="collage-work",
     answer="In Chicago, a fractional CMO gives a growing company senior marketing leadership part-time, usually one to three days a week, for a monthly retainer instead of a full-time executive package. Published Chicago pricing commonly runs $5,000 to $20,000 a month. Extra Medium works with Chicago companies the same way: founder-led, senior-only leadership that owns the plan, the budget and the team&rsquo;s direction, run remotely day to day and in the room when it matters. The exact price is in writing before work begins.",
     sections=[
       ("A B2B town that runs on payback math", "<p>Chicago is a B2B town. Manufacturing, logistics, food, distribution and professional services anchor the economy, with a large startup scene layered on top. Marketing buyers here are practical: they expect plain payback math, cost per qualified opportunity and revenue per channel, not impressions and reach. That makes the fractional model a natural fit. Most of these companies have real marketing activity and real spend, but the plan lives in pieces: an agency here, a freelancer there, a sales team working from different assumptions. A fractional CMO joins it up, sets priorities against the numbers, and is accountable for what the spend returns.</p>"),
       ("What it costs in Chicago", "<p>Published 2026 pricing for Chicago puts fractional CMO retainers commonly between $5,000 and $20,000 a month, depending on days per week and scope. Seasoned operators billing hourly run roughly $200 to $350 an hour. Chicago rates sit about 15 to 20 percent below New York and San Francisco for comparable seniority, which is part of the city&rsquo;s appeal: the leadership is the same caliber, the overhead is not. Extra Medium does not publish a rate card. Your engagement is priced on the days and the remit, and you get the exact figure in writing before any work begins.</p>"),
       ("Who it fits, and how it starts", "<p>It fits the Chicago pattern well: a manufacturer or distributor with a strong product and marketing that has not kept up, a services firm whose growth still runs on referrals, or a startup past its first traction that needs a plan and a leader before it needs a bigger team. It does not fit if the need is hands alone, or a leader on site five days a week. Working together runs on a weekly cadence, remotely day to day and in the room for planning, launches and board-level moments. It starts with a free conversation, followed by the engagement shape and price in writing.</p>"),
     ],
     faqs=[
       ("Are you based in Chicago?", "Extra Medium is headquartered in Virginia Beach, and Chicago is one of the markets listed on our site because we work with companies there. There is no staffed Chicago office and no junior local team. You work directly with the founder-led senior team: remotely day to day, and in the room in Chicago when the work calls for it."),
       ("What does a fractional CMO cost in Chicago?", "Published Chicago ranges put retainers commonly at $5,000 to $20,000 a month, with seasoned operators at roughly $200 to $350 an hour, about 15 to 20 percent below coastal rates. Extra Medium prices each engagement on days per week and scope. After a free first conversation, the exact price is in writing before work begins. No surprises, and no hourly meter running."),
       ("How do we work together if you are not in Chicago?", "On a set rhythm, usually one to three days a week. Leadership meetings, planning and reporting run on video and shared documents; your fractional CMO directs your team and vendors, owns the budget and reports against the numbers monthly. Chicago trips are scheduled around the moments that benefit from a person in the room: kickoffs, planning sessions, launches and board meetings."),
     ]),

dict(slug="fractional-cmo-london", title="Fractional CMO in London | Extra Medium",
     q="Fractional CMO in London: how does the model work for UK companies?",
     desc="Fractional CMO leadership for London scale-ups and PE-backed companies: how the model works, what it costs, and how a US studio runs it.",
     hero="collage-labs",
     answer="A fractional CMO is a senior marketing leader who works with a company part-time, typically one to three days a week on a business-to-business contract, and owns the marketing plan without a full-time hire. Extra Medium is a US studio that works with UK companies: you get senior leadership plus a working studio behind it, run on a fixed weekly cadence across the time zones, and in the room in London when it matters. Engagements are priced in writing before work begins.",
     sections=[
       ("The densest fractional market in the UK", "<p>London has the deepest bench of growing companies in the UK, and the densest demand for fractional marketing leadership. Scale-ups, fintech and SaaS firms and PE-backed companies share the same shape: real revenue, real spend, investors asking harder questions, and marketing that has outgrown the founder and the first hires without yet justifying a full-time chief marketing officer. The fractional model fits that gap exactly. Senior judgment, a plan the board can interrogate, and a team directed against numbers, bought by the day or the week instead of as a permanent package.</p>"),
       ("What it costs, and how the contract works", "<p>Published UK figures put fractional CMO day rates typically between £750 and £1,400, with London&rsquo;s senior specialists at £1,000 to £2,500. Monthly retainers run from £3,000 to £15,000 depending on days and remit. Set that against a full-time London CMO at £120,000 to £150,000 base, around £180,000 as a package, before recruitment costs and the months a search takes. Engagements are business-to-business contracts, commonly structured outside IR35, with no permanent headcount added. Extra Medium prices the same way: days and scope agreed up front, the figure in writing before work begins.</p>"),
       ("Working with a US studio from London", "<p>The honest question is the time zone, and cadence is the answer. Engagements run on fixed days each week, with live meetings scheduled in the overlap, London&rsquo;s afternoon and Virginia&rsquo;s morning, and decisions, documents and reporting moving asynchronously in between. Nothing waits a day for a signature or a steer. When the work needs a person in the room, a launch, a board session, a planning week, we are in London for it. It fits scale-ups and PE-backed firms that need senior marketing ownership now. It starts with a free conversation, then the engagement shape and price in writing.</p>"),
     ],
     faqs=[
       ("Are you based in London?", "No. Extra Medium is a US studio headquartered in Virginia Beach, and London is on our site because we work with UK companies. There is no staffed London office. What you get is senior, founder-led marketing leadership plus a working studio, run on a fixed weekly cadence across the time zones, with London trips for the moments that need a person in the room."),
       ("What does a fractional CMO cost in London?", "Published UK ranges put day rates typically at £750 to £1,400, with London senior specialists at £1,000 to £2,500, and monthly retainers from £3,000 to £15,000. Extra Medium prices each engagement on days per week and scope, business to business. After a free first conversation, the exact figure is in writing before any work begins."),
       ("How does the time difference work day to day?", "Engagements run on fixed days with a set weekly rhythm. Live meetings sit in the overlap window, London afternoon and Virginia morning. Between them, plans, documents and reporting move asynchronously, so work is waiting for you at the start of your day rather than the end of it. The cadence is agreed up front, and it does not drift."),
     ]),
]

_ALTS = {
 "collage-home": "Black and white collage of a marble statue head merged with a bird, over a magenta field",
 "collage-cmo": "Black and white collage of a vintage microphone and a hand tuning a retro television, over deep teal",
 "collage-labs": "Black and white collage of a bird perched on a marble statue head beside a vintage camera, over electric blue",
 "collage-work": "Black and white collage of chess pieces, a pointing hand and a telescope, over a sunny yellow field",
 "collage-about": "Black and white collage of a typewriter, a rotary telephone and a marble statue head, over magenta",
 "collage-contact": "Black and white collage of a bird carrying an envelope, a mailbox and a megaphone, over deep teal",
 "collage-extra": "Black and white collage of a marble statue wearing a 1920s newsboy cap, mouth open yelling the news, with flying newspaper pages and a megaphone, over a yellow field",
}
for _an in ANSWERS:
    _secs = "".join("<h2>" + h + "</h2>" + b for h, b in _an["sections"])
    _faq_html = "".join('<details class="rv"><summary>' + q + "</summary><p>" + a + "</p></details>" for q, a in _an["faqs"])
    _hero = _an.get("hero", "collage-cmo")
    _abody = """
<section class="phero"><div class="wrap">
<p class="kick rv">Straight answers</p>
<h1 class="rv">""" + _an["q"] + """</h1>
<div class="answer-first rv"><p>""" + _an["answer"] + """</p></div>
</div></section>
[[layers:""" + _hero + "|" + _ALTS[_hero] + """]]
<section><div class="wrap"><div class="prose rv">""" + _secs + """</div>
<h2 class="rv" style="margin:34px 0 6px">Asked <span class="it">often.</span></h2>
""" + _faq_html + """
<p class="rv" style="margin-top:28px"><a href="/answers/">More straight answers &rarr;</a></p>
</div></section>
""" + CTA
    page(_an["title"], _an["desc"], "/" + _an["slug"] + "/", "", _abody,
         faq_ld(_an["faqs"]) + crumb_ld([("Home", "/"), ("Answers", "/" + _an["slug"] + "/")]))
    print("answer done:", _an["slug"])

# ============ ANSWERS HUB ============
_CITY_SLUGS = {"marketing-agency-virginia-beach", "fractional-cmo-hampton-roads", "fractional-cmo-richmond", "fractional-cmo-charlottesville", "fractional-cmo-raleigh", "fractional-cmo-washington-dc", "fractional-cmo-chicago", "fractional-cmo-london"}
def _ans_cards(items):
    return "".join('<a class="card rv" href="/' + a["slug"] + '/"><span class="num">Straight answers</span><h3>' + a["q"] + '</h3><p>' + a["desc"] + '</p><span class="arrow">Read &rarr;</span></a>' for a in items)
_qs = [a for a in ANSWERS if a["slug"] not in _CITY_SLUGS]
_cs = [a for a in ANSWERS if a["slug"] in _CITY_SLUGS]
_hub = """
<section class="phero"><div class="wrap">
<p class="kick rv">Straight answers</p>
<h1 class="rv">Questions, <span class="it">answered straight.</span></h1>
<p class="lede rv">What a fractional CMO is, what one costs, when to hire one, and how the seat works in the markets we serve &mdash; answered the way we&rsquo;d answer in the first conversation, out in the open.</p>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">The questions</p><h2 style="margin-top:14px">Before you <span class="it">hire anyone.</span></h2></div>
<div class="grid3" style="margin-top:26px">""" + _ans_cards(_qs) + """</div>
</div></section>
<section><div class="wrap">
<div class="sec-head block rv"><p class="kick">By market</p><h2 style="margin-top:14px">Fractional CMO, <span class="it">by city.</span></h2></div>
<div class="grid3" style="margin-top:26px">""" + _ans_cards(_cs) + """</div>
</div></section>
""" + CTA
_hub_items = ",".join(_json.dumps({"@type": "ListItem", "position": i + 1, "url": "https://xmedium.co/" + a["slug"] + "/"}) for i, a in enumerate(ANSWERS))
_hub_ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Straight Answers — Extra Medium",'
           '"url":"https://xmedium.co/answers/","mainEntity":{"@type":"ItemList","itemListElement":[' + _hub_items + "]}}</script>")
page("Straight Answers | Extra Medium",
     "Straight answers from Extra Medium: what a fractional CMO is, what one costs, when to hire one, and fractional CMO by city — Hampton Roads, Richmond, Charlottesville, Raleigh, Washington DC, Chicago and London.",
     "/answers/", "", _hub, _hub_ld + crumb_ld([("Home", "/"), ("Answers", "/answers/")]))
print("answers hub done")



# 404 in the new system
pathlib.Path(ROOT / "404.html").write_text("""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Not found | Extra Medium</title><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/img/em-icon-shout.png"><link rel="stylesheet" href="/assets/css/site.css?v=21">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"></head>
<body><section class="phero"><div class="wrap"><p class="kick">404</p><h1>This page is a Small. <span class="it">We don&rsquo;t stock those.</span></h1>
<p class="lede">It doesn&rsquo;t exist anymore &mdash; the site was rebuilt around the work and our flagship product. Try one of these:</p>
<div class="cta-row" style="margin-top:28px"><a class="btn p" href="/">Home</a><a class="btn" href="/labs/magpie/">Magpie, our flagship</a><a class="btn" href="/work/">Work</a></div>
</div></section></body></html>""")
print("404 done")
