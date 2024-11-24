dict_name = {"a": 1, "b": 2, "c": 3} # Creando un diccionario

print(f"Diccionario original: {dict_name}")

dict_name.update({"z": 4, "d": 5}) # Agregando elementos al diccionario
print(f"Agregando 'z' y 'd': {dict_name}")

dict_name.update({"a": 6, "b": 5}) # Actualizando elementos del diccionario
print(f"Actualizando 'a' y 'b': {dict_name}")
