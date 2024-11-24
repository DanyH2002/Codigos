print("****************************************************")
print("*PROGRAMA QUE DETERMINA SI UN NUMERO ES PAR O IMPAR*")
print("****************************************************")

numero = int(input("Por favor introduce un numero entero: ")) # Se solicita al usuario que introduzca un numero entero

if numero % 2 == 0: # Se determina si el numero es par o impar
    print("El numero ", numero, " es par.")
elif numero % 2 == 1:
    print("El numero ", numero, " es impar.")
    
