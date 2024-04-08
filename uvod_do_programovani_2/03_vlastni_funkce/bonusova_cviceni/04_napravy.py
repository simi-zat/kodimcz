# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs2/napravy

vahove_limity = {2: 18,
                 3: 25,
                 4: 32,
                 5: 48}
vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]


def spocitej_pokutu(pocet_naprav, hmotnost):
    if hmotnost > vahove_limity[pocet_naprav]:
        return 1000 * (hmotnost - vahove_limity[pocet_naprav])
    else:
        return 0


pokuta = spocitej_pokutu(4, 34)
print(pokuta)

for v in vazeni:
    print(spocitej_pokutu(v[0], v[1]))
