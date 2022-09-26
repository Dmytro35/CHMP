import numpy as np

A = np.matrix('1 2 -3; 0 1 2; 0 0 1')

A_inv = np.linalg.inv(A)#обернена матриця

print(A_inv)