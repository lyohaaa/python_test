from src.calc import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(4, 6) == 10;


def test_multiply():
    assert calc.multiply(12, 3) == 36;