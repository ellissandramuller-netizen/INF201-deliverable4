
import pytest
from temperature import Temperature


def test_default_unit():
    temp = Temperature(25)
    assert temp.unit == "C"

def test_case_insensitive_units():
    temp1 = Temperature(25, "c")
    temp2 = Temperature(77, "f")
    temp3 = Temperature(300, "k")

    assert temp1.unit == "C"
    assert temp2.unit == "F"
    assert temp3.unit == "K"  

def test_read_only_attributes():
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 100

    with pytest.raises(AttributeError):
        temp.unit = "K"

def test_invalid_units():
    with pytest.raises(ValueError):
        Temperature(25, "X")

    with pytest.raises(ValueError):
        Temperature(25, "Celsius")

    with pytest.raises(ValueError):
        Temperature(25, "")

def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-274, "C")

    with pytest.raises(ValueError):
        Temperature(-460, "F")

    with pytest.raises(ValueError):
        Temperature(-1, "K")

def test_absolute_zero():
    temp_c = Temperature(-273.15, "C")
    temp_f = Temperature(-459.67, "F")
    temp_k = Temperature(0, "K")

    assert temp_c.value == -273.15
    assert temp_f.value == -459.67
    assert temp_k.value == 0