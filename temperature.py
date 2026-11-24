class Temperature:
    # Tolerance used for floating-point comparisons
    TOLERANCE = 1e-9

    # --------------------------------------------------
    # Initialization and validation
    # --------------------------------------------------

    def __init__(self, value, unit="C"):
        # Convert unit to uppercase to allow case-insensitive input
        unit = unit.upper()

        # Check that the unit is supported
        if unit not in ("C", "F", "K"):
            raise ValueError("Unit is not valid")

        # Reject temperatures below absolute zero
        if unit == "C" and value < -273.15:
            raise ValueError("Temperature below absolute zero")

        elif unit == "F" and value < -459.67:
            raise ValueError("Temperature below absolute zero")

        elif unit == "K" and value < 0:
            raise ValueError("Temperature below absolute zero")

        # Store temperature values in private attributes
        self._value = value
        self._unit = unit

    # --------------------------------------------------
    # Read-only properties
    # --------------------------------------------------

    # Allow reading the temperature value without modifying it
    @property
    def value(self):
        return self._value

    # Allow reading the temperature unit without modifying it
    @property
    def unit(self):
        return self._unit

    # --------------------------------------------------
    # Temperature conversions
    # --------------------------------------------------

    # Convert the temperature to Celsius
    def to_celsius(self):
        if self.unit == "C":
            return float(self.value)

        elif self.unit == "F":
            return (self.value - 32) * 5 / 9

        elif self.unit == "K":
            return self.value - 273.15

    # Convert the temperature to Fahrenheit
    def to_fahrenheit(self):
        if self.unit == "F":
            return float(self.value)

        elif self.unit == "C":
            return (self.value * 9 / 5) + 32

        elif self.unit == "K":
            return ((self.value - 273.15) * 9 / 5) + 32

    # Convert the temperature to Kelvin
    def to_kelvin(self):
        if self.unit == "K":
            return float(self.value)

        elif self.unit == "C":
            return self.value + 273.15

        elif self.unit == "F":
            return ((self.value - 32) * 5 / 9) + 273.15

    # --------------------------------------------------
    # Conversion to new Temperature objects
    # --------------------------------------------------

    # Return a new Temperature object in the requested unit
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

    # --------------------------------------------------
    # String representations
    # --------------------------------------------------

    # Return a human-readable temperature with two decimal places
    def __str__(self):
        return f"{self.value:.2f} °{self.unit}"

    # Return an unambiguous representation of the Temperature object
    def __repr__(self):
        return f"Temperature({self.value!r}, {self.unit!r})"

    # --------------------------------------------------
    # Comparison operators
    # --------------------------------------------------

    # Compare temperatures for equality using Celsius and tolerance
    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_celsius() - other.to_celsius()) <= self.TOLERANCE

    # Return the opposite result of the equality comparison
    def __ne__(self, other):
        result = self.__eq__(other)

        if result is NotImplemented:
            return NotImplemented

        return not result

    # Check if this temperature is lower than another temperature
    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() < other.to_celsius() - self.TOLERANCE

    # Check if this temperature is lower than or equal to another
    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() <= other.to_celsius() + self.TOLERANCE

    # Check if this temperature is higher than another temperature
    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() > other.to_celsius() + self.TOLERANCE

    # Check if this temperature is higher than or equal to another
    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() >= other.to_celsius() - self.TOLERANCE