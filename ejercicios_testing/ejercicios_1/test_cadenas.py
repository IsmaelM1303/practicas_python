import pytest
from cadenas import es_palindromo, contar_vocales

def test_es_palindromo():
    assert es_palindromo("reconocer") == True
    assert es_palindromo("Anita lava la tina") == True
    assert es_palindromo("Hola mundo") == False

def test_contar_vocales():
    assert contar_vocales("Hola mundo") == 4
    assert contar_vocales("AEIOU") == 5
    assert contar_vocales("xyz") == 0
