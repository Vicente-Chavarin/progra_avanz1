### EJERCICIO (Funciones)
# Somos una caja registradora...
# El cliente nos paga con "x" cantidad de dinero, y compra un articulo de "y" precio
# Cuanto nos sobra? (imprimir)
# Podemos tener varios clientes (tenemos que usar un ciclo)
# Billetes 100,50,20 y monedas de 10,5,2,1,.50 centavos
def caja(pago, precio):
    if(pago > precio):
        resultado = pago - precio
        feria = sobra(resultado)
        return "El cambio es: " + str(resultado) + "pesos \n" + str(feria) 
    elif(pago == precio):
        return "no te sobra dinero"
    else:
        return "Mañana se fi, hoy no"


def sobra(pago):
    feria100 = pago/100
    feria50 = feria100/50
    feria20 = feria50/20
    feria10 = feria20/10
    feria5 = feria10/5
    return "Tu feria en billetes de 100 es= " +str(feria100) + "\n Tu feria en billetes de 50 es= " +str(feria50)

n = int(input("ingresa los clientes: "))
for x in range(n):
    pago = float(input('Ingrese la cantidad de dinero: '))
    precio = float(input('Ingrese el precio del articulo a comprar: '))
    resultado = caja(pago, precio)
    print (resultado)

