lista_de_numeros_decimales = [4.3, 5.7, 8.2, 9.9, 2.5]

def redondear_numero(numero_decimal):
    numero_redondeado = round(numero_decimal)
    return numero_redondeado

lista_de_numeros_redondeados = list(map(redondear_numero, lista_de_numeros_decimales))

print("Lista original de números decimales:")
print(lista_de_numeros_decimales)

print("\nLista de números redondeados:")
print(lista_de_numeros_redondeados)
