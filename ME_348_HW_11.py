import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec

data = pd.read_csv(
    r"C:\Users\cacam\OneDrive\Documents\ME348_python_project\proj_4_1_25_nd_suspension\sol_eigenvalues.txt",
                   delimiter='\s+') 

data.columns = ["num", "Xi", "eigen_1", 'eigen_1_imagery', 'eigen_2', 'eigen_2_imagery', 'eigen_3', 'eigen_3_imagery',
                'eigen_4', 'eigen_4_imagery']

xi = data["Xi"]
e1 = data["eigen_1"]
e1_i = data["eigen_1_imagery"]
e2 = data["eigen_2"]
e2_i = data["eigen_2_imagery"]
e3 = data["eigen_3"]
e3_i = data["eigen_3_imagery"]
e4 = data["eigen_4"]
e4_i = data["eigen_4_imagery"]


################################################################################################################################


plt.figure(1, figsize = (19, 8))

plt.yticks(fontsize = 20, fontweight = "bold")
plt.xticks(fontsize = 20, fontweight = "bold")
plt.grid(True, which="both", ls="-")

plt.scatter(xi, e1, color = "blue", label = "Eigen 1", s = 150)
plt.scatter(xi, e2, color = "gold", label = "Eigen 2")
plt.scatter(xi, e3, color = "red", label = "Eigen 3")
plt.scatter(xi, e4, color = "green", label = "Eigen 3")

plt.title("Real Eigen Values vs Xi", fontweight = 'bold', fontsize = 25)
plt.ylabel("Eigen Values", fontweight = "bold", fontsize = 20)
plt.xlabel("Xi", fontweight = "bold", fontsize = 20)
plt.legend(loc = "lower left", fontsize = 16, ncol = 2)
plt.xticks(np.arange(round(min(xi)), round(max(xi))+0.05, 0.05), rotation = -90)
plt.xlim(0,3)
plt.ylim(-20, 0.01)
#plt.show()
#plt.savefig("me348_hw_11_eigen_real.png", bbox_inches='tight')

################################################################################################################################


plt.figure(2, figsize = (19, 8))

plt.yticks(fontsize = 20, fontweight = "bold")
plt.xticks(fontsize = 18, fontweight = "bold")
plt.grid(True, which="both", ls="-")

plt.scatter(xi, e1_i, color = "blue", label = "Eigen 1")
plt.scatter(xi, e2_i, color = "gold", label = "Eigen 2")
plt.scatter(xi, e3_i, color = "red", label = "Eigen 3")
plt.scatter(xi, e4_i, color = "green", label = "Eigen 3")

plt.title("Imaginary Eigen Values vs Xi", fontweight = 'bold', fontsize = 25)
plt.ylabel("Eigen Values", fontweight = "bold", fontsize = 20)
plt.xlabel("Xi", fontweight = "bold", fontsize = 20)
plt.legend(loc = "lower right", fontsize = 16, ncol = 2)
plt.xticks(np.arange(round(min(xi)), round(max(xi))+0.1, 0.1), rotation = -50)
plt.xlim(0,3)
#plt.show()
#plt.savefig("me348_hw_11_eigen_imaginary.png", bbox_inches='tight')

'''
################################################### # Input the values here # ##################################################

m1 = 71 # kg
m2 = 455 # kg
k1 = 183888 # N/m
k2 = 17659 # N/m
c1 = 0
L = 0.950 # m
a = -0.05  # m
V = 8 # m/s
v_tld = 1


#------------------------------------------------------------------------------------------------------------------------------#
xi = 2.35
#------------------------------------------------------------------------------------------------------------------------------#


################################################################################################################################

m_ratio = m2/m1
k_ratio = k1/k2
c2 = 2 * xi * np.sqrt(m2 * k2)
c_ratio = c1 / c2
a_tld = a / L
T = L * v_tld / V
k_tld = k2 * T**2 / m2

################################################################################################################################

print("----------------------")
print(f"k_tld:    {k_tld:.4f} nd")
print(f"m_ratio:  {m_ratio:.4f} kg")
print(f"k_ratio:  {k_ratio:.4f} N/m")
print(f"c_ratio:  {c_ratio:.4f} N/ms")
print(f"a_tld:    {a_tld:.4f} nd")
print("----------------------")
print(f"c2:       {c2:.4f} nd")
print("----------------------")

'''

################################################################################################################################

