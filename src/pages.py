# Page content for the Oahu Medical Group website.
# Each function returns a dict: path, title, description, nav (which menu item is current), body (HTML).
# Run `python3 build.py` after editing.

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]

ICON = {
    "pin": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "cal": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M8 2v4M16 2v4M3 10h18"/></svg>',
    "card": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg>',
    "doc": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M9 14h6M9 17h4"/></svg>',
    "hospital": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6M12 9v4M10 11h4"/></svg>',
    "person": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/></svg>',
    "home": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8M5 10v10h14V10M10 20v-5h4v5"/></svg>',
}


def days_summary(p):
    """Compact clinic-days line for provider cards, e.g. 'Tue am · Wed pm · alt Fri pm, Hilo'."""
    out = []
    for day, half, note in p.get("week", []):
        s = f"{day} {half}"
        if "alternate" in note:
            s = "alt " + s
        if "Hilo" in note:
            s += ", Hilo"
        out.append(s)
    return " · ".join(out)
DAY_NAMES = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday"}

# Form endpoint. Create a free form at https://formspree.io, then paste its ID here (looks like "xabcdefg").
FORMSPREE_ID = "YOUR_FORM_ID"


def hilo_phone(site):
    """Hilo line if set, else the Honolulu number."""
    if site.get("hilo_phone"):
        return site["hilo_phone"], site["hilo_phone_tel"]
    return site["phone"], site["phone_tel"]


def title_block(crumb, h1, lede=""):
    c = f'<div class="crumb"><a href="/">Home</a> › {crumb}</div>' if crumb else ""
    l = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<div class="wrap page-title">{c}<h1>{h1}</h1>{l}</div>'


def provider_card(p):
    if p.get("photo"):
        img = f'<img src="/assets/img/{p["photo"]}" alt="" width="96" height="96" loading="lazy">'
    else:
        initials = "".join(w[0] for w in p["name"].replace(",", "").split()[:2])
        img = f'<div class="placeholder" aria-hidden="true">{initials}</div>'
    days = days_summary(p) or "Call for clinic days"
    return f'<li class="provider"><a href="/our_teams/{p["slug"]}/">{img}<span><h3>{p["name"]}</h3><p>{days}</p></span></a></li>'


def week_grid(providers):
    cols = []
    for d in DAYS:
        am, pm = [], []
        for p in providers:
            for day, half, note in p.get("week", []):
                if day == d:
                    (am if half == "am" else pm).append((p["short"], p["slug"], note))
        def items(lst, label):
            if not lst:
                return ""
            out = "".join(
                f'<li><a href="/our_teams/{slug}/">{name}</a>{" <em>(" + note + ")</em>" if note else ""}</li>'
                for name, slug, note in lst
            )
            return f'<li><span>{label}</span></li>{out}'
        cols.append(f'<div class="day"><h3>{DAY_NAMES[d]}</h3><ul>{items(am, "Morning")}{items(pm, "Afternoon")}</ul></div>')
    return '<div class="week">' + "".join(cols) + "</div>"


def contact_strip(site):
    return f"""<div class="contact-strip">
  <div class="card"><h3>Call</h3><p><a class="big-link" href="tel:{site['phone_tel']}">{site['phone']}</a></p><p class="muted small">Weekdays during office hours. Fax {site['fax']}.</p></div>
  <div class="card"><h3>Visit</h3><p><a class="big-link" href="/how-to-find-us/">{site['address1']}</a><br>{site['address2']}</p><p class="muted small">Corner of Piʻikoi and Waimanu. Free patient parking. <a href="/how-to-find-us/">Directions</a> · Also <a href="/hilo/">in Hilo</a> every other Friday.</p></div>
  <div class="card"><h3>Request an appointment</h3><p>Most new patients are referred by their primary care physician. PrEP visits need no referral.</p><p><a class="btn btn-quiet" href="/make-an-appointment/">Send a request</a></p></div>
</div>"""


# ---------------------------------------------------------------- pages

def home(ctx):
    s, P = ctx["site"], ctx["providers"]
    cards = "".join(provider_card(p) for p in P)
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Specialists in treating infections — in hospital, in clinic, and at home.</h1>
      <p class="lede">Seven doctors in Honolulu and Hilo. Most patients come to us from their own doctor; call us if you have questions about a referral.</p>
      <ul class="wayfind">
        <li><a href="/how-to-find-us/">{ICON['pin']}Find our office</a></li>
        <li><a href="/our-providers/">{ICON['cal']}Clinic days</a></li>
        <li><a href="/payments/">{ICON['card']}Pay my bill</a></li>
        <li><a href="/refer-a-patient/">{ICON['doc']}Refer a patient</a></li>
      </ul>
      <p class="hero-note"><a href="/prep/">PrEP</a> visits need no referral. On the Big Island? See the <a href="/hilo/">Hilo clinic</a>.</p>
    </div>
    <figure class="hero-photo">
      <img src="/assets/img/clinic-entrance.jpg" alt="Entrance to the Oahu Medical Group clinic on Waimanu Street" width="317" height="442">
      <figcaption><strong>88 Piʻikoi Street, Honolulu.</strong> Enter on Waimanu Street. Free parking in the stalls marked “OMG”. <a href="/how-to-find-us/">Directions</a></figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <h2>Who is in clinic this week</h2>
      <p class="muted">Physicians round at the hospitals when they are not in clinic.</p>
    </div>
    {week_grid(P)}
    <p class="week-foot">Clinic hours are 8:00 AM – 5:00 PM, Monday to Friday. Schedules change for holidays and travel; call {s['phone']} to confirm a visit with a specific physician.</p>
  </div>
</section>

<section class="section-sea">
  <div class="wrap">
    <div class="section-head"><h2>How we can help</h2><p><a href="/our-services/">All services</a></p></div>
    <div class="grid-3">
      <div class="tile tile-sand">{ICON['hospital']}<h3>If you’re in the hospital</h3><p>Your hospital doctor may ask us to see you. We visit daily, and then see you in our clinic after you go home.</p></div>
      <div class="tile tile-sky">{ICON['person']}<h3>If your doctor referred you</h3><p>We call you to set up a visit in Honolulu, or in Hilo every other Friday. Bring your medication list and insurance card.</p></div>
      <div class="tile tile-sea" style="background:#fff">{ICON['home']}<h3>If you need IV antibiotics at home</h3><p>Our nurses teach you the infusion, visit for line care and labs, and are on call day and night. <a href="/home-infusion/">Home infusion guide</a></p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>Our doctors</h2><p><a href="/our-providers/">Bios and the full clinic schedule</a></p></div>
    <ul class="providers">{cards}</ul>
  </div>
</section>

