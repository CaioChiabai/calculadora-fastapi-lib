import pytest
from calculator_lib import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(0, 0) == 1
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8
    assert power(2, 0.5) == pytest.approx(1.4142, 0.0001)
    assert power(9, 0.5) == pytest.approx(3, 0.0001)
    assert power(0, 5) == 0

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(2) == pytest.approx(1.4142, 0.0001)
    
    assert square_root(0) == 0

def test_square_root_negative():
    with pytest.raises(ValueError, match="Não é possível calcular a raiz quadrada de um número negativo."):
        square_root(-4)
