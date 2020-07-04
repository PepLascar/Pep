if (opcion==3):
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