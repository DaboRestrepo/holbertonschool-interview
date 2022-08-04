#!/usr/bin/python3
"""
This modulo support the
function to unlock the boxes.
"""


def canUnlockAll(boxes):
    """
    This function has to find the boxes key.
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False
    for i in range(1, len(boxes) - 1):
        checking = False
        for j in range(len(boxes)):
            checking = i in boxes[j] and i != j
            if checking:
                break
        if checking is False:
            return checking
    return True
