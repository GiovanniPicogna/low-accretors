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
import pandas as pd
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

fig, ax = plt.subplots(2, 1, sharex=True, squeeze=True, figsize=[8.5, 17.])

data_path = "../data/"
fig_path = "../figures/"

data_Mamajek = np.genfromtxt(data_path+'disc_fraction_Mamajek2009.csv', delimiter=',')

# reading XEUV
path = data_path+'pop_XEUV/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["XEUV"] * np.size(arr_stacked[:,1]))

data_xeuv = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_xeuv = mask_accretion(data_xeuv, 1.e-13)
data_xeuv_masked = mask_accretion(data_xeuv, 1.e-11)

# reading EUV 0.3 pop-synth
path = data_path+'pop_EUV/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["EUV"] * np.size(arr_stacked[:,1]))

data_euv = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_euv = mask_accretion(data_euv, 1.e-13)
data_euv_masked = mask_accretion(data_euv, 1.e-11)


# reading XEUV 0.3 pop-synth
path = data_path+'pop_XEUV/03Msun/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["XEUV $M_\star \leq 0.3 M_\odot$"] * np.size(arr_stacked[:,1]))

data_xeuv_03Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_xeuv_03Msun = mask_accretion(data_xeuv_03Msun, 1.e-13)
data_xeuv_03Msun_masked = mask_accretion(data_xeuv_03Msun, 1.e-11)

# reading EUV 0.3 pop-synth
path = data_path+'pop_EUV/03Msun/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["EUV $M_\star \leq 0.3 M_\odot$"] * np.size(arr_stacked[:,1]))

data_euv_03Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_euv_03Msun = mask_accretion(data_euv_03Msun, 1.e-13)
data_euv_03Msun_masked = mask_accretion(data_euv_03Msun, 1.e-11)

# reading XEUV 0.6 pop-synth
path = data_path+'pop_XEUV/06Msun/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["XEUV $0.3 < M_\star \leq 0.6 M_\odot$"] * np.size(arr_stacked[:,1]))

data_xeuv_06Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_xeuv_06Msun = mask_accretion(data_xeuv_06Msun, 1.e-13)
data_xeuv_06Msun_masked = mask_accretion(data_xeuv_06Msun, 1.e-11)

# reading EUV 0.6 pop-synth
path = data_path+'pop_EUV/06Msun/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["EUV $0.3 < M_\star \leq 0.6 M_\odot$"] * np.size(arr_stacked[:,1]))

data_euv_06Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_euv_06Msun = mask_accretion(data_euv_06Msun, 1.e-13)
data_euv_06Msun_masked = mask_accretion(data_euv_06Msun, 1.e-11)

# reading XEUV 1 pop-synth
path = data_path+'pop_XEUV/1Msun/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["XEUV $0.6 < M_\star \leq M_\odot$"] * np.size(arr_stacked[:,1]))

data_xeuv_1Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_xeuv_1Msun = mask_accretion(data_xeuv_1Msun, 1.e-13)
data_xeuv_1Msun_masked = mask_accretion(data_xeuv_1Msun, 1.e-11)

# reading EUV 1 pop-synth
path = data_path+'pop_EUV/1Msun/'

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")
disk_frac = np.loadtxt(path+"frac.dat")

arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

age = arr_stacked[:, 0]
frac = arr_stacked[:, 1]*0.86
mdot_acc = arr_stacked[:, 2]

profile = np.array(["EUV $0.6 < M_\star \leq M_\odot$"] * np.size(arr_stacked[:,1]))

data_euv_1Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "disk_fraction": frac,
        "age": age,
        "profile": profile
    }
)

data_euv_1Msun = mask_accretion(data_euv_1Msun, 1.e-13)
data_euv_1Msun_masked = mask_accretion(data_euv_1Msun, 1.e-11)