<section class="section-ink">
  <div class="wrap grid-2">
    <div>
      <h2>Referring a patient?</h2>
      <p>Fax a referral with recent notes, labs and imaging to <strong style="color:#fff">{s['fax']}</strong>. We call the patient to schedule and send your office the consult note.</p>
      <p><a class="btn btn-primary" href="/refer-a-patient/">Referral details and form</a></p>
    </div>
    <div>
      <h2>Already a patient?</h2>
      <p>Pay a bill, download new-patient paperwork, or find answers to common questions.</p>
      <p><a class="btn btn-light" href="/for-patients/">Patient information</a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    {contact_strip(s)}
  </div>
</section>
"""
    return {"path": "/", "title": s["name"], "nav": None,
            "description": "Oahu Medical Group is a seven-physician infectious disease practice in Honolulu providing hospital consultation, outpatient care, PrEP and home IV antibiotic therapy.",
            "body": body}


def about(ctx):
    s = ctx["site"]
    body = title_block("About", "About Oahu Medical Group",
                       "An independent infectious disease practice in Honolulu, caring for Oʻahu patients since the practice’s founding by physicians who trained and stayed here.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <p>We diagnose, treat and prevent infections caused by bacteria, viruses and fungi — from pneumonia and cellulitis to HIV, bone and joint infections, and infections that have not responded to first-line treatment. Our seven physicians are board-certified in Infectious Diseases and hold leadership roles in infection prevention and antimicrobial stewardship at Oʻahu’s hospitals.</p>
      <p>Most of our patients come to us from their primary care physician or from a hospital admission. We work alongside that physician: you keep your doctor, and we add the specialist piece — the diagnosis, the antibiotic plan, and the follow-up until the infection is resolved.</p>
      <p>When treatment means weeks of IV antibiotics, our own home-infusion nurses make it possible to go home rather than stay in the hospital or travel to an infusion center.</p>
      <h2>Conditions we treat</h2>
      <p><a href="/conditions/">Read our plain-language guides</a> to the infections we see most.</p>
      <ul class="chips">
        <li>Osteomyelitis (bone infection)</li><li>Prosthetic joint infections</li><li>Cellulitis and skin infections</li><li>Diabetic foot infections</li><li>Bloodstream infections</li><li>Endocarditis and cardiovascular infections</li><li>Pneumonia</li><li>HIV care and PrEP</li><li>Nontuberculous mycobacteria</li><li>Fungal infections</li><li>Recurrent sinusitis</li><li>Transplant-associated infections</li><li>Travel-related infections</li>
      </ul>
      <h2>Where we see patients</h2>
      <ul>
        <li><strong>Honolulu</strong> — our main clinic at 88 Piʻikoi Street, Monday to Friday.</li>
        <li><strong>Hilo</strong> — Dr. Thomas consults on inpatients at Hilo Benioff Medical Center and holds clinic there every other Friday afternoon, and our home-infusion program covers East Hawaiʻi. <a href="/hilo/">Hilo details</a></li>
      </ul>
      <h2>Hospitals where our physicians consult</h2>
      <ul>
        <li>The Queen’s Medical Center and Queen’s – West Oʻahu</li>
        <li>Kuakini Medical Center</li>
        <li>Straub Medical Center</li>
        <li>Pali Momi Medical Center</li>
        <li>Adventist Health Castle</li>
        <li>Hilo Benioff Medical Center, on the Big Island (Dr. Thomas)</li>
      </ul>
    </div>
    <div>
      <img src="/assets/img/office-building.jpg" alt="The Hawaiki Tower office building at 88 Piʻikoi Street" width="315" height="442">
      <div class="card">
        <h3>Oahu Medical Group, LLC</h3>
        <address>{s['address1']}<br>{s['address2']}</address>
        <p class="small muted" style="margin-top:.5rem">Formerly presented online as Hawaii Infectious Disease Associates. Same physicians, same office.</p>
        <p><a href="/our-providers/">Meet the physicians</a></p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/about-us/", "title": "About", "nav": "about",
            "description": "Oahu Medical Group is an independent, seven-physician infectious disease practice in Honolulu.", "body": body}


def providers_page(ctx):
    s, P = ctx["site"], ctx["providers"]
    cards = "".join(provider_card(p) for p in P)
    body = title_block("Our doctors", "Our doctors",
                       "All seven are board-certified in Infectious Diseases and see patients at the hospitals and in our Honolulu clinic; Dr. Thomas also holds clinic in Hilo.") + f"""
<div class="wrap">
  <ul class="providers">{cards}</ul>
</div>
<section class="section-sea" style="margin-top:3rem">
  <div class="wrap">
    <h2>Clinic schedule</h2>
    {week_grid(P)}
    <p class="week-foot">Call {s['phone']} to schedule. Hospital patients are seen daily by the physician on service.</p>
  </div>
</section>
"""
    return {"path": "/our-providers/", "title": "Our physicians", "nav": "providers",
            "description": "Meet the seven board-certified infectious disease physicians of Oahu Medical Group in Honolulu.", "body": body}


def bio(ctx, p):
    s = ctx["site"]
    paras = "".join(f"<p>{t}</p>" for t in p["bio"])
    hours = "".join(f"<li><span>{d}</span><span>{t}</span></li>" for d, t in p["hours"])
    hours_block = f'<div class="hours"><h3>Clinic hours</h3><ul>{hours}</ul></div>' if hours else '<div class="hours"><h3>Clinic hours</h3><p class="small muted" style="margin:0">Call the office for availability.</p></div>'
    facts = "".join(f"<li><span>{k}</span><span>{v}</span></li>" for k, v in p["facts"])
    facts_block = f'<ul class="facts">{facts}</ul>' if facts else ""
    photo = (f'<img src="/assets/img/{p["photo"]}" alt="{p["name"]}" width="532" height="747">' if p.get("photo")
             else '<div class="provider"><div class="placeholder" aria-hidden="true">Photo coming soon</div></div>')
    draft = '<div class="notice"><p>Full biography and clinic hours for Dr. Kim will be added shortly.</p></div>' if p.get("draft") else ""
    body = title_block('<a href="/our-providers/">Our physicians</a>', p["name"], p["title"]) + f"""
<div class="wrap bio-grid">
  <div>
    {photo}
    {hours_block}
    <p style="margin-top:1rem"><a class="btn btn-primary" href="tel:{s['phone_tel']}">Call {s['phone']}</a></p>
    <p class="small"><a href="{p['pay']}" rel="noopener">Pay a bill from {p['short']}</a></p>
  </div>
  <div class="prose">
    {draft}
    {paras}
    {facts_block}
  </div>
</div>
"""
    return {"path": f"/our_teams/{p['slug']}/", "title": p["name"], "nav": "providers",
            "description": f"{p['name']}, infectious disease physician with Oahu Medical Group in Honolulu.", "body": body}


def services(ctx):
    s = ctx["site"]
    body = title_block("Services", "Services",
                       "We follow an infection from diagnosis to cure, wherever the patient is: hospital, clinic or home.") + f"""
