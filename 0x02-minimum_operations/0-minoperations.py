#!/usr/bin/python3
"""
0-minoperations.py - Provides a function for calculating
 the minimum operations needed to get n letters using only
 'Copy All' and 'Paste', starting with one letter
"""


def minOperations(n):
    """
    Calculates the minimum 'Copy All' and 'Paste' operations
     needed to get n letters from just one

    n (int): The final number of letters needed

    Returns: the minimum operations, 0 if not possible
    """

    if type(n) != int or n <= 1:
        return 0

    prime_factors = 0

    # Make the number odd by dividing by the needed 2's
    while (n % 2) == 0 and n > 2:
        prime_factors += 2
        n = n // 2

    # Dealing with the other prime factors
    factor = 3
    while factor < n:
        while (n % factor) == 0 and factor < n:
            prime_factors += factor
            n = n // factor
        # move divisor to next odd number (simpler than prime)
        factor += 2

    prime_factors += n

    return prime_factors
