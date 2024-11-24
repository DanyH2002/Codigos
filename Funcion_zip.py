names =("Luis", "Diego", "Andres", "Carlos") # Tupla
ages = [15, 30, 26, 12, 40] # Lista
text = "Geekipedia" # Cadena de texto

print(names)
print(ages)
print(text)

print("\nFuncion zip() como iterable: \n")
combination = zip(names, ages, text) # Se crea un objeto iterable, donde zip() combina los elementos de las listas
print(combination)

print("\nFuncion zip() con la funcion list(): \n")
combination = list(zip(names, ages, text)) # Se convierte el objeto iterable en una lista
print(combination)

print("\nFuncion zip() con la funcion tuple(): \n")
combination = tuple(zip(names, ages, text)) # Se convierte el objeto iterable en una tupla
print(combination)

print("\nFuncion zip() con for: \n")
for name, age, s_text in zip(names, ages, text): # Se recorre el objeto iterable
    print(names, ages, s_text)
