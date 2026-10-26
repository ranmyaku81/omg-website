# Page content for the Oahu Medical Group website.
# Each function returns a dict: path, title, description, nav (which menu item is current), body (HTML).
# Run `python3 build.py` after editing.

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
DAY_NAMES = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday"}

# Form endpoint. Create a free form at https://formspree.io, then paste its ID here (looks like "xabcdefg").
FORMSPREE_ID = "YOUR_FORM_ID"


def title_block(crumb, h1, lede=""):
    c = f'<div class="crumb"><a href="/">Home</a> › {crumb}</div>' if crumb else ""
    l = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<div class="wrap page-title">{c}<h1>{h1}</h1>{l}</div>'


def provider_card(p):
    if p.get("photo"):
        img = f'<img src="/assets/img/{p["photo"]}" alt="{p["name"]}" width="532" height="747" loading="lazy">'
    else:
        initials = "".join(w[0] for w in p["name"].replace(",", "").split()[:2])
        img = f'<div class="placeholder" aria-hidden="true">{initials}</div>'
    return f'<li class="provider"><a href="/our_teams/{p["slug"]}/">{img}<h3>{p["name"]}</h3><p>{p["title"]}</p></a></li>'


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
  <div class="card"><h3>Visit</h3><p><a class="big-link" href="/how-to-find-us/">{site['address1']}</a><br>{site['address2']}</p><p class="muted small">Corner of Piʻikoi and Waimanu. Free patient parking. <a href="/how-to-find-us/">Directions</a></p></div>
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
      <h1>Infectious disease specialists for Oʻahu</h1>
      <p class="lede">Seven board-certified physicians caring for patients in the hospital, in our Honolulu clinic, and at home — including home IV antibiotic therapy with nurses on call around the clock.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="tel:{s['phone_tel']}">Call {s['phone']}</a>
        <a class="btn btn-secondary" href="/refer-a-patient/">Refer a patient</a>
      </div>
      <p class="hero-note">New patients are usually referred by their primary care physician. <a href="/prep/">PrEP</a> visits need no referral.</p>
    </div>
    <figure class="hero-photo">
      <img src="/assets/img/clinic-entrance.jpg" alt="Entrance to the Oahu Medical Group clinic on Waimanu Street" width="317" height="442">
      <figcaption>Our clinic entrance is on Waimanu Street, at 88 Piʻikoi. <a href="/how-to-find-us/">Parking and directions</a></figcaption>
    </figure>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <h2>Who is in clinic this week</h2>
      <p class="muted">Physicians round at the hospitals when they are not in clinic.</p>
    </div>
    {week_grid(P)}
    <p class="week-foot">Clinic hours are 8:00 AM – 5:00 PM, Monday to Friday. Schedules change for holidays and travel; call {s['phone']} to confirm a visit with a specific physician.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>How we care for patients</h2><p><a href="/our-services/">All services</a></p></div>
    <div class="grid-3">
      <div class="card"><h3>In the hospital</h3><p>We consult on infections at hospitals across Oʻahu — The Queen’s Medical Center, Kuakini, Straub, Pali Momi, Queen’s – West Oʻahu and Adventist Health Castle — and continue care in clinic after discharge.</p></div>
      <div class="card"><h3>In clinic</h3><p>Outpatient diagnosis and treatment of complex, persistent or recurring infections, with a plan shared back to your referring physician.</p></div>
      <div class="card"><h3>At home</h3><p>Home IV antibiotic therapy (OPAT) coordinated by our own nurses, so you can finish treatment at home instead of an infusion center. A nurse is on call 24 hours a day.</p></div>
    </div>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <div class="section-head"><h2>Our physicians</h2><p><a href="/our-providers/">Bios and clinic hours</a></p></div>
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
      <p><a class="btn btn-secondary" style="border-color:#fff;color:#fff" href="/for-patients/">Patient information</a></p>
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
      <ul class="chips">
        <li>Osteomyelitis (bone infection)</li><li>Prosthetic joint infections</li><li>Cellulitis and skin infections</li><li>Diabetic foot infections</li><li>Bloodstream infections</li><li>Endocarditis and cardiovascular infections</li><li>Pneumonia</li><li>HIV care and PrEP</li><li>Nontuberculous mycobacteria</li><li>Fungal infections</li><li>Recurrent sinusitis</li><li>Transplant-associated infections</li><li>Travel-related infections</li>
      </ul>
      <h2>Hospitals where our physicians consult</h2>
      <ul>
        <li>The Queen’s Medical Center and Queen’s – West Oʻahu</li>
        <li>Kuakini Medical Center</li>
        <li>Straub Medical Center</li>
        <li>Pali Momi Medical Center</li>
        <li>Adventist Health Castle</li>
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
    body = title_block("Our physicians", "Our physicians",
                       "All seven are board-certified in Infectious Diseases and see patients at the hospitals and in our Honolulu clinic.") + f"""
<div class="wrap">
  <ul class="providers">{cards}</ul>
</div>
<section class="section-paper" style="margin-top:3rem">
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
    <a class="card" href="/make-an-appointment/" style="text-decoration:none;color:inherit"><h3>Request an appointment</h3><p>Send us your contact details and we will call you back.</p></a>
    <a class="card" href="/forms/" style="text-decoration:none;color:inherit"><h3>Forms</h3><p>Print and complete the new patient form before your first visit.</p></a>
    <a class="card" href="/how-to-find-us/" style="text-decoration:none;color:inherit"><h3>Parking and directions</h3><p>Where to park, which entrance to use, and a GPS tip.</p></a>
    <a class="card" href="/payments/" style="text-decoration:none;color:inherit"><h3>Pay my bill</h3><p>Pay online using the link for your physician.</p></a>
    <a class="card" href="/frequently-asked-questions/" style="text-decoration:none;color:inherit"><h3>Common questions</h3><p>Referrals, cancellations, insurance and more.</p></a>
    <a class="card" href="/prep/" style="text-decoration:none;color:inherit"><h3>PrEP</h3><p>HIV prevention without a referral.</p></a>
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
    return {"path": "/frequently-asked-questions/", "title": "Common questions", "nav": "patients",
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
    body = title_block("Refer a patient", "Refer a patient",
                       "We see referred patients for outpatient consultation and manage home IV antibiotic therapy. Urgent referrals are usually seen within a few days.") + f"""
