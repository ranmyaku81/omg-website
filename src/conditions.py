# Plain-language condition pages. Each physician should review the pages in their area before launch.
# Fields: slug, name, short (for the index), sections: list of (heading, html), calls: list of "call us if" items.
# Run `python3 build.py` after editing.

CONDITIONS = [
    {
        "slug": "osteomyelitis",
        "name": "Osteomyelitis (bone infection)",
        "short": "Infection inside a bone, often after a wound, surgery or a long-standing ulcer.",
        "sections": [
            ("What it is", "<p>Osteomyelitis is an infection inside a bone. Bacteria reach the bone through a wound or ulcer that goes deep enough, through surgery or a fracture, or occasionally through the bloodstream. Because bone has a limited blood supply, antibiotics reach it slowly and the infection can smolder for weeks or months. In Hawaiʻi we most often see it in the feet of people with diabetes, in the spine, and after orthopedic surgery.</p>"),
            ("How we diagnose it", "<p>We look at the wound and the bone around it, and usually order imaging — an X-ray first, often an MRI. Blood tests show how much inflammation there is. The most useful test is a sample of the bone itself, taken by a surgeon or a radiologist, because it tells us exactly which organism is present and which antibiotics will work. We try to get that sample before antibiotics start whenever it is safe to wait.</p>"),
            ("How we treat it", "<p>Treatment is a course of antibiotics chosen for the specific organism, usually lasting six weeks or more. Many patients need IV antibiotics for part or all of that time, which we provide at home through our infusion program rather than in the hospital. Some infections also need surgery to remove dead bone or hardware; we work with your surgeon on the timing. We check labs regularly during treatment to watch for side effects and to confirm the infection is responding.</p>"),
            ("What to expect", "<p>Improvement is gradual: pain and drainage ease over the first weeks, and blood tests fall toward normal. We see you in clinic during treatment and again after antibiotics stop, because a small number of bone infections return and are easier to treat when caught early. Good blood sugar control, pressure relief for foot ulcers, and not smoking all improve the chance of a lasting cure.</p>"),
        ],
        "calls": ["New or worsening pain, redness or swelling around the bone", "Drainage from a wound that had been closing", "Fever or chills", "Any side effect from your antibiotic, such as rash, diarrhea or nausea that keeps you from eating"],
    },
    {
        "slug": "prosthetic-joint-infection",
        "name": "Prosthetic joint infection",
        "short": "Infection around an artificial hip, knee or shoulder.",
        "sections": [
            ("What it is", "<p>An artificial joint can become infected soon after surgery or years later, when bacteria from elsewhere in the body settle on the implant. Bacteria form a coating called biofilm on the metal and plastic that protects them from antibiotics and the immune system, which is why these infections rarely clear with antibiotics alone.</p>"),
            ("How we diagnose it", "<p>Pain in a joint that had been working well, swelling, warmth, drainage or a wound that will not heal are the usual signs. We check blood inflammation markers and, most importantly, sample fluid from the joint so the organism can be grown in the laboratory. Imaging helps show whether the implant has loosened.</p>"),
            ("How we treat it", "<p>Treatment is a partnership between your orthopedic surgeon and us. Depending on how long the infection has been present and how well the implant is fixed, the surgeon may wash out the joint and exchange the plastic parts, or remove and later replace the implant. We direct the antibiotics around that surgery: usually several weeks of IV therapy, often given at home, sometimes followed by a longer course of pills. Which antibiotic and for how long depends on the organism grown from the joint.</p>"),
            ("What to expect", "<p>Recovery takes months and involves both infection treatment and rehabilitation. We follow you in clinic through the antibiotic course and afterwards. Most patients keep a functioning joint; the chance of cure is highest when infection is recognized early, so do not wait on a joint that has become newly painful.</p>"),
        ],
        "calls": ["New pain, swelling or warmth in a replaced joint", "Drainage or an opening in the surgical scar", "Fever", "Antibiotic side effects"],
    },
    {
        "slug": "diabetic-foot-infection",
        "name": "Diabetic foot infection",
        "short": "Infected ulcers and wounds on the feet of people with diabetes.",
        "sections": [
            ("What it is", "<p>Diabetes can reduce feeling in the feet and slow healing, so a blister or small cut can become an ulcer, and an ulcer can become infected without much pain to warn you. Infection can spread into the soft tissue and down to the bone. Caught early, most foot infections are treated without hospitalization or surgery; caught late, they are the leading cause of amputation.</p>"),
            ("How we diagnose it", "<p>We examine the wound carefully, including how deep it goes and whether bone can be felt at its base. Imaging looks for bone involvement and gas or abscess in the tissue. A culture from deep in the wound, rather than from the surface, tells us which bacteria to treat. We also check the circulation in the foot, because antibiotics cannot work in tissue without blood flow.</p>"),
            ("How we treat it", "<p>Mild infections are treated with oral antibiotics, pressure relief and wound care. Deeper infections may need IV antibiotics, which we provide at home, and sometimes surgery to drain pus or remove infected bone. If circulation is poor we involve a vascular specialist. Antibiotic courses range from one to two weeks for soft-tissue infection to six weeks or more when bone is involved.</p>"),
            ("What to expect", "<p>Healing depends as much on offloading the wound, blood sugar control and footwear as on the antibiotic. We coordinate with your primary care physician, podiatrist and wound clinic, and see you until the wound has closed and stayed closed. Checking your feet daily and seeing someone promptly about any new sore is the best way to avoid a repeat.</p>"),
        ],
        "calls": ["Redness spreading up the foot or leg", "New drainage, odor or a wound getting deeper", "Fever, or blood sugars suddenly running high", "A foot that is pale, cold or newly painful at rest"],
    },
    {
        "slug": "bloodstream-infection-endocarditis",
        "name": "Bloodstream infection and endocarditis",
        "short": "Bacteria in the blood, and infection of the heart valves.",
        "sections": [
            ("What it is", "<p>A bloodstream infection (bacteremia) means bacteria are circulating in the blood. It usually starts somewhere else — a urinary infection, a skin infection, an IV line, a dental source — and can seed other sites. Endocarditis is infection of the heart valves or the lining of the heart, and is the most serious form, because bacteria growing on a valve can damage it and break off into the circulation.</p>"),
            ("How we diagnose it", "<p>Blood cultures identify the organism. Depending on which bacteria is found, we look for where it came from and where it may have spread: an ultrasound of the heart (echocardiogram), imaging of the spine or other sites if there is pain, and repeat blood cultures to confirm the blood has cleared. Certain bacteria, especially <em>Staphylococcus aureus</em>, always get a full evaluation because they so often involve the heart or bone.</p>"),
            ("How we treat it", "<p>Treatment is IV antibiotics, usually started in the hospital and continued at home through our infusion program. Length depends on the organism and whether the heart or bone is involved: two weeks for a simple bloodstream infection, four to six weeks for endocarditis or a deep source. Some patients with endocarditis need heart surgery to repair or replace a damaged valve; we work closely with cardiology and cardiac surgery on that decision. Removing the source — an infected line, an abscess — is as important as the antibiotic.</p>"),
            ("What to expect", "<p>We see you in clinic during home therapy to review labs, check the IV line and watch for complications, and again after treatment ends. If you have had endocarditis, you will need antibiotics before certain dental procedures in the future, and we will give you a card explaining this.</p>"),
        ],
        "calls": ["Fever or chills returning after they had settled", "New shortness of breath, chest pain, or swelling of the legs", "Sudden weakness, trouble speaking, vision change or severe headache — call 911", "New back pain, joint pain or a painful area under the skin"],
    },
    {
        "slug": "cellulitis",
        "name": "Cellulitis and skin infections",
        "short": "Infection of the skin and the tissue beneath it, including abscesses and infections that keep returning.",
        "sections": [
            ("What it is", "<p>Cellulitis is a bacterial infection of the skin and the layer beneath it: an area that is red, warm, swollen and tender, often on the lower leg. Bacteria enter through a crack, scratch, insect bite, athlete’s foot or a wound. An abscess is a collection of pus under the skin. Most cases are treated by primary care; we see people whose infection is severe, is not responding, keeps coming back, or occurs in someone with a weakened immune system.</p>"),
            ("How we diagnose it", "<p>The diagnosis is usually made by examination. We look for the entry point, for pus that needs draining, and for conditions that mimic cellulitis, such as a blood clot, gout, or inflammation from poor circulation, which are often mistaken for infection and treated with antibiotics that do not help. Cultures are useful when there is pus or an open wound.</p>"),
            ("How we treat it", "<p>Uncomplicated cellulitis responds to five to ten days of oral antibiotics; abscesses need to be drained. Severe infections, or infections in people who cannot take pills, are treated with IV antibiotics, which can often be given at home. For people with repeated episodes, we treat the underlying cause — chronic leg swelling, athlete’s foot, skin breakdown — and sometimes use a low-dose preventive antibiotic.</p>"),
            ("What to expect", "<p>Redness often spreads slightly in the first day of treatment before it improves, and can take one to two weeks to fade fully. Elevating the leg speeds recovery. We follow up to confirm the infection has cleared and to put prevention in place if this has happened before.</p>"),
        ],
        "calls": ["Redness spreading quickly, or streaks running up the limb", "Severe pain out of proportion to what you see, or skin turning dark or blistering — go to an emergency department", "Fever, confusion or feeling very unwell", "No improvement after two days of antibiotics"],
    },
    {
        "slug": "nontuberculous-mycobacteria",
        "name": "Nontuberculous mycobacteria (NTM)",
        "short": "Slow-growing environmental bacteria that infect the lungs, skin or soft tissue, common in Hawaiʻi.",
        "sections": [
            ("What it is", "<p>Nontuberculous mycobacteria are relatives of the tuberculosis bacterium that live in soil and water, including household water. They are not spread from person to person. Hawaiʻi has one of the highest rates of NTM lung disease in the country. NTM most often cause a slow lung infection in people with underlying lung conditions or a particular slender body type, and can also infect skin and soft tissue after an injury, surgery or a cosmetic procedure.</p>"),
            ("How we diagnose it", "<p>Lung disease shows up as a chronic cough, fatigue, weight loss or repeated chest infections, with characteristic changes on a CT scan. Diagnosis requires growing the organism from sputum or a bronchoscopy sample, usually more than once, because NTM can also be present without causing disease. Skin infections are diagnosed by biopsy and culture. These cultures take weeks to grow.</p>"),
            ("How we treat it", "<p>Not everyone with NTM needs treatment; for mild lung disease, monitoring and airway clearance may be the right approach. When treatment is needed, it involves a combination of two to four antibiotics taken for a year or more — typically twelve months after the sputum turns negative — with regular monitoring of hearing, vision, liver and kidney function. Some infections require an inhaled or IV antibiotic as well. We make this decision with you, weighing symptoms, scan changes and the side effects of long treatment.</p>"),
            ("What to expect", "<p>NTM treatment is a long commitment and we see you regularly throughout, with sputum cultures every one to two months to track the response. Many patients improve substantially; some have the infection return and need another course. Reducing exposure — avoiding hot tubs and letting showers run hot, for example — may lower the chance of reinfection.</p>"),
        ],
        "calls": ["Ringing in the ears or any change in hearing or vision", "Yellowing of the eyes, dark urine or persistent nausea", "Coughing up blood", "Fever or worsening breathlessness"],
    },
    {
        "slug": "fungal-infections",
        "name": "Fungal infections",
        "short": "Serious infections caused by yeasts and molds, usually in people with weakened immunity or after surgery.",
        "sections": [
            ("What it is", "<p>Fungi are everywhere, and most fungal infections are minor, such as thrush or athlete’s foot. The infections we treat are the invasive ones: yeast (<em>Candida</em>) in the bloodstream or around an implant, molds such as <em>Aspergillus</em> in the lungs or sinuses, and <em>Cryptococcus</em> in the lungs or around the brain. They occur mainly in people whose immune system is weakened by chemotherapy, transplant medicines, steroids, uncontrolled diabetes or advanced HIV, and in people who have been very ill in intensive care.</p>"),
            ("How we diagnose it", "<p>Fungal infections can be hard to prove. We use blood cultures, blood tests that detect parts of the fungus, imaging, and often a biopsy or sample from the infected site. Because the fungi grow slowly in the laboratory, we sometimes have to start treatment before the results are final.</p>"),
            ("How we treat it", "<p>Antifungal medicines are chosen for the specific fungus and may be given by mouth or by IV, sometimes at home. Courses run from two weeks for a bloodstream yeast infection to many months for mold or <em>Cryptococcus</em>. Several antifungals interact with other medicines or need blood-level monitoring, so we review every medication you take and check levels and liver function during treatment. Removing an infected line or draining an abscess is often part of the plan, and we work with your other specialists to reduce immune-suppressing medicines where that is possible.</p>"),
            ("What to expect", "<p>We follow you closely during treatment, with imaging or blood tests repeated to confirm the infection is clearing. Dr. Majewski has a particular interest in fungal infections and sees many of these patients.</p>"),
        ],
        "calls": ["Fever that returns during treatment", "New headache, confusion, vision change or neck stiffness", "Yellowing of the skin or eyes, or dark urine", "Any new medicine started by another doctor, so we can check for interactions"],
    },
    {
        "slug": "hiv-care",
        "name": "HIV care",
        "short": "Ongoing treatment for people living with HIV, new diagnoses, and PrEP for prevention.",
        "sections": [
            ("What it is", "<p>HIV is a treatable, long-term condition. With modern medicines, usually one pill a day or an injection every two months, the virus becomes undetectable in the blood, the immune system recovers, life expectancy is close to normal, and the virus cannot be passed on to sexual partners. Our physicians have cared for people with HIV in Hawaiʻi for decades, including those newly diagnosed, those transferring care from the mainland, and those who have been on treatment for many years.</p>"),
            ("Starting or transferring care", "<p>At a first visit we review your history and any previous treatment, check your viral load, immune cell count and general health, screen for other infections, and talk through the options. Treatment starts right away, often the same day for a new diagnosis. If you are transferring care, bring your most recent labs and a list of the medicines you have taken; we can usually continue your current regimen without a gap.</p>"),
            ("Ongoing care", "<p>Once the virus is suppressed, visits are every three to six months with labs, and we handle prescription refills, prior authorizations and manufacturer assistance programs. We also look after the things that matter more as people with HIV grow older: heart health, bone health, kidney function, cancer screening, vaccinations and mental health, in coordination with your primary care physician. Our office staff are experienced with the state AIDS Drug Assistance Program and the insurance questions specific to HIV medicines.</p>"),
            ("Prevention", "<p>For people who are HIV-negative and at risk, we prescribe <a href='/prep/'>PrEP</a> as daily pills or long-acting injections, with no referral needed. If you have had a possible exposure in the last 72 hours, call the office or go to an emergency department the same day for PEP.</p>"),
        ],
        "calls": ["You have missed doses or run out of medicine", "A new medicine or supplement started elsewhere, so we can check for interactions", "Fever, rash, or a new illness that is not settling", "You are planning a pregnancy or have become pregnant"],
    },
]
