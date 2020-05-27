# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:15:10 2020

@author: Quitoq
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


datos1= np.genfromtxt ('DATOS 1.txt', delimiter=',')
datos2 =  np.genfromtxt ('DATOS 2.txt', delimiter=',')
datos3 =  np.genfromtxt ('DATOS 3.txt', delimiter=',')
datos4 =  np.genfromtxt ('DATOS 4.txt', delimiter=' ')

#Actividad 1

vs = datos1[:,1]
frec = datos1[:,0]
omega = frec*np.pi*2

plt.figure(1)
plt.plot(omega,vs,"o")
plt.xlabel ('Omega [Hz]')
plt.ylabel ('Voltaje secundario [V]')
plt.title('Grafico de respuesta voltaje vs omega')
p=np.polyfit(omega, vs, 1)
plt.plot(omega,p[0]*omega+p[1],'r-',label='Regresion lineal')

matrizcov = np.corrcoef(omega, vs)
cov_xy = matrizcov[0,1]
rcuadrado = cov_xy**2

#Testeo de comportamiento funcion pearson de matriz de covarianza por las dudas.
#No tiene funcion alguna dentro del tp, solo sirve para chequar la funcion r^2


cov = np.corrcoef(omega,10*omega)
cov1= cov[0,1]
rcuadrado1 = cov1**2

'HAY UNA FUNCION INTEGRADA MAS FACIL'
'ESTA EN LA SIGUIENTE WEB'
'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html'


#Actividad 2

vsprimario = datos2[:,0]
vsecundario = datos2[:,1]

plt.figure (2)
plt.plot (vsprimario,vsecundario,"o")

p=np.polyfit(vsprimario, vsecundario, 1)
plt.plot(vsprimario,p[0]*vsprimario+p[1],'r-',label='Regresion lineal')
plt.xlabel('Voltaje primario [V]')
plt.ylabel('Voltaje secundario [V]')
plt.title('Voltaje primario vs secundario')

pendiente , ordenada = np.polyfit (np.log(vsprimario),np.log(vsecundario),1) #Busco pendiente y ordenada. Esta en escala logaritmica
print (pendiente)
print (ordenada)
plt.figure(3)
plt.title ('Comparacion sin nucleo vs con nucleo. Escala logaritmica ')
plt.loglog (vsprimario,vsecundario,'--')

#Actividad 3

vs3primario = datos3[:,0]
vs3ecundario = datos3[:,1]

plt.figure (4)
plt.plot (vs3primario,vs3ecundario,"o")

p=np.polyfit(vs3primario, vs3ecundario, 1)
plt.plot(vs3primario,p[0]*vs3primario+p[1],'r-',label='Regresion lineal')
plt.xlabel('Voltaje primario [V]')
plt.ylabel('Voltaje secundario [V]')

pendiente3 , ordenada3 = np.polyfit (np.log(vs3primario),np.log(vs3ecundario),1) #Busco pendiente y ordenada. Esta en escala logaritmica
print (pendiente3)
print (ordenada3)

plt.figure(3)
plt.loglog (vs3primario,vs3ecundario,'--')
plt.xlabel('Voltaje del Primario [V]')
plt.ylabel('Voltaje del secundario [V]')
#Actividad 4

tiempo = datos4[:,0]
vs4primario = datos4[:,1]
vs4ecundario = datos4[:,2]

plt.figure(5)
plt.plot(tiempo, vs4primario)
plt.plot(tiempo, vs4ecundario)
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (V)')



