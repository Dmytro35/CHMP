import matplotlib.pyplot as plt 
from scipy.interpolate import UnivariateSpline 
import numpy as np 
 
x = [0.5,0.7,1,1.4,1.9] 
y = [1.83,2.14,1.46,1.15,3.28] 
 
spl = UnivariateSpline(x, y) 
xs = np.linspace(0.5, 1.9, 1000) 
plt.plot(x,y,'bo', xs, spl(xs), 'r') 
plt.show() 