<div class="wrap prose">
  <div class="grid-3">
    <div class="card">
      <h3>Hospital consultation</h3>
      <p>When a hospital physician asks us to see a patient, we evaluate the infection, direct testing and antibiotic choice, and follow the patient daily until discharge. After discharge, we see the patient in clinic to confirm the infection is resolving and to adjust or stop treatment.</p>
    </div>
    <div class="card">
      <h3>Outpatient consultation</h3>
      <p>Referred patients are seen in our Honolulu clinic for infections that are complex, slow to resolve, or recurring. We take a thorough history, review prior cultures and imaging, order what is missing, and send a written plan back to the referring physician.</p>
    </div>
    <div class="card">
      <h3>Home IV antibiotic therapy</h3>
      <p>Outpatient parenteral antimicrobial therapy (OPAT) lets patients finish weeks of IV antibiotics at home. Our nurses teach you or a family member to run the infusion, visit for line care and labs, and are on call 24 hours a day. Doses are prepared by the practice and delivered to you.</p>
    </div>
  </div>

  <h2>What to expect at a first visit</h2>
  <ol>
    <li>Your referring physician faxes us a referral with recent notes, labs and imaging. We call you to schedule — usually within a few days for urgent problems.</li>
    <li>Arrive 15 minutes early with your medication list, insurance card, and the completed <a href="/forms/New-Patient-Form.pdf">new patient form</a> if you printed it at home.</li>
    <li>The visit typically runs 45–60 minutes. You leave with a plan, any prescriptions or lab orders, and a follow-up date. Your referring physician receives the consult note.</li>
  </ol>

  <h2>Also offered</h2>
  <ul>
    <li><a href="/conditions/">Guides to the conditions we treat</a>, from bone infections to HIV care.</li>
    <li><a href="/prep/">HIV pre-exposure prophylaxis (PrEP)</a> — no referral needed.</li>
    <li>HIV treatment and long-term care.</li>
    <li>Antimicrobial stewardship and infection-prevention leadership at Oʻahu hospitals.</li>
  </ul>
  <p><a class="btn btn-primary" href="tel:{s['phone_tel']}">Call {s['phone']}</a></p>
</div>
"""
    return {"path": "/our-services/", "title": "Services", "nav": "services",
            "description": "Hospital consultation, outpatient infectious disease care, PrEP and home IV antibiotic therapy (OPAT) in Honolulu.", "body": body}


def prep(ctx):
    s = ctx["site"]
    body = title_block("PrEP", "PrEP: medicine that prevents HIV",
                       "Pre-exposure prophylaxis is a daily pill or a long-acting injection that keeps HIV from taking hold. We prescribe it without a referral.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <h2>How well it works</h2>
      <p>Taken as prescribed, PrEP reduces the risk of getting HIV from sex by about 99%, and from injection drug use by at least 74%. It is much less effective when doses are missed.</p>

      <h2>Who it is for</h2>
      <p>PrEP may be right for you if you test negative for HIV and any of the following apply:</p>
      <ul>
        <li>You have had anal or vaginal sex in the past six months and have a partner with HIV, do not consistently use condoms, or have been diagnosed with an STI in that time.</li>
        <li>You inject drugs, or share needles or other injection equipment.</li>
        <li>You have been prescribed PEP (post-exposure prophylaxis) more than once, or after ongoing exposure.</li>
      </ul>
      <p>You can also choose PrEP if none of these apply to you. If you have a partner with HIV and are planning a pregnancy, PrEP can protect you and your baby before, during and after pregnancy.</p>

      <h2>Starting PrEP with us</h2>
      <p>Call {s['phone']} and ask for a PrEP visit. No referral is needed. The first visit includes an HIV test, kidney function and other baseline labs, and a conversation about which option fits your life. Follow-up visits and HIV testing happen every two to three months while you are on PrEP.</p>
      <p><a class="btn btn-primary" href="tel:{s['phone_tel']}">Call {s['phone']}</a></p>
    </div>
    <div>
      <div class="card">
        <h3>The options</h3>
        <table>
          <tr><th>Medication</th><th>How it is taken</th><th>Who it is approved for</th></tr>
          <tr><td>Truvada® (emtricitabine/tenofovir disoproxil) and generics</td><td>One pill daily</td><td>All adults and adolescents at risk through sex or injection drug use</td></tr>
          <tr><td>Descovy® (emtricitabine/tenofovir alafenamide)</td><td>One pill daily</td><td>Sexually active men and transgender women; not studied for receptive vaginal sex</td></tr>
          <tr><td>Apretude® (cabotegravir)</td><td>Injection every two months</td><td>Adults and adolescents weighing at least 35 kg (77 lb), at risk through sex</td></tr>
          <tr><td>Yeztugo® (lenacapavir)</td><td>Injection twice a year, with two days of pills to start</td><td>Adults and adolescents weighing at least 35 kg (77 lb), at risk through sex</td></tr>
        </table>
        <p class="small muted" style="margin-top:.75rem">Most insurance plans, including Medicaid, cover PrEP and the related visits and labs at no cost. We can help with manufacturer assistance programs if you are uninsured.</p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/prep/", "title": "PrEP", "nav": "prep",
            "description": "HIV pre-exposure prophylaxis (PrEP) in Honolulu: daily pills or long-acting injections, no referral needed.", "body": body}


def for_patients(ctx):
    s = ctx["site"]
    body = title_block("For patients", "For patients",
                       "Everything you need before, during and after a visit.") + f"""
<div class="wrap">
  <div class="grid-3">
    <a class="card" href="/new-patients/"><h3>Your first visit</h3><p>What to bring, what happens, how long it takes.</p></a>
    <a class="card" href="/make-an-appointment/"><h3>Request an appointment</h3><p>Send us your contact details and we will call you back.</p></a>
    <a class="card" href="/forms/"><h3>Forms</h3><p>Print and complete the new patient form before your first visit.</p></a>
    <a class="card" href="/how-to-find-us/"><h3>Parking and directions</h3><p>Where to park, which entrance to use, and a GPS tip.</p></a>
    <a class="card" href="/payments/"><h3>Pay my bill</h3><p>Pay online using the link for your physician.</p></a>
    <a class="card" href="/frequently-asked-questions/"><h3>Common questions</h3><p>Referrals, cancellations, insurance and more.</p></a>
    <a class="card" href="/prep/"><h3>PrEP</h3><p>HIV prevention without a referral.</p></a>
    <a class="card" href="/hilo/"><h3>Hilo clinic</h3><p>Every other Friday afternoon at Hilo Benioff Medical Center.</p></a>
    <a class="card" href="/home-infusion/"><h3>Home IV antibiotics guide</h3><p>When to call, line care, doses, deliveries and labs.</p></a>
  </div>
  <div style="margin-top:2.5rem">{contact_strip(s)}</div>
