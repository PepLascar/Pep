#ventas del supermercado

#ahora usaremos un arreglo bidimensional(matríz) [0,0] primera coordenada
import numpy as np  

matriz = np.empty([3, 5], dtype='int')  #un arreglo de 3 filas y 5 columnas de tipo de dato integer, estructura que trabaja por filas y columnas.

for i in range (3): #recorro las filas  i = 1 eje
    for j in range (5): #recorro columna j = 2 eje
        ven = int(input(f"Ingrese la venta de la posición {i+1} {j+1}: "))
        matriz[i, j] = ven #en esa posicion acabo de ingresar la venta que quiero registrar

print(matriz)  #print rapido

#para ingresar con un valor random
import random
for i in range (3): #recorro las filas  i = 1 eje
    for j in range (5): #recorro columna j = 2 eje
        #ven = int(input(f"Ingrese la venta de la posición {i+1} {j+1}: "))
        ven = random.randint(1,10000)
        matriz[i, j] = ven #en esa posicion acabo de ingresar la venta que quiero registrar






