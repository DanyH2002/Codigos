string = "Diana se peina sola"
resultado = 0
starts_with = "ejemplos con startswith():"

# Ejemplos con startswith(), que devuelve True si la cadena comienza con la subcadena especificada
print(f"\n{starts_with.rjust(50, 'm')}")

resultado = string.startswith("D")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado = string.startswith("d")
print(f"\n{string} comienza con la subcadena d: {resultado}")

resultado = string.startswith("Diana")
print(f"\n{string} comienza con la subcadena Diana: {resultado}")

resultado = string.startswith("se")
print(f"\n{string} comienza con la subcadena se, desde la posicion 6: {resultado}")

resultado = string.startswith("se")
print(
    f"\n{string} comienza con la subcadena se, desde la posicion 6 hasta la posicion 7: {resultado}"
)

resultado = string.startswith("se")
print(
    f"\n{string} comienza con la subcadena se, desde la posicion 100 hasta la posicion 100: {resultado}"
)

resultado = string.startswith("se")
print(
    f"\n{string} comienza con la subcadena se, desde la posicion -4 hasta la posicion -1: {resultado}"
)

# Ejemplos con endswith(), que devuelve True si la cadena termina con la subcadena especificada
print(f"\n(ends_with_rjust(50, '='))")

resultado = string.startswith("A")
print(f"\n{string} termina con la subcadena A: {resultado}")

resultado = string.startswith("a")
print(f"\n{string} termina con la subcadena a: {resultado}")

resultado = string.startswith("sola")
print(f"\n{string} termina con la subcadena sola: {resultado}")

resultado = string.startswith("sola")
print(f"\n{string} termina con la subcadena sola, desde la posicion 10: {resultado}")

resultado = string.startswith("s")
print(
    f"\n{string} termina con la subcadena s, desde la posicion 9 hasta la posicion 14: {resultado}"
)

resultado = string.startswith("s")
print(
    f"\n{string} termina con la subcadena s, desde la posicion 100 hasta la posicion 100: {resultado}"
)

resultado = string.startswith("s")
print(
    f"\n{string} termina con la subcadena s, desde la posicion -4 hasta la posicion -2: {resultado}"
)
