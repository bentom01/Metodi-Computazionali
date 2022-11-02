'''creare un secondo script python che:
definisca una funzione lognormale da usare per il fit dei dati;
legga il file di dati fit_data.csv;
esegua il fit dei dati con la funzione lognormale;
produca il grafico della funzione di fit ottimizzata sovrapposta ai dati;
stampi il valore dei parametri del fit e del chi quadrato;

SUGGERIMENTO: esplorare la possibilità di mostrare uno o entrambi gli assi 
dei grafici in maniera logaritmica.'''

#funzione lognormale = gaussiana nel log(x)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt

tab = pd.read_csv('fit_data.csv')
#print(tab)

ax = np.array(tab['x'])
ay = np.array(tab['y'])
erry = np.array(np.sqrt(ay))

def lognorm(x, A, s, m):
    return A*np.exp(-0.5*((np.log(x)-m)/s)**2)

pstart = np.array([100, 2, 5])

params, params_covariance = opt.curve_fit(lognorm, ax, ay, p0=[pstart])
err_params = np.sqrt(params_covariance.diagonal())

paramse, paramse_covariance = opt.curve_fit(lognorm, ax, ay, sigma=erry,
                                          absolute_sigma='True', p0=[pstart])
err_paramse = np.sqrt(paramse_covariance.diagonal())

y1 = lognorm(ax, params[0], params[1], params[2])

y2 = lognorm(ax, paramse[0], paramse[1], paramse[2])

plt.errorbar(ax, ay, erry, fmt='o', color='salmon', label='dati')
plt.plot(ax, y1 , color='lightseagreen', label='fit senza sigma')
plt.plot(ax, y2 , color='mediumpurple', label='fit con sigma')

plt.legend()
plt.xscale('log')
plt.show()

print('params senza sigma', params )
print('params_cov senza sigma', params_covariance)
print('errori params senza sigma', err_params)

print('paramse con sigma', paramse )
print('paramse_cov con sigma', paramse_covariance)
print('errori paramse con sigma', err_paramse)

chi2_1 = np.sum( (y1 - ay)**2 /ay )
chi2_2 = np.sum( (y2 - ay)**2 /ay )

ngl_1 = len(ax) - len(params)
ngl_2 = len(ax) - len(paramse)

print('chi quadro senza sigma: ', chi2_1)
print('chi quadro con sigma: ', chi2_2)

chi_rid_1 = chi2_1/ngl_1
chi_rid_2 = chi2_2/ngl_2

print('chi quadro ridotto senza sigma: ', chi_rid_1)
print('chi quadro ridotto con sigma: ', chi_rid_2)
