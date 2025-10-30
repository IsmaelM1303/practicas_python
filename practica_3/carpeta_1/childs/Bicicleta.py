#Bicicleta.py

#Aquí hago los imports
from ..Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo, velocidad=0, encendido=False):
        super().__init__(marca, modelo, año, velocidad, encendido)
        self.tipo = tipo  # montaña, ruta, BMX

    def pedalear(self):
        print(f"La bicicleta {self.marca} {self.modelo} está pedaleando 🚴")

    def frenar_mano(self):
        print("Frenando con el freno de mano")

    def cambiar_marcha(self, marcha):
        print(f"Cambiando a la marcha {marcha}")

    def sonar_timbre(self):
        print("¡Ring ring!")

    def estacionar(self):
        print("La bicicleta está apoyada en el soporte")
