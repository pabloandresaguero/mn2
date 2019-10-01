#'''
#TP3-2 - MNII - 2019
#Agüero, Pablo Andrés
#'''

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.array([0.0, 2.0, 3.0,  5.0])
y = np.array([-1.0, 0.0, 2.0, 1.0])
z = np.polynomial.polynomial.polyfit(x, y, 1)
print(z)
f = np.poly1d(z)
xx = linspace(0, max(x), 500)
pylab.plot(xx, pn(xx),'-g', xx, pq(xx),'-b')

fig = plt.figure()
ax  = fig.add_subplot(111)
plt.plot(x, y, 'bo', label="Data")
plt.plot(x,f(x), 'b-',label="Polyfit")
plt.show()
