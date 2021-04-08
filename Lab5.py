# Zad 1
print("\nZadanie 1\n")


class Material:

    # Konstruktor
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    # Metody
    def wyswietl_nazwe(self):
        print(self.rodzaj)


class Ubrania(Material):

    # Konstruktor
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        super().__init__(rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    # Metody
    def wyswietl_dane(self):
        print("Rozmiar:", self.rozmiar, "\nKolor:", self.kolor, "\nDla:", self.dla_kogo, sep=' ')


class Sweter(Ubrania):

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
        super().__init__(rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        super().wyswietl_dane()
        print("Rodzaj swetra: ", self.rodzaj_swetra)


sweter1 = Sweter("Dres", 50, 50, "XL", "zielony", "Mój", "Golf")
print(sweter1)
sweter1.wyswietl_nazwe()
sweter1.wyswietl_dane()

ubranie1 = Ubrania("Polar", 50, 50, "L", "Czarny", "Dla mamy")
print(ubranie1)
ubranie1.wyswietl_nazwe()
ubranie1.wyswietl_dane()

material1 = Material("Jakaś tkanina", 50, 50)
print(material1)
material1.wyswietl_nazwe()

del ubranie1
del material1
del sweter1

# Zad 2
print("\nZadanie 2\n")


class Kwadrat:
    def __init__(self, x):
        self.x = x

    def __add__(self):
        return Kwadrat(self.x + 4 * self.x)

    def __ge__(self, other):
        return self.x >= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __lt__(self, other):
        return self.x < other.x


kwadrat1 = Kwadrat(5)
kwadrat2 = kwadrat1.__add__()

print(kwadrat2.x)

# Zad 3
print("\nZadanie 3\n")

print(kwadrat2 >= kwadrat1)
print(kwadrat1 >= kwadrat2)

print(kwadrat2 > kwadrat1)
print(kwadrat1 > kwadrat2)

print(kwadrat2 <= kwadrat1)
print(kwadrat1 <= kwadrat2)

print(kwadrat2 < kwadrat1)
print(kwadrat1 < kwadrat2)

del kwadrat1
del kwadrat2

# Zad 4
print("\nZadanie 4\n")


class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)


p1 = Point()
p2 = Point(1, 1)
p3 = Point(2, 2)

print(p1.counter, p2.counter, p3.counter, sep='\n')
p1.update(p1.x)
print(p1.counter, p2.counter, p3.counter, sep='\n')
p2.update(p2.x)
print(p1.counter, p2.counter, p3.counter, sep='\n')
p3.update(p3.y)
print(p1.counter, p2.counter, p3.counter, sep='\n')

del p1, p2, p3

# Zad 5
print("\nZadanie 5\n")


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko)
        self.pensja = pensja


class Menadzer(Pracownik):
    def przedstaw_sie(self):
        print("Jestem menadzerem,", self.imie, self.nazwisko, "i zarabiam", str(self.pensja), sep=' ')


Andrzej = Osoba("Andrzej", "Kowalski")
Adam = Pracownik("Adam", "Zdolny", 2000)
Zdzislaw = Menadzer("Zdzisław", "Złodziej", 10000)

print("Czy to osoby?\nAndrzej:", isinstance(Andrzej, Osoba),
      "\nAdam:", isinstance(Adam, Osoba),
      "\nZdzisław:", isinstance(Zdzislaw, Osoba), sep=' ')

print("Czy to pracownicy?\nAndrzej:", isinstance(Andrzej, Pracownik),
      "\nAdam:", isinstance(Adam, Pracownik),
      "\nZdzisław:", isinstance(Zdzislaw, Pracownik), sep=' ')

print("Czy to Menadżerowie?\nAndrzej:", isinstance(Andrzej, Menadzer),
      "\nAdam:", isinstance(Adam, Menadzer),
      "\nZdzisław:", isinstance(Zdzislaw, Menadzer), sep=' ')

print("Czy osoba jest podklasą pracownika?", issubclass(Osoba, Pracownik))
print("A może na odwrót?", issubclass(Pracownik, Osoba))
print("Czyli Menadżer jest podklasą pracownika?", issubclass(Menadzer, Pracownik))
print("A czy drzewo idzie głębiej? Jest podklasą osoby?", issubclass(Menadzer, Osoba))

del Adam, Andrzej, Zdzislaw

# Zad 7
print("\nZadanie 7\n")


class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index += 1
        if self.index % 2 == 0:
            return self.data[self.index]


SprawdzmyTo = Parzyste([0, 1, 2, 3, 4, 5, 6])
for i in SprawdzmyTo:
    print(i)

del SprawdzmyTo

# Zad 8
print("\nZadanie 8\n")


class Samogloski:

    def __init__(self, data):
        self.data = data
        self.index = -1
        self.samogloski = ['a', 'ą', 'e', 'ę', 'u', 'ó', 'y', 'o', 'i']

    def __iter__(self):
        return self

    def __next__(self):
        if isinstance(self.data, str):
            if self.index == len(self.data) - 1:
                raise StopIteration
            self.index += 1
            if self.data[self.index].casefold() in self.samogloski:
                return self.data[self.index]


SprawdzmyTo = Samogloski("Abrakadabra osądźmy dziś Elektorięńską ugodówkę yup")

for i in SprawdzmyTo:
    print(i)

del SprawdzmyTo

# Zad 9
print("\nZadanie 9\n")


def generatorParzyste(data):
    for index in range(len(data) - 1):
        if index % 2 == 0:
            yield data[index]


SprawdzmyTo = generatorParzyste([0, 1, 2, 3, 4, 5, 6, 7])
for i in SprawdzmyTo:
    print(i)

del SprawdzmyTo

# Zad 10
print("\nZadanie 10\n")


def generatorArytmetyczne(data):
    r = data[1] - data[0]
    for i in range(0, len(data) - 2, 1):
        if data[i + 1] == data[i] + r:
            yield data[i]


SprawdzmyTo = generatorArytmetyczne([1, 2, 3, 5, 4, 3])
for i in SprawdzmyTo:
    print(i)