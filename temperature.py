
class Temperature:

    def __init__(self, value, unit):

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