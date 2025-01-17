import random

maara = int(input("Syötä testilukujen määrä: "))

sisalla = 0

for i in range(maara):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2+y**2 < 1:
        sisalla += 1

print(4*sisalla/maara)

