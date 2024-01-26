library(tidyverse)
library(mosaic)
library(patchwork)

# Erasing First Entry
ms10 = ms10 %>% 
  filter(Iteration != 0)

ms100 = ms100 %>% 
  filter(Iteration != 0)

ms1000 = ms1000 %>% 
  filter(Iteration != 0)

ms1200 = ms1200 %>% 
  filter(Iteration != 0)

ms1500 = ms1500 %>% 
  filter(Iteration != 0)

ms25 = ms25 %>% 
  filter(Iteration != 0)

ms250 = ms250 %>% 
  filter(Iteration != 0)

ms2500 = ms2500 %>% 
  filter(Iteration != 0)

ms400 = ms400 %>% 
  filter(Iteration != 0)

ms4000 = ms4000 %>% 
  filter(Iteration != 0)

ms50 = ms50 %>% 
  filter(Iteration != 0)

ms600 = ms600 %>% 
  filter(Iteration != 0)

ms800 = ms800 %>% 
  filter(Iteration != 0)


# RMS Voltage Summaries
sdV10 = sd(~newV10, data = Lab9Data)
sdV47k = sd(~newV47k, data = Lab9Data)
sdV94k = sd(~newV94k, data = Lab9Data)
sdV220k = sd(~newV220k, data = Lab9Data)
sdV672k = sd(~newV672k, data = Lab9Data)


# Histograms
p1 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV10)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "Counts",
       subtitle = "10 Ohm, RMS = 5.28 mV")

p2 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV47k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "",
       subtitle = "47 kOhm, RMS = 7.80 mV")

p3 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV94k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "",
       subtitle = "94 kOhm, RMS = 7.75 mV")

p4 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV220k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "Counts",
       subtitle = "220 kOhm, RMS = 6.87 mV")

p5 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV672k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "Residual Voltage (Volts)",
       y = "",
       subtitle = "672 kOhm, RMS = 6.80 mV")

p1 + p2 + p3 + p4  + p5  +
  plot_annotation(title = "Johnson Noise Histograms") & 
  theme(plot.title = element_text(size = rel(1.5))) 