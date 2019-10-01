#'''
#TP4 - MNII - 2019
#Aguero, Pablo Andrés
#'''

#importar librerias
import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import math as m


def Ajuste(x,y,g):
    #Función que calcula el ajuste.
    #Parametros: x,y: mediciones. g: grado
    coefs = poly.polyfit(x, y, g)           #cálculos de coeficientes a0 y a1
    print("a0="+str(coefs[0]))              #muestro el coeficiente a0
    print("a1="+str(coefs[1]))              #muestro el coeficiente a1
    print("--------------------------")
    return poly.polyval(x, coefs)           #retorna puntos de la estimación (los puntos de x evaluados en la función Y=a0+a1X)

#Inicio las graficas

#Punto 1A
x = np.array([0.0, 2.0, 3.0,  5.0]) #medición de x
y = np.array([-1.0, 0.0, 2.0, 1.0]) #medición de y
plt.subplot(1,3,1)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,1), 'go-', label="Recta")
plt.plot(x, Ajuste(x,y,2), 'yo-', label="Parábola")   #Llamo a la funciopn ajuste con grado2 
plt.title("Punto 1")
plt.xlabel("ejex")
plt.ylabel("ejey")
plt.grid()
plt.legend()


#Punto 2
x = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0]) #medición de x
y = np.array([0.0, 9.85, 14.32, 17.63, 19.34, 22.41]) #medición de y
plt.subplot(1,3,2)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,1), 'ro-', label="Ajuste")
plt.title("Punto 2")
plt.xlabel("ejex")
plt.ylabel("ejev")
plt.grid()
plt.legend()

#Punto 3
x = np.array([1.0, 2.0, 4.0, 6.0, 8.0, 10.0]) #medición de x=ln(t)
y = np.array([1100.0, 1600.0, 3650.0, 9900.0, 18000.0, 70100.0]) #medición de y=ln(p(t))
plt.subplot(1,3,3)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,1), 'ko-', label="Ajuste")
plt.title("Punto 3")
plt.xlabel("Tiempo")
plt.ylabel("número de células")
plt.grid()
plt.legend()


plt.show()

