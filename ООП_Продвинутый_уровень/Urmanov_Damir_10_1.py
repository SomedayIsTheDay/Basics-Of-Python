from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t | \t'.join(str(el) for el in i) for i in self.matrix)

    def __add__(self, other):
        return Matrix(map(sum, zip_longest(i, v, fillvalue=0))
                      for i, v in zip_longest(self.matrix, other.matrix, fillvalue=[]))


mat_one = [[23, 4, 54], [1, 6, 2], [1, 2]]
mat_two = [[55, 11, 97], [6, 6, 6], [53, 232, 1], [19, 6]]
mat_thr = [[105, 231, 124], [5, 222, 123123], [234, 567, 134], [754, 555]]

matrix_1 = Matrix(mat_one)
matrix_2 = Matrix(mat_two)
matrix_3 = Matrix(mat_thr)
print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2 + matrix_3)
