'''
TP1 - MNII - 2019
Agüero, Pablo Andrés
'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoEulerRK1(a,b,h,y0, f, freal):
        # ***** metodo de Euler (RK1) *******

        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        yreal = np.arange(a,b+h,h)      #arreglo de valores de yreal
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        el = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        yreal[0] = y0                   #inicializo y real
        el[0] = 0   		        #calculo de error local
        e[0]= m.fabs(yreal[0]-y[0])     #calculo de error global
        #bucle de calculos
        for i in range(1,len(x)):
                y[i] = y[i-1] + h * f(x[i-1],y[i-1])    #calculo de y aproximado
                yreal[i] = freal(x[i],y[i])             #calculo de y real
                e[i]= m.fabs(yreal[i]-y[i])             #calculo de error global
                el[i]= m.fabs(y[i]-y[i-1])             #calculo de error global

        print("x",x[i])
        print("yaprox",y[i])
        print("yreal",yreal[i])
        print("e global",e[i])
        print("e local",el[i])

        # --- graficas ----
        plt.subplot(1, 2, 1)
        plt.title("Gráficas de Y real e Y aproximada")
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,y)
        plt.plot(x,yreal)
        plt.subplot(1, 2, 2)
        plt.title("Gráficas de errores")
        plt.ylabel('error')
        plt.xlabel('x')
        plt.plot(x,e)
        plt.show()

       #****** Fin del Metodo ******         

                

# ---------- defino funiones del ejecicio 1A -------
#funcion para y aproximado
def f(x,y):
     return(1 + ( x - y )**2)
#funcion para y real
def freal(x,y):
    return(x + 1 / (1-x))        

# ---------- defino funiones del ejecicio 1B -------
#funcion para y aproximado
def f2(x,y):
     return((x* m.e **(3*x))-(2*y))
#funcion para y real
def freal2(x,y):
    return(((1/5)*x* m.e**(3*x))-((1/25)* m.e**(3*x))+((1/25)* m.e**(-2*x)))        



# llamada al metodo

metodoEulerRK1(2,3,0.1,1, f, freal)           #ejecuto el metodo para el apartado 1A

metodoEulerRK1(0,1,0.1,0, f2, freal2)         #ejecuto el metodo para el apartado 1B
