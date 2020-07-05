import funciones_1

flag=1
while(flag==1):
    print("\nMenu:\n------------------------------------")
    opcion = input("1) Calcular IVA.\n2) Descuento.\n3) Calcular IMC.\n4) Salir.\n Ingrese opción: ")
    if(opcion=="1"):
        iva = int(input("Ingrese el producto para calcular el IVA: "))
        print(f"El IVA del producto es: {funciones_1.calcularIva(iva)}")

    if(opcion=="2"):
        precio = int(input("Ingrese precio del producto: "))
        descuento = int(input("Ingrese descuento: "))
        print(f"El descuento es: {funciones_1.descuento(precio, descuento)}")
       
    if(opcion=="3"):
        estatura = int(input("Ingrese su estatura (centimetros): "))
        masa = int(input("Ingrese su masa (kilos): "))
        print(f"Su IMC ES: {funciones_1.calcularImc(masa, estatura)}")
        if(funciones_1.calcularImc(masa, estatura)<18.5):
            print("BAJO PESO")
        if(funciones_1.calcularImc(masa, estatura)>18.5 and funciones_1.calcularImc(masa, estatura)<24.9):
            print("ADECUADO")
        if(funciones_1.calcularImc(masa, estatura)>25 and funciones_1.calcularImc(masa, estatura)<29.9):
            print("WATON QLO")
        if(funciones_1.calcularImc(masa, estatura)>30 and funciones_1.calcularImc(masa, estatura)<34.9):
            print("OBESO QL")
        if(funciones_1.calcularImc(masa, estatura)>40):
            print("MORIRAS")


    if (opcion=="4"):
        flag=0          