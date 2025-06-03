import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculadora import somar, subtrair, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_dividir():
    assert dividir(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)