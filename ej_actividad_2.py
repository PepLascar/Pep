import numpy
personas = numpy.empty(10, dtype='str')
limite = 0
indice = 0

loop = "S"
while( loop == "S"):
    print("Menu:\n----------------------------------------")
    opcion = input("1) Presione 1 para agregar persona.\n2) Presione 2 para ver persona.\n")


    if(opcion=="1" and limite<10):
        nombre = input(str("Ingrese nombre: "))
        personas[limite] = nombre
        limite = limite + 1
        

    if(limite > 10 and opcion =="1"):
        print("Alcanzó limite máximo de nombres.")

    if(opcion=="2"):
        indice = int(input("Ingrese índice que desea ver: "))
        print(personas[indice])
    if(indice > 10):
        IndexError
            print("Ingrese valor dentro del rango")


        
            

        
        

    

