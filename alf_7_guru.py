def ejercicio7():
    #Lista con el abecedario
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    #Lista para almacenar los multiplos de 3
    m3 = []
    #Recorro la lista "abecedario" e inserto en la lista "m3" todos los elementos que esten en un indice multiplo de 3
    for i in range(0,len(abecedario)):
        if(i%3==0):
            m3.append(abecedario[i])
    #Recorro la lista "m3" y elimino de la lista "abecedario" los elementos contenidos en la lista "m3"
    for i in range(0,len(m3)):
        abecedario.remove(m3[i])
    #Imprimo el resultado de remover de la lista "abecedario" los elementos de la lista "m3"
    print(abecedario)
    #Condicion para volver a ejecutar la funcion
    continuar = input("Si desea continuar escriba cualquier wea:")
    if(continuar!=""):
        ejercicio7()

ejercicio7()