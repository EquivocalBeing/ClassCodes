import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec

data = pd.read_csv(
    r"C:\Users\cacam\OneDrive\Documents\ME348_python_project\proj_3_18_25_nd_res\solution.txt",
                   delimiter='\s+') 

data.columns = ["time_nd", "m1_x_nd", "m1_v_nd", "m2_x_nd", "m2_v_nd", "m1_dx/dt_nd", "m1_dv/dt_nd", 
                "m2_dx/dt_nd", "m2_dv/dt_nd"]

time_nd = data["time_nd"]
m1_x_nd = data["m1_x_nd"]
m1_v_nd = data["m1_v_nd"]
m2_x_nd = data["m2_x_nd"]
m2_v_nd = data["m2_v_nd"]

################################################### # Input the values here # ##################################################

#f_tld = a_tld * np.sin(b_tld * t)

m1 = 1250 # kg
m1_m2 = 0.12 # kg/kg
b_omega = 5 # [?]
b_tld = 1.5 # [?]
a_tld = 5  # [?]
V = 0.1 # m/s

################################################################################################################################

k_tld = b_tld**2
m2 = m1 * m1_m2
k2 = m2 * b_tld**2
k = m2 * b_omega**2
T = b_tld / b_omega
L = (V * k_tld * T) / (a_tld * b_tld)
v_tld = (T / L) * V
test = (a_tld * b_tld) / k_tld

#------------------------------------------------------------------------------------------------------------------------------#

time_d = T * time_nd
m1_x_d = L * m1_x_nd 
m1_v_d = v_tld * m1_v_nd 
m2_x_d = L * m2_x_nd
m2_v_d = v_tld * m2_v_nd

################################################################################################################################

print("-----------------")
print(f"v_tld: {v_tld:.4f} nd")
print("m2:    " + str(m2) + " kg")
print("k:     " + str(k2) + " N/m")
print("-----------------")
print("T:     " + str(T))
print(f"L:     {L:.4f}")
print("k_tld: " + str(k_tld))
print("-----------------")

################################################################################################################################

fig = plt.figure(1, figsize = (28,20))
gs = gridspec.GridSpec(2,2, height_ratios = [1,1], hspace = 0.2, wspace = 0.2)

fig.suptitle("Non-Dimensional", fontweight = 'bold', fontsize = 30, va = "center", y = .93)

axis1 = fig.add_subplot(gs[0,0])
axis1.tick_params(labelsize=22)
axis1.yaxis.get_offset_text().set_fontsize(18)

axis1.plot(time_nd, m1_x_nd, color = "blue", linewidth = 3)

axis1.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis1.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis1.set_ylabel("Displacement [m]", fontweight = "bold", fontsize = 20)
axis1.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis2 = fig.add_subplot(gs[0,1])
axis2.tick_params(labelsize=22)
axis2.yaxis.get_offset_text().set_fontsize(18)

axis2.plot(time_nd, m1_v_nd, color = "red", linewidth = 3)

axis2.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis2.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis2.set_ylabel("Velocity [m/s]", fontweight = "bold", fontsize = 20)
axis2.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis3 = fig.add_subplot(gs[1,0])
axis3.tick_params(labelsize=22)


axis3.plot(time_nd, m2_x_nd, color = "blue", linewidth = 3)

axis3.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis3.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis3.set_ylabel("Displacement [m]", fontweight = "bold", fontsize = 20)
axis3.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis4 = fig.add_subplot(gs[1,1])
axis4.tick_params(labelsize=22)

axis4.plot(time_nd, m2_v_nd, color = "red", linewidth = 3)

axis4.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis4.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis4.set_ylabel("Velocity [m/s]", fontweight = "bold", fontsize = 20)
axis4.grid(True, which="both", ls="-")

#plt.savefig("ME_348_HW_10.png", bbox_inches='tight')

################################################################################################################################

fig2 = plt.figure(2, figsize = (28,20))
gs = gridspec.GridSpec(2,2, height_ratios = [1,1], hspace = 0.2, wspace = 0.2)

fig2.suptitle("Dimensional", fontweight = 'bold', fontsize = 30, va = "center", y = .93)

axis1 = fig2.add_subplot(gs[0,0])
axis1.tick_params(labelsize=22)
axis1.yaxis.get_offset_text().set_fontsize(18)

axis1.plot(time_d, m1_x_d, color = "blue", linewidth = 3)

axis1.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis1.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis1.set_ylabel("Displacement [m]", fontweight = "bold", fontsize = 20)
axis1.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis2 = fig2.add_subplot(gs[0,1])
axis2.tick_params(labelsize=22)
axis2.yaxis.get_offset_text().set_fontsize(18)

axis2.plot(time_d, m1_v_d, color = "red", linewidth = 3)

axis2.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis2.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis2.set_ylabel("Velocity [m/s]", fontweight = "bold", fontsize = 20)
axis2.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis3 = fig2.add_subplot(gs[1,0])
axis3.tick_params(labelsize=22)


axis3.plot(time_d, m2_x_d, color = "blue", linewidth = 3)

axis3.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis3.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis3.set_ylabel("Displacement [m]", fontweight = "bold", fontsize = 20)
axis3.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis4 = fig2.add_subplot(gs[1,1])
axis4.tick_params(labelsize=22)

axis4.plot(time_d, m2_v_d, color = "red", linewidth = 3)

axis4.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis4.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis4.set_ylabel("Velocity [m/s]", fontweight = "bold", fontsize = 20)
axis4.grid(True, which="both", ls="-")

#plt.savefig("ME_348_HW_10.png", bbox_inches='tight')