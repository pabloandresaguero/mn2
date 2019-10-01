#'''
#TP3-1 - MNII - 2019
#Agüero, Pablo Andrés
#'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoAdamsBashford(a,b,h,y0, faprox,freal):
        # ***** metodo de Euler (RK1) *******
        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        yreal = np.arange(a,b+h,h)      #arreglo de valores de yreal
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        el = np.arange(a,b+h,h)          #arreglo de errores locales
        y[0] = y0                       #inicializo con el valor y0
        yreal[0] = y0                   #inicializo y real
        e[0]= m.fabs(yreal[0]-y[0])     #calculo de error global
        el[0]= 0     #calculo de error locales

        # ***** Primer punto inicializo con metodo de Euler (RK1) *******
        y[1] = (y[0] + h * faprox(x[0],y[0]))    #calculo de y aproximado para el primer punto
        yreal[1] = freal(x[1],y[1])             #calculo de y real
        e[1]= m.fabs(yreal[1]-y[1])             #calculo de error global
        el[1]= m.fabs(y[1]-y[0])             #calculo de error local
        
        #bucle de calculos para Adans Bashford
        for i in range(2,len(x)):
                y[i] = y[i-1] + (h/2) * (3 * faprox(x[i-1],y[i-1]) - faprox(x[i-2],y[i-2]))   #calculo de y aproximado
                yreal[i] = freal(x[i],y[i])             #calculo de y real
                e[i]= m.fabs(yreal[i]-y[i])             #calculo de error global
                el[i]= m.fabs(y[i]-y[i-1])             #calculo de error local

        #muestro los valores        
        print("Valores de X",x)
        print("Yaprox",y)
        print("Yreal",yreal)
        print("ErrorGlobal",e)
        print("ErrorLocal",el)
        
        # --- graficas ----
        plt.subplot(1, 2, 1)
        plt.title("Gráficas de Y real e Y aproximada - PASO: " + str(h))
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,y, 'bo-', label="Y aproximado")
        plt.plot(x,yreal, 'ro-', label="Y real")
        plt.grid()
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.title("Gráfica de errores globales")
        plt.ylabel('error')
        plt.xlabel('x')
        plt.plot(x,e, 'bo-', label="error global")
        plt.plot(x,el, 'ro-', label="error local")
        plt.grid()
        plt.legend()
        plt.show()

       #****** Fin del Metodo ******         

                

#funcion para y aproximado
def faprox(x,y):
    return(2*x*(1+(x**2))**(-1))        


#funcion para y real
def freal(x,y):
    return(m.log(1+(x**2)))        



# llamada al metodo
metodoAdamsBashford(0,1,0.25,0,faprox,freal)           #ejecuto el metodo para el apartado 1A Adams Bashford
