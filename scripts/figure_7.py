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

plt.rc('font', size=8.)
plt.rc('xtick', labelsize=8.)
plt.rc('ytick', labelsize=8.)
plt.rc('axes', labelsize=8.)
plt.rc('legend', fontsize=8.)

plt.rcParams["errorbar.capsize"]

fig, ax = plt.subplots(1, 4, figsize=[7.03058, 2.])

data_path = "../data/"
fig_path = "../figures/"

path = data_path+"pop_EUV/"

Macc_arr_euv = np.loadtxt(path+"Macc.dat")
age_arr_euv = np.loadtxt(path+"age.dat")

arr_stacked_euv = np.array([age_arr_euv/1e6, Macc_arr_euv]).T

mdot_acc_euv = arr_stacked_euv[:, 1]
age_euv = arr_stacked_euv[:, 0]

profile_euv = np.array(["EUV"] * np.size(arr_stacked_euv[:, 1]))

data_euv = pd.DataFrame(
    {
        "mdot_acc": mdot_acc_euv,
        "age": age_euv,
        "profile": profile_euv
    }
)

data_euv = mask_accretion(data_euv, 1.e-12)

path = data_path+"pop_XEUV/"

Macc_arr_xeuv = np.loadtxt(path+"Macc.dat")
age_arr_xeuv = np.loadtxt(path+"age.dat")

arr_stacked_xeuv = np.array([age_arr_xeuv/1e6, Macc_arr_xeuv]).T

mdot_acc_xeuv = arr_stacked_xeuv[:, 1]
age_xeuv = arr_stacked_xeuv[:, 0]

profile_xeuv = np.array(["XEUV"] * np.size(arr_stacked_xeuv[:, 1]))

data_xeuv = pd.DataFrame(
    {
        "mdot_acc": mdot_acc_xeuv,
        "age": age_xeuv,
        "profile": profile_xeuv
    }
)

data_xeuv = mask_accretion(data_xeuv, 1.e-12)

path = data_path+"pop_EUV/03Msun/"

Macc_arr_euv03 = np.loadtxt(path+"Macc.dat")
age_arr_euv03 = np.loadtxt(path+"age.dat")

arr_stacked_euv03 = np.array([age_arr_euv03/1e6, Macc_arr_euv03]).T

mdot_acc_euv03 = arr_stacked_euv03[:, 1]
age_euv03 = arr_stacked_euv03[:, 0]

profile_euv03 = np.array(["EUV"] * np.size(arr_stacked_euv03[:, 1]))

data_euv_03Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc_euv03,
        "age": age_euv03,
        "profile": profile_euv03
    }
)

data_euv_03Msun = mask_accretion(data_euv_03Msun, 1.e-12)

path = data_path+"pop_XEUV/03Msun/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["XEUV"] * np.size(arr_stacked[:, 1]))

data_xeuv_03Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_xeuv_03Msun = mask_accretion(data_xeuv_03Msun, 1.e-12)

path = data_path+"pop_EUV/06Msun/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["EUV"] * np.size(arr_stacked[:, 1]))

data_euv_06Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_euv_06Msun = mask_accretion(data_euv_06Msun, 1.e-12)

path = data_path+"pop_XEUV/06Msun/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["XEUV"] * np.size(arr_stacked[:, 1]))

data_xeuv_06Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_xeuv_06Msun = mask_accretion(data_xeuv_06Msun, 1.e-12)

path = data_path+"pop_EUV/1Msun/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["EUV"] * np.size(arr_stacked[:, 1]))

data_euv_1Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_euv_1Msun = mask_accretion(data_euv_1Msun, 1.e-12)

path = data_path+"pop_XEUV/1Msun/"

Macc_arr = np.loadtxt(path+"Macc.dat")
age_arr = np.loadtxt(path+"age.dat")

arr_stacked = np.array([age_arr/1e6, Macc_arr]).T

mdot_acc = arr_stacked[:, 1]
age = arr_stacked[:, 0]

profile = np.array(["XEUV"] * np.size(arr_stacked[:, 1]))

data_xeuv_1Msun = pd.DataFrame(
    {
        "mdot_acc": mdot_acc,
        "age": age,
        "profile": profile
    }
)

data_xeuv_1Msun = mask_accretion(data_xeuv_1Msun, 1.e-12)

data = pd.concat([data_euv, data_xeuv])
data.reset_index(drop=True, inplace=True)
data_03 = pd.concat([data_euv_03Msun, data_xeuv_03Msun])
data_03.reset_index(drop=True, inplace=True)
data_06 = pd.concat([data_euv_06Msun, data_xeuv_06Msun])
data_06.reset_index(drop=True, inplace=True)
data_1 = pd.concat([data_euv_1Msun, data_xeuv_1Msun])
data_1.reset_index(drop=True, inplace=True)

