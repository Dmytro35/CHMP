import numpy as np

A = np.matrix('2 -1 1; 3 4 -2; 1 -3 1')

B = np.matrix('5; -3; 4')

print('A=', A)

print('B=',B)

A_inv = np.linalg.inv(A)

print(A_inv)

X = A_inv.dot(B)

print('X=',X)