
class Temperature:

    def __init__(self, value, unit="C"):

        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Unit is not valid")

        if unit == "C" and value < -273.15:
            raise ValueError("Temperature below absolute zero")

        elif unit == "F" and value < -459.67:
            raise ValueError("Temperature below absolute zero")

        elif unit == "K" and value < 0:
            raise ValueError("Temperature below absolute zero")

        self._value = value
        self._unit = unit

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def to_celsius(self):
        if self.unit == "C":
            return float(self.value)

        elif self.unit == "F":
            return (self.value - 32) * 5 / 9

        elif self.unit == "K":
            return self.value - 273.15

    def to_fahrenheit(self):
        if self.unit == "F":
            return float(self.value)

        elif self.unit == "C":
            return (self.value * 9 / 5) + 32

        elif self.unit == "K":
            return ((self.value - 273.15) * 9 / 5) + 32

    def to_kelvin(self):
        if self.unit == "K":
            return float(self.value)

        elif self.unit == "C":
            return self.value + 273.15

        elif self.unit == "F":
            return ((self.value - 32) * 5 / 9) + 273.15

    def convert_to(self, target_unit):
        target_unit = target_unit.upper()

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")

        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")

        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")

        else:
            raise ValueError("Target unit is not valid")

    def __str__(self):
        return f"{self.value:.2f} °{self.unit}"

    def __repr__(self):
        return f"Temperature({self.value!r}, {self.unit!r})"

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_celsius() - other.to_celsius()) <= 1e-9

    def __ne__(self, other):
        result = self.__eq__(other)

        if result is NotImplemented:
            return NotImplemented

        return not result

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() < other.to_celsius() - 1e-9

    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() <= other.to_celsius() + 1e-9

    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() > other.to_celsius() + 1e-9

    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() >= other.to_celsius() - 1e-9