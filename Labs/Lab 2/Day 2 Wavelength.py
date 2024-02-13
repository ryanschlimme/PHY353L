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

tests = [12, 13, 14, 15, 16, 17]
nameIndex = [
    r"C:\Users\ryans\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 2\Raw Data\Test" +
    str(i) for i in tests]

dfList = []

for i in nameIndex:
    dfList.append(pd.read_csv(i, sep="\t", engine="python"))

# for i in range(6):
#     plt.plot(dfList[i]["applied voltage (volts)"].tolist(), dfList[i]["measured current (nanoamps)"].tolist())
#     plt.show()

# Melissinos linear fitting
# Fit linear equation to pre Vs data and post Vs data. Intersection is Vs.

VdataPre = []
AdataPre = []
VdataPost = []
AdataPost = []

# Test12
# VdataPre.append(dfList[0]["applied voltage (volts)"][0:103].tolist())
# AdataPre.append(dfList[0]["measured current (nanoamps)"][0:103].tolist())
# VdataPost.append(dfList[0]["applied voltage (volts)"][252:].tolist())
# AdataPost.append(dfList[0]["measured current (nanoamps)"][252:].tolist())

# Test13
VdataPre.append(dfList[1]["applied voltage (volts)"][0:77].tolist())
AdataPre.append(dfList[1]["measured current (nanoamps)"][0:77].tolist())
VdataPost.append(dfList[1]["applied voltage (volts)"][202:].tolist())
AdataPost.append(dfList[1]["measured current (nanoamps)"][202:].tolist())

# Test14
VdataPre.append(dfList[2]["applied voltage (volts)"][0:77].tolist())
AdataPre.append(dfList[2]["measured current (nanoamps)"][0:77].tolist())
VdataPost.append(dfList[2]["applied voltage (volts)"][202:].tolist())
AdataPost.append(dfList[2]["measured current (nanoamps)"][202:].tolist())

# Test15
VdataPre.append(dfList[3]["applied voltage (volts)"][0:152].tolist())
AdataPre.append(dfList[3]["measured current (nanoamps)"][0:152].tolist())
VdataPost.append(dfList[3]["applied voltage (volts)"][227:].tolist())
AdataPost.append(dfList[3]["measured current (nanoamps)"][227:].tolist())

# Test16
VdataPre.append(dfList[4]["applied voltage (volts)"][0:177].tolist())
AdataPre.append(dfList[4]["measured current (nanoamps)"][0:177].tolist())
VdataPost.append(dfList[4]["applied voltage (volts)"][232:].tolist())
AdataPost.append(dfList[4]["measured current (nanoamps)"][232:].tolist())

# # Test17
# VdataPre.append(dfList[5]["applied voltage (volts)"][0:750].tolist())
# AdataPre.append(dfList[5]["measured current (nanoamps)"][0:750].tolist())
# VdataPost.append(dfList[5]["applied voltage (volts)"][916:].tolist())
# AdataPost.append(dfList[5]["measured current (nanoamps)"][916:].tolist())

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


wavelength = [(365+375)/2, 405, (431+440)/2, 548]

wavelength = [i*10**(-9) for i in wavelength]

absVs = [abs(i) for i in Vs]
invW = [1/i for i in wavelength]

plt.plot(invW, absVs)
plt.show()
plt.close()

popt, pcov = curve_fit(Linear, invW, absVs)

print(str(popt[0]/(c/e)) + " +/-" + str((np.sqrt(np.diag(pcov))/(c/e))[0]) + " Js")

