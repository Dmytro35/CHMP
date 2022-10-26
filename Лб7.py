import numpy as np

import math

array_x = [2.4,2.6,2.8,3.0,3.2,3.4,3.6]

array_y = [3.526,3.782,3.945,4.043,4.104,4.155]

h = array_x[1] - array_x[0]

array1 = []

array2 = []

array3 = []

array4 = []

for i in range(len(array_y)):

    array1.append(array_y[i] - array_y[i-1])

array1.pop (0)

for j in range(len(array1)):

    array2.append(array1[j] - array1[j-1])

array2.pop (0)

for k in range(len(array2)):

    array3.append(array2[k] - array2[k-1])

array3.pop (0)

for l in range(len(array3)):

    array4.append(array3[l] - array3[l-1])

array4.pop (0)

y1 = 1/ h * (array1[1] - (array2[1]/ 2) + (array3[1] /3) - (array4[1]/4))

y2 = 1/ (h**2) * (array2[1] - array3[1] + 11/12*array4[1])

print ('Перша похідна =', y1)

print ('Друга похідна =', y2)
