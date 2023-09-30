#!/usr/bin/env python3
#!/usr/bin/python3
"""
Defines a function that returns a list of lists of integers
representing Pascal's triangle of n rows
"""
def pascal_triangle(num_rows):
    """
    Creates a list of lists of integers representing Pascal's triangle
    parameters:
        num_rows [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if type(num_rows) is not int:
        raise TypeError("num_rows must be an integer")
    triangle = []
    if num_rows <= 0:
        return triangle
