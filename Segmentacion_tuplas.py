#Acceder a los elementos mediante el operador de segmentacion

vowels_tuple = ("a", "e", "i", "o", "u")
print(vowels_tuple, "\n")

print(f"Porsiciones [0:2] -> {vowels_tuple[0:2]}")
print(f"Porsiciones [::2] -> {vowels_tuple[::2]}")
print(f"Porsiciones [-3:] -> {vowels_tuple[-3:]}")
