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
        self.time = time
    def __gt__(self, altro):
        return self.time > altro.time
    def __lt__(self, altro):
        return self.time < altro.time
    def __eq__(self, altro):
        return self.time == altro.time
 
class Event:
    def __init__(self):
        self.numero = 0
        self.timefirst = -1
        self.timelast = -1
        self.deltat = -1
        self.hit = np.empty(0)
    def aggiungi(self, hit):
        self.hit = np.append(self.hit, hit)
        self.numero = len(self.hit)
        if len(self.hit) == 1:
            self.timefirst = hit.time
        self.timelast = hit.time
        self.durata = self.timelast - self.timefirst
