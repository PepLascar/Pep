def ejercicio6():
    
    asignaturas = ["Matematica", "Fisica", "Quimica", "Historia", "Lenguaje" ]
    
    notas = []
    
    for i in range(0,len(asignaturas)):
        nota = (input(f"Que nota te sacaste en {asignaturas[i]}: "))
        notas.append(float(nota))
    
    for i in range(0,len(asignaturas)):
        if(notas[i]>=4.0):
            asignaturas[i]="borrar"
    
    for asignatura in asignaturas:   
        if(asignatura=="borrar"):
            asignaturas.remove("borrar")
    
    print(f"Debes repetir las siguientes asignaturas: {asignaturas}")
    
    continuar = input("Si desea continuar escriba cualquier wea:")
    if(continuar!=""):
        ejercicio6()

ejercicio6()