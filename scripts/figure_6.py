"""
Script to generate Figure 6 of the paper.

Giovanni Picogna, 08.05.2023
"""
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from astropy import constants as const
from scipy import interpolate as interpolate
import seaborn as sns
from matplotlib.colors import LogNorm

plt.style.use('science')
sns.set_palette("pastel")

plt.rc('font', size=18.)
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=18.)
plt.rc('ytick', labelsize=18.)
plt.rc('axes', labelsize=18.)
plt.rc('lines', linewidth=3.)

plt.rcParams["errorbar.capsize"]

fig, ax = plt.subplots(1, 2, sharey=True, figsize=[17., 8.5])

data_path = "../data/"
fig_path = "../figures/"
path = data_path+"pop_EUV/"

r1_arr = np.loadtxt(path+"r1.dat")
md_arr = np.loadtxt(path+"md.dat")
alpha_arr = np.loadtxt(path+"alpha.dat")

sns.kdeplot(x=md_arr, y=alpha_arr, fill=True, common_norm=True,
            log_scale=(False, True), cmap='turbo', cbar=True,
            cbar_kws={'label': 'density', 'orientation': 'horizontal',
                      'ticks': [20, 40, 50]},
            levels=500, ax=ax[0])
sns.kdeplot(x=r1_arr, y=alpha_arr, fill=True, common_norm=True,
            log_scale=(False, True), cmap='turbo', cbar=True,
            cbar_kws={'label': 'density', 'orientation': 'horizontal',
                      'ticks': [0.01, 0.015, 0.017]},
            levels=500, ax=ax[1])

ax[0].set_xlim(0.01, 0.05)
ax[0].set_ylim(1.e-4, 1.e-2)
ax[0].set_xlabel('$M_d$ / $M_\\star$')
ax[0].set_ylabel('$\\log_{10}{(\\alpha)}$')
ax[1].set_xlim(10, 100)
ax[1].set_ylim(1.e-4, 1.e-2)
ax[1].set_xlabel('$R_1$ / au')
fig.tight_layout()
fig.savefig('parameter_space_EUV.png', format='png', dpi=400)

fig.savefig(fig_path+'Fig5.png', format='png', dpi=400)
