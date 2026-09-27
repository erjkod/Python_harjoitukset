import random

luku = random.randint(1, 10)

arvaus = int(input("Arvaa luku 1-10: "))

while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")

    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein")
