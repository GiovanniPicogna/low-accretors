import numpy as np


def Phi_Mstar(Mstar):
    """
    Return the mean ionizing flux for a given stellar mass.

    Adopts the scaling for Lx as a function of Mstar from Güdel et al. (2007)
    """
    return 1.54*np.log10(Mstar) + 42.


def IMF(masses, profile="Kroupa"):
    if profile == "Kroupa":
        IMF = []

        for i in range(len(masses)):
            if masses[i] < 0.5:
                IMF.append([masses[i], masses[i]**(-1.3)])
            elif masses[i] >= 0.5:
                IMF.append([masses[i], masses[i]**(-2.3)])

        IMF = np.array(IMF)
        return IMF
    else:
        print("IMF profile not defined.\n")
    return 0


def mask_accretion(data, value):
    mask = (data["mdot_acc"] > value)
    output = data[mask]
    return output


def load_data(path, profile_name="Full sample", mask=True, mask_val=1.e-11):
    import pandas as pd
    Macc_arr = np.loadtxt(path+"Macc.dat")
    age_arr = np.loadtxt(path+"age.dat")
    disk_frac = np.loadtxt(path+"frac.dat")

    arr_stacked = np.array([age_arr/1e6, disk_frac, Macc_arr]).T

    age = arr_stacked[:, 0]
    frac = arr_stacked[:, 1]*0.86
    mdot_acc = arr_stacked[:, 2]

    profile = np.array([profile_name] * np.size(arr_stacked[:, 1]))

    data = pd.DataFrame(
        {
            "mdot_acc": mdot_acc,
            "disk_fraction": frac,
            "age": age,
            "profile": profile
        }
    )

    data = mask_accretion(data, 1.e-13)

    if mask is True:
        data = mask_accretion(data, mask_val)

    return data
