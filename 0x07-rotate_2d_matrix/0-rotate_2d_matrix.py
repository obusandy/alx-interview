#!/usr/bin/python3
"""
an n x n 2D matrix, rotate it 90dgr
The matrix must be edited in-place.
Returns: None
The function modifies the matrix in place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the 2d
    Args:
        matrix: The 2D matrix to be rotated.
    """
    nw = len(matrix)
    # Create a cpy
    tmpr = [r.copy() for r in matrix]
    # Rotate
    for i in range(nw):
        for j in range(nw):
            matrix[j][i] = tmpr[nw - i - 1][j]
