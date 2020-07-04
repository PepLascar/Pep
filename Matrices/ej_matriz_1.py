import numpy as np  
acum = 0
matriz = np.empty([3, 5], dtype='int') 

import random
for i in range (3): #recorro las filas  i = 1 eje
    for j in range (5): #recorro columna j = 2 eje
        #ven = int(input(f"Ingrese la venta de la posición {i+1} {j+1}: "))
        ven = random.randint(1,10000)
        matriz[i, j] = ven #en esa posicion acabo de ingresar la venta que quiero registrar

print(matriz)

#como hago para obtener el promedio de las ventas de la tienda
#1° recorrer la matriz para acceder a cada elemento
#2° sumar cada elemento en un acumulador,.. para acumular la suma
#3° fuera del ciclo calcular el promedio y mostrarlo por pantalla
#
# tarea específica: obtener el promedio

for i in range(3):
    for j in range(5):
        acum = acum + matriz[i,j]

promedio = acum // 15 #relleno por 15 por que ya me se las posiciones de la matriz 3x5 posiciones

print(promedio)