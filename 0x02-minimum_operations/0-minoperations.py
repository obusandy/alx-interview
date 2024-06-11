#!/usr/bin/python3
"""
This script contains a method to calculate the fewest number of
operations needed to achieve a specific no. of 'H'
xters in a text file
"""


def minOperations(nos):
    """Params:
    - n (interger): The target no. of 'H' xters.

    Returns:
    - int: The minimum no of operations needed to achieve exactly 'n' xters.
      If nos is impossible to achieve, return 0.
    """
    if nos <= 1:
        return 0

    iinterger = 2
    kount = 0

    while iinterger <= nos:
        if nos % iinterger == 0:
            kount += iinterger
            nos /= iinterger
        else:
            iinterger += 1

    return kount


if __name__ == '__main__':
    nos = 4
    print("Min # of operations to reach {} characters: {}"
          .format(nos, minOperations(nos)))

    nos = 12
    print("Min # of operations to reach {} characters: {}"
          .format(nos, minOperations(nos)))
