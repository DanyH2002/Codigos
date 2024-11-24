dictionary = {"a": 1, "b": 2, "c": 3} # Creando un diccionario

print(dictionary)
print(f"\nLas keys del diccionario son: \n{dictionary.keys()}") # Imprimiendo las keys del diccionario

print("\nConvirtiendo keys a lista utilizando el constructor list()")
list_keys = list(dictionary.keys()) # Convirtiendo las keys a lista

print(f"La lista es: {list_keys}") # Imprimiendo la lista keys
print(f"Posicion 1 de la lista keys: {list_keys[1]}") # Imprimiendo la posicion 1 de la lista keys
