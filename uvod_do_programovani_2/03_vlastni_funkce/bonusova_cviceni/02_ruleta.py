# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs2/ruleta

import random


def roulette(cislo_rady, vyse_sazky):
    vyherni_cislo = random.randint(0, 36)
    rada_vyherniho_cisla = vyherni_cislo % 3

    if rada_vyherniho_cisla == 0:
        rada_vyherniho_cisla += 3

    print(f"Vyherni cislo je {vyherni_cislo}, ktere patri do {rada_vyherniho_cisla} rady")

    if vyherni_cislo == 0 or rada_vyherniho_cisla != cislo_rady:
        return 0
    else:
        return vyse_sazky * 2


cislo_rady = int(input("Na kterou radu chcete sazet? [1-3] "))
vyse_sazky = int(input("Kolik si prejete vsadit? "))

vyhra = roulette(cislo_rady, vyse_sazky)
print(f"Vyhravate {vyhra} korun.")
