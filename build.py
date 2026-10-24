#!/usr/bin/env python3
"""Extra Medium v2 — light, orange->pink gradient, video-first, scroll experience.
Edit content here, run `python3 build.py`, commit the output."""
import pathlib
ROOT = pathlib.Path(__file__).parent

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;600;700;800&family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'

def head(title, desc, path):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://xmedium.co{path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Extra Medium">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="https://xmedium.co{path}">
<meta property="og:image" content="https://xmedium.co/assets/img/em-logo.png">
<meta name="theme-color" content="#ff3d8a">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/css/site.css">
{FONTS}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Extra Medium","legalName":"Extra Medium LLC","url":"https://xmedium.co/","logo":"https://xmedium.co/assets/img/em-logo.png","email":"hello@xmedium.co","founder":{{"@type":"Person","name":"Jeff Rimmer"}},"address":{{"@type":"PostalAddress","addressLocality":"Virginia Beach","addressRegion":"VA","addressCountry":"US"}}}}</script>
</head><body><div id="progress"></div><div id="glow"></div>"""

def header(on=""):
    def cls(k): return ' class="on"' if on == k else ""
    return f"""<header class="site"><div class="wrap nav">
<a class="brand" href="/"><img src="/assets/img/em-logo.png" alt="Extra Medium logo"><span>extra medium<small>Studio &amp; Labs</small></span></a>
<button class="burger" aria-label="Menu" onclick="document.querySelector('.nav nav').classList.toggle('open')">&#9776;</button>
<nav>
<a href="/work/"{cls('work')}>Work</a>
<a href="/services/"{cls('services')}>Studio</a>
<a href="/labs/"{cls('labs')}>Labs</a>
<a href="/about/"{cls('about')}>About</a>
<a href="/contact/" class="btn small">Start a conversation</a>
</nav></div></header>"""

FOOTER = """<footer class="site"><div class="wrap">
<a href="/contact/" style="text-decoration:none"><div class="foot-big">Let&rsquo;s make<br>something <span style="font-family:var(--serif);font-style:italic;font-weight:400">extra.</span></div></a>
<div class="foot-grid">
<div><a class="brand" href="/"><img src="/assets/img/em-logo.png" alt="Extra Medium logo"><span>extra medium<small>Studio &amp; Labs</small></span></a>
<p style="color:rgba(255,255,255,.85);margin-top:16px;max-width:32ch">A strategy, creative, growth and technology studio. We build businesses people can&rsquo;t ignore &mdash; for clients, and for ourselves.</p></div>
<div><h4>Studio</h4><a href="/work/">Work</a><a href="/services/">What we do</a><a href="/about/">About</a><a href="/contact/">Contact</a></div>
<div><h4>Labs</h4><a href="/labs/">Extra Medium Labs</a><a href="/labs/signl/">SIGNL &mdash; flagship</a><a href="https://joinsignl.com">joinsignl.com</a></div>
<div><h4>Talk to us</h4><a href="mailto:hello@xmedium.co">hello@xmedium.co</a><a href="/contact/">Start a project</a><a href="https://www.linkedin.com/in/jeffrimmer">Jeff on LinkedIn</a></div>
</div>
<div class="foot-base"><span>&copy; 2026 Extra Medium LLC &middot; Virginia Beach &middot; Chicago &middot; London</span><span>SIGNL is a product of Extra Medium Labs.</span></div>
</div></footer>
<script src="/assets/js/site.js"></script></body></html>"""

def page(title, desc, path, on, body):
    html = head(title, desc, path) + header(on) + body + FOOTER
    out = ROOT / (path.strip("/") + "/index.html" if path.strip("/") else "index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out)

def filmstrip():
    imgs = [("hero-restaurant-night.jpg","A packed local restaurant at night"),
            ("chef-flame.jpg","A chef working a flame in a kitchen"),
            ("cocktails-toast.jpg","Friends toasting with cocktails"),
            ("salon-barber.jpg","Inside a neighborhood barbershop and salon"),
            ("kitchen-line.jpg","A kitchen line mid-service"),
            ("street-night.jpg","A city street at night"),
            ("bar-friends.jpg","Friends gathered at a local bar"),
            ("creator-cocktail-photo.jpg","A creator photographing a cocktail")]
    one = "".join(f'<img src="/assets/img/{f}" alt="{a}" loading="lazy">' for f, a in imgs)
    return f'<div class="film" aria-hidden="true"><div class="film-track">{one}{one}</div></div>'

CTA = """<section style="padding-top:0"><div class="wrap"><div class="band rv">
<p class="kicker">Let&rsquo;s talk</p><h2>What are you trying to <span class="it">make happen?</span></h2>
<p class="lede">Don&rsquo;t know exactly what you need? Good. That&rsquo;s our job. Tell us where the business is headed and we&rsquo;ll tell you honestly whether we can help &mdash; and if we can&rsquo;t, who might.</p>
<div class="cta-row"><a class="btn white" href="/contact/">Start a conversation</a><a class="btn ghost" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div>
<p class="note">Usually replies within one business day.</p></div></div></section>"""

MARQUEE = """<div class="marquee"><div>Launch <span>&bull;</span> <i>Reinvent</i> <span>&bull;</span> Grow <span>&bull;</span> <i>Expand</i> <span>&bull;</span> Lead <span>&bull;</span> <i>Intelligence</i> <span>&bull;</span> Experiences <span>&bull;</span> Launch <span>&bull;</span> <i>Reinvent</i> <span>&bull;</span> Grow <span>&bull;</span> <i>Expand</i> <span>&bull;</span> Lead <span>&bull;</span> <i>Intelligence</i> <span>&bull;</span> Experiences <span>&bull;</span>&nbsp;</div></div>"""

# ============ HOMEPAGE ============
home = """
<section class="hero-full">
<video autoplay muted loop playsinline poster="/assets/img/hero-poster.jpg" src="/assets/video/hero.mp4"></video>
<div class="shade"></div>
<div class="wrap">
<p class="kicker rv">Extra Medium &middot; Strategy, creative, growth &amp; technology studio</p>
<h1 class="rv">Your business doesn&rsquo;t need more marketing. It needs something <span class="it">worth noticing.</span></h1>
<p class="lede rv" style="transition-delay:.12s">We launch, reinvent and grow businesses &mdash; and we build our own products to prove we know how. Founder-led, senior-only, no theater.</p>
<div class="cta-row rv" style="transition-delay:.22s"><a class="btn" href="/contact/">Start a conversation</a><a class="btn ghost" href="/work/">See the work</a></div>
<div class="hero-meta rv" style="transition-delay:.32s">
<div><b>20+ yrs</b><span>Every side of the table</span></div>
<div><b>1 live</b><span>Product of our own &mdash; SIGNL</span></div>
<div><b>3 shapes</b><span>Fractional &middot; project &middot; ongoing</span></div>
<div><b>US + UK</b><span>Virginia Beach &middot; Chicago &middot; London</span></div>
</div></div>
<div class="scrollcue">Scroll</div>
</section>
""" + MARQUEE + """
<section><div class="wrap">
<div class="sec-head rv"><p class="kicker">From our Labs &middot; Flagship product</p><h2>We don&rsquo;t just launch products for clients. <span class="it gtext">We launched our own.</span></h2></div>
<div class="flagship tilt rv"><div class="flagship-grid">
<div class="flagship-copy">
<span class="badge">Live now &middot; Founding markets forming</span>
<img class="logo" src="/assets/img/signl-logo.png" alt="SIGNL">
<h3 style="font-size:1.7rem;line-height:1.1">Local creator marketing, city by city.</h3>
<p>Local businesses comp or pay creators who actually live in their city to visit and post honestly &mdash; and every visit is tracked. 500 followers is enough when they&rsquo;re the right 500.</p>
<div class="stats"><div><b data-count="37">37</b><span>Founding markets</span></div><div><b data-count="8">8</b><span>Countries</span></div><div><b data-count="500">500</b><span>Followers is enough</span></div></div>
<div class="cta-row"><a class="btn grad-s" href="/labs/signl/">The SIGNL story</a><a class="btn ink" href="https://joinsignl.com">Visit joinsignl.com</a></div>
</div>
<div class="flagship-media"><video autoplay muted loop playsinline poster="/assets/img/cafe-poster.jpg" src="/assets/video/cafe.mp4"></video></div>
</div></div>
<p class="note rv">Why lead with our own product? Because a studio that launches its own thing &mdash; brand, platform, pricing, go-to-market, operations &mdash; gives different advice than one that only sells launches. <a href="/labs/">More from Labs &rarr;</a></p>
</div></section>
""" + filmstrip() + """
<section><div class="wrap">
<div class="sec-head rv"><p class="kicker">Selected work</p><h2>Proof, <span class="it gtext">not promises.</span></h2>
<p class="lede">Some clients prefer not to be named, and fractional work belongs to the client &mdash; so stories are told without logos, with the details that matter. Ask us about any of it.</p></div>
<div class="rv"><div class="case"><div class="tag">Growth system</div><h3>The consumer brand that needed a growth system, not more ads</h3>
<p>A high-growth supplement brand had traction and scattered channels. We took ownership of strategy end to end &mdash; search, social, affiliate, creator and AI-driven channels under one owner. <span class="outcome">Growth became a system with an owner, not a pile of campaigns.</span></p></div>
<div class="case"><div class="tag">Reinvention</div><h3>The manufacturer that had to become one brand</h3>
<p>A global radiation-protection manufacturer needed one brand after an acquisition &mdash; global marketing across web, CRM, ecommerce, SEO and product marketing, plus a physician-facing podcast. <span class="outcome">One brand, one digital foundation, international expansion supported.</span></p></div>
<div class="case"><div class="tag">Our own launch</div><h3>The platform we launched ourselves</h3>
<p>Before Extra Medium, our founder built a digital music platform from a blank page &mdash; seed funding raised, team built, artists onboarded. <span class="outcome">Grew past 900,000 users.</span> SIGNL is us doing it again, in public.</p></div></div>
<div class="cta-row rv" style="margin-top:36px"><a class="btn" href="/work/">All the work &rarr;</a></div>
</div></section>

