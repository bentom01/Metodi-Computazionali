'''
Diversi tipi di rumore sono identificati da come l'ampiezza delle oscillazioni 
è legata alla loro frequenza, tale relazione si rispecchia in uno spettro di 
potenza di pendenza diversa.

Il rumore bianco (white noise) ha la stessa ampiezza a tutte le frquenze;
Il rumore rosa (pink noise) ha una dipendenza dello spettro di potenza come 1/f;
Il rumore rosso (red noise), anche detto brown noise perchè legato al moto 
browninano, ha una dipendenza dello spettro di potenza come 1/f^2.
In generale la dipendenza dello spettro di potenza dalla frequenza può essere 
espressa come 1/f^beta.

Vengono messi a disposizione tre file con diversi campioni di rumore:

data_sample1.csv
data_sample2.csv
data_sample3.csv
Realizzare uno script python che:

-Legga i tre file messi a disposizione;
-Produca un grafico dei tre segnali di ingresso;
-Calcoli la trasformata di Fourier dei segnali di ingreso e produca 
il grafico dello spettro di potenza;
-Faccia il fit dei tre spettri di potenza per determinarne l'andamento 
in funzione della frequenza e identifichi il tipo di rumore per ogni 
serie di dati.
-Confronti i tre spettri di potenza e i relativi fit
'''
import numpy as np
import pandas as pd
from scipy import constants, fft, optimize
import matplotlib.pyplot as plt

#leggo il file csv
dati1 = pd.read_csv('data_sample1.csv')
dati2 = pd.read_csv('data_sample2.csv')
dati3 = pd.read_csv('data_sample3.csv')

#print delle tabelle
'''
print(dati1)
print(dati2)
print(dati3)
'''

#array dei dati delle tabelle
t1 = dati1['time'].values
t2 = dati2['time'].values
t3 = dati3['time'].values
m1 = dati1['meas'].values
m2 = dati2['meas'].values
m3 = dati3['meas'].values

'''
#grafico dei rumori
plt.plot(t1, m1, color='lightgrey')
plt.plot(t2, m2, color='magenta')
plt.plot(t3, m3, color='red')

plt.xlabel('t')
plt.ylabel('frequenza')

plt.show()
'''
#trasformata di fourier
trasf1 = fft.rfft(m1)
trasf2 = fft.rfft(m2)
trasf3 = fft.rfft(m3)

#frequenze
a = 0.5

freq1 = a*fft.rfftfreq(trasf1.size, d=1)
freq2 = a*fft.rfftfreq(trasf2.size, d=1)
freq3 = a*fft.rfftfreq(trasf3.size, d=1)

'''
print(len(freq1))
print(len(trasf1))
'''
'''
#grafico delle trasformate
plt.plot(freq1[:trasf1.size//2], np.absolute(trasf1[:trasf1.size//2])**2, 'o', markersize=4, color='lightgrey')
plt.plot(freq2[:trasf2.size//2], np.absolute(trasf2[:trasf2.size//2])**2, 'o', markersize=4, color='magenta')
plt.plot(freq3[:trasf3.size//2], np.absolute(trasf3[:trasf3.size//2])**2, 'o', markersize=4, color='red')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('t')
plt.ylabel('noise')

plt.show()
'''

#fit

#definizione funzione
def noise(f, a, n):
    return a/(f**n)
#n=0 -> white noise, n=1 -> pink noise, n=2 -> red noise


pstart = np.array([1, 1])
params1, params_covariance1 = optimize.curve_fit(noise, freq1[30:trasf1.size//2], np.absolute(trasf1[30:trasf1.size//2])**2, p0=[pstart])
params2, params_covariance2 = optimize.curve_fit(noise, freq2[30:trasf2.size//2], np.absolute(trasf2[30:trasf2.size//2])**2, p0=[pstart])
params3, params_covariance3 = optimize.curve_fit(noise, freq3[30:trasf3.size//2], np.absolute(trasf3[30:trasf3.size//2])**2, p0=[pstart])

print('params1 ', params1)
print('params_covariance1 ', params_covariance1)
print('params2 ', params2)
print('params_covariance2 ', params_covariance2)
print('params3 ', params3)
print('params_covariance3 ', params_covariance3)

y1=noise(freq1[1:trasf1.size//2], params1[0], params1[1])
y2=noise(freq2[1:trasf2.size//2], params2[0], params2[1])
y3=noise(freq3[1:trasf3.size//2], params3[0], params3[1])

#grafico fit
'''
plt.plot(freq1[1:trasf1.size//2], y1, color='lightgrey', label='fit white noise')
plt.plot(freq2[1:trasf2.size//2], y2, color='magenta', label='fit pink noise')
plt.plot(freq3[1:trasf3.size//2], y3, color='red', label='fit red noise')

plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
'''
#grafico spettri e fit
plt.plot(freq1[:trasf1.size//2], np.absolute(trasf1[:trasf1.size//2])**2, 'o', markersize=4, color='lightgrey')
plt.plot(freq2[:trasf2.size//2], np.absolute(trasf2[:trasf2.size//2])**2, 'o', markersize=4, color='pink')
plt.plot(freq3[:trasf3.size//2], np.absolute(trasf3[:trasf3.size//2])**2, 'o', markersize=4, color='tomato')
plt.plot(freq1[1:trasf1.size//2], y1, color='grey', label='fit white noise')
plt.plot(freq2[1:trasf2.size//2], y2, color='magenta', label='fit pink noise')
plt.plot(freq3[1:trasf3.size//2], y3, color='red', label='fit red noise')


plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
           
