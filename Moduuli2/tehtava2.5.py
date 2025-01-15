

print("Anna leiviskät.")
leivat = float(input())
print()
print("Anna naulat.")
naulat = float(input())
print()
print("Anna luodit.")
luodit = float(input())
print()

leivat = leivat * 20 * 32 * 13.3
naulat = naulat * 32 * 13.3
luodit = luodit * 13.3

summa = leivat + naulat + luodit

grammat = summa % 1000
kilot = summa // 1000

print("Massa nykymittojen mukaan:")
print(f"{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa.")