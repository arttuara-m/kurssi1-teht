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

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for osallistuja in self.osallistujat:
            osallistuja.kiihdyta(random.randint(-10, 15))
            osallistuja.kulje(1)

    def tulosta_tilanne(self):
        for osallistuja in self.osallistujat:
            print(osallistuja.rekisteritunnus)
            print("huippunopeus: " + str(osallistuja.huippunopeus))
            print("nopeus: " + str(osallistuja.nopeus))
            print("kuljettu matka: " + str(osallistuja.kuljettumatka))
            print()

    def kilpailu_ohi(self):
        for osallistuja in self.osallistujat:
            if osallistuja.kuljettumatka >= self.pituus:
                return True

#luo kilpailijat
autolista = []
for i in range(10):
    autolista.append(Auto("ABC-" + str(i+1), random.randint(100,200)))

#luo kilpailun
kilpailu = Kilpailu("Suuri romuralli", 8000, autolista)

#suorittaa kilpailun
ohi = False
tunnit = 0
while not ohi:
    kilpailu.tunti_kuluu()
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
    ohi = kilpailu.kilpailu_ohi()

#tulostaa tulokset
print("------------------------------------")
print()
kilpailu.tulosta_tilanne()