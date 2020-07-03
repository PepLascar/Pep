#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por 
# pantalla el menor y el mayor de los precios."
import os
os.system('cls')

precios =[50, 75, 46, 22, 80, 65, 8]
mayor = max(precios)                                #DE LA FORMA QUE DESARROLLÉ EL EJERCICIO
menor = min(precios)
print(f"El mayor de los precios es: {mayor}\nEl menor de los precios es: {menor}")



#   A L F 

#prices = [50, 75, 46, 22, 80, 65, 8]
#min = max = prices[0]
#for price in prices:
#    if price < min:
#        min = price
#    elif price > max:
#        max = price 
#print("El mínimo es " + str(min)) 
#print("El máximo es " + str(max))