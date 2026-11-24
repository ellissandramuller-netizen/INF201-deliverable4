
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

        self.value = value
        self.unit = unit