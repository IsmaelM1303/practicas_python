import os

"""Para limpiar la consola"""
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

inventario = {}

def mostrar_inventario():
    limpiar()
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario actual:")
    for nombre, datos in inventario.items():
        print(f"- {nombre}: cantidad = {datos['cantidad']}, precio = {datos['precio']}")

def agregar_producto():
    limpiar()
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("Nombre inválido.")
        return
    if nombre in inventario:
        print("El producto ya existe. Use modificar cantidad para cambiarla.")
        return
    cantidad_texto = input("Cantidad (entero): ").strip()
    if not cantidad_texto.isdigit():
        print("Cantidad inválida.")
        return
    precio_texto = input("Precio (ej. 12.50): ").strip()
    try:
        precio_valor = float(precio_texto)
    except:
        print("Precio inválido.")
        return
    inventario[nombre] = {"cantidad": int(cantidad_texto), "precio": precio_valor}
    print("Producto agregado.")

def modificar_cantidad():
    limpiar()
    nombre = input("Nombre del producto a modificar: ").strip()
    if nombre not in inventario:
        print("Producto no encontrado.")
        return
    cantidad_texto = input("Nueva cantidad (entero): ").strip()
    if not cantidad_texto.isdigit():
        print("Cantidad inválida.")
        return
    inventario[nombre]["cantidad"] = int(cantidad_texto)
    print("Cantidad actualizada.")

def eliminar_producto():
    limpiar()
    nombre = input("Nombre del producto a eliminar: ").strip()
    if nombre not in inventario:
        print("Producto no encontrado.")
        return
    del inventario[nombre]
    print("Producto eliminado.")

def menu():
    while True:
        limpiar()
        print("")
        print("1) Ver inventario")
        print("2) Agregar producto")
        print("3) Modificar cantidad")
        print("4) Eliminar producto")
        print("5) Salir")
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            limpiar()
            mostrar_inventario()
        elif opcion == "2":
            limpiar()
            agregar_producto()
        elif opcion == "3":
            limpiar()
            modificar_cantidad()
        elif opcion == "4":
            limpiar()
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()