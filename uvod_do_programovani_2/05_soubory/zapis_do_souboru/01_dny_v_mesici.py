# Zadani: https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/zapis-souboru/dny-v-mesici

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('kalendar.txt', mode='w', encoding='utf-8') as output_file:
    for den in pocty_dni:
        print(den, file=output_file)

# jiny reseni

with open('kalendar2.txt', mode='w') as output_file:
    for den in pocty_dni:
        output_file.write(f"{den}\n")
