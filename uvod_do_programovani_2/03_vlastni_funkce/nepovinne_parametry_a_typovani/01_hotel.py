def total_price(persons, breakfast=False):
    cena_osoba_noc = 850
    snidane = 125

    if breakfast:
        cena_noc = cena_osoba_noc + snidane
    else:
        cena_noc = cena_osoba_noc

    return cena_noc * persons


print(total_price(3))
print(total_price(3, False))
print(total_price(2))
print(total_price(2, True))
