
class Hissi:
    def __init__(self, alin, ylin):
        self.sijainti = 0
        self.alin = alin
        self.ylin = ylin

    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            self.sijainti = self.sijainti + 1
            print(self.sijainti)

    def kerros_alas(self):
        if self.sijainti > self.alin:
            self.sijainti = self.sijainti - 1
            print(self.sijainti)

    def siirry_kerrokseen(self, kerros):
        if self.alin <= kerros <= self.ylin:
            if kerros < self.sijainti:
                for i in range(self.sijainti - kerros):
                    self.kerros_alas()
            elif kerros > self.sijainti:
                for i in range(kerros - self.sijainti):
                    self.kerros_ylos()

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissienmaara):
        self.alin = alinkerros
        self.ylin = ylinkerros
        self.hissit = []
        for i in range(hissienmaara):
            self.hissit.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, hissinnro, kerros):
        ajettava = self.hissit[hissinnro - 1]
        ajettava.siirry_kerrokseen(kerros)


talo = Talo(0,9,3)
while True:
    hhissi = int(input("Syötä haluttu hissi: "))
    hkerros = int(input("Syötä haluttu kerros: "))

    talo.aja_hissia(hhissi, hkerros)

    if input("Haluatko ajaa vielä hissiä y/n: ") == "n":
        break
