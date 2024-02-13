# 25 January 2023
# Ryan Schlimme

# Importing supplied data, creating plots, analyzing counting statistics

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


def Linear(x, m, b):
    return m*x + b


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
# for i, x in zip(dfList, intervals):
#     plt.hist(i["Ch1"], bins = 20, color = "b")
#     plt.hist(i["Ch2"], bins = 20, color = "r")
#     plt.legend(["Channel 1", "Channel 2"])
#     plt.xlabel("Gamma Ray Events per Interval")
#     plt.ylabel("Counts")
#     plt.title(str(x) + "ms")
#     plt.savefig(str(x)+"ms.pdf")
#     plt.close()
    
# Creating Figure Histograms
fig, axes = plt.subplots(2, 1, figsize = [3.375, 5], sharex= True, sharey= True)

for i, z, ax in zip(["Ch1", "Ch2"], ["b", "r"], axes.flatten()):
    ax.hist(dfList[0][i], bins = np.arange(0-0.25, max(dfList[0][i] + 0.25), 0.5), color = z)
    ax.legend([i])
fig.supxlabel("Gamma Ray Events per Interval")
fig.supylabel("Counts")
plt.savefig("Poissonian Hist Paper Figure.svg", bbox_inches = "tight")
plt.close()

fig, axes = plt.subplots(2, 1, figsize = [3.375, 5], sharey= True)

for i, z, ax in zip(["Ch1", "Ch2"], ["b", "r"], axes.flatten()):
    ax.hist(dfList[-1][i], bins = 16, color = z)
    ax.legend([i])
fig.supxlabel("Gamma Ray Events per Interval")
fig.supylabel("Counts")
plt.savefig("Gaussian Hist Paper Figure.svg", bbox_inches = "tight")
plt.close()

# Comparing Statistics Graph
plt.figure(figsize= [3.375, 2.75])
plt.plot(intervals, Ch1Avg, color = "b")
plt.plot(intervals, Ch2Avg, color = "r")
plt.plot(intervals, Ch1Std, "--b")
plt.plot(intervals, Ch2Std, "--r")
plt.xlabel("Time Interval (ms)")
plt.ylabel("Counts")
plt.legend(["Ch1 Avg", "Ch2 Avg", "Ch1 Std", "Ch2 Std"])
plt.savefig("Statistics Paper Figure.svg", bbox_inches = "tight")
plt.close()

# Linear Fit
'''
Channel 1:
m = 0.146 +/- 0.003, b = 1.8 +/- 0.4

Channel 2:
m = 0.108 +/- 0.002, b = 1.2 =/- 0.3

'''
popt, pcov = curve_fit(Linear, intervals, Ch1Avg)
print("Channel 1")
print("Fitted Parameters: ", popt)
print("Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))
print()

popt, pcov = curve_fit(Linear, intervals, Ch2Avg)
print("Channel 2")
print("Fitted Parameters: ", popt)
print("Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))
print()

