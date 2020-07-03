import numpy
import random
v_arreglo = []
cont = 0

for i in range(8):
    numero_rand = int(random.randint(1,8))  #crear una lista con números aleatorios
    v_arreglo.append(numero_rand)
print(v_arreglo)

for i in range(len(v_arreglo)):  #recorrer el largo del arreglo
    if(v_arreglo[i] == 3):
        cont = cont + 1
print(f"La cantidad de ese determinado número que contiene la lista aleatoria es:\n {cont}")