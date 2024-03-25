school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

soucet_znamek = 0
pocet_predmetu = len(school_report)

for predmet, znamka in school_report.items():
    soucet_znamek += znamka

    if znamka == 1:
        print(f"Z predmetu {predmet} mas 1.")

prumer_znamek = soucet_znamek / pocet_predmetu
print(f"Prumer znamek je {prumer_znamek}")
