# Se requiere crear un vector de tamaño 10, completar los valores del vector
# aleatoriamente con números enteros del 0 al 10, para ello deberá investigar
# la función que permita crear números aleatorios.
import os
import random
import numpy 
os.system("cls")

arreglo = []

for i in range(10):
    numero_rand = int(random.randint(0,10))
    arreglo.append(numero_rand)

print(arreglo)
print("Aquí vamos a ver los VALORES en INDICES pares...")
for i in range(10):
    if(i%2==0):
        print(f"Elemento {arreglo[i]}, posición elemento: {[i]}")

mayor = max(arreglo)
indice_mayor = arreglo.index(mayor)
print(f"El elemento mayor es: {mayor}\nSu posición en la lista es: {indice_mayor}")  

menor = min(arreglo)
indice_menor = arreglo.index(menor)
print(f"El elemento menor es: {menor}\nSu posición en la lista es: {indice_menor}") 

#menor = min(arreglo)
#print(f"El elemento menor es: {menor}\nSu posición en la lista es: {i}")  