<div class="wrap prose">
  <div class="grid-2" style="align-items:start">
    <div>
      <h2>How to refer</h2>
      <ol>
        <li>Complete the <a href="/forms/Patient-Referral-Form.pdf">one-page referral form</a>, or use your own.</li>
        <li>Fax it to <strong>{s['fax']}</strong> with the most recent progress note, relevant cultures and labs, imaging reports, and the patient’s insurance information.</li>
        <li>We call the patient to schedule and fax or send you the consult note after the visit. For urgent problems, call {s['phone']} and ask to speak with the physician on call.</li>
      </ol>
      <h2>What we see most</h2>
      <ul class="chips">
        <li>Bone and joint infections</li><li>Prosthetic joint infections</li><li>Diabetic foot infections</li><li>Bacteremia and endocarditis</li><li>Cellulitis that fails first-line therapy</li><li>Recurrent UTI with resistant organisms</li><li>HIV</li><li>Nontuberculous mycobacteria</li><li>Fungal infections</li><li>Fever of unknown origin</li><li>Pre-travel and post-travel evaluation</li>
      </ul>
      <h2>Home IV antibiotics (OPAT)</h2>
      <p>For patients being discharged on IV antibiotics, our team arranges the home infusion, nursing visits, weekly labs and line care, and follows the patient to the end of therapy. Contact us before discharge so the first home dose is ready when the patient arrives.</p>
    </div>
    <div>
      <div class="card card-ink">
        <h3>Referral fax</h3>
        <p style="font-family:var(--font-serif);font-size:1.6rem;margin:0 0 .5rem;color:#fff">{s['fax']}</p>
        <p>Office {s['phone']}<br>{s['address1']}, {s['address2']}</p>
        <p><a class="btn btn-primary" href="/forms/Patient-Referral-Form.pdf">Referral form (PDF)</a></p>
      </div>
      <div class="card" style="margin-top:1rem">
        <h3>Hospital consults</h3>
        <p>For inpatients, place a consult order in your hospital’s system or page the infectious disease physician on service through the operator.</p>
      </div>
    </div>
  </div>
</div>
"""
    return {"path": "/refer-a-patient/", "title": "Refer a patient", "nav": "refer",
            "description": "How to refer a patient to Oahu Medical Group infectious disease specialists: fax number, referral form, and OPAT coordination.", "body": body}


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
      <h3>Referring physicians</h3>
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
            find_us(ctx), payments(ctx), refer(ctx), contact(ctx), privacy(ctx), terms(ctx)]
    return out
