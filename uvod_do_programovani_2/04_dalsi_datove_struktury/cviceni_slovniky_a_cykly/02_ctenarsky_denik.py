books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

celkovy_pocet_stran = 0
pocet_super_knih = 0

for kniha in books:
    celkovy_pocet_stran += kniha["pages"]

    if kniha["rating"] >= 7:
        pocet_super_knih += 1

print(f"Celkovy pocet prectenych stran je {celkovy_pocet_stran}")
print(f"Pocet knih se super hodnocenim je {pocet_super_knih}")
