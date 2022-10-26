import math

x1 = 66 # sqrt(x1 )

x2=7/3 

x1_1 = 8.12 

x2_2 = 2.33 

def f (x1, x1_1, x2, x2_2):

    dx1 = abs((math.sqrt(x1) - x1_1)/ math.sqrt (x1))

    dx2 = abs((x2 - x2_2)/x2)

    if (dx1>dx2):

        print ("Друга рівність точніше")

    else:

        print("Перша рівність точніше")

f(x1,x1_1,x2,x2_2)