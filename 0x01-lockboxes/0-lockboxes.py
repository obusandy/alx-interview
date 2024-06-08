#!/usr/bin/python3
"""Module to determine if all boxes can be unlocked"""

def canUnlockAll(boxes):
    """
     Determines if all boxes
     can be unlocked.
     Each box contains keys to other boxes.
    """
    unlocked_boxes = [0]
    for boxIndex, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes and key != boxIndex:
                unlocked_boxes.append(key)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False


def canUnlockAll2(boxes):
    """
     Determines if all boxes can be unlocked.
     Each box contains keys to other boxes.
    Returns:
        bool: True if all boxes can be unlocked
    """
    unlocked_boxes = set()
    for boxIndex, box in enumerate(boxes):
        if len(box) == 0 or boxIndex == 0:
            unlocked_boxes.add(boxIndex)
        for key in box:
            if key < len(boxes) and key != boxIndex:
                unlocked_boxes.add(key)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
