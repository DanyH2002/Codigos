print("Sistema para calcular el promedio de un alumno.")

nombre = input("Nombre del Alumno: ") # Recibe el nombre del alumno

matematicas = int(input(nombre + "calificación en matematicas: ")) # Recibe la calificación de matematicas
quimica = int(input(nombre + "calificación en quimica: ")) # Recibe la calificación de quimica
biologia = int(input(nombre + "calificación en biologia: ")) # Recibe la calificación de biologia

promedio = (matematicas + quimica + biologia) / 3 # Calcula el promedio
promedio = int(promedio)

if promedio >= 6: # Si el promedio es mayor o igual a 6
    print('Felicidades '+ nombre + ', "aprobaste" con un promedio de: ', promedio) # Imprime el promedio de aprobado

print("Fin.")

