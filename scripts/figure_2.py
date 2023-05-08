"""
Script to generate Figure 1 of the paper.

Giovanni Picogna, 08.05.2023
"""
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy import interpolate as interpolate
import seaborn as sns
import pandas as pd
from scipy import stats

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

ONC025_Lx, ONC025_cdf = np.loadtxt(data_path+'LxfuncONC025.dat',
                                   unpack=True, comments='#')
inv_cdf_ONC025 = interpolate.interp1d(ONC025_cdf, ONC025_Lx)

ONC05_Lx, ONC05_cdf = np.loadtxt(data_path+'LxfuncONC05.dat',
                                 unpack=True, comments='#')
inv_cdf_ONC05 = interpolate.interp1d(ONC05_cdf, ONC05_Lx)

ONC1_Lx, ONC1_cdf = np.loadtxt(data_path+'LxfuncONC1.dat',
                               unpack=True, comments='#')
inv_cdf_ONC1 = interpolate.interp1d(ONC1_cdf, ONC1_Lx)

bins_Lx = np.linspace(27, 32, num=1000)

sample = np.array(['COUP $M \\leq 0.25 M_\\odot$'] * np.size(bins_Lx))
kde_ONC025 = stats.gaussian_kde(inv_cdf_ONC025(ONC025_cdf), bw_method='scott')
data_025 = pd.DataFrame(
    {
        "$\\log_{10}(L_X[erg\\, s^{-1}])$": bins_Lx,
        "Probability density": kde_ONC025.evaluate(bins_Lx),
        "sample": sample
    }
)

sample = np.array(['COUP $0.25 < M \\leq 0.5 M_\\odot$'] * np.size(bins_Lx))
kde_ONC05 = stats.gaussian_kde(inv_cdf_ONC05(ONC05_cdf), bw_method='scott')
data_05 = pd.DataFrame(
    {
        "$\\log_{10}(L_X[erg \\, s^{-1}])$": bins_Lx,
        "Probability density": kde_ONC05.evaluate(bins_Lx),
        "sample": sample
    }
)

sample = np.array(['COUP $0.5 < M \\leq 1 M_\\odot$'] * np.size(bins_Lx))
kde_ONC1 = stats.gaussian_kde(inv_cdf_ONC1(ONC1_cdf), bw_method='scott')
data_1 = pd.DataFrame(
    {
        "$\\log_{10}(L_X[erg \\, s^{-1}])$": bins_Lx,
        "Probability density": kde_ONC1.evaluate(bins_Lx),
        "sample": sample
    }
)

data_XLF = pd.concat([data_025, data_05, data_1])

sns.lineplot(data_XLF, x="$\\log_{10}(L_X[erg\\, s^{-1}])$", 
             y="Probability density", hue="sample")
plt.vlines(np.mean(inv_cdf_ONC025(ONC025_cdf)), 0., 0.44, ls='--',
           color=sns.color_palette("pastel")[0], alpha=0.5)
plt.vlines(np.mean(inv_cdf_ONC05(ONC05_cdf)), 0., 0.52, ls='--',
           color=sns.color_palette("pastel")[1], alpha=0.5)
plt.vlines(np.mean(inv_cdf_ONC1(ONC1_cdf)), 0., 0.7, ls='--',
           color=sns.color_palette("pastel")[2], alpha=0.5)
plt.ylim(0, 0.8)
plt.xlim(27, 32)

fig.savefig(fig_path+"Fig2.png", format='png', dpi=400)
