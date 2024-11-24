rows = int(input("¿Cuantas filas tendra la matriz?: ")) # Pide al usuario el número de filas
columns = int(input("¿Cuantas columnas tendra la matriz?:")) # Pide al usuario el número de columnas

matrix = [] # Crea una matriz vacia

for row_position in range(rows): # Recorre las filas
    row = [] # Crea una fila vacia
    for element in range(columns): # Recorre los elementos de la fila 
        row.append(int(input(f"Introduce un elemento a la fila {row_position}:"))) # Pide al usuario un elemento y lo agrega a la fila
    matrix.append(row) # Agrega la fila a la matriz

for row in matrix: # Recorre las filas de la matriz
    print(row) # Imprime la fila
