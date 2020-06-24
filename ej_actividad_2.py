def reset():
    import os
    
    import numpy
    personas = numpy.empty(10, dtype='object')
    limite = 0
    indice = 0
    continuar = "S"

    while(continuar == "S"):
        print("\nMenu:\n------------------------------------")
        opcion = input("1) Presione 1 para agregar persona.\n2) Presione 2 para ver persona.\n3) Presione 3 para ver lista de personas.\n")
        if(opcion=="1" and limite<10):
            nombre = input("Ingrese nombre: ")
            personas[limite] = nombre
            limite = limite + 1

        if(limite > 10 and opcion =="1"):
            print("Alcanzó limite máximo de nombres.")

        if(opcion=="3"):
            print(personas  )

        try:
            if(opcion=="2"):
                indice = int(input("Ingrese índice que desea ver: "))
                print(personas[indice])
        
        except:
            if(indice > 10):
                print("Ingrese un índice menor a 10")
                continuar = input("¿Desea continuar? S/N: ").upper()
                if(continuar == "S"):
                    reset()
                else:
                    print("Fin del programa")
    os.system ("cls")              
reset()    

        
            

        
        

    

