#!/usr/bin/python3
"""
0-making_change.py - Provides a method:
 makeChange(coins, total)
"""


from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Given multiple infinite piles of different coin values,
    this method determines the fewest number of coins needed to meet
    a given total

    Args:
        coins (List[int]): the values of coins in each pile
        total (int): the amount to be gotten

    Returns:
        int: the fewest number of coins or -1 if impossible
    """
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin

    if total != 0:
        return -1
    return count


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
