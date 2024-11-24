num = int(input("¿Que tabla de multiplicar quieres ver?:")) # Se pide un numero al usuario

print(f"La tabla de multiplicar del {num} es: ")
for i in range(11): # Ciclo para imprimir la tabla de multiplicar
    print(f"{num} x {i} = {num * i} ") # Se imprime la tabla de multiplicar
