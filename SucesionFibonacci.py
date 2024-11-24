num_uno, num_dos = 0, 1 # Inicializacion de variables para la sucesion de Fibonacci
while num_dos <= 1597: # Condicion para que la sucesion no pase de 1597
    print(num_uno, num_dos, end =" ") # Impresion de los numeros de la sucesion
    num_uno = num_uno + num_dos # Suma de los dos numeros anteriores para obtener el siguiente numero
    num_dos = num_uno + num_dos