</div>
"""
    return {"path": "/for-patients/", "title": "For patients", "nav": "patients",
            "description": "Appointments, forms, directions, billing and common questions for Oahu Medical Group patients.", "body": body}


def appointment(ctx):
    s = ctx["site"]
    body = title_block('<a href="/for-patients/">For patients</a>', "Request an appointment",
                       "Tell us how to reach you and we will call to schedule. For anything urgent, please call us directly.") + f"""
<div class="wrap grid-2" style="align-items:start">
  <form class="request" action="https://formspree.io/f/{FORMSPREE_ID}" method="POST">
    <div class="field-row">
      <div class="field"><label for="first">First name</label><input id="first" name="first_name" autocomplete="given-name" required></div>
      <div class="field"><label for="last">Last name</label><input id="last" name="last_name" autocomplete="family-name" required></div>
    </div>
    <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel" required></div>
    <div class="field"><label for="email">Email <span class="hint">Optional</span></label><input id="email" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="when">Best time to call</label>
      <select id="when" name="best_time"><option>Any time during office hours</option><option>Morning (8–12)</option><option>Afternoon (1–5)</option></select></div>
    <div class="field"><label for="who">Do you have a preferred physician? <span class="hint">Optional</span></label>
      <select id="who" name="physician"><option value="">No preference</option>{''.join(f'<option>{p["name"]}</option>' for p in ctx["providers"])}</select></div>
    <div class="field"><label for="type">What is this about?</label>
      <select id="type" name="request_type"><option>New patient — I have a referral</option><option>New patient — I don’t have a referral yet</option><option>PrEP visit</option><option>Existing patient — schedule or change a visit</option><option>Something else</option></select></div>
    <input type="hidden" name="_subject" value="Website appointment request">
    <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
    <p class="small muted">Please don’t include medical details, insurance numbers or your date of birth here. We will collect those by phone or at your visit.</p>
    <button class="btn btn-primary" type="submit">Send request</button>
  </form>
  <div>
    <div class="card">
      <h3>Prefer to call?</h3>
      <p><a class="big-link" href="tel:{s['phone_tel']}">{s['phone']}</a></p>
      <p class="muted small">Monday to Friday, 8:00 AM – 5:00 PM.</p>
    </div>
    <div class="card" style="margin-top:1rem">
      <h3>Already have a Queen’s MyChart account?</h3>
      <p>You can request, change or cancel an appointment with us through MyChart. One of our medical assistants will follow up.</p>
    </div>
    <div class="card" style="margin-top:1rem">
      <h3>Cancellations</h3>
      <p>Please give us 24 hours’ notice if you need to reschedule or cancel.</p>
    </div>
  </div>
</div>
"""
    return {"path": "/make-an-appointment/", "title": "Request an appointment", "nav": "patients",
            "description": "Request an appointment with Oahu Medical Group, infectious disease specialists in Honolulu.", "body": body}


def forms(ctx):
    body = title_block('<a href="/for-patients/">For patients</a>', "Forms",
                       "Print, complete and bring these with you. They are PDFs that open in any browser.") + """
<div class="wrap">
  <div class="grid-2">
    <div class="card">
      <h3>New patient form</h3>
      <p>Medical history, medications, allergies and consent. Completing it at home saves about 15 minutes at your first visit.</p>
      <p><a class="btn btn-primary" href="/forms/New-Patient-Form.pdf">Download new patient form (PDF)</a></p>
    </div>
    <div class="card">
      <h3>Referral form for physicians</h3>
      <p>For referring offices: a one-page referral form to fax with recent notes, labs and imaging.</p>
      <p><a class="btn btn-secondary" href="/forms/Patient-Referral-Form.pdf">Download referral form (PDF)</a></p>
    </div>
  </div>
  <div class="notice" style="margin-top:2rem"><p>Please bring your photo ID, insurance card and a current list of medications to every first visit.</p></div>
</div>
"""
    return {"path": "/forms/", "title": "Forms", "nav": "patients",
            "description": "Download the Oahu Medical Group new patient form and physician referral form.", "body": body}


def faq(ctx):
    s = ctx["site"]
    qa = [
        ("Do I need a referral?", f"<p>For most visits, yes — ask your primary care physician to fax a referral to {s['fax']}. PrEP visits do not need a referral; just call.</p>"),
        ("How do I schedule, change or cancel an appointment?", f"<p>Call {s['phone']} during office hours, or <a href='/make-an-appointment/'>send a request online</a>. If you have a Queen’s MyChart account you can also request changes there and a medical assistant will follow up.</p>"),
        ("What is your cancellation policy?", "<p>Please let us know at least 24 hours in advance if you need to reschedule or cancel.</p>"),
        ("Which insurance plans do you accept?", "<p>We accept most major plans. Call the office with your plan name and we will confirm before your visit.</p>"),
        ("Where do I park?", "<p>Enter the Hawaiki Tower lot from Piʻikoi Street and park in any stall marked “OMG” on your right. Our entrance is around the corner on Waimanu Street. See <a href='/how-to-find-us/'>parking and directions</a>.</p>"),
        ("How long is a first visit?", "<p>Plan on 45–60 minutes. Follow-up visits are usually 15–30 minutes.</p>"),
        ("How do I pay a bill?", "<p>Each physician bills under their own practice entity, so use the link for your physician on the <a href='/payments/'>Pay my bill</a> page. The entity name appears on your statement.</p>"),
        ("Who do I call about home IV antibiotics after hours?", "<p>If you are receiving home infusion through us, a nurse is on call 24 hours a day at the number on your infusion instructions. For emergencies, call 911.</p>"),
    ]
    items = "".join(f'<details class="faq"><summary>{q}</summary><div class="answer">{a}</div></details>' for q, a in qa)
    body = title_block('<a href="/for-patients/">For patients</a>', "Common questions") + f'<div class="wrap">{items}</div>'
    import re as _re
    plain = [(q, _re.sub(r"<[^>]+>", "", a_).strip()) for q, a_ in qa]
    return {"path": "/frequently-asked-questions/", "title": "Common questions", "nav": "patients", "faq": plain,
            "description": "Answers to common questions about referrals, scheduling, insurance, parking and billing at Oahu Medical Group.", "body": body}


def find_us(ctx):
    s = ctx["site"]
    body = title_block('<a href="/for-patients/">For patients</a>', "Parking and directions",
                       f"{s['address1']}, {s['address2']} — on the ground floor of Hawaiki Tower, at the corner of Piʻikoi and Waimanu Streets.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <div class="notice warn"><p><strong>GPS tip.</strong> Navigation apps may send you up the Hawaiki condominium ramp. Don’t take it. For the parking entrance, search for <strong>Westley Rowe LLC, Piʻikoi Street</strong> instead, or use the <a href="{s['maps']}">map link</a> and enter from Piʻikoi.</p></div>
      <h2>Parking</h2>
      <ol>
        <li>Enter the parking lot from Piʻikoi Street. Look for the sign “Parking for Hawaiki Residents, KHON TV, Oahu Medical Group.”</li>
        <li>Immediately after entering, the patient stalls are on your right.</li>
        <li>Park in any stall with the hanging sign “Oahu Medical Group Patients” or “OMG” painted in red on the ground. Parking is free.</li>
      </ol>
      <h2>Walking to the clinic</h2>
      <ol>
        <li>Walk back out of the lot to Piʻikoi Street and turn left, past the KHON2 building.</li>
        <li>At the corner, turn onto Waimanu Street. Our entrance, with the Oahu Medical Group sign, is on your left.</li>
      </ol>
      <h2>Drop-off</h2>
      <p>If someone is dropping you off, they can stop briefly in the ride-share stalls on Waimanu Street, right by our door.</p>
      <h2>Contact</h2>
      <p>Phone <a href="tel:{s['phone_tel']}">{s['phone']}</a> · Fax {s['fax']}</p>
    </div>
    <div>
      <img src="/assets/img/clinic-entrance.jpg" alt="Clinic entrance on Waimanu Street, with the Oahu Medical Group sign above the door" width="317" height="442" style="margin-top:0">
      <p class="small muted">Clinic entrance on Waimanu Street.</p>
      <p><a href="/assets/img/how-to-find-us.jpg">Printable directions sheet with photos</a></p>
    </div>
  </div>
</div>
"""
    return {"path": "/how-to-find-us/", "title": "Parking and directions", "nav": "patients",
            "description": "Parking and walking directions to Oahu Medical Group at 88 Piʻikoi Street, Honolulu.", "body": body}


