lista_de_temperaturas_celsius = [0, 20, 30, 37, 100]

def convertir_celsius_a_fahrenheit(temperatura_en_celsius):
    temperatura_en_fahrenheit = temperatura_en_celsius * 9/5 + 32
    return temperatura_en_fahrenheit


lista_de_temperaturas_fahrenheit = list(map(convertir_celsius_a_fahrenheit, lista_de_temperaturas_celsius))

print("Lista original de temperaturas en Celsius:")
print(lista_de_temperaturas_celsius)

print("\nLista convertida a temperaturas en Fahrenheit:")
print(lista_de_temperaturas_fahrenheit)
