import numpy as np

import random as rand


#zad 1
zad = 1
print("Zadanie", zad)
a = np.arange(1, 4)
b = np.arange(4, 7)
print(a, b, a * b)

del a, b
#zad 2
zad += 1
print("Zadanie", zad)


def randmatrix(a, b):
    mac = np.zeros((a, b))
    for x in range(a):
        for y in range(b):
            mac[x][y] = rand.randint(1, 100)
    return mac


def foo(mac):
    mincol = [mac[0][x] for x in range(mac.shape[0])]
    minrow = [mac[x][0] for x in range(mac.shape[1])]
    for b in range(mac.shape[0]):
        for c in range(mac.shape[1]):
            if minrow[b] >= mac[b][c]:
                minrow[b] = mac[b][c]
            if b == 0:
                for d in range(mac.shape[0]):
                    if mincol[c] >= mac[d][c]:
                        mincol[c] = mac[d][c]
    return minrow, mincol

a = randmatrix(3, 3)
a1, a2 = foo(a)

print(a, a1, a2)

a = randmatrix(4, 4)
a1, a2 = foo(a)

print(a, a1, a2)

del a, a1, a2

#zad 3
zad += 1
print("Zadanie", zad)

a = np.arange(1, 4)
b = np.arange(4, 7)
print(a, b, np.dot(a, b))

del a, b

#zad 4
zad += 1
print("Zadanie", zad)

a = randmatrix(1, 3)
a = a*2.5
b = randmatrix(1, 3)
b = b.astype('int64')

print(a, b, a * b)

del a, b

#zad 5
zad += 1
print("Zadanie", zad)


a = randmatrix(2, 3)

print(a)

a = np.sin(a)

print(a)

del a

#zad 6
zad += 1
print("Zadanie", zad)

a = randmatrix(2, 3)

print(a)

a = np.cos(a)

print(a)

del a

#zad 7
zad += 1
print("Zadanie", zad)

a = randmatrix(1, 3)
b = randmatrix(1, 3)

c = np.add(a, b)

print(a, b, c)

del a, b, c


#zad 8
zad += 1
print("Zadanie", zad)

a = randmatrix(3, 3)
print(a)
for b in range(a.shape[0]):
    print(a[b, :])

del a

#zad 9
zad += 1
print("Zadanie", zad)

a = randmatrix(3, 3)
print(a)
for b in a.flat:
    print(b)

del a

#zad 10
zad += 1
print("Zadanie", zad)

a = randmatrix(9, 9)
b = a.reshape((27, 3)) #zmienianie kształtu na taką samą ilość elementów
c = a[0:5, 0:5] #Wycinanie pewnych rzędów/kolumn

print(a, b, c)

del a, b, c

#zad 11
zad += 1
print("Zadanie", zad)

a = randmatrix(1, 12)
b = a.reshape((3, 4))
c = a.reshape((4, 3))
d = a.reshape((2, 6))

print(a, b, c, d, a.flatten(), b.flatten(), c.flatten(), d.flatten(), sep='\n\n')

