print("Palindroma Validator")
palindroma = "no"
continuar = "S"
while(continuar=="S"):
    frase = input("Ingrese una frase: ")

    for x in range(0,len(frase)):
        for y in range(len(frase),0,-1):
            if(frase[x]==frase[y-1]):
                palindroma="si"
            else:
                palindroma="no"

    print(f"La frase {  palindroma  } es palindroma.")

    continuar = input("Desea continuar S/N").upper()