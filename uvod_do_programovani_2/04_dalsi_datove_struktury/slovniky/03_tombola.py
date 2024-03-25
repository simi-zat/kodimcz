tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

# funkce input vraci text, musime proto pretypovat hodnotu na cislo
cislo_od_uzivatele = int(input("Zadejte cislo: "))

if cislo_od_uzivatele in tombola:
    print(tombola[cislo_od_uzivatele])
else:
    print("Bohužel nevyhráváš nic.")
