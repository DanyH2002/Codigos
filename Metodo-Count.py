string = "mi mamá me mima"
contador = 0

print(string.center(40, "="))

contador = string.count("M")
print(f"\nLa letra M se encontró {contador} vecs en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador} vecs en la cadena: {string}")

contador = string.count("mamá")
print(f"\nLa letra mamá se encontró {contador} vecs en la cadena: {string}")

contador = string.count("me mima")
print(f"\nLa letra me mima se encontró {contador} vecs en la cadena: {string}")

contador = string.count("ma")
print(f"\nLa letra ma se encontró {contador} vecs en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador}, desde la posicion 13 en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador}, desde la posicion 100 en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador}, desde la posicion -3 en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador}, desde la posicion 3 en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador}, desde la posicion 100 en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontró {contador}, desde la posicion -4 en la cadena: {string}")
