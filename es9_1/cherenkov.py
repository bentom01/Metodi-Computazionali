'''
Passo 3:

Creare uno script python che svolga le seguenti operazioni:
-Importi il modulo reco
-Legga i file di dati e per ognuno di essi produca un array di reco.Hit
--SUGGERIMENTO: creare un funzione da richiamare per ogni file
-Produca una un array che corrisponda al conbinazione, 
ordinata temporalmente, di tutti i reco.Hit
-Produca un istogramma dei (delta_t) fra reco.Hit consecutivi
--Come stabilire la finestra temporale da applicare ai delta_t
che permetta di raggruppare gli Hit dello stesso evento 
ma separi quelii apparteneti ad eventi differenti?
'''

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
    event = np.empty([])
    conta = 0
    deltatimes = np.diff(arrhit)
    for i in range(len(arrhit)-1):
        if harrhit[i+1]-arrhit[i] > treshold:
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

for i in range(len(hit)-1):
    if hit[i] > hit[i+1]:
        a = hit[i]
        hit[i] = hit[i+1]
        hit[i+1] = a

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

Modificare lo script del Passo 3 aggiungendo funzionalità in modo che:
1) Crei un array di oggeti di tipo reco.Event a partire dall'array 
ordinato di reco.Hit applicando a una finestra temporale ai deltat 
tra reco.Hit consecutivi
SUGGERIMENTO: creare un funzione apposita
2) Stampi informazioni dettagliate per i primi 10 reco.Event
SUGGERIMENTO: verificare che le informazioni stampate 
non contengano indizi di errore
3) Produca l'istogramma del numero di reco.Hit per reco.Event
4) Produca l'istogramma della durata dei reco.Event
5) Produca l'istogramma delle differenze di tempo fra reco.Event consecutivi
6)Produca il grafico 2D del numero di hit nell'evento in funzione della durata
* SUGGERIMENTO: usare `plt.scatter`
'''
   
