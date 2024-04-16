library(tidyverse)
library(mosaic)

# Quick check of all data
ggplot(Charge) +
  geom_histogram(aes(x = Charge), bins = 90)
# RECREATE THIS HISTOGRAM IN PYTHON

# Removing high charge, low count data
Charge_mod = Charge %>% 
  filter(Charge < 1.2e-18)

# Save dataframe for use in Python
setwd("C:/Users/Ryan Schlimme/OneDrive/Desktop/College/Spring 2024/PHY353L/Labs/Lab 5")
write.csv(Charge_mod, "Charge_mod.csv")

# Histogram with cutoffs for mean/sd calculation
ggplot(Charge_mod) +
  geom_histogram(aes(x = Charge), bins = 45) +
  geom_vline(xintercept = 3e-19) +
  geom_vline(xintercept = 4.3e-19) +
  geom_vline(xintercept = 6e-19) +
  geom_vline(xintercept = 7.3e-19)
# RECREATE THIS HISTOGRAM IN PYTHON


# Separating data for mean/sd calculation
e1 = Charge_mod %>% 
  filter(Charge < 3e-19)

e2 = Charge_mod %>% 
  filter(Charge < 4.3e-19 & Charge > 3e-19)

e3 = Charge_mod %>% 
  filter(Charge < 6e-19 & Charge > 4.3e-19)

e4 = Charge_mod %>% 
  filter(Charge < 7.3e-19 & Charge > 6e-19)

# Means
mean1 = mean(~Charge, data = e1)
mean2 = mean(~Charge, data = e2)
mean3 = mean(~Charge, data = e3)
mean4 = mean(~Charge, data = e4)

# Standard Deviations
sd1 = sd(~Charge, data = e1)
sd2 = sd(~Charge, data = e2)
sd3 = sd(~Charge, data = e3)
sd4 = sd(~Charge, data = e4)

# Difference in Means
diff1 = mean2 - mean1
diff2 = mean3 - mean2
diff3 = mean4 - mean3

# Variance for difference in means
error1 = sd2^2/9 + sd1^2/28 
error2 = sd3^2/15 + sd2^2/9
error3 = sd4^2/6 + sd3^2/15

# Average difference
mean(diff1, diff2, diff3) * 10^19
# Sd of mean variance
sqrt(mean(error1, error2, error3)) * 10^19

