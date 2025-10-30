nombre = input("Ingrese su nombre: ")

print("Bienvenido, " + nombre)

print("A continuación se solicitarán sus 2 notas para obtener el promedio")
def notas():
    nota1 = int(input("Ingrese su primera nota: "))
    nota2 = int(input("Ingrese su segunda nota: "))
    resultado = promedio(nota1, nota2)
    return resultado

def promedio(nota1, nota2):
    calificacionPromedio = (nota1+nota2)/2
    return calificacionPromedio

resultado = notas()
print("Su nota final es de: ", resultado)