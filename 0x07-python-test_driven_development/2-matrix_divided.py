#!/usr/bin/python3
"""division of each element of a matrix.
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Arguments:
        matrix {list} -- It is a matrix with n number of rows
        div {int or float} -- [number to be divided]

    Raises:
        TypeError: matrix must be a matrix (list of lists) \
            of integers/floats.
        It raises when the matrix is none or its rows are \
        different to each other.
        TypeError: div must be a number, when the div is a string.
        ZeroDivisionError: division by zero, when div is zero

    Returns:
    int or float -- the result of the division of each \
        element of the matrix with div
    """
    errormsn = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) is 0:
        raise TypeError(errormsn)

    for row in matrix:
        if not row:
            raise TypeError(errormsn)
        if len(row) is 0:
            raise TypeError(errormsn)
        for column in row:
            if column is 0:
                ZeroDivisionError("division by zero")
            elif type(column) not in (int, float):
                raise TypeError(errormsn)
    length = len(matrix[0])
    if any(len(i) is not length for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    oper = [[round(column/div, 2) for column in row] for row in matrix]
    return oper
