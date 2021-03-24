# Importy
import random

import Lab3Funkcje

# Zadanie 1
print("\nZadanie 1")

A = [1 - x for x in range(1, 10)]
print(A)

B = [4 ** x for x in range(8)]
print(B)

C = [x for x in B if x % 2 == 0]
print(C)

del A

del B

del C

# Zadanie 2
print("\nZadanie 2")

# Wykonane na floatach
print("\nWykonane na floatach")
lista1 = [random.random() for x in range(10)]
lista2 = [x for x in lista1 if Lab3Funkcje.evenCheck(x)]

print(lista1)
print(lista2)

del lista1

del lista2

# Wykonane na int
print("\nWykonane na int")
lista1 = [random.randint(1, 100) for x in range(10)]
lista2 = [x for x in lista1 if x % 2 == 0]

print(lista1)
print(lista2)

del lista1

del lista2

# Zadanie 3
print("\nZadanie 3")

listaZakupow = {"Pomidory": "kg", "Czekolada": "sztuki", "Kawa": "sztuki", "Jabłka": "kg", "Jogurty": "sztuki"}

#produktyNaSztuki: List[Any] = [key for key, value in listaZakupow if value == "sztuki"]

print(produktyNaSztuki)

# Zadanie 4
print("\nZadanie 4")

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

while not Lab3Funkcje.czyProstokatny(a, b, c):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)

if Lab3Funkcje.czyProstokatny(a, b, c):
    print("Trójkąt", a, b, c, "jest prostokątny", sep=' ', end='\n')

del a

del b

del c

# Zadanie 5
print("\nZadanie 5")

print("\nPoniżej wykonanie z wartościami domyślnymi")
print(Lab3Funkcje.poleTrapezu())

print("\nPoniżej wykonania poprawne")
for x in range(10):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    h = random.randint(1, 20)

    print("Trapez o podstawach", a, "i", b, "oraz wysokości", h, "ma pole", Lab3Funkcje.poleTrapezu(a, b, h),
          sep=' ', end='\n')

del a
del b
del h

# Zadanie 6
print("\nZadanie 6\nIloczyn ciągu dziesięcio elementowego o wyrazie początkowym 1 i ilorazie 4 to:",
      Lab3Funkcje.iloczynCiagu())

# Zadanie 7
print("\nZadanie 7")

print("Iloczyn ciągu o elementach 1, 2, 4, 8 =", Lab3Funkcje.iloczynCiagu_n_Elementowego(1, 2, 4, 8))

# Zadanie 8
print("\nZadanie 8")
