#Genere un vector con 100 datos de forma aleatoria, los datos deben estar en el rango (0-1000), una vez generado el vector, obtenga y muestre 
#la cantidad de elementos que son números pares y la cantidad de elementos que son impares

import numpy
import random
vector = []
cont_par = 0
cont_imp = 0

for i in range(100):
    numero_rand = int(random.randint(1,1000))  
    vector.append(numero_rand)
print(f"Listado de números al azar: \n{vector}")

for i in range(len(vector)):  
    if(vector[i] %2==0):
        cont_par = cont_par + 1
    else:
        vector[i] %2!=0
        cont_imp = cont_imp + 1
print("\n-----------------------------------------------------------------")
print(f"La cantidad de números:\nPar:{cont_par} \nImpar:{cont_imp}")
print("Fin del programa")






