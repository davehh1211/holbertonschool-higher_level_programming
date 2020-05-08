#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix2 = matrix.copy()
    return [list(map((lambda x: x * x), row)) for row in matrix2]
