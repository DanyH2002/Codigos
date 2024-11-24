#conjuncion

print("Conjuncion (and)")
num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: ")) # Se pide un numero al usuario

if num_uno >2 and num_uno <5: # Se evalua si el numero cumple con la condición
    print("El numero ", num_uno, " cumple con la condición.")
else:
    print("El numero ", num_uno, " NO cumple con la condición.")


#Disyunción
print("Disyunción (or)")

palabra= input("Para cumplir con la condición escribe 'si' o 'yes': ") # Se pide una palabra al usuario

if palabra == "si" or palabra == "yes": # Se evalua si la palabra cumple con la condición
    print("La condición se ha cumplido.")
else:
    print("La condición NO se ha cumplido.")


#Negación
print("Negación (not)")

num_uno = int(input("Introduce un numero igual a 5: ")) # Se pide un numero al usuario

if not num_uno == 5: # Se evalua si el numero cumple con la condición
    print("El numero es diferente de cinco y SI cumple la condición.")
else:
    print(" El numero es igual a cinco y NO cumple la condición.")