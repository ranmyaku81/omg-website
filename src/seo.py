# Structured data (schema.org JSON-LD) for search engines.
# Google reads these blocks to understand the practice, its locations, physicians and health content.
# Facts here must match the visible page; edit the page data, not this file, where possible.
import json


def _addr(street, city, zip_):
    return {"@type": "PostalAddress", "streetAddress": street, "addressLocality": city,
            "addressRegion": "HI", "postalCode": zip_, "addressCountry": "US"}


def organization(site, providers):
    d = site["domain"]
    honolulu = {
        "@type": "MedicalClinic",
        "@id": d + "/#honolulu",
        "name": f"{site['name']} — Honolulu",
        "url": d + "/",
        "telephone": "+1-808-531-7111",
        "faxNumber": "+1-808-528-5507",
        "address": _addr("88 Piikoi Street", "Honolulu", "96814"),
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "17:00"}],
        "medicalSpecialty": "InfectiousDisease",
        "image": d + "/assets/img/clinic-entrance.jpg",
        "hasMap": site["maps"],
        "isAcceptingNewPatients": True,
    }
    hilo = {
        "@type": "MedicalClinic",
        "@id": d + "/hilo/#clinic",
        "name": f"{site['name']} — Hilo clinic",
        "url": d + "/hilo/",
        "telephone": "+1-808-531-7111" if not site.get("hilo_phone_tel") else site["hilo_phone_tel"],
        "address": _addr("1190 Waianuenue Avenue", "Hilo", "96720"),
        "containedInPlace": {"@type": "Hospital", "name": "Hilo Benioff Medical Center"},
        "medicalSpecialty": "InfectiousDisease",
        "hasMap": site["hilo_maps"],
        "description": "Infectious disease clinic every other Friday afternoon, first floor Orthopedics office, Hilo Benioff Medical Center.",
    }
    org = {
        "@type": "MedicalOrganization",
        "@id": d + "/#org",
        "name": f"{site['name']}, LLC",
        "alternateName": ["Oahu Medical Group", "Hawaii Infectious Disease Associates"],
        "url": d + "/",
        "logo": d + "/assets/img/favicon.png",
        "telephone": "+1-808-531-7111",
        "faxNumber": "+1-808-528-5507",
        "address": _addr("88 Piikoi Street", "Honolulu", "96814"),
        "medicalSpecialty": "InfectiousDisease",
        "areaServed": [{"@type": "State", "name": "Hawaii"}, {"@type": "Place", "name": "Oahu"}, {"@type": "Place", "name": "Hilo"}],
        "department": [{"@id": d + "/#honolulu"}, {"@id": d + "/hilo/#clinic"}],
        "member": [{"@id": f"{d}/our_teams/{p['slug']}/#physician"} for p in providers],
    }
    website = {"@type": "WebSite", "@id": d + "/#website", "url": d + "/", "name": site["name"], "publisher": {"@id": d + "/#org"}}
    return [org, honolulu, hilo, website]


def physician(site, p):
    d = site["domain"]
    node = {
        "@type": "Physician",
        "@id": f"{d}/our_teams/{p['slug']}/#physician",
        "name": p["name"],
        "url": f"{d}/our_teams/{p['slug']}/",
        "medicalSpecialty": "InfectiousDisease",
        "telephone": "+1-808-531-7111",
        "address": _addr("88 Piikoi Street", "Honolulu", "96814"),
        "parentOrganization": {"@id": d + "/#org"},
        "worksFor": {"@id": d + "/#org"},
    }
    if p.get("photo"):
        node["image"] = f"{d}/assets/img/{p['photo']}"
    hosp = dict(p.get("facts", [])).get("Hospitals")
    if hosp:
        node["hospitalAffiliation"] = [{"@type": "Hospital", "name": h.strip()} for h in hosp.split(",")]
    if p["slug"] == "benjamin-thomas-md":
        node["workLocation"] = [{"@id": d + "/#honolulu"}, {"@id": d + "/hilo/#clinic"}]
    return node


def condition_page(site, c):
    d = site["domain"]
    return {
        "@type": "MedicalWebPage",
        "@id": f"{d}/conditions/{c['slug']}/#page",
        "url": f"{d}/conditions/{c['slug']}/",
        "name": c["name"],
        "description": c["short"],
        "about": {"@type": "MedicalCondition", "name": c["name"]},
        "audience": {"@type": "PeopleAudience", "audienceType": "Patient"},
        "lastReviewed": "2026-10",
        "reviewedBy": {"@id": d + "/#org"},
        "publisher": {"@id": d + "/#org"},
        "inLanguage": "en-US",
    }


def faq(qa_pairs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa_pairs]}


def breadcrumbs(site, trail):
    """trail: list of (name, path)."""
    d = site["domain"]
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": d + p} for i, (n, p) in enumerate(trail)]}


def script(nodes):
    if not nodes:
        return ""
    data = {"@context": "https://schema.org", "@graph": nodes}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"
