import numpy as np

a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2; 4 3 -2 -1')

a_det = np.linalg.det(a)#Визначник матриці

print(format(a_det, '.9g'))