ax[0].plot(data_xeuv_masked["age"], data_xeuv_masked["disk_fraction"], '.', color='black', label=r'XEUV')
ax[0].plot(data_xeuv_03Msun_masked["age"], data_xeuv_03Msun_masked["disk_fraction"], '.', label=r'XEUV $M_\star \leq 0.3 M_\odot$')
ax[0].plot(data_xeuv_06Msun_masked["age"], data_xeuv_06Msun_masked["disk_fraction"], '.', label=r'XEUV $0.3 M_\odot < M_\star \leq 0.6 M_\odot$')
ax[0].plot(data_xeuv_1Msun_masked["age"], data_xeuv_1Msun_masked["disk_fraction"], '.', label=r'XEUV $M_\star > 0.6 M_\odot$')

ax[0].errorbar(data_Mamajek[:,1], data_Mamajek[:,4], 
               xerr=[data_Mamajek[:,1]-data_Mamajek[:,2], data_Mamajek[:,3]-data_Mamajek[:,1]], 
               yerr=[data_Mamajek[:,4]-data_Mamajek[:,5], data_Mamajek[:,6]-data_Mamajek[:,4]], 
               fmt='o', markersize=5, color='black', ecolor='darkgrey', markeredgewidth=0, elinewidth=1, 
               capsize=0, alpha=0.9, zorder=2, label='Mamajek+2009')

#ax[0].vlines(np.median(data_xeuv_masked["age"]),0,80,alpha=0.5,color='black',ls='--')
ax[0].vlines(np.median(data_xeuv_03Msun_masked["age"]),0,80,alpha=0.5,color=sns.color_palette("pastel")[0],ls='--')
ax[0].vlines(np.median(data_xeuv_06Msun_masked["age"]),0,80,alpha=0.5,color=sns.color_palette("pastel")[1],ls='--')
ax[0].vlines(np.median(data_xeuv_1Msun_masked["age"]),0,80,alpha=0.5,color=sns.color_palette("pastel")[2],ls='--')

ax[0].legend(loc='upper right')
ax[0].set_ylabel(r'disk fraction / \%')

ax[0].set_xlim(0., 20.)
ax[0].set_ylim(0, 90.)

ax[1].plot(data_euv_masked["age"], data_euv_masked["disk_fraction"], '.', color='black', label=r'EUV')
ax[1].plot(data_euv_03Msun_masked["age"], data_euv_03Msun_masked["disk_fraction"], '.', label=r'EUV $M_\star \leq 0.3 M_\odot$')
ax[1].plot(data_euv_06Msun_masked["age"], data_euv_06Msun_masked["disk_fraction"], '.', label=r'EUV $0.3 M_\odot < M_\star \leq 0.6 M_\odot$')
ax[1].plot(data_euv_1Msun_masked["age"], data_euv_1Msun_masked["disk_fraction"], '.', label=r'EUV $M_\star > 0.6 M_\odot$')

ax[1].errorbar(data_Mamajek[:,1], data_Mamajek[:,4], 
             xerr=[data_Mamajek[:,1]-data_Mamajek[:,2], data_Mamajek[:,3]-data_Mamajek[:,1]], 
             yerr=[data_Mamajek[:,4]-data_Mamajek[:,5], data_Mamajek[:,6]-data_Mamajek[:,4]], 
             fmt='o', markersize=5, color='black', ecolor='darkgrey', markeredgewidth=0, elinewidth=1, 
             capsize=0, alpha=0.9, zorder=2, label='Mamajek+2009')

#ax[1].vlines(np.median(data_euv_masked["age"]),0,80,alpha=0.5,color='black',ls='--')
ax[1].vlines(np.median(data_euv_03Msun_masked["age"]),0,80,alpha=0.5,color=sns.color_palette("pastel")[0],ls='--')
ax[1].vlines(np.median(data_euv_06Msun_masked["age"]),0,80,alpha=0.5,color=sns.color_palette("pastel")[1],ls='--')
ax[1].vlines(np.median(data_euv_1Msun_masked["age"]),0,80,alpha=0.5,color=sns.color_palette("pastel")[2],ls='--')

ax[1].legend(loc='upper right')
ax[1].set_ylabel(r'disk fraction / \%')
ax[1].set_xlabel(r'age / Myr')

ax[1].set_xlim(0., 20.)
ax[1].set_ylim(0, 90.)

fig.savefig(fig_path+'Fig8.png', format='png', dpi=400)