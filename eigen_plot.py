import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv(
    r"C:\Users\cacam\OneDrive\Documents\ME348_python_project\proj_3_18_25_nd_res\sol_eigenvalues.txt",
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
#plt.show()
plt.savefig("eigen_real.png", bbox_inches='tight')

################################################################################################################################


plt.figure(2, figsize = (19, 8))

plt.yticks(fontsize = 20, fontweight = "bold")
plt.xticks(fontsize = 18, fontweight = "bold")
plt.grid(True, which="both", ls="-")

plt.scatter(xi, e1_i, color = "blue", label = "Eigen 1")
plt.scatter(xi, e2_i, color = "gold", label = "Eigen 2")
plt.scatter(xi, e3_i, color = "red", label = "Eigen 3")
plt.scatter(xi, e4_i, color = "green", label = "Eigen 3")

#plt.text(0.6, e1_i[0], str(e1_i[0]), bbox={'facecolor': 'lightgrey', 'alpha': 0.5, 'pad': 3}, fontsize = 15, color = "blue")
#plt.text(0.6, e3_i[0], str(e3_i[0]), bbox={'facecolor': 'lightgrey', 'alpha': 0.5, 'pad': 3}, fontsize = 15, color = "red")

plt.scatter(0, e1_i[0], 
            s=700, facecolors='none', edgecolors='lime', linewidths=5, label='Natural Frequency(s)')

plt.scatter(0, e3_i[0], 
            s=700, facecolors='none', edgecolors='lime', linewidths=5)

plt.title("Imaginary Eigen Values vs Xi", fontweight = 'bold', fontsize = 25)
plt.ylabel("Eigen Values", fontweight = "bold", fontsize = 20)
plt.xlabel("Xi", fontweight = "bold", fontsize = 20)
plt.legend(loc = "lower right", fontsize = 16, ncol = 3)
plt.xticks(np.arange(round(min(xi)), round(max(xi))+0.1, 0.1), rotation = -50)
plt.xlim(0,3)
#plt.show()
plt.savefig("eigen_imaginary.png", bbox_inches='tight')


print("Max Imaginary Eigen 1:\n"+ str(e1_i[0]))
print("\nMax Imaginary Eigen 3:\n"+ str(e3_i[0]))