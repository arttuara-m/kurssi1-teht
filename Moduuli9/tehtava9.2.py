class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    def kiihdyta(self, nopeudenmuutos):
        if self.nopeus + nopeudenmuutos < 0:
            self.nopeus = 0
        elif self.nopeus + nopeudenmuutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += nopeudenmuutos

auto = Auto("ABC-123", 142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.nopeus)
auto.kiihdyta(-200)
print(auto.nopeus)
