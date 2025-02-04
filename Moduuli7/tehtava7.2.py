nimet = set()

nimi = input("Syötä nimi: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
    nimi = input("Syötä nimi: ")

for i in nimet:
    print(i)
