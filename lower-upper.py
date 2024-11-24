string = input("Introduce un String: ")

# Verificar si todas las letras están en minúsculas
print(f"\n¿Todas las letras están en minúsculas?: {string.islower()}")
string = string.lower()
print(f"String en minúsculas: {string}")

# Verificar si todas las letras están en mayúsculas
print(f"\n¿Todas las letras están en mayúsculas?: {string.isupper()}")
print(f"String en mayúsculas: {string.upper()}")
print(f"String original: {string}")
