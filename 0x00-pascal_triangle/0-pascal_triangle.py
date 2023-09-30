#!/usr/bin/env python3
#!/usr/bin/python3
"""
Defines a function that returns a list of lists of integers
representing Pascal's triangle of n rows
"""
def pascal_triangle(num_rows):
    if type(num_rows) is not int:
        raise TypeError("num_rows must be an integer")
    
    triangle = []
    
    if num_rows <= 0:
        return triangle
    
    for i in range(num_rows):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    
    return triangle

