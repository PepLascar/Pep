#1.- Registrar la cantidad de empleados que trabajan en el grupo empresarial “Master IT”, el grupo está compuesto 
#por 2 empresas (master retail y master asesorías), los empleados de cada empresa se distribuyen en 5 departamentos diferentes:  
#gerencia, marketing, producción, recursos humanos y finanzas

#2.- Ver totales, que permite mostrar el total de empleados del grupo empresarial y el promedio de empleados de cada departamento para 
#todo el grupo empresarial, (ejemplo: promedio de empleados de gerencia, promedio de empleados de marketing y otros) .

#Recuerde validar la información para el ingreso de la cantidad de empleados (mayor a cero) y evitar ingresar texto en los diferentes datos de entrada del sistema.
import os
os.system("cls")

import numpy
empleados_retail = numpy.empty(5, dtype='object')
empleados_asesorias = numpy.empty(5, dtype='object')

departamentos =  ["Gerencia", "Marketing","Producción", "RRHH", "Finanzas"]
empresas = ["Empresa Master Retail", "Empresa Master Asesorías"]


print("------------------------------------")
for i in range(0,2):
    print(empresas[i])
    for j in range(0,5):
        print(f"{departamentos[j]}", end="\t")
    print("\n------------------------------------")







#registrar cantidad empleados