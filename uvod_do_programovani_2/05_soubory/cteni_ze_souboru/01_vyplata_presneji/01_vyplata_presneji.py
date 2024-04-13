# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/cteni-souboru/vyplata-presneji

vykaz = []

with open('vykaz.txt') as file:
    for hodnota in file.read().split("\n"):
        vykaz.append(int(hodnota))

print(vykaz)

hodinova_mzda = int(input("Zadejte hodinovou mzdu: "))
pocet_hodin_celkem = sum(vykaz)

print(f"Celkova vyplata za cely rok: {pocet_hodin_celkem * hodinova_mzda}")
print(f"Prumerna vyplata za mesic: {pocet_hodin_celkem * hodinova_mzda / 12}")
