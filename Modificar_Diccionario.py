# Creacion de un diccionario con frutas y sus precios, 
# modificar el precio de una fruta y agregar una nueva fruta con su precio
fruits_dict = {"manzana": 2.50, "platano": 1.75, "naranja": 3.00, "mango": 4.25}

print(f"Diccionario original: {fruits_dict}")

fruits_dict["manzana"] = 3.50
print(f"Diccionario modificado: {fruits_dict}")

fruits_dict["uva"] = 4.00
print(f"Nuevo valor agregado: {fruits_dict}")
