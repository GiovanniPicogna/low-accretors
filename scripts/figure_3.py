"""
Script to generate Figure 1 of the paper.

Giovanni Picogna, 08.05.2023
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from astropy import constants as const
from scipy import interpolate as interpolate
import seaborn as sns
from lib import IMF

plt.style.use('science')
sns.set_palette("pastel")

plt.rc('font', size=18.)
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=18.)
plt.rc('ytick', labelsize=18.)
plt.rc('axes', labelsize=18.)
plt.rc('lines', linewidth=3.)

plt.rcParams["errorbar.capsize"]

fig = plt.figure(figsize=[8.5, 8.5])

data_path = "../data/"
fig_path = "../figures/"

Lx_func_025 = data_path+'LxfuncONC025.dat'
Lx_func_05 = data_path+'LxfuncONC05.dat'
Lx_func_1 = data_path+'LxfuncONC1.dat'

# cumulative density function of Guedel+2007 (which is the inverted Kaplan-Maier-estimator)
lxs025, cdf025 = np.loadtxt(Lx_func_025, unpack=True, comments='#')
lxs05, cdf05 = np.loadtxt(Lx_func_05, unpack=True, comments='#')
lxs1, cdf1 = np.loadtxt(Lx_func_1, unpack=True, comments='#')

mass_ini = 0.1
mass_end = 1.1
mass_bins = 10000

masses = np.linspace(mass_ini, mass_end, mass_bins)
IMF_Kroupa = IMF(masses, profile="Kroupa")
weights = IMF_Kroupa[:, 1]

Lx_PE = []

for j in range(10000):
    Mstar = np.random.choice(masses, size=1, p=weights/np.sum(weights), replace=True)[0]
    if Mstar <= 0.25:
        lxs_rescaled = lxs025 + np.log10((Mstar/0.16)**1.54)
        inv_cdf025 = interpolate.interp1d(cdf025, lxs_rescaled, fill_value="extrapolate")
        lx = inv_cdf025(np.random.random())
    elif Mstar <= 0.5:
        lxs_rescaled = lxs05 + np.log10((Mstar/0.36)**1.54)
        inv_cdf05 = interpolate.interp1d(cdf05, lxs_rescaled, fill_value="extrapolate")
        lx = inv_cdf05(np.random.random())
    else:
        lxs_rescaled = lxs1 + np.log10((Mstar/0.7)**1.54)
        inv_cdf1 = interpolate.interp1d(cdf1, lxs_rescaled, fill_value="extrapolate")
        lx = inv_cdf1(np.random.random())
    Lx_PE.append(lx)

Lx_PE = np.array(Lx_PE)

sns.histplot(x=Lx_PE, binwidth=0.25, stat='density', kde=True)

plt.xlabel(r'$\\log_{10}(L_X / erg\, s^{-1})$')
plt.ylabel('density')

plt.vlines(np.median(Lx_PE), 0, 0.44, ls='-.', color='r')

fig.savefig(fig_path+'Fig3.png', format='png', dpi=400)
