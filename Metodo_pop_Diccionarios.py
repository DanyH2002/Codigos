dict_name = {"a": 1, "b": 2, "c": 3} # Creando un diccionario

print(f"Diccionario Original: {dict_name}")
last_value = dict_name.pop("b") # Eliminando la clave "b" del diccionario

print(f"Diccionario Modificado: {dict_name}")
print(f"Valor Eliminado: {last_value}") # Imprimiendo el valor eliminado

print()
dict_name = {"a": 1, "b": 2, "c": 3} # Creando un diccionario

print(f"Diccionario Original: {dict_name}")
last_value = dict_name.pop("z", "No se encuentra la clave dentro del diccionario.") # Eliminando la clave "z" del diccionario

print(f"Diccionario Modificado: {dict_name}") # Imprimiendo el diccionario modificado
print(f"Valor Eliminado: {last_value}")
