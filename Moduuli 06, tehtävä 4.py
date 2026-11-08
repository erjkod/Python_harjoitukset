def laske_summa(lista):
    summa = 0

    for luku in lista:
        summa = summa + luku

    return summa


luvut = [2, 5, 8, 10, 4]

tulos = laske_summa(luvut)

print("Listan lukujen summa on:", tulos)
