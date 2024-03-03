# Ryan Schlimme
# 28 February 2024

'''
Determine interplanar spacing of graphite crystal via electron diffraction
using image measured radii
'''

import statistics as stat
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import os

my_path = os.path.dirname(__file__)

e = 1.60217663e-19      # Electron charge (C)
c = 299792458           # Speed of light (m/s)
h = 6.62607015e-34      # Placnk's Constant (Js)
me = 9.1093837e-31      # Mass of electron (kg)

constant = h*c / np.sqrt(2* me * c**2 * e) * 10**9


def spacing(Va, r):
    return constant/np.sqrt(Va)*(2*140)/r


def uncertainty(Va, r, n, L = 140):
    dV = (-1*n*constant/10e9*L) / (2*Va**(-3/2)*r)
    dR = (-n*constant/10e9*L) / (np.sqrt(Va)*r**2)
    return np.sqrt((dV*100)**2 + (dR*0.5)**2)



df = pd.read_csv(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 3\ImageData.csv", sep=",", engine="python")

spacings = []

# for i in range(21):
#     row = df.loc[i].values.flatten().tolist()
#     row[:] = [x for x in row if str(x) != "nan"]
#     intermediate = []
#     for j in range(1, len(row) - 1):
#         intermediate.append(spacing(row[0], row[j]))
#     spacings.append(intermediate)


# Calculating the spacing from each radius and voltage combination
# for i in df:
#     if i == "Va":
#         voltages = df[i].tolist()
#         continue
#     radii = df[i].tolist()
#     for v in voltages:
#         intermediate = []
#         for r in radii:
#             if str(r) == "nan":
#                 continue
#             intermediate.append(spacing(v, r))
#     spacings.append(intermediate)

radii_list = []

for i in df:
    if str(i) == "Va":
        voltages = df[i].tolist()
        continue
    radii_list.append(df[i].tolist())

for i in range(len(radii_list)):
    radii = radii_list[i]
    intermediate = []
    for v,r in zip(voltages, radii):
        if str(r) == "nan":
            continue
        intermediate.append(spacing(v,r))
    spacings.append(intermediate)

'''Radii vs Voltages Line Graph'''
plt.figure(figsize= [2*3.375, 2.75])
for i in range(len(radii_list)):
    plt.plot(voltages[1:], radii_list[i][1:], "-o")
plt.xlabel("Accelerating Voltage, $V_A$ (V)")
plt.ylabel("Radius (mm)")
#plt.legend(["r1", "r2", "r3", "r4", "r5", "r6"])
#plt.show()
plt.savefig(my_path + r"\Figures\RadiiTraces.svg", bbox_inches = "tight")
plt.close()

# Calculating the average and sd spacing for each radius
# Theoretically identical
meanSpacings = []
sdSpacings = []

for i in spacings:
    meanSpacings.append(stat.fmean(i))
    sdSpacings.append(np.std(i))

# Calculating pairwise ratios of elements in mean list
# Theoretically, rational if comparing two modes
# If not approximately rational with a reaosnable ratio, comparing two different planes
# Ratio of radii (r1/r2) corresponds to ratio of modes (n2/n1)!!!!!
output = []

for i in range(0,len(meanSpacings)):
    intermediate = []
    for j in range(0,len(meanSpacings)):
        if (i!=j):
            intermediate.append(("r" + str(j+1) + "/" + "r" + str(i+1), 
                           meanSpacings[j]/meanSpacings[i]))
    output.append(intermediate)

# print(output[4])

# From our output, we see radii corresponding to a unique spacing

# r1: GUESS 1st ORDER MODE

# r2: likely a 2nd order mode
    # r2/r1 ~ 0.47 (~1/2)

# r3: likely a 3rd order mode
    # r3/r1 ~ 0.34 (~1/3)
    # r3/r2 ~ 0.71 (~2/3)

# r4: likely a 4th order mode
    # r4/r1 ~ 0.24 (~1/4)
    # r4/r2 ~ 0.50 (~2/4)
    # r4/r3 ~ 0.70 (~3/4) EHH

# r5: likely a 5th order mode
    # r5/r1 ~ 0.21 (~1/5)
    # r5/r2 ~ 0.44 (~2/5) EHH
    # r5/r3 ~ 0.63 (~3/5)
    # r5/r4 ~ 0.89 (~4/5) EHH

# r6: maybe a 7th order mode
    # r6/r1 ~ 0.135 (~1/7 = 0.143) EHHH
    # r6/r2 ~ 0.287 (~2/7 = 0.286)
    # r6/r3 ~ 0.403 (~3/7 = 0.429) NO
    # r6/r4 ~ 0.573 (~4/7 = 0.572)
    # r6/r5 ~ 0.648 (~5/7 = 0.714) EHHH

Modes = [1, 2, 3, 4, 5, 7]

modifiedModes = [i/10 for i in Modes]  

modesMeanSpacings = []

for i, n in zip(range(0, len(meanSpacings)), modifiedModes):
    modesMeanSpacings.append(meanSpacings[i]*n)

print(np.mean(modesMeanSpacings))
print(np.std(modesMeanSpacings))

'''
Conclusion:

We observed several modes of the inter-planar spacing of graphite (theoretical 0.15 nm)
By correcting the spacing function using our predicted modes, we get a spacing of 17.6 +/- 0.7 nm
This is far too high.

We predict that our calculated modes are in fact multiples of the true mode which would correct for this
By dividing each number by 10, we claim to observe a spacing of 0.176 +/- 0.007 nm.
We expect to see spacings of 0.123 nm and 0.213 nm. However, we observed approximately the average of 0.168 nm.

'''