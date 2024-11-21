string = "Diana se peina sola"
resultado = 0
starts_with = "ejemplos con startswith():"

print(f"\n{starts_with.rjust(50, 'm')}")

resultado =string.stratswith("D")
print(f"\n(string) comienza con la subcadena D: (resultado)")

resultado =string.stratswith("d")
print(f"\n(string) comienza con la subcadena d: (resultado)")

resultado =string.stratswith("Diana")
print(f"\n(string) comienza con la subcadena Diana: (resultado)")

resultado =string.stratswith("se")
print(f"\n(string) comienza con la subcadena se, desde la posicion 6: (resultado)")

resultado =string.stratswith("se")
print(f"\n(string) comienza con la subcadena se, desde la posicion 6 hasta la posicion 7: (resultado)")

resultado =string.stratswith("se")
print(f"\n(string) comienza con la subcadena se, desde la posicion 100 hasta la posicion 100: (resultado)")

resultado =string.stratswith("se")
print(f"\n(string) comienza con la subcadena se, desde la posicion -4 hasta la posicion -1: (resultado)")


print(f"\n(ends_with_rjust(50, '='))")

resultado =string.stratswith("A")
print(f"\n(string) termina con la subcadena A: (resultado)")

resultado =string.stratswith("a")
print(f"\n(string) termina con la subcadena a: (resultado)")

resultado =string.stratswith("sola")
print(f"\n(string) termina con la subcadena sola: (resultado)")

resultado =string.stratswith("sola")
print(f"\n(string) termina con la subcadena sola, desde la posicion 10: (resultado)")

resultado =string.stratswith("s")
print(f"\n(string) termina con la subcadena s, desde la posicion 9 hasta la posicion 14: (resultado)")

resultado =string.stratswith("s")
print(f"\n(string) termina con la subcadena s, desde la posicion 100 hasta la posicion 100: (resultado)")

resultado =string.stratswith("s")
print(f"\n(string) termina con la subcadena s, desde la posicion -4 hasta la posicion -2: (resultado)")
