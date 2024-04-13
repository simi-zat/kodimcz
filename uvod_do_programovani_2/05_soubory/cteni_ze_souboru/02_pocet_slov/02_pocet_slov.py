# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/cteni-souboru/pocet-slov

celkovy_pocet_slov = 0

with open('slohova_prace.txt') as file:
    for radek in file.read().split("\n"):
        pocet_slov = len(radek.split(" "))
        print(f"Pocet slov v radku je {pocet_slov}")

        celkovy_pocet_slov += pocet_slov

print(f"Celkovy pocet slov v radku je {celkovy_pocet_slov}")
