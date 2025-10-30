numeros = [1, 2, 3, 4, 5]

nueva_lista = []

def triplica(numero):
    global nueva_lista
    nueva_lista.append(numero)
    nueva_lista.append(numero)
    nueva_lista.append(numero)
    return numero

list(map(triplica, numeros))

print(nueva_lista)
