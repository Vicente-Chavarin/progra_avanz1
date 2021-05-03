nombre = []
a = int(input("ingresa el rango: "))
for x in range(a):
    ingresar = input("ingresa los nombres: ")
    nombre.append(ingresar)
nombre.reverse()
print(nombre)
