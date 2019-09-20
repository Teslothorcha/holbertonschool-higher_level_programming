#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    copy = list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
    return(copy)
