contador = False
def validaciones():
    edad = int(input("Ingrese su edad: "))

    if validacionNino(edad):
        return "Es niño"
    elif validacionAdolescente(edad):
        return "Es adolescente"
    elif validacionAdulto(edad):
        return "Es adulto"
    elif validacionAdultoMayor(edad):
        return "Es adulto mayor"
    else:
        return "Edad no válida"

def validacionNino(edad):
    return edad < 13

def validacionAdolescente(edad):
    return 13 <= edad < 18

def validacionAdulto(edad):
    return 18 <= edad < 60

def validacionAdultoMayor(edad):
    return edad >= 60

while contador == False:
    opcion = input("Desea hacer una validación de edad y/n: ")
    if opcion == "y":
        print(validaciones())
    elif opcion == "n":
        contador = True
    else:
        print("Opción incorrecta")
