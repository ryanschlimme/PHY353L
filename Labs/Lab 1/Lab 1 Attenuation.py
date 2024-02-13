# 31 January 2023
# Ryan Schlimme

# Importing supplied data, creating plots, analyzing attenuation coef of lead

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


def Exp(x, a, b):
    return a*np.exp(-b*x)


dfList025 = []
dfList100 = []
dfList400 = []
dfList600 = []
dfList800 = []

dfMain = [dfList025, dfList100, dfList400, dfList600, dfList800]

tests = [i for i in range(2, 9)]
tests.insert(0, 9)

nameIndex025 = [r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 1\Lab 1 Data\Cleaned Data Day 2\Test" +
                str(i) + "_25.lvm" for i in tests]
nameIndex100 = [r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 1\Lab 1 Data\Cleaned Data Day 2\Test" +
                str(i) + "_100.lvm" for i in tests]
nameIndex400 = [r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 1\Lab 1 Data\Cleaned Data Day 2\Test" +
                str(i) + "_400.lvm" for i in tests]
nameIndex600 = [r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 1\Lab 1 Data\Cleaned Data Day 2\Test" +
                str(i) + "_600.lvm" for i in tests]
nameIndex800 = [r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 1\Lab 1 Data\Cleaned Data Day 2\Test" +
                str(i) + "_800.lvm" for i in tests]

for i in nameIndex025:
    dfList025.append(pd.read_csv(i, sep="\t", engine="python"))

for i in nameIndex100:
    dfList100.append(pd.read_csv(i, sep="\t", engine="python"))

for i in nameIndex400:
    dfList400.append(pd.read_csv(i, sep="\t", engine="python"))

for i in nameIndex600:
    dfList600.append(pd.read_csv(i, sep="\t", engine="python"))

for i in nameIndex800:
    dfList800.append(pd.read_csv(i, sep="\t", engine="python"))

# Removing Iteration 0 from all as contains inaccurate counts
dfList1 = []
for z in dfList025:
    z = z.drop(0)
    dfList1.append(z)
dfList025 = dfList1

dfList1 = []
for z in dfList100:
    z = z.drop(0)
    dfList1.append(z)
dfList100 = dfList1

dfList1 = []
for z in dfList400:
    z = z.drop(0)
    dfList1.append(z)
dfList400 = dfList1

dfList1 = []
for z in dfList600:
    z = z.drop(0)
    dfList1.append(z)
dfList600 = dfList1

dfList1 = []
for z in dfList800:
    z = z.drop(0)
    dfList1.append(z)
dfList800 = dfList1

# Generate Averages and Std for Each dataframe
Ch1Avgs = []
Ch2Avgs = []
Ch1Stds = []
Ch2Stds = []

for j in dfMain:
    Ch1Avg = []
    Ch2Avg = []
    Ch1Std = []
    Ch2Std = []
    for i in range(0, 8):
        Ch1Avg.append(j[i]["Ch1"].mean())
        Ch2Avg.append(j[i]["Ch2"].mean())
        Ch1Std.append(j[i]["Ch1"].std())
        Ch2Std.append(j[i]["Ch2"].std())
    Ch1Avgs.append(Ch1Avg)
    Ch2Avgs.append(Ch2Avg)
    Ch1Stds.append(Ch1Std)
    Ch2Stds.append(Ch2Std)

thicknesses = [0, 1.530, 3.060, 5.800, 8.670, 14.500, 20.300, 29.000]
intervals = [25, 100, 400, 600, 800]

fig, axes = plt.subplots(2, 3)

z = range(0, 5)
for i, ax, j in zip(z, axes.flatten(), intervals):
    ax.plot(thicknesses, Ch1Avgs[i], "b")
    ax.plot(thicknesses, Ch2Avgs[i], "r")
    ax.plot(thicknesses, Ch1Stds[i], "b--d"])
plt.ylabel("Counts")
plt.xlabel("Lead thickness (mm)")
plt.savefig("Attenuation Paper Figure.svg", bbox_inches = "tight")
plt.close()

# Fitting Exponential Decay Functions
bList1 = []
bList2 = []
sdList1 = []
sdList2 = []
for i, j in zip(z, intervals):
    popt, pcov = curve_fit(Exp, thicknesses, Ch1Avgs[i])
    bList1.append(popt[1])
    sdList1.append(pcov[1]**2)  # Can only average variance
    print(str(j) + str(" ms"))
    print("     Channel 1")
    print("     Fitted Parameters: ", popt)
    print("     Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))
    print()
    popt, pcov = curve_fit(Exp, thicknesses, Ch2Avgs[i])
    bList2.append(popt[1])
    sdList2.append(pcov[1]**2)  # Can only average variance
    print("     Channel 2")
    print("     Fitted Parameters: ", popt)
    print("     Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))
    print()

# Measuring Attenuation Coefficients
    
'''
Cobalt 60 decays by means of ejecting a beta particle and 2 gamma rays of
approximate energies 1.2 and 1.3 MeV. The linear absorption coefficient of Pb
was found to be 0.545 cm^-1 by https://issuu.com/ijmretjournal/docs/03082838

We found
Channel 1: 0.5261 +/- 0.0003 cm^-1
Channel 2: 0.4336 +/- 0.0004 cm^-1
'''

print("Channel 1:", round(np.mean(bList1)*10, 4), "+/-", round(np.sqrt(np.mean(sdList1)*10), 4), "cm^-1") 
print("Channel 2:", round(np.mean(bList2)*10, 4), "+/-", round(np.sqrt(np.mean(sdList2)*10), 4), "cm^-1")