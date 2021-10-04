class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        return Cell(self.n - other.n)

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __floordiv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, r):
        return '\n'.join('*' * r for i in range(self.n // r)) + '\n' + '*' * (self.n % r)  # hard


cell_1 = Cell(31)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(30))
