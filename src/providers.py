# Provider data for Oahu Medical Group.
# Edit here, then run `python3 build.py` from the repo root.
#
# hours: list of (day, time) as shown on the bio page.
# week: entries for the homepage "in clinic this week" grid: (day, "am"/"pm", note or "")

PROVIDERS = [
    {
        "slug": "heath-chung-md",
        "name": "Heath Chung, MD",
        "short": "Dr. Chung",
        "photo": "heath-chung.jpg",
        "title": "Infectious Diseases",
        "hours": [("Monday", "1:30 – 5:00 PM"), ("Wednesday", "1:30 – 5:00 PM"), ("Thursday", "8:00 AM – 12:00 PM")],
        "week": [("Mon", "pm", ""), ("Wed", "pm", ""), ("Thu", "am", "")],
        "bio": [
            "Dr. Heath Chung was born and raised in Captain Cook, Kona, on the Big Island of Hawaiʻi. He attended Brown University in Providence, Rhode Island; received his medical degree from the University of Hawaiʻi John A. Burns School of Medicine; completed a residency in Internal Medicine at the University of Hawaiʻi; and completed his fellowship in Infectious Diseases at the Mayo Clinic College of Medicine in Rochester, Minnesota.",
            "Dr. Chung is affiliated with multiple hospitals on Oʻahu, including The Queen’s Medical Center and Kuakini Medical Center, and currently serves as Chief of the Division of Infectious Diseases at The Queen’s Medical Center. His interests include HIV medicine, pre-exposure prophylaxis for HIV, diabetes-associated infections, transplant-associated infections, and skin and soft-tissue infections.",
            "In his free time he enjoys spending time with his family and shoreline fishing.",
        ],
        "facts": [("Medical school", "University of Hawaiʻi, John A. Burns School of Medicine"), ("Residency", "Internal Medicine, University of Hawaiʻi"), ("Fellowship", "Infectious Diseases, Mayo Clinic"), ("Hospitals", "The Queen’s Medical Center, Kuakini Medical Center")],
        "pay": "https://heathhchungmd.securepayments.cardpointe.com/pay",
        "pay_entity": "",
    },
    {
        "slug": "john-raymond-go-md",
        "name": "John Raymond Go, MD",
        "short": "Dr. Go",
        "photo": "john-raymond-go.jpg",
        "title": "Infectious Diseases",
        "hours": [("Friday", "9:30 AM – 12:00 PM")],
        "week": [("Fri", "am", "")],
        "bio": [
            "After graduating from the University of Santo Tomas Faculty of Medicine and Surgery in Manila, Philippines, Dr. Go completed Internal Medicine residency training at the University of Hawaiʻi Internal Medicine Residency Program in Honolulu, where he also served as a chief resident. He then completed his Infectious Diseases fellowship at the Mayo Clinic School of Graduate Medical Education in Minnesota.",
            "Within Infectious Diseases, Dr. Go has a special interest in cardiovascular infections, antimicrobial stewardship, and gram-positive bloodstream infections.",
        ],
        "facts": [("Medical school", "University of Santo Tomas, Manila"), ("Residency", "Internal Medicine, University of Hawaiʻi (chief resident)"), ("Fellowship", "Infectious Diseases, Mayo Clinic")],
        "pay": "https://hawaiiinfectious.securepayments.cardpointe.com/pay",
        "pay_entity": "Hawaii Infectious Disease Associates",
    },
    {
        "slug": "james-joyner-md",
        "name": "James Joyner, MD",
        "short": "Dr. Joyner",
        "photo": "james-joyner.jpg",
        "title": "Infectious Diseases",
        "hours": [("Every other Tuesday", "8:00 AM – 12:00 PM"), ("Wednesday", "8:00 AM – 12:00 PM"), ("Thursday", "1:30 – 5:00 PM")],
        "week": [("Tue", "am", "alternate weeks"), ("Wed", "am", ""), ("Thu", "pm", "")],
        "bio": [
            "After completing medical training at the University of Colorado, Dr. Joyner moved to Florida to fulfill his National Health Service Corps contract, providing care for HIV-infected immigrants and indigent patients. He then returned to Colorado to work at Denver Public Health in HIV, tuberculosis, and sexually transmitted diseases.",
            "Those years of public health service cemented his interest in infectious diseases and HIV care, and led to a fellowship in Infectious Diseases at the University of California, Irvine.",
        ],
        "facts": [("Medical school", "University of Colorado"), ("Fellowship", "Infectious Diseases, University of California, Irvine"), ("Background", "National Health Service Corps; Denver Public Health")],
        "pay": "https://jamesjoynerllc.securepayments.cardpointe.com/pay",
        "pay_entity": "",
    },
    {
        "slug": "eric-kajioka-md",
        "name": "Eric Kajioka, MD",
        "short": "Dr. Kajioka",
        "photo": "eric-kajioka.jpg",
        "title": "Infectious Diseases",
        "hours": [("Monday", "10:30 AM – 12:00 PM"), ("Tuesday", "1:30 – 3:30 PM"), ("Alternating Wednesdays and Fridays", "10:30 AM – 12:00 PM")],
        "week": [("Mon", "am", ""), ("Tue", "pm", ""), ("Wed", "am", "alternate weeks"), ("Fri", "am", "alternate weeks")],
        "bio": [
            "Dr. Eric Kajioka was born and raised in Pearl City, Oʻahu. He graduated from the University of Hawaiʻi John A. Burns School of Medicine and completed his Internal Medicine internship and residency at the University of Hawaiʻi, followed by fellowship training in Infectious Diseases at the University of Colorado School of Medicine in Denver.",
            "As a board-certified Infectious Diseases physician, Dr. Kajioka treats patients at multiple hospitals on Oʻahu, including The Queen’s Medical Center, Straub Hospital, Kuakini Medical Center, Pali Momi Medical Center, and The Queen’s Medical Center – West Oʻahu.",
        ],
        "facts": [("Medical school", "University of Hawaiʻi, John A. Burns School of Medicine"), ("Residency", "Internal Medicine, University of Hawaiʻi"), ("Fellowship", "Infectious Diseases, University of Colorado"), ("Hospitals", "Queen’s, Straub, Kuakini, Pali Momi, Queen’s – West Oʻahu")],
        "pay": "https://erickajiokamd.securepayments.cardpointe.com/pay",
        "pay_entity": "",
    },
    {
        "slug": "jani-kim-md",
        "name": "Jani Kim, MD",
        "short": "Dr. Kim",
        "photo": "",
        "title": "Infectious Diseases",
        "hours": [],
        "week": [],
        "bio": [
            "Dr. Jani Kim is a board-certified Infectious Diseases physician with Oahu Medical Group.",
        ],
        "facts": [],
        "pay": "https://hawaiiinfectious.securepayments.cardpointe.com/pay",
        "pay_entity": "Hawaii Infectious Disease Associates",
        "draft": True,  # bio, photo and hours still to come
    },
    {
        "slug": "lorrance-majewski-do",
        "name": "Lorrance Majewski, DO",
        "short": "Dr. Majewski",
        "photo": "lorrance-majewski.jpg",
        "title": "Infectious Diseases",
        "hours": [("Thursday", "9:00 – 11:00 AM"), ("Friday", "1:30 – 4:00 PM")],
        "week": [("Thu", "am", ""), ("Fri", "pm", "")],
        "bio": [
            "Dr. Majewski’s focus is general infectious disease, with a particular interest in fungal infections. He completed fellowship training at Rush University Medical Center in Chicago, Illinois, after the University of Hawaiʻi Internal Medicine Residency Program.",
            "He studied medicine at A.T. Still University School of Osteopathic Medicine in Arizona and received his Bachelor of Science in Biology from the University of Hawaiʻi at Mānoa.",
        ],
        "facts": [("Medical school", "A.T. Still University School of Osteopathic Medicine in Arizona"), ("Residency", "Internal Medicine, University of Hawaiʻi"), ("Fellowship", "Infectious Diseases, Rush University Medical Center"), ("Interest", "Fungal infections")],
        "pay": "https://majewski.securepayments.cardpointe.com/pay",
        "pay_entity": "Majewski Infectious Diseases LLC",
    },
    {
        "slug": "benjamin-thomas-md",
        "name": "Benjamin Thomas, MD",
        "short": "Dr. Thomas",
        "photo": "benjamin-thomas.jpg",
        "title": "Infectious Diseases",
        "hours": [("Tuesday", "8:00 AM – 12:00 PM"), ("Wednesday", "1:30 – 5:00 PM"), ("Every other Friday, Hilo", "Afternoon")],
        "week": [("Tue", "am", ""), ("Wed", "pm", ""), ("Fri", "pm", "Hilo, alternate weeks")],
        "bio": [
            "After graduating from Mercer University School of Medicine in Macon, Georgia, Dr. Benjamin Thomas completed Internal Medicine residency training at the University of Hawaiʻi Internal Medicine Residency Program in Honolulu. He then pursued his Infectious Diseases fellowship at Washington University in St. Louis, where he also completed a Master’s degree in Clinical Investigation.",
            "Dr. Thomas serves as medical director of both Infection Prevention and Antimicrobial Stewardship at Adventist Health Castle, and as co-director of Antimicrobial Stewardship at The Queen’s Medical Center.",
            "He also cares for patients on the Big Island, consulting on inpatients at Hilo Benioff Medical Center and holding clinic there every other Friday afternoon.",
        ],
        "facts": [("Medical school", "Mercer University School of Medicine"), ("Residency", "Internal Medicine, University of Hawaiʻi"), ("Fellowship", "Infectious Diseases, Washington University in St. Louis (MS, Clinical Investigation)"), ("Hospitals", "Adventist Health Castle, The Queen’s Medical Center, Hilo Benioff Medical Center")],
        "pay": "https://alohainfectious.securepayments.cardpointe.com/pay",
        "pay_entity": "Aloha Infectious Diseases LLC",
    },
]

# Order for the payment page and the providers grid (alphabetical by last name)
ORDER = ["heath-chung-md", "john-raymond-go-md", "james-joyner-md", "eric-kajioka-md", "jani-kim-md", "lorrance-majewski-do", "benjamin-thomas-md"]
