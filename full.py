import os
os.system("cls")

import numpy
empleados_retail = numpy.empty(5, dtype='object')
empleados_asesorias = numpy.empty(5, dtype='object')

departamentos = ["Gerencia","Marketing","Producción","RRHH","Finanzas"]
empresas = ["Empresa Master Retail","Empresa Master Asesorías"]
flag=1
while(flag==1):
    opcion = input("\nIngrese una opcion\n1) Registrar empleados.\n2) TOTAL Y PROMEDIO.\n3) LISTAR TODO.\n")

    if(opcion=="1"):
        print(empresas[0])
        for i in range(0,5):
            empleados_retail[i] = int(input(f"Ingrese número empleados de {departamentos[i]}: "))
        print(empresas[1])
        for i in range(0,5):
            empleados_asesorias[i] = int(input(f"Ingrese número empleados de {departamentos[i]}: "))
        
    if (opcion=="2"):
        print("------------------------------------------------------------------------")
        print(f"Total de empleados en el grupo Master IT: {sum(empleados_retail+empleados_asesorias)}")
        for i in range(0,5):
            print(f"Promedio de empleados de {departamentos[i]}: {(empleados_retail[i]+empleados_asesorias[i])/2}")
    

    if (opcion=="3"):
        print("------------------------------------------------------------------------")
        print(empresas[0])
        for j in range(0,5):
            print(f"{departamentos[j]}", end="\t")
        print()
        for j in range(0,5):
            if (j<3):  
                print(f"{empleados_retail[j]}", end="\t\t")
            else:
                print(f"{empleados_retail[j]}", end="\t")

        print("\n------------------------------------------------------------------------")
        print(empresas[1])
        for j in range(0,5):
            print(f"{departamentos[j]}", end="\t")
        print()
        for n in range(0,5):
            if (n<3):  
                print(f"{empleados_asesorias[n]}", end="\t\t")
            else:
                print(f"{empleados_asesorias[n]}", end="\t")