<section class="grad-sec"><div class="wrap">
<div class="sec-head rv"><p class="kicker">The studio</p><h2>What are you trying to change?</h2></div>
<div class="grid4">
<a class="card rv" href="/services/#launch"><span class="num">01 &middot; Launch</span><h3>Launch something</h3><p>Shape it, position it, build it, launch it and make people care &mdash; the whole arc, not a handoff.</p><span class="arrow">Launch &rarr;</span></a>
<a class="card rv" style="transition-delay:.08s" href="/services/#reinvent"><span class="num">02 &middot; Reinvent</span><h3>Fix what isn&rsquo;t working</h3><p>Figure out what needs to change without throwing away what still works.</p><span class="arrow">Reinvent &rarr;</span></a>
<a class="card rv" style="transition-delay:.16s" href="/services/#grow"><span class="num">03 &middot; Grow</span><h3>Grow faster</h3><p>More traffic might help. We&rsquo;d rather first find out why the traffic you already have isn&rsquo;t doing more.</p><span class="arrow">Grow &rarr;</span></a>
<a class="card rv" style="transition-delay:.24s" href="/services/#lead"><span class="num">04 &middot; Lead</span><h3>Become the name</h3><p>Fractional CMO leadership and executive branding for founders who need a senior brain, not another vendor.</p><span class="arrow">Lead &rarr;</span></a>
</div></div></section>

