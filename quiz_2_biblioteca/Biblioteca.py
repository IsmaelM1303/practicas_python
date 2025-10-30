# Biblioteca.py

from childs_Libro.LibroDigital import LibroDigital
from childs_Libro.LibroImpreso import LibroImpreso
import os
import time

class Biblioteca:

    # Lista quemada de libros para iniciar
    def __init__(self):
        self.inventario = [
            LibroDigital("1984", "George Orwell", 1949, "d", True, 1.2),
            LibroDigital("El Principito", "Antoine de Saint-Exupéry", 1943, "d", True, 0.8),
            LibroImpreso("Cien años de soledad", "Gabriel García Márquez", 1967, "f", True, 471),
            LibroImpreso("Don Quijote", "Miguel de Cervantes", 1605, "f", False, 863)
        ]

    # método para limpiar la consola
    def limpiar(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # método para añadir libros
    def guardar_libros(self):
        while True:
            self.limpiar()
            print("")
            print("1) Añadir libro")
            print("2) Volver")
            opcion = input("Elija una opción: ").strip()
            if opcion == "1":
                self.limpiar()
                print("Qué tipo de libro desea añadir:")
                print("1) Físico")
                print("2) Digital")
                print("3) Volver")
                tipo = input("Elija un tipo: ")

                if tipo == "1":
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    anio = int(input("Año de publicación: "))
                    disponible = True
                    paginas = int(input("Número de páginas: "))
                    nuevo = LibroImpreso(titulo, autor, anio, "f", disponible, paginas)
                    self.inventario.append(nuevo)
                    print("Libro físico añadido con éxito.")
                    time.sleep(2)

                elif tipo == "2":
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    anio = int(input("Año de publicación: "))
                    disponible = True
                    tamano = float(input("Tamaño del archivo (MB): "))
                    nuevo = LibroDigital(titulo, autor, anio, "d", disponible, tamano)
                    self.inventario.append(nuevo)
                    print("Libro digital añadido con éxito.")
                    time.sleep(2)

                elif tipo == "3":
                    print("Volviendo . . . ")
                    time.sleep(2)
                    continue
                else:
                    print("Tipo inválido")
                    time.sleep(2)
                    continue

            elif opcion == "2":
                print("Volviendo . . .")
                time.sleep(2)
                break
            else:
                print("Opción inválida.")
                time.sleep(2)

    # método para mostrar libros
    def mostrar_libros(self):
        self.limpiar()
        print("=== Inventario de libros ===")
        if not self.inventario:
            print("No hay libros en la biblioteca.")
        else:
            for i, libro in enumerate(self.inventario, start=1):
                estado = "Disponible" if libro.disponible else "No disponible"
                tipo = "Digital" if libro.tipo == "d" else "Físico"
                print(f"{i}) {libro.titulo} - {libro.autor} ({libro.anio}) [{tipo}] [{estado}]")
        input("\nPresione Enter para continuar...")

    # método para alquiler y devolución
    def alquiler_devolucion(self):
        while True:
            self.limpiar()
            print("1) Alquilar libro")
            print("2) Devolver libro")
            print("3) Volver")
            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                self.mostrar_libros()
                indice = int(input("Ingrese el número del libro a alquilar: ")) - 1
                if 0 <= indice < len(self.inventario):
                    if self.inventario[indice].disponible:
                        self.inventario[indice].disponible = False
                        print("Libro alquilado con éxito.")
                    else:
                        print("El libro no está disponible.")
                else:
                    print("Índice inválido.")
                time.sleep(2)

            elif opcion == "2":
                self.mostrar_libros()
                indice = int(input("Ingrese el número del libro a devolver: ")) - 1
                if 0 <= indice < len(self.inventario):
                    if not self.inventario[indice].disponible:
                        self.inventario[indice].disponible = True
                        print("Libro devuelto con éxito.")
                    else:
                        print("Ese libro ya estaba disponible.")
                else:
                    print("Índice inválido.")
                time.sleep(2)

            elif opcion == "3":
                print("Volviendo . . .")
                time.sleep(2)
                break
            else:
                print("Opción inválida.")
                time.sleep(2)

    # método que funciona como menú
    def menu(self):
        while True:
            self.limpiar()
            print("")
            print("1) Guardar libros")
            print("2) Mostrar los libros disponibles")
            print("3) Alquiler y devolución")
            print("4) Salir")
            opcion = input("Elija una opción: ").strip()
            if opcion == "1":
                self.guardar_libros()
            elif opcion == "2":
                self.mostrar_libros()
            elif opcion == "3":
                self.alquiler_devolucion()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")
                time.sleep(2)

# Ejecutar el menú si este archivo se corre directamente
if __name__ == "__main__":
    app = Biblioteca()
    app.menu()
