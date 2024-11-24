print("Sistema para calcular el promedio de un alumno.")

nombre = input("Nombre del Alumno: ") # Recibe el nombre del alumno

matematicas = float(input(nombre + ", calificación de matematicas: ")) # Recibe la calificación de matematicas
quimica = float(input(nombre + ", calificación de quimica: ")) # Recibe la calificación de quimica
biologia = float(input(nombre + ", calificación de biologia: ")) # Recibe la calificación de biologia

promedio = (matematicas + quimica + biologia)/3 # Calcula el promedio

if promedio >=6: # Si el promedio es mayor o igual a 6
    print('Felicidades, ' + nombre + ' "aprobaste" con un promedio de: ', promedio) # Imprime el promedio de  aprovado
    print('Felicidades, ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2)) # Imprime el promedio, redondeado a 2 decimales
else: # Si el promedio es menor a 6
    print('Lo sentimos, ' + nombre + " has 'reprobado' con un promedio de: ", promedio) # Imprime el promedio de reprobado
    print('Lo sentimos, ' + nombre + " has 'reprobado' con un promedio de: ", round(promedio,1)) # Imprime el promedio, redondeado a 1 decimal

print("fin.")          
