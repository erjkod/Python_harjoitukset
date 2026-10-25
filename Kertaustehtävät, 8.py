kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]

yhteensa = 0

for hinta in kustannukset:
    print("Tuotteen valmistuskustannus:", hinta, "€")
    yhteensa = yhteensa + hinta

print("Valmistuskustannukset yhteensä:", yhteensa, "€")