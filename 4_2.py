import numpy as lista

arreglo = lista.empty(5, dtype='object') #crear arreglo, object = tipo de dato genérico

for i in range(1): #recorrido para rellenar arreglo
    nombre = input("Ingrese su nombre: ")
    arreglo[i] = nombre

for i in range(1): #mostrar recorrido del arreglo
    print(f"Su nombre es {arreglo[i]}")

    import random #incorporar numero al azar
    num = random.randint(0,100) #esta funcion randint me entre un n° aleatorio entre 0 y 100
    print(num)