#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    square = []
    for row in new_matrix:
        square.append(list(map(lambda x: x * x, row)))
    return square
