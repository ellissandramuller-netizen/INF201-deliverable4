import pytest
from fraction import Fraction

def test_initialization():
    fraction = Fraction(3, 4)

    assert fraction.numerator == 3
    assert fraction.denominator == 4


# Test invalid numerator and denominator types
def test_invalid_types():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)

    with pytest.raises(TypeError):
        Fraction(1, "2")

    with pytest.raises(TypeError):
        Fraction(True, 2)


# Test invalid denominator values
def test_invalid_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)

    with pytest.raises(ValueError):
        Fraction(1, -2)


# Test all six comparison operators
def test_comparisons():
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    c = Fraction(1, 3)

    assert a == b
    assert a != c
    assert c < a
    assert c <= a
    assert a <= b
    assert a > c
    assert a >= c
    assert a >= b


# Test string representations
def test_string_methods():
    fraction = Fraction(1, 2)

    assert str(fraction) == "1/2"
    assert repr(fraction) == "Fraction(1, 2)"


# Test addition
def test_addition():
    result = Fraction(1, 2) + Fraction(1, 4)
    assert result == Fraction(3, 4)


# Test multiplication
def test_multiplication():
    result = Fraction(1, 2) * Fraction(2, 3)
    assert result == Fraction(1, 3)


# Test unsupported comparisons
def test_unsupported_comparisons():
    assert Fraction(1, 2) != "hello"

    with pytest.raises(TypeError):
        Fraction(1, 2) < "hello"
