# Ryan Schlimme
# 08 February 2024

'''
Investigating preliminary relationship between applied voltage and
photocurrent for photoelectric effect measurements using Hg lamp'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Fit abs(Vs) = hc/e * 1/lambda + phi/e
# Order of lists is Tests [8, 9, 10, 11, 6, 7]


def Linear(x, m, b):
    return m*x + b


e = 1.60217663e-19      # Electron charge (C)
c = 299792458           # Speed of light (m/s)
hTrue = 6.62607015e-34  # Placnk's Constant (Js)

# Plot raw data to determine cutoff for pre and post Vs

tests = range(1, 5)
nameIndex = [
    r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 2\Raw Data\NDTest" +
    str(i) for i in tests]

dfList = []

for i in nameIndex:
    dfList.append(pd.read_csv(i, sep="\t", engine="python"))

Vmax = dfList[0]["measured current (nanoamps)"][292]
scaling = []

for i in range(4):
    data = dfList[i]["measured current (nanoamps)"].tolist()
    scaling = Vmax/data[292]
    data1 = [z*scaling for z in data[227:292]]
    dfList[i]["measured current (nanoamps)"] = data[0:227] + data1 + data[292:]

for i in range(4):
    plt.plot(dfList[i]["applied voltage (volts)"].tolist(), dfList[i]["measured current (nanoamps)"].tolist())
plt.show()

# Melissinos linear fitting
# Fit linear equation to pre Vs data and post Vs data. Intersection is Vs.

# first to -0.75, -.25 to 0.4

VdataPre = []
AdataPre = []
VdataPost = []
AdataPost = []

for i in range(4):
    VdataPre.append(dfList[i]["applied voltage (volts)"][0:177].tolist())
    AdataPre.append(dfList[i]["measured current (nanoamps)"][0:177].tolist())
    VdataPost.append(dfList[i]["applied voltage (volts)"][227:292].tolist())
    AdataPost.append(dfList[i]["measured current (nanoamps)"][227:292].tolist())

Vs = []


for i in range(4):
    popt1, pcov1 = curve_fit(Linear, VdataPre[i], AdataPre[i])
    popt2, pcov2 = curve_fit(Linear, VdataPost[i], AdataPost[i])
    # append Vs as the intersection
    # plt.plot(dfList[(i)]["applied voltage (volts)"].tolist(), dfList[(i)]["measured current (nanoamps)"].tolist())
    # xvals = np.linspace(-2.5, 1, 1000)
    # plt.plot(xvals, Linear(xvals, *popt1))
    # plt.plot(xvals, Linear(xvals, *popt2))
    # plt.close()
    Vs.append((popt1[1]-popt2[1])/(popt2[0]-popt1[0]))


OD = [0.1, 0.3, 0.5, 0.9]
intensities = [10**i for i in OD]

absVs = [abs(i) for i in Vs]

plt.plot(intensities, absVs)
plt.show()
plt.close()

popt, pcov = curve_fit(Linear, intensities, absVs)

print("Parameter Estimates: ", popt)
print("Parameter Errors: ", np.sqrt(np.diag(pcov)))