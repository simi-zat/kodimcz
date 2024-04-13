# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/cteni-souboru/pujcovna

ujete_kilometry_celkem = 0

with open('auta.txt') as file:
    for auto in file.read().split("\n"):
        informace = auto.split(" ")

        if "," in informace[1]:
            pocet_km = float(informace[1].replace(",", "."))
        else:
            pocet_km = float(informace[1])

        ujete_kilometry_celkem += pocet_km * 1000

print(f"Pocet ujetych kilometru celkem je {ujete_kilometry_celkem}")
