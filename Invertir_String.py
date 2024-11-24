string = input("Introduce un String para invertirlo: ") # Se solicita un string al usuario
string_reversed = ""

for character in string: # Se recorre el string de forma inversa
    string_reversed = character + string_reversed # Se va concatenando el string invertido

print(f"String invertido: {string_reversed}") # Se imprime el string invertido
