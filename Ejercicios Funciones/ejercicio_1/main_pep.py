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
        estatura = int(input("Ingrese su estatura: "))
        masa = int(input("Ingrese su masa: "))
        print("EJECUTAR FUNCIÓN")

    if (opcion=="4"):
        flag=0          