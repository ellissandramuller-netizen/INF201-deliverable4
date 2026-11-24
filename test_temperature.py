import pytest
from temperature import Temperature


# --------------------------------------------------
# Initialization and read-only attributes
# --------------------------------------------------

# Check that Celsius is the default temperature unit
def test_default_unit():
    temp = Temperature(25)
    assert temp.unit == "C"


# Check that lowercase units are accepted and stored as uppercase
def test_case_insensitive_units():
    temp1 = Temperature(25, "c")
    temp2 = Temperature(77, "f")
    temp3 = Temperature(300, "k")

    assert temp1.unit == "C"
    assert temp2.unit == "F"
    assert temp3.unit == "K"


# Verify that value and unit cannot be modified after initialization
def test_read_only_attributes():
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 100

    with pytest.raises(AttributeError):
        temp.unit = "K"


# --------------------------------------------------
# Unit validation and absolute zero
# --------------------------------------------------

# Check that invalid temperature units raise ValueError
def test_invalid_units():
    with pytest.raises(ValueError):
        Temperature(25, "X")

    with pytest.raises(ValueError):
        Temperature(25, "Celsius")

    with pytest.raises(ValueError):
        Temperature(25, "")


# Verify that temperatures below absolute zero are rejected
def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-274, "C")

    with pytest.raises(ValueError):
        Temperature(-460, "F")

    with pytest.raises(ValueError):
        Temperature(-1, "K")


# Check that temperatures exactly at absolute zero are allowed
def test_absolute_zero():
    temp_c = Temperature(-273.15, "C")
    temp_f = Temperature(-459.67, "F")
    temp_k = Temperature(0, "K")

    assert temp_c.value == -273.15
    assert temp_f.value == -459.67
    assert temp_k.value == 0


# --------------------------------------------------
# Temperature conversions
# --------------------------------------------------

# Test conversions using five reference points from the assignment
def test_temperature_conversions():
    reference_points = [
        (-273.15, -459.67, 0),
        (-40, -40, 233.15),
        (0, 32, 273.15),
        (37, 98.6, 310.15),
        (100, 212, 373.15)
    ]

    # Compare conversions between all three temperature units
    for c, f, k in reference_points:
        temp_c = Temperature(c, "C")
        temp_f = Temperature(f, "F")
        temp_k = Temperature(k, "K")

        # Use a tolerance of 1e-9 to account for floating-point errors
        assert temp_c.to_fahrenheit() == pytest.approx(f, abs=1e-9)
        assert temp_c.to_kelvin() == pytest.approx(k, abs=1e-9)

        assert temp_f.to_celsius() == pytest.approx(c, abs=1e-9)
        assert temp_f.to_kelvin() == pytest.approx(k, abs=1e-9)

        assert temp_k.to_celsius() == pytest.approx(c, abs=1e-9)
        assert temp_k.to_fahrenheit() == pytest.approx(f, abs=1e-9)


# Verify that conversion methods return float values
def test_conversion_return_types():
    temp = Temperature(25, "C")

    assert isinstance(temp.to_celsius(), float)
    assert isinstance(temp.to_fahrenheit(), float)
    assert isinstance(temp.to_kelvin(), float)


# --------------------------------------------------
# Converting Temperature objects
# --------------------------------------------------

# Check that convert_to returns Temperature objects with correct values
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


# Verify that conversion creates a new object without modifying the original
def test_convert_to_new_object():
    temp = Temperature(25, "C")

    converted = temp.convert_to("F")

    assert converted is not temp
    assert temp.value == 25
    assert temp.unit == "C"


# Check that target units are case-insensitive and invalid units are rejected
def test_convert_to_unit_validation():
    temp = Temperature(25, "C")

    converted = temp.convert_to("f")

    assert converted.unit == "F"

    with pytest.raises(ValueError):
        temp.convert_to("X")


# Check conversion from Fahrenheit to Kelvin at absolute zero
def test_convert_absolute_zero():
    temp_f = Temperature(-459.67, "F")
    converted = temp_f.convert_to("K")

    assert converted.value == pytest.approx(0, abs=1e-9)
    assert converted.unit == "K"


# --------------------------------------------------
# Round-trip conversions
# --------------------------------------------------

# Verify that converting C -> F -> K -> C preserves the original temperature
def test_round_trip_conversion():
    original = Temperature(25, "C")

    temp_f = original.convert_to("F")
    temp_k = temp_f.convert_to("K")
    temp_c = temp_k.convert_to("C")

    assert temp_c == original
    assert temp_c.value == pytest.approx(25, abs=1e-9)
    assert temp_c.unit == "C"


# --------------------------------------------------
# Temperature comparisons
# --------------------------------------------------

# Verify equality and inequality across different temperature units
def test_temperature_equality():
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")
    temp_k = Temperature(273.15, "K")

    assert temp_c == temp_f
    assert temp_c == temp_k
    assert temp_f == temp_k

    assert temp_c != Temperature(100, "C")


# Check ordering comparisons between freezing and boiling points
def test_temperature_ordering():
    freezing = Temperature(0, "C")
    boiling = Temperature(212, "F")

    assert freezing < boiling
    assert freezing <= boiling

    assert boiling > freezing
    assert boiling >= freezing


# Verify ordering operators when temperatures are equivalent
def test_equal_temperature_ordering():
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")

    assert temp_c <= temp_f
    assert temp_c >= temp_f

    assert not (temp_c < temp_f)
    assert not (temp_c > temp_f)


# Check that differences smaller than 1e-9 are treated as equal
def test_comparison_tolerance():
    temp1 = Temperature(25, "C")
    temp2 = Temperature(25 + 1e-10, "C")

    assert temp1 == temp2
    assert temp1 <= temp2
    assert temp1 >= temp2


# Verify that comparisons with unsupported types return NotImplemented
def test_comparison_with_other_types():
    temp = Temperature(25, "C")

    assert temp.__eq__(25) is NotImplemented
    assert temp.__ne__(25) is NotImplemented
    assert temp.__lt__(25) is NotImplemented
    assert temp.__le__(25) is NotImplemented
    assert temp.__gt__(25) is NotImplemented
    assert temp.__ge__(25) is NotImplemented


# --------------------------------------------------
# String representations
# --------------------------------------------------

# Check human-readable formatting and unambiguous representation
def test_string_representations():
    temp = Temperature(25.0, "C")

    assert str(temp) == "25.00 °C"
    assert repr(temp) == "Temperature(25.0, 'C')"


# Verify string formatting with different units and temperature values
def test_string_formatting():
    temp_c = Temperature(-40, "C")
    temp_f = Temperature(98.6, "F")
    temp_k = Temperature(300, "K")

    assert str(temp_c) == "-40.00 °C"
    assert str(temp_f) == "98.60 °F"
    assert str(temp_k) == "300.00 °K"