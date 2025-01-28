def summaaja(lukulista):
    summa = 0
    for i in lukulista:
        summa += i
    return summa

syote = input("Syötä luku, tyhjä summaa: ")
lista = []

while syote != "":
    lista.append(int(syote))
    syote = input("Syötä luku, tyhjä summaa: ")

print(summaaja(lista))