def payments(ctx):
    P = ctx["providers"]
    seen = set()
    items = []
    for p in P:
        label = p["pay_entity"] or f"{p['name']}"
        key = p["pay"]
        if key in seen:
            # merge physicians who bill under the same entity
            for it in items:
                if it["pay"] == key:
                    it["names"].append(p["name"])
            continue
        seen.add(key)
        items.append({"pay": key, "names": [p["name"]], "entity": p["pay_entity"]})
    lis = ""
    for it in items:
        names = " and ".join(it["names"])
        ent = f"<span>{it['entity']}</span>" if it["entity"] and it["entity"] != names else ""
        lis += f'<li><div><strong>{names}</strong>{ent}</div><a class="btn btn-primary" href="{it["pay"]}" rel="noopener">Pay my bill</a></li>'
    body = title_block('<a href="/for-patients/">For patients</a>', "Pay my bill",
                       "Each physician bills under their own practice entity. Find your physician below; the entity name also appears on your statement.") + f"""
<div class="wrap">
  <ul class="pay-list">{lis}</ul>
  <p class="small muted" style="margin-top:1.5rem">Payment links open a secure CardPointe payment page. Questions about a statement? Call (808) 531-7111.</p>
</div>
"""
    return {"path": "/payments/", "title": "Pay my bill", "nav": "patients",
            "description": "Pay your Oahu Medical Group bill online using the secure link for your physician.", "body": body}


def refer(ctx):
    s = ctx["site"]
    body = title_block("Refer a patient", "For referring clinicians",
                       "Outpatient infectious disease consultation in Honolulu and Hilo, hospital consults across Oʻahu and at Hilo Benioff Medical Center, and a home IV antibiotic (OPAT) program run by our own nurses.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <h2>How to refer</h2>
      <ol>
        <li>Complete the <a href="/forms/Patient-Referral-Form.pdf">one-page referral form</a>, or send your own with a reason for consultation.</li>
        <li>Fax to <strong>{s['fax']}</strong> with the items below.</li>
        <li>We call the patient to schedule and fax your office the consult note after the visit. For urgent problems, call {s['phone']} and ask for the physician on call.</li>
      </ol>

      <h2>What to include</h2>
      <p>The more of this we have before the visit, the less often we have to repeat testing or call your office:</p>
      <ul class="checklist">
        <li>Most recent progress note and problem list, with the specific question you want answered</li>
        <li>Culture results with susceptibilities (blood, urine, wound, bone, joint fluid)</li>
        <li>Imaging reports, and the facility where images can be retrieved</li>
        <li>Recent labs: CBC, creatinine, CRP or ESR, liver enzymes if on antimicrobials</li>
        <li>Antibiotics given so far, with dates and doses</li>
        <li>Allergies and reactions, and current medication list</li>
        <li>Insurance information and the patient’s best phone number</li>
      </ul>

      <h2>When a referral helps most</h2>
      <ul class="chips">
        <li>Bone and joint infections, including diabetic foot</li><li>Prosthetic joint or hardware infections</li><li>Bacteremia and endocarditis</li><li>Infections failing first-line therapy</li><li>Recurrent UTI with resistant organisms</li><li>Any patient who needs IV antibiotics at home</li><li>HIV: new diagnosis, care transfer, or PrEP</li><li>Nontuberculous mycobacteria</li><li>Fungal infections</li><li>Fever of unknown origin</li><li>Infection in immunocompromised patients</li><li>Pre-travel or post-travel evaluation</li>
      </ul>
      <p class="small muted">Not sure a formal consult is needed? Call the office; a brief physician-to-physician conversation is often enough to answer a question about antibiotic choice or duration.</p>

      <h2>Discharging a patient on IV antibiotics</h2>
      <p>For hospitalists and discharge planners: our OPAT program takes over the infusion, nursing visits, weekly labs, line care and physician follow-up through end of therapy, on Oʻahu and in East Hawaiʻi. To make the first home dose happen on the day of discharge, we need:</p>
      <ul class="checklist">
        <li>Infectious disease consult note with the antimicrobial, dose, frequency and planned stop date</li>
        <li>Vascular access placed and documented (PICC or midline, tip position confirmed)</li>
        <li>Most recent susceptibilities, creatinine and weight</li>
        <li>Discharge address, phone, and who will help with infusions at home</li>
        <li>Insurance information for authorization</li>
        <li>24 hours’ notice where possible; same-day discharges can usually be covered on Oʻahu with a morning call</li>
      </ul>
      <p>Call {s['phone']} and ask for the infusion team, or fax the above to {s['fax']} marked “OPAT”.</p>

      <h2>East Hawaiʻi</h2>
      <p>Dr. Thomas consults on inpatients at Hilo Benioff Medical Center and sees referred outpatients there every other Friday afternoon; our home-infusion nurse covers Hilo and the surrounding districts. Fax Hilo referrals to the same number and write “Hilo clinic” on the form. <a href="/hilo/">Hilo clinic details</a></p>
    </div>
    <div>
      <div class="card card-ink">
        <h3>Referral fax</h3>
        <p style="font-family:var(--font-serif);font-size:1.7rem;margin:0 0 .5rem;color:#fff">{s['fax']}</p>
        <p>Office {s['phone']}<br>{s['address1']}, {s['address2']}</p>
        <p><a class="btn btn-light" href="/forms/Patient-Referral-Form.pdf">Referral form (PDF)</a></p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Hospital consults</h3>
        <p>For inpatients, place a consult order in your hospital’s system or page the infectious disease physician on service through the operator. We cover Queen’s, Queen’s – West Oʻahu, Kuakini, Straub, Pali Momi and Adventist Health Castle on Oʻahu, and Dr. Thomas consults at Hilo Benioff Medical Center.</p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>What you get back</h3>
        <p>A consult note after each visit with the diagnosis, antimicrobial plan and stop date, monitoring labs we are following, and when we will see the patient again. We copy you on significant changes.</p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Turnaround</h3>
        <p>Urgent referrals are seen within a few days; routine referrals typically within one to two weeks. Tell us on the form if the patient is being discharged or is deteriorating.</p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/refer-a-patient/", "title": "For referring clinicians", "nav": "refer",
            "description": "How to refer a patient to Oahu Medical Group: fax number, what to include, OPAT discharge checklist, and what to expect back.", "body": body}


