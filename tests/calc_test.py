import pytest

from src.calc import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(4, 6) == 10;

def test_multiply():
    assert calc.multiply(12, 3) == 36;

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 8),
        (-2, 7, 5),
        (0, 0, 0)
    ]
)
def test_sum(a, b, expected):
    """Проверка сложения"""
    assert calc.sum(a, b) == expected