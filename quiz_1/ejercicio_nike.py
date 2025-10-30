import os
import time

"""Para limpiar la consola"""
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

"""Lista de diccionarios"""
productos = [
    {
        "nombre": "Nike Air Zoom Pegasus 41",
        "categoria": "Running",
        "precio": 129.99,
        "colores": ["Negro", "Blanco", "Azul"],
        "tallas": [38, 39, 40, 41, 42, 43, 44],
        "disponible": True
    },
    {
        "nombre": "Nike Dunk Low Retro",
        "categoria": "Lifestyle",
        "precio": 119.99,
        "colores": ["Rojo/Blanco", "Negro/Gris"],
        "tallas": [36, 37, 38, 39, 40, 41, 42],
        "disponible": True
    },
    {
        "nombre": "Nike Pro Dri-FIT Camiseta",
        "categoria": "Entrenamiento",
        "precio": 34.99,
        "colores": ["Negro", "Gris", "Verde"],
        "tallas": ["S", "M", "L", "XL"],
        "disponible": False
    }
]

def editar():
    while True:
        limpiar()
        print("-----------------------------------")
        for producto in productos:
            print(f"{producto['nombre']} - ${producto['precio']}")
            print("-----------------------------------")
        print("")
        print("----------------------------------------------------")
        print("(1) Modificar producto (2) Eliminar producto (3) Volver")
        print("----------------------------------------------------")
        opcion_1 = input("Seleccione una opción: ").strip()

        if opcion_1 in ["1", "2"]:
            nombre = input("Escriba el nombre EXACTO del producto: ").strip()
            producto = next((p for p in productos if p["nombre"] == nombre), None)

            if not producto:
                print("Producto no encontrado.")
                input("Enter para continuar...")
                continue

            if opcion_1 == "1":
                print(f"Modificando {producto['nombre']}")
                nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
                if nuevo_precio:
                    try:
                        producto["precio"] = float(nuevo_precio)
                    except ValueError:
                        print("Precio inválido, no se modificó.")
                nuevo_estado = input("Disponible? (s/n, dejar vacío para no cambiar): ").strip().lower()
                if nuevo_estado == "s":
                    producto["disponible"] = True
                elif nuevo_estado == "n":
                    producto["disponible"] = False
                print("Producto modificado con éxito.")

            elif opcion_1 == "2":  # Eliminar
                productos.remove(producto)
                print("Producto eliminado con éxito.")

        elif opcion_1 == "3":
            break
        else:
            print("Elija una opción válida.")

        input("Enter para continuar...")

def menu():
    while True:
        limpiar()
        print("----------------------------------------------------")
        print(" (1) Editar el diccionario (2) Salir")
        print("----------------------------------------------------")
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            editar()
        elif opcion == "2":
            break
        else:
            print("Elija una opción válida")
            time.sleep(2)

menu()
