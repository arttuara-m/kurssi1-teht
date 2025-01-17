kuhanpituus = float(input("Syötä kuhasi pituus senttimetreinä: "))

if kuhanpituus < 37:
    puute = str(37 - kuhanpituus)
    print("Kala on liian pieni, päästä se takaisin järveen.")
    print("Kuha on " + puute + " senttimetriä alle sallitun rajan.")
