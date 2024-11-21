# Secuencia con lista sin valor asignado
sequence = ["uno", "dos", "tres"]
dic_name = dict.fromkeys(sequence)
print("Secuencia con lista sin valor: ", dic_name)

#secuencia con lsita con valor asignado
sequence = ["uno", "dos", "tres"]
value = 5
dic_name = dict.fromkeys(sequence, value)
print("Secuencia con lista y valor: ", dic_name)

#Secuencia con diccionario
sequence = {"uno": 1,
            "dos": 2,
            "tres": 3
            }

value = 5
dic_name = dict.fromkeys(sequence, value)
print("Secuencia con diccioanrio y valor:",dic_name)

# Secuencia con texto
dic_name = {}.fromkeys("hola", 1)
print("Secuencia con texto y valor:",dic_name)

# Secuencia con texto y lista
dic_name = {}.fromkeys("hola", [1, 2, "Hola"])
print("Secuencia con texto y valor:",dic_name)

# Secuencia con texto y diccionario
dic_name = {}.fromkeys("hola", {})
print("Secuencia con texto y valor:",dic_name)
