dictionary = {"a": 1, "e": 2} # Diccionario con dos elementos

print(dictionary) # Imprime el diccionario
print(f"Clave a: {dictionary['a']}") # Imprime el valor de la clave 'a'
print(f"Clave e: {dictionary['e']}") # Imprime el valor de la clave 'e'

print()

dictionary = {"numbers": [18, 20, 28], "groups": {"a": 1, "b": 2}} # Diccionario con listas y diccionarios

print(dictionary) # Imprime el diccionario
print(f"Clave numbers: {dictionary['numbers']}") # Imprime el valor de la clave 'numbers'
print(f"Clave groups: {dictionary['groups']}") # Imprime el valor de la clave 'groups'

print(f"Clave numbers: {dictionary['numbers'][1]}") # Imprime el valor de la clave 'numbers' en la posicion 1
print(f"Clave groups: {dictionary['groups']['b']}") # Imprime el valor de la clave 'groups' en la clave 'b'
