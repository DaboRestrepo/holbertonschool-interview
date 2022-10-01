#!/usr/bin/python3
"""
This module soport a function that mesure the island perimeter.
"""


def island_perimeter(grid):
    """This func mesure the island perimeter.
    """
    add, limit = (0, 0)
    gridLen, colLen = (len(grid), len(grid[0]))

    for col in range(gridLen):
        add += sum(grid[col])
        for row in range(colLen):
            if grid[col][row]:
                if row > 0 and grid[col][row - 1] == 1:
                    limit += 1

                if col > 0 and grid[col - 1][row] == 1:
                    limit += 1
    return add * 4 - limit * 2
