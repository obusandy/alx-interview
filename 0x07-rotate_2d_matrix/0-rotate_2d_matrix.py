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
    for indx in range(int(len(matrix) / 2)):
        for i in range(indx, (len(matrix) - indx - 1)):
            trix = (len(matrix) - 1 - i)
            tmprary = matrix[indx][i]
            matrix[indx][i] = matrix[trix][indx]
            matrix[trix][indx] = matrix[(len(matrix) - indx - 1)][trix]
            matrix[(len(matrix) - indx - 1)][trix] = matrix[i][(len(matrix) - indx - 1)]
            matrix[i][(len(matrix) - indx - 1)] = tmprary
