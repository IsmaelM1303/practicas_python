#LibroDigital.py

#Aquí hago los imports
from Libro import Libro

class LibroDigital(Libro):

    def __init__(self, titulo, autor, anio, tipo, disponible, peso_mb):
        super().__init__(titulo, autor, anio, tipo, disponible)
        self.peso_mb = peso_mb
    
    def mostrar_info(self):
        print("------------------------------------------------")
        print(f"Título del libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio}")
        print("El libro es formato digital")
        print(f"El libro tiene {self.peso_mb} páginas")
        print("El libro que busca está disponible") if self.disponible == True else print("El libro que busca no está disponible")
        print("------------------------------------------------")