import random

lukko1 = ""
lukko2 = ""

for n in range(3):
    i = str(random.randint(0,9))
    lukko1 = lukko1 + i

for n in range(4):
    i = str(random.randint(1, 6))
    lukko2 = lukko2 + i

print("kolminumeroinen koodi " + lukko1)

print("nelinumeroinen koodi " + lukko2)