def palindromaFunction():
    palindroma  =   "no"
    x           =   0
    frase = input("Ingrese una frase: ")
    for y in range(len(frase)-1,0,-1):
        print(f"frase[X]={ frase[x] }, frase[y]={ frase[y] }")
        if(frase[x]==frase[y]):
                palindroma="si"
        else:
            palindroma="no"
            break
        x=x+1
        if(x==y):
            break       
    print(f"La frase {  palindroma  } es palindroma.")
    continuar = input("Desea continuar S/N: ").upper()
    if(continuar=="S"):
        palindromaFunction()

print("Palindroma Validator")
palindromaFunction()