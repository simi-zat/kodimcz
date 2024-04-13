# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/zapis-souboru/rozepsana-vyplata

vykaz = []

with open('vykaz.txt') as file:
    for hodnota in file.read().split("\n"):
        vykaz.append(int(hodnota))

print(vykaz)

hodinova_mzda = int(input("Zadejte hodinovou mzdu: "))
pocet_hodin_celkem = sum(vykaz)

print(f"Celkova vyplata za cely rok: {pocet_hodin_celkem * hodinova_mzda}")
print(f"Prumerna vyplata za mesic: {pocet_hodin_celkem * hodinova_mzda / 12}")

with open("vyplata.txt", mode='w', encoding='utf-8') as output_file:
    for castka in vykaz:
        print(castka * hodinova_mzda)
        print(castka * hodinova_mzda, file=output_file)
