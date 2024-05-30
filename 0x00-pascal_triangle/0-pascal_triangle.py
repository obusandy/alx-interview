#!/usr/bin/python3
''' returns a list of lists of integers'''

def pascal_triangle(n):
    '''
    Pascal's triangle
    Argumentss:
      n (interger): no of rows of the triangle
    Returns:
      List of lists of intgs rep the Pascal’s tri.
    '''
    trianglelist = []
    if n == 0:
        return trianglelist
    for integr in range(n):
        trianglelist.append([])
        trianglelist[integr].append(1)
        if (integr > 0):
            for r in range(1, integr):
                trianglelist[integr].append(trianglelist[integr - 1][r - 1] + trianglelist[integr - 1][r])
            trianglelist[integr].append(1)
    return trianglelist
