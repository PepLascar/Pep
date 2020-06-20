#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
import os
os.system("cls")

print("Ingrese 6 números para su boleto de lotería: ")
import numpy as lista
num_loteria = lista.empty(6, dtype='int')
for i in range(6):
    num_loteria[i] = int(input("Número: "))

num_loteria.sort()
print(f"Los números de su boleto son:\n{num_loteria}\nGracias ")


#¿cómo ordenarlos de mayor a menor?, me imaginaría que aplicandole a la lista con un comando "sort" o algo así, 
#que de momento no cacho como implementarlo

print(f"Los números de su boleto son:\n{num_loteria[::-1]}\nGracias ")