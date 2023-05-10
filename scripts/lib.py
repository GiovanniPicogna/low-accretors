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
