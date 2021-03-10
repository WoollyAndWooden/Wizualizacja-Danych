#Zad 1
UlubioneFilmy = ["Władca Pierścieni: Drużyna Pierścienia", "Władca Pierścieni: Dwie WIeże",
                 "Władca Pierścieni: Powrót Króla", "Joker", "Into the Spiderverse",
                 "Skazani na Shawshank", "El Camino"]

UlubioneFilmy.reverse()

for i in range(5, (10-len(UlubioneFilmy))+5, 1):
    UlubioneFilmy.insert(i, input(u"Wpisz jeden z ulubionych filmów"))

for i in UlubioneFilmy:
    print(i)

#Zad 2
RankingFilmow = {}
for i in range(len(UlubioneFilmy)):
    RankingFilmow['Miejsce nr ' + str(i+1)] = UlubioneFilmy[i]

print(RankingFilmow)

#Zad 3
Przedmioty = {'WD': 'Wizualizacja Danych', 'PS': 'Programowanie Strukturalne',
              'CAD': 'Komputerowe Wspomaganie Programowania', 'AM': 'Analiza Matematyczna dla informatyków',
              'MD': 'Matematyka Dyskretna dla informatyków', 'JA': 'Język Angielski', 'WoT': 'World of Tanks'}
Przedmioty['WoT'] = 'Wiedza o Teatrze'

print(len(Przedmioty)+1)

#Zad 10
a = input(u"podaj liczbę")

try:
    a = float(a)
except ValueError:
    print("Podałeś literę zamiast liczby")
