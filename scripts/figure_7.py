"""
Script to generate Figure 7 of the paper.

Giovanni Picogna, 08.05.2023
"""
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
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

fig = plt.figure(figsize=[8.5, 8.5])

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

data_euv = mask_accretion(data_euv, 1.e-13)

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

data_xeuv = mask_accretion(data_xeuv, 1.e-13)

data = pd.concat([data_euv, data_xeuv])
data.reset_index(drop=True, inplace=True)

low_acc_data = pd.read_csv(data_path+'low_accretors.dat', sep=' ')
low_acc_data["Mdot"] *= 1.e-10
low_acc_data["dMdot"] *= 1.e-10

sns.histplot(data, x='mdot_acc', hue="profile", stat='density', log_scale=True,
             bins=30, kde=True)
plt.vlines(np.median(data_euv["mdot_acc"][~np.isnan(data_euv["mdot_acc"])]),
           0, 0.32, ls='-.', color=sns.color_palette("pastel")[0])
plt.vlines(np.median(data_xeuv["mdot_acc"][~np.isnan(data_xeuv["mdot_acc"])]),
           0, 0.32, ls='-.', color=sns.color_palette("pastel")[1])
plt.vlines(np.median(low_acc_data["Mdot"]), 0, 0.32, ls='-.', color='k')
plt.xlabel('$\\log(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)')
plt.xlim(1e-13, 3e-7)

fig.tight_layout()

fig.savefig(fig_path+'Fig7.png', format='png', dpi=400)
