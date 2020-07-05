import funciones_guru

flag=1
while(flag==1):
    opcion = input("\nIngrese una opcion\n1) Calcular Iva.\n2) Descuento.\n3) Calcular Imc.\n4) Salir.\n")

    if(opcion=="1"):
        funciones.calcularIva()
        
    if (opcion=="2"):
        print("ejecuto funcion 2")

    if (opcion=="3"):
        print("ejecuto funcion 3")

    if (opcion=="4"):
        flag=0