print("***** Usando el operador + ***** \n")
tupla1 = (1, 2, 3) # Creando una tupla
tupla2 = (4, 5, 6)

print(f"Tupla1: {tupla1} | tupla2: {tupla2}")
tupla_concatenada = tupla1 + tupla2 # Concatenando las tuplas con el operador +
print(tupla_concatenada, "\n")


print("***** Usando el operador += ***** \n")
tupla1 = (1, 2, 3) # Creando una tupla
tupla2 = (4, 5, 6)

print(f"Tupla1: {tupla1} | tupla2: {tupla2}")
tupla1 += tupla2 # Concatenando las tuplas con el operador +=
print("tupla1: ", tupla1, "\n")


print("***** Usando la funcion tuple() ***** \n")
tupla1 = (1, 2, 3) # Creando una tupla
tupla2 = (4, 5, 6)

print(f"Tupla1: {tupla1} | lista: {list}") # Convertir la tupla a lista
tupla_concatenada = tupla1 + tuple(list(tupla2)) # Concatenando las tuplas con la tupla convertida a lista
print(tupla_concatenada)
