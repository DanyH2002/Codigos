print("Introduce dos numeros a compartir: ")

num_uno = int(input("Introduce el primer numero: ")) # Pide un numero entero
num_dos = int(input("Introduce el segundo numero: ")) # Pide un numero entero

print("Los numeros a comparar son: ", num_uno, "y", num_dos)

if num_uno == num_dos: # Compara si los numeros son iguales
    print("Es igual...")
if num_uno != num_dos: # Compara si los numeros son diferentes
    print("Es diferente...")
if num_uno < num_dos: # Compara si el primer numero es menor que el segundo
    print("Es menor...")
if num_uno > num_dos: # Compara si el primer numero es mayor que el segundo
    print("Es mayor...")
if num_uno <= num_dos: # Compara si el primer numero es menor o igual que el segundo
    print("Es menor o igual...")
if num_uno >= num_dos: # Compara si el primer numero es mayor o igual que el segundo
    print("Es mayor o igual...")
