# Ryan Schlimme
# 08 February 2024

'''
Investigating preliminary relationship between applied voltage and
photocurrent for photoelectric effect measurements using Hg lamp'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import statistics as stat
import os

my_path = os.path.dirname(__file__)

# Fit abs(Vs) = hc/e * 1/lambda + phi/e
# Order of lists is Tests [8, 9, 10, 11, 6, 7]


def Linear(x, m, b):
    return m*x + b


e = 1.60217663e-19      # Electron charge (C)
c = 299792458           # Speed of light (m/s)
hTrue = 6.62607015e-34  # Placnk's Constant (Js)

# Plot raw data to determine cutoff for pre and post Vs

tests = [13, 14, 15, 16]
nameIndex = [
    r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 2\Raw Data\Test" +
    str(i) for i in tests]

repeatedIndex = [
    r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 2\Repeated Raw Data\Test" +
    str(i) for i in range(3, 11)]

dfList = []
dfListRepeated = []

for i in nameIndex:
    dfList.append(pd.read_csv(i, sep="\t", engine="python"))

for i in repeatedIndex:
    dfListRepeated.append(pd.read_csv(i, sep="\t", engine="python"))


avgVdata = []
avgAdata = []

for x in range(len(dfList)):
    xVlist = dfList[x]["applied voltage (volts)"].values.tolist()
    y1Vlist = dfListRepeated[2*x]["applied voltage (volts)"].tolist()
    y2Vlist = dfListRepeated[2*x+1]["applied voltage (volts)"].tolist()
    xAlist = dfList[x]["measured current (nanoamps)"].tolist()
    y1Alist = dfListRepeated[2*x]["measured current (nanoamps)"].tolist()
    y2Alist = dfListRepeated[2*x+1]["measured current (nanoamps)"].tolist()
    avgVinternal = []
    avgAinternal = []
    for i in range(len(xVlist)):
        avgVinternal.append(stat.fmean([xVlist[i], y1Vlist[i], y2Vlist[i]]))
        avgAinternal.append((xAlist[i] + y1Alist[i] + y2Alist[i])/3)
    avgVdata.append(avgVinternal)
    avgAdata.append(avgAinternal)

Amax = avgAdata[0][-1]
scaling = []

for i in range(len(avgAdata)):
    data = avgAdata[i]
    scaling = Amax/data[-1]
    data1 = [z*scaling for z in data]
    avgAdata[i] = data1


'''Single Trace Figure'''
plt.figure(figsize= [3.375, 2.75])
plt.plot(avgVdata[0], avgAdata[0])
plt.plot(avgVdata[2], avgAdata[2])
plt.xlabel("Applied Voltage (V)")
plt.ylabel("Photocurrent (nA)")
plt.legend(["365-375 nm", "431-440 nm"])
plt.savefig(my_path + r"\Figures\Wavelength Single.svg", bbox_inches = "tight")
plt.close()

# Melissinos linear fitting
# Fit linear equation to pre Vs data and post Vs data. Intersection is Vs.

VdataPre = []
AdataPre = []
VdataPost = []
AdataPost = []


# Test13, 3, 4
VdataPre.append(avgVdata[0][0:77])
AdataPre.append(avgAdata[0][0:77])
VdataPost.append(avgVdata[0][202:])
AdataPost.append(avgAdata[0][202:])

# Test14, 5, 6
VdataPre.append(avgVdata[1][0:77])
AdataPre.append(avgAdata[1][0:77])
VdataPost.append(avgVdata[1][202:])
AdataPost.append(avgAdata[1][202:])

# Test15, 7, 8
VdataPre.append(avgVdata[2][0:152])
AdataPre.append(avgAdata[2][0:152])
VdataPost.append(avgVdata[2][227:])
AdataPost.append(avgAdata[2][227:])

# Test16, 9, 10
VdataPre.append(avgVdata[3][0:177])
AdataPre.append(avgAdata[3][0:177])
VdataPost.append(avgVdata[3][232:])
AdataPost.append(avgAdata[3][232:])

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

'''Linear Model Trace Figure'''
plt.figure(figsize= [3.375, 2.75])
popt1, pcov1 = curve_fit(Linear, VdataPre[2], AdataPre[2])
popt2, pcov2 = curve_fit(Linear, VdataPost[2], AdataPost[2])
intersection = (popt1[1]-popt2[1])/(popt2[0]-popt1[0])
print(intersection)

xvals = np.linspace(-2.5, -0.2, 1000)
xvals2 = np.linspace(-0.5, 0.5, 1000)

plt.plot(avgVdata[2], avgAdata[2], label = "431-440 nm Raw Trace")
plt.plot(xvals, Linear(xvals, *popt1), color = "black", alpha = 0.5, label = "")
plt.plot(xvals2, Linear(xvals2, *popt2), color = "black", alpha = 0.5, label = "")
plt.plot(intersection, Linear(intersection, *popt1), "ko", label = "$V_S = -0.43$ V", markersize = "5")
plt.xlabel("Applied Voltage (V)")
plt.ylabel("Photocurrent (nA)")
plt.legend()
plt.savefig(my_path + r"\Figures\Wavelength Fit.svg", bbox_inches = "tight")
plt.close()



wavelength = [(365+375)/2, 405, (431+440)/2, 548]

wavelength2 = [i*10**(-9) for i in wavelength]

absVs = [abs(i) for i in Vs]
invW = [1/i for i in wavelength]
invW2 = [1/i for i in wavelength2]

popt, pcov = curve_fit(Linear, invW2, absVs)

print(str(popt[0]/(c/e)) + " +/- " + str((np.sqrt(np.diag(pcov))/(c/e))[0]) + " Js")
print(str(popt[1]*e) + " +/- " + str(np.sqrt(np.diag(pcov))[1]*e) + " J")

'''Linear Fit Figure'''
plt.figure(figsize= [3.375, 2.75])

xvals = np.linspace(np.min(invW), np.max(invW), 1000)
popt, pcov = curve_fit(Linear, invW, absVs)

plt.plot(invW, absVs, "o-", label = "Raw Data")
plt.plot(xvals, Linear(xvals, *popt), label = "Fitted Line", alpha = 0.5, color = "k")

plt.xlabel(r"$1/\lambda$ (1/nm)")
plt.ylabel("$|V_S|$ (V)")
plt.legend()

plt.savefig(my_path + r"\Figures\Vs vs Lambda.svg", bbox_inches = "tight")
plt.close()
