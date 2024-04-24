library(tidyverse)
library(mosaic)

# Quick check of all data
ggplot(Charge) +
  geom_histogram(aes(x = Charge), bins = 90)
# RECREATE THIS HISTOGRAM IN PYTHON

# Removing high charge, low count data
Charge_mod = Charge %>% 
  filter(Charge < 12e-19)

# Save dataframe for use in Python
setwd("C:/Users/Ryan Schlimme/OneDrive/Desktop/College/Spring 2024/PHY353L/Labs/Lab 5")
write.csv(Charge_mod, "Charge_mod.csv")

# Histogram with cutoffs for mean/sd calculation
ggplot(Charge_mod) +
  geom_histogram(aes(x = Charge), bins = 55) +
  geom_vline(xintercept = 2.9e-19) +
  geom_vline(xintercept = 4.4e-19) +
  geom_vline(xintercept = 5.9e-19) +
  geom_vline(xintercept = 7.3e-19) +
  geom_vline(xintercept = 10e-19)
# RECREATE THIS HISTOGRAM IN PYTHON


# Separating data for mean/sd calculation
e1 = Charge_mod %>% 
  filter(Charge < 2.9e-19)

e2 = Charge_mod %>% 
  filter(Charge < 4.4e-19 & Charge > 3e-19)

e3 = Charge_mod %>% 
  filter(Charge < 5.9e-19 & Charge > 4.3e-19)

e4 = Charge_mod %>% 
  filter(Charge < 7.3e-19 & Charge > 5.9e-19)

e5 = Charge_mod %>% 
  filter(Charge < 10e-19 & Charge > 7.3e-19)

e6 = Charge_mod %>% 
  filter(Charge < 12e-19 & Charge > 10e-19)

# Means
mean1 = mean(~Charge, data = e1)
mean2 = mean(~Charge, data = e2)
mean3 = mean(~Charge, data = e3)
mean4 = mean(~Charge, data = e4)
mean5 = mean(~Charge, data = e5)
mean6 = mean(~Charge, data = e6)

# Standard Deviations
sd1 = sd(~Charge, data = e1)
sd2 = sd(~Charge, data = e2)
sd3 = sd(~Charge, data = e3)
sd4 = sd(~Charge, data = e4)
sd5 = sd(~Charge, data = e5)
sd6 = sd(~Charge, data = e6)

# Difference in Means
diff1 = mean2 - mean1
diff2 = mean3 - mean2
diff3 = mean4 - mean3
diff4 = mean5 - mean4
diff5 = mean6 - mean5

# Variance for difference in means
error1 = sd2^2/44 + sd1^2/17 
error2 = sd3^2/16 + sd2^2/17
error3 = sd4^2/10 + sd3^2/16
error4 = sd5^2/10 + sd4^2/10
error5 = sd6^2/3 + sd5^2/10
  
# Average difference
(diff1 + diff2 + diff3 + diff4) / 4

# Sd of mean variance
sqrt((error1^2 + error2^2 + error3^2 + error4^2)/4)

