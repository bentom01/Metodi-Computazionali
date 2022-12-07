'''
Creare uno script python che esegua le seguenti operazioni:
-Legga uno o più file di input
-Produca un istogramma dei tempi per uno dei moduli (file)
-Produca un istogramma delle differenze di tempi (delta_t) fra Hit 
consecutivi per uno dei moduli
--SUGGERIMENTO: usare il log_10(delta_t)
--Interpretare il grafico risultante
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#leggo i file
m0 = pd.read_csv('hit_times_M0.csv')
m1 = pd.read_csv('hit_times_M1.csv')
m2 = pd.read_csv('hit_times_M2.csv')
m3 = pd.read_csv('hit_times_M3.csv')
'''
print(m0)
print(m1)
print(m2)
print(m3)
'''
det0=m0['det_id'].values
hit0=m0['hit_time'].values
det1=m1['det_id'].values
hit1=m1['hit_time'].values
det2=m2['det_id'].values
hit2=m2['hit_time'].values
det3=m3['det_id'].values
hit3=m3['hit_time'].values

#istogramma dei tempi per uno dei moduli
plt.hist(hit0, bins=50, alpha=0.8, color='mediumpurple', ec='rebeccapurple')
plt.show()

#istogramma della differenza dei tempi
diff0=np.diff(hit0)
diff1=np.diff(hit1)
diff2=np.diff(hit2)
diff3=np.diff(hit3)
plt.hist(diff0, bins=50, alpha=0.8, color='paleturquoise', ec='darkcyan')
plt.show()

#applico il log10(delta_t)
mask = diff0 > 0
log0 = np.log10(diff0[mask])
plt.hist(log0, bins=50, alpha=0.8, color='paleturquoise', ec='darkcyan')
plt.show()

'''
interpreto il grafico:
picco iniziale: eventi che sono pate dello stesso evento
secondo picco: generato da un altro evento
'''
