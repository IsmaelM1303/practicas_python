palabras = ["sol", "ola", "montaña", "viento", "camino"]

palabras_mayusculas = []

def mayus(palabra):
    palabra_mayus = palabra.upper()
    palabras_mayusculas.append(palabra_mayus)
    return palabra_mayus

list(map(mayus, palabras))

print(palabras_mayusculas)
