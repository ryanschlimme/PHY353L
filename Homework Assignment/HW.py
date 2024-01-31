# 16 January 2023
# Ryan Schlimme

# Importing supplied data, creating plots and other analyses as specified in homework instructions


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

cols = [str(j)+str(i) for i in range(1,7) for j in ["x","y","z"]]
cols1 = ["t"] + cols

df = pd.read_csv(r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Homework Assignment\Homework Data\SampleData_Spring2024.dat", 
                   header = None, sep = "  *", names = cols1, engine = "python")


def Gaussian(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))


# Problem 1
# Plot all data as a function of time
plt.figure(figsize= (10, 4))
plt.plot(df["t"], df["x1"])
plt.plot(df["t"], df["x2"])
plt.plot(df["t"], df["x3"])
plt.xlabel("Time (arb units)")
plt.ylabel("$x$ position of three particles (arb units)")
plt.savefig("Problem 1.png")
plt.close()


# Problem 2
# Compute the mean and standard deviation of all columns after the first.
# Present results as table.
print("      ", str("Mean").center(5), "   ", str("Std Dev").center(10))
for col in df.columns[1:]:
    print(str(col), "--  ", str(round(np.mean(df[col]), 3)).ljust(5), "   ", str(round(np.std(df[col]), 3)).ljust(10))
print()

# Problem 3
# Compare average values of z for first 6 particles. Are they different? How do you quantify difference?
# ANSWER: a t test???


# Problem 4
# Make a historgram plot of columns 2 and 5. What is connection between these plots and question 2.
# ANSWER: Histograms show a distribution of numerical data with center at a mean and spread dictated by the standard dev.
# fig, axes = plt.subplots(2,1, sharey=True, sharex= True)
plt.hist(df["x1"], bins = 20)
plt.hist(df["x2"], bins = 20)
plt.legend(["Particle 1", "Particle 2"])
plt.xlabel("$x$ positions over time scan (arb units)")
plt.ylabel("Counts")
plt.savefig("Problem 4.png")
plt.close()


# Problem 5
# Make a plot comparing columns 2 and 3. Points in plot should be connected by lines. 
plt.plot(df["x1"], df["y1"], "-o")
plt.xlabel("$x$ position (arb units)")
plt.ylabel("$y$ position (arb units)")
plt.savefig("Problem 5.png")
plt.close()
    

# Problem 6
# Make a 3D plot
ax = plt.figure().add_subplot(projection="3d")
ax.plot(df["x1"], df["y1"], df["z1"], "-o")
ax.set_xlabel("$x$ position (arb units)")
ax.set_ylabel("$y$ position (arb units)")
ax.set_zlabel("$z$ position (arb units)")
plt.savefig("Problem 6.png")
plt.close()


# Problem 7
# Make a 3D plot for all 6 particles
ax = plt.figure().add_subplot(projection="3d")
for i in range(0, len(cols)-2, 3):
    string = str("Particle ")+str(i//3+1)
    ax.plot(df[str(cols[i])], df[str(cols[i+1])], df[str(cols[i+2])], "-o", label=string)
ax.set_xlabel("$x$ position (arb units)")
ax.set_ylabel("$y$ position (arb units)")
ax.set_zlabel("$z$ position (arb units)")
ax.legend()
plt.savefig("Problem 7.png")
plt.close()


# Problem 8
# Suggest what physical situation the data is computed for. Start by describing in words the result of the
# last two problems.

# This could be a lattice of harmonic oscillators bound in some sort of crystal structure. Each oscillates about
# some central location in 3D real space.


# Problem 9
# Fit the plot from question 4 to a Gaussian function. Compute the standard deviation of the mean and compare
# to the standard deviation computed in question 2. Is the Gaussian a good fit?

# Using the average of the bin boundaries
counts, bins, bars = plt.hist(df["x1"], bins = 20)
bindiff = [(bins[n]+bins[n-1])/2 for n in range(1,len(bins))]
popt, pcov = curve_fit(Gaussian, bindiff, counts)
print("Particle 1 x position")
print("Fitted Parameters: ", popt)
print("Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))
print("RMSE: ", np.sqrt(np.mean((counts-Gaussian(bindiff, *popt))**2)/len(counts)))
print()

xvals = np.linspace(-0.5, 0.5, 1000)
plt.plot(xvals, Gaussian(xvals, *popt))
plt.xlabel("$x$ positions over time scan (arb units)")
plt.ylabel("Counts")
plt.legend(["Gaussian Fit", "Raw Histogram"])
plt.savefig("Problem 9.1.png")
plt.close()

counts, bins, bars = plt.hist(df["x2"], bins = 20)
bindiff = [(bins[n]+bins[n-1])/2 for n in range(1,len(bins))]
popt, pcov = curve_fit(Gaussian, bindiff, counts)
print("Particle 1 x position")
print("Fitted Parameters: ", popt)
print("Parameter Standard Errors: ", np.sqrt(np.diag(pcov)))
print("RMSE: ", np.sqrt(np.mean((counts-Gaussian(bindiff, *popt))**2)/len(counts)))
print()

xvals = np.linspace(2.25, 3.25, 1000)
plt.plot(xvals, Gaussian(xvals, *popt))
plt.xlabel("$x$ positions over time scan (arb units)")
plt.ylabel("Counts")
plt.legend(["Gaussian Fit", "Raw Histogram"])
plt.savefig("Problem 9.2.png")