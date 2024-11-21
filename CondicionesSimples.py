print("Sistema para calcular el promedio de un alumno.")

nombre = input("Nombre del Alumno: ")

matematicas = int(input(nombre + "calificación en matematicas: "))
quimica = int(input(nombre + "calificación en quimica: "))
biologia = int(input(nombre + "calificación en biologia: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades '+ nombre + ', "aprobaste" con un promedio de: ', promedio)

print("Fin.")

