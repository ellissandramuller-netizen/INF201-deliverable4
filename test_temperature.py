
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

def test_convert_to():
    temp = Temperature(25, "C")

    converted_f = temp.convert_to("F")
    converted_k = temp.convert_to("K")

    assert isinstance(converted_f, Temperature)
    assert isinstance(converted_k, Temperature)

    assert converted_f.value == pytest.approx(77, abs=1e-9)
    assert converted_k.value == pytest.approx(298.15, abs=1e-9)

    assert converted_f.unit == "F"
    assert converted_k.unit == "K"

def test_convert_to_new_object():
    temp = Temperature(25, "C")

    converted = temp.convert_to("F")

    assert converted is not temp
    assert temp.value == 25
    assert temp.unit == "C"

def test_convert_to_unit_validation():
    temp = Temperature(25, "C")

    converted = temp.convert_to("f")

    assert converted.unit == "F"

    with pytest.raises(ValueError):
        temp.convert_to("X")

def test_round_trip_conversion():
    original = Temperature(25, "C")

    temp_f = original.convert_to("F")
    temp_k = temp_f.convert_to("K")
    temp_c = temp_k.convert_to("C")

    assert temp_c == original
    assert temp_c.value == pytest.approx(25, abs=1e-9)
    assert temp_c.unit == "C"

def test_temperature_equality():
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")
    temp_k = Temperature(273.15, "K")

    assert temp_c == temp_f
    assert temp_c == temp_k
    assert temp_f == temp_k

    assert temp_c != Temperature(100, "C")

def test_temperature_ordering():
    freezing = Temperature(0, "C")
    boiling = Temperature(212, "F")

    assert freezing < boiling
    assert freezing <= boiling

    assert boiling > freezing
    assert boiling >= freezing

def test_equal_temperature_ordering():
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")

    assert temp_c <= temp_f
    assert temp_c >= temp_f

    assert not (temp_c < temp_f)
    assert not (temp_c > temp_f)

def test_comparison_tolerance():
    temp1 = Temperature(25, "C")
    temp2 = Temperature(25 + 1e-10, "C")

    assert temp1 == temp2
    assert temp1 <= temp2
    assert temp1 >= temp2
