import os
os.system ("cls")

import numpy as Guru
#"import numpy as(X)""  (NN Aa Lista) = así se puede usar numpy con otro nombre

v_arreglo = Guru.array( [20,45,32,100]) #aquí se crea el arreglo. Con la función de Numpy hace agregar datos en posiciones vacías.
    #Se asignan los datos (hay 4 elementos)
print( v_arreglo[1])
print( v_arreglo[0])
print( v_arreglo[3])

#Se define arreglo con posiciones vacías -> 7 es el número de posiciones vacías que tendrá el arreglo
nombres = Guru.empty(6, dtype='object')   #Aquí se genera un arreglo vació para que pueda ser rellenado por el usuario
apellidos = Guru.empty(6, dtype='str')    

for i in range(0,5):
    nombres[i] = input("Ingrese su nombre: ")

for i in range(0,apellidos.size):
    apellidos[i] = input("Ingrese su apellido: ")

for i in range(0,5): #aquí se muestra en base al rango del ciclo
    print(f"{nombres[i]} {apellidos[i]} {apellidos[i+1]}")

#mostrar la lista completa de forma linea       