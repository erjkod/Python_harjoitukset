syote = input("Anna luku: ")

if syote != "":
    luku = float(syote)
    pienin = luku
    suurin = luku

    while syote != "":
        luku = float(syote)

        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

        syote = input("Anna luku: ")

    print("Pienin:", pienin)
    print("Suurin:", suurin)