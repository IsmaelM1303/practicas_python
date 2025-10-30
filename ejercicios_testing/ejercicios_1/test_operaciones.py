import pytest
from operaciones import suma, resta, multiplicar, dividir

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 4) == -4

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
