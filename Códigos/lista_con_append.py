print("Bienvenido al contador de frases")
cont = 0
continuar = "S"
listafrase = [] 
while(continuar=="S"):
    frase = input("Ingrese la frase para contar sus letras: ")
    listafrase.append(frase) #aquí es donde se están guardando los nombres/datos en la lista
    cantidad = len(frase)
    print(f"El número de letras de la frase es: {  cantidad  }")
    cont = cont + 1

    continuar = input("Desea continuar S/N").upper()

print(listafrase)

