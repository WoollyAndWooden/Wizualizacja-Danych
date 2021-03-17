# nty Element Ciągu
def nElementGeo(a1, q, n):
    return a1 * q ** (n - 1)


# Suma Ciągu
def sumGeo(a1, n, q = 1):
    if(q == 1):
        return n * a1
    return a1 * ((1 - q ** n) / (1 - q))


# Wyraz Środkowy
def wyrazSrodkowyGeo(a, b):
    return sqrt(a * b)