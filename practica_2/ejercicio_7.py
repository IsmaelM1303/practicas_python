palabras = ["sol", "montaña", "camino", "ola", "viento", "mar"]

def es_larga(palabra):
    return len(palabra) >= 5

palabras_largas = list(filter(es_larga, palabras))

print("Lista original de palabras:")
print(palabras)

print("\nPalabras con 5 o más letras:")
print(palabras_largas)
