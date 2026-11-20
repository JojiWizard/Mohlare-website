"""Generates every page of the Mohlare Group site. Run: python3 build.py
Edit CONFIG and DIVS below, re-run, done."""
CONFIG = dict(
    site="https://www.mohlaregroup.co.za",      # TODO your real domain
    whatsapp="27631340328",
    phone="063 134 0328",
    email="hx16mane@gmail.com",
    area="South Africa",                        # TODO city / province
    hours="Mon - Fri, 08:00 - 17:00",           # TODO
)
FONTS = ("https://fonts.googleapis.com/css2?family=Anton&family=Bodoni+Moda:ital,wght@1,900&family=Cinzel:wght@600"
         "&family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Fraunces:wght@600&family=Oswald:wght@700"
         "&family=Outfit:wght@300;400&family=Space+Grotesk:wght@700&display=swap")

DIVS = [
 dict(k="learn", file="learn.html", name="Mohlare Learn", f="f-learn", img="learn.jpg", live=True,
  tag="Education & Tutoring",
  lead="Seamless tutoring for every learner, from Grade 1 to Grade 12, following the South African CAPS curriculum.",
  pts=["Personal tutoring for children and students", "Grades 1 - 12, Foundation Phase to Matric", "Structured plans, homework help and exam preparation", "Progress updates parents can actually understand"],
  cta="Enrol your child today", cta2="Book a free consultation"),
 dict(k="market", file="market.html", name="Mohlare Market", f="f-market", img="market.jpg", live=False,
  tag="Retail", lead="Proudly South African retail, curated and brought to your door. Our doors open soon.",
  pts=["Local products and local makers", "Simple, trusted shopping", "Launching after Mohlare Learn"],
  cta="Be first through the door", cta2="Join the early list"),
 dict(k="fit", file="fit.html", name="Mohlare Fit", f="f-fit", img="fit.jpg", live=False,
  tag="Fitness & Wellness", lead="Healthy body, healthy mind, healthy soul. Training and wellness built around real life.",
  pts=["Coaching and training programmes", "Wellness for body, mind and soul", "Launching soon"],
  cta="Start your journey", cta2="Join the early list"),
 dict(k="wear", file="wear.html", name="Mohlare Wear", f="f-wear", img="wear.jpg", live=False,
  tag="Fashion", lead="Bold, confident, unmistakably South African. Fashion made to be seen.",
  pts=["Statement pieces and signature collections", "Runway attitude, everyday wear", "Launching soon"],
  cta="Get first look", cta2="Join the early list"),
 dict(k="kgokagano", file="kgokagano.html", name="Mohlare Kgokagano", f="f-kgokagano", img="kgokagano.jpg", live=False,
  tag="Web Design & Tech", lead="Websites and digital tools that connect businesses to their people. Kgokagano means connection.",
  pts=["Business websites and web apps", "Branding and online presence", "Launching soon"],
  cta="Let's connect", cta2="Request a quote"),
]
C = CONFIG
def wa(msg): return f"https://wa.me/{C['whatsapp']}?text=" + msg.replace(" ", "%20")

def head(title, desc, extra=""):
    return f'''<!DOCTYPE html>
<html lang="en-ZA"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#070707">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet"><link rel="stylesheet" href="style.css">{extra}</head><body>'''

HEADER = '''<header class="top"><a class="logo" href="index.html#divisions">MOHLARE GROUP</a>
<nav><a href="learn.html">Learn</a><a href="market.html">Market</a><a href="fit.html">Fit</a><a href="wear.html">Wear</a><a href="kgokagano.html">Kgokagano</a><a href="index.html#contact">Contact</a></nav></header>'''
FOOT = f'''<footer><div class="tagline">South African Reimagined.</div>
<p>&copy; 2026 Mohlare Group. All rights reserved.</p></footer><script src="app.js"></script></body></html>'''

def li(pts): return "".join(f"<li>{p}</li>" for p in pts)

