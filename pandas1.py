import pandas as pd
import xlrd
import openpyxl

names = pd.ExcelFile('datasets/imiona.xlsx')
names = pd.read_excel(names)
names = pd.DataFrame(names)


#1
print("############################")
print("Liczba nadanych imion < 1000")
print(names[names['Liczba'] < 1000])


#2
print("############")
print("Te same imie")
print(names[names['Imie'] == 'DANIEL'])


#3
print("############")
print("Suma urodzeń")
print(names['Liczba'].sum())


#4
print("###########################")
print("Suma urodzeń lata 2005-2010")
var = names[((names.Rok >= 2005) & (names.Rok <= 2010))]
print(var.Liczba.sum())

del var

#5
print("##############################")
print("Suma urodzeń chłopców rok 2000")
var = names[((names.Rok == 2000) & (names.Plec == 'M'))]
print(var.Liczba.sum())

del var


#6
print("#######################################")
print("Najpopularniejsze imie M/F na każdy rok")
var = names.groupby(['Rok'])

for a, frame in var:
    var2 = frame.groupby(['Plec'])
    for b, frame2 in var2:
        print(frame2[frame2['Liczba'].max() == frame2['Liczba']], end='\n\n')

del var


#7
print("########################################")
print("Najpopularniejsze imie M/F na cały okres")
var = names.groupby('Plec')

for a, frame in var:
    print(frame[frame['Liczba'].max() == frame['Liczba']], end='\n\n')

del names


#Kolejny plik
zam = pd.read_csv('datasets/zamowienia.csv', sep=';', decimal='.')
zam = pd.DataFrame(zam)
print(zam)

#11
print("########################")
print("Lista unikalnych nazwisk")
print(zam['Sprzedawca'].unique())


#12
print("######################")
print("5 najwyższych zamówień")
zam2 = zam.sort_values('Utarg', ascending=0)
print(zam2.head(5))
del zam2


#13
print("#################################################")
print("ilość zamówień złożonych przez każdego sprzedawcę")
zam2 = zam.groupby('Sprzedawca')

for a, frame in zam2:
    print(a, "złożył", frame['idZamowienia'].count(), "zamówień")

del zam2

#14
print("###############################")
print("sumę zamówień dla każdego kraju")
zam2 = zam.groupby('Kraj')

for a, frame in zam2:
    print("Do kraju", a, "złożono", frame['idZamowienia'].count(), "zamówień o wartości", frame['Utarg'].sum())

del zam2


#15
print("#####################################################")
print("sumę zamówień dla roku 2005, dla sprzedawców z Polski")
zam['Data zamowienia'] = pd.to_datetime(zam['Data zamowienia'])
zam["Rok"] = pd.DatetimeIndex(zam['Data zamowienia']).year

zam2 = zam[((zam['Rok'] == 2005) & (zam['Kraj'] == 'Polska'))]
print(zam2['Utarg'].sum())
del zam2


#15
print("####################################")
print("średnią kwotę zamówienia w 2004 roku")

zam2 = zam[zam['Rok'] == 2004]
print(zam2['Utarg'].mean())

del zam2



#15
print("################################################################################################")
print("zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv")
zam2004 = zam[zam.Rok == 2004]
zam2005 = zam[zam.Rok == 2005]
zam2004.to_csv('datasets/2004.csv', columns=('Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'), index='False')
zam2005.to_csv('datasets/2005.csv', columns=('Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'), index='False')