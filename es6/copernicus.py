'''
Scrivere uno script python che:
1)Legga il file copernicus_PG_selected.csv;
2)Produca un grafico della concentrazione di inquinanti in funzione del tempo;
  -Si noti che il tempo è espresso in due modi diversi in altrettante colonne;
  -Scegliere il metodo più adatto per rappresentare il tempo;
3)Analizzi i dati per la CO come di seguito:
  -Calcoli la trasformata di Fourier della serie temporale
  -Produca un grafico dello spettro di potenza in funzione della frequenza
  -Identifichi eventuali periodicità
  -Produca il grafico dello spettro di potenza in funzione del periodo
  -Applichi un filtro ai coefficienti di fourier selezionando solo le 
componenti che descrivono l'andamento generale in funzione del tempo 
(escludendo futtuazioni di breve periodo)
  -Calcoli la trafsformata di Fourier inversa a partire dai coefficienti filtarti
  -Produca un grafico che confronti il segale originale con quello filtrato
  -OPZIONALE: Ripeta l'analisi per uno o più degli altri inquinanti e 
confronti lo spettro di potenza dei diversi inquinanti
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants, fft, optimize

#leggo il file
tab = pd.read_csv('copernicus_PG_selected.csv')

#print(tab.size)
#print(tab.columns)

date = (tab['date'].values) - 58112.0
co = tab['mean_co_ug/m3'].values
nh3 = tab['mean_nh3_ug/m3'].values
no2 = tab['mean_no2_ug/m3'].values
o3 = tab['mean_o3_ug/m3'].values
pm10 = tab['mean_pm10_ug/m3'].values
pm2p5 = tab['mean_pm2p5_ug/m3'].values
so2 = tab['mean_so2_ug/m3']

#grafico inquinanti

fig,ax = plt.subplots(7,1, figsize=(40,40))
ax[0].plot(date, co, color='forestgreen')
ax[1].plot(date, nh3, color='limegreen')
ax[2].plot(date, no2, color='darkseagreen')
ax[3].plot(date, o3, color='yellowgreen')
ax[4].plot(date, pm10, color='greenyellow')
ax[5].plot(date, pm2p5, color='springgreen')
ax[6].plot(date, so2, color='mediumseagreen')

ax[0].set_title('CO', loc='left', y=0.75, x=0.02)
ax[1].set_title('NH3', loc='left', y=0.75, x=0.02)
ax[2].set_title('NO2', loc='left', y=0.75, x=0.02)
ax[3].set_title('O3', loc='left', y=0.75, x=0.02)
ax[4].set_title('PM10', loc='left', y=0.75, x=0.02)
ax[5].set_title('PM2P5', loc='left', y=0.75, x=0.02)
ax[6].set_title('SO2', loc='left', y=0.75, x=0.02)

fig.suptitle('media della densità di inquinanti atmosferici [$\mu g/m^3$] al giorno [d]')

plt.show()

#analizzo i dati del monossido di carbonio (CO)

#trasformata di fourier della serie temporale
trasfco = fft.rfft(co)
#spettro di potenza
spco = np.absolute(trasfco)**2
#freqenza
a = 0.5
freqco = a*fft.rfftfreq(trasfco.size, d=1)

#grafico spettro di potenza in funzione della frequenza
plt.plot(freqco[:trasfco.size//2], np.absolute(trasfco[:trasfco.size//2])**2, 'o', markersize=4, color='rebeccapurple')
plt.xlabel(r'f [$d^{-1}$]', fontsize=14)
plt.ylabel(r'$|c_{FFT}|^2$ [$\mu g^2/m^6$]', fontsize=14)
plt.yscale('log')
plt.xscale('log')
plt.title('spettro di potenza su frequenza CO')
plt.show()

#periodicità
#massimo dello spettro di potenza
maxco = np.argmax(spco[1:trasfco.size//2])+1
print('Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( spco[maxco], freqco[maxco], int(1/freqco[maxco])))

#grafico spettro di potenza in funzione del periodo
plt.title('spettro di potenza su periodo CO')
plt.plot(1/freqco[1:trasfco.size//2], spco[1:trasfco.size//2], color='plum')
plt.plot(1/freqco[maxco], spco[maxco], 'o', color='magenta')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'T [$d$]',                       fontsize=14)
plt.ylabel(r'$|c_{FFT}|^2$ [$\mu g^2/m^6$]', fontsize=14)
plt.show()

#filtro ai coefficienti di fourier selezionando solo le componenti che descrivono l'andamento generale in funzione del tempo (escludendo futtuazioni di breve periodo)

trasfmask1 = spco< 5e7
trasfmask2 = spco< 7e6

filtered_trasfco1 = trasfco.copy()
filtered_trasfco1[trasfmask1] = 0
filtered_trasfco2 = trasfco.copy()
filtered_trasfco2[trasfmask2] = 0

# Trasformata FFT inversa con coeff filtrati 
filtered_co1 = fft.irfft(filtered_trasfco1, n=len(co))
filtered_co2 = fft.irfft(filtered_trasfco2, n=len(co))

#grafico di confronto tra segnale originale e il segnale filtrato
plt.subplots(figsize=(11,7))
plt.plot(date, co, color='paleturquoise',      label='Dati Originali')
plt.plot(date, filtered_co2,     color='steelblue', label='Filtro $coeff>7\cdot 10^6$')
plt.plot(date, filtered_co1,     color='cadetblue',   label='Filtro $coeff>5\cdot 10^7$')
plt.legend(fontsize=13)
plt.xlabel('Giorni')
plt.ylabel('Densità CO nell\'aria [$\mu g^2/m^6$]')
plt.title('Segnali originale e filtrati sulla densità di CO', fontsize = 12)
plt.show()
