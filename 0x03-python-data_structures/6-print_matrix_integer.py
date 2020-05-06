#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        print(' '.join("{:d}".format(elem) for elem in row))
