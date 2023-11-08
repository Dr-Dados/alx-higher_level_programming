#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix_item = []
        for y in x:
            new_matrix_item.append(y**2)
        new_matrix.append(new_matrix_item)
    return new_matrix
