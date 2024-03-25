passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

jmeno_hosta = input("Zadejte jmeno: ")

if jmeno_hosta in passwords:
    heslo_hosta = input("Zadejte vase heslo: ")

    if heslo_hosta == passwords[jmeno_hosta]:
        print("Smíš vstoupit.")
    else:
        print("Špatný heslo!")
else:
    print("Nejseš na seznamu!")
