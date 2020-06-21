# Se requiere crear un vector de tamaño 10, completar los valores del vector
# aleatoriamente con números enteros del 0 al 10, para ello deberá investigar
# la función que permita crear números aleatorios.
import os
import random
import numpy 
os.system("cls")

arreglo = numpy.empty(10, dtype='object')

for i in range(10):
    arreglo[i] = int(random.randint(0,10))

print(arreglo)
print("Aquí vamos a ver cuales son pares...")
for i in range(10):
    if(arreglo[i]%2==0):
        print(f"Elemento {i} es par, número elemento: {arreglo[i]}")

mayor = max(arreglo)
print(f"El elemento mayor es: {mayor}\nSu posición en la lista es: {i}")  

#menor = min(arreglo)
#print(f"El elemento menor es: {menor}\nSu posición en la lista es: {i}")  


