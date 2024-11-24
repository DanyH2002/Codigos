# Secuencia con lista sin valor asignado
sequence = ["uno", "dos", "tres"]
dic_name = dict.fromkeys(sequence) # Se crea un diccionario con las llaves de la lista y sin valor
print("Secuencia con lista sin valor: ", dic_name)

# secuencia con lsita con valor asignado
sequence = ["uno", "dos", "tres"]
value = 5
dic_name = dict.fromkeys(sequence, value) # Se crea una lista con las llaves de la lista y con el valor asignado
print("Secuencia con lista y valor: ", dic_name)

# Secuencia con diccionario
sequence = {"uno": 1, "dos": 2, "tres": 3}

value = 5
dic_name = dict.fromkeys(sequence, value) # Se crea un diccionario con las llaves del diccionario y con el valor asignado
print("Secuencia con diccioanrio y valor:", dic_name)

# Secuencia con texto
dic_name = {}.fromkeys("hola", 1) # Se crea un texto con las llaves de la lista y con el valor asignado
print("Secuencia con texto y valor:", dic_name)

# Secuencia con texto y lista
dic_name = {}.fromkeys("hola", [1, 2, "Hola"]) # Se crea un texto con las llaves de la lista y con el valor asignado
print("Secuencia con texto y valor:", dic_name)

# Secuencia con texto y diccionario
dic_name = {}.fromkeys("hola", {}) # Se crea un texto con las llaves de la lista y con el valor asignado
print("Secuencia con texto y valor:", dic_name)
