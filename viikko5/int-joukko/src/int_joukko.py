class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, koko=5, kasvatuskoko=5):
        self.koko = koko
        self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.koko)

        self.alkio_laskuri = 0

    def kuuluu(self, alkio):
        return alkio in self.lista

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            if self.alkio_laskuri == len(self.lista):
                self.lista = self.lista + self._luo_lista(self.kasvatuskoko)

            self.lista[self.lista.index(0)] = alkio
            self.alkio_laskuri += 1

            return True

        return False


    def poista(self, alkio):
        if self.kuuluu(alkio):
            alkion_paikka = self.lista.index(alkio)

            for i in range(alkion_paikka, len(self.lista) - 1):
                self.lista[i] = self.lista[i+1]
            self.lista[-1] = 0
            self.alkio_laskuri -= 1
            return True
        
        return False

    def mahtavuus(self):
        return self.alkio_laskuri

    def to_int_list(self):
        taulu = self._luo_lista(self.alkio_laskuri)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkio_laskuri == 0:
            return "{}"
        elif self.alkio_laskuri == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkio_laskuri - 1):
                tuotos = tuotos + str(self.lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lista[self.alkio_laskuri - 1])
            tuotos = tuotos + "}"
            return tuotos
