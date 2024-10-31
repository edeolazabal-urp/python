# test_main.py

import pytest
from main import suma

def test_suma_positivos():
    assert suma(1, 2) == 3

def test_suma_negativos():
    assert suma(-1, -2) == -3

def test_suma_cero():
    assert suma(0, 0) == 0

def test_suma_mixto():
    assert suma(-1, 1) == 0
    
@pytest.mark.parametrize("x, y, resultado", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_suma_parametrizada(x, y, resultado):
    assert suma(x, y) == resultado
    