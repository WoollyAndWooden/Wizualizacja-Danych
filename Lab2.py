#Zad 1
print("Zadanie 1")

UlubioneFilmy = ["Władca Pierścieni: Drużyna Pierścienia", "Władca Pierścieni: Dwie WIeże",
                 "Władca Pierścieni: Powrót Króla", "Joker", "Into the Spiderverse",
                 "Skazani na Shawshank", "El Camino"]

UlubioneFilmy.reverse()

for i in range(5, (10-len(UlubioneFilmy))+5, 1):
    UlubioneFilmy.insert(i, input(u"Wpisz jeden z ulubionych filmów"))

for i in UlubioneFilmy:
    print(i)

#Zad 2
print("\nZadanie 2")

RankingFilmow = {}

for i in range(len(UlubioneFilmy)):
    RankingFilmow['Miejsce nr ' + str(i+1)] = UlubioneFilmy[i]

print(RankingFilmow)

del UlubioneFilmy
del RankingFilmow

#Zad 3
print("\nZadanie 3")

Przedmioty = {'WD': 'Wizualizacja Danych', 'PS': 'Programowanie Strukturalne',
              'CAD': 'Komputerowe Wspomaganie Programowania', 'AM': 'Analiza Matematyczna dla informatyków',
              'MD': 'Matematyka Dyskretna dla informatyków', 'JA': 'Język Angielski', 'WoT': 'World of Tanks'}

Przedmioty['WoT'] = 'Wiedza o Teatrze'

print(len(Przedmioty)+1)

del Przedmioty

#Zad 4
print("\nZadanie 4")

a = float(input(u"Podaj liczbę"))

print(a, '**', a, '=', a**a, sep=' ')

del a

#Zad 5
print("\nZadanie 5")

#By wyczyścić po działaniu programu
import os

f = open("Zad5.txt", "w")
f.write(input(u"Wpisz dowolny ciąg znaków"))
f.close()

f = open('Zad5.txt', 'r')
LiniaPliku = f.readline()
f.close()

os.remove('Zad5.txt')

Licznik = 0
for i in range(len(LiniaPliku)):
    if LiniaPliku[i].casefold() == 'a'.casefold():
        Licznik+=1

print(u"Litera \'a\' wystąpiła w tym ciągu", Licznik, 'razy', sep=' ')

del Licznik
del f

#Zad 6
print("\nZadanie 6")

a=int(input('Podaj pierwszą liczbę'))
b=int(input('Podaj drugą liczbę'))
c=int(input('Podaj trzecią liczbę'))

if(a%2 == 0 and b>c):
    print('Liczba', a, 'jest parzysta, oraz jednocześnie', b, 'jest większe od', c, sep=' ')
else:
    print('Warunki nie zostały spełnione')

del a
del b
del c

#Zad 7
print("\nZadanie 7")

lista = [4, 5.5, 3, 6, 3, 9.22, 8.7, 5.2]

for i in range(1, len(lista)):
    print('Suma elementu', i, 'oraz elementu', i-1, '=', lista[i]+lista[i-1])

del lista
#Zad 8
print("\nZadanie 8")

i = 0
lista = []
while i < 10:
    i+=1
    a=int(input('Podaj liczbę'))
    if(a%2==0):
        lista.append(a)

for i in lista:
    print(i)
#Zad 9
print("\nZadanie 9")

for i in range(6):
    for j in range(6):
        if (i == 0 or i == 5) or (j == 0 or j == 5):
            if j == 5:
                print('O')
            else:
                print('O', end='')

        else:
            print(' ', end='')

#To takie na poboczu tylko
a = int(input(u"Podaj wysokość"))
b = int(input(u"Podaj Szerokość"))
for i in range(a):
    for j in range(b):
        if (i == 0 or i == a-1) or (j == 0 or j == b-1):
            if j == b-1:
                print('O')
            else:
                print('O', end='')

        else:
            print(' ', end='')

del a
del b

#Zad 10
print("\nZadanie 10")

a = input(u"podaj liczbę")

try:
    a = float(a)
except ValueError:
    print("Podałeś literę zamiast liczby")

del a
