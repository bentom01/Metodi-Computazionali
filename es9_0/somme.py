'''
Creare il file python somme.py in cui vanno definite due funzioni:
->una funzione che restituisca la somma dei primi n numeri naturali;
->una funzione che restituisca la somma delle radici dei primi n numeri 
naturali.
Creare uno script python che importi il modulo somme appena creato e ne 
utilizzi le funzioni
Esaminare la cartella di lavoro
'''

import numpy as np
import sys, os


def naturali(n):
    '''
funzione che restituisce la somma dei 
primi n numeri naturali
'''
    sn=np.arange(1, n+1)
    return np.sum(sn)

def radici(n):
    '''
funzione che resituisce la somma delle 
radici dei primi n numeri naturali
'''
    sr=np.arange(1, n+1)
    sr=np.sqrt(sr)
    return np.sum(sr)

sys.path.append('~/Metodi-Computazionali/es9_0')
