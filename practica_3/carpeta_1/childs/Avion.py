#Avion.py

#Aquí hago los imports
from ..Vehiculo import Vehiculo


class Avion(Vehiculo):
    def __init__(self, marca, modelo, año, aerolinea, velocidad=0, encendido=False):
        super().__init__(marca, modelo, año, velocidad, encendido)
        self.aerolinea = aerolinea

    def despegar(self):
        print(f"El avión {self.marca} {self.modelo} está despegando ✈️")

    def aterrizar(self):
        print(f"El avión {self.marca} {self.modelo} está aterrizando")

    def desplegar_tren_aterrizaje(self):
        print("Tren de aterrizaje desplegado")

    def activar_piloto_automatico(self):
        print("Piloto automático activado")

    def comunicar_torre(self):
        print("Comunicando con la torre de control...")