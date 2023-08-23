"""
Script to generate Figure 1 of the paper.

Giovanni Picogna, 08.05.2023
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy import interpolate as interpolate
import seaborn as sns
import pandas as pd
from lib import Phi_Mstar, IMF

plt.style.use('science')
sns.set_palette("pastel")

plt.rc('font', size=8.)
plt.rc('xtick', labelsize=8.)
plt.rc('ytick', labelsize=8.)
plt.rc('axes', labelsize=8.)
plt.rc('legend', fontsize=4.5)

plt.rcParams["errorbar.capsize"]

fig, ax = plt.subplots(1, 3, figsize=[7.03058, 2.])

data_path = "../data/"
fig_path = "../figures/"

low_acc = pd.read_csv(data_path+'low_accretors.dat', sep=' ', comment="#")
low_acc["Mdot"] *= 1.e-10

data_Mamajek = np.genfromtxt(data_path+'disc_fraction_Mamajek2009.csv', delimiter=',')

f_disc = data_Mamajek[:, 1]/100/0.86  # assume that 14% of discs are formed by binary interactions, see Owen+2011

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

# Calculate all the Mdot_winds for randomly sampled Lx from the XLF
Mstar_PE = []
Phi_PE = []
Lx_PE = []

for j in range(10000):
    Mstar = np.random.choice(masses, size=1, p=weights/np.sum(weights), replace=True)[0]
    if Mstar <= 0.25:
        lxs_rescaled = lxs025 + np.log10((Mstar/0.16)**1.54)
        inv_cdf025 = interpolate.interp1d(cdf025, lxs_rescaled)
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
    Phi = np.random.normal(Phi_Mstar(Mstar), 0.25, size=1)
    Phi_PE.append(Phi)
    Mstar_PE.append(Mstar)

Mstar_PE = np.array(Mstar_PE)
Phi_PE = np.array(Phi_PE)
Lx_PE = np.array(Lx_PE)

sns.histplot(x=Mstar_PE, binwidth=0.0666, stat='density', kde=True, label="population synthesis", ax=ax[0])
sns.histplot(x=low_acc["M$_\star$"], stat='density', binwidth=0.0666, kde=True, label="low accretor sample", ax=ax[0])
# ax[0].plot(IMF_Kroupa[:, 0], IMF_Kroupa[:, 1]/np.max(IMF_Kroupa[:, 1]), 'r--')
ax[0].set_xlabel(r'$M_\star / M_\odot$')
ax[0].set_xlim(0.08, 1.1)
ax[0].set_ylabel('density')
ax[0].legend(loc="upper center")
ax[0].vlines(np.median(Mstar_PE), 0, 2.5, ls='--', lw=2.5, color='lightskyblue')
ax[0].vlines(np.median(low_acc["M$_\star$"]), 0, 2.5, ls='--', lw=2.5, color='orange')
print(np.median(low_acc["M$_\star$"]))
ax[0].text(0.85, 0.95, '(a)', transform=ax[0].transAxes, va='top')

sns.histplot(x=Lx_PE, binwidth=0.25, stat='density', kde=True, ax=ax[1])
ax[1].set_xlabel(r'$\\log_{10}(L_X / erg\, s^{-1})$')
ax[1].set_ylabel('')
ax[1].vlines(np.median(Lx_PE), 0, 0.44, ls='-.', color='r')
ax[1].text(0.85, 0.95, '(b)', transform=ax[1].transAxes, va='top')

sns.histplot(x=Phi_PE[:, 0], binwidth=0.2, stat='density', kde=True, ax=ax[2])
ax[2].set_xlabel(r'$\\log_{10}(\Phi_\mathrm{EUV} / s^{-1})$')
ax[2].set_ylabel('')
ax[2].set_xlim(39.4, 43)
ax[2].vlines(np.median(Phi_PE[:, 0]), 0, 0.6, ls='-.', color='r')
ax[2].text(0.85, 0.95, '(c)', transform=ax[2].transAxes, va='top')

fig.savefig(fig_path+'Fig1.png', format='png', dpi=400)
