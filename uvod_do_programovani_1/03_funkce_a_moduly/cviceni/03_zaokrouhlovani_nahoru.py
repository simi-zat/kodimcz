# Zadani: https://kodim.cz/czechitas/uvod-do-progr-1/prvni-krucky/funkce-moduly/excs/zaokrouhlovani-nahoru

import math

# z predesleho cviceni
eura = 0.65 * 12
kurz = 24
koruny = round(kurz * eura)

print("Cena listku v celych korunach")
print(koruny)

# reseni tohoto ukolu
koruny2 = math.ceil(kurz * eura)

print("Cena listku v celych korunach zaokrouhleno nahoru")
print(koruny2)
