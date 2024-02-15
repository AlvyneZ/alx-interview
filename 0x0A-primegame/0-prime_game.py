#!/usr/bin/python3
"""
0-prime_game.py - Provides a method:
 isWinner(x, nums)
"""


def isWinner(x, nums):
    """
    Given the n's for each round of the prime game,
     this function determines who wins the most rounds

    Args:
        x (int): the number of rounds
        nums (list[int]): the n's of each round

    Returns:
        str: The overall winner (Ben or Maria)
    """
    if x <= 0:
        return None
    Maria = 0
    Ben = 0
    for round in range(x):
        count = 0
        if nums[round] > 1:
            pile = [1] * (nums[round] + 1)
            for cur in range(2, len(pile)):
                if pile[cur] == 1:
                    count += 1
                    mul = cur
                    try:
                        pile[mul * cur] = 0
                        mul += 1
                    except IndexError:
                        pass
        if (count % 2) == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return 'Maria'
    return 'Ben'


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
