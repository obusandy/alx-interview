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
    for rw_indx in range(grid_hgt):
        for colmn in range(len(grid[rw_indx])):
            if grid[rw_indx][colmn] == 1:
                if rw_indx - 1 < 0 or grid[rw_indx - 1][colmn] == 0:
                    ttl_perimeter += 1
                if colmn - 1 < 0 or grid[rw_indx][colmn - 1] == 0:
                    ttl_perimeter += 1
                if colmn + 1 >= len(grid[rw_indx]) or grid[rw_indx][colmn + 1] == 0:
                    ttl_perimeter += 1
                if rw_indx + 1 >= grid_hgt or grid[rw_indx + 1][colmn] == 0:
                    ttl_perimeter += 1
    return ttl_perimeter
