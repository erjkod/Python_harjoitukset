luvut = []

while True:
    luku = input("Anna luku (tyhjä lopettaa): ")

    if luku == "":
        break

    luvut.append(int(luku))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")

for i in luvut[:5]:
    print(i)