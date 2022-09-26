import numpy as np

A = np.matrix('1 2 3 4; 3 -1 2 5; 1 2 3 4; 1 3 4 5')

rank = np.linalg.matrix_rank(A)#визначення рангу матриці

print(rank)