def caja(pago, precio):
    resultado = (pago - precio)
    return resultado

n = int(input("ingresa los clientes: "))
for caja in range(n):
    pago = float(input('Ingrese la cantidad de dinero: '))
    precio = float(input('Ingrese el precio del articulo a comprar: '))
resultado = (caja(pago - precio))
print ("El cambio es de: " + float(resultado) + " pesos")
