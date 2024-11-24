nums_tuple = (5, 8, 3, 3, 1, 6, 2) # Tupla original
print(f"Tupla original: {nums_tuple} \n")

num = int(input("¿Cual de esos numeros quieres modificar por 0?"))
nums_tuple = list(nums_tuple) # Convertir la tupla a lista para poder modificarla
len_tuple = len(nums_tuple) # Longitud de la tupla

for index in range(len_tuple): # Recorrer la tupla para modificar el numero deseado
    if nums_tuple[index] == num: # Si el numero en la posicion actual es igual al numero deseado se cambia por 0
        nums_tuple[index] = 0 # Modificar el numero deseado por 0

nums_tuple = tuple(nums_tuple) # Convertir la lista a tupla
print(f"\nTupla modificada: {nums_tuple} \n") # Imprimir la tupla modificada
