from contator import Contador

def test_incrementar():
    c = Contador()
    c.incrementar()
    assert c.valor == 1
    c.incrementar()
    assert c.valor == 2

def test_resetar():
    c = Contador()
    c.incrementar()
    c.resetar()
    assert c.valor == 0