# 15 April 2024
# Ryan Schlimme

# Importing data, creating plots

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Importing charge data as list
file_name = r"C:\Users\Ryan Schlimme\OneDrive\Desktop\College\Spring 2024\PHY353L\Labs\Lab 5\Charge.csv"
data = pd.read_csv(file_name, sep=",", engine="python")

# Extract raw data
data = data["Charge"].to_list()

# Remove higher charge data
data_reduced = [i for i in data if i < 9.4e-19]
data_erased = [i for i in data if i >= 9.4e-19]
bins = np.histogram(np.hstack((data, data_reduced)), bins=125)[1]

'''Paper Figures'''
# Creating Histogram w/ Cutoffs
plt.figure(figsize=[2*3.375, 2.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5, label = "Included Data")
plt.hist(data_erased, bins=bins, color="red", edgecolor = "black", linewidth = 0.5, alpha=0.4, label = "Excluded Data")
plt.vlines([3e-19, 4.4e-19, 5.9e-19, 7.4e-19, 9.2e-19],
           ymin=0, ymax=25, color="black", label = "Cutoffs")
plt.text(3.2e-19, 9, "1st Cutoff", rotation=90)
plt.text(4.6e-19, 9, "2nd Cutoff", rotation=90)
plt.text(6.1e-19, 9, "3rd Cutoff", rotation=90)
plt.text(7.6e-19, 9, "4th Cutoff", rotation=90)
plt.text(9.4e-19, 9, "5th Cutoff", rotation=90)
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
plt.legend()
# plt.show()
# plt.savefig("Raw Hist.svg", bbox_inches = "tight")
plt.close()


# Creating Histogram w/ Local Averages Differences
plt.figure(figsize=[2*3.375, 2.5])
plt.hist(data_reduced, bins=bins, edgecolor="black", label="Included Data")
# plt.vlines([1e-19, 2.9e-19, 4.4e-19, 6e-19, 7.3e-19], ymin=0, ymax=11, color="black", label = "Cutoffs", alpha = 0.75)
plt.vlines([1.938045e-19, 3.803902e-19, 5.058158e-19, 6.754783e-19, 8.331667e-19], ymin=0,
           ymax=25, colors="red", ls="--", label="Local Means ($\mu_i$)")
plt.annotate(text='', xy=(1.938045e-19, 15), xytext=(3.803902e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
plt.annotate(text='', xy=(5.058158e-19, 15), xytext=(3.803902e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
plt.annotate(text='', xy=(5.058158e-19, 15), xytext=(6.754783e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
plt.annotate(text='', xy=(6.754783e-19, 15), xytext=(8.331667e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
plt.annotate(text = "$\mu_2-\mu_1$", xy = (2.5e-19, 16))
plt.annotate(text = "$\mu_3-\mu_2$", xy = (4.05e-19, 16))
plt.annotate(text = "$\mu_4-\mu_3$", xy = (5.55e-19, 16))
plt.annotate(text = "$\mu_5-\mu_4$", xy = (7.2e-19, 16))
plt.ylim(0, 20)
plt.xlim(-1.4e-19, 9.4e-19)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
plt.legend(loc="upper left")
#plt.show()
# plt.savefig("Processed Hist.svg", bbox_inches = "tight")
plt.close()


'''Presentation Figures'''
# Creating Raw Histogram w/o Cutoffs
plt.rcParams.update({'font.size': 18})
plt.figure(figsize=[13.333, 7.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5)
plt.hist(data_erased, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5)
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
# plt.show()
plt.savefig("PresRaw.svg", bbox_inches = "tight")
plt.close()

# Creating Raw Histogram w/ Main Cutoff
plt.rcParams.update({'font.size': 18})
plt.figure(figsize=[13.333, 7.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5, label = "Included Data")
plt.hist(data_erased, bins=bins, color="red", edgecolor = "black", linewidth = 0.5, alpha=0.4, label = "Excluded Data")
plt.vlines([9.4e-19], ymin=0, ymax=25, color="black", label = "Cutoffs")
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
# plt.legend()
# plt.show()
plt.savefig("PresCut.svg", bbox_inches = "tight")
plt.close()

# Creating Zoomed Histogram w/o Cutoffs
plt.rcParams.update({'font.size': 18})
plt.figure(figsize=[13.333, 7.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5, label = "Included Data")
plt.xlim(0, 9.4e-19)
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
# plt.legend()
# plt.show()
plt.savefig("PresReduced.svg", bbox_inches = "tight")
plt.close()


# Creating Zoomed Histogram w/ Cutoffs
plt.rcParams.update({'font.size': 18})
plt.figure(figsize=[13.333, 7.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5, label = "Included Data", alpha = 0.5)
plt.vlines([2.8e-19, 4.4e-19, 5.9e-19, 7.4e-19],
           ymin=0, ymax=25, color="black", label = "Cutoffs", linewidth = 3)
plt.xlim(0, 9.4e-19)
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
# plt.legend()
# plt.show()
plt.savefig("PresRedLines.svg", bbox_inches = "tight")
plt.close()

# Creating Zoomed Histogram w/ Cutoffs and Means
plt.rcParams.update({'font.size': 18})
plt.figure(figsize=[13.333, 7.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5, label = "Included Data", alpha = 0.5)
plt.vlines([2.8e-19, 4.4e-19, 5.9e-19, 7.4e-19],
           ymin=0, ymax=25, color="black", label = "Cutoffs", linewidth = 3, alpha = 0.5)
plt.vlines([1.938045e-19, 3.803902e-19, 5.058158e-19, 6.754783e-19, 8.331667e-19], ymin=0,
           ymax=25, colors="red", ls="--", label="Local Means ($\mu_i$)", linewidth = 3)
plt.xlim(0, 9.4e-19)
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
# plt.legend()
# plt.show()
plt.savefig("PresRedMeans.svg", bbox_inches = "tight")
plt.close()

# Creating Zoomed Histogram w/ Cutoffs and Means and DiffMeans
plt.rcParams.update({'font.size': 18})
plt.figure(figsize=[13.333, 7.5])
plt.hist(data_reduced, bins=bins, color="#1f77b4", edgecolor = "black", linewidth = 0.5, label = "Included Data", alpha = 0.5)
plt.vlines([2.8e-19, 4.4e-19, 5.9e-19, 7.4e-19],
           ymin=0, ymax=25, color="black", label = "Cutoffs", linewidth = 3, alpha = 0.5)
plt.vlines([1.938045e-19, 3.803902e-19, 5.058158e-19, 6.754783e-19, 8.331667e-19], ymin=0,
           ymax=25, colors="red", ls="--", label="Local Means ($\mu_i$)", linewidth = 3)
plt.annotate(text='', xy=(1.938045e-19, 15), xytext=(3.803902e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0, linewidth = 3))
plt.annotate(text='', xy=(5.058158e-19, 15), xytext=(3.803902e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0, linewidth = 3))
plt.annotate(text='', xy=(5.058158e-19, 15), xytext=(6.754783e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0, linewidth = 3))
plt.annotate(text='', xy=(6.754783e-19, 15), xytext=(8.331667e-19, 15),
             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0, linewidth = 3))
plt.xlim(0, 9.4e-19)
plt.ylim(0, 20)
plt.xlabel("Oil Drop Charge Magnitude (Coulombs)")
plt.ylabel("Counts")
# plt.legend()
# plt.show()
plt.savefig("PresRedDiffMeans.svg", bbox_inches = "tight")
plt.close()
