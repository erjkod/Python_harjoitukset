pituus = float(input("Anna kalan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kala pitää laskea takaisin järveen.")
    print("Alimmasta sallitusta pyyntimitasta puuttuu", puuttuu, "cm.")
else:
    print("Kalan voi pitää.")