'''
TP2-2 - MNII - 2019
Agüero, Pablo Andrés
'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoEulerRK4(a,b,h,y0,f, freal):
        # ***** metodo de Euler (RK1) *******

        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        el = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        e[0]= 0     #calculo de error global
        el[0]= 0     #calculo de error global
        yreal = np.arange(a,b+h,h)      #arreglo de valores de yreal
        yreal[0] = y0                   #inicializo y real

        #bucle de calculos
        for i in range(1,len(x)):
                k1=f(x[i-1],y[i-1])
                print("k1",k1)
                k2=f(x[i-1]+(h/2),y[i-1]+(h*k1)/2)
                print("k2",k2)
                k3=f(x[i-1]+(h/2),y[i-1]+(h*k2)/2)
                print("k3",k3)
                k4=f(x[i-1] + h, y[i-1]+(h*k3))
                print("k4",k4)
                y[i] = y[i-1] + ((h/6) * (k1 + 2*k2 + 2*k3 + k4))    #calculo de y aproximado
                print("Y",i," ",y[i])        
                e[i]= m.fabs(y[i]-y[i-1])             #calculo de error global
                print("error",i," ",e[i])
                yreal[i] = freal(x[i],y[i])
                print("y real",i," ",yreal[i])
                el[i]= m.fabs(yreal[i]-y[i])             #calculo de error global
                print("error global",i," ",el[i])
                # --- graficas ----
        plt.title("Runge Kuta 4")
        plt.subplot(1, 2, 1)
        plt.title("Gráficas de Y real e Y aproximada - H="+str(h))
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,y, 'bo-', label="Y aproximado")
        plt.plot(x,yreal, 'ro-', label="Y real")
        plt.legend()
        plt.grid()
        plt.subplot(1, 2, 2)
        plt.title("Gráficas de errores")
        plt.ylabel('error')
        plt.xlabel('x')
        plt.plot(x,el, 'ro-', label="Error Global")
        plt.grid()
        plt.legend()
        plt.show()
       #****** Fin del Metodo ******         

#funcion para y real
def freal(x,y):
    return(((1/5)*x* m.e**(3*x))-((1/25)* m.e**(3*x))+((1/25)* m.e**(-2*x)))
                
#funcion f a aproximar
def f(x,y):
     return    (x * (m.e ** (3 * x))) - ( 2 *y )

# llamada al metodo
metodoEulerRK4(0,1,0.1,0, f, freal)        
