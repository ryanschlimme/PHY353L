# 15 April 2024
# Ryan Schlimme

# Importing data, creating plots

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# Importing charge data as list
file_name = r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 5\Charge_mod.csv"
data = pd.read_csv(file_name, sep = ",", engine = "python")

data = data["Charge"].to_list()
    
# Creating Histogram w/ Cutoffs
plt.figure(figsize=[2*3.375, 2.5])
plt.hist(data, bins = 45)
plt.vlines([3e-19, 4.3e-19, 6e-19, 7.3e-19], ymin = 0, ymax = 11, color = "black")
plt.text(3.1e-19, 4, "1st Cutoff", rotation = 90)
plt.text(4.4e-19, 4, "2nd Cutoff", rotation = 90)
plt.text(6.1e-19, 4, "3rd Cutoff", rotation = 90)
plt.text(7.4e-19, 4, "4th Cutoff", rotation = 90)
plt.ylim(0, 11)
plt.xlabel("Oil Drop Charge (Coulombs)")
plt.ylabel("Counts")
plt.show()
# plt.savefig("Poissonian Hist Paper Figure.svg", bbox_inches = "tight")
# plt.close()


# Creating Histogram w/ Local Averages Differences

plt.figure(figsize=[2*3.375, 2.5])
plt.hist(data, bins = 34)
plt.vlines([3e-19, 4.3e-19, 6e-19, 7.35e-19], ymin = 0, ymax = 11, color = "black")
plt.text(3.1e-19, 4, "1st Cutoff", rotation = 90)
plt.text(4.4e-19, 4, "2nd Cutoff", rotation = 90)
plt.text(6.1e-19, 4, "3rd Cutoff", rotation = 90)
plt.text(7.4e-19, 4, "4th Cutoff", rotation = 90)
# plt.xlim(0, 7.3e-19)
# plt.ylim(0, 11)
plt.xlabel("Oil Drop Charge (Coulombs)")
plt.ylabel("Counts")
plt.show()
# plt.savefig("Poissonian Hist Paper Figure.svg", bbox_inches = "tight")
# plt.close()