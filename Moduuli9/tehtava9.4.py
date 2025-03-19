import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, nopeudenmuutos):
        if self.nopeus + nopeudenmuutos < 0:
            self.nopeus = 0
        elif self.nopeus + nopeudenmuutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += nopeudenmuutos

    def kulje(self, tuntimaara):
        self.kuljettumatka += int(self.nopeus * tuntimaara)

autolista = []

for i in range(10):
    autolista.append(Auto("ABC-" + str(i+1), random.randint(100,200)))

kisakaynnissa = 1
while kisakaynnissa:
    for auto in autolista:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
    for auto in autolista:
        if auto.kuljettumatka >= 10000:
            kisakaynnissa = 0

for auto in autolista:
    print(auto.rekisteritunnus)
    print("huippunopeus: " + str(auto.huippunopeus))
    print("kuljettu matka: " + str(auto.kuljettumatka))
    print(auto.nopeus)
    print()