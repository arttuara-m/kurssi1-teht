def muuttaja(gallonat):
    return gallonat * 3.785

ngallonat = float(input("Syötä nestegallonoiden määrät: "))

while ngallonat >= 0:
    print(muuttaja(ngallonat))

    ngallonat = int(input("Syötä nestegallonoiden määrät: "))