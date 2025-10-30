def es_palindromo(palabra):
    palabra_limpia = palabra.lower().replace(" ", "")
    return palabra_limpia == palabra_limpia[::-1]

def contar_vocales(texto):
    texto = texto.lower()
    vocales = "aeiou"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador
    