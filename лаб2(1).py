import numpy as np

from math import fabs

 
def f( x ):
    return 2*x**4+4*x**3-x**2-3*x-1
a = 0
b = 1
eps = 0.0001
 
def dihotomia( a, b, eps ):
    abs = ( a + b ) / 2
    if ( fabs( f(a) - f(b) ) <= eps ) or ( fabs( f(abs) ) <= eps ):
        return ( a + b ) / 2
    if ( f( a )*f( abs ) <= 0 ):
        return dihotomia( a, abs, eps )
    else:
        return dihotomia( abs, b, eps )
        

print('Корінь рівняння x =', dihotomia ( a, b, eps ) )
