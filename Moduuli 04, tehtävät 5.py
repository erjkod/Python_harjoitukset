oikea_tunnus = "opiskelija"
oikea_salasana = "python"

yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Väärät tiedot")

    yritykset = yritykset + 1

if yritykset == 5:
    print("Pääsy evätty")