dictionary = {"a": 1, "b": 2, "c": 3} # Creación de un diccionario

print(dictionary)
print(f"\nLos items del diccionario son:\n{dictionary.items()}") # Método items() retorna una vista de los items del diccionario

print("\nConvirtiendo items a lista utilizando el constructor list()")
list_items = list(dictionary.items()) # Convertir items a lista

print(f"La lista es: {list_items}") # Imprimir la lista
print(f"La posición 1 de la lista items: {list_items[1]}") # Imprimir la posición 1 de la lista
