# Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad= int(input("Por favor, ingresa tu edad: "))

# paso 2: Verificar si la edad ingresada cumplle con el requisito  para ingresar a la discoteca

permitido= True if edad >= 18 else False # ternario1
# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca

if permitido:
    print("puedes ingresar a la discoteca!")
else:
   print(" Lo siento mucho, no se puede ingresar a la discoteca siendo menor de edad")
