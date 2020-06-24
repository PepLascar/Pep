import os
os.system('cls')
cont_a = cont_e = cont_i = cont_o = cont_u = 0
palabra = input("Ingrese una palabra para saber cuantas vocales contiene:\n ").lower()
for i in range(len(palabra)):

    if(palabra[i] == "a"):  
        cont_a = cont_a + 1

    if(palabra[i] == "e"):  
        cont_e = cont_e + 1

    if(palabra[i] == "i"):  
        cont_i = cont_i + 1

    if(palabra[i] == "o"):  
        cont_o = cont_o + 1

    if(palabra[i] == "u"): 
        cont_u = cont_u + 1
            
print(f"El total de vocales de la frase: {palabra} es: \nA:{(cont_a)}\nE:{(cont_e)}\nI:{(cont_i)}\nO:{(cont_o)}\nU:{(cont_u)}")


