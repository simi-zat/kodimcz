# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs2/zarovnani

numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]


def zarovnej(numbers):
    nejdelsi_cislo = str(max(numbers))
    max_delka = len(nejdelsi_cislo)

    for n in numbers:
        num_as_string = str(n)
        print(" " * (max_delka - len(num_as_string)) + num_as_string)


zarovnej(numbers)
