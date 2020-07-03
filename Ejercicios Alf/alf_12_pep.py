import numpy 
cont = 0
cont_2 = -2
matriz = numpy.empty([2,3], dtype='int')
for i in range (2):
    for j in range(3):
        cont = cont + 1
        matriz[i, j] = cont
    
print(matriz)

matriz_2 = numpy.empty([3, 2], dtype='int')
for i in range(3):
    for j in range(2):
        cont_2 = cont_2 + 1
        matriz_2[i, j] = cont_2

print(matriz_2)
