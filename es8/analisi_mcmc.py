'''
Scivere un script python che esegua l'analisi MCMC dei dati forniti.
Assicurarsi di eseguire i seguenti passi:
-Leggere i dati e farne il grafico
-Definire una funzione per il modello teorico f(E)

SUGGERIMENTO: fare in modo che tutti i parametri liberi vengano passati
come lista o ntupla
SUGGERIMENTO: confrontarei dati con la funzone teorica attraverso una 
valutazione approssimativa dei parametri

-Definire la funzione di loglikelihhod
-Definire la funzione con il logaritmo della distribuzione prior
-Definire la funzione di probabilità logaritimica

SUGGERIMENTO: logprob=logprior+loglikelihhod

-Definire il numero di walker
-Definire la posizione di partena per tutti i walker
-Definire un emcee.EnsembleSampler
-Dopo aver fatto girare il sampler produrre il grafico dei 
parametri in funzone dei passi
-Escludere i passi che risentono della scelta dei parametri iniziali
-Confrontare graficamente i dati con alcuni modelli teorici 
presi dalla distribuzione posterior dei parametri
-Produrre un corner plot
'''
import pandas as pd
import numpy as np
import emcee
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy import stats
import corner

#definisco la funzione per il modello teorico
def flusso(p, E):
    m, b, alpha, mu, sigma = p
    return m*E + b + alpha*np.exp(-((E-mu)**2)/(2*sigma**2))

#definisco la funzione loglikelihhod
def lnlike_fl(p, E, f, ferr):
    return -0.5 * np.sum(((fl - flusso(p, E))/err_fl) ** 2)

#definisco la funzione con il log della distribuzione prior
def lnprior_fl(p):
    m, b, alpha, mu, sigma = p
    if ( -2<m<0 and  5<b<15 and -10<alpha<0 and 0<mu<10 and 0<sigma<5 ):
        return 0.0
    return -np.inf

#definisco la funzione di probabilità logaritmica
def lnprob_fl(p, E, f, ferr):
    lp = lnprior_fl(p)
    if np.isfinite(lp):
        return lp + lnlike_fl(p, E, f, ferr) 
    return -np.inf

#leggo i dati e faccio il grafico
dati = pd.read_csv('absorption_line.csv')
#print(dati)

en = dati['E'].values                    
fl = dati['f'].values
err_fl = dati['ferr'].values

par = np.array([-0.1, 9, -6, 5, 1])
mod_fl = flusso(par, en)
'''
plt.errorbar(en, fl, err_fl, color='rebeccapurple')
plt.plot(en, mod_fl, color='teal')
plt.xlabel('Energia')
plt.ylabel('Flusso')
plt.show()
'''
#definisco il numero di walker
nw = 32

#definisco la posizione di partenza per tutti i walker
initial_fl = par
ndim_fl = len(initial_fl)
p0 = np.array(initial_fl)  +0.1*np.random.randn(nw, ndim_fl) 

#definisco il sampler di emcee
sampler_fl = emcee.EnsembleSampler(nw, ndim_fl, lnprob_fl, args=(en, fl, err_fl))

print('Running production... ')
sampler_fl.run_mcmc(p0, 1000, progress=True)

#grafico parametri per numero dei passi
fig, axes = plt.subplots(ndim_fl, figsize=(10, 9), sharex=True)
samples_fl = sampler_fl.get_chain()
labels = [r'm', r'b', r'$\alpha$', r'$\mu$', r'$\sigma$' ]
for i in range(ndim_fl):
    ax = axes[i]
    ax.plot(samples_fl[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(samples_fl))
    ax.set_ylabel(labels[i])
    ax.yaxis.set_label_coords(-0.1, 0.5)
axes[-1].set_xlabel("numero passi");
plt.show()

# Grafico dati con alcuni campionamenti dei paramtri
plt.errorbar(en, fl, yerr=err_fl, fmt="ok", capsize=0)
plt.xlabel('energia')
plt.ylabel('flusso')

#grafico 50 campionamenti posterior.
samples_fl = sampler_fl.flatchain
for s in samples_fl[np.random.randint(len(samples_fl), size=50)]:
    plt.plot(en, flusso(s, en), color="orange", alpha=0.3)

plt.show()

#escludo i passi che risentono dei parametri iniziali (200 passi)
flat_samples_fl = sampler_fl.get_chain(discard=200, thin=15, flat=True)
print(samples_fl.shape)

# Grafico dei dati e dei campionamenti escludendo i primi 200 passi
plt.errorbar(en, fl, yerr=err_fl, fmt="ok", capsize=0)
plt.xlabel('energia')
plt.ylabel('flusso')

# Plot 50 posterior samples.
for s in flat_samples_fl[np.random.randint( len(flat_samples_fl), size=50)]:
    plt.plot(en, flusso(s, en), color="orange", alpha=0.3)

plt.show()

#corner plot
fig = corner.corner( flat_samples_fl, labels=labels, show_titles=True, color='orange');
plt.show()
