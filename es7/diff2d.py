'''
Esercitazione su Metodi Montecarlo
Diffusione 2D
Produrre uno script python che definisca una procedura di Random Walk 
in due dimensioni.

Diffusione 2D simmetrica
Ad ogni passo lo spostamento può andare con uguale probabilità in ogni direzione
(probabilità costante per  0<=phi<=2pigreco)
Delta_x=s*cos(phi);
Delta_y=s*sen(phi);
1)Produrre un grafico 2D delle posizioni di 5 random walker per 1000 passi.
2)Produrre un grafico 2D della posizione di 1000 random walker dopo
10, 100 e 1000 passi.
'''
import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt

def rwalk2d(step, N):
    deltax = np.zeros(N+1)
    tmpx = 0.
    deltay = np.zeros(N+1)
    tmpy = 0.
    phi = np.random.uniform(low=0, high=2*np.pi, size=N)
    for i in range(len(phi)):
        tmpx = tmpx + step*np.cos(phi[i])
        deltax[i+1] = tmpx
        tmpy = tmpy + step*np.sin(phi[i])
        deltay[i+1] = tmpy
    return deltax, deltay
for i in range(5):
    x,y = rwalk2d(1, 1000)
    plt.plot(x, y)
plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$\Delta y$')
plt.show()

passi10x = np.zeros(1000)
passi100x = np.zeros(1000)
passi1000x = np.zeros(1000)

passi10y = np.zeros(1000)
passi100y = np.zeros(1000)
passi1000y = np.zeros(1000)
for i in range(1000):
    x,y = rwalk2d(1, 1000)
    passi10x[i] = x[10]
    passi10y[i] = y[10]
    passi100x[i] = x[100]
    passi100y[i] = y[100]
    passi1000x[i] = x[1000]
    passi1000y[i] = y[1000]
plt.plot(passi1000x, passi1000y, 'o', markersize=3, color='teal', label='millesimo passo')
plt.plot(passi100x, passi100y, 'o',markersize=3, color='cyan', label='centesimo passo')
plt.plot(passi10x, passi10y, 'o', markersize=3, color='cornflowerblue', label=' decimo passo')


plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$\Delta y$')
plt.legend()
plt.show()