<div class="band-media"><video data-para="0.10" autoplay muted loop playsinline poster="/assets/img/cafe-poster.jpg" src="/assets/video/bowls.mp4"></video>
<div class="cap"><div class="wrap"><p class="kicker light">The standard</p><h2 style="max-width:20ch">Real businesses. Real people. <span class="it">Real posts.</span></h2></div></div></div>

<section><div class="wrap"><div class="split">
<div class="rv"><img class="round" src="/assets/img/jeff-rimmer.jpg" alt="Jeff Rimmer, founder of Extra Medium"></div>
<div class="prose rv"><p class="kicker">Founder-led</p><h2 style="margin-bottom:20px">Hi. I&rsquo;m <span class="it gtext">Jeff.</span></h2>
<p>I&rsquo;ve spent a career sitting in pretty much every seat around this table: inside big companies, building companies, hiring agencies, being the agency, launching things, fixing things &mdash; and occasionally wondering why everyone made it so complicated.</p>
<p><b>Extra Medium came from wanting to do the useful parts without all the theater.</b> Founder-led. Built around the right people for the problem. Every engagement led personally.</p>
<div class="cta-row"><a class="btn" href="/about/">The longer version &rarr;</a></div></div>
</div></div></section>
""" + CTA

page("Extra Medium | Strategy, Growth & AI Studio in Virginia Beach",
     "Extra Medium is a strategy, creative, growth and technology studio in Virginia Beach. We launch, reinvent and grow businesses — and build our own products, led by flagship product SIGNL.",
     "/", "home", home)
print("home done")

# ============ WORK ============
work = """
<section class="hero-media">
<img class="bg" src="/assets/img/bar-friends.jpg" alt="Friends gathered at a local bar, laughing">
<div class="shade"></div>
<div class="wrap"><p class="kicker rv">Work</p>
<h1 class="rv">Done from <span class="it">both sides</span> of the table.</h1>
<p class="lede rv">Built brands from inside the building. Built companies from nothing. Sat across from agencies, founders and executive teams. We know what good advice looks like &mdash; and what survives Monday morning.</p></div>
</section>
<section><div class="wrap">
<div class="flagship tilt rv" style="margin-bottom:64px"><div class="flagship-grid">
<div class="flagship-copy"><span class="badge">From our Labs &middot; Live</span>
<img class="logo" src="/assets/img/signl-logo.png" alt="SIGNL">
<h3 style="font-size:1.7rem;line-height:1.1">Our own product is our newest case study.</h3>
<p>Brand, platform, pricing, creator operations and go-to-market for a two-sided local marketplace &mdash; designed, built and operated by this studio, on our own money. If you&rsquo;re judging whether we can launch yours, start here.</p>
<div class="cta-row"><a class="btn grad-s" href="/labs/signl/">Read the SIGNL case study</a></div></div>
<div class="flagship-media"><img src="/assets/img/creator-cocktail-photo.jpg" alt="A creator photographing a cocktail for a local business"></div>
</div></div>
<p class="kicker rv">Client stories &mdash; scroll the stack</p>
<div class="stack-card rv" style="top:96px;background:linear-gradient(120deg,#ff7a18,#ff3d8a)"><span class="tag">Growth</span><h3 style="font-size:1.9rem;margin-top:10px">The consumer brand that needed a growth system, not more ads</h3>
<p>A high-growth nutritional supplement brand had traction and a scattered set of channels. We took ownership of strategy end to end: investment across Google, Meta, affiliate, influencer, creator, UGC, Reddit and AI-driven channels; creator and affiliate programs built into real acquisition channels; AI across reporting, creative and workflow. <b>Growth became a system with an owner.</b></p></div>
<div class="stack-card rv" style="top:112px;background:linear-gradient(120deg,#ff3d8a,#c86bff)"><span class="tag">Reinvention</span><h3 style="font-size:1.9rem;margin-top:10px">The manufacturer that had to become one brand after an acquisition</h3>
<p>A global radiation protection manufacturer needed global marketing strategy across website, CRM, automation, ecommerce, SEO, paid media and product marketing, plus post-acquisition brand integration. We built the digital foundation, a physician-facing podcast, KOL and education programs, and supported product launches and international expansion.</p></div>
<div class="stack-card rv" style="top:128px;background:linear-gradient(120deg,#2a1220,#571c3f)"><span class="tag">Scale</span><h3 style="font-size:1.9rem;margin-top:10px">The Fortune 500 retailer whose websites and apps had to work harder</h3>
<p>Leading planning, execution and optimization for the websites and apps of three retail banners &mdash; ecommerce, mobile, merchandising, loyalty and seasonal campaigns for millions of customers. <b>Improvements to average order value, engagement, mobile installs and SEO</b> from content strategy, technical optimization and continuous testing.</p></div>
<div class="stack-card rv" style="top:144px;background:linear-gradient(120deg,#ff7a18,#ffb347)"><span class="tag">New revenue</span><h3 style="font-size:1.9rem;margin-top:10px">The music company whose next chapter was enterprise</h3>
<p>A subscription music-licensing business needed a new revenue model. We helped launch its enterprise licensing product, shaped go-to-market with product, engineering and sales leadership, and onboarded early enterprise adopters <b>including Microsoft and Baylor University</b>.</p></div>
<div class="stack-card rv" style="top:160px;background:linear-gradient(120deg,#0aa06e,#3d7bff)"><span class="tag">Launch</span><h3 style="font-size:1.9rem;margin-top:10px">The platform we launched ourselves</h3>
<p>Before Extra Medium, our founder created a digital music platform from idea to launch &mdash; raised seed funding, built the team, onboarded artists and led the marketing that <b>grew it past 900,000 users</b>.</p></div>
<div class="stack-card rv" style="top:176px;background:linear-gradient(120deg,#571c3f,#ff3d8a)"><span class="tag">Build</span><h3 style="font-size:1.9rem;margin-top:10px">The B2B division that needed to exist</h3>
<p>A contract manufacturer wanted to sell a new idea: helping major brands in hospitality, travel, food and beverage, fitness and retail create wellness products under their own names. We built the positioning and website for the division as <b>the invisible engine behind other brands</b>, with clear industry pages and a focused path to partnership.</p></div>
<div class="sec-head rv" style="margin-top:70px"><p class="kicker">The range</p><h2>From a napkin sketch to a <span class="it gtext">Fortune 100 partner.</span></h2>
<p class="lede">Pre-launch startups. Founder-led growth brands. Makers and manufacturers. Fortune 500 retail. Industries: consumer products, ecommerce, healthcare and medical devices, retail, media and broadcast, music and entertainment, hospitality, professional services, technology and SaaS. The thread is ambition, not industry.</p></div>
</div></section>
""" + CTA

page("Work: From Startups to Fortune 100 | Extra Medium",
     "Extra Medium case stories: growth systems, brand reinvention, enterprise launches and our own products, from pre-launch startups to Fortune 100 partners.",
     "/work/", "work", work)

# ============ SERVICES ============
services = """
<section class="hero-media">
<img class="bg" src="/assets/img/kitchen-line.jpg" alt="A busy kitchen line mid-service">
<div class="shade"></div>
<div class="wrap"><p class="kicker rv">The studio</p>
<h1 class="rv">Whatever the medium. <span class="it">Make it matter.</span></h1>
<p class="lede rv">We care more about what moves the business than what department it belongs to. Strategy, creative, growth and technology, practiced together by one small senior team.</p></div>
</section>
<section><div class="wrap"><div class="grid2">
<div class="card rv" id="launch"><img class="thumb" src="/assets/img/chef-flame.jpg" alt="A chef working a flame"><span class="num">Chapter 01</span><h3>Launch</h3><p>For things that don&rsquo;t exist yet, or haven&rsquo;t been introduced properly. Positioning, naming, brand identity, website, go-to-market and product launch &mdash; shaped as one arc, because launching something nobody has searched for yet is a different sport.</p></div>
<div class="card rv" id="reinvent"><img class="thumb" src="/assets/img/street-night.jpg" alt="A city street at night"><span class="num">Chapter 02</span><h3>Reinvent</h3><p>For businesses that moved faster than their brand. Brand strategy, rebranding, messaging and website redesign that close the gap between what the business became and what the market still thinks it is &mdash; without starting from zero.</p></div>
<div class="card rv" id="grow"><img class="thumb" src="/assets/img/cocktails-toast.jpg" alt="Friends toasting with cocktails"><span class="num">Chapter 03</span><h3>Grow</h3><p>Growth marketing with an owner. Paid media, SEO and AI search, ecommerce and Shopify growth, lifecycle and creator channels &mdash; run as one system against revenue, not separate campaigns reporting vanity numbers.</p></div>
<div class="card rv" id="lead"><img class="thumb" src="/assets/img/salon-barber.jpg" alt="Inside a neighborhood salon"><span class="num">Chapter 04</span><h3>Lead</h3><p>Fractional CMO leadership for businesses that need a senior marketing brain without another permanent executive seat. Plus executive and personal branding for the founders and physicians leading them.</p></div>
<div class="card rv" id="intelligence"><span class="num">Chapter 05</span><h3>Intelligence</h3><p>AI consulting, AI agents and automation that connect how a company actually operates &mdash; not another unused tool. Applied AI across marketing, reporting, creative development and workflow, wired into the business instead of demoed at it.</p></div>
<div class="card rv" id="experiences"><span class="num">Chapter 06</span><h3>Experiences</h3><p>Podcasts, events and experiential marketing &mdash; the things people are still talking about a year later. Strategy and production for shows and moments that build a reputation, not just reach.</p></div>
</div></div></section>
<section class="grad-sec"><div class="wrap">
<div class="sec-head rv"><p class="kicker">How engagements work</p><h2>No giant process.</h2>
<p class="lede">You tell us what&rsquo;s going on. We ask questions. We figure out whether we can actually help. If we can, we tell you what the right engagement looks like. If we can&rsquo;t, we tell you that too.</p></div>
<div class="grid3">
<div class="card rv"><span class="num">Shape 01</span><h3>Fractional leadership</h3><p>Senior marketing leadership, embedded, without adding a permanent executive seat. For founder-led and high-growth companies.</p></div>
<div class="card rv" style="transition-delay:.08s"><span class="num">Shape 02</span><h3>Project</h3><p>A defined problem, launch or build with a clear beginning and end &mdash; scoped after the first conversation, priced with a clear range.</p></div>
<div class="card rv" style="transition-delay:.16s"><span class="num">Shape 03</span><h3>Ongoing growth</h3><p>Continuous senior thinking and execution around growth, brand and performance. One owner, one system.</p></div>
</div>
<p class="note rv" style="margin-top:28px">Full capability list: brand strategy &middot; rebranding &middot; growth marketing &middot; fractional CMO &middot; website design &amp; development &middot; ecommerce &amp; Shopify &middot; paid media &middot; SEO &amp; AI search &middot; AI consulting, agents &amp; automation &middot; go-to-market &middot; product launches &middot; executive branding &middot; podcasts &middot; experiential.</p>
</div></section>
""" + CTA

page("Studio: Launch, Reinvent, Grow, Lead | Extra Medium",
     "Extra Medium studio services: launch, reinvention, growth marketing, fractional CMO leadership, AI and experiences — one senior team, three engagement shapes.",
     "/services/", "services", services)

# ============ LABS ============
labs = """
<section class="hero-media">
<video class="bg" autoplay muted loop playsinline poster="/assets/img/cafe-poster.jpg" src="/assets/video/cafe.mp4"></video>
<div class="shade"></div>
<div class="wrap"><p class="kicker rv">Extra Medium Labs</p>
<h1 class="rv">Things we build when <span class="it">nobody hired us to.</span></h1>
<p class="lede rv">Labs is where the studio puts its own money where its advice is. One flagship product, live and operating. A small number of ventures behind it. Nothing else &mdash; a flagship only means something if most things aren&rsquo;t one.</p></div>
</section>
<section><div class="wrap">
<div class="flagship tilt rv"><div class="flagship-grid">
<div class="flagship-copy"><span class="badge">00 &middot; Flagship &middot; Live</span>
<img class="logo" src="/assets/img/signl-logo.png" alt="SIGNL">
<h3 style="font-size:1.8rem;line-height:1.08">Local creator marketing, city by city.</h3>
<p>Influencer marketing skipped local. The creators who move a neighborhood business live there &mdash; and 500 local followers beat 500,000 strangers. A business makes an offer, a creator visits, posts honestly within 48 hours, and every visit is tracked down to register spend.</p>
<div class="stats"><div><b data-count="37">37</b><span>Founding markets</span></div><div><b data-count="8">8</b><span>Countries</span></div><div><b>$299+</b><span>Published pricing</span></div></div>
<div class="cta-row"><a class="btn grad-s" href="/labs/signl/">The full case study</a><a class="btn ink" href="https://joinsignl.com">joinsignl.com</a></div></div>
<div class="flagship-media"><img src="/assets/img/cafe-window-night.jpg" alt="A neighborhood cafe glowing at night"></div>
</div></div>
<p class="note rv">Status, honestly: live platform, founding rosters forming market by market, home market Virginia Beach activating first. Operated by Extra Medium LLC. Pricing, standards and the Visit Guarantee are published on the product site &mdash; because that&rsquo;s how products should behave.</p>
</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><p class="kicker">In development</p><h2>The next <span class="it gtext">bench.</span></h2>
<p class="lede">Three ventures in active development. Everything else we&rsquo;ve explored has been archived off this page &mdash; focus is a feature.</p></div>
<div class="grid3">
<div class="card rv"><span class="num">01 &middot; Prototype &middot; Waitlist open</span><h3>Roon</h3><p>The days you&rsquo;d give anything to have back. A memory-keeping app that turns the photos, videos and voice notes a family already has into stories you can step back into &mdash; because storage isn&rsquo;t the problem. Meaning is.</p><span class="arrow"><a href="https://roonapp.co" style="text-decoration:none;color:inherit">roonapp.co &rarr;</a></span></div>
<div class="card rv" style="transition-delay:.08s"><span class="num">02 &middot; In development</span><h3>JAWNRA</h3><p>The world&rsquo;s music, in motion. A global music discovery and chart platform that measures momentum instead of popularity &mdash; the chart that tells you what&rsquo;s about to win, not what already did.</p><span class="arrow"><a href="https://jawnra.com" style="text-decoration:none;color:inherit">jawnra.com &rarr;</a></span></div>
<div class="card rv" style="transition-delay:.16s"><span class="num">03 &middot; In development</span><h3>hapsta</h3><p>Make something happen. An AI engine for spontaneous real life: tell it what you&rsquo;re looking for and get a Happening &mdash; people, place, activity, time. Software that gets you off the phone and into a room.</p><span class="arrow"><a href="https://hapsta.co" style="text-decoration:none;color:inherit">hapsta.co &rarr;</a></span></div>
</div></div></section>
<div class="band-media"><img data-para="0.10" src="/assets/img/hero-restaurant-night.jpg" alt="A packed restaurant seen through its windows at night">
<div class="cap"><div class="wrap"><p class="kicker light">Why a studio builds its own things</p><h2 style="max-width:22ch">Because it keeps us <span class="it">honest.</span></h2></div></div></div>
<section><div class="wrap"><div class="split">
<div class="prose rv"><h2 style="margin-bottom:20px">Our money first. <span class="it gtext">Then yours.</span></h2>
<p>Labs is where we test our own thinking about launching something nobody has searched for yet and growing a product from zero. Every lesson &mdash; pricing in public, standards as marketing, distribution built into the product &mdash; <b>flows straight back into client work</b>.</p>
<p>It also changes the conversation. We&rsquo;re not theorizing about your launch with your money. We&rsquo;ve made the same decisions with ours.</p>
<div class="cta-row"><a class="btn" href="/contact/">Talk to Labs</a><a class="btn ink" href="mailto:hello@xmedium.co">hello@xmedium.co</a></div></div>
<div class="rv"><img class="ph" src="/assets/img/street-night.jpg" alt="A city street at night"></div>
</div></div></section>
"""

page("Extra Medium Labs | SIGNL, Our Flagship Product",
     "Extra Medium Labs builds the studio's own products. Flagship: SIGNL, the live local creator marketing platform. Plus ventures in development: Roon, JAWNRA and hapsta.",
     "/labs/", "labs", labs)

# ============ SIGNL CASE STUDY ============
signl = """
<section class="hero-media">
<video class="bg" autoplay muted loop playsinline poster="/assets/img/cafe-poster.jpg" src="/assets/video/cafe.mp4"></video>
<div class="shade"></div>
<div class="wrap"><p class="kicker rv">Extra Medium Labs &middot; Flagship &middot; Case study</p>
<img class="rv" src="/assets/img/signl-logo.png" alt="SIGNL" style="height:60px;width:auto;margin-bottom:26px">
<h1 class="rv">Get talked about by the people your city <span class="it">actually follows.</span></h1>
<p class="lede rv">SIGNL is the local creator marketing platform built, branded and operated by Extra Medium. Local businesses comp or pay creators who live in their city to visit and post honestly &mdash; and every visit is tracked.</p>
<div class="cta-row rv"><a class="btn grad-s" href="https://joinsignl.com">Visit joinsignl.com</a><a class="btn ghost" href="https://app.joinsignl.com">Open the app</a></div>
<div class="hero-meta rv">
<div><b>Live</b><span>Platform &amp; founding markets</span></div>
<div><b data-count="37">37</b><span>Founding markets, 8 countries</span></div>
<div><b data-count="500">500</b><span>Followers is enough</span></div>
<div><b>$299&ndash;999</b><span>Published business plans / mo</span></div>
</div></div></section>
<section><div class="wrap"><div class="split">
<div class="prose rv"><p class="kicker">The problem</p><h2 style="margin-bottom:20px">Influencer marketing <span class="it gtext">skipped local.</span></h2>
<p>A neighborhood restaurant doesn&rsquo;t need a creator with two million followers in another state. It needs the 2,000 people within walking distance who decide where Friday night happens &mdash; and those people follow <b>neighbors, not influencers</b>.</p>
<p>Meanwhile local creators with small, fiercely local audiences had no front door: brands couldn&rsquo;t find them, couldn&rsquo;t book them properly, and couldn&rsquo;t tell what a visit brought in.</p>
<p><b>So we built the front door</b> &mdash; a two-sided platform where the standards are the marketing: published pricing, a two-business-day decision on every application, tracked visits, and a Visit Guarantee.</p></div>
<div class="rv"><img class="round" src="/assets/img/cafe-window-night.jpg" alt="A neighborhood cafe glowing at night"></div>
</div></div></section>
<div class="band-media"><video data-para="0.10" autoplay muted loop playsinline poster="/assets/img/hero-poster.jpg" src="/assets/video/hero.mp4"></video>
<div class="cap"><div class="wrap"><p class="kicker light">Built by the studio</p><h2 style="max-width:24ch">Brand. Product. Platform. Pricing. <span class="it">Go-to-market. Ops.</span></h2></div></div></div>
<section><div class="wrap"><div class="split">
<div class="prose rv"><p class="kicker">What we built</p><h2 style="margin-bottom:20px">Everything a launch takes. <span class="it gtext">Ours.</span></h2>
<p><b>Brand &amp; naming</b> &mdash; SIGNL, a one-word invented name with its gradient identity system, designed here.</p>
<p><b>Product &amp; platform</b> &mdash; creator applications with automatic tiering (Neighbors 500&ndash;2k, Locals 2k&ndash;15k, Headliners 15k+, stacked across platforms), business onboarding, and the offer &rarr; visit &rarr; post &rarr; tracked-outcome lifecycle.</p></div>
<div class="prose rv"><p><b>Business model</b> &mdash; two lanes: comped visits, and paid bookings where creators keep 97%. Published plans at $299 / $599 / $999 a month.</p>
<p><b>Go-to-market</b> &mdash; city-by-city founding rosters, hand-picked market by market, home market Virginia Beach first. <b>Operations</b> &mdash; run daily by this studio, under Extra Medium LLC.</p>
<div class="cta-row"><a class="btn" href="/contact/">Want this for your product? &rarr;</a></div></div>
</div></div></section>
<section class="grad-sec"><div class="wrap">
<div class="sec-head rv"><p class="kicker">How a visit works</p><h2>Four steps, <span class="it">no theater.</span></h2></div>
<div class="steps">
<div class="step rv"><b>01 &middot; The offer</b><h3>A business makes an offer</h3><p>A comped dinner, a service, an experience &mdash; or a paid booking at the creator&rsquo;s own rate.</p></div>
<div class="step rv" style="transition-delay:.07s"><b>02 &middot; The visit</b><h3>A local creator shows up</h3><p>Someone from the neighborhood. Their followers are your neighbors too.</p></div>
<div class="step rv" style="transition-delay:.14s"><b>03 &middot; The post</b><h3>They post it honestly</h3><p>One post or reel plus two stories within 48 hours. Disclosed, in their own voice, never a script.</p></div>
<div class="step rv" style="transition-delay:.21s"><b>04 &middot; The proof</b><h3>The business sees what it brought in</h3><p>Every visit tracked. Register spend counted at the till; media value modeled and labeled as modeled.</p></div>
</div></div></section>
<section><div class="wrap">
<div class="sec-head rv"><p class="kicker">Why it&rsquo;s the flagship</p><h2>SIGNL is the studio&rsquo;s <span class="it gtext">proof of work.</span></h2>
<p class="lede">Every discipline we sell is inside this product, exercised on our own budget. When a client asks whether we can launch their thing, SIGNL is the answer we can point at.</p></div>
<div class="grid3">
<a class="card rv" href="https://joinsignl.com/businesses.html"><span class="num">For businesses</span><h3>Put a visit in front of local creators</h3><p>Founding businesses join the list now and activate when their market opens.</p><span class="arrow">joinsignl.com &rarr;</span></a>
<a class="card rv" style="transition-delay:.08s" href="https://joinsignl.com/creators.html"><span class="num">For creators</span><h3>500 followers is enough</h3><p>Free for creators, always. Get comped or paid by the businesses near you.</p><span class="arrow">joinsignl.com &rarr;</span></a>
<a class="card rv" style="transition-delay:.16s" href="/contact/"><span class="num">For your launch</span><h3>Want this done for your product?</h3><p>That&rsquo;s the studio side. Same team, same standards, your budget this time.</p><span class="arrow">Start a conversation &rarr;</span></a>
</div>
<p class="note rv">SIGNL is a product of Extra Medium Labs, operated by Extra Medium LLC. Status: live, in founding-market formation; full platform terms apply at market launch.</p>
</div></section>
"""

page("SIGNL — Flagship Product of Extra Medium Labs",
     "SIGNL is the live local creator marketing platform built and operated by Extra Medium Labs: local businesses comp or pay local creators to visit and post honestly, every visit tracked.",
     "/labs/signl/", "labs", signl)
print("part 2 done")

# ============ ABOUT ============
about = """
<section class="hero-media">
<img class="bg" src="/assets/img/street-night.jpg" alt="A city street at night">
<div class="shade"></div>
<div class="wrap"><p class="kicker rv">About Extra Medium</p>
<h1 class="rv">A studio for businesses becoming <span class="it">who they were meant to be.</span></h1>
<p class="lede rv">Most agencies will tell you what they do. We&rsquo;d rather talk about where you&rsquo;re going. But since you asked &mdash; here is who we are, and why it works.</p></div>
</section>
<section><div class="wrap"><div class="split">
<div class="rv"><img class="round" src="/assets/img/jeff-rimmer.jpg" alt="Jeff Rimmer, founder and principal of Extra Medium"></div>
<div class="prose rv"><p class="kicker">Founder &amp; Principal</p><h2 style="margin-bottom:20px">Jeff <span class="it gtext">Rimmer</span></h2>
<p><b>More than twenty years in marketing, on every side of the table.</b> Inside startups and inside Fortune 100 companies. Founder of several businesses of his own &mdash; including a music platform taken from a blank page to hundreds of thousands of users, and now SIGNL, built in our own Labs. And the outside partner to clients across that same range, from a founder with a napkin sketch to enterprise teams serving millions.</p>
<p>That mix is the point. Jeff can write the positioning, direct the creative, build the growth engine and wire the intelligence underneath it &mdash; and has done each of those jobs for real, with his own budget on the line. Deepest experience: music and entertainment, retail and ecommerce, healthcare and wellness &mdash; three industries where attention is expensive and trust is everything.</p>
<p>He founded Extra Medium to give ambitious businesses one senior partner who thinks like an owner, builds like a studio and measures like an operator. He leads every engagement personally, works from Virginia Beach, and travels regularly to Chicago and the UK.</p>
<div class="cta-row"><a class="btn" href="https://www.linkedin.com/in/jeffrimmer">LinkedIn</a><a class="btn ink" href="/work/">See the work</a></div></div>
</div></div></section>
<section style="background:var(--bg2)"><div class="wrap">
<div class="sec-head rv"><p class="kicker">A word about the name</p><h2>Medium is a compliment <span class="it gtext">nobody wants.</span></h2>
<p class="lede">We believe boring is a choice, and we don&rsquo;t make it. We believe extra isn&rsquo;t too much &mdash; it&rsquo;s the whole point. And great businesses are built when someone connects every medium together: brand and growth, story and intelligence, leadership and experience. The medium changes. The idea doesn&rsquo;t.</p></div>
<div class="sec-head rv" style="margin-bottom:8px"><p class="kicker">How we work</p><h2>Principles, <span class="it gtext">not process decks.</span></h2></div>
<div class="prin">
<div class="rv"><b>01</b><h3>Where you are going, not what you need built</h3><p>Every engagement starts with the destination. The deliverable is decided after we understand the ambition, never before.</p></div>
<div class="rv"><b>02</b><h3>Creative on the surface, structured underneath</h3><p>Memorable work that is also disciplined: clear positioning, clean architecture, honest measurement.</p></div>
<div class="rv"><b>03</b><h3>Operators, not vendors</h3><p>We have owned budgets, teams and P&amp;Ls. We make recommendations we would make with our own money &mdash; and say the uncomfortable thing when it needs saying.</p></div>
<div class="rv"><b>04</b><h3>Connect the dots</h3><p>Brand, growth, technology and experiences are one system. We work across them because that is where the leverage is.</p></div>
<div class="rv"><b>05</b><h3>Real experience only</h3><p>What we publish and advise comes from work we have actually done. No borrowed case studies, no invented results. SIGNL is the standing proof.</p></div>
<div class="rv"><b>06</b><h3>A conversation, not a proposal</h3><p>Engagements begin with a real conversation. If we are not the right fit, we will tell you who might be.</p></div>
</div>
<p class="note rv" style="margin-top:34px">Headquartered in Virginia Beach, Virginia, with presence in Chicago and London. Clients across the US and UK.</p>
</div></section>
""" + CTA

page("About Extra Medium | Studio Founded by Jeff Rimmer",
     "Extra Medium is a founder-led strategy, creative, growth and technology studio founded by Jeff Rimmer — 20+ years on every side of the marketing table, now building SIGNL in its own Labs.",
     "/about/", "about", about)

# ============ CONTACT ============
contact = """
<section class="hero-media" style="min-height:64svh">
<img class="bg" src="/assets/img/cocktails-toast.jpg" alt="Friends toasting with cocktails">
<div class="shade"></div>
<div class="wrap"><p class="kicker rv">Contact</p>
<h1 class="rv">What are you trying to <span class="it">make happen?</span></h1>
<p class="lede rv">A project, a bigger problem, a product of your own you want built the way we built SIGNL &mdash; or Labs business. All reasonable ways to start.</p></div>
</section>
<section><div class="wrap"><div class="split" style="align-items:start">
<div class="rv">
<form class="lead" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/contact/?sent=1">
<input type="hidden" name="form-name" value="contact"><p hidden><label>Don&rsquo;t fill this out: <input name="bot-field"></label></p>
<div><label for="name">Your name</label><input id="name" name="name" required autocomplete="name"></div>
<div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
<div><label for="kind">What is this about?</label><select id="kind" name="kind">
<option>A project for the studio</option><option>A bigger problem / not sure yet</option>
<option>Fractional CMO</option><option>Labs &mdash; SIGNL</option><option>Labs &mdash; partnership or another venture</option><option>Something else</option></select></div>
<div><label for="msg">Tell us what&rsquo;s going on</label><textarea id="msg" name="message" required></textarea></div>
<button class="btn" type="submit">Send it</button>
<p class="note">Usually replies within one business day. If it&rsquo;s urgent, email <a href="mailto:hello@xmedium.co">hello@xmedium.co</a>.</p>
</form></div>
<div class="prose rv">
<img src="/assets/img/em-logo.png" alt="Extra Medium logo" style="width:96px;height:96px;border-radius:22px;margin-bottom:24px">
<p class="kicker">Prefer email?</p><h2 style="margin-bottom:18px">hello@<span class="gtext">xmedium.co</span></h2>
<p><b>Studio</b> &mdash; launches, reinventions, growth systems, fractional leadership.</p>
<p><b>Labs</b> &mdash; SIGNL partnerships, founding markets, venture collaborations.</p>
<p>Virginia Beach (HQ) &middot; Chicago &middot; London. Most engagements run remotely, with in-person time when it matters.</p>
<p class="note">Extra Medium LLC, Virginia Beach, Virginia.</p>
</div>
</div></div></section>
"""

page("Contact | Extra Medium",
     "Start a conversation with Extra Medium — studio projects, fractional CMO, or Labs and SIGNL partnerships. Replies usually within one business day.",
     "/contact/", "contact", contact)

# 404 gets the new treatment too
pathlib.Path(ROOT / "404.html").write_text("""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Not found | Extra Medium</title><link rel="icon" href="/favicon.ico" sizes="any"><link rel="stylesheet" href="/assets/css/site.css">
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;600;700;800&family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet"></head>
<body><section class="hero-media"><img class="bg" src="/assets/img/street-night.jpg" alt="A city street at night"><div class="shade"></div>
<div class="wrap"><p class="kicker">404</p><h1>That page went <span class="it">extra.</span></h1>
<p class="lede">It doesn&rsquo;t exist anymore &mdash; the site was rebuilt around the work and our flagship product. Try one of these:</p>
<div class="cta-row" style="margin-top:28px"><a class="btn" href="/">Home</a><a class="btn ghost" href="/labs/signl/">SIGNL, our flagship</a><a class="btn ghost" href="/work/">Work</a></div>
</div></section></body></html>""")
print("part 3 done")
