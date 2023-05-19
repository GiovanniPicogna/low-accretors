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
from lib import load_data

plt.style.use('science')
sns.set_palette("pastel")

plt.rc('font', size=8.)
plt.rc('xtick', labelsize=8.)
plt.rc('ytick', labelsize=8.)
plt.rc('axes', labelsize=8.)
plt.rc('legend', fontsize=4.5)

plt.rcParams["errorbar.capsize"]

fig, ax = plt.subplots(2, 4, sharex=True, sharey=True, figsize=[7.03058, 4])
fig.subplots_adjust(right=0.96, hspace=0.075, wspace=0.075, left=0.15)
cbar_ax = fig.add_axes([0.97, 0.15, 0.015, 0.7])

data_path = "../data/"
fig_path = "../figures/"

mask = False
mask_val = 1.e-13

path = data_path+'pop_EUV/'
profile_name = "Full sample"
data_euv = load_data(path, profile_name=profile_name, mask=mask, 
                     mask_val=mask_val)

path = data_path+'pop_EUV/03Msun/'
profile_name_03 = "$M_\\star \\leq 0.3 M_\\odot$"
data_euv_03 = load_data(path, profile_name=profile_name_03, mask=mask,
                        mask_val=mask_val)

path = data_path+'pop_EUV/06Msun/'
profile_name_06 = "$0.3 < M_\\star \\leq 0.6 M_\\odot$"
data_euv_06 = load_data(path, profile_name=profile_name_06, mask=mask,
                        mask_val=mask_val)

path = data_path+'pop_EUV/1Msun/'
profile_name_1 = "$0.6 < M_\\star \\leq M_\\odot$"
data_euv_1 = load_data(path, profile_name=profile_name_1, mask=mask,
                       mask_val=mask_val)

path = data_path+'pop_XEUV/'
data_xeuv = load_data(path, profile_name=profile_name, mask=mask,
                      mask_val=mask_val)

path = data_path+'pop_XEUV/03Msun/'
data_xeuv_03 = load_data(path, profile_name=profile_name_03, mask=mask,
                         mask_val=mask_val)

path = data_path+'pop_XEUV/06Msun/'
data_xeuv_06 = load_data(path, profile_name=profile_name_06, mask=mask,
                         mask_val=mask_val)

path = data_path+'pop_XEUV/1Msun/'
data_xeuv_1 = load_data(path, profile_name=profile_name_1, mask=mask,
                        mask_val=mask_val)

low_acc_data = pd.read_csv(data_path+'low_accretors.dat', sep=' ')
low_acc_data["Mdot"] *= 1.e-10
low_acc_data["dMdot"] *= 1.e-10
low_acc_data_03 = low_acc_data[low_acc_data["M$_\star$"] <= 0.3]
low_acc_data_06 = low_acc_data[low_acc_data["M$_\star$"] > 0.3]
low_acc_data_06 = low_acc_data_06[low_acc_data_06["M$_\star$"] <= 0.6]
low_acc_data_1 = low_acc_data[low_acc_data["M$_\star$"] > 0.6]

z = sns.histplot(data=data_euv, x="age", y="mdot_acc",
                 binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                 cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                 vmin=None, vmax=None, log_scale=(False, True),
                 cbar_kws={'label': 'density'}, kde=True, ax=ax[0][0])
