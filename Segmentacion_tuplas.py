#Acceder a los elementos mediante el operador de segmentacion

vowels_tuple = ("a", "e", "i", "o", "u") #Tupla de vocales
print(vowels_tuple, "\n")

print(f"Porsiciones [0:2] -> {vowels_tuple[0:2]}") #Acceder a los elementos de la tupla mediante el operador de segmentacion, en este caso se accede a las posiciones 0 y 1
print(f"Porsiciones [::2] -> {vowels_tuple[::2]}") #Acceder a los elementos de la tupla mediante el operador de segmentacion, en este caso se accede a las posiciones 0 y 2
print(f"Porsiciones [-3:] -> {vowels_tuple[-3:]}") #Acceder a los elementos de la tupla mediante el operador de segmentacion, en este caso se accede a las posiciones -3, -2 y -1
