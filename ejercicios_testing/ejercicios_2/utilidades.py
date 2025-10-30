# utilidades.py

import re

def formatear_nombre(nombre):
    return nombre.title()

def es_correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def contar_palabras(texto):
    return len(texto.split())
