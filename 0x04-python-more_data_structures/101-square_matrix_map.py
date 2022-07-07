#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    new_matrix = matrix.copy()
    return list(map(lambda row: list(map(lambda x: x * x, row)), new_matrix))
