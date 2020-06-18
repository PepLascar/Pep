#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas 
# introducidas por el usuario.
import numpy

def alf3():
    asignatura = ["Matematicas", "Lenguaje", "Fisica"]
    nota = numpy.empty(len(asignatura), dtype='float')
    for i in range(0,len(asignatura)):
        nota[i] = float(input(f"Que nota te sacaste en {asignatura[i]}: "))
    
    for i in range(0,len(asignatura)):
        print(f"En {asignatura[i]} has sacado {(nota[i])}")
    
    continuar = input("Si desea continuar escriba cualquier wea:")
    if(continuar!=""):
        alf3()

alf3()