low_acc_data = pd.read_csv(data_path+'low_accretors.dat', sep=' ')
low_acc_data["Mdot"] *= 1.e-10
low_acc_data["dMdot"] *= 1.e-10
low_acc_data_03 = low_acc_data[low_acc_data["M$_\star$"] <= 0.3]
low_acc_data_06 = low_acc_data[low_acc_data["M$_\star$"] > 0.3]
low_acc_data_06 = low_acc_data_06[low_acc_data_06["M$_\star$"] <= 0.6]
low_acc_data_1 = low_acc_data[low_acc_data["M$_\star$"] > 0.6]

sns.histplot(data, x='mdot_acc', hue="profile", stat='density', log_scale=True,
             bins=20, ax=ax[0], kde=True)
ax[0].vlines(np.median(data_euv["mdot_acc"][~np.isnan(data_euv["mdot_acc"])]),
             0, 0.32, ls='-.', color='lightskyblue')
ax[0].vlines(np.median(data_xeuv["mdot_acc"][~np.isnan(data_xeuv["mdot_acc"])]),
             0, 0.32, ls='-.', color='orange')
ax[0].vlines(np.median(low_acc_data["Mdot"]), 0, 0.32, ls='-.', color='k')
ax[0].set_xlabel('$\\log(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)')
ax[0].set_xlim(1e-12, 3e-7)
ax[0].legend(loc='upper right')
ax[0].set_title("Full sample")

sns.histplot(data_03, x='mdot_acc', hue="profile", stat='density', log_scale=True,
             bins=20, ax=ax[1], kde=True)
ax[1].vlines(np.median(data_euv_03Msun["mdot_acc"][~np.isnan(data_euv_03Msun["mdot_acc"])]),
             0, 0.32, ls='-.', color='lightskyblue')
ax[1].vlines(np.median(data_xeuv_03Msun["mdot_acc"][~np.isnan(data_xeuv_03Msun["mdot_acc"])]),
             0, 0.32, ls='-.', color='orange')
ax[1].vlines(np.median(low_acc_data_03["Mdot"]), 0, 0.32, ls='-.', color='k')
ax[1].set_xlabel('$\\log(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)')
ax[1].set_ylabel('')
ax[1].set_xlim(1e-12, 3e-7)
ax[1].legend(loc='upper right')
ax[1].set_title("$M_\\star \\leq 0.3 M_\\odot$")

sns.histplot(data_06, x='mdot_acc', hue="profile", stat='density', log_scale=True,
             bins=20, ax=ax[2], kde=True)
ax[2].vlines(np.median(data_euv_06Msun["mdot_acc"][~np.isnan(data_euv_06Msun["mdot_acc"])]),
             0, 0.5, ls='-.', color='lightskyblue')
ax[2].vlines(np.median(data_xeuv_06Msun["mdot_acc"][~np.isnan(data_xeuv_06Msun["mdot_acc"])]),
             0, 0.5, ls='-.', color='orange')
ax[2].vlines(np.median(low_acc_data_06["Mdot"]), 0, 0.5, ls='-.', color='k')
ax[2].set_xlabel('$\\log(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)')
ax[2].set_ylabel('')
ax[2].set_xlim(1e-12, 3e-7)
ax[2].legend(loc='upper right')
ax[2].set_title("$0.3 < M_\\star \\leq 0.6 M_\\odot$")

sns.histplot(data_1, x='mdot_acc', hue="profile", stat='density', log_scale=True,
             bins=20, ax=ax[3], kde=True)
ax[3].vlines(np.median(data_euv_1Msun["mdot_acc"][~np.isnan(data_euv_1Msun["mdot_acc"])]),
             0, 0.65, ls='-.', color='lightskyblue')
ax[3].vlines(np.median(data_xeuv_1Msun["mdot_acc"][~np.isnan(data_xeuv_1Msun["mdot_acc"])]),
             0, 0.65, ls='-.', color='orange')
ax[3].vlines(np.median(low_acc_data_1["Mdot"]), 0, 0.65, ls='-.', color='k')
ax[3].set_xlabel('$\\log(\\dot{M}_\\mathrm{acc}/M_{\\odot}\\,\\mathrm{yr}^{-1}$)')
ax[3].set_ylabel('')
ax[3].set_xlim(1e-12, 3e-7)
ax[3].legend(loc='upper right')
ax[3].set_title("$0.6 < M_\\star \\leq 1 M_\\odot$")

fig.tight_layout()

fig.savefig(fig_path+'Fig7.png', format='png', dpi=400)
