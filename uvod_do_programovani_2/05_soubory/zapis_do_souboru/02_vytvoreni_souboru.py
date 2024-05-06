# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/zapis-souboru/vytvoreni-souboru

nazev_souboru = input("Zadejte nazev souboru: ")
obsah_souboru = input("Zadejte obsah souboru: ")

with open(nazev_souboru, mode='w', encoding='utf-8') as output_file:
    print(obsah_souboru, file=output_file)


# Rozsirene zadani - opakovane dotazovni na novy radek textu

nazev_souboru = input("Zadejte nazev souboru: ")

while True:
    obsah_souboru = input("Zadejte obsah souboru: ")

    with open(nazev_souboru, mode='a', encoding='utf-8') as output_file:
        print(obsah_souboru, file=output_file)
