




while(continuar == "S"):
        print("\nMenu:\n------------------------------------")
        opcion = input("1) Registrar empleados.\n2) TOTAL Y PROMEDIO.\n3) LISTAR TODO.\n")
        if(opcion=="1"):
                for i in range(0,5):
                    empleados_retail = int(input(f"Ingrese número empleados de {departamenos[i]} "))

           

        if(limite > 10 and opcion =="1"):
            print("Alcanzó limite máximo de nombres.")

        if(opcion=="3"):
            print(personas)

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

        
            

        
        

    

