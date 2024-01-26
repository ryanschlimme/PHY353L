# 25 January 2023
# Ryan Schlimme

# Importing supplied data, creating plots, analyzing counting statistics

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


def Gaussian(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))


# Importing data as list of dataframes
dfList = []
intervals = [10, 25, 50, 100, 250, 400, 600, 800, 1000, 1200, 1500, 2500, 4000]
nameIndex = [r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 1\Lab 1 Data\Cleaned Data\ms" + str(i) + ".lvm" for i in intervals]
for i in nameIndex:
    dfList.append(pd.read_csv(i, sep = "\t", engine = "python"))

# Removing Iteration 0 from all as contains inaccurate counts
dfList1 = []
for z in dfList:
    z = z.drop(0)
    dfList1.append(z)
dfList = dfList1

dfList[-2] = dfList[-2].drop(80)    # Removing Iteration 80 from 2500 ms run as contains 0.0

# Compute Statistics
Ch1Avg = []
Ch2Avg = []
Ch1Std = []
Ch2Std = []

for i in dfList:
    Ch1Avg.append(i["Ch1"].mean())
    Ch2Avg.append(i["Ch2"].mean())
    Ch1Std.append(i["Ch1"].std())
    Ch2Std.append(i["Ch2"].std())


# Creating Histograms
for i, x in zip(dfList, intervals):
    plt.hist(i["Ch1"], bins = 20, color = "b")
    plt.hist(i["Ch2"], bins = 20, color = "r")
    plt.legend(["Channel 1", "Channel 2"])
    plt.xlabel("Gamma Ray Events per Interval")
    plt.ylabel("Counts")
    plt.title(str(x) + "ms")
    plt.show()