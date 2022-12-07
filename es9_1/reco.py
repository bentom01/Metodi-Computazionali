'''
Creare il file reco.py che:
-Definisca la classe Hit
--Un oggetto di tipo Hit deve contenere informazioni su:
---Id Modulo
---Id Sensore
---Time Stamp rivelazione
-Definisca la classe Event
--Un oggetto di tipo Event deve contenere informazioni su:
---Numero di Hit
---Time Stamp del primo Hit
---Time Stamp dell'ultimo Hit
---Durata temporale
---Array di tutti gli Hit
'''

class Hit:
    def __init__(self, mod, sens, time):
        self.modulo = mod
        self.sensore = sens
        self.timestamp = time

class Event:
    def __init__(self, n, tf, tl, dt, arr):
        self.numero = n
        self.timefirst = tf
        self.timelast = tl
        self.deltat = dt
        self.array = arr
