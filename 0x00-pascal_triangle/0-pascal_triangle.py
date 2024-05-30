#!/usr/bin/python3
''' returns a list of lists of integers '''

def pascal_triangle(n):
    '''
    Pascal's triangle
    Argumentss:
      n (interger): no of rows of the triangle
    Returns:
      List of lists of intgs rep the Pascal’s tri
    '''
    tril = []
    if n == 0:
        return tril
    for intgr in range(n):
        tril.append([])
        tril[intgr].append(1)
        if (intgr > 0):
            for r in range(1, intgr):
                tril[intgr].append(tril[intgr - 1][r - 1] + tril[intgr - 1][r])
            tril[intgr].append(1)
    return tril
