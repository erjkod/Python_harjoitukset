lista = []

luku = int(input("Anna luku (0 lopettaa): "))

while luku != 0:
    lista.append(luku)

    print(lista)
    print(sorted(lista))

    luku = int(input("Anna luku (0 lopettaa): "))