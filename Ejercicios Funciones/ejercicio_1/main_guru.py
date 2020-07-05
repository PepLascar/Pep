import funciones_guru

flag=1
while(flag==1):
    opcion = input("\nIngrese una opcion\n1) Calcular Iva.\n2) Descuento.\n3) Calcular Imc.\n4) Salir.\n")

    if(opcion=="1"):
        iva = int(input("Ingrese el valor del producto para calcular el IVA: "))
        print(f"El IVA es: {funciones_guru.calcularIva(iva)}")
        
    if (opcion=="2"):
        precio = int(input("Ingrese el valor del producto: "))
        descuento = int(input("Ingrese el descuento que se le aplicara al producto: "))
        print(f"El precio con el descuento aplicado es: {funciones_guru.descuento(precio,descuento)}")
    
    if (opcion=="3"):
        altura = float(input("Ingrese su altura en metros: "))
        peso = float(input("Ingrese su peso en kilos: "))
        print(f"De acuerdo el IMC su estado es: {funciones_guru.calcularImc(altura,peso)}")


    if (opcion=="4"):
        flag=0