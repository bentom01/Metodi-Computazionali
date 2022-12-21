import numpy as np

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
    def __str__(self):
        return 'Evento con ' + str(self.numero) + ' hit rilevati \n tempo del primo hit ' + str(self.timefirst) + "\n tempo dell'ultimo hit " + str(self.timelast) + "\n durata dell'evento " + str(self.durata)
