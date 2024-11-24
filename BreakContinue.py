#ejemplo para break

print("while con la sentencia break")
contador = 0 # Se inicializa la variable contador en 0
while contador <10: # Se inicia un ciclo while, que se ejecutara mientras la variable contador sea menor a 10
    contador += 1 # Se incrementa la variable contador en 1

    if contador == 5: # Si la variable contador es igual a 5 se ejecuta la sentencia break
        break


    print("Valor actual de la variable: ", contador)

print("Fin del programa, la sentencia break se ha ejecutado")

#ejemplo para continue

print("while con la sentencia continue")
contador = 0 # Se inicializa la variable contador en 0
while contador <10: # Se inicia un ciclo while, que se ejecutara mientras la variable contador sea menor a 10
    contador += 1

    if contador == 5: # Si la variable contador es igual a 5 se ejecuta la sentencia continue
        continue

    print("Valor actual de la variable: ", contador)
    
