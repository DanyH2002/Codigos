string = "Menu" # Variable de tipo string, que se va a modificar con los metodos center, ljust y rjust

print("Metodos con espacios: ")
print(string.center(20)) # Metodo center, centra el texto en 20 espacios
print(string.ljust(20)) # Metodo ljust, justifica el texto a la izquierda en 20 espacios
print(string.rjust(20)) # Metodo rjust, justifica el texto a la derecha en 20 espacios


print("\nMetodos con caracter:")
print(string.center(20, "=")) # Metodo center, centra el texto en 20 espacios y rellena con el caracter "="
print(string.ljust(20, "="))
print(string.rjust(20, "="))

print("\nVariable modificada:")
string = string.center(10, "=") # Se modifica la variable string, centrandola en 10 espacios y rellenando con el caracter "="
print(string)


