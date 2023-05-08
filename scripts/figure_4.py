"""
Script to generate Figure 4 of the paper.

Giovanni Picogna, 08.05.2023
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from astropy import constants as const
from scipy import interpolate as interpolate
import seaborn as sns
from lib import IMF, Phi_Mstar

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

Phi_PE = []

for j in range(10000):
    Mstar = np.random.choice(masses, size=1, p=weights/np.sum(weights), replace=True)[0]
    Phi = np.random.normal(Phi_Mstar(Mstar), 0.25, size=1)
    Phi_PE.append(Phi)

Phi_PE = np.array(Phi_PE)

sns.histplot(x=Phi_PE[:, 0], binwidth=0.2, stat='density', kde=True)

plt.xlabel(r'$\\log_{10}(\Phi_\mathrm{EUV} / s^{-1})$')
plt.ylabel('density')
plt.xlim(39.4, 43)
plt.vlines(np.median(Phi_PE[:, 0]), 0, 0.6, ls='-.', color='r')

fig.savefig(fig_path+'Fig4.png', format='png', dpi=400)