def new_patients(ctx):
    s = ctx["site"]
    body = title_block('<a href="/for-patients/">For patients</a>', "Your first visit",
                       "What to bring, what happens, and how long it takes.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <h2>Before you come</h2>
      <ul class="checklist">
        <li>Photo ID and insurance card(s)</li>
        <li>A list of every medication and supplement you take, with doses — or bring the bottles</li>
        <li>Any antibiotics you have taken in the past few months, and whether they helped</li>
        <li>The <a href="/forms/New-Patient-Form.pdf">new patient form</a>, printed and completed if you can</li>
        <li>Names of your other doctors, so we can send them our note</li>
        <li>A family member or friend, if you would like someone to listen with you</li>
      </ul>
      <p>If your doctor referred you, they have usually already sent your records. If you were seen in a hospital, we can get those records ourselves.</p>

      <h2>What happens at the visit</h2>
      <p>Plan on about an hour. We go through the history of the infection in detail — when it started, what has been tried, what the cultures showed — and examine you. We review any imaging and labs, and order what is missing. You leave with a plan in plain language: what we think is going on, how we will treat it, how long it will take, and when we will see you again. Your referring doctor receives the same plan in writing.</p>
      <p>Follow-up visits are shorter, usually 15 to 30 minutes.</p>

      <h2>Insurance and payment</h2>
      <p>We accept most major plans. Call the office with your plan name if you want to confirm before your visit. Each physician bills under their own practice, so your statement and online payment link will show the physician’s practice name. <a href="/payments/">Pay my bill</a></p>

      <h2>Cancellations</h2>
      <p>Please give us 24 hours’ notice if you need to reschedule or cancel, so the time can go to another patient.</p>

      <h2>Your records and privacy</h2>
      <p>You receive our Notice of Privacy Practices at your first visit. To request copies of your records or have them sent elsewhere, fax a signed authorization to {s['fax']} or ask at the front desk.</p>
    </div>
    <div>
      <div class="card">
        <h3>Where</h3>
        <p>{s['address1']}, {s['address2']}<br>Enter on Waimanu Street. Free parking in the stalls marked “OMG”.</p>
        <p><a href="/how-to-find-us/">Parking and directions</a></p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Running late or lost?</h3>
        <p>Call <a href="tel:{s['phone_tel']}">{s['phone']}</a>. If you are more than 15 minutes late we may need to reschedule, but call first.</p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Hilo patients</h3>
        <p>Dr. Thomas sees patients at Hilo Benioff Medical Center every other Friday afternoon. <a href="/hilo/">Hilo clinic</a></p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/new-patients/", "title": "Your first visit", "nav": "patients",
            "description": "What to bring and what to expect at your first visit to Oahu Medical Group, infectious disease specialists in Honolulu.", "body": body}


def hilo(ctx):
    s = ctx["site"]
    ph, tel = hilo_phone(s)
    body = title_block("Hilo clinic", "Hilo clinic",
                       "Infectious disease care on the Big Island: hospital consultation and clinic visits at Hilo Benioff Medical Center, and home IV antibiotic therapy across East Hawaiʻi.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <h2>Clinic visits</h2>
      <p>Dr. Benjamin Thomas sees patients in Hilo every other Friday afternoon, in the Orthopedics office on the first floor of {s['hilo_facility']}. Visits are by appointment; call to find the next clinic date.</p>
      <ul class="facts" style="margin-top:0">
        <li><span>Where</span><span>{s['hilo_facility']}<br>{s['hilo_where']}<br>{s['hilo_address1']}, {s['hilo_address2']} · <a href="{s['hilo_maps']}">Map</a></span></li>
        <li><span>When</span><span>{s['hilo_when']}</span></li>
        <li><span>Physician</span><span><a href="/our_teams/benjamin-thomas-md/">Benjamin Thomas, MD</a></span></li>
        <li><span>Phone</span><span><a href="tel:{tel}">{ph}</a></span></li>
        <li><span>Fax (referrals)</span><span>{s['fax']}</span></li>
      </ul>
      <h2>In the hospital</h2>
      <p>Dr. Thomas also sees patients admitted to Hilo Benioff Medical Center. If you are in the hospital with a serious infection, your hospital team can ask for an infectious disease consultation; he will direct testing and antibiotics, plan any IV therapy you need at home, and see you in the Hilo clinic after you go home — no trip to Honolulu needed.</p>
      <h2>Getting a clinic appointment</h2>
      <p>Ask your primary care physician or hospital team to fax a referral to {s['fax']} and write “Hilo clinic” on it. We call you to schedule.</p>
      <p>If you need to be seen sooner than the next Hilo date, we can usually see you in Honolulu or arrange a telehealth visit; ask when you call.</p>
      <h2>Home IV antibiotics in East Hawaiʻi</h2>
      <p>Our home-infusion program covers Hilo and the surrounding districts. A nurse visits to teach you or a family member the infusion, checks the IV line and draws weekly labs, and the practice delivers your doses. A nurse is on call 24 hours a day.</p>
    </div>
    <div>
      <div class="card">
        <h3>Next clinic date</h3>
        <p>Clinic falls on alternate Fridays. Call <a href="tel:{tel}">{ph}</a> for the next date and to schedule.</p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Honolulu clinic</h3>
        <p>{s['address1']}, {s['address2']}<br>Monday to Friday, all seven physicians.<br><a href="/how-to-find-us/">Parking and directions</a></p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/hilo/", "title": "Hilo clinic", "nav": "patients",
            "description": "Oahu Medical Group in Hilo: infectious disease hospital consultation and an every-other-Friday clinic at Hilo Benioff Medical Center, plus home IV antibiotic therapy across East Hawaiʻi.", "body": body}


