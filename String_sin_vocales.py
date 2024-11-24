string = input("Introduce una frase: ") #Introducimos una frase
letter = input("¿Con que frase deseas terminar el bucle?: ")

for character in string: # Recorremos la frase
    if character.lower() ==letter.lower(): # Si la letra es igual a la letra que el usuario introdujo, se rompe el bucle
        break
    elif character.lower() == "a": # Si la letra es igual a una vocal, se salta la letra
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character,end = "") # Imprimimos la letra
    
