def funcionBase():
    
    #Condicion para volver a ejecutar la funcion
    continuar = input("Si desea continuar escriba cualquier wea:")
    if(continuar!=""):
        funcionBase()

funcionBase()