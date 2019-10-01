'''
TP1 - MNII - 2019
Agüero, Pablo Andrés
'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt


plt.ion()

# valores de t, yreal, yaprox, error global del punto A)
t=[2,2.25,2.5,2.75,3]
yreal=[1,1.45,1.833,2.178,2.5]
yaprox=[1,1.5,1.89,2.233,2.55]
eglobal=[0,0.05,0.057,0.055,0.05]

#gráfica del de Y real y aproximado del punto A)
plt.subplot(2, 2, 1)
plt.title("A) Gráficas de Y real e Y aproximada")
plt.ylabel('y')
plt.xlabel('t')
plt.plot(t,yreal)
plt.plot(t,yaprox)

#gráfica del error del método utilizado en el punto A)
plt.subplot(2, 2, 2)
plt.title("Gráfica de error")
plt.ylabel('error gobal')
plt.xlabel('t')
plt.plot(t,eglobal)

#valores de t, yreal, yaprox, error global del punto B)
t=[0,0.25,0.5,0.75,1]
yreal=[0,0.045,0.284,1.053,3.219]
yaprox=[0,0,0.132,0.626,2.092]
eglobal=[0,0.045,0.152,0.427,1.127]

#gráfica del de Y real y aproximado del punto B)
plt.subplot(2, 2, 3)
plt.title("B) Gráficas de Y real e Y aproximada")
plt.ylabel('y')
plt.xlabel('t')
plt.plot(t,yreal)
plt.plot(t,yaprox)

#gráfica del error del método utilizado en el punto B)
plt.subplot(2, 2, 4)
plt.title("Gráfica de error")
plt.ylabel('error gobal')
plt.xlabel('t')
plt.plot(t,eglobal)



