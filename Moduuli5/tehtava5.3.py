luku = int(input("Syötä luku: "))
alkuluku = True

if luku == 1:
    alkuluku = False

for i in range(2, luku-1):
    if luku % i == 0:
        alkuluku = False
        break

if alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")