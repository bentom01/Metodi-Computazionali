'''
In uno script seaparato generare una distribuzione random di phi tale che 
p(phi)=1/4sin(phi/2).

SUGGERIMENTO: utilizzare il metodo della cumulativa;
SUGGERIMENTO: controllare che il risultato sia corretto 
attraverso un istogramma dei valori di phi generati (plt.hist).
'''
import numpy as np
import scipy
import matplotlib.pyplot as plt

#la cumulativa è (1-cos(phi/2))/2, quindi calcolo l'inversa
def inv_cum(y):
    return 2*np.arccos(1-2*y)
#grafico
yc  = np.arange(0,1, 0.001)
xc  = inv_cum(yc)
plt.plot(yc, xc, color='darkcyan')
plt.grid()
plt.xlabel('y')
plt.ylabel(r'$c^{-1}$(y)')
plt.show()

#istrogrammi
yp = np.random.uniform(low=0, high=1, size=10000)
xp = inv_cum(yp) 
fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(yp, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(xp, bins=100, range=(0,2*np.pi), color='orange', ec='darkorange')
ax[1].set_title(r'$\frac{1}{4}sin(\frac{\phi}{2})$')
ax[1].set_xlabel('x')
plt.show()
