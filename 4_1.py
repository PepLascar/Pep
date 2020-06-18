import os
os.system ("cls")

import numpy
#"import numpy as(X)""  (NN Aa Lista) = así se puede usar numpy con otro nombre

v_arreglo = numpy.array( [20,45,32,100]) #aquí se crea el arreglo. Con la función de Numpy hace agregar datos en posiciones vacías.
    #Se asignan los datos (hay 4 elementos)
print( v_arreglo[1])
print( v_arreglo[0])
print( v_arreglo[3])

#Se define arreglo con posiciones vacías -> 7 es el número de posiciones vacías que tendrá el arreglo
nombres = numpy.empty(7, dtype='object')   #Aquí se genera un arreglo vació para que pueda ser rellenado por el usuario


for i in range(0,7):
    nombres[i] = input("Ingrese su nombre: ")

for i in range(7): #aquí se muestra en base al rango del ciclo
    print(nombres[i])

#mostrar la lista completa de forma lineal
print(nombres)