#!/usr/bin/env python3
"""Build the Oahu Medical Group website.

Usage:  python3 build.py
Reads content from src/ and writes finished HTML into docs/ (served by GitHub Pages).
Standard library only; nothing to install.
"""
import html
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "docs"
sys.path.insert(0, str(SRC))

from providers import PROVIDERS, ORDER  # noqa: E402
import pages  # noqa: E402

SITE = {
    "name": "Oahu Medical Group",
    "tagline": "Infectious Disease Specialists",
    "domain": "https://www.hawaiiinfectiousdisease.com",
    "phone": "(808) 531-7111",
    "phone_tel": "+18085317111",
    "fax": "(808) 528-5507",
    "address1": "88 Piʻikoi Street",
    "address2": "Honolulu, HI 96814",
    "maps": "https://www.google.com/maps/search/?api=1&query=88+Piikoi+St,+Honolulu,+HI+96814",
    "year": "2026",
}

NAV = [
    ("about", "About", "/about-us/"),
    ("providers", "Our physicians", "/our-providers/"),
    ("services", "Services", "/our-services/"),
    ("prep", "PrEP", "/prep/"),
    ("patients", "For patients", "/for-patients/"),
    ("refer", "Refer a patient", "/refer-a-patient/"),
    ("contact", "Contact", "/contact-us/"),
]


def e(s):
    return html.escape(s, quote=True)


def head(title, description, path):
    full = f"{title} | {SITE['name']}" if title != SITE["name"] else f"{SITE['name']} — {SITE['tagline']}, Honolulu"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{SITE['domain']}{path}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE['domain']}{path}">
<meta property="og:image" content="{SITE['domain']}/assets/img/clinic-entrance.jpg">
<link rel="icon" href="/assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&family=Source+Serif+4:opsz,wght@8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
</head>"""


def header(active):
    items = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if key == active else ""}>{e(label)}</a></li>'
        for key, label, href in NAV
    )
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <div class="topbar">
      <a class="brand" href="/">
        <img src="/assets/img/favicon.png" alt="" width="40" height="40">
        <span class="brand-name">{SITE['name']}<span class="brand-sub">{SITE['tagline']} · Honolulu</span></span>
      </a>
      <div class="actions">
        <a class="btn btn-secondary" href="/payments/">Pay my bill</a>
        <a class="btn btn-primary" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
        <button class="menu-toggle" aria-expanded="false" aria-controls="primary-nav" onclick="var n=document.getElementById('primary-nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
      </div>
    </div>
    <nav class="primary" id="primary-nav" aria-label="Main">
      <ul>{items}</ul>
    </nav>
  </div>
</header>
<main id="main">"""


def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>{SITE['name']}, LLC</h4>
        <address>{SITE['address1']}<br>{SITE['address2']}</address>
        <ul>
          <li>Phone <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li>
          <li>Fax {SITE['fax']}</li>
          <li><a href="/how-to-find-us/">Parking and directions</a></li>
        </ul>
      </div>
      <div>
        <h4>Practice</h4>
        <ul>
          <li><a href="/about-us/">About</a></li>
          <li><a href="/our-providers/">Our physicians</a></li>
          <li><a href="/our-services/">Services</a></li>
          <li><a href="/prep/">PrEP</a></li>
        </ul>
      </div>
      <div>
        <h4>Patients</h4>
        <ul>
          <li><a href="/make-an-appointment/">Request an appointment</a></li>
          <li><a href="/forms/">Forms</a></li>
          <li><a href="/frequently-asked-questions/">Questions</a></li>
          <li><a href="/payments/">Pay my bill</a></li>
        </ul>
      </div>
      <div>
        <h4>Clinicians</h4>
        <ul>
          <li><a href="/refer-a-patient/">Refer a patient</a></li>
          <li><a href="/forms/Patient-Referral-Form.pdf">Referral form (PDF)</a></li>
          <li><a href="/contact-us/">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© {SITE['year']} {SITE['name']}, LLC. All rights reserved.</span>
      <span><a href="/privacy-policy/">Privacy</a> · <a href="/terms-conditions/">Terms of use</a></span>
    </div>
  </div>
</footer>
</body>
</html>
"""


# BASE_PATH lets the same build run at a sub-folder (the GitHub preview at
# ranmyaku81.github.io/omg-website) and at the domain root (production).
BASE_PATH = os.environ.get("BASE_PATH", "").rstrip("/")


def rebase(html_):
    if not BASE_PATH:
        return html_
    for attr in ('href="/', 'src="/', 'action="/', 'content="/'):
        html_ = html_.replace(attr, attr[:-1] + BASE_PATH + "/")
    html_ = html_.replace('content="0; url=/', 'content="0; url=' + BASE_PATH + "/")
    return html_


def render(page):
    body = header(page.get("nav")) + page["body"] + footer()
    return head(page["title"], page["description"], page["path"]) + "\n<body>\n" + body


def write(path, content):
    dest = OUT / path.strip("/") / "index.html" if path != "/" else OUT / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(rebase(content), encoding="utf-8")
    return dest


def redirect(path, to):
    html_ = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Redirecting</title>
<meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{SITE['domain']}{to}"></head>
<body><p>This page has moved to <a href="{to}">{to}</a>.</p></body></html>"""
    write(path, html_)


def main():
    providers = {p["slug"]: p for p in PROVIDERS}
    ordered = [providers[s] for s in ORDER]
    ctx = {"site": SITE, "providers": ordered, "e": e}

    count = 0
    for page in pages.all_pages(ctx):
        write(page["path"], render(page))
        count += 1

    # Old WordPress paths that no longer exist on the new site
    redirect("/cookie-policy/", "/privacy-policy/")

    # Housekeeping files
    (OUT / "CNAME").write_text("www.hawaiiinfectiousdisease.com\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{SITE['domain']}{p['path']}</loc></url>" for p in pages.all_pages(ctx))
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (OUT / "404.html").write_text(rebase(render({
        "path": "/404.html", "title": "Page not found", "nav": None,
        "description": "That page could not be found.",
        "body": '<div class="narrow page-title"><h1>Page not found</h1><p class="lede">That address doesn’t exist on our site. Try the <a href="/">home page</a> or <a href="/contact-us/">call us</a>.</p></div>',
    })))
    print(f"Built {count} pages into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
