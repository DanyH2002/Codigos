# Creacion de una tupla con 5 elementos, 
# creacion de otra tupla con 5 elementos y suma de ambas tuplas.
tuple1 =(1, 2, 3, 4, 5)
tuple2 =(8, 6, 4, 2, 0)

add_tuples = [] # Lista vacia para almacenar la suma de las tuplas
for x, y in zip(tuple1, tuple2): # zip() empareja los elementos de las tuplas
    add_tuples.append(x + y) # Suma de los elementos emparejados

# Impresion de las tuplas y su suma en pantalla
print("Tupla 1:".ljust(13), tuple1)
print("".ljust(14) + "+")
print("Tupla 2:".ljust(13), tuple2)
print("".ljust(14) + "==============")
print("suma:".ljust(13), tuple(add_tuples))

