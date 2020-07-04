import numpy as np
numeros = 0 
matriz = np.empty([3,6], dtype='int')

for i in range (3):
    for j in range (6):
        try:
            numeros = input(f"Ingrese número para la posición de la matriz: {i} {j}:  ")
        except:
            print("ingre alid")
        matriz[i, j] = numeros

print(matriz)

