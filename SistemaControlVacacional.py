print("****************************************")
print("*SISTEMA DE CONTROL VACACIONAL DE RAPPI*")
print("****************************************")

nombre_empleado = input("Favor de introducir el nombre del empleado: ") # Se solicita el nombre del empleado
clave_departamento = int(input("Por favor, introduce la clave del departamento (1, 2, o 3): ")) # Se solicita la clave del departamento
antiguedad_empleado = float(input("Por favor introduce los años laborados del empleado: ")) # Se solicita la antigüedad del empleado

if clave_departamento == 1: # Se evalúa la clave del departamento, y se asignan los días de vacaciones correspondientes
    if antiguedad_empleado < 2: # Se evalúa la antigüedad del empleado, y se asignan los días de vacaciones correspondientes
        print(f"El empleado {nombre_empleado} tiene derecho a 6 días de vacaciones.")
    elif 2 <= antiguedad_empleado <= 6:
        print(f"El empleado {nombre_empleado} tiene derecho a 14 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print(f"El empleado {nombre_empleado} tiene derecho a 20 días de vacaciones.")
    else:
        print(f"El empleado {nombre_empleado} aún no tiene derecho a vacaciones.")

elif clave_departamento == 2:
    if antiguedad_empleado < 2:
        print(f"El empleado {nombre_empleado} tiene derecho a 7 días de vacaciones.")
    elif 2 <= antiguedad_empleado <= 6:
        print(f"El empleado {nombre_empleado} tiene derecho a 15 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print(f"El empleado {nombre_empleado} tiene derecho a 22 días de vacaciones.")
    else:
        print(f"El empleado {nombre_empleado} aún no tiene derecho a vacaciones.")

elif clave_departamento == 3:
    if antiguedad_empleado < 2:
        print(f"El empleado {nombre_empleado} tiene derecho a 10 días de vacaciones.")
    elif 2 <= antiguedad_empleado <= 6:
        print(f"El empleado {nombre_empleado} tiene derecho a 20 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print(f"El empleado {nombre_empleado} tiene derecho a 30 días de vacaciones.")
    else:
        print(f"El empleado {nombre_empleado} aún no tiene derecho a vacaciones.")

else:
    print(f"La clave del departamento ingresada ({clave_departamento}) no es válida.")
