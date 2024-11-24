matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Creacion de matrices de 3x3

matrix_b = [[1, 2, 3], [4, 1, 2], [1, 1, 0]]

matrix_c = [] # Creacion de matriz vacia
for row in range(len(matrix_a)): # Recorrido de las filas de la matriz
    new_row = [] # Creacion de lista vacia
    for column in range(len(matrix_a[0])): # Recorrido de las columnas de la matriz
        new_row.append(matrix_a[row][column] + matrix_b[row][column]) # Suma de los elementos de las matrices
    matrix_c.append(new_row) # Agregar la lista a la matriz vacia

for row in range(len(matrix_a)): # Recorrido de las filas de la matriz
    if row != 1: # Si la fila es diferente de 1 imprimir la matriz
        print(f"{matrix_a[row]}  {matrix_b[row]}  {matrix_c[row]}") # Imprimir las matrices
    else: # Si no, imprimir la suma de las matrices
        print(f"{matrix_a[row]} + {matrix_b[row]} = {matrix_c[row]}") # Imprimir la suma de las matrices
