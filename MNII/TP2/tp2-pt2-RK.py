'''
TP2-2 - MNII - 2019
Agüero, Pablo Andrés
'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoEulerRK4(a,b,h,y0,f):
        # ***** metodo RK$ *******

        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        e[0]= 0     #calculo de error global
        #bucle de calculos
        for i in range(1,len(x)):
                k1=f(x[i-1],y[i-1])
                k2=f(x[i-1]+(h/2),y[i-1]+(h*k1)/2)
                k3=f(x[i-1]+(h/2),y[i-1]+(h*k2)/2)
                k4=f(x[i-1] + h, y[i-1]+(h*k3))
                y[i] = y[i-1] + ((h/6) * (k1 + 2*k2 + 2*k3 + k4))    #calculo de y aproximado
                e[i]= m.fabs(y[i]-y[i-1])             #calculo de error local
        return e[b]
       #****** Fin del Metodo ******         

                
#funcion f a aproximar
def f(x,y):
     return    (x * (m.e ** (3 * x))) - ( 2 *y )

# llamada al metodo
h=1  #empieza el calculo con h=1

while (metodoEulerRK4(0,1,h,0, f)>(1*(10**(-4)))):
        #estructura de repeticion que busca el h
        print("paso",h,":")
        print("error",metodoEulerRK4(0,1,h,0, f))           
        h=h/10
print("paso",h)
print("error",metodoEulerRK4(0,1,h,0, f))
