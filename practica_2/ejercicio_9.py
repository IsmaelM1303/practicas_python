numeros = [-10, -5, 0, 3, 7, -2, 15, -8, 20]

def es_positivo(numero):
    return numero > 0

numeros_positivos = list(filter(es_positivo, numeros))

print("Lista original de números:")
print(numeros)

print("\nNúmeros positivos filtrados:")
print(numeros_positivos)
