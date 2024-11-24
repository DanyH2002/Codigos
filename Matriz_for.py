matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] # Matriz de 3x3

print("Mostrar todos los elementos de la matriz fila por fila")
for row in matrix: # Recorre cada fila de la matriz
    print(row)

print("Mostrar todos los elementos de la matriz a elemento en columna")
for row in matrix: # Recorre cada fila de la matriz
    for element in row:
        print(element)

print("Mostrar todos los elementos de la matriz en formato de matriz")
for row in matrix: # Recorre cada fila de la matriz
    for element in row: # Recorre cada elemento de la fila
        print(element, end = "")
    print()