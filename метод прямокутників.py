from scipy import integrate

import math

eps = 0.0001

def f1(x):

    return 1/math.sqrt(x+2.5)

def left_rec(f1,a,b,n):

    h=(b-a)/n

    sum=0

    for i in range(0,n):

        sum+=f1(a+i*h)

    return sum*h

v,err = integrate.quad(f1,0.32,0.66)

if abs(left_rec(f1,0.32,0.66,2*10) - left_rec(f1,0.32,0.66,10))/3. <=eps:

    print("left rectangle:",round (left_rec(f1,0.32,0.66,10), 5))

def right_rec(f1,a,b,n):

    h=(b-a)/n

    sum=0

    for i in range(1,n+1):

        sum+=f1(a+i*h)

    return sum*h

print("right rectangle:",round (right_rec(f1,0.32,0.66,10), 5))

def aver_rec(f1,a,b,n):

    h=0.034

    sum=0

    for i in range(0,n):

        sum+=f1(a+i*h)

    return sum*h

print("average rectangle:",round (aver_rec(f1,0.32,0.66,10), 5))

print("Check for the rectangle method= ",round (v, 5))