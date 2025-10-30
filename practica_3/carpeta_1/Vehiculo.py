#Vehiculo.py

#Aquí hago los imports
import os
import time

class Vehiculo:
    
    #Esto es para limpiar la consola siempre que necesite
    def limpiar_consola(self):
        os.system("cls")

    #Aquí declaro los atributos de la clase
    def __init__(self, marca, modelo, año, velocidad=0, encendido=False):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = velocidad
        self.encendido = encendido

    #Aquí hago los métodos de la clase

    #Métodos de encendido y apagado
    def encender(self):
        self.encendido = True
        print(f"Ahora el vehículo {self.marca} está encendido")

    def apagar(self):
        self.encendido = False
        print(f"Ahora el vehículo {self.marca} está apagado")

    #Métodos de aceleración y freno
    def acelerar(self, limite=90):
        print("Preparando para acelerar...")
        time.sleep(2) 
        contador = 1
        while contador <= limite:
            self.limpiar_consola()
            self.velocidad += 1
            print(f"Velocidad actual: {self.velocidad}")
            contador += 1

    def frenar(self, limite=0):
        print("Preparando para frenar...")
        time.sleep(2) 
        while self.velocidad > limite:
            self.limpiar_consola()
            self.velocidad -= 1
            print(f"Velocidad actual: {self.velocidad}")

    #Método para mostrar información
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año del vehículo: {self.año}")
        print(f"Velocidad actual del vehículo: {self.velocidad}")
        print("El vehículo se encuentra encendido" if self.encendido else "El vehículo se encuentra apagado")
