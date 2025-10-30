palabras = ["sol", "montaña", "camino", "viento", "ola"]

def longitud(palabra):
    return len(palabra)

longitudes = list(map(longitud, palabras))

print("Lista original de palabras:")
print(palabras)

print("\nLongitudes de cada palabra:")
print(longitudes)
