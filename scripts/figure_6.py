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
import pandas as pd
from matplotlib.colors import LogNorm
from lib import mask_accretion

plt.style.use('science')
sns.set_palette("pastel")

plt.rc('font', size=18.)
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=18.)
plt.rc('ytick', labelsize=18.)
plt.rc('axes', labelsize=18.)
plt.rc('lines', linewidth=3.)

plt.rcParams["errorbar.capsize"]

fig, ax = plt.subplots(1, 2, sharey=True, squeeze=True, figsize=[17., 8.5])
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.1, 0.03, 0.8])

data_path = "../data/"
fig_path = "../figures/"

path = data_path+"pop_EUV/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["EUV"] * np.size(arr_stacked[:,1]))

data_euv = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_euv = mask_accretion(data_euv, 1.e-12)

path = data_path+"pop_XEUV/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["XEUV"] * np.size(arr_stacked[:,1]))

data_xeuv = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_xeuv = mask_accretion(data_xeuv, 1.e-12)

low_acc_data = pd.read_csv(data_path+'low_accretors.dat', sep=' ')
low_acc_data["Mdot"] *= 1.e-10
low_acc_data["dMdot"] *= 1.e-10

z = sns.histplot(data=data_euv, x="age", y="mdot_acc", binwidth=(0.1*20./6., 0.1), cbar=False, stat='density', 
                 cmap='turbo', norm=LogNorm(vmin=1.e-4,vmax=1.e-1), vmin=None, vmax=None, log_scale=(False,True), 
                 cbar_kws={'label': 'density'}, kde=True, ax=ax[0])
ax[0].errorbar(x=low_acc_data["t"], y=low_acc_data["Mdot"],
               xerr=low_acc_data["dt"], yerr=low_acc_data["dMdot"],
               fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data, x="t", y="Mdot", hue="Mstar", 
                size="Mstar", ax=ax[0], zorder=5)
ax[0].set_yscale('log')
ax[0].hlines(1.e-11, 0, 20, 'k',ls='--')
ax[0].set_ylabel('$\log_{10}(\dot{M}_\mathrm{acc}/M_{\odot}\,\mathrm{yr}^{-1}$)')
ax[0].set_xlabel('age / Myr')
ax[0].set_xlim(0., 20.)
ax[0].set_ylim(1e-12, 1e-7)
ax[0].set_title("EUV")

z1 = sns.histplot(data=data_xeuv, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=True, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'}, cbar_ax=cbar_ax,
                  kde=True, ax=ax[1])
ax[1].set_yscale('log')
ax[1].errorbar(x=low_acc_data["t"], y=low_acc_data["Mdot"],
               xerr=low_acc_data["dt"], yerr=low_acc_data["dMdot"],
               fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data, x="t", y="Mdot", hue="Mstar", 
                size="Mstar", legend=False, ax=ax[1], zorder=5)

ax[1].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[1].set_ylabel('$\log_{10}(\dot{M}_\mathrm{acc}/M_{\odot}\,\mathrm{yr}^{-1}$)')
ax[1].set_xlabel('age / Myr')
ax[1].set_xlim(0., 20.)
ax[1].set_ylim(1e-12, 1e-7)
ax[1].set_title("XEUV")

fig.savefig(fig_path+'Fig6.png', format='png', dpi=400)
