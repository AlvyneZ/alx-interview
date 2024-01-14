#!/usr/bin/python3
"""
0-nqueens.py - Provides a solution for the N-queen problem
"""


from typing import List
from copy import deepcopy


class Board:
    """Holds information about the board
    """
    def __init__(self, N: int) -> None:
        """Initializes an empty board of size N

        Args:
            N (int): board size
        """
        self.N: int = N
        self.queenCol: List[int] = [-1] * N

    def __repr__(self) -> str:
        """Gives the official representation of the board
         allowing printing of queen coordinates

        Returns:
            str: queen coordinates
        """
        locations = []
        for row in range(self.N):
            locations.append([row, self.queenCol[row]])
        return str(locations)

    def isGood(self, row: int, col: int) -> bool:
        """Checks if a location is good for placing a queen
         assuming no queens are placed in the following rows

        Args:
            row (int): row to place
            col (int): column to place

        Returns:
            bool: True if it is OK, False otherwise
        """
        if (col in self.queenCol[:row]):
            return False
        jn = col - 1
        for i in reversed(range(row)):
            if jn < 0:
                break
            if self.queenCol[i] == jn:
                return False
            jn -= 1
        jp = col + 1
        for i in reversed(range(row)):
            if jp >= self.N:
                break
            if self.queenCol[i] == jp:
                return False
            jp += 1
        return True


def solve(N: int) -> List[Board]:
    """Gets all possible N-queen solutions for
     an N by N grid

    Args:
        N (int): size of the grid

    Returns:
        List[Board]: all possible solutions
    """
    validBoards: List[Board] = []
    board = Board(N)

    def solveRow(b: Board, row: int) -> None:
        """Solves for a certain grid row recursively

        Args:
            b (Board): current state of the row only
             considering rows above the current row to
             be solved
            row (int): current row to be solved
        """
        for col in range(N):
            if b.isGood(row, col):
                b.queenCol[row] = col
                if row == N - 1:
                    validBoards.append(deepcopy(b))
                    return
                solveRow(b, row + 1)

    solveRow(board, 0)
    return validBoards


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    try:
        N = int(N)
    except Exception as e:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    boards = solve(N)
    for board in boards:
        print(board)
