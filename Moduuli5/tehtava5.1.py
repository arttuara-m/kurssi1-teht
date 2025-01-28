import random

maara = int(input("Syötä heitettävien noppien määrä: "))
summa = 0

for i in range(maara):
    summa += random.randint(1,6)

print(summa)