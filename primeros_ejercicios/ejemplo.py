import keyboard as teclado

resultado_actual = 0
cantidad_operaciones = 0
print("Calculadora")

def sumar(primer_numero, segundo_numero):
    global cantidad_operaciones
    total = primer_numero + segundo_numero
    cantidad_operaciones += 1
    return total

def restar(primer_numero, segundo_numero):
    global cantidad_operaciones
    diferencia = primer_numero - segundo_numero
    cantidad_operaciones += 1
    return diferencia

def multiplicar(primer_numero, segundo_numero):
    global cantidad_operaciones
    producto = primer_numero * segundo_numero
    cantidad_operaciones += 1
    return producto

def dividir(primer_numero, segundo_numero):
    global cantidad_operaciones
    cociente = primer_numero / segundo_numero
    cantidad_operaciones += 1
    return cociente

def realizar_operacion(primer_numero, segundo_numero, simbolo_operacion):
    global resultado_actual
    if simbolo_operacion == "+":
        resultado_actual = sumar(primer_numero, segundo_numero)
    elif simbolo_operacion == "-":
        resultado_actual = restar(primer_numero, segundo_numero)
    elif simbolo_operacion == "*":
        resultado_actual = multiplicar(primer_numero, segundo_numero)
    elif simbolo_operacion == "/":
        resultado_actual = dividir(primer_numero, segundo_numero)
    else:
        print("Operación no válida")
        return
    print("Resultado:", resultado_actual)
    print("Cantidad de operaciones:", cantidad_operaciones)

while True:
    if teclado.is_pressed('esc'):
        print("Programa finalizado por tecla ESC")
        break
    if teclado.is_pressed('backspace'):
        resultado_actual = 0
        cantidad_operaciones = 0
        print("Reiniciado por backspace")
        continue
        if resultado_actual == 0:
            primer_numero = float(input("Ingrese el primer número: "))
            simbolo_operacion = input("Ingrese la operación (+, -, *, /): ")
            segundo_numero = float(input("Ingrese el segundo número: "))
            realizar_operacion(primer_numero, segundo_numero, simbolo_operacion)
        else:
            simbolo_operacion = input("Ingrese la operación (+, -, *, /): ")
            segundo_numero = float(input("Ingrese el siguiente número: "))
            realizar_operacion(resultado_actual, segundo_numero, simbolo_operacion)