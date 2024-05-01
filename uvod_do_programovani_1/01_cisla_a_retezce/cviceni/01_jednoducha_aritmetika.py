# Zadani: https://kodim.cz/czechitas/uvod-do-progr-1/prvni-krucky/cisla-retezce/excs/jednoducha-aritmetika

cena_listku = 12
prumerny_pocet_navstevniku = 174
pocet_predstaveni_mesicne = 15

print("Mesicni prijem divadla je")
print(cena_listku * prumerny_pocet_navstevniku * pocet_predstaveni_mesicne)

studentska_cena = cena_listku * 0.65
print("Mesicni prijem divadla (se slevou pro studenty) je")
print(((cena_listku * prumerny_pocet_navstevniku / 2) + (
            studentska_cena * prumerny_pocet_navstevniku / 2)) * pocet_predstaveni_mesicne)
