# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs2/zprehazena-pismena
import random

puvodni_slovo = "abcdefghij"
text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''


def zprehazej_pismena_v_slove(slovo):
    stred_slova = list(slovo[1:-1])
    random.shuffle(stred_slova)
    return slovo[0] + "".join(stred_slova) + slovo[-1]


nove_slovo = zprehazej_pismena_v_slove(puvodni_slovo)
print(f"{puvodni_slovo} -> {nove_slovo}")

# Bonus
text_as_list = text.split()
novy_text = []

for s in text_as_list:
    novy_text.append(zprehazej_pismena_v_slove(s))

print(" ".join(novy_text))
