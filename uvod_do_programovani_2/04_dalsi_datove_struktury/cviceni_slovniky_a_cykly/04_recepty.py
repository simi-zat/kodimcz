recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

celkova_cena = 0

for potravina in recept["ingredience"]:
    # -- Prvni moznost - vic upovidana
    cena_jako_text = potravina[2]
    cena_jako_seznam_textu = cena_jako_text.split()
    cena_potraviny = float(cena_jako_seznam_textu[0])

    # -- Druha moznost - strucna
    # cena_potraviny = float(potravina[2].split()[0])

    celkova_cena += cena_potraviny

# Ruzne moznosti zaokrouhleni
print(f"Celkova cena za potraviny je {int(celkova_cena)}")
print(f"Celkova cena za potraviny je {round(celkova_cena)}")