def home():
    ld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Mohlare Group","url":"{C["site"]}","slogan":"South African Reimagined","email":"{C["email"]}"}}</script>'
    s = head("Mohlare Group | South African Reimagined", "Mohlare Group: tutoring from Grade 1 to 12 with Mohlare Learn, plus retail, fitness, fashion and web design coming soon.", ld)
    s += '''<section id="intro"><div class="stack"><div class="name" id="nm" aria-label="Mohlare Group"></div>
<div class="treewrap"><svg class="tree" viewBox="0 0 120 120" aria-hidden="true">
<path pathLength="1" style="--d:0" d="M60 112 C57 94 63 82 60 60"/><path pathLength="1" style="--d:1" d="M60 74 C50 66 40 62 26 54"/>
<path pathLength="1" style="--d:1" d="M60 68 C72 60 84 56 98 48"/><path pathLength="1" style="--d:2" d="M60 90 C52 88 46 86 38 84"/>
<path pathLength="1" style="--d:2" d="M8 46 C26 18 94 18 112 46 C92 34 28 34 8 46Z"/><path pathLength="1" style="--d:3" d="M24 30 C40 14 80 14 96 30"/>
<path pathLength="1" style="--d:3" d="M44 112 H76"/></svg>
<svg class="star" viewBox="0 0 100 100" aria-hidden="true"><path fill="#fff" d="M50 0 C53 34 66 47 100 50 C66 53 53 66 50 100 C47 66 34 53 0 50 C34 47 47 34 50 0Z"/></svg></div></div>
<div class="bottom"><div class="welcome">Welcome</div><div class="tag">South African Reimagined.</div><button class="btn" id="enter">Enter</button></div></section>
''' + HEADER
    s += '''<main><section class="hero"><div class="eyebrow rv">Proudly South African</div><h1 class="rv">Mohlare Group</h1>
<p class="rv">One tree, many branches. Education, retail, fitness, fashion and technology, grown at home and built to stand tall.</p>
<a class="btn solid rv" href="#divisions" style="--accent:#d8b26e">Explore our branches</a></section>
<h2 class="section-title rv" id="divisions">Our Branches</h2>'''
    for d in DIVS:
        badge = '<span class="badge live">Now enrolling</span>' if d["live"] else '<span class="badge">Coming soon</span>'
        s += f'''<article class="div d-{d["k"]} rv"><div class="pic"><img src="img/{d["img"]}" alt="{d["name"]}" loading="lazy"></div>
<div class="txt">{badge}<h2 class="{d["f"]}">{d["name"]}</h2><p class="lead">{d["lead"]}</p><ul>{li(d["pts"])}</ul>
<a class="btn" href="{d["file"]}">{d["cta"]} &rarr;</a></div></article>'''
    s += f'''<section class="contact rv" id="contact"><div class="eyebrow">Get in touch</div><h2 class="section-title" style="margin:0">Let&rsquo;s grow together</h2>
<div class="cards"><div class="card"><b>WhatsApp</b><a href="{wa("Hi Mohlare Group, I would like to find out more")}" target="_blank" rel="noopener">{C["phone"]}</a></div>
<div class="card"><b>Email</b><a href="mailto:{C["email"]}">{C["email"]}</a></div>
<div class="card"><b>Based in</b>{C["area"]}</div><div class="card"><b>Hours</b>{C["hours"]}</div></div></section></main>'''
    return s + FOOT

def division(i):
    d = DIVS[i]; nxt = DIVS[(i + 1) % len(DIVS)]
    s = head(f'{d["name"]} | Mohlare Group', d["lead"]) + HEADER
    s += f'''<main class="d-{d["k"]}"><section class="dhero"><img src="img/{d["img"]}" alt="{d["name"]}"><div>
<div class="eyebrow">{d["tag"]}</div><h1 class="{d["f"]}">{d["name"]}</h1><p>{d["lead"]}</p></div></section><div class="wrap">'''
    if d["k"] == "learn":
        s += '''<h3 class="rv">Mohlare Group offers a stream where you can enrol your child on a seamless tutoring service from Grade 1 to Grade 12.</h3>
<p class="rv" style="color:var(--mute)">Following the standard South African grading (CAPS), our tutors support learners at every stage, for children and for yourself.</p>
<h3 class="rv">Find your grade</h3><div class="cards bands rv">
<div class="card"><b>Grades 1 - 3</b>Foundation Phase: reading, writing and number confidence.</div>
<div class="card"><b>Grades 4 - 6</b>Intermediate Phase: building strong subject foundations.</div>
<div class="card"><b>Grades 7 - 9</b>Senior Phase: subject choices, skills and study habits.</div>
<div class="card"><b>Grades 10 - 12</b>FET Phase: Maths, Sciences, Accounting and Matric exam prep.</div></div>
<h3 class="rv">How it works</h3><ol class="steps rv"><li>Reach out on WhatsApp or email</li><li>A quick chat to understand the learner&rsquo;s needs</li>
<li>A personal tutoring plan for the grade and subjects</li><li>Regular sessions with simple progress updates</li></ol>'''
    else:
        s += f'<h3 class="rv">What to expect</h3><ul class="rv" style="list-style:none;display:grid;gap:8px">{li(d["pts"])}</ul>'
    s += f'''<div class="cta rv"><h3>{d["cta"]}</h3><p style="color:var(--mute);margin-bottom:16px">{"Spaces are open now. Tell us the grade and subjects and we will take it from there." if d["live"] else "This branch is launching soon. Leave a message and we will let you know first."}</p>
<a class="btn solid" target="_blank" rel="noopener" href="{wa("Hi Mohlare Group, I am interested in " + d["name"])}">{d["cta2"]}</a>
<a class="btn" href="mailto:{C["email"]}?subject={d["name"].replace(" ", "%20")}">Email us</a></div></div>
<a class="next" href="{nxt["file"]}"><small>Next branch</small><span class="{nxt["f"]}" style="--accent:{ {"learn":"#e0b35a","market":"#ff5a4d","fit":"#9bd36a","wear":"#f4f0ea","kgokagano":"#59d2ff"}[nxt["k"]] }">{nxt["name"]} &rarr;</span></a></main>'''
    return s + FOOT

open("index.html", "w").write(home())
for i, d in enumerate(DIVS): open(d["file"], "w").write(division(i))
print("built")
