import random
luku = 0

def arpa(korkein):
    return random.randint(1,korkein)

tavoite = int(input("Syötä nopan tahkojen määrä: "))

while luku != tavoite:
    luku = arpa(tavoite)
    print(luku)