ax[0][0].errorbar(x=low_acc_data["t"], y=low_acc_data["Mdot"],
                  xerr=low_acc_data["dt"], yerr=low_acc_data["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[0][0], zorder=5)
ax[0][0].set_yscale('log')
ax[0][0].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[0][0].set_ylabel("EUV\n$\\log_{10}(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)")
ax[0][0].set_xlim(0., 20.)
ax[0][0].set_ylim(1e-12, 1e-7)
ax[0][0].set_title("Full sample")

z1 = sns.histplot(data=data_euv_03, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'}, kde=True, ax=ax[0][1])
ax[0][1].errorbar(x=low_acc_data_03["t"], y=low_acc_data_03["Mdot"],
                  xerr=low_acc_data_03["dt"], yerr=low_acc_data_03["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data_03, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[0][1], zorder=5)
ax[0][1].set_yscale('log')
ax[0][1].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[0][1].set_xlim(0., 20.)
ax[0][1].set_ylim(1e-12, 1e-7)
ax[0][1].set_title("$M_\\star \\leq 0.3 M_\\odot$")

z2 = sns.histplot(data=data_euv_06, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'}, kde=True, ax=ax[0][2])
ax[0][2].errorbar(x=low_acc_data_06["t"], y=low_acc_data_06["Mdot"],
                  xerr=low_acc_data_06["dt"], yerr=low_acc_data_06["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data_06, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[0][2], zorder=5)
ax[0][2].set_yscale('log')
ax[0][2].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[0][2].set_xlim(0., 20.)
ax[0][2].set_ylim(1e-12, 1e-7)
ax[0][2].set_title("$0.3 < M_\\star \\leq 0.6 M_\\odot$")

z3 = sns.histplot(data=data_euv_1, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'}, kde=True, ax=ax[0][3])
ax[0][3].errorbar(x=low_acc_data_1["t"], y=low_acc_data_1["Mdot"],
                  xerr=low_acc_data_1["dt"], yerr=low_acc_data_1["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data_1, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[0][3], zorder=5)
ax[0][3].set_yscale('log')
ax[0][3].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[0][3].set_xlim(0., 20.)
ax[0][3].set_ylim(1e-12, 1e-7)
ax[0][3].set_title("$0.6 < M_\\star \\leq 1 M_\\odot$")

z4 = sns.histplot(data=data_xeuv, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=True, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'}, cbar_ax=cbar_ax,
                  kde=True, ax=ax[1][0])
ax[1][0].set_yscale('log')
ax[1][0].errorbar(x=low_acc_data["t"], y=low_acc_data["Mdot"],
                  xerr=low_acc_data["dt"], yerr=low_acc_data["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[1][0], zorder=5)
ax[1][0].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[1][0].set_ylabel("XEUV\n$\\log_{10}(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)")
ax[1][0].set_xlabel('age / Myr')
ax[1][0].set_xlim(0., 20.)
ax[1][0].set_ylim(1e-12, 1e-7)

z5 = sns.histplot(data=data_xeuv_03, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'},
                  kde=True, ax=ax[1][1])
ax[1][1].set_yscale('log')
ax[1][1].errorbar(x=low_acc_data_03["t"], y=low_acc_data_03["Mdot"],
                  xerr=low_acc_data_03["dt"], yerr=low_acc_data_03["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data_03, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[1][1], zorder=5)
ax[1][1].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[1][1].set_xlabel('age / Myr')
ax[1][1].set_xlim(0., 20.)
ax[1][1].set_ylim(1e-12, 1e-7)

z6 = sns.histplot(data=data_xeuv_06, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'},
                  kde=True, ax=ax[1][2])
ax[1][2].set_yscale('log')
ax[1][2].errorbar(x=low_acc_data_06["t"], y=low_acc_data_06["Mdot"],
                  xerr=low_acc_data_06["dt"], yerr=low_acc_data_06["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data_06, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[1][2], zorder=5)
ax[1][2].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[1][2].set_xlabel('age / Myr')
ax[1][2].set_xlim(0., 20.)
ax[1][2].set_ylim(1e-12, 1e-7)

z7 = sns.histplot(data=data_xeuv_1, x="age", y="mdot_acc",
                  binwidth=(0.1*20./6., 0.1), cbar=False, stat='density',
                  cmap='turbo', norm=LogNorm(vmin=1.e-4, vmax=1.e-1),
                  vmin=None, vmax=None, log_scale=(False, True),
                  cbar_kws={'label': 'density'},
                  kde=True, ax=ax[1][3])
ax[1][3].set_yscale('log')
ax[1][3].errorbar(x=low_acc_data_1["t"], y=low_acc_data_1["Mdot"],
                  xerr=low_acc_data_1["dt"], yerr=low_acc_data_1["dMdot"],
                  fmt='none', barsabove=False, color='black', alpha=0.5)
sns.scatterplot(data=low_acc_data_1, x="t", y="Mdot", hue="M$_\star$",
                size="M$_\star$", sizes=(2, 20), legend='auto',
                ax=ax[1][3], zorder=5)
ax[1][3].hlines(1.e-11, 0, 20, 'k', ls='--')
ax[1][3].set_xlabel('age / Myr')
ax[1][3].set_xlim(0., 20.)
ax[1][3].set_ylim(1e-12, 1e-7)

fig.savefig(fig_path+'Fig61.png', format='png', dpi=400)
