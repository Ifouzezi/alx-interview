#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for current_box in range(1, len(boxes) - 1):
        found_key = False
        for box in range(len(boxes)):
            found_key = (current_box in boxes[box] and current_box != box)
            if found_key:
                break
        if not found_key:
            return found_key
    return True
