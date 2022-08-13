#!/usr/bin/python3
"""
This module soport the function minOperations.
"""


def minOperations(n):
    """
    Mesure the min operations needed to get
    n times H in the file.
    sum: fewest number of operations.
    """
    if n <= 1:
        return 0
    sum = 0
    idx = 2
    while (idx < n + 1):
        while n % idx == 0:
            sum += idx
            n /= idx
        idx += 1
    return sum
