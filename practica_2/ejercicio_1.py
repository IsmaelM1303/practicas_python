numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_par(numero):
    return numero % 2 == 0

numeros_pares = list(filter(es_par, numeros))

print(numeros_pares)