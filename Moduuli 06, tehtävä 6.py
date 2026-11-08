import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade * sade
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

pizza1 = yksikkohinta(halkaisija1, hinta1)
pizza2 = yksikkohinta(halkaisija2, hinta2)

print("Ensimmäisen pizzan yksikköhinta:", pizza1)
print("Toisen pizzan yksikköhinta:", pizza2)

if pizza1 < pizza2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif pizza2 < pizza1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")