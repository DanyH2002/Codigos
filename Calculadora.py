print("CALCULADORA CON UNA VARIABLE \n")

print("*******************")
print("* MENU DE OPCIONES*")
print("*******************")

# Se muestran las opciones que el usuario puede elegir
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISIÓN")
print("5. DIVISIÓN ENTERA")
print("6. EXPONENTE")
print("7. MODULO O RESTO \n")

# Recibe la opción que el usuario elige
numero = int(input("Introduce la opción deseada: "))

if numero == 1:

    print ("Elegiste suma \n")
    numero = int(input("Introduce el primer numero: ")) # Se introduce el primer numero
    numero += int(input("Introduce el segundo numero: ")) # Se realiza la suma con el operador +=
    print("El resultado de la suma es: ", numero)

elif numero ==2:

    print ("Elegiste resta \n")
    numero = int(input("Introduce el primer numero: ")) # Se introduce el primer numero
    numero -= int(input("Introduce el segundo numero: ")) # Se realiza la resta con el operador -=
    print("El resultado de la resta es: ", numero)

elif numero ==3:

    print ("Elegiste multiplicación \n")
    numero = int(input("Introduce el primer numero: ")) # Se introduce el primer numero
    numero *= int(input("Introduce el segundo numero: ")) # Se realiza la multiplicación con el operador *=
    print("El resultado de la multiplicación es: ", numero)


elif numero ==4:

    print ("Elegiste división \n")
    numero = int(input("Introduce el primer numero: "))   # Se introduce el primer numero
    numero /= int(input("Introduce el segundo numero: ")) # Se realiza la división con el operador /=
    print("El resultado de la división es: ", numero)


elif numero ==5:

    print ("Elegiste división entera \n")
    numero = int(input("Introduce el primer numero: ")) # Se introduce el primer numero
    numero //= int(input("Introduce el segundo numero: ")) # Se realiza la división entera con el operador //=
    print("El resultado de la división entera es: ", numero)


elif numero ==6:

    print ("Elegiste exponente \n")
    numero = int(input("Introduce el primer numero: ")) # Se introduce el primer numero
    numero **= int(input("Introduce el segundo numero: ")) # Se realiza el exponente con el operador **=
    print("El resultado del exponente es: ", numero)


elif numero ==7:

    print ("Elegiste modulo o resto \n")
    numero = int(input("Introduce el primer numero: ")) # Se introduce el primer numero
    numero %= int(input("Introduce el segundo numero: ")) # Se realiza el modulo o resto con el operador %=
    print("El resultado de modulo o resto es: ", numero)

    
