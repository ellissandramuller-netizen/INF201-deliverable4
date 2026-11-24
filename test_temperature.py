
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

def test_temperature_conversions():
    reference_points = [
        (-273.15, -459.67, 0),
        (-40, -40, 233.15),
        (0, 32, 273.15),
        (37, 98.6, 310.15),
        (100, 212, 373.15)
    ]

    for c, f, k in reference_points:
        temp_c = Temperature(c, "C")
        temp_f = Temperature(f, "F")
        temp_k = Temperature(k, "K")

        assert temp_c.to_fahrenheit() == pytest.approx(f, abs=1e-9)
        assert temp_c.to_kelvin() == pytest.approx(k, abs=1e-9)

        assert temp_f.to_celsius() == pytest.approx(c, abs=1e-9)
        assert temp_f.to_kelvin() == pytest.approx(k, abs=1e-9)

        assert temp_k.to_celsius() == pytest.approx(c, abs=1e-9)
        assert temp_k.to_fahrenheit() == pytest.approx(f, abs=1e-9)

def test_conversion_return_types():
    temp = Temperature(25, "C")

    assert isinstance(temp.to_celsius(), float)
    assert isinstance(temp.to_fahrenheit(), float)
    assert isinstance(temp.to_kelvin(), float)

    