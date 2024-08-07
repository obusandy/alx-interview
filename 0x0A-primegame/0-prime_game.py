#!/usr/bin/python3
""" Prime game module """

def isWinner(x, nums):
    """
    Function that determines the
    winner of the prime game
    The player that cannot make a move loses the game.
    Return: Winner
    """
    if not nums or x < 1:
        return None
    high_fig = max(nums)

    figrs_filtr = [True for _ in range(max(high_fig + 1, 2))]
    for intg in range(2, int(pow(high_fig, 0.5)) + 1):
        if not figrs_filtr[intg]:
            continue
        for k in range(intg * intg, high_fig + 1, intg):
            figrs_filtr[k] = False
    figrs_filtr[0] = figrs_filtr[1] = False
    primeInt = 0
    for intg in range(len(figrs_filtr)):
        if figrs_filtr[intg]:
            primeInt += 1
        figrs_filtr[intg] = primeInt
    maria_Wns = 0
    for i in nums:
        maria_Wns += figrs_filtr[i] % 2 == 1
    if maria_Wns * 2 == len(nums):
        return None
    if maria_Wns * 2 > len(nums):
        return "Maria"
    return "Ben"