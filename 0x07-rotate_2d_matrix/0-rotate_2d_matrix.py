#!/usr/bin/python3
"""
an n x n 2D matrix, rotate it 90 degrees clockwise
The matrix must be edited in-place.
Returns: None: The function modifies the matrix in place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the 2d
    Args:
        matrix: The 2D matrix to be rotated.
    """
    tmprary = []
    for indx in matrix:
        tmprary.append(indx.copy())
    new = len(matrix)
    for indx in range(new):
        for n in range(new):
            matrix[n][indx] = tmprary[new - indx - 1][n]
