'''
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

#leggo i file
m0 = pd.read_csv('hit_times_M0.csv')
m1 = pd.read_csv('hit_times_M1.csv')
m2 = pd.read_csv('hit_times_M2.csv')
m3 = pd.read_csv('hit_times_M3.csv')

mod0=m0['mod_id'].values
det0=m0['det_id'].values
hit0=m0['hit_time'].values
mod1=m1['mod_id'].values
det1=m1['det_id'].values
hit1=m1['hit_time'].values
mod2=m2['mod_id'].values
det2=m2['det_id'].values
hit2=m2['hit_time'].values
mod3=m3['mod_id'].value
det3=m3['det_id'].values
hit3=m3['hit_time'].values

def hit(m, s, t):
    
