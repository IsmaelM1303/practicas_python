# matematica.py

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fibonacci(n):
    if n <= 0:
        return []
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]
