#!/usr/bin/python3
"""
0-pascal_triangle.py - Provides a function for
 generating pascal's triangle
"""


def pascal_triangle(n):
    """
    Generates the Pascal's triangle of n
    
    n (int): Size of the triangle

    Returns: an empty list if n <= 0, triangle list otherwise
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(0, (n - 1)):
        # Note: i points to previous row
        row = [1]
        for j in range(0, i):
            row.append(triangle[i][j] + triangle[i][j + 1])

        row.append(1)
        triangle.append(row)

    return triangle
