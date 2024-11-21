names_tuple = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina")
print(names_tuple, "\n")

validator = 0
while validator == 0:
    number =int(input("Introduce un numero entero entre 0 y 4: "))

    if 0 <= number <= 4:
        print(f"El nombre es: {names_tuple[number]}")
    else:
        print("¡ERROR! Numero invalido, vuelve a intentarlo. \n")
        
