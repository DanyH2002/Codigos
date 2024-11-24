string = "mi mamá me mima" # Cadena de texto
contador = 0 # Variable para contar las veces que se repite una letra

print(string.center(40, "=")) # Imprime la cadena de texto centrada

contador = string.count("M") # Cuenta las veces que se repite la letra M
print(f"\nLa letra M se encontró {contador} vecs en la cadena: {string}")

contador = string.count("m") # Cuenta las veces que se repite la letra m
print(f"\nLa letra m se encontró {contador} vecs en la cadena: {string}")

contador = string.count("mamá") # Cuenta las veces que se repite la palabra mamá
print(f"\nLa letra mamá se encontró {contador} vecs en la cadena: {string}")

contador = string.count("me mima") # Cuenta las veces que se repite la palabra me mima
print(f"\nLa letra me mima se encontró {contador} vecs en la cadena: {string}")

contador = string.count("ma") # Cuenta las veces que se repite la palabra ma
print(f"\nLa letra ma se encontró {contador} vecs en la cadena: {string}")

contador = string.count("m") # Cuenta las veces que se repite la letra m
print(
    f"\nLa letra m se encontró {contador}, desde la posicion 13 en la cadena: {string}"
)

contador = string.count("m") # Cuenta las veces que se repite la letra m
print(
    f"\nLa letra m se encontró {contador}, desde la posicion 100 en la cadena: {string}"
)

contador = string.count("m")
print(
    f"\nLa letra m se encontró {contador}, desde la posicion -3 en la cadena: {string}"
)

contador = string.count("m")
print(
    f"\nLa letra m se encontró {contador}, desde la posicion 3 en la cadena: {string}"
)

contador = string.count("m")
print(
    f"\nLa letra m se encontró {contador}, desde la posicion 100 en la cadena: {string}"
)

contador = string.count("m")
print(
    f"\nLa letra m se encontró {contador}, desde la posicion -4 en la cadena: {string}"
)
