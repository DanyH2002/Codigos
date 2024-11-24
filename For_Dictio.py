dict_name = {"a": 1, "b": 2, "c": 3}

# Recorriendo unicamente las claves:
for key in dict_name:
    print(f"{key} : {dict_name[key]}") # Imprime la clave y el valor
print()


# Recorriendo las claves y los valores:
for key, value in dict_name.items():
    print(f"{key} : {value}") # Imprime la clave y el valor
