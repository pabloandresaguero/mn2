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
        el = np.arange(a,b+h,h)          #arreglo de errores globales
        y[0] = y0                       #inicializo con el valor y0
        el[0] = 0   		        #calculo de error local
        #bucle de calculos
        for i in range(1,len(x)):
                y[i] = y[i-1] + h * f(x[i-1],y[i-1])    #calculo de y aproximado
                el[i]= m.fabs(y[i]-y[i-1])             #calculo de error global
        print("x",x[i])
        print("yaprox",y[i])
        print("yreal",freal)
        print("e local",el[i])

        # --- graficas ----
        plt.subplot(2, 2, 1)
        plt.title("Gráficas de Y real e Y aproximada - PASO:"+str(h))
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,y, 'ro-', label="euler")
        plt.plot(x[i],freal, 'bo-', label="y real")
        plt.grid()
        plt.legend()
        plt.subplot(2, 2, 2)
        plt.title("Gráficas de errores locales")
        plt.ylabel('error')
        plt.xlabel('x')
        plt.plot(x,el, 'ro-', label="euler")
        plt.grid()
        plt.legend()

        ##    RK4    popppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp

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
                el[i]= m.fabs(y[i]-y[i-1])             #calculo de error global
                print("error",i," ",el[i])
                # --- graficas ----

        plt.subplot(2, 2, 1)
        plt.plot(x,y, 'ko-', label="rk4")
        plt.legend()
        plt.grid()
        plt.subplot(2, 2, 2)
        plt.plot(x,el, 'ko-', label="rk4")
        plt.grid()
        plt.legend()



      

        #lddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd   cambio de paso#        

        h=0.05
        n=(b-a)/h                       #calculo de n
        y[0] = y0                       #inicializo con el valor y0
        el[0] = 0   		        #calculo de error local
        #bucle de calculos
        for i in range(1,len(x)):
                y[i] = y[i-1] + h * f(x[i-1],y[i-1])    #calculo de y aproximado
                el[i]= m.fabs(y[i]-y[i-1])             #calculo de error global
        print("x",x[i])
        print("yaprox",y[i])
        print("yreal",freal)
        print("e local",el[i])

        # --- graficas ----
        plt.subplot(2, 2, 3)
        plt.title("Gráficas de Y real e Y aproximada - PASO:"+str(h))
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,y, 'ro-', label="euler")
        plt.plot(x[i],freal, 'bo-', label="y real")
        plt.grid()
        plt.legend()
        plt.subplot(2, 2, 4)
        plt.title("Gráficas de errores locales")
        plt.ylabel('error')
        plt.xlabel('x')
        plt.plot(x,el, 'ro-', label="euler")
        plt.grid()
        plt.legend()

        ##    RK4    popppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp

        for i in range(1,len(x)):
                k1=f(x[i-1],y[i-1])
                
                k2=f(x[i-1]+(h/2),y[i-1]+(h*k1)/2)
               
                k3=f(x[i-1]+(h/2),y[i-1]+(h*k2)/2)
               
                k4=f(x[i-1] + h, y[i-1]+(h*k3))
              
                y[i] = y[i-1] + ((h/6) * (k1 + 2*k2 + 2*k3 + k4))    #calculo de y aproximado
                      
                el[i]= m.fabs(y[i]-y[i-1])             #calculo de error global
              
                # --- graficas ----

        plt.subplot(2, 2, 3)
        plt.plot(x,y, 'ko-', label="rk4")
        plt.legend()
        plt.grid()
        plt.subplot(2, 2, 4)
        plt.plot(x,el, 'ko-', label="rk4")
        plt.grid()
        plt.legend()
        
        plt.show()



       #****** Fin del Metodo ******         

                

# ---------- defino funiones del ejecicio 1A -------
#funcion para y aproximado
def f(x,y):
     return((-20*y)+(20*m.sin(x))-(m.cos(x)))


# llamada al metodo
metodoEulerRK1(0,2,0.1,1, f, 0.9092974268256817)           #ejecuto el metodo para el apartado 1 - EULER
