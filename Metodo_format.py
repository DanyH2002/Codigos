#alternativa 1
nombre = "Carlos"
edad = 22

# Con las llaves se indica que se va a sustituir por una variable, 
# y con el método format se indica que se va a sustituir por la variable que se le indique en el orden que se le indique.

print("Hola {}, tienes {} años.".format(nombre, edad)) 

#Alternativa 2
nombre = "Carlos"
edad = 22

# Con las llaves se indica que se va a sustituir por una variable,
# que estan dentro de las llaves, y con el método format se indica 
# que se va a sustituir por la variable que se le indique en el orden que se le indique.
print("Hola {nombre}, tienes {edad} años.".format(nombre = "Carlos", edad = 22))


#Alternativa 3
nombre = "Carlos"
edad = 22

# Con el método f se indica que se va a sustituir por una variable,
# que estan dentro de las llaves, y se inidca el nombre de la variable acorde
# al indice de la variable que se le indique en el orden que se le indique.
print("Hola {1}, tienes {0} años.".format(edad, nombre))

