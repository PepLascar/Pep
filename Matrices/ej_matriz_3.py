#Crear un Arreglo [10][4] en el cual simule un bus, tendrá que darle de forma
#automática los números de asiento y luego mostrarlo por pantalla
#de la siguiente forma

import numpy as np
cont = 0 
m = np.empty([10,4], dtype='int')
for i in range (10):
    for j in range (4):
        cont = cont + 1
        m[i, j] = cont

for i in range(10):
    print(f"{m[i,0]}\t{m[i,1]}\t\t{m[i,2]}\t{m[i,3]} ")

