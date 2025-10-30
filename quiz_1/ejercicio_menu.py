import os
import time
import random

programa = True

"""Para limpiar la consola"""
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


"""Listas de información necesarias"""

mensajes = [
    "Cree en ti mismo y todo será posible.",
    "Cada día es una nueva oportunidad para mejorar.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No cuentes los días, haz que los días cuenten.",
    "La disciplina es el puente entre metas y logros.",
    "Fracasar no es caer, es negarse a levantarse.",
    "Haz hoy lo que otros no quieren, y mañana vivirás como otros no pueden.",
    "El único límite a tus sueños eres tú mismo.",
    "La constancia convierte lo imposible en inevitable.",
    "Nunca es tarde para ser la mejor versión de ti.",

    "Tu actitud determina tu altitud.",
    "El esfuerzo de hoy es el éxito de mañana.",
    "No tienes que ser grande para empezar, pero debes empezar para ser grande.",
    "Cada error te acerca un paso más al acierto.",
    "La motivación te impulsa, pero la disciplina te mantiene.",
    "Sueña en grande, trabaja duro y mantén la humildad.",
    "El dolor que sientes hoy será la fuerza que sentirás mañana.",
    "No dejes que el miedo decida tu futuro.",
    "La perseverancia convierte lo ordinario en extraordinario.",
    "Haz de tu vida un sueño, y de tu sueño una realidad."
]

lista_nombres = [
    "Sofía",
    "Mateo",
    "Valentina",
    "Sebastián",
    "Camila"
]

"""La función que muestra los mensajes"""

def mensaje():
    global mensajes
    while True:
        limpiar()
        ver_mensaje = random.choice(mensajes)
        print(ver_mensaje)
        print("")
        print("---------------------------------")
        print(" (1) Ver otro mensaje (2) Volver")
        print("---------------------------------")
        print("")
        opcion_mensaje = input("Elija una opción: ").strip()
        if opcion_mensaje == "1":
            mensaje()
        elif opcion_mensaje == "2":
            break

"""La función que muestra los nombres"""

def nombres():
    while True:
        limpiar()
        global lista_nombres

        for nombre in lista_nombres:
            print(nombre)
            print("-----------")
        print("")
        print("---------------------------------")
        print("          (1) Volver")
        print("---------------------------------")
        print("")
        opcion_mensaje = input("Elija una opción: ").strip()
        if opcion_mensaje == "1":
            break
        else:
            print("Elija una opción válida")
            time.sleep(2)


"""El menú principal"""

def menu ():
    global programa
    while programa:
        limpiar()
        print("----------------------------------------------------")
        print(" (1)Mostrar un mensaje (2)Mostrar nombres (3)Salir")
        print("----------------------------------------------------")
        print("")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            mensaje()
        elif opcion == "2":
            nombres()
        elif opcion == "3":
            print("Muchas gracias por usar este programa")
            time.sleep(2)
            programa = False
        else:
            print("Elija una opción válida")
            time.sleep(2)

"""Lo que inicia el programa"""
menu()
