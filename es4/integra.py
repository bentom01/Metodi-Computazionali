'''Distanza percorsa in funzine del tempo
il file di dati vel_vs_time.csv contiene dei valori di velocitÃƒÂ  in funzione del tempo;
creare uno script python che:
-legga il file scaricato;
-produca un grafico della velocità  in funzione del tempo;
-calcoli la distanza percorsa in funzopne del tempo (utilizzando scipy.integrate.simpson);
-produca il grafico della distanza percorsa in funzione del tempo.
SUGGERIMENTO: assicurarsi di comprendere bene il comportamento della funzione 
scipy.integrate.simpson agli estremi dell'intervallo di integrazione.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate

tab = pd.read_csv('vel_vs_time.csv')
#print(tab)
tem = np.array(tab['t'])
vel = np.array(tab['v'])

#print('i tempi sono: ', vel)
#print('le velocità sono: ', tem)

plt.plot(tem, vel, color='purple')
plt.xlabel('tempo [s]')
plt.ylabel('velocità [m/s]')

plt.show()

#print(integrate.simpson(vel, tem))

s = np.array([0])

for i in range(1, 200):
    s =np.append(s,  integrate.simpson(vel[:i], tem[:i]))

#s = np.append(s,integrate.simpson(vel, tem)) 

#print('gli spazi percorsi sono. ',s)
#print(len(s))

plt.plot(tem, s, color='violet')
plt.xlabel('tempo [s]')
plt.ylabel('spazio [m]')

plt.show()

