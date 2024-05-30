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
    trilist = []
    if n == 0:
        return trilist
    for integr in range(n):
        trilist.append([])
        trilist[integr].append(1)
        if (integr > 0):
            for r in range(1, integr):
                trilist[integr].append(trilist[integr - 1][r - 1] + trilist[integr - 1][r])
            trilist[integr].append(1)
    return trilist
