#Libro.py

#Aquí hago los imports

class Libro:

    #Contructor
    def __init__(self, titulo, autor, anio, tipo, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.tipo = tipo
        self.disponible = disponible

    def mostrar_info(self):
        print("------------------------------------------------")
        print(f"Título del libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio}")
        print("El libro es formato digital") if tipo == "d" else print ("El libro es formato físico")
        print("El libro que busca está disponible") if self.disponible == True else print("El libro que busca no está disponible")
        print("------------------------------------------------")

    def alquilar(self):
        self.disponible = False
        print("------------------------------------------------")
        print("        El libro le ha sido entregado")
        print("------------------------------------------------")

    def devolver(self):
        self.disponible = True
        print("------------------------------------------------")
        print("        El libro ha sido devuelto")
        print("------------------------------------------------")
