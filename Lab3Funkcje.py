# Definicje funkcji
# Do zadania 2
def evenCheck(n):
    n = str(n)
    l = len(n)
    dotEncountered = False

    # Przewijamy liczbę przez jej długość, ale wyświetlać będziemy od tyłu
    for i in range(1, l + 1):

        # Sprawdzamy czy minęliśmy część ułamkową liczby czy nie
        # i przechodzimy do kolejnego kroku pętli
        if n[i * -1] == '.':
            dotEncountered = True
            continue

        # Jeśli na końcu jest 0, oraz nie było kropki,
        # znajdujemy się w części ułamkowej,
        # więc pierwsze 0 nie mają znaczenia
        if n[i * -1] == '0' and not dotEncountered:
            # do kolejnego kroku pętli
            continue

        # Jeśli żadne z powyższych nie są spełnione,
        # sprawdćź czy aktualna pozycja jest podzielna przez 2
        # jeśli jest,
        # cała liczba jest parzysta
        if int(n[i * -1]) % 2 == 0:
            return True
        return False


# Do zadania 4
def czyProstokatny(a, b, c):
    if c > a and c > b:
        if c ** 2 == a ** 2 + b ** 2:
            return True
        return False
    if b > c and b > a:
        if b ** 2 == a ** 2 + c ** 2:
            return True
        return False

    if a ** 2 == b ** 2 + c ** 2:
        return True
    return False


# Do zadania 5
def poleTrapezu(a=0, b=0, h=0):
    if a == 0 or b == 0 or h == 0:
        print("Zapomniałeś podać któregoś z argumentów")
        return 0
    return ((a + b) * h) / 2


# Do zadania 6
def iloczynCiagu(a = 1, b = 4, ile = 10):
    if ile == 1:
        return a
    return (a * b ** (ile - 1)) * iloczynCiagu(a, b, ile - 1)


# Do zadania 7
def iloczynCiagu_n_Elementowego(* elementy):

    if len(elementy) == 0:
        return 0

    iloczyn = 1

    for i in elementy:
        iloczyn *= i

    return iloczyn

