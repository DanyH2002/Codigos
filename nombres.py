names_tuple = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina") # Tupla con nombres
print(names_tuple, "\n")

validator = 0 # Variable para validar el numero ingresado
while validator == 0: # Ciclo para validar el numero ingresado
    number =int(input("Introduce un numero entero entre 0 y 4: "))

    if 0 <= number <= 4: # Condicional para validar el numero ingresado
        print(f"El nombre es: {names_tuple[number]}")
    else:
        print("¡ERROR! Numero invalido, vuelve a intentarlo. \n")
        
