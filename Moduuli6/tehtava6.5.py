def paritonkarsija(lista):
    palautettava = []
    for i in lista:
        if i%2 == 0:
            palautettava.append(i)
    return palautettava

lista = []
luku = input("Syötä luku: ")

while luku != "":
    lista.append(int(luku))
    luku = input("Syötä luku: ")

print(lista)
print(paritonkarsija(lista))
