
def calcularIva(iva):
    iva=iva*0.19
    return int(iva)

def descuento(precio,descuento):
    precio=precio - int(precio*(descuento/100))
    return precio

def calcularImc(altura,peso):
    imc=peso/(altura*altura)
    if(imc < 18.5):
        estado="Bajo peso"
    if(imc >= 18.5 and imc < 25.0):
        estado="Adecuado"
    if(imc >= 25.0 and imc < 30.0):
        estado="Sobrepeso"
    if(imc >= 30.0 and imc < 35.0):
        estado="Obesidad grado 1"
    if(imc >= 35.0 and imc < 40.0):
        estado="Obesidad grado 2"
    if(imc >= 40.0):
        estado="Obesidad grado 3"
    return estado