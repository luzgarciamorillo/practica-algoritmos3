# ----------------------------------------------------------
# PRÁCTICA ALGORITMOS 3: INGRESO A DISCOTECA
# ----------------------------------------------------------

# Paso 1: Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Por favor, ingresa tu edad: "))

# Paso 2: Verificar si al edad ingresada cumple con el requisito para ingresar a la discoteca
permitido = True
if edad >= 18:
    permitido = True
else:
    permitido = False

# Paso 3: Mostrar al usuario si el cliente puede o no ingresar a la discoteca
if permitido == True:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, no se puede ingresar a la discoteca siendo menor de edad")

# Podemos reducir esto
# Paso 1: Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Por favor, ingresa tu edad: "))

# Paso 2: Verificar si al edad ingresada cumple con el requisito para ingresar a la discoteca
permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si el cliente puede o no ingresar a la discoteca
if permitido == True:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, no se puede ingresar a la discoteca siendo menor de edad")
