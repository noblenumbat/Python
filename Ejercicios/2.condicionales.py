# EJEMPLO 1: Número positivo o negativo

# Sintaxis Propia

# numero = 0 

# if numero < 0:
#     print(f"El numero {numero} es negativo")
    
# elif numero > 0: 
#     print(f"El número es {numero} positivo")

# else:
#     print(f"El numero es  {numero}")

# -----------------------------------------------------

# Sintaxis moderna

# match numero:
#     case n if n > 0:
#         print(f"El numero {numero} es positivo.")
#     case n if n < 0:
#         print(f"El numero {numero} es negativo.")
#     case _:
#         print("El numero es cero.")

# -----------------------------------------------------

# EJEMPLO 2: Mayor o menor de edad

# Sintaxis propia

edad = 17

# if edad >= 18:
#     print("Puedes ingresar a la disco")
# else:
#     print("Queda en casa")

# -----------------------------------------------------

# Otra manera de escribir 

mensaje = ("Puedes ingresar a la disco" if edad >= 18 else "Quedate en casa")

print(f"1 mensaje nuevo = {mensaje}")

# -----------------------------------------------------

#EJEMPLO 3: Comparando dos números

num1 = 2
num2 = 2

# if num1 != num2:
#     print("Los numeros son distintos")
# else:
#     print("Los numeros coinciden")

# -----------------------------------------------------

# Operador ternario

# print("Los numeros son diferentes" if num1 != num2 else "Los numeros son iguales")