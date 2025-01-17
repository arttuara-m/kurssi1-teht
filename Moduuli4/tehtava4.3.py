luku = input("Syötä luku: ")
pienin = int(luku)
suurin = int(luku)

while luku != "":

    luku = int(luku)
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku

    luku = input("Syötä luku: ")

print("pienin luku on " + str(pienin))
print("suurin luku on " + str(suurin))
