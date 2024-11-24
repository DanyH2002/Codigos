print("===================================")
print("¡¡CONVERTIDOR DE NUMEROS A LETRAS!!")
print("===================================")

# Solicitamos el número a convertir
num_uno = int(input("¿Cual es el numero que deseas convertir?: "))

# Comparamos el número ingresado, para mostrar su equivalente en letras
if num_uno == 1:
    print("El numero es 'Uno'")
elif num_uno == 2:
    print("El número es 'Dos'")
elif num_uno == 3:
    print("El número es 'Tres'")
elif num_uno == 4:
    print("El número es 'Cuatro'")
elif num_uno == 5:
    print("El número es 'Cinco'")
else: # Si el número ingresado no es del 1 al 5, se muestra un mensaje de error
    print("Este programa solo puede convertir hasta el numero 5")

print("Fin.")
