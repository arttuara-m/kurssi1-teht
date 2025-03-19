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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus=0, kuljettumatka=0):
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettumatka)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki, nopeus=0, kuljettumatka=0):
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettumatka)
        self.bensatankki = bensatankki


sahkoauto = Sahkoauto("ABC-15", 180, "52.5 kWh")
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, " 32.3 l")

sahkoauto.kiihdyta(200)
polttomoottoriauto.kiihdyta(200)
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)
print("Kuljetut matkat")
print(f"Sähköauto:          {sahkoauto.kuljettumatka}km")
print(f"Polttomoottoriauto: {polttomoottoriauto.kuljettumatka}km")