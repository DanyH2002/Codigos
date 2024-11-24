vocales = ["a", "e", "i", "o", "u"] # Lista de vocales
print(f"Listas[3]: {vocales}") # Imprime la lista de vocales
del vocales[3] # Elimina el elemento en la posición 3
print(f"del vocales[3]: {vocales}") # Imprime la lista de vocales sin el elemento en la posición 3

vocales = ["a", "e", "i", "o", "u"] # Lista de vocales
print(f"Listas: {vocales}") # Imprime la lista de vocales
del vocales[0:2] # Elimina los elementos en las posiciones 0 y 1
print(f"del vocales[0:2]: {vocales}") # Imprime la lista de vocales sin los elementos en las posiciones 0 y 1

vocales = ["a", "e", "i", "o", "u"] # Lista de vocales
print(f"Listas: {vocales}") # Imprime la lista de vocales
del vocales[:] # Elimina todos los elementos de la lista
print(f"del vocales[:]: {vocales}") # Imprime la lista de vocales sin elementos

vocales = ["a", "e", "i", "o", "u"] # Lista de vocales
print(f"Listas[3]: {vocales}") # Imprime la lista de vocales
del vocales # Elimina la variable vocales
print(f"La variable vocales ha sido eliminada.") # Imprime que la variable vocales ha sido eliminada
