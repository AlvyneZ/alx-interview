#!/usr/bin/python3
"""
0-rotate_2d_matrix.py - Provides a method:
 rotate_2d_matrix()
"""


def rotate_2d_matrix(m):
    """Rotates a matrix 90 degrees clockwise in place

    Args:
        m (List[List[int]]): n*n matrix to be rotated
    """
    n = len(m)
    if n <= 1:
        return
    for row in range(n // 2):
        x_r = (n - 1) - row
        for col in range(row, x_r):
            x_c = (n - 1) - col
            (m[row][col], m[col][x_r]) = (m[col][x_r], m[row][col])
            (m[row][col], m[x_r][x_c]) = (m[x_r][x_c], m[row][col])
            (m[row][col], m[x_c][row]) = (m[x_c][row], m[row][col])


if __name__ == "__main__":
    matrix = [[0]]
    rotate_2d_matrix(matrix)
    print(matrix)

    matrix = [[1, 2],
              [3, 4]]
    rotate_2d_matrix(matrix)
    print(matrix)

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)

    matrix = [[11, 12, 13, 14],
              [15, 16, 17, 18],
              [19, 20, 21, 22],
              [23, 24, 25, 26]]
    rotate_2d_matrix(matrix)
    print(matrix)

    matrix = [[31, 32, 33, 34, 35],
              [36, 37, 38, 39, 40],
              [41, 42, 43, 44, 45],
              [46, 47, 48, 49, 50],
              [51, 52, 53, 54, 55]]
    rotate_2d_matrix(matrix)
    print(matrix)
