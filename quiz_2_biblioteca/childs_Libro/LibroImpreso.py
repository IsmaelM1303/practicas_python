#LibroImpreso.py

#Aquí hago los imports
from Libro import Libro

class LibroImpreso(Libro):

    def __init__(self, titulo, autor, anio, tipo, disponible, num_paginas):
        super().__init__(titulo, autor, anio, tipo, disponible)
        self.num_paginas = num_paginas
    
    def mostrar_info(self):
        print("------------------------------------------------")
        print(f"Título del libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio}")
        print("El libro es formato físico")
        print(f"El libro tiene {self.num_paginas} páginas")
        print("El libro que busca está disponible") if self.disponible == True else print("El libro que busca no está disponible")
        print("------------------------------------------------")