'''
TP2-2 - MNII - 2019
Agüero, Pablo Andrés
'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoEulerRK4(a,b,h,y0,f,fr):
        # ***** metodo RK$ *******

        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        yr = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        yr[0] = y0                       #inicializo con el valor y0
        e[0]= 0     #calculo de error global
        #bucle de calculos
        for i in range(1,len(x)):
                k1=f(x[i-1],y[i-1])
                k2=f(x[i-1]+(h/2),y[i-1]+(h*k1)/2)
                k3=f(x[i-1]+(h/2),y[i-1]+(h*k2)/2)
                k4=f(x[i-1] + h, y[i-1]+(h*k3))
                y[i] = y[i-1] + ((h/6) * (k1 + 2*k2 + 2*k3 + k4))    #calculo de y aproximado
                yr[i] = fr(x[i])
                e[i]= m.fabs(yr[i]-y[i])             #calculo de error local
        print (e)
        print (k4)
       #****** Fin del Metodo ******         

                
#funcion f a aproximar
def f(x,y):
     return    (m.cos(2*x)+m.sin(3*x))
#funcion f a aproximar
def fr(x):
     return    (((1/2)*m.sin(2*x)) - ((1/3)* m.cos(3*x)) + 4/3)


# llamada al metodo

metodoEulerRK4(0,1,0.5,1,f,fr)

