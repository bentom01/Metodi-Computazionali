'''Partendo dalla formula per il periodo T appena ricavata,
scrivere uno script python che:
-calcoli il periodo in funzione del punto di partenza x0
 (utilizzando scipy.integrate.simpson)
-produca un grafico di T in funzione di x0
-OPZIONALE: provare formule alternative per  (rispettando la condizione di simmetria rispetto all'origine).'''

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

'''xx = np.arange(-5,5.05, 0.1)
plt.plot(xx, 0.1*xx**6, color='slategray')
plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('V(x)')
plt.plot(4.5, 0.1*4.5**6, 'o', markersize=12, color='tomato')
plt.show()'''

def V(x, k):
    return k*x**6

def periodo(x0, m, k):
    x = np.arange(0, x0-0.00001, 0.00001)
    t = 1/np.sqrt((V(x0, k)-V(x, k)))
    return np.sqrt(8*m)*integrate.simpson(t, x)

print('T = ', periodo(2,1,1))

s = np.arange(0.5, 5, 0.1)
T = np.empty(0)
for i in range(0, len(s)):
    T = np.append(T, periodo(s[i], 1, 1))

plt.plot(s, T, color='lightblue')
plt.xlabel('posizione iniziale')
plt.ylabel('periodo')
plt.yscale('log')
plt.show()

