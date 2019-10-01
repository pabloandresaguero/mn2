import numpy as np
import matplotlib.pyplot as plt
import math as m

def metodoEulerRK1(a,b,h,y10,y20, f1, f2, fr1, fr2):
        # ***** metodo de Euler (RK1) 
        n=(b-a)/h 
        x = np.arange(a,b+h,h)
        y1 = np.arange(a,b+h,h)
        y2 = np.arange(a,b+h,h)
        yr1 = np.arange(a,b+h,h)
        yr2 = np.arange(a,b+h,h)
        e1 = np.arange(a,b+h,h)
        el1 = np.arange(a,b+h,h)
        e2 = np.arange(a,b+h,h)
        el2 = np.arange(a,b+h,h)
        y1[0] = y10
        y2[0] = y20
        yr2[0] = y20
        yr1[0] = y10
        el1[0] = 0   		        
        e1[0]= 0
        e2[0] = 0   		        
        el2[0]= 0

        for i in range(1,len(x)):
                y1[i] = y1[i-1] + h * (f1(x[i-1],y1[i-1],y2[i-1]))
                y2[i] = y2[i-1] + h * (f2(x[i-1],y1[i-1],y2[i-1]))
                yr1[i] = fr1(x[i],y1[i])
                yr2[i] = fr2(x[i],y2[i]) 
                e1[i]= m.fabs(yr1[i]-y1[i])
                el1[i]= m.fabs(y1[i]-y1[i-1])
                e2[i]= m.fabs(yr2[i]-y2[i])
                el2[i]= m.fabs(y2[i]-y2[i-1])

        print(x)
        print(y1)
        print(yr1)
        print(e1)
        print(el1)
        print("+++++++++++++++++++")
        print(x)
        print(y2)
        print(yr2)
        print(e2)
        print(el2)


def f1(x,y1,y2):
    ##        return y2
    return ((-500*y1)+(6880*y2))

def f2(x,y1,y2):
    ##        return ((3*y2)-(2*y1)+x)
    return ((36*y1)-(500*y2))
    
def fr1(x,y):
    return (83*(m.exp(-2*x)))

def fr2(x,y):
        return (6*(m.exp(-2*x)))

metodoEulerRK1(0,1,0.001,83.0,6.0, f1, f2, fr1,fr2)



