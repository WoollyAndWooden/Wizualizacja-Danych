# Importy
import random
import os

# Zad 1
print("\nZadanie 1")
with open("Zad1.txt", "w") as f:
    for i in range(10):
        f.write(str(random.randint(0, 30) * 2))
        f.write('\n')

# Zad 2
print("\nZadanie 2")
with open("Zad1.txt", 'r') as f:
    print(f.read())

os.remove("Zad1.txt")

# Zad 3
print("\nZadanie 3")

with open("Zad2.txt", "w+") as f:
    f.write("Tu zapisuje\nKilka linijek\nTekstu jak mnie proszono\nDowidzenia")
    f.seek(0)
    for line in f:
        print(line)

os.remove("Zad2.txt")

# Zad 4
print("\nZadanie 4")


class NaZakupy:

    # Konstruktor
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = int(ilosc)
        self.jednostka_miary = jednostka_miary
        self.cena_jed = float(cena_jed)

    # Metody
    def wyswietl_produkt(self):
        print("Nazwa produktu:", self.nazwa_produktu, sep=' ')
        print("\nIlosc produktu:", self.ilosc, sep=' ')
        print("\nLiczony w:", self.jednostka_miary, sep=' ')
        print("\nCena za", self.jednostka_miary, "=", self.cena_jed, sep=' ')

    def ilosc_produktu(self):
        if self.ilosc == 1 or self.ilosc > 4:
            print("Na stanie jest", self.ilosc, self.jednostka_miary, "produktu", sep=' ')
        else:
            print("Na stanie są", self.ilosc, self.jednostka_miary, "produktu", sep=' ')

    def ile_kosztuje(self, wybrana_ilosc):
        print(wybrana_ilosc, self.jednostka_miary, "produktu kosztuje", self.cena_jed * wybrana_ilosc, sep=' ')

Ziemniak = NaZakupy("ziemniak", 5, "kg", 3)

Ziemniak.wyswietl_produkt()

Ziemniak.ilosc_produktu()

Ziemniak.ile_kosztuje(4)

del Ziemniak

# Zad 5
print("\nZadanie 5")

class CiagiArytmetyczne:
    roznica = 0
    elementy_ciagu = [0]

    def wyswietl_dane(self):
        for i in self.elementy_ciagu:
            print(i)

    def pobierz_elementy(self, * element):
        self.elementy_ciagu = [x for x in element]

        self.roznica = self.elementy_ciagu[1] - self.elementy_ciagu[0]

        for i in range(1, len(self.elementy_ciagu)):
            if self.roznica != self.elementy_ciagu[i] - self.elementy_ciagu[i-1]:
                print("Ciąg nieprawidłowy, proszę usuń objekt, lub zmień parametry")

    def pobierz_parametry(self, a1, r, ile):

        # Te działanie zawiera w sobie metodę policz_elementy
        self.elementy_ciagu = [a1 + (r * x) for x in range(ile)]
        self.roznica = r

    def policz_sume(self):
        print(str(((self.elementy_ciagu[0] + self.elementy_ciagu[len(self.elementy_ciagu) - 1]) / 2) * self.roznica))

ciag1 = CiagiArytmetyczne()
print("Elementy ciągu 1")
ciag1.pobierz_elementy(5, 10, 15)
ciag1.wyswietl_dane()
print("Suma ciągu 1")
ciag1.policz_sume()

ciag2 = CiagiArytmetyczne()
print("Elementy ciągu 2")
ciag1.pobierz_parametry(2, 2, 4)
ciag1.wyswietl_dane()
print("Suma ciągu 2")
ciag1.policz_sume()

del ciag1

del ciag2

# Zad 6
print("\nZadanie 6")

class Robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += self.krok * ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.y -= self.krok * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x -= self.krok * ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x += self.krok * ile_krokow

    def pokaz_gdzie_jestes(self):
        print("X:", self.x, "\nY:", self.y, sep=' ')


Robak = Robaczek(0, 0, 15)

Robak.pokaz_gdzie_jestes()

Robak.idz_w_gore(5)

Robak.idz_w_dol(2)

Robak.idz_w_lewo(10)

Robak.idz_w_prawo(3)

Robak.pokaz_gdzie_jestes()

del Robak