# input() es una función que permite al usuario ingresar datos por teclado, en este caso el nombre del usuario
nombre = input("¿Cual es tu nombre?: ") 
print("Hola " + nombre + ", vamos a realizar una suma.") # Se concatena el nombre del usuario con el mensaje

num_uno = int(input("Por favor introduce el primer valor: ")) # Se solicita al usuario que ingrese un número
num_dos = int(input("Por favor introduce el segundo valor: "))

resultado = num_uno + num_dos # Se realiza la suma de los dos números ingresados por el usuario

print(nombre + " ,el resultado de la suma es: ", resultado) # Se concatena el nombre del usuario con el resultado de la suma
