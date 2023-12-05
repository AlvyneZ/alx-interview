#!/usr/bin/python3
"""
0-lockboxes.py - Provides a function for
 checking if lockboxes can be opened
"""


def canUnlockAll(boxes):
    """
    Checks if a set of boxes provided the keys contained
     can all be unlocked

    boxes (int): A list of lists of keys contained in each box

    Returns: true if the boxes can all be unlocked,
     false otherwise
    """

    if type(boxes) != list:
        return False
    unlocked = [False] * len(boxes)
    unlockedCount = 1
    unlocked[0] = True

    current = [0]
    done = 0
    while (done < len(current)) and (unlockedCount < len(boxes)):
        if type(boxes[current[done]]) != list:
            return False
        for key in boxes[current[done]]:
            if (not unlocked[key]):
                current.append(key)
                unlocked[key] = True
                unlockedCount += 1
        done += 1

    for boxState in unlocked:
        if not boxState:
            return False
    return True
