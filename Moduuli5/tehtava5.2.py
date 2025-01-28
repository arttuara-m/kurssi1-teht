nimilista = []

nimi = input("Syötä luku: ")
while nimi != "":
    nimilista.append(int(nimi))
    nimi = input("Syötä luku: ")

nimilista.sort(reverse=True)
print(nimilista[:5])
