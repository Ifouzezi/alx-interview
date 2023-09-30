#!/usr/bin/env python3
#!/usr/bin/python3
"""
Defines a function that returns a list of lists of integers
representing Pascal's triangle of n rows
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first two rows
    triangle = [[1], [1, 1]]

    # Generate the remaining rows of Pascal's triangle
    for i in range(2, n):
        previous_row = triangle[-1]
        new_row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            new_row.append(previous_row[j - 1] + previous_row[j])
        new_row.append(1)  # The last element of each row is always 1
        triangle.append(new_row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
