print("Sistema para calcular el promedio de un alumno.")

nombre = input("Nombre del Alumno: ")

matematicas = float(input(nombre + ", calificación de matematicas: "))
quimica = float(input(nombre + ", calificación de quimica: "))
biologia = float(input(nombre + ", calificación de biologia: "))

promedio = (matematicas + quimica + biologia)/3

if promedio >=6:
    print('Felicidades, ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    print('Felicidades, ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2))
else:
    print('Lo sentimos, ' + nombre + " has 'reprobado' con un promedio de: ", promedio)
    print('Lo sentimos, ' + nombre + " has 'reprobado' con un promedio de: ", round(promedio,1))

print("fin.")          
