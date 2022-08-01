#!/usr/bin/python3
"""
Define a funct that returns a list of lists of integers
representing the Pascal triangle of n
"""


def pascal_triangle(n):
    """
    This function creates a list of integers
    representing the Pascal's triangle of n.
    """
    if type(n) is not int:
        raise TypeError('n must be an integer')
    triangle = []
    if n <= 0:
        return triangle
    prev = [1]
    for inx in range(n):
        list = []
        if inx == 0:
            list = [1]
        else:
            for i in range(inx + 1):
                if i == 0:
                    list.append(0 + prev[i])
                elif i == (inx):
                    list.append(prev[i - 1] + 0)
                else:
                    list.append(prev[i - 1] + prev[i])
        prev = list
        triangle.append(list)
    return triangle
