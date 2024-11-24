dictionary = {"a": 1, "b": 2, "c": 3} # Creando un diccionario

print(dictionary)
print(f"\nLos valores del diccionario son: \n{dictionary.values()}") # Imprimiendo los valores del diccionario

print("\nConvirtiendo los valores a lista utilizando el contructor list()")
list_values = list(dictionary.values()) # Convirtiendo los valores del diccionario a lista

print(f"La lista es: {list_values}") # Imprimiendo la lista
print(f"Posicion 1 de la lista values: {list_values[1]}") # Imprimiendo el valor en la posicion 1 de la lista
