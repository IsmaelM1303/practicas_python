import random
import os
import time

"""Limpiar"""
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def alto_bajo(intento, numero):
    if intento > numero:
        return "El número es más bajo que eso..."
    elif intento < numero:
        return "El número es más alto que eso..."
    elif intento == numero:
        return "ganador"


def juego_numero():
    numero = random.randint(1, 100)
    intento = 0
    intentos = 0
    while True:
        limpiar()
        print("--------------------------------------------------------------------")
        if intento == 0:
            print("Bienvenido, Estoy pensando en un número... Crees poder adivinar?")
        else:
            resultado = alto_bajo(intento, numero)
            if resultado == "ganador":
                print("¡Has ganado!")
                print("Gracias por jugar")
                print("-------------------------------------------------------------------")
                time.sleep(2)
                break
            print(resultado)
            intentos += 1
        print("--------------------------------------------------------------------")
        print("Usted lleva una cantidad de: ", intentos, " intentos")
        intento = int(input("Adivine el número: "))
juego_numero()