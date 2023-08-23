"""
Script to generate Figure 4 of the paper.

Giovanni Picogna, 10.05.2023
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from astropy import constants as const
from scipy import interpolate as interpolate
import seaborn as sns
from lib import load_data

plt.style.use('science')
sns.set_palette("pastel")

plt.rc('font', size=8.)
plt.rc('xtick', labelsize=8.)
plt.rc('ytick', labelsize=8.)
plt.rc('axes', labelsize=8.)
plt.rc('legend', fontsize=8.)

plt.rcParams["errorbar.capsize"]

fig, ax = plt.subplots(3, 1, sharex=True, figsize=[3.37689, 6.])
fig.subplots_adjust(left=0.15, wspace=0.075, hspace=0.075)

data_path = "../data/"
fig_path = "../figures/"

data_Mamajek = np.genfromtxt(data_path+'disc_fraction_Mamajek2009.csv',
                             delimiter=',')

mask = True
mask_val = 1.e-11

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

path = data_path+'pop_FUV/'
data_fuv = load_data(path, profile_name=profile_name, mask=mask,
                     mask_val=mask_val)

path = data_path+'pop_FUV/03Msun/'
data_fuv_03 = load_data(path, profile_name=profile_name_03, mask=mask,
                         mask_val=mask_val)

path = data_path+'pop_FUV/06Msun/'
data_fuv_06 = load_data(path, profile_name=profile_name_06, mask=mask,
                         mask_val=mask_val)

path = data_path+'pop_FUV/1Msun/'
data_fuv_1 = load_data(path, profile_name=profile_name_1, mask=mask,
                        mask_val=mask_val)

ax[0].plot(data_euv["age"], data_euv["disk_fraction"], '.',
           color='black', markersize=2, label=profile_name)
ax[0].plot(data_euv_03["age"], data_euv_03["disk_fraction"], '.',
           markersize=2, label=profile_name_03)
ax[0].plot(data_euv_06["age"], data_euv_06["disk_fraction"], '.',
           markersize=2, label=profile_name_06)
ax[0].plot(data_euv_1["age"], data_euv_1["disk_fraction"], '.',
           markersize=2, label=profile_name_1)

ax[0].vlines(np.median(data_euv["age"]), 0, 80,
             color='black', ls='--')
ax[0].vlines(np.median(data_euv_03["age"]), 0, 80,
             color=sns.color_palette("pastel")[0], ls='--')
ax[0].vlines(np.median(data_euv_06["age"]), 0, 80,
             color=sns.color_palette("pastel")[1], ls='--')
ax[0].vlines(np.median(data_euv_1["age"]), 0, 80,
             color=sns.color_palette("pastel")[2], ls='--')

ax[1].plot(data_xeuv["age"], data_xeuv["disk_fraction"], '.',
           markersize=2, color='black', label=profile_name)
ax[1].plot(data_xeuv_03["age"], data_xeuv_03["disk_fraction"], '.',
           markersize=2, label=profile_name_03)
ax[1].plot(data_xeuv_06["age"], data_xeuv_06["disk_fraction"], '.',
           markersize=2, label=profile_name_06)
ax[1].plot(data_xeuv_1["age"], data_xeuv_1["disk_fraction"], '.',
           markersize=2, label=profile_name_1)

ax[1].vlines(np.median(data_xeuv["age"]), 0, 80, 
             color='black', ls='--')
ax[1].vlines(np.median(data_xeuv_03["age"]), 0, 80,
             color=sns.color_palette("pastel")[0], ls='--')
ax[1].vlines(np.median(data_xeuv_06["age"]), 0, 80,
             color=sns.color_palette("pastel")[1], ls='--')
ax[1].vlines(np.median(data_xeuv_1["age"]), 0, 80,
             color=sns.color_palette("pastel")[2], ls='--')

ax[2].plot(data_fuv["age"], data_fuv["disk_fraction"], '.',
           markersize=2, color='black', label=profile_name)
ax[2].plot(data_fuv_03["age"], data_fuv_03["disk_fraction"], '.',
           markersize=2, label=profile_name_03)
ax[2].plot(data_fuv_06["age"], data_fuv_06["disk_fraction"], '.',
           markersize=2, label=profile_name_06)
ax[2].plot(data_fuv_1["age"], data_fuv_1["disk_fraction"], '.',
           markersize=2, label=profile_name_1)

ax[2].vlines(np.median(data_fuv["age"]), 0, 80, 
             color='black', ls='--')
ax[2].vlines(np.median(data_fuv_03["age"]), 0, 80,
             color=sns.color_palette("pastel")[0], ls='--')
ax[2].vlines(np.median(data_fuv_06["age"]), 0, 80,
             color=sns.color_palette("pastel")[1], ls='--')
ax[2].vlines(np.median(data_fuv_1["age"]), 0, 80,
             color=sns.color_palette("pastel")[2], ls='--')

for j in range(3):
    ax[j].errorbar(data_Mamajek[:, 1], data_Mamajek[:, 4],
                   xerr=[data_Mamajek[:, 1]-data_Mamajek[:, 2], data_Mamajek[:, 3]-data_Mamajek[:, 1]],
                   yerr=[data_Mamajek[:, 4]-data_Mamajek[:, 5], data_Mamajek[:, 6]-data_Mamajek[:, 4]],
                   fmt='o', markersize=5, color='black', ecolor='darkgrey', markeredgewidth=0, elinewidth=1,
                   capsize=0, alpha=0.9, zorder=2, label='Mamajek+2009')

    ax[j].legend(loc='upper right')
    ax[j].set_xlim(0., 20.)
    ax[j].set_ylim(0, 90.)

ax[0].set_ylabel('EUV\ndisk fraction / \\%')
ax[1].set_ylabel('XEUV\ndisk fraction / \\%')
ax[2].set_ylabel('FUV\ndisk fraction / \\%')
ax[2].set_xlabel(r'age / Myr')

fig.savefig(fig_path+'Fig81.png', format='png', dpi=400)
