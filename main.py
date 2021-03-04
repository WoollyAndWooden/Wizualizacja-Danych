#Zad 1

zmiennastring1 = 'To zmienna łańcuchowa'

zmiennastring2 = '''To
Kilkulinijkowa
Zmienna
łańcuchowa'''

zmiennaint1, zmiennaint2 = 5, 15

zmiennafloat1, zmiennafloat2 = 3.14, 4.20

zmiennacomplex1, zmiennacomplex2 = 5 + 3j, 4 - 2j

print(zmiennastring1 + ' ' + zmiennastring2)
print(zmiennaint1)
print(zmiennaint2)
print(zmiennafloat1)
print(zmiennafloat2)
print(zmiennacomplex1)
print(zmiennacomplex2)

#Zad 2

#a = input(u"Wprowadź pierwszą liczbę")
a = 5 #int(a)
operator = '+' #input(u"Wprowadź operator działania (+, -, *, **, /, //, %")

#b = input(u"Wprowadź drugą liczbę")
b= 4#int(b)
if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '*':
    print(a*b)
elif operator == '**':
    print(a ** b)
elif operator == '/':
    print(a / b)
elif operator == '//':
    print(a // b)
elif operator == '%':
    print(a%b)
else:
    print(u"Błędny operator")

#Zad 3

a = int(2)
a+=1
print(a)

a = 2
a-=1
print(a)

a = 2
a*=a
print(a)

a = 2
a**=a
print(a)

a = 2
a/=a
print(a)

a = 2
a%=2
print(a)

#Zad 4
import math
e = 2.718281

print('e^10')
print(e**10)

print('(ln(5+sin^2(8))^(1/6)')
print(math.log(5+(math.sin(8)**2))**(1/6))

#Zad 5
Imie = 'DANIEL'
Nazwisko = 'KNOPF'

print(Imie.capitalize()+' '+Nazwisko.capitalize())

#Zad 6
Piosenka = 'la la la'
ile = Piosenka.count('la')
print(ile)
print("\'la\' się powtórzyło", ile, 'razy', sep=' ')

#Zad 7
Lancuch = 'To jest jakiś napis'

print(Lancuch[1], Lancuch[len(Lancuch)-1], sep=' ')

#Zad 8
Podzielone = Piosenka.split()
print(Podzielone)




