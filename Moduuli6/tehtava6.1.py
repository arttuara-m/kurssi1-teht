import random
luku = 0

def arpa():
    return random.randint(1,6)

while luku != 6:
    luku = arpa()
    print(luku)