'''


data = pd.read_csv(
    r"C:\Users\cacam\OneDrive\Documents\ME348_python_project\proj_4_1_25_nd_suspension\solution.txt",
                   delimiter='\s+') 

data.columns = ["time_nd", "m1_x_nd", "m1_v_nd", "m2_x_nd", "m2_v_nd", "m1_dx/dt_nd", "m1_dv/dt_nd", 
                "m2_dx/dt_nd", "m2_dv/dt_nd"]

time_nd = data["time_nd"]
m1_x_nd = data["m1_x_nd"]
m1_v_nd = data["m1_v_nd"]
m2_x_nd = data["m2_x_nd"]
m2_v_nd = data["m2_v_nd"]



#------------------------------------------------------------------------------------------------------------------------------#

time_d = T * time_nd
m1_x_d = L * m1_x_nd 
m1_v_d = v_tld * m1_v_nd 
m2_x_d = L * m2_x_nd
m2_v_d = v_tld * m2_v_nd

################################################################################################################################


fig = plt.figure(1, figsize = (28,20))
gs = gridspec.GridSpec(2,2, height_ratios = [1,1], hspace = 0.2, wspace = 0.2)

fig.suptitle("Non-Dimensional", fontweight = 'bold', fontsize = 30, va = "center", y = .93)

axis1 = fig.add_subplot(gs[0,0])
axis1.tick_params(labelsize=22)
axis1.yaxis.get_offset_text().set_fontsize(18)

axis1.scatter(time_nd, m1_x_nd, color = "blue", linewidth = 3)

axis1.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis1.set_xlabel("Time", fontweight = "bold", fontsize = 20)
axis1.set_ylabel("Displacement", fontweight = "bold", fontsize = 20)
#axis1.set_ylim(1,-1)
axis1.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis2 = fig.add_subplot(gs[0,1])
axis2.tick_params(labelsize=22)
axis2.yaxis.get_offset_text().set_fontsize(18)

axis2.scatter(time_nd, m1_v_nd, color = "red", linewidth = 3)

axis2.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis2.set_xlabel("Time", fontweight = "bold", fontsize = 20)
axis2.set_ylabel("Velocity", fontweight = "bold", fontsize = 20)
#axis2.set_ylim(1,-1)
axis2.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis3 = fig.add_subplot(gs[1,0])
axis3.tick_params(labelsize=22)


axis3.scatter(time_nd, m2_x_nd, color = "blue", linewidth = 3)

axis3.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis3.set_xlabel("Time", fontweight = "bold", fontsize = 20)
axis3.set_ylabel("Displacement", fontweight = "bold", fontsize = 20)
axis3.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis4 = fig.add_subplot(gs[1,1])
axis4.tick_params(labelsize=22)

axis4.scatter(time_nd, m2_v_nd, color = "red", linewidth = 3)

axis4.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis4.set_xlabel("Time", fontweight = "bold", fontsize = 20)
axis4.set_ylabel("Velocity", fontweight = "bold", fontsize = 20)
axis4.grid(True, which="both", ls="-")

#plt.savefig("ME_348_HW_11_nd_comf.png", bbox_inches='tight')


################################################################################################################################


fig2 = plt.figure(2, figsize = (28,20))
gs = gridspec.GridSpec(2,2, height_ratios = [1,1], hspace = 0.2, wspace = 0.2)

fig2.suptitle("Dimensional", fontweight = 'bold', fontsize = 30, va = "center", y = .93)

axis1 = fig2.add_subplot(gs[0,0])
axis1.tick_params(labelsize=22)
axis1.yaxis.get_offset_text().set_fontsize(18)

axis1.scatter(time_d, m1_x_d, color = "blue", linewidth = 3)

axis1.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis1.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis1.set_ylabel("Displacement [m]", fontweight = "bold", fontsize = 20)
#axis1.set_ylim(1,-1)
axis1.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis2 = fig2.add_subplot(gs[0,1])
axis2.tick_params(labelsize=22)
axis2.yaxis.get_offset_text().set_fontsize(18)

axis2.scatter(time_d, m1_v_d, color = "red", linewidth = 3)

axis2.set_title("Mass 1", fontweight = 'bold', fontsize = 25)
axis2.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis2.set_ylabel("Velocity [m/s]", fontweight = "bold", fontsize = 20)
#axis2.set_ylim(1,-1)
axis2.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis3 = fig2.add_subplot(gs[1,0])
axis3.tick_params(labelsize=22)


axis3.scatter(time_d, m2_x_d, color = "blue", linewidth = 3)

axis3.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis3.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis3.set_ylabel("Displacement [m]", fontweight = "bold", fontsize = 20)
axis3.grid(True, which="both", ls="-")

#------------------------------------------------------------------------------------------------------------------------------#

axis4 = fig2.add_subplot(gs[1,1])
axis4.tick_params(labelsize=22)

axis4.scatter(time_d, m2_v_d, color = "red", linewidth = 3)

axis4.set_title("Mass 2", fontweight = 'bold', fontsize = 25)
axis4.set_xlabel("Time [s]", fontweight = "bold", fontsize = 20)
axis4.set_ylabel("Velocity [m/s]", fontweight = "bold", fontsize = 20)
axis4.grid(True, which="both", ls="-")

#plt.savefig("ME_348_HW_11_d_comf.png", bbox_inches='tight')

'''