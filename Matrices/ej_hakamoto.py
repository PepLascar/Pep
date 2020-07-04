#CASO TIENDAS “HAKAMOTO”
#La tienda “Hakamoto” necesita obtener las estadísticas del mes de enero de sus ventas, para ello
#se debe registrar la información y obtener la suma total y el promedio de ventas de todas las
#ventas del mes.
#Se debe registrar SOLO las ventas de 5 vendedores que trabajan en turnos en 3 sucursales de la
#tienda.
#las sucursales son: Santiago, Rancagua y Temuco.
#MATRIZ TRIDIMENSIONAL FILA - COLUMNA - PROFUNDIDAD
#3x5 (3 sucursales el profe pone primero)

import numpy as np  
tienda = np.empty([3, 5], dtype='int')
acum = 0
#tarea SOLAMENTE LLENAR --> tarea específica
for i in range(3):  #sucursal
    for j in range(5):  #vendedores
        venta = int(input(f"Ingrese venta del vendedor {i} {j}:"))  
        tienda [i, j] = venta
print(tienda)


#Tarea: sumar y promediar el total de ventas, debo recorrer y acumular  --> tarea específica
for i in range(3):  
    for j in range(5):  
        acum = acum +  venta[i,j]

#Tarea: mostrar los totales
print(f"La suma total es {acum}")
promedio = acum / 15