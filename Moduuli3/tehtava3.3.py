spuoli = input("Syötä biologinen sukupuoli: ")
arvo = int(input("Syötä hemoglobiiniarvo: "))

tuomio = ""

if (spuoli == "nainen" and arvo < 117) or (spuoli == "mies" and arvo < 134):
    tuomio = "hemoglobiiniarvo on alhainen"
elif (spuoli == "nainen" and arvo > 175) or (spuoli == "mies" and arvo > 195):
    tuomio = "hemoglobiiniarvo on korkea"
elif (spuoli == "nainen" and 117 < arvo < 175) or (spuoli == "mies" and 134 < arvo < 195):
    tuomio = "hemoglobiiniarvo on normaali"
else:
    print("Ole yhteydessä järjestelmästä vastaavaan")

print(tuomio)