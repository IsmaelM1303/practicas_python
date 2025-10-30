class CifradoCesar:
    def __init__(self, mensaje, cantidad_cifrado, abecedario):
        self.mensaje = mensaje
        self.cantidad_cifrado = cantidad_cifrado
        self.abecedario = list("abcdefghijklmnopqrstuvwxyz")

    def cifrar(self):
        mensaje_cifrado = []

        for letra in self.mensaje.lower():
            if letra in self.abecedario:
                pos = self.abecedario.index(letra)
                nueva_pos = (pos + self.cantidad_cifrado) % len(self.abecedario)
                mensaje_cifrado.append(self.abecedario[nueva_pos])

            elif letra == "ñ":
                pos = self.abecedario.index("n")
                nueva_pos = (pos + self.cantidad_cifrado) % len(self.abecedario)
                mensaje_cifrado.append(self.abecedario[nueva_pos])

            else:
                mensaje_cifrado.append(letra)

        return "".join(mensaje_cifrado)

mensaje = input("Escriba el mensaje que quiere cifrar: ")

while True:
    cantidad = input("Escriba la cantidad de espacios que quiere para el cifrado: ")
    if cantidad.isdigit():
        cantidad = int(cantidad)
        break
    else:
        print("Solo se permiten números enteros positivos. Intente de nuevo.")

solicitud = CifradoCesar(mensaje, cantidad, list("abcdefghijklmnopqrstuvwxyz"))
mensaje_cifrado = solicitud.cifrar()
print("Mensaje cifrado:", mensaje_cifrado)