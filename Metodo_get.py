# Creacion de un diccionario para almacenar los precios de las frutas
fruits_dict = {"manzana": 1.55, "platano": 3.55, "naranja": 1.25} 

print(fruits_dict)

# Obtener el precio de la manzana por medio del metodo get
precio_manzana = fruits_dict.get("manzana")
print(f"El precio de la manzana es: {precio_manzana}")

# Obtener el precio del mango por medio del metodo get,
# como no existe el mango en el diccionario, se le asignara un valor de None
precio_mango = fruits_dict.get("mango")
print(f"El precio del mango es: {precio_mango}")

# Obtener el precio del mango por medio del metodo get, si no existe el mango se le asignara un precio de 4.55
precio_mango = fruits_dict.get("mango", 4.55)
print(f"El precio del mango es: {precio_mango}")
