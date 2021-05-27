import pandas as pd
import xlrd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

zad=1
#Zad 1
print("Zad", zad)
z = np.arange(0, 2.1, 0.1)
plt.plot(z, np.sin(z), label='sin(z)')
plt.plot(z, np.cos(z), label='cos(z)')
plt.xlabel('z')
plt.ylabel('sin(x) cos(x)')
plt.legend(loc='upper right')
plt.title('Wykres sin(x), cos(x)')
plt.show()

