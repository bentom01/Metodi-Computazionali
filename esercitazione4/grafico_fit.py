'''il file di dati fit_data.csv contiene dei valori per le variabili x e y;
i valori di  possono essere considerati dei conteggi e 
seguono la statistica poissoniana;
si può ipotizzare che i dati rappresentino una curva lognormale 
(gaussiana nel logaritmo dei valori di x);
creare uno script python che:
legga il file di dati fit_data.csv;
produca un grafico di y in funzione di x nella forma più appropriata;'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tab = pd.read_csv('fit_data.csv')
print(tab)

x1 = np.array(tab['x'])
y1 = np.array(tab['y'])
erry = np.sqrt(y1)

print('ascisse: ', x1, len(x1))
print('ordinate: ', y1, len(y1))
print(erry, len(erry))

plt.errorbar(x1, y1, erry, fmt='-o', color='aqua')
plt.xlabel('x')
plt.ylabel('y')
plt.xscale('log')
plt.show()
