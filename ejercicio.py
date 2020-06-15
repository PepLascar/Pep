print("Bienvenido al contador de frases")
cont = 0
continuar = "S"
while(continuar=="S"):
    frase = input("Ingrese la frase para contar sus letras: ")
    for x in range(0,len(frase)):
        if(frase[x]=="a"):
            cont = cont+1
    print(f"El número de letras 'a' de la frase es: {  cont  }")

    continuar = input("Desea continuar S/N").upper()
