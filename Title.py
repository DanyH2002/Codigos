first_name = input("Nombre: ") # Se solicita el nombre al usuario
last_name = input("Apellido: ") # Se solicita el apellido al usuario
full_name = f"{first_name} {last_name}" # Se concatenan el nombre y el apellido

print()
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}") # Se verifica si el metodo title() se ha aplicado
print(f"Aplicando el metodo title(): {full_name.title()}") # Se aplica el metodo title() al nombre completo
print(f"Volvemos a imprimir el nombre: {full_name}") # Se imprime el nombre completo

print()
full_name = full_name.title() # Se aplica el metodo title() de manera permanente
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}") # Se verifica si el metodo title() se ha aplicado
print(f"Se ha aplicado el metodo title() de manera permanente: {full_name}") # Se imprime el nombre completo
