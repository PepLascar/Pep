import os
os.system("cls")
espacio = " "

cont = "S"
while(cont == "S"):
    try:
        des = int(input("Ingrese cuantos espacios quiere mover la frase: "))
        if(des>=0 and des<81):
            print(f"{espacio * des}DUOC-UC")
     
    except ValueError:
        print("Debe ingresar un valor númerico")