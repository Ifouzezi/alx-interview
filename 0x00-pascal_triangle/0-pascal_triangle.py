#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    result = []
    if n <= 0:
        return result
    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(len(result[i - 1]) - 1):
            current_row = result[i - 1]
            row.append(result[i - 1][j] + result[i - 1][j + 1])
        row.append(1)
        result.append(row)
    return result
