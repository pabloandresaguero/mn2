'''
TP2-1 - MNII - 2019
Agüero, Pablo Andrés
'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoEulerRK1(a,b,h,y0, freal):
        # ***** metodo de Euler (RK1) *******

        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        yreal = np.arange(a,b+h,h)      #arreglo de valores de yreal
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        yreal[0] = y0                   #inicializo y real
        e[0]= m.fabs(yreal[0]-y[0])     #calculo de error global
        #bucle de calculos
        for i in range(1,len(x)):
                y[i] = (y[i-1] + h * x[i] * (m.e ** (3 * x[i]))) / 1.5    #calculo de y aproximado
                yreal[i] = freal(x[i],y[i])             #calculo de y real
                e[i]= m.fabs(yreal[i]-y[i])             #calculo de error global

        print(y)
        # --- graficas ----
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
        plt.plot(x,e, 'bo-', label="Error Global")
        plt.grid()
        plt.legend()
        plt.show()

       #****** Fin del Metodo ******         

                



#funcion para y real
def freal(x,y):
    return(((1/5)*x* m.e**(3*x))-((1/25)* m.e**(3*x))+((1/25)* m.e**(-2*x)))        



# llamada al metodo

metodoEulerRK1(0,1,0.25,0, freal)           #ejecuto el metodo para el apartado 1A
