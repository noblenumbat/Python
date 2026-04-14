opcion = None

print("1. Helado")
print("2. Cafe")
print("3. Agua")
print("4. Salir\n")

while True: # Permite regresar al menú principal tras seleccionar una opcion
    try:
        opcion = int(input("Elige una opción:"))
    except ValueError:
        print("Opción no valida")

    match opcion:
        case opc if opc == 1:
            print("Son 10.50")
        case opc if opc == 2:
            print("Son 5.00")
        case opc if opc == 3:
            print("Son 2.00")
        case opc if opc == 4:
            print("Salio del programa")
            break
        case _m:
            opcion = "" # Limpiando la variable

    opcion = ""

