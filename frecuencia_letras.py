string = input("Ingresa un texto:")

letters = dict.fromkeys(string, 0) # Crea un diccionario con las letras de la cadena y las inicializa en 0
for letter in string: # Recorre la cadena y cuenta las letras que aparecen
    letters[letter] += 1 # Incrementa el contador de la letra en el diccionario
print(letters)
