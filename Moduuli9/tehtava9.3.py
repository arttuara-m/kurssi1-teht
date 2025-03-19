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

auto = Auto("ABC-123", 142, 0, 2000)
print(auto.kuljettumatka)
auto.kiihdyta(60)
auto.kulje(1.5)
print(auto.kuljettumatka)