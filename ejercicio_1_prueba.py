#1.- Registrar la cantidad de empleados que trabajan en el grupo empresarial “Master IT”, el grupo está compuesto 
#por 2 empresas (master retail y master asesorías), los empleados de cada empresa se distribuyen en 5 departamentos diferentes:  
#gerencia, marketing, producción, recursos humanos y finanzas

#2.- Ver totales, que permite mostrar el total de empleados del grupo empresarial y el promedio de empleados de cada departamento para 
#todo el grupo empresarial, (ejemplo: promedio de empleados de gerencia, promedio de empleados de marketing y otros) .

#Recuerde validar la información para el ingreso de la cantidad de empleados (mayor a cero) y evitar ingresar texto en los diferentes datos de entrada del sistema.



import numpy as np  
empresas = np.empty([2, 5], dtype='int')

for i in range(2):  #empresas
    for j in range(5):  #departamentos
        empleados = input(f"Ingrese nuevo colaborador: {i} {j}")
        empresas [i, j] = empleados

#registrar cantidad empleados