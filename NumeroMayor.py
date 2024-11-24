print("*******************************************************")
print("*PROGRAMA PARA DETERMINAR EL NUMERO MAS GRANDE DE TRES*")
print("*******************************************************")

num_uno = int(input("Introduce el primer numero: ")) # Pide un numero al usuario y lo convierte a entero
num_dos = int(input("Introduce el segundo numero: "))
num_tres = int(input("Introduce el tercer numero: "))

if num_uno > num_dos and num_uno > num_tres: # Si el primer numero es mayor que los otros dos
    print("El numero ", num_uno, " es el numero mas grande de los tres.")
else:
    if num_dos > num_tres: # Si el segundo numero es mayor que
        print("El numero ", num_dos, " es el numero mas grande de los tres.")
    else: # Si el tercero es el mayor
        print("El numero ", num_tres, " es el numero mas grande de los tres.")