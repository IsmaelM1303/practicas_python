lista_de_numeros = input("Escriba una lista de números separados por una coma: ")

lista_iterada = lista_de_numeros.split(",")
contador_pares = 0
contador_impares = 0
for numero in lista_iterada:
    numero = int(numero.strip())
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
print("La cantidad de números pares es de:", contador_pares, ". Mientras que la cantidad de números impares es de:", contador_impares)