# Ryan Schlimme
# 28 February 2024

'''
Determine interplanar spacing of graphite crystal via electron diffraction
using manually measured radii
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



df = pd.read_csv(r"C:\Users\ryans\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 3\ManualData.csv", sep=",", engine="python")

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

print(output)

# From our output, we see radii corresponding to a unique spacing

# r1: GUESS 1st ORDER MODE

# r2: likely a 2nd order mode
    # r2/r1 ~ 0.54 (~1/2)

Modes = [1, 2]

modifiedModes = [i/3 for i in Modes]   

modesMeanSpacings = []

for i, n in zip(range(0, len(meanSpacings)), modifiedModes):
    modesMeanSpacings.append(meanSpacings[i]*n)

print(modesMeanSpacings)

'''
Conclusion:

We observed several modes of the inter-planar spacing of graphite (theoretical 0.15 nm)
By correcting the spacing function using our predicted modes, we get a spacing of 0.62 +/- 0.02 nm
This is far too high.

We predict that our calculated modes are in fact multiples of the true mode which would correct for this
By dividing each number by 3, we claim to observe a spacing of 0.204 +/- 0.007 nm.
We expect to see spacings of 0.123 nm and 0.213 nm. However, we only observed the larger interplanar spacing.

To verify this claim:
- We observe r1 = 9.05, r2 = 19.05. Theory predicts, we should see r1 = 7.22, r2 = 14.49 

'''