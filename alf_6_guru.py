def ejercicio6():
    #Lista con asignaturas
    asignaturas = ["Matematica", "Fisica", "Quimica", "Historia", "Lenguaje" ]
    #Lista vacia para almacenar las notas
    notas = []
    #Pregunto al usuario la nota que obtuvo en cada asignatura y lo transformo en un float y lo almaceno en una lista
    for i in range(0,len(asignaturas)):
        nota = (input(f"Que nota te sacaste en {asignaturas[i]}: "))
        notas.append(float(nota))
    #Recorro la lista y reemplazo la asignatura por "borrar" las signitaturas con notas iguales o superiores a 4.0
    for i in range(0,len(asignaturas)):
        if(notas[i]>=4.0):
            asignaturas[i]="borrar"
    #Recorro la lista de asignaturas con un for de elementos str y borro el valor "borrar" cada vez que este aparece 
    for asignatura in asignaturas:   
        if(asignatura=="borrar"):
            asignaturas.remove("borrar")
    #Imprimo la lista con las asignaturas que debe repetir
    print(f"Debes repetir las siguientes asignaturas: {asignaturas}")
    #Condicion para volver a ejecutar la funcion
    continuar = input("Si desea continuar escriba cualquier wea:")
    if(continuar!=""):
        ejercicio6()

ejercicio6()