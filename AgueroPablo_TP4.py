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
    coefs = poly.polyfit(x, y, g)
    return poly.polyval(x, coefs)

#Inicio las graficas

#Punto 1A
x = np.array([0.0, 2.0, 3.0,  5.0]) #medición de x
y = np.array([-1.0, 0.0, 2.0, 1.0]) #medición de y
plt.subplot(2,2,1)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,1), 'go-', label="Ajuste")
plt.title("Punto 1A")
plt.xlabel("ejex")
plt.ylabel("ejey")
plt.grid()
plt.legend()

#Punto 1B
plt.subplot(2,2,2)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,2), 'yo-', label="Ajuste")   #Llamo a la funciopn ajuste con grado2 
plt.title("Punto 1B")
plt.xlabel("ejex")
plt.ylabel("ejey")
plt.grid()
plt.legend()

#Punto 2
x = np.array([0.0, 9.85, 14.32, 17.63, 19.34, 22.41]) #medición de x
y = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0]) #medición de y=v**2
plt.subplot(2,2,3)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,1), 'ro-', label="Ajuste")
plt.title("Punto 2")
plt.xlabel("ejex")
plt.ylabel("ejey=v**2")
plt.grid()
plt.legend()

#Punto 3
x = np.array([0.0, 0.69, 1.39, 1.79, 2.08, 2.30]) #medición de x=ln(t)
y = np.array([7.0, 7.38, 8.20, 9.20, 9.80, 11.16]) #medición de y=ln(p(t))
plt.subplot(2,2,4)
plt.plot(x, y, 'bo', label="Mediciones")
plt.plot(x, Ajuste(x,y,1), 'ko-', label="Ajuste")
plt.title("Punto 3")
plt.xlabel("ejex=ln(t)")
plt.ylabel("ejey=ln(p(t))")
plt.grid()
plt.legend()


plt.show()

