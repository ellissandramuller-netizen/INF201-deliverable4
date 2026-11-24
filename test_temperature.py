
class Temperature:

    def __init__(self, value, unit):

        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Unit is not valid")

        self.value = value
        self.unit = unit
        