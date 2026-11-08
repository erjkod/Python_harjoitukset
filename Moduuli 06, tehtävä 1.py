import random

def heita_noppaa():
    silmaluku = random.randint(1, 6)
    return silmaluku


tulos = 0

while tulos != 6:
    tulos = heita_noppaa()
    print("Nopan silmäluku:", tulos)