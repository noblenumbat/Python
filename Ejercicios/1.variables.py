# Mi código original
""" nombre = "" 
edad = 0
fijo = 0
celular = 0

print("Ingresa los siguientes datos:")
print("")
nombre = input("Ingresa tu nombre: ")
edad = input("Cuantos años tienes: ")
fijo = input("Teléfono fijo: ")
celular = input("Celular: ")

print("Tus datos personales son: " + "NOMBRE " + nombre + " EDAD " + edad + " CONTACTOS " + fijo + "-" + celular)
 """
# Existe una mejor manera de escribir el código anterior?

print("Ingresa los siguientes datos:\n") # incluyo un salto de linea

# No necesito declarar variables
nombre = input("Ingresa tu nombre: ")
edad = input("Cuantos años tienes: ")
fijo = input("Teléfono fijo: ")
celular = input("Celular: ")

# Con f-strings puedo concatenar texto y variables 
print(f"Tus datos personales son: NOMBRE {nombre} EDAD {edad} CONTACTOS {fijo} - {celular}")
# Esto se ve mucho mejor y más fácil de leer y escribir, además se elimina el uso de + y strings vacíos "".