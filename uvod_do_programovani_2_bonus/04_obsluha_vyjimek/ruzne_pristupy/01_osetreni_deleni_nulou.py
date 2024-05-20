'''

Vytvoř program, který vypíše výsledek dělení těchto čísel. Program se postupně zeptá na dvě čísla (mohou být celá i desetinná).
Vyděl tato čísla mezi sebou a vypiš výsledek dělení. Ošetři, aby program nezhavaroval při pokusu o dělení nulou.
V tomto případě nemusíš ošetřovat zadání nečíselného vstupu, ošetření více výjimek v jednom bloku si ukážeme v další části.

'''

while True:

    num_1 = input("Zadej prvni cislo: ")
    num_2 = input("Zadej druhe cislo: ")

    print(f"Zadana cisla jsou:\n{num_1}, {num_2}")

    try:
        division = float(num_1) / float(num_2)
        print(division)

    except TypeError:
        print("Musi byt cisla")

    except ValueError:
        print("Musi byt int nebo float")

    except ZeroDivisionError:
        print("Nemuzes delit nulou")

# Odchyta vschny chyby - pouzivat opatrne :)
# except Exception:
#     print("ERROR")





