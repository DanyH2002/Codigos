#conjuncion

print("Conjuncion (and)")
num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_uno >2 and num_uno <5:
    print("El numero ", num_uno, " cumple con la condición.")
else:
    print("El numero ", num_uno, " NO cumple con la condición.")


#Disyunción
print("Disyunción (or)")

palabra= input("Para cumplir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.")
else:
    print("La condición NO se ha cumplido.")


#Negación
print("Negación (not)")

num_uno = int(input("Introduce un numero igual a 5: "))

if not num_uno == 5:
    print("El numero es diferente de cinco y SI cumple la condición.")
else:
    print(" El numero es igual a cinco y NO cumple la condición.")

              
 
