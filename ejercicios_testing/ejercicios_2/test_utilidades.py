# test_utilidades.py

from utilidades import formatear_nombre, es_correo_valido, contar_palabras

def test_formatear_nombre():
    assert formatear_nombre("juan pérez") == "Juan Pérez"
    assert formatear_nombre("MARÍA LOPEZ") == "María Lopez"

def test_es_correo_valido():
    assert es_correo_valido("ejemplo@correo.com") == True
    assert es_correo_valido("malformado.com") == False
    assert es_correo_valido("otro@correo") == False

def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("Esto es una prueba de conteo") == 6
    assert contar_palabras("") == 0
