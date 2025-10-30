valores = {
    "a": 3.14159,
    "b": 2.71828,
    "c": 1.61803,
    "d": 4.56789
}

print("Diccionario original:")
print(valores)

valores_redondeados = {}

for clave, valor in valores.items():
    valor_redondeado = round(valor)
    
    valores_redondeados[clave] = valor_redondeado

print("Diccionario con valores redondeados:" )
print(valores_redondeados)
