print("Accediendo a las posiciones de una lista")
marcas = ["Apple", "Samsung", "Xiami", "Huawei"] # Lista de marcas de celulares

print(f"\nLista completa: {marcas}") # Imprime la lista completa

print(f"\n¿Cuantos elementos tiene la lista? - len(marcas): {len(marcas)}") # Imprime la cantidad de elementos de la lista

print(f"\nmarcas[1]: {marcas[1]}") # Imprime el elemento en la posición 1

print(f"\nmarcas[3]: {marcas[3]}") # Imprime el elemento en la posición 3

print(f"\nmarcas[-1]: {marcas[-1]}") # Imprime el último elemento de la lista

print(f"\nmarcas[-3]: {marcas[-3]}") # Imprime el elemento en la posición -3

print(f"\nmarcas[1:3]: {marcas[1:3]}") # Imprime los elementos en las posiciones 1 y 2

print(f"\nmarcas[:2]: {marcas[:2]}") # Imprime los elementos en las posiciones 0 y 1

print(f"\nmarcas[1:]: {marcas[1:]}") # Imprime los elementos en las posiciones 1, 2 y 3

print(f"\nmarcas[:]: {marcas[:]}") # Imprime todos los elementos de la lista
print(marcas) 

print(f"Generando error - marcas[4]") # Genera un error porque la lista tiene 4 elementos
