class Fraction:
    def __init__(self, numerator, denominator):
        # Check that the numerator and denominator are integers
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Numerator and denominator must be integers.")

        # Check that the denominator is positive
        if denominator <= 0:
            raise ValueError("Denominator must be greater than zero.")

        
        self.numerator = numerator
        self.denominator = denominator

    # Check if two  fractions are equal
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator

    # Check if two fractions are not equal
    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self == other

    # Check if a fraction is less than another
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator < self.denominator * other.numerator)

    # Check if a fraction is less than or equal to another
    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator <= self.denominator * other.numerator)

    # Check if a fraction is greater than another
    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator > self.denominator * other.numerator)

    # Check if a fraction is greater than or equal to another
    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator >= self.denominator * other.numerator)

    # return a readable string representation
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # return a representation of the fraction object
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    # Add two fractions
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = (self.numerator * other.denominator
                     + other.numerator * self.denominator)
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # Multiply two fractions
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)




    
