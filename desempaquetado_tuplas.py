# Creacion de una tupla con frutas y sus atributos
fruits_tuple = ("001", "Manzana", "rojo"), ("002", "Pera", "verde"), ("003", "Naranja", "naranja")
print(fruits_tuple, "\n") # Imprime la tupla de frutas

for code, fruit, color in fruits_tuple: # Desempaquetado de la tupla
    print(f"La {fruit} tiene el codigo {code} y es de color {color}.") # Imprime los atributos de las frutas
