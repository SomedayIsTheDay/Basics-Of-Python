from cmath import sqrt


# good start
class ComplexNumber:
    def __init__(self, complex_1, complex_2):
        self.complex_1 = complex_1
        self.complex_2 = complex_2
        self.j = sqrt(-1)

    def __add__(self, other):
        return (self.complex_1 + other.complex_1) + (self.complex_2 + other.complex_2) * self.j

    def __mul__(self, other):
        return (self.complex_1 * self.complex_2 - other.complex_1 * other.complex_2)\
             + (self.complex_1 * other.complex_2 + self.complex_2 * other.complex_1) * self.j


cn_1 = ComplexNumber(5, 6)
cn_2 = ComplexNumber(10, 3)
print(cn_1 * cn_2)
print(cn_1 + cn_2)
