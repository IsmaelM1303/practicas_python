#Barco.py

#Aquí hago los imports
from ..Vehiculo import Vehiculo

class Barco(Vehiculo):
    def __init__(self, marca, modelo, año, tipo, velocidad=0, encendido=False):
        super().__init__(marca, modelo, año, velocidad, encendido)
        self.tipo = tipo  # velero, crucero, lancha

    def zarpar(self):
        print(f"El barco {self.marca} {self.modelo} ha zarpado 🚢")

    def fondear(self):
        print("El barco ha echado el ancla")

    def encender_motor(self):
        print("Motor del barco encendido")

    def desplegar_velas(self):
        print("Velas desplegadas")

    def usar_radar(self):
        print("Radar activado para navegación")