def home_infusion(ctx):
    s = ctx["site"]
    body = title_block('<a href="/for-patients/">For patients</a>', "Home IV antibiotics: a guide for patients and families",
                       "What happens when you finish your antibiotic treatment at home with Oahu Medical Group’s infusion nurses. Keep this page, or print it, next to your supplies.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <div class="call-now">
        <h3>Call the nurse on call right away if</h3>
        <ul>
          <li>Fever of 100.4 °F (38 °C) or higher, or shaking chills</li>
          <li>Redness, swelling, pain, warmth or pus where the IV line enters the skin</li>
          <li>Swelling or pain in the arm, shoulder or neck on the side of the line</li>
          <li>The line is leaking, cracked, has pulled out partly, or won’t flush</li>
          <li>Rash, itching, hives, or new diarrhea that is watery or frequent</li>
          <li>You missed a dose, or a dose was damaged, late or not delivered</li>
        </ul>
        <p><strong>Call 911</strong> for trouble breathing, swelling of the face or throat, chest pain, or if the line comes all the way out and bleeding won’t stop with firm pressure.</p>
        <p>The on-call number is on your infusion instructions. A nurse answers 24 hours a day, 7 days a week.</p>
      </div>

      <h2>How the program works</h2>
      <p>Your infectious disease physician has decided you need antibiotics that must be given into a vein, for a set number of weeks. Instead of staying in the hospital or going to an infusion center every day, you receive the doses at home. Oahu Medical Group prepares the doses, delivers them to you, and provides the nurses who teach you, visit you, and watch your progress. Your physician sees you in clinic during treatment and decides when to stop.</p>

      <h2>Your IV line</h2>
      <p>Most patients have a PICC line — a thin, soft tube placed in the upper arm that reaches a large vein near the heart — or a midline, a shorter version. It stays in for the whole course and is removed at the end. The line lets you receive medicine without repeated needle sticks, and blood for your weekly labs can usually be drawn from it.</p>
      <ul>
        <li>Keep the dressing clean, dry and sealed. Your nurse changes it weekly, or sooner if it gets wet or loose.</li>
        <li>Cover the arm with a waterproof sleeve or plastic wrap taped above and below for showers. No baths, swimming or ocean until the line is out.</li>
        <li>Don’t lift more than about 10 pounds with that arm, and avoid blood pressure cuffs and needle sticks on it.</li>
        <li>Flush the line as your nurse taught you, before and after each dose, to keep it open.</li>
      </ul>

      <h2>Giving the dose</h2>
      <p>At your first visit a nurse walks you — and a family member if possible — through every step, and watches you do it until you are comfortable. The method depends on the antibiotic: some run in from a small pump or ball-shaped infuser over 30 minutes to a few hours, some are pushed slowly by syringe, and some run continuously from a pump you carry. Your written instructions list your medicine, the dose, the exact times, and how long each infusion takes. <span class="muted">[Nurses: insert practice-specific steps here, or link the teaching sheet for each delivery method.]</span></p>
      <ul>
        <li>Wash your hands and set up on a clean surface before every dose.</li>
        <li>Check the label: your name, the medicine, and the date. Let a refrigerated dose come to room temperature as instructed.</li>
        <li>Give doses on time. Timing matters more for some antibiotics than others; your instructions say how late is too late and what to do if you miss one.</li>
        <li>Record each dose on your log sheet. Bring it to clinic.</li>
      </ul>

      <h2>Deliveries and supplies</h2>
      <p>Doses are delivered to your home on a schedule — usually weekly, sometimes more often for medicines that don’t keep long. Keep them in the refrigerator unless told otherwise, away from the freezer section, and don’t use a dose that looks cloudy, discolored or has particles in it. If a delivery hasn’t arrived when expected, call the office before you run out. Used needles and syringes go in the sharps container we give you; we take the full container back. <span class="muted">[Confirm delivery days and the Hilo delivery arrangement.]</span></p>

      <h2>Nurse visits and labs</h2>
      <p>A nurse visits at least weekly to change your dressing, check the line and draw blood. The blood tests look for side effects of the antibiotic on your kidneys, liver and blood counts, and for some medicines measure the drug level. Your physician reviews every result; we call you if a dose needs to change. Please keep your phone on and let us know if you will be away from home on a visit day.</p>

      <h2>Side effects</h2>
      <p>Each antibiotic has its own common side effects and your instructions describe yours. In general, mild nausea, a metallic taste, or soft stools are common and manageable; tell the nurse so we can help. Watery or frequent diarrhea, a rash, ringing in the ears, dizziness, or tingling in the hands and feet are reasons to call the same day. Never stop the antibiotic on your own — call us first.</p>

      <h2>Daily life</h2>
      <ul>
        <li>You can work, drive and walk as your energy allows; many people return to normal activity within the first week.</li>
        <li>Alcohol: avoid it with certain antibiotics; your instructions will say. Ask before taking any new medicine or supplement, including over-the-counter ones.</li>
        <li>Travel between islands is possible with planning; tell us at least a week ahead so doses and nursing can be arranged.</li>
        <li>Keep every clinic appointment. Your physician decides the stop date based on how you are doing, the labs, and sometimes repeat imaging.</li>
      </ul>

      <h2>Finishing treatment</h2>
      <p>When the course is complete, a nurse removes the line — it takes a few minutes and is not painful — and you keep a small dressing on for a day. Your physician sees you in clinic a few weeks later to confirm the infection has stayed away. Call us after treatment ends if any of the original symptoms return.</p>

      <p class="small muted">Draft for review by the Oahu Medical Group infusion nursing team before publication. Replace bracketed notes with practice-specific instructions. Last edited October 2026.</p>
    </div>
    <div>
      <div class="card card-ink">
        <h3>Nurse on call</h3>
        <p style="font-family:var(--font-serif);font-size:1.4rem;margin:0 0 .5rem;color:#fff">See your infusion instructions</p>
        <p>24 hours a day, 7 days a week.<br>Office {s['phone']}, weekdays.</p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Keep handy</h3>
        <ul class="checklist" style="margin:0">
          <li>Your written infusion instructions</li>
          <li>Dose log sheet</li>
          <li>Thermometer</li>
          <li>Waterproof arm cover</li>
          <li>Sharps container</li>
          <li>Next clinic appointment date</li>
        </ul>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>East Hawaiʻi patients</h3>
        <p>Our home-infusion nurse covers Hilo and the surrounding districts, and Dr. Thomas follows you at the <a href="/hilo/">Hilo clinic</a>.</p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Print this guide</h3>
        <p>Use your browser’s Print command; the page is laid out to print cleanly on letter paper.</p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/home-infusion/", "title": "Home IV antibiotics guide", "nav": "patients",
            "description": "A guide for Oahu Medical Group patients receiving IV antibiotics at home: when to call, caring for your PICC line, giving doses, deliveries, labs and side effects.", "body": body}


