frase = input("Ingrese una frase o palabra: ")
lista_de_letras = list(frase)

contadorVocales = 0
for letra in lista_de_letras:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        contadorVocales += 1

print("La cantidad de vocales dentro de su palabra o frase es de: " , contadorVocales)
