lentoasemat = dict()

syote = ""

while syote != "lopeta":
    if syote == "syötä":
        icao = input("Syötä lentoaseman ICAO-koodin: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif syote == "hae":
        nimi = input("Syötä ICAO-koodi: ")
        print(lentoasemat[nimi])

    else:
        print("Virheellinen komento!")

    syote = input("Syötä, hae vai lopeta?: ")
