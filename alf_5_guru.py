def ejercicio5():
    #Declaro una lista vacia
    lista = []
    #Lleno la lista con numeros de 1 al 10
    for i in range(0,10):
        lista.append(i+1)
    #Invierto el orden de la lista
    lista.reverse()
    #Imprimo la lista pero los primeros 9 indices incluyen una "," al final
    for i in range(0,10):
        if(i<9):
            print(lista[i], end=",")
        else:
            print(lista[i])
    #Condicion para volver a ejecutar la funcion
    continuar = input("Si desea continuar escriba cualquier wea:")
    if(continuar!=""):
        ejercicio5()

ejercicio5()