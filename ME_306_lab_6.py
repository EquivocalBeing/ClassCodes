import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv(r"C:\Users\cacam\OneDrive\Documents\ME 306\ME_306_lab_6_data.csv", delimiter =',')

q1 = data["Flow_Rate_1"]
P1 = data["delta_P_1"]
L1 = data["Bed_Height_1"]

q2 = data["Flow_Rate_2"]
p2 = data["delta_P_2"]
L2 = data["Bed_Height_2"]

rho= 998 # kg/m^3
rho_p = 2500
dp = 0.001 # m
mu = 1.0E-03 # kg/ms  
epsilon = 0.4 # [?]


A1 = (np.pi * L1**2) / 4
U1 = q1 / A1

alfa = (150 * mu * (1 - epsilon)**2 * U1) / ( epsilon**3 * dp**2)
bravo = (1.75 * (1 - epsilon) * rho * U1**2) / dp
delta_P_1 = L1*(alfa + bravo)

print(delta_P_1)

A2 = (np.pi * L2**2) / 4
U2 = q2 / A2

charle = (150 * mu * (1 - epsilon)**2 * U2) / ( epsilon**3 * dp**2)
delta = (1.75 * (1 - epsilon) * rho * U2**2) / dp
delta_P_2 = L2*(charle + delta)

print("Trial 2")
print(delta_P_2)

u = (dp**2 * (rho_p - rho) * g) / (150 * mu) 
print(u)

################################################################################################################################


Q_1 = [0,1.58376,3.16752,4.75128,6.33504,7.9188]
delta_p_1 = [0,3.9343374,3.8540448,3.0109725,2.8905336,2.4890706]
height_1 = [54,54,54,54,54,55]


Q_2 = [0,13.198,21.7767,30.3554,39.594,47.5128]
delta_p_2 = [0,1.8868761,1.5255594,0.7226334,0.401463,0]
height_2 = [54,60,71,86,107,127]



fig, ax1 = plt.subplots(figsize = (19, 8))

ax2 = ax1.twinx()

ax1.plot(Q_2, delta_p_2, 'g-', label ="$\Delta P$ 2", linewidth = 5)
ax2.plot(Q_2, height_2, 'b-', label = "Bed Height 2", linewidth = 5)

ax1.plot(Q_1, delta_p_1, 'lime', label ="$\Delta P$ 1", linewidth = 5)
ax2.plot(Q_1, height_1, 'red', label = "Bed Height 1", linewidth = 5)


ax2.tick_params(axis='y', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax1.tick_params(axis='x', labelsize=14)


ax1.grid(True, which="both", ls="-", color = "black")
ax2.grid(True, which="both", ls="-", color = "black")

ax1.set_xlabel('Flow Rate [m^3/s]', fontsize = 20, fontweight = "bold")
ax1.set_ylabel('$\Delta P$ [Pa]', fontsize = 20, fontweight = "bold")
ax2.set_ylabel('L [m]', fontsize = 20, fontweight = "bold")

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Combine and place legend only on ax1
ax1.legend(handles1 + handles2, labels1 + labels2, loc="upper left", fontsize=15, ncol = 2)

#plt.savefig("lab_6.png", bbox_inches='tight')