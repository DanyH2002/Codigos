print("Lista original")
letters = ["b", "d", "f", "g"] # Lista original
print(f"Lista:{letters}") # Imprimiendo la lista original

print("\nInsertando 'a' en posicion 0")
letters.insert(0, "a") # Insertando 'a' en la posicion 0
print(f"Lista: {letters}") # Imprimiendo la lista, con las modificaciones

print("\nInsertando 'c' en posicion 2")
letters.insert(2, "c") # Insertando 'c' en la posicion 2
print(f"Lista:{letters}")

print("\nInsertando 'e' en posicion 4")
letters.insert(4, "e") # Insertando 'e' en la posicion 4
print(f"La lista: {letters}")

print("\nInsertando 'z' en posicion 100")
letters.insert(100, "z") # Insertando 'z' en la posicion 100
print(f"La lista: {letters}")
