#'''
#TP3-2 - MNII - 2019
#Agüero, Pablo Andrés
#'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

       
def metodoHuen(a,b,h,y0,faprox,Ep,itMax):
        
        n=(b-a)/h                       #calculo de n
        x = np.arange(a,b+h,h)          #arreglo de valores de x
        y = np.arange(a,b+h,h)          #arreglo de valores de yaprox
        e = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        e[0]= 0                         #calculo de error local
        
       
        
        #bucle de calculos huen
        for i in range(1,len(x)):
                # ***** Predictor metodo de Euler (RK1) *******
                y[i] = (y[i-1] + h * faprox(x[i-1],y[i-1]))    #calculo de y aproximado para el primer punto
                it=0                                           #inicio iterador para el punto buscando
                yit=y[i-1]
                # ***** Corrector metodo Trapecio                
                while ((m.fabs(y[i]-yit)>Ep) and (it<itMax)):
                     yit=y[i]
                     y[i] = (y[i-1] + ((h/2) * ( faprox(x[i-1],y[i-1]) + faprox(x[i],y[i]) )))     # Corrijo Yaprox con trapecio
                     print("X="+str(x[i])+" - Y="+str(y[i])+" - It="+str(it)+" error: ",(m.fabs(y[i]-y[i-1])))      # Muestra el valor del error y del numero de iteracion
                     it += 1
                e[i]= m.fabs(y[i]-y[i-1])               #calculo de error local

        #muestro los valores        
        print("Valores de X",x)
        print("Yaprox",y)
        print("ErrorLocal",e)
        
        # --- graficas ----
        plt.subplot(1, 2, 1)
        plt.title("Gráfica de Y aproximada - PASO: " + str(h))
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,y, 'b', label="Y aproximado")
        plt.grid()
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.title("Gráfica de errores locales")
        plt.ylabel('error')
        plt.xlabel('x')
        plt.plot(x,e, 'r', label="error")
        plt.grid()
        plt.legend()
        plt.show()

       #****** Fin del Metodo ******         

                

#funcion para y aproximado
def faprox(x,y):
    return((2*(y/x))+((x**2)*((m.e)**x)))        

  
# llamada al metodo
metodoHuen(1,2,0.1,0,faprox,0.01,100)           #ejecuto el metodo para el apartado 2b HUEN
