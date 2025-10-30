import os
import time
import random

programa = True

"""Para limpiar la consola"""
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


"""m -> km / km -> m"""

def metros_kilometros():
    while True:
        limpiar()
        print("")
        print("---------------------------------")
        print(" (1) metros a kilómetros (2) kilómetros a metros (3)Salir")
        print("---------------------------------")
        print("")
        opcion_m_km = input("Elija una opción: ").strip()
        if opcion_m_km == "1":
            m = int(input("Ingrese la cantidad de metros: "))
            resultado = float(m/1000)
            print("Resultado: ", m, "m, son ", resultado, "km")
            time.sleep(3)
            metros_kilometros()
        elif opcion_m_km == "2":
            km = int(input("Ingrese la cantidad de kilómetros: "))
            resultado = float(km*1000)
            print("Resultado: ", km, "km, son ", resultado, "m")
            time.sleep(3)
            metros_kilometros()
        elif opcion_m_km == "3":
            break

"""g -> kg / kg -> g"""

def gramos_kilogramos():
    while True:
        limpiar()
        print("")
        print("---------------------------------")
        print(" (1) gramos a kilogramos (2) kilgramos a gramos (3)Salir")
        print("---------------------------------")
        print("")
        opcion_g_kg = input("Elija una opción: ").strip()
        if opcion_g_kg == "1":
            g = int(input("Ingrese la cantidad de gramos: "))
            resultado = float(g/1000)
            print("Resultado: ", g, "g, son ", resultado, "kg")
            time.sleep(3)
            gramos_kilogramos()
        elif opcion_g_kg == "2":
            kg = int(input("Ingrese la cantidad de kilogramos: "))
            resultado = float(kg*1000)
            print("Resultado: ", kg, "kg, son ", resultado, "g")
            time.sleep(3)
            gramos_kilogramos()
        elif opcion_g_kg == "3":
            break

"""°C -> °F / °F -> °C"""
def centigrados_farenheit():
    while True:
        limpiar()
        print("")
        print("-------------------------------------------------------------------")
        print(" (1)Centígrados a Farenheit  (2) Farenheit a Centígrados (3)Salir")
        print("-------------------------------------------------------------------")
        print("")
        opcion_c_f = input("Elija una opción: ").strip()
        if opcion_c_f == "1":
            c = int(input("Ingrese la cantidad de grados Centígrados: "))
            resultado = float((c * 9/5) + 32)
            print("Resultado: ", c, "°C, son ", resultado, "°F")
            time.sleep(3)
            centigrados_farenheit()
        elif opcion_c_f == "2":
            f = int(input("Ingrese la cantidad de grados Farenheit: "))
            resultado = float((f - 32) * 5/9)
            print("Resultado: ", f, "°F, son ", resultado, "°C")
            time.sleep(3)
            centigrados_farenheit()
        elif opcion_c_f == "3":
            break



"""El menú principal"""

def menu ():
    global programa
    while programa:
        limpiar()
        print("                       Bienvenido al conversor de de unidades")
        print("-----------------------------------------------------------------------------------------")
        print("    (1)Metros a kilómetros (2)Gramos a kilogramos (3)Centígrados a Farenheit (4)Salir")
        print("-----------------------------------------------------------------------------------------")
        print("")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            metros_kilometros()
        elif opcion == "2":
            gramos_kilogramos()
        elif opcion == "3":
            centigrados_farenheit()
        elif opcion == "4":
            print("Muchas gracias por usar este programa")
            time.sleep(2)
            programa = False
        else:
            print("Elija una opción válida")
            time.sleep(2)

"""Lo que inicia el programa"""
menu()
