#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for p in range (0, len(matrix)):
        matrix[p] = (matrix[p]**2)
        return (matrix)
