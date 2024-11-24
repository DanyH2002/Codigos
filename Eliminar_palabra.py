string = input("Introduce una frase: ") # Pide al usuario que introduzca una frase
palabra = input("Introduce la palabra que deseas eliminar: ") # Pide al usuario que introduzca la palabra que desea eliminar
substring = ""

indice = string.find(palabra) # Busca la palabra en la frase
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ] # Elimina la palabra de la frase

print(f"Cadena resultante: {substring}")
