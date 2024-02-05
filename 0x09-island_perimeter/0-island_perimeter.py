#!/usr/bin/python3
"""
0-island_perimeter.py - Provides a method:
 island_perimeter(grid)
"""


from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Given a grid of 1's and 0's connected horizontally and
     vertically, this method calulates the perimeter of an
     island of 1's

    Args:
        grid (List[List[int]]): the 1's and 0's

    Returns:
        int: the perimeter of the island
    """
    prm = 0
    N = len(grid)
    M = len(grid[0])
    for row in range(N):
        for col in range(M):
            if row < (N - 1):
                prm += grid[row][col] ^ grid[row + 1][col]
            if col < (M - 1):
                prm += grid[row][col] ^ grid[row][col + 1]
    for row in range(N):
        prm += grid[row][0] + grid[row][M - 1]
    for col in range(M):
        prm += grid[0][col] + grid[N - 1][col]
    return prm


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0]
    ]
    print(island_perimeter(grid))
