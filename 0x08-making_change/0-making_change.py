#!/usr/bin/python3
"""
This module returns the fewest no of coins
needed to meet a given amount total
Return: fewest no of coins needed to meet total
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins
    needed to meet the given amount.
    Params:
    coins (list): A list of the coin denominations available.
    total (int): The total amount to be made
    with the fewest no of coins
    Returns: the fewest number of coins needed
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    indx, noofcoins = (0, 0)
    cp_ttl = total
    len_c = len(noofcoins)

    while(indx < len_c and cp_ttl > 0):
        if (cp_ttl - coins[indx]) >= 0:
            cp_ttl -= coins[indx]
            ncoins += 1
        else:
            indx += 1

    isposs = cp_ttl > 0 and noofcoins > 0
    return -1 if isposs or noofcoins == 0 else noofcoins