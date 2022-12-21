import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importo reco
import reco

#leggo i file e produco un array di reco.Hit
def arr_hit(tab):
    mod = tab['mod_id'].values
    det = tab['det_id'].values
    time = tab['hit_time'].values
    arr = np.full(len(mod), reco.Hit(0,0,0))
    for i in range(len(mod)):
        arr[i] = reco.Hit(mod[i], det[i], time[i])
    return arr

def arr_event(arrhit, treshold):
    event = np.empty(0)
    event = np.append(event, reco.Event())
    for i in range(len(arrhit)-1):
        if arrhit[i+1].time-arrhit[i].time > treshold:
            event = np.append(event, reco.Event())
        event[-1].aggiungi(arrhit[i])
    return event
    

m0 = pd.read_csv('hit_times_M0.csv')
m1 = pd.read_csv('hit_times_M1.csv')
m2 = pd.read_csv('hit_times_M2.csv')
m3 = pd.read_csv('hit_times_M3.csv')

hit0 = arr_hit(m0)
hit1 = arr_hit(m1)
hit2 = arr_hit(m2)
hit3 = arr_hit(m3)

#produco un array ordinato temporalmente di tutti gli array
hit = np.concatenate((hit0, hit1, hit2, hit3))
'''
for i in range(len(hit)-1):
    if hit[i] > hit[i+1]:
        a = hit[i]
        hit[i] = hit[i+1]
        hit[i+1] = a
'''
hit.sort(kind='mergesort')
'''
for i in range(len(hit)):
    print(hit[i].time)
'''
#istogramma delta_t fra reco.Hit consecutivi

times=np.array([h.time for h in hit])

deltat = np.diff(times)
mask = deltat > 0
plt.hist(np.log10(deltat[mask]), bins=70, alpha=0.8, color='paleturquoise', ec='darkcyan')
plt.show()

#finestra temporale del primo evento è 10^2 ns,
#poi iniziano gli hit collegati al secondo evento

'''
Passo 4:
5) Produca l'istogramma delle differenze di tempo fra reco.Event consecutivi
6)Produca il grafico 2D del numero di hit nell'evento in funzione della durata
* SUGGERIMENTO: usare `plt.scatter`
'''
timewindow = 10**2.3

ev = arr_event(hit, timewindow)
#stampo le informazioni dei primi 10 eventi
for i in range(11):
    print(ev[i])

print(len(ev))
    
nhits = np.empty(0)
deltahits = np.empty(0)
for e in ev:
    nhits = np.append(nhits, e.numero)
    deltahits = np.append(deltahits, e.durata)
    
#istogramma del numero di reco.Hit per reco.Event    
plt.hist(nhits, bins=20, alpha=0.8, color='yellowgreen', ec='olivedrab')
plt.yscale('log')
plt.show()

#istogramma della durata degli eventi
plt.hist(deltahits, bins=70, alpha=0.8, color='lightpink', ec='palevioletred')
plt.yscale('log')
plt.show()

#istogramma della differenza dei tempi tra reco.Event consecutivi

