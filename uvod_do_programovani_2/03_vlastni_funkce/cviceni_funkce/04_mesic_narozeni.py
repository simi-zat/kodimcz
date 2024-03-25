def month_of_birth(rodne_cislo):
    if rodne_cislo[2] == "0":
        return rodne_cislo[3]
    elif rodne_cislo[2] == "1":
        return rodne_cislo[2:4]

    elif rodne_cislo[2] == "5":
        return rodne_cislo[3]
    elif rodne_cislo[2] == "6":
        return "1" + rodne_cislo[3]
