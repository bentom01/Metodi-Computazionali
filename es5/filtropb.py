'''Scrivere uno script python che:

- Risolva l'equazione differenziale per Vout dato Vin.

-Definisca Vin per il tempo 0<=t<=10 tale che:
Vin(t) è +1 per t pari e -1 per t dispari (onda quadra?)

-Produca un grafico di Vin e Vout per:
RC=1, RC=0.1, RC=0.01
con la condizione iniziale Vout(0)=0.

-Salvi i risultati (t, Vin(t), Vout(t)) in un file CSV. 
I risultati per Vout(t) per i tre valori di RC vanno salvati nello stesso file.

-OPZIONALE ripetere i passi precendenti con in potenziale Vin diverso.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd
import csv

#funzione di Vin
def ddpi(t):
    if int(t)%2 == 0:
        return 1
    else:
        return -1

#funzione per l'equazione differenziale
def fddpo(vout, t, ff, RC):
    '''
    funzine fddp(vout)= 1/RC(vin - vout) -> inizialmente R=C=1
    '''
    return (ff(t) - vout)/RC

#intervallo [a,b] e punto di partenza Vout(0)=0
a = 0.
b = 10.
v0 = 0.

NN = 1000 #numero intervalli di tempo
h = (b-a)/NN #passo intervalli
tt = np.arange(a,b,h) #intervalli

#ottengo i valori di Vin
Vin=np.zeros(len(tt))
for i in range(len(tt)):
    Vin[i]=ddpi(tt[i])

#grafico Vin in funzione del tempo
plt.plot(tt, Vin, color='turquoise')
plt.title('Vin in funzione del tempo', color='teal', fontsize=14)
plt.show()

#calcolo soluzioni tramite scipy.integrate.odeint
vv1 = np.empty(0)
vv2 = np.empty(0)
vv3 = np.empty(0)
vv1 = integrate.odeint(fddpo, v0, tt, args=(ddpi, 1))
vv2 = integrate.odeint(fddpo, v0, tt, args=(ddpi, 0.1))
vv3 = integrate.odeint(fddpo, v0, tt, args=(ddpi, 0.01))



#grafico soluzioni RC=1
plt.title('Vout con RC=1 ', color='indigo', fontsize=14)
plt.plot(tt, vv1, color='mediumpurple' )
plt.xlabel('t')
plt.ylabel('Vout')
plt.show() 

#grafico soluzioni RC=0.1
plt.title('Vout con RC=0,1 ', color='forestgreen', fontsize=14)
plt.plot(tt, vv2, color='seagreen' )
plt.xlabel('t')
plt.ylabel('Vout')
plt.show() 

#grafico soluzioni RC=0.01
plt.title('Vout con RC=0.01 ', color='cadetblue', fontsize=14)
plt.plot(tt, vv3, color='paleturquoise' )
plt.xlabel('t')
plt.ylabel('Vout')
plt.show() 

#grafico in cui li raggruppo tutti
plt.plot(tt, vv1, color='mediumpurple', label='RC=1')
plt.plot(tt, vv2, color='seagreen', label='RC=0.1')
plt.plot(tt, vv3, color='paleturquoise', label='RC=0.01')
plt.xlabel('t')
plt.ylabel('Vout')
plt.show()
