#Auto.py
#Aquí hago los imports
from ..Vehiculo import Vehiculo

class Auto (Vehiculo):
    def __init__(self, puertas, marca, modelo, año, velocidad=0, encendido=False):
        super(). __init__(marca, modelo, año, velocidad=0, encendido=False)
        self.puertas = puertas
        

    def abrir_puertas(self):
        print(f"Se han abierto las {self.puertas} puertas del auto {self.marca} {self.modelo}")

    def tocar_bocina(self):
        print("¡Piiiiip! 🚗")

    def poner_radio(self):
        print("Radio encendida en el auto")

    def usar_aire(self):
        print("Aire acondicionado funcionando")

    def estacionar(self):
        if self.velocidad == 0:
            print(f"El auto {self.marca} {self.modelo} está estacionado")
        else:
            print("No puedes estacionar mientras el auto está en movimiento")