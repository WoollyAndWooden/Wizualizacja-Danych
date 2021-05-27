import numpy as np

import random as rand

import string

zad = 1
# Zad 1
print("\nZadanie", zad, sep=' ', end='\n')

tab = np.arange(4, 4*21, 4)

print(tab)

del tab
zad+=1

# Zad 2
print("\nZadanie", zad, sep=' ', end='\n')

tab = np.arange(1.1, 10, 1.1, dtype='float')
print(tab)
tab2 = tab.astype('int64')
print(tab2)

del tab, tab2
zad+=1

# Zad 3
print("\nZadanie", zad, sep=' ', end='\n')


def foo3(n):
    n = int(n)
    return np.arange(1, n * n + 1)


print(foo3(5.5))
zad+=1

# Zad 4
print("\nZadanie", zad, sep=' ', end='\n')


def foo4(n1, n2):
    return np.logspace(1, n2, num=n2, base=n1,dtype='int64')


print(foo4(2, 4))
zad+=1

# Zad 5
print("\nZadanie", zad, sep=' ', end='\n')

def foo5(n):
    x1 = rand.randint(1, n-1);
    x2 = (n**2 - (x1 ** 2))**(1/2)
    wektor = np.zeros((2,2))

    wektor[0][0] = x1
    wektor[1][1] = x2
    return wektor

wektor = foo5(10)
print(wektor)

del wektor
zad+=1

# Zad 6
print("\nZadanie", zad, sep=' ', end='\n')

def foo6(word1, word2, word3):
    wykreslanka = np
zad+=1

# Zad 7
print("\nZadanie", zad, sep=' ', end='\n')

def foo7(n):
    mac = np.diag([2 for a in range(n)])
    for i in range(n):
        b = 1
        for j in range(i+1, n):
            b+=1
            mac[i][j] = 2*(b)
            mac[j][i] = 2*(b)

    return mac

mac = foo7(5)
print(mac)

del mac
zad+=1

# Zad 8
print("\nZadanie", zad, sep=' ', end='\n')


def foo8(mac, kier):
    if mac.shape[kier] % 2 != 0:
        print("nie można podzielić na pół w tym kierunku")
    elif kier == 0:

       mac = mac[:int(mac.shape[kier] / 2)]

    else:
        mac = mac[:, :int(mac.shape[kier] / 2)]

    return mac

mac = np.ones((2, 6))

mac = foo8(mac, 1)

print(mac)

del mac

zad+=1

# Zad 9
print("\nZadanie", zad, sep=' ', end='\n')

def foo9(a1, r):
    mac = np.arange(a1, a1 + 25 * r, r)
    return mac.reshape((5, 5))


print(foo9(1, 10))
zad+=1




