#!/usr/bin/python3
"""
below is a function def island_perimeter(grid)that:
returns: the perimeter of the island described
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island
    Args:
        grid: the grid of the island

    return: the perimeter of the island
    """
    ttl_perimeter = 0
    grid_hgt = len(grid)
    for rw in range(grid_hgt):
        for colmn in range(len(grid[rw])):
            if grid[rw][colmn] == 1:
                if rw - 1 < 0 or grid[rw - 1][colmn] == 0:
                    ttl_perimeter += 1
                if colmn - 1 < 0 or grid[rw][colmn - 1] == 0:
                    ttl_perimeter += 1
                if colmn + 1 >= len(grid[rw]) or grid[rw][colmn + 1] == 0:
                    ttl_perimeter += 1
                if rw + 1 >= grid_hgt or grid[rw + 1][colmn] == 0:
                    ttl_perimeter += 1
    return ttl_perimeter
