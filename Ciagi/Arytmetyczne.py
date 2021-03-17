# nty Element Ciągu z wyrazu pierwszego
def nElementArytma1(a1, n, r):
    return a1 + (n - 1) * r


#nty element z wyrazu w środku
def nElementArytmaak(ak, k, n, r):
    return ak + (n - k) * r


# Suma
def sumaArytma(a1, an, n):
    return ((a1 + an) / 2) * n


# Wyraz środkowy
def wyrazSrodkowyArytma(x, z):
    return (x + z) / 2