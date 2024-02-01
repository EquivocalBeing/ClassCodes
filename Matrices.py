####################################################################################################################
#
# import required packages
# Set A matrix
# b if needed to find the x matrix
#
####################################################################################################################

import numpy as np
import math
import warnings
from fractions import Fraction


A = np.array([[2, 3, 2],
            [-1, -3, -8],
            [-3, 2, -7]])

b = np.array([[-2],
            [-2],
             [2]])

print('A:' + '\n' + str(A) + '\n' )
print('B:' + '\n' + str(b) + '\n')
print()
####################################################################################################################
#
#Finding Transpose of A
#
####################################################################################################################
trans = np.transpose(A)
print('A^T:' + '\n' + str(trans) + '\n')


####################################################################################################################
#
# Finding Determinate of A
#
####################################################################################################################

det = np.linalg.det(A)
print('Determinate of A:' + '\n' +str(round(det, 2))+ '\n')

####################################################################################################################
#
# Finding the Inverse of A
#
####################################################################################################################

if det != 0:
    warnings.simplefilter('ignore')
    A_inv = np.linalg.inv(A)
    print('A^-1:' +'\n' + str(np.around(A_inv, 2)) + '\n')
else:
    
    print('A is not invertible')

####################################################################################################################
#
# Finding the x matrix
#
####################################################################################################################

if det != 0:
    x = A_inv @ b
print('x:' + '\n' +str(x))

####################################################################################################################
#
# Using Cramer's Rule for a 3x3
#
####################################################################################################################

coeff = [[2, 3, 2, -2],
        [-1, -3, -8, -2],
        [-3, 2, -7, 2]]


d = [[coeff[0][0], coeff[0][1], coeff[0][2]],
    [coeff[1][0], coeff[1][1], coeff[1][2]],
    [coeff[2][0], coeff[2][1], coeff[2][2]]]

d1 = [[coeff[0][3], coeff[0][1], coeff[0][2]],
    [coeff[1][3], coeff[1][1], coeff[1][2]],
    [coeff[2][3], coeff[2][1], coeff[2][2]]]

d2 = [[coeff[0][0], coeff[0][3], coeff[0][2]],
    [coeff[1][0], coeff[1][3], coeff[1][2]],
    [coeff[2][0], coeff[2][3], coeff[2][2]]]

d3 = [[coeff[0][0], coeff[0][1], coeff[0][3]],
    [coeff[1][0], coeff[1][1], coeff[1][3]],
    [coeff[2][0], coeff[2][1], coeff[2][3]]]


D = np.linalg.det(d)
D1 = np.linalg.det(d1)
D2 = np.linalg.det(d2)
D3 = np.linalg.det(d3)

print("D is : ", str(round(D, 2)))
print("D1 is : ", str(round(D1, 2)))
print("D2 is : ", str(round(D2, 2)))
print("D3 is : ", str(round(D3, 2)))


if D != 0:

    x = D1 / D
    y = D2 / D

    z = D3 / D 

    print("Value of x is : ", x)
    print("Value of y is : ", y)
    print("Value of z is : ", z)

else:
    if (D1 == 0 and D2 == 0 and
        D3 == 0):
        print("Infinite solutions")
    elif (D1 != 0 or D2 != 0 or
        D3 != 0):
        print("No solutions")
        
