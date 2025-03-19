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

hissi = Hissi(0, 8)
hkerros = int(input("Syötä kerros: "))

hissi.siirry_kerrokseen(hkerros)