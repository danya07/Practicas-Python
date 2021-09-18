# Si es mayor de 18
# --------------------------------
# Licencia de conducir
# Nombre y Apellido
# ## años
# Direccion completita
# --------------------------------
# Si es mayor de 16
# --------------------------------
# Permiso de conducir
# Nombre y Apellido
# ## años
# Direccion
# --------------------------------
# Si es menor de 16
# --------------------------------
# No tienes la edad para cunducir

def run():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    direccion = input("Onde vives?: ")
    if int(edad) >= 18:
        print("Nombre:", nombre, "\n", "Edad:", edad, "\n", "Su direshion:", direccion, "\n" "Tienes: Licencia de conducir FELICIDADESSSS!!!")
    elif int(edad) <= 15:
        print("Nombre:", nombre, "\n", "Edad:", edad, "\n", "Su direshion:", direccion, "\n" "No tienes permiso ni licencia luseeeeeeeeeer")
    else:
        print("Nombre:", nombre, "\n", "Edad:", edad, "\n", "Su direshion:", direccion, "\n" "Tienes Permiso de conducir FELICIDADES, SIGUE CRECIENDO!!!")

if __name__ == '__main__':
    run()


