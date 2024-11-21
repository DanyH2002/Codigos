num = int(input("¿Que tabola de multiplicar quieres ver?:"))

print(f"La tabla de multiplicar del {num} es: ")
for i in range(11):
    print(f"{num} x {i} = {num * i} ")
