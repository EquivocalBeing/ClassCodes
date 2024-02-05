from matplotlib import pyplot as plt
import numpy as np

start_time = 0
end_time = 1
sample_rate = 1000
time = np.arange(start_time, end_time, 1/sample_rate)
theta = 0
frequency = 2
amplitude = 14.12
sinewave = amplitude * np.sin(2 * np.pi * frequency * time + theta)
plt.figure(figsize=(20, 6), dpi=80)
plt.axhline(y = (21.22), color = 'black', linestyle = '-.', label = 'Sigma Mean')
plt.axhline(y = (35.4), color = 'red', linestyle = '-.', label = 'Sigma Max')
plt.axhline(y = (7.07), color = 'green', linestyle = '-.', label = 'Sigma Min')
plt.legend(loc = 'upper right', fontsize = 15)

plt.title('Round Bar: Stress V Time', fontsize = '15')
plt.xlabel('Time (s)', fontsize = '15')
plt.ylabel('Sigma (MPa)', fontsize = '15')
plt.plot(sinewave + 21.22)
plt.savefig('HW3_Q3_P1_Round_Bar.pdf')


start_time = 0
end_time = 1
sample_rate = 1000
time = np.arange(start_time, end_time, 1/sample_rate)
theta = 0
frequency = 2
amplitude = 4625 / 2
sinewave = amplitude * np.sin(2 * np.pi * frequency * time + theta)
plt.figure(figsize=(20, 6), dpi=80)
plt.axhline(y = (3187.5), color = 'black', linestyle = '-.', label = 'Sigma Mean')
plt.axhline(y = (5500), color = 'red', linestyle = '-.', label = 'Sigma Max')
plt.axhline(y = (875), color = 'green', linestyle = '-.', label = 'Sigma Min')
plt.legend(loc = 'upper right', fontsize = 15)

plt.title('Square Bar: Stress V Time', fontsize = '15')
plt.xlabel('Time (s)', fontsize = '15')
plt.ylabel('Sigma (MPa)', fontsize = '15')
plt.plot(sinewave + 3187.5)
plt.savefig('HW3_Q3_P2_Square_Bar.pdf')