def conditions_index(ctx):
    s = ctx["site"]
    cards = "".join(f'<a class="card" href="/conditions/{c["slug"]}/"><h3>{c["name"]}</h3><p>{c["short"]}</p></a>' for c in ctx["conditions"])
    body = title_block("Conditions", "Conditions we treat",
                       "Plain-language guides to the infections we see most, written by our physicians for patients and families. They describe what to expect in general; your own plan may differ.") + f"""
<div class="wrap">
  <div class="grid-2">{cards}</div>
  <p class="muted" style="margin-top:2rem">We also treat pneumonia, urinary infections with resistant organisms, infections in transplant and chemotherapy patients, sinus infections that keep returning, travel-related illness, and fevers without an obvious cause. If your condition isn’t listed, ask your doctor to call us.</p>
</div>
"""
    return {"path": "/conditions/", "title": "Conditions we treat", "nav": "services",
            "description": "Plain-language guides from Oahu Medical Group to osteomyelitis, prosthetic joint infection, diabetic foot infection, endocarditis, cellulitis, NTM, fungal infections and HIV care.", "body": body}


def condition_page(ctx, c):
    s = ctx["site"]
    secs = "".join(f"<h2>{h}</h2>{html_}" for h, html_ in c["sections"])
    calls = "".join(f"<li>{x}</li>" for x in c["calls"])
    body = title_block('<a href="/conditions/">Conditions</a>', c["name"], c["short"]) + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      {secs}
      <div class="call-now">
        <h3>Call us if</h3>
        <ul>{calls}</ul>
        <p style="margin-top:1rem"><strong>{s['phone']}</strong> during office hours. Patients on home IV therapy can reach a nurse any time at the number on their infusion instructions. In an emergency, call 911.</p>
      </div>
      <p class="small muted">This page is general information from Oahu Medical Group and is not a substitute for advice from your own physician. Reviewed by our physicians; last updated October 2026.</p>
    </div>
    <div>
      <div class="card">
        <h3>Seeing us about this</h3>
        <p>Most patients are referred by their primary care physician or hospital team. Ask them to fax a referral to {s['fax']}.</p>
        <p><a href="/new-patients/">What to expect at a first visit</a></p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Treatment at home</h3>
        <p>Many of these infections are treated with IV antibiotics at home through our infusion program, with nurses on call around the clock.</p>
        <p><a href="/home-infusion/">Home infusion guide</a></p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Other conditions</h3>
        <ul style="padding-left:1.1rem;margin:0">{''.join(f'<li><a href="/conditions/{o["slug"]}/">{o["name"]}</a></li>' for o in ctx["conditions"] if o["slug"] != c["slug"])}</ul>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": f"/conditions/{c['slug']}/", "title": c["name"], "nav": "services",
            "description": f"{c['name']}: what it is, how it is diagnosed and treated, and when to call. From the infectious disease physicians of Oahu Medical Group, Honolulu.", "body": body}


def contact(ctx):
    s = ctx["site"]
    body = title_block("Contact", "Contact us") + f"""
<div class="wrap">
  {contact_strip(s)}
  <div class="grid-2" style="margin-top:1.5rem;align-items:start">
    <div class="card">
      <h3>Office hours</h3>
      <ul class="facts" style="margin-top:0">
        <li><span>Monday – Friday</span><span>8:00 AM – 5:00 PM</span></li>
        <li><span>Saturday – Sunday</span><span>Closed</span></li>
      </ul>
      <p class="small muted" style="margin-top:.75rem">Patients on home IV therapy: a nurse is on call 24 hours a day at the number on your infusion instructions.</p>
    </div>
    <div class="card">
      <h3>Hilo clinic</h3>
      <p>{s['hilo_facility']}, {s['hilo_where'].lower()}<br>{s['hilo_address1']}, {s['hilo_address2']}</p>
      <p class="small muted">{s['hilo_when']}, Dr. Thomas. Phone <a href="tel:{hilo_phone(s)[1]}">{hilo_phone(s)[0]}</a>. <a href="/hilo/">Details</a></p>
      <h3 style="margin-top:1rem">Referring physicians</h3>
      <p>Fax referrals to {s['fax']}. See <a href="/refer-a-patient/">how to refer</a>.</p>
      <h3 style="margin-top:1rem">Medical records</h3>
      <p>Requests for records can be faxed to {s['fax']} with a signed authorization.</p>
    </div>
  </div>
</div>
"""
    return {"path": "/contact-us/", "title": "Contact", "nav": "contact",
            "description": "Contact Oahu Medical Group: phone, fax, address and office hours in Honolulu.", "body": body}


def privacy(ctx):
    s = ctx["site"]
    body = title_block("", "Website privacy") + f"""
<div class="narrow prose">
  <p>This page describes how this website handles information. How we protect your medical information as a patient is covered by our Notice of Privacy Practices, which you receive at your first visit and can request from the office at any time.</p>
  <h2>What this website collects</h2>
  <p>Browsing this site does not require an account and we do not use analytics or advertising trackers. The site sets no cookies of its own.</p>
  <p>If you use the appointment request form, we receive the name, phone number, email address and visit type you enter. The form is delivered to our office by a form-processing service and used only to contact you about scheduling. We ask you not to enter medical details, insurance numbers or your date of birth in the form.</p>
  <h2>Links to other sites</h2>
  <p>Bill payment links go to CardPointe, a payment processor, which has its own privacy policy. Medication links go to manufacturer or government websites.</p>
  <h2>Questions</h2>
  <p>Contact our office at {s['phone']} or write to {s['name']}, LLC, {s['address1']}, {s['address2']}.</p>
</div>
"""
    return {"path": "/privacy-policy/", "title": "Website privacy", "nav": None,
            "description": "How the Oahu Medical Group website handles information.", "body": body}


def terms(ctx):
    s = ctx["site"]
    body = title_block("", "Terms of use") + f"""
<div class="narrow prose">
  <p>The information on this website is general and educational. It is not medical advice and does not create a physician–patient relationship. For advice about your own health, see your physician, and in an emergency call 911.</p>
  <p>Submitting a request through this website does not guarantee an appointment; we will confirm by phone.</p>
  <p>Text, photographs and graphics on this site belong to {s['name']}, LLC and may not be reused without permission. Medication names are trademarks of their manufacturers.</p>
</div>
"""
    return {"path": "/terms-conditions/", "title": "Terms of use", "nav": None,
            "description": "Terms of use for the Oahu Medical Group website.", "body": body}


def all_pages(ctx):
    out = [home(ctx), about(ctx), providers_page(ctx)]
    out += [bio(ctx, p) for p in ctx["providers"]]
    out += [services(ctx), prep(ctx), for_patients(ctx), appointment(ctx), forms(ctx), faq(ctx),
            find_us(ctx), payments(ctx), refer(ctx), hilo(ctx), new_patients(ctx), home_infusion(ctx), conditions_index(ctx)]
    out += [condition_page(ctx, c) for c in ctx["conditions"]]
    out += [contact(ctx), privacy(ctx), terms(ctx)